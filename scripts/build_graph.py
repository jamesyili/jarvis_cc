#!/usr/bin/env python3
"""
Graph backend for Leo's KB. Thin wrapper around graphify (https://github.com/safishamsi/graphify).

Usage:
    python scripts/build_graph.py build [--domain all|hard|soft] [--mode deep|fast]
    python scripts/build_graph.py refresh                 # incremental --update pass
    python scripts/build_graph.py stats                   # print graph statistics
    python scripts/build_graph.py show <node_id>          # node + neighbors + community
    python scripts/build_graph.py neighbors <concept>     # find and list neighbors
    python scripts/build_graph.py god-nodes [-n 20]       # top-degree concepts
    python scripts/build_graph.py orphans                 # degree-0 articles
    python scripts/build_graph.py communities             # Leiden clusters
    python scripts/build_graph.py surprising              # cross-community insights
    python scripts/build_graph.py open                    # open graph.html in browser
    python scripts/build_graph.py postprocess             # filter scaffolding + consolidate

Requires: graphifyy installed. Intended python: ~/.venvs/graphify/bin/python.
"""
import argparse
import json
import re
import subprocess
import sys
import webbrowser
from collections import Counter, defaultdict
from pathlib import Path

LEO_ROOT = Path(__file__).parent.parent
KB_ROOT = LEO_ROOT / "kb"
GRAPH_DIR = KB_ROOT / ".kb" / "graph"
GRAPH_JSON = GRAPH_DIR / "graph.json"
GRAPH_HTML = GRAPH_DIR / "graph.html"
COMMUNITIES_JSON = GRAPH_DIR / "communities.json"

MODEL = "claude-sonnet-4-6"

# Post-processing filters — scaffolding and explicit excludes
EXCLUDE_FILENAMES = {"_index.md", "_plan.md"}
EXCLUDE_DIR_SEGMENTS = {"do_not_index_sources"}


def _ensure_graphify():
    """Verify graphify library is importable. Fail loud with install hint."""
    try:
        import graphify  # noqa: F401
    except ImportError:
        print(
            "ERROR: graphify not installed. Run:\n"
            "  python3 -m venv ~/.venvs/graphify\n"
            "  ~/.venvs/graphify/bin/pip install graphifyy\n"
            "  ~/.venvs/graphify/bin/graphify install\n"
            "Then run this script with: ~/.venvs/graphify/bin/python scripts/build_graph.py ...",
            file=sys.stderr,
        )
        sys.exit(2)


# ---------------------------------------------------------------------------
# Build — subprocess-invoke the graphify Claude Code skill
# ---------------------------------------------------------------------------

def build(domain: str = "all", mode: str = "deep", update: bool = False) -> Path:
    """Run graphify on kb/ via claude -p subprocess. Returns path to graph.json."""
    _ensure_graphify()

    if domain == "all":
        target = KB_ROOT
    elif domain in ("hard", "soft"):
        target = KB_ROOT / domain
    else:
        raise ValueError(f"unknown domain: {domain}")

    # Skill runs from CWD and writes to CWD/graphify-out/. Use a scratch dir
    # outside Leo's tree so intermediate files don't pollute git.
    scratch = Path("/tmp") / f"graphify-leo-{domain}"
    scratch.mkdir(parents=True, exist_ok=True)

    flags = f"--mode {mode}"
    if update:
        flags += " --update"

    system_prompt = (
        "CRITICAL INSTRUCTION: When running the graphify skill, if you encounter the "
        "Step 2 '>200 files' or '>2,000,000 words' warning and subdirectory selection "
        "prompt, do NOT ask the user for subfolder selection. Proceed immediately on "
        "the full corpus as provided. The user has pre-approved running on the full "
        "corpus. Skip the interactive prompt and continue directly to Step 3."
    )

    cmd = [
        "claude", "-p", f"/graphify {target} {flags}",
        "--append-system-prompt", system_prompt,
        "--permission-mode", "bypassPermissions",
        "--add-dir", str(target),
        "--model", "sonnet",
        "--fallback-model", "haiku",
        "--output-format", "text",
    ]
    print(f"Running: {' '.join(cmd)}")
    print(f"CWD: {scratch}")
    print("This may take 1-3 hours for the full corpus.")

    result = subprocess.run(cmd, cwd=scratch)
    if result.returncode != 0:
        print(f"ERROR: graphify exited {result.returncode}", file=sys.stderr)
        sys.exit(result.returncode)

    # Move artifacts into kb/.kb/graph/
    GRAPH_DIR.mkdir(parents=True, exist_ok=True)
    src_out = scratch / "graphify-out"
    for name in ("graph.json", "graph.html", "GRAPH_REPORT.md", "manifest.json", "cost.json"):
        src = src_out / name
        if src.exists():
            (GRAPH_DIR / name).write_bytes(src.read_bytes())

    # Run post-processing automatically
    postprocess()
    return GRAPH_JSON


# ---------------------------------------------------------------------------
# Post-processing — filter scaffolding + cross-chunk consolidation
# ---------------------------------------------------------------------------

def _is_excluded_source(source_file: str) -> bool:
    """True if a node's source_file should be dropped from the graph."""
    if not source_file:
        return False
    p = Path(source_file)
    if p.name in EXCLUDE_FILENAMES:
        return True
    if any(seg in EXCLUDE_DIR_SEGMENTS for seg in p.parts):
        return True
    return False


def _normalize_label(label: str) -> str:
    """Canonical key for cross-chunk dedup. Lowercase, strip parens/punct."""
    s = label.lower()
    s = re.sub(r"\([^)]*\)", "", s)           # remove parentheticals
    s = re.sub(r"[^a-z0-9]+", " ", s)          # collapse punct → space
    s = s.strip()
    # collapse duplicate whitespace
    s = re.sub(r"\s+", " ", s)
    return s


def _export_filtered_html() -> None:
    """Export an HTML viz of the high-degree subgraph.

    graphify.export.to_html caps at 5000 nodes, so we filter to degree >= 2
    (~4.5K nodes on the full corpus). String fields with None values crash the
    template — coerce to empty strings first.
    """
    try:
        from graphify.export import to_html, MAX_NODES_FOR_VIZ
        from networkx.readwrite import json_graph
    except ImportError:
        return

    data = json.loads(GRAPH_JSON.read_text())
    string_fields = ("source_location", "source_url", "author", "contributor", "captured_at", "source_file", "label")
    for n in data["nodes"]:
        for k in string_fields:
            if n.get(k) is None:
                n[k] = ""
    for l in data["links"]:
        for k in string_fields:
            if l.get(k) is None:
                l[k] = ""

    G = json_graph.node_link_graph(data, edges="links")

    # Keep degree >= 2 until under MAX_NODES_FOR_VIZ
    cutoff = 2
    while True:
        keep = [n for n in G.nodes() if G.degree(n) >= cutoff]
        if len(keep) <= MAX_NODES_FOR_VIZ:
            break
        cutoff += 1

    if not keep:
        print(f"  HTML export: skipped (no nodes with degree >= {cutoff})")
        return

    H = G.subgraph(keep).copy()
    comms: dict = {}
    keep_set = set(keep)
    for n in data["nodes"]:
        if n["id"] not in keep_set:
            continue
        c = n.get("community")
        if c is None:
            continue
        comms.setdefault(c, []).append(n["id"])

    try:
        to_html(H, comms, str(GRAPH_HTML))
        size_kb = GRAPH_HTML.stat().st_size / 1024
        print(f"  HTML export: {H.number_of_nodes()} nodes (degree >= {cutoff}), {size_kb:.0f} KB")
    except Exception as e:
        print(f"  HTML export failed: {e}")


def postprocess() -> dict:
    """Filter scaffolding nodes and consolidate cross-chunk duplicates.

    Returns a stats dict describing what was changed.
    """
    if not GRAPH_JSON.exists():
        print(f"ERROR: {GRAPH_JSON} not found. Run build first.", file=sys.stderr)
        sys.exit(1)

    data = json.loads(GRAPH_JSON.read_text())
    nodes = data.get("nodes", [])
    links = data.get("links", [])
    hyperedges = data.get("hyperedges", [])

    n_before = len(nodes)
    e_before = len(links)

    # Pass 1: drop scaffolding / excluded sources
    kept_ids = {
        n["id"]
        for n in nodes
        if not _is_excluded_source(n.get("source_file", ""))
    }
    dropped_scaffolding = n_before - len(kept_ids)

    # Pass 2: cross-chunk consolidation. Group nodes by normalized label.
    # Elect the node with the highest degree (most edges) as the canonical ID,
    # then rewrite every reference to the others to point at the canonical.
    by_norm = defaultdict(list)
    for n in nodes:
        if n["id"] not in kept_ids:
            continue
        key = _normalize_label(n.get("label", n["id"]))
        if key:
            by_norm[key].append(n)

    # Compute degree from links (ignore already-dropped nodes)
    deg = Counter()
    for link in links:
        s, t = link.get("source"), link.get("target")
        if s in kept_ids and t in kept_ids:
            deg[s] += 1
            deg[t] += 1

    id_rewrite: dict[str, str] = {}  # old_id -> canonical_id
    merges = 0
    for key, group in by_norm.items():
        if len(group) < 2:
            continue
        # Pick the one with the highest degree; tiebreak on shortest id
        group.sort(key=lambda n: (-deg.get(n["id"], 0), len(n["id"])))
        canonical = group[0]["id"]
        for n in group[1:]:
            if n["id"] != canonical:
                id_rewrite[n["id"]] = canonical
                merges += 1

    # Apply rewrites: rebuild nodes list and links list
    final_nodes = []
    seen = set()
    for n in nodes:
        nid = n["id"]
        if nid not in kept_ids:
            continue
        if nid in id_rewrite:
            continue  # merged away
        if nid in seen:
            continue
        seen.add(nid)
        final_nodes.append(n)

    final_links = []
    for link in links:
        s = link.get("source")
        t = link.get("target")
        if s not in kept_ids or t not in kept_ids:
            continue
        s = id_rewrite.get(s, s)
        t = id_rewrite.get(t, t)
        if s == t:
            continue  # self-loop after merge
        final_links.append({**link, "source": s, "target": t})

    # Deduplicate links on (source, target, relation)
    link_keys = set()
    deduped_links = []
    for link in final_links:
        key = (link["source"], link["target"], link.get("relation", ""))
        if key in link_keys:
            continue
        link_keys.add(key)
        deduped_links.append(link)

    # Rewrite hyperedge node references too
    final_hyperedges = []
    for h in hyperedges:
        new_nodes = [id_rewrite.get(n, n) for n in h.get("nodes", [])]
        new_nodes = [n for n in new_nodes if n in {fn["id"] for fn in final_nodes}]
        if len(new_nodes) >= 2:
            final_hyperedges.append({**h, "nodes": new_nodes})

    data["nodes"] = final_nodes
    data["links"] = deduped_links
    data["hyperedges"] = final_hyperedges

    GRAPH_JSON.write_text(json.dumps(data, indent=2))

    # Emit communities.json for the committed artifact set
    communities_by_id = defaultdict(list)
    for n in final_nodes:
        c = n.get("community")
        if c is not None:
            communities_by_id[c].append(n["id"])
    COMMUNITIES_JSON.write_text(
        json.dumps({str(k): v for k, v in communities_by_id.items()}, indent=2)
    )

    stats = {
        "nodes_before": n_before,
        "nodes_after": len(final_nodes),
        "edges_before": e_before,
        "edges_after": len(deduped_links),
        "dropped_scaffolding": dropped_scaffolding,
        "merged_duplicates": merges,
        "communities": len(communities_by_id),
        "hyperedges": len(final_hyperedges),
    }
    print("Post-processing stats:")
    for k, v in stats.items():
        print(f"  {k}: {v}")

    # Regenerate the HTML viz (filtered to stay under graphify's 5000-node cap)
    _export_filtered_html()
    return stats


# ---------------------------------------------------------------------------
# Query helpers — used by build_graph CLI and Phase 2-4 consumers
# ---------------------------------------------------------------------------

def load_graph():
    """Load graph.json into a NetworkX graph. Lazy-imports networkx."""
    _ensure_graphify()
    import networkx as nx
    from networkx.readwrite import json_graph
    if not GRAPH_JSON.exists():
        raise FileNotFoundError(f"{GRAPH_JSON} not found — run `build_graph.py build` first")
    data = json.loads(GRAPH_JSON.read_text())
    return json_graph.node_link_graph(data, edges="links")


def load_raw():
    """Return the raw graph.json dict (no NetworkX reconstruction)."""
    return json.loads(GRAPH_JSON.read_text())


def neighbors(node_id_or_label: str, depth: int = 1, min_weight: float = 0.0):
    """Return direct or depth-limited neighbors of a node.

    Accepts either a node id or a human-readable label (case-insensitive match).
    """
    G = load_graph()
    target = _resolve_node(G, node_id_or_label)
    if target is None:
        return []
    if depth == 1:
        out = []
        for nbr in G.neighbors(target):
            edata = G.get_edge_data(target, nbr) or {}
            if edata.get("weight", 1.0) < min_weight:
                continue
            out.append({
                "id": nbr,
                "label": G.nodes[nbr].get("label", nbr),
                "relation": edata.get("relation", ""),
                "confidence": edata.get("confidence", ""),
                "source_file": G.nodes[nbr].get("source_file", ""),
            })
        return out
    # Multi-hop: BFS
    import networkx as nx
    reached = nx.single_source_shortest_path_length(G, target, cutoff=depth)
    return [
        {"id": n, "label": G.nodes[n].get("label", n), "distance": d}
        for n, d in reached.items()
        if n != target
    ]


def _resolve_node(G, query: str):
    """Find a node by id, label, or case-insensitive label substring."""
    if query in G.nodes:
        return query
    q = query.lower()
    # Exact label match
    for nid, d in G.nodes(data=True):
        if d.get("label", "").lower() == q:
            return nid
    # Substring label match, prefer highest degree
    matches = [
        (nid, G.degree(nid))
        for nid, d in G.nodes(data=True)
        if q in d.get("label", "").lower()
    ]
    if matches:
        matches.sort(key=lambda x: -x[1])
        return matches[0][0]
    return None


def god_nodes(top_n: int = 20):
    """Top-degree nodes. Delegates to graphify.analyze if available."""
    _ensure_graphify()
    try:
        from graphify.analyze import god_nodes as _g
        return _g(load_graph(), top_n=top_n)
    except Exception:
        G = load_graph()
        ranked = sorted(G.degree, key=lambda x: -x[1])[:top_n]
        return [
            {"id": nid, "label": G.nodes[nid].get("label", nid), "degree": d}
            for nid, d in ranked
        ]


def communities():
    """Return Leiden clusters from committed communities.json."""
    if COMMUNITIES_JSON.exists():
        return json.loads(COMMUNITIES_JSON.read_text())
    # Fallback: reconstruct from node community field
    data = load_raw()
    by_id = defaultdict(list)
    for n in data.get("nodes", []):
        c = n.get("community")
        if c is not None:
            by_id[str(c)].append(n["id"])
    return dict(by_id)


def orphans():
    """Article-level orphans: nodes with degree 0."""
    G = load_graph()
    return [
        {"id": nid, "label": G.nodes[nid].get("label", nid), "source_file": G.nodes[nid].get("source_file", "")}
        for nid, d in G.degree
        if d == 0
    ]


def backlinks(node_id_or_label: str):
    """Nodes that point TO the given node."""
    G = load_graph()
    target = _resolve_node(G, node_id_or_label)
    if target is None:
        return []
    # For an undirected graph this is identical to neighbors()
    return neighbors(target)


def sources_for_concept(concept_label: str):
    """Given a concept label, return the set of raw article paths that mention it."""
    G = load_graph()
    target = _resolve_node(G, concept_label)
    if target is None:
        return []
    sources = set()
    nd = G.nodes[target]
    if nd.get("source_file"):
        sources.add(nd["source_file"])
    for nbr in G.neighbors(target):
        sf = G.nodes[nbr].get("source_file")
        if sf:
            sources.add(sf)
    return sorted(sources)


def surprising_connections(top_n: int = 10):
    """Cross-community high-confidence edges. Uses graphify.analyze."""
    _ensure_graphify()
    from graphify.analyze import surprising_connections as _s
    G = load_graph()
    comms_raw = communities()
    comms = {int(k): v for k, v in comms_raw.items()}
    return _s(G, comms, top_n=top_n)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _cmd_stats(args):
    G = load_graph()
    degs = sorted((d for _, d in G.degree), reverse=True)
    n = G.number_of_nodes()
    e = G.number_of_edges()
    data = load_raw()
    orphan_count = sum(1 for d in degs if d == 0)
    print(f"Nodes:       {n}")
    print(f"Edges:       {e}")
    print(f"Hyperedges:  {len(data.get('hyperedges', []))}")
    print(f"Communities: {len(communities())}")
    print(f"Orphans:     {orphan_count}")
    print(f"Max degree:  {degs[0] if degs else 0}")
    print(f"Median deg:  {degs[n // 2] if n else 0}")
    print(f"graph.json:  {GRAPH_JSON.stat().st_size / 1024:.1f} KB")


def _cmd_show(args):
    G = load_graph()
    target = _resolve_node(G, args.node)
    if target is None:
        print(f"No node matching: {args.node}")
        sys.exit(1)
    nd = G.nodes[target]
    print(f"Node:       {target}")
    print(f"Label:      {nd.get('label', '')}")
    print(f"Source:     {nd.get('source_file', '')}")
    print(f"Community:  {nd.get('community', '')}")
    print(f"Degree:     {G.degree(target)}")
    print(f"\nNeighbors ({G.degree(target)}):")
    for nbr_info in neighbors(target):
        rel = nbr_info.get("relation", "")
        print(f"  → [{rel}] {nbr_info['label']}  ({nbr_info.get('source_file', '')})")


def _cmd_neighbors(args):
    for nbr_info in neighbors(args.concept, depth=args.depth):
        print(f"  {nbr_info.get('label', nbr_info.get('id'))}")


def _cmd_god_nodes(args):
    for g in god_nodes(top_n=args.n):
        deg = g.get("edges", g.get("degree", g.get("centrality", "?")))
        print(f"  [{deg}] {g.get('label', g.get('id', ''))}")


def _cmd_orphans(args):
    for o in orphans():
        print(f"  {o['label']}  ({o['source_file']})")


def _cmd_communities(args):
    comms = communities()
    for cid, members in sorted(comms.items(), key=lambda x: -len(x[1]))[: args.n]:
        print(f"\nCommunity {cid} ({len(members)} nodes):")
        for m in members[:6]:
            print(f"  • {m}")


def _cmd_surprising(args):
    for s in surprising_connections(top_n=args.n):
        src = s.get("source", s.get("from", "?"))
        tgt = s.get("target", s.get("to", "?"))
        rel = s.get("relation", "")
        print(f"  {src} → {tgt}  [{rel}]")


def _cmd_open(args):
    if not GRAPH_HTML.exists():
        print(f"{GRAPH_HTML} not found. Run build first.", file=sys.stderr)
        sys.exit(1)
    webbrowser.open(f"file://{GRAPH_HTML}")


def _cmd_build(args):
    build(domain=args.domain, mode=args.mode, update=args.update)


def _cmd_refresh(args):
    build(domain="all", mode="deep", update=True)


def _cmd_postprocess(args):
    postprocess()


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    sb = sub.add_parser("build", help="Build graph on full kb corpus")
    sb.add_argument("--domain", choices=["all", "hard", "soft"], default="all")
    sb.add_argument("--mode", choices=["deep", "fast"], default="deep")
    sb.add_argument("--update", action="store_true", help="Incremental --update pass")
    sb.set_defaults(func=_cmd_build)

    sr = sub.add_parser("refresh", help="Incremental refresh (--update)")
    sr.set_defaults(func=_cmd_refresh)

    ss = sub.add_parser("stats", help="Print graph statistics")
    ss.set_defaults(func=_cmd_stats)

    sh = sub.add_parser("show", help="Show a node with neighbors")
    sh.add_argument("node", help="Node id or label (case-insensitive)")
    sh.set_defaults(func=_cmd_show)

    sn = sub.add_parser("neighbors", help="List neighbors of a concept")
    sn.add_argument("concept")
    sn.add_argument("--depth", type=int, default=1)
    sn.set_defaults(func=_cmd_neighbors)

    sg = sub.add_parser("god-nodes", help="Top-degree concepts")
    sg.add_argument("-n", type=int, default=20)
    sg.set_defaults(func=_cmd_god_nodes)

    so = sub.add_parser("orphans", help="Nodes with degree 0")
    so.set_defaults(func=_cmd_orphans)

    sc = sub.add_parser("communities", help="Leiden clusters")
    sc.add_argument("-n", type=int, default=15)
    sc.set_defaults(func=_cmd_communities)

    sx = sub.add_parser("surprising", help="Cross-community insights")
    sx.add_argument("-n", type=int, default=10)
    sx.set_defaults(func=_cmd_surprising)

    sp = sub.add_parser("open", help="Open graph.html in browser")
    sp.set_defaults(func=_cmd_open)

    spp = sub.add_parser("postprocess", help="Filter scaffolding + consolidate duplicates")
    spp.set_defaults(func=_cmd_postprocess)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
