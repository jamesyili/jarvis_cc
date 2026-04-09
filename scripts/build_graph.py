#!/usr/bin/env python3
"""
Graph backend for Leo's KB. Thin wrapper around graphify (https://github.com/safishamsi/graphify).

Usage:
    python scripts/build_graph.py build [--domain all|hard|soft] [--mode deep|fast]
    python scripts/build_graph.py refresh                     # incremental --update pass
    python scripts/build_graph.py stats                       # print graph statistics
    python scripts/build_graph.py show <node_id>              # node + neighbors + community
    python scripts/build_graph.py neighbors <concept>         # find and list neighbors
    python scripts/build_graph.py god-nodes [-n 20]           # top-degree concepts (authors filtered)
    python scripts/build_graph.py god-nodes --include-people  # raw top-degree (no filter)
    python scripts/build_graph.py orphans                     # degree-0 articles
    python scripts/build_graph.py communities                 # Leiden clusters
    python scripts/build_graph.py surprising                  # cross-community insights
    python scripts/build_graph.py compute-surprising          # rebuild surprising.json from raw chunks
    python scripts/build_graph.py open                        # open graph.html in browser
    python scripts/build_graph.py postprocess                 # filter scaffolding + consolidate

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
SURPRISING_JSON = GRAPH_DIR / "surprising.json"

MODEL = "claude-sonnet-4-6"

# Post-processing filters — scaffolding and explicit excludes
EXCLUDE_FILENAMES = {"_index.md", "_plan.md"}
EXCLUDE_DIR_SEGMENTS = {"do_not_index_sources"}

# Patterns that mark a node as a person/author/podcast, not a concept.
_PERSON_QUALIFIER_RE = re.compile(
    r"\(\s*(?:Author|Authors?|Host|Co-Host|Researcher|Professor|CEO|CTO|CPO|COO|CFO|CXO|"
    r"SVP|VP|EVP|Founder|Co-Founder|Chief|Director|Coach|Guest|Speaker|Podcast|Partner|"
    r"Principal|Investor|Angel|Advisor|Executive|Fellow|Engineer|Scientist|Lead)\s*\)",
    re.IGNORECASE,
)
# Podcast / show / channel names that show up as god-nodes.
_SHOW_PATTERNS = re.compile(
    r"(Podcast|Show|Newsletter|Substack|YouTube Channel|Bulletin|Blog)\b",
    re.IGNORECASE,
)


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


def _known_people_from_graph(data: dict) -> set[str]:
    """Build a set of author/contributor names referenced anywhere in the graph.

    Used to catch person nodes whose label is a bare name (no '(Author)' tag).
    """
    people: set[str] = set()
    for n in data.get("nodes", []):
        for field in ("author", "contributor"):
            v = n.get(field)
            if v and isinstance(v, str):
                people.add(v.strip())
    return people


def _is_person_node(node: dict, known_people: set[str]) -> bool:
    label = (node.get("label") or "").strip()
    if not label:
        return False
    # Explicit qualifier like "(Author)", "(Host)", "(CEO)"
    if _PERSON_QUALIFIER_RE.search(label):
        return True
    # Show/podcast/newsletter names
    if _SHOW_PATTERNS.search(label):
        return True
    # Bare-name match against known authors/contributors
    if label in known_people:
        return True
    # Strip parenthetical and retry (e.g. "Wes Kao (Founder, Maven)")
    stripped = _PERSON_QUALIFIER_RE.sub("", label)
    stripped = re.sub(r"\([^)]*\)", "", stripped).strip()
    if stripped and stripped in known_people:
        return True
    # Podcast-guest heuristic: if node sourced from a podcast directory AND its
    # label is a slug-matching substring of the source filename, it's likely
    # the guest's name (e.g. "Ben Williams" appears in "...ben-williams-vp-of-product.md").
    source_file = (node.get("source_file") or "").lower()
    if any(marker in source_file for marker in ("lennys-podcast", "/podcast", "/youtube")):
        slug = re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-")
        if slug and len(slug) >= 5 and slug in source_file:
            return True
    return False


def god_nodes(top_n: int = 20, concepts_only: bool = True):
    """Top-degree nodes. If concepts_only is True, filter out author/podcast nodes.

    Delegates degree ranking to graphify.analyze.god_nodes, then post-filters.
    """
    _ensure_graphify()
    data = load_raw()
    known_people = _known_people_from_graph(data) if concepts_only else set()
    label_by_id = {n["id"]: n for n in data.get("nodes", [])}

    try:
        from graphify.analyze import god_nodes as _g
        # Ask for more than top_n so we have headroom after filtering.
        raw = _g(load_graph(), top_n=top_n * 4 if concepts_only else top_n)
    except Exception:
        G = load_graph()
        ranked = sorted(G.degree, key=lambda x: -x[1])[: top_n * 4]
        raw = [
            {"id": nid, "label": G.nodes[nid].get("label", nid), "edges": d}
            for nid, d in ranked
        ]

    if not concepts_only:
        return raw[:top_n]

    filtered = []
    for entry in raw:
        nid = entry.get("id")
        node = label_by_id.get(nid, {"label": entry.get("label", nid)})
        if _is_person_node(node, known_people):
            continue
        filtered.append(entry)
        if len(filtered) >= top_n:
            break
    return filtered


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
    """Cross-community high-confidence edges.

    Reads from kb/.kb/graph/surprising.json if present (computed on the
    pre-consolidation raw graph — see compute_surprising_from_chunks). Otherwise
    falls back to computing on the current post-processed graph, which often
    returns an empty list because cross-community edges collapse to intra-
    community after label-normalized merges.
    """
    if SURPRISING_JSON.exists():
        data = json.loads(SURPRISING_JSON.read_text())
        return data.get("edges", [])[:top_n]

    _ensure_graphify()
    from graphify.analyze import surprising_connections as _s
    G = load_graph()
    comms_raw = communities()
    try:
        comms = {int(k): v for k, v in comms_raw.items()}
    except (TypeError, ValueError):
        comms = comms_raw
    try:
        return _s(G, comms, top_n=top_n)
    except Exception as e:
        print(f"WARN: surprising_connections fallback failed: {e}", file=sys.stderr)
        return []


def compute_surprising_from_chunks(chunk_dir: Path, top_n: int = 25) -> Path:
    """Rebuild the pre-consolidation graph from raw chunk files, compute
    surprising_connections on it, and persist to SURPRISING_JSON.

    This exists because Phase 1's label-normalized consolidation merges
    cross-community edges back into their canonical node, which destroys
    the graphify.analyze.surprising_connections signal on the post-processed
    graph. Running on the pre-merge chunks preserves it.
    """
    _ensure_graphify()
    from graphify.build import build_from_json
    from graphify.cluster import cluster as _cluster
    from graphify.analyze import surprising_connections as _sc

    chunk_files = sorted(chunk_dir.glob(".graphify_chunk_*.json"))
    if not chunk_files:
        raise FileNotFoundError(
            f"No .graphify_chunk_*.json files found in {chunk_dir}. "
            "Run a fresh build first — chunks are written during the extraction phase."
        )

    merged_nodes: list = []
    merged_edges: list = []
    merged_hyperedges: list = []
    seen_ids: set = set()
    for p in chunk_files:
        try:
            d = json.loads(p.read_text())
        except json.JSONDecodeError:
            continue
        for n in d.get("nodes", []):
            nid = n.get("id")
            if not nid or nid in seen_ids:
                continue
            seen_ids.add(nid)
            merged_nodes.append(n)
        merged_edges.extend(d.get("edges", []))
        merged_hyperedges.extend(d.get("hyperedges", []))

    # Prune dangling edges
    valid_edges = [
        e for e in merged_edges
        if e.get("source") in seen_ids and e.get("target") in seen_ids
    ]

    extraction = {
        "nodes": merged_nodes,
        "edges": valid_edges,
        "hyperedges": merged_hyperedges,
        "input_tokens": 0,
        "output_tokens": 0,
    }
    G = build_from_json(extraction)
    communities_map = _cluster(G)
    raw_surprises = _sc(G, communities_map, top_n=top_n)

    # Enrich each surprise with labels + source files for committed readability.
    node_by_id = {n["id"]: n for n in merged_nodes}
    enriched = []
    for s in raw_surprises:
        src_id = s.get("source") or s.get("from") or ""
        tgt_id = s.get("target") or s.get("to") or ""
        src_node = node_by_id.get(src_id, {})
        tgt_node = node_by_id.get(tgt_id, {})
        enriched.append({
            "source": src_id,
            "source_label": src_node.get("label", src_id),
            "source_file": src_node.get("source_file", ""),
            "target": tgt_id,
            "target_label": tgt_node.get("label", tgt_id),
            "target_file": tgt_node.get("source_file", ""),
            "relation": s.get("relation", ""),
            "confidence": s.get("confidence", ""),
            "confidence_score": s.get("confidence_score", 0.0),
            "reason": s.get("reason", ""),
        })

    SURPRISING_JSON.parent.mkdir(parents=True, exist_ok=True)
    SURPRISING_JSON.write_text(json.dumps({
        "computed_from": "pre-consolidation raw chunks",
        "chunk_dir": str(chunk_dir),
        "chunk_count": len(chunk_files),
        "raw_nodes": len(merged_nodes),
        "raw_edges": len(valid_edges),
        "raw_communities": len(communities_map),
        "edges": enriched,
    }, indent=2))
    return SURPRISING_JSON


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
    concepts_only = not args.include_people
    for g in god_nodes(top_n=args.n, concepts_only=concepts_only):
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
        src = s.get("source_label") or s.get("source") or s.get("from", "?")
        tgt = s.get("target_label") or s.get("target") or s.get("to", "?")
        rel = s.get("relation", "")
        conf = s.get("confidence", "")
        reason = s.get("reason", "")
        tag = f"[{rel}, {conf}]" if conf else f"[{rel}]"
        line = f"  {src}  →  {tgt}  {tag}"
        if reason:
            line += f"\n    {reason}"
        print(line)


def _cmd_compute_surprising(args):
    chunk_dir = Path(args.chunk_dir)
    out = compute_surprising_from_chunks(chunk_dir, top_n=args.n)
    data = json.loads(out.read_text())
    print(f"Wrote {out} ({len(data.get('edges', []))} cross-community edges)")
    print(f"  chunks: {data.get('chunk_count')}")
    print(f"  raw nodes: {data.get('raw_nodes')}")
    print(f"  raw communities: {data.get('raw_communities')}")


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

    sg = sub.add_parser("god-nodes", help="Top-degree concepts (authors/podcasts filtered by default)")
    sg.add_argument("-n", type=int, default=20)
    sg.add_argument("--include-people", action="store_true", help="Include author/podcast nodes (default: excluded)")
    sg.set_defaults(func=_cmd_god_nodes)

    so = sub.add_parser("orphans", help="Nodes with degree 0")
    so.set_defaults(func=_cmd_orphans)

    sc = sub.add_parser("communities", help="Leiden clusters")
    sc.add_argument("-n", type=int, default=15)
    sc.set_defaults(func=_cmd_communities)

    sx = sub.add_parser("surprising", help="Cross-community insights (reads surprising.json if present)")
    sx.add_argument("-n", type=int, default=10)
    sx.set_defaults(func=_cmd_surprising)

    scs = sub.add_parser(
        "compute-surprising",
        help="Rebuild surprising.json from raw chunks (pre-consolidation graph)",
    )
    scs.add_argument("--chunk-dir", default="/tmp/graphify-phase1/graphify-out",
                     help="Directory containing .graphify_chunk_*.json files")
    scs.add_argument("-n", type=int, default=25)
    scs.set_defaults(func=_cmd_compute_surprising)

    sp = sub.add_parser("open", help="Open graph.html in browser")
    sp.set_defaults(func=_cmd_open)

    spp = sub.add_parser("postprocess", help="Filter scaffolding + consolidate duplicates")
    spp.set_defaults(func=_cmd_postprocess)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
