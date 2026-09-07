#!/usr/bin/env python3
"""Learner model over the KB — what James knows, how deeply, and how relevant it is.

Two dimensions on every hard-side concept (design ratified 2026-09-07, James):

  understanding  1 very little exposure / unknown (DEFAULT for most things)
                 2 basic understanding (assumed where James's background applies:
                   PhD statistical ML, 12 years recsys, 4-5 on content quality/integrity,
                   5 on content understanding)
                 3 proven depth (demonstrated to Leo/Codex in dialogue or practice,
                   or authored/co-authored)
                 4 boundary pushing
  relevance      0 not obviously relevant to current role / career goals
                 2 somewhat or potentially relevant
                 3 very relevant

The CONCEPT is the unit (the kb/hard/wiki slugs plus a few the wiki predates).
Raw articles inherit through their tags: understanding = min over matched concepts,
relevance = max. Levels move only on evidence written by the `learn` and
`context-update` skills (or James). Stdlib only; works from Codex and Claude Code.

  python3 scripts/kb_knowledge_state.py init                 # create/refresh the sidecar
  python3 scripts/kb_knowledge_state.py set <concept> [--understanding N] [--relevance N]
                                             --note "..." [--kind dialogue|practice|work|authored|seed|manual] [--by codex|claude|james]
  python3 scripts/kb_knowledge_state.py bulk <json-file>     # many sets at once
  python3 scripts/kb_knowledge_state.py get <concept>
  python3 scripts/kb_knowledge_state.py list [--sort relevance|understanding|name]
  python3 scripts/kb_knowledge_state.py queue                # relevance 3 & understanding <= 2
  python3 scripts/kb_knowledge_state.py article <kb-relative-path>   # inherited values
  python3 scripts/kb_knowledge_state.py render               # frontmatter in wiki articles
  python3 scripts/kb_knowledge_state.py export               # self/learning/knowledge_state.md
  python3 scripts/kb_knowledge_state.py check                # drift between wiki and sidecar

State file: kb/.kb/knowledge_state.json (committed). Human view: self/learning/knowledge_state.md.
"""

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KB = ROOT / "kb"
WIKI = KB / "hard" / "wiki"
STATE_PATH = KB / ".kb" / "knowledge_state.json"
EXPORT_PATH = ROOT / "self" / "learning" / "knowledge_state.md"

UNDERSTANDING = {
    1: "very little exposure / unknown (default)",
    2: "basic understanding (assumed where James's background applies)",
    3: "proven depth (demonstrated in dialogue/practice, or authored)",
    4: "boundary pushing",
}
RELEVANCE = {
    0: "not obviously relevant",
    2: "somewhat / potentially relevant",
    3: "very relevant",
}
KINDS = ("dialogue", "practice", "work", "authored", "seed", "manual")
DEFAULTS = {"understanding": 1, "relevance": 0}
NON_CONCEPT_WIKI = {"progression-log"}

# Concepts the wiki predates (no article yet). Tags let raw articles inherit from them.
EXTRA_CONCEPTS = {
    "semantic-id-tokenization": {
        "name": "Semantic-ID Tokenization (codebooks, RQ-VAE, collisions, re-minting)",
        "tags": ["semantic-ids", "rq-vae", "codebook", "tokenizer", "sid", "collision", "generative-retrieval"],
    },
    "recsys-scaling-laws": {
        "name": "Scaling Laws for Recommenders (HSTU, Wukong, compute allocation)",
        "tags": ["scaling-laws", "hstu", "wukong", "compute-allocation", "scaling"],
    },
    "serving-efficiency-and-user-state-caching": {
        "name": "Serving Efficiency & User-State Caching (KV/prefix caching, quantization, MFU)",
        "tags": ["kv-cache", "prefix-caching", "gpu-serving", "mfu", "quantization", "disaggregation", "serving-cost"],
    },
    "agent-harnesses-and-self-evolution": {
        "name": "Agent Harnesses & Self-Evolving Agents",
        "tags": ["agent-harness", "agent-evolution", "self-evolving", "skill-evolution", "gepa", "autoharness", "llm-agents", "multi-agent"],
    },
    "pre-ranking-cross-stage-consistency": {
        "name": "Pre-Ranking (L1) & Cross-Stage Consistency",
        "tags": ["pre-ranking", "preranking", "l1", "cross-stage-consistency", "sample-selection-bias", "rank-distillation"],
    },
    "user-foundation-models-and-distillation": {
        "name": "User Foundation Models & Teacher Distillation",
        "tags": ["foundation-model", "user-model", "teacher-distillation", "cfm", "pretrain-finetune"],
    },
    "offline-online-calibration-and-candidate-logging": {
        "name": "Offline→Online Calibration & Candidate Logging",
        "tags": ["offline-online", "calibration", "candidate-logging", "full-funnel", "offline-replay"],
    },
}


# ---------------------------------------------------------------------------
# Wiki parsing
# ---------------------------------------------------------------------------

def _split_frontmatter(text):
    """Return (frontmatter_lines, body_text) or (None, text) when no YAML block."""
    if not text.startswith("---"):
        return None, text
    lines = text.splitlines(keepends=True)
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return lines[1:i], "".join(lines[i + 1:])
    return None, text


def _yaml_scalar(fm_lines, key):
    for line in fm_lines:
        if line.startswith(key + ":"):
            return line.split(":", 1)[1].strip()
    return None


def _yaml_tags(fm_lines):
    raw = _yaml_scalar(fm_lines, "tags") or ""
    raw = raw.strip("[]")
    return [normalize_tag(t) for t in raw.split(",") if t.strip()]


def normalize_tag(tag):
    return re.sub(r"[^a-z0-9]+", "-", tag.strip().lower()).strip("-")


def wiki_concepts():
    """slug -> {name, tags, related} from kb/hard/wiki/*.md."""
    out = {}
    for f in sorted(WIKI.glob("*.md")):
        slug = f.stem
        if slug.startswith("_") or slug in NON_CONCEPT_WIKI:
            continue
        text = f.read_text(encoding="utf-8", errors="replace")
        fm, _ = _split_frontmatter(text)
        name = slug.replace("-", " ").title()
        tags, related = [], []
        if fm:
            name = _yaml_scalar(fm, "concept") or name
            tags = _yaml_tags(fm)
            related = re.findall(r"\[\[hard/wiki/([\w-]+)", "".join(fm))
        out[slug] = {"name": name, "tags": tags, "related": related, "wiki": f"kb/hard/wiki/{f.name}"}
    return out


# ---------------------------------------------------------------------------
# State
# ---------------------------------------------------------------------------

def load_state():
    if STATE_PATH.exists():
        with open(STATE_PATH, encoding="utf-8") as fh:
            return json.load(fh)
    return None


def save_state(state):
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    state["updated"] = date.today().isoformat()
    with open(STATE_PATH, "w", encoding="utf-8") as fh:
        json.dump(state, fh, indent=1, ensure_ascii=False)
        fh.write("\n")


def new_concept(slug, meta):
    return {
        "name": meta["name"],
        "wiki": meta.get("wiki"),
        "tags": meta.get("tags", []),
        "related": meta.get("related", []),
        "understanding": DEFAULTS["understanding"],
        "relevance": DEFAULTS["relevance"],
        "note": "",
        "updated": None,
        "updated_by": None,
        "evidence": [],
    }


def init_state(state=None):
    """Create the sidecar, or add concepts that appeared since (never overwrite levels)."""
    if state is None:
        state = {
            "version": 1,
            "created": date.today().isoformat(),
            "scales": {
                "understanding": {str(k): v for k, v in UNDERSTANDING.items()},
                "relevance": {str(k): v for k, v in RELEVANCE.items()},
            },
            "defaults": dict(DEFAULTS),
            "inheritance": "raw articles: understanding = min over matched concepts, relevance = max; match = article tag == concept tag or concept slug",
            "concepts": {},
        }
    added = []
    for slug, meta in wiki_concepts().items():
        if slug not in state["concepts"]:
            state["concepts"][slug] = new_concept(slug, meta)
            added.append(slug)
        else:  # refresh descriptive fields only
            c = state["concepts"][slug]
            c["name"], c["tags"], c["related"], c["wiki"] = meta["name"], meta["tags"], meta["related"], meta["wiki"]
    for slug, meta in EXTRA_CONCEPTS.items():
        if slug not in state["concepts"]:
            state["concepts"][slug] = new_concept(slug, {**meta, "wiki": None})
            added.append(slug)
    return state, added


def require_state():
    state = load_state()
    if state is None:
        sys.exit("No knowledge_state.json yet — run: python3 scripts/kb_knowledge_state.py init")
    return state


def resolve_concept(state, name):
    """Accept a slug, a wiki path, or a case-insensitive concept name."""
    key = name.strip()
    if key.endswith(".md"):
        key = Path(key).stem
    if key in state["concepts"]:
        return key
    low = key.lower()
    for slug, c in state["concepts"].items():
        if slug.lower() == low or c["name"].lower() == low:
            return slug
    matches = [slug for slug, c in state["concepts"].items() if low in slug or low in c["name"].lower()]
    if len(matches) == 1:
        return matches[0]
    if matches:
        sys.exit(f"Ambiguous concept '{name}': {', '.join(sorted(matches))}")
    sys.exit(f"Unknown concept '{name}'. Use `list` to see slugs, or add it to EXTRA_CONCEPTS.")


def set_levels(state, slug, understanding=None, relevance=None, note="", kind="manual", by="claude", when=None):
    c = state["concepts"][slug]
    if understanding is not None and understanding not in UNDERSTANDING:
        sys.exit(f"understanding must be one of {sorted(UNDERSTANDING)}")
    if relevance is not None and relevance not in RELEVANCE:
        sys.exit(f"relevance must be one of {sorted(RELEVANCE)}")
    if kind not in KINDS:
        sys.exit(f"kind must be one of {KINDS}")
    when = when or date.today().isoformat()
    ev = {"date": when, "kind": kind, "by": by, "note": note}
    if understanding is not None and understanding != c["understanding"]:
        ev["understanding"] = [c["understanding"], understanding]
        c["understanding"] = understanding
    if relevance is not None and relevance != c["relevance"]:
        ev["relevance"] = [c["relevance"], relevance]
        c["relevance"] = relevance
    if note:
        c["note"] = note
    c["updated"], c["updated_by"] = when, by
    c["evidence"].append(ev)
    return c


# ---------------------------------------------------------------------------
# Inheritance for raw articles
# ---------------------------------------------------------------------------

def article_tags(path):
    """Tags from a raw article (**Tags:** line) or a wiki article (YAML tags)."""
    text = path.read_text(encoding="utf-8", errors="replace")
    fm, _ = _split_frontmatter(text)
    if fm:
        return _yaml_tags(fm)
    for line in text.splitlines()[:20]:
        if line.startswith("**Tags:**"):
            return [normalize_tag(t) for t in line.replace("**Tags:**", "").split(",") if t.strip()]
    return []



# Tags too generic to identify a concept from a title alone.
GENERIC_KEYS = {
    "recsys", "retrieval", "ranking", "llm", "llms", "scaling", "evaluation", "training", "personalization",
    "search", "embeddings", "agents", "inference", "serving", "optimization", "fundamentals", "ml-systems",
    "deep-learning", "ai-agents", "ml-research", "architectures", "generation", "classification", "monitoring",
    "operational", "interview", "system-design", "ml-system-design", "case-studies", "labeling", "moat", "sft",
    "distillation", "quantization", "l1", "sid", "moe", "rl", "mdp", "ann", "lsh", "icl", "ssm", "vlm", "clip",
}


def article_title(path):
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines()[:5]:
        if line.startswith("# "):
            return line[2:].strip().lower()
    return path.stem.replace("-", " ").lower()


def title_matches(title, keys):
    """True if a specific (non-generic) concept key appears as a phrase in the title."""
    for key in keys:
        key = normalize_tag(key)
        if not key or key in GENERIC_KEYS or len(key) < 4:
            continue
        pattern = r"\b" + r"[ -]?".join(re.escape(part) for part in key.split("-")) + r"s?\b"
        if re.search(pattern, title):
            return True
    return False


def inherit(state, path):
    """Return {understanding, relevance, matched:[slugs]} for a KB file."""
    p = path if path.is_absolute() else ROOT / path
    if not p.exists():
        p = KB / path
    if not p.exists():
        sys.exit(f"No such file: {path}")
    if p.parent == WIKI and p.stem in state["concepts"]:
        c = state["concepts"][p.stem]
        return {"understanding": c["understanding"], "relevance": c["relevance"], "matched": [p.stem]}
    tags = set(article_tags(p))
    title = article_title(p)
    matched = []
    for slug, c in state["concepts"].items():
        if slug in tags or tags.intersection(c["tags"]) or title_matches(title, [slug] + c["tags"]):
            matched.append(slug)
    if not matched:
        return {**DEFAULTS, "matched": []}
    return {
        "understanding": min(state["concepts"][s]["understanding"] for s in matched),
        "relevance": max(state["concepts"][s]["relevance"] for s in matched),
        "matched": sorted(matched),
    }


# ---------------------------------------------------------------------------
# Render into wiki frontmatter + export a human view
# ---------------------------------------------------------------------------

RENDER_KEYS = ("understanding", "relevance", "knowledge_updated")


def render(state):
    """Write understanding/relevance/knowledge_updated into each wiki article's YAML block."""
    touched = 0
    for slug, c in state["concepts"].items():
        if not c.get("wiki"):
            continue
        path = ROOT / c["wiki"]
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        fm, body = _split_frontmatter(text)
        if fm is None:
            continue
        kept = [line for line in fm if not line.startswith(tuple(k + ":" for k in RENDER_KEYS))]
        kept += [
            f"understanding: {c['understanding']}  # {UNDERSTANDING[c['understanding']]}\n",
            f"relevance: {c['relevance']}  # {RELEVANCE[c['relevance']]}\n",
            f"knowledge_updated: {c['updated'] or 'never'}\n",
        ]
        new_text = "---\n" + "".join(kept) + "---\n" + body
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            touched += 1
    return touched


def export(state):
    concepts = state["concepts"]
    order = sorted(concepts.items(), key=lambda kv: (-kv[1]["relevance"], kv[1]["understanding"], kv[0]))
    queue = [(s, c) for s, c in order if c["relevance"] == 3 and c["understanding"] <= 2]
    depth = [(s, c) for s, c in order if c["understanding"] >= 3]
    lines = [
        "# Knowledge state — what James knows, how deeply, and how relevant it is",
        "",
        f"> Auto-generated by `scripts/kb_knowledge_state.py export` on {date.today().isoformat()} from `kb/.kb/knowledge_state.json`. "
        "Do not edit by hand — change levels with `set` (the `learn` and `context-update` skills do this on evidence).",
        "",
        "**Understanding:** 1 very little exposure / unknown (default) · 2 basic (assumed where the PhD-stat-ML + 12-yr-recsys background applies) · 3 proven depth (demonstrated or authored) · 4 boundary pushing.  ",
        "**Relevance:** 0 not obviously relevant · 2 somewhat / potentially · 3 very relevant (current role + 2027 agenda).",
        "",
        f"## Learning queue — relevance 3, understanding ≤ 2 ({len(queue)})",
        "",
        "| Concept | U | R | Note |",
        "|---|---|---|---|",
    ]
    for s, c in queue:
        lines.append(f"| `{s}` | {c['understanding']} | {c['relevance']} | {c['note']} |")
    lines += ["", f"## Proven depth and beyond — understanding ≥ 3 ({len(depth)})", "", "| Concept | U | R | Note |", "|---|---|---|---|"]
    for s, c in depth:
        lines.append(f"| `{s}` | {c['understanding']} | {c['relevance']} | {c['note']} |")
    lines += ["", f"## All concepts ({len(concepts)}), by relevance then understanding", "", "| Concept | U | R | Updated | Wiki | Note |", "|---|---|---|---|---|---|"]
    for s, c in order:
        wiki = f"[[{c['wiki']}]]" if c.get("wiki") else "—"
        lines.append(f"| `{s}` | {c['understanding']} | {c['relevance']} | {c['updated'] or '—'} | {wiki} | {c['note']} |")
    EXPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    EXPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(queue), len(depth)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def fmt(slug, c):
    return f"{slug:50s} U{c['understanding']} R{c['relevance']}  {c['note'][:70]}"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("init")
    p = sub.add_parser("set")
    p.add_argument("concept")
    p.add_argument("--understanding", "-u", type=int)
    p.add_argument("--relevance", "-r", type=int)
    p.add_argument("--note", "-n", default="", help="one line: what was demonstrated / why")
    p.add_argument("--kind", "-k", default="manual", choices=KINDS)
    p.add_argument("--by", "-b", default="claude", help="codex | claude | james")
    p.add_argument("--date", help="YYYY-MM-DD (default today)")
    p.add_argument("--no-render", action="store_true")
    p = sub.add_parser("bulk")
    p.add_argument("json_file", help='[{"concept":..., "understanding":N, "relevance":N, "note":"...", "kind":"seed", "by":"claude"}]')
    p.add_argument("--no-render", action="store_true")
    p = sub.add_parser("get"); p.add_argument("concept")
    p = sub.add_parser("list"); p.add_argument("--sort", default="relevance", choices=["relevance", "understanding", "name"])
    sub.add_parser("queue")
    p = sub.add_parser("article"); p.add_argument("path")
    sub.add_parser("render")
    sub.add_parser("export")
    sub.add_parser("check")
    args = ap.parse_args(argv)

    if args.cmd == "init":
        state, added = init_state(load_state())
        save_state(state)
        print(f"knowledge_state.json: {len(state['concepts'])} concepts ({len(added)} added: {', '.join(added) or 'none'})")
        return

    state = require_state()

    if args.cmd == "set":
        slug = resolve_concept(state, args.concept)
        if args.understanding is None and args.relevance is None:
            sys.exit("Nothing to set: pass --understanding and/or --relevance")
        if not args.note:
            sys.exit("--note is required: one line of evidence or reason")
        c = set_levels(state, slug, args.understanding, args.relevance, args.note, args.kind, args.by, args.date)
        save_state(state)
        if not args.no_render:
            render(state); export(state)
        print(fmt(slug, c))
        return

    if args.cmd == "bulk":
        rows = json.loads(Path(args.json_file).read_text(encoding="utf-8"))
        for row in rows:
            slug = resolve_concept(state, row["concept"])
            set_levels(state, slug, row.get("understanding"), row.get("relevance"), row.get("note", ""),
                       row.get("kind", "manual"), row.get("by", "claude"), row.get("date"))
        save_state(state)
        if not args.no_render:
            n = render(state); q, d = export(state)
            print(f"rendered {n} wiki articles; queue {q}, depth {d}")
        print(f"applied {len(rows)} rows")
        return

    if args.cmd == "get":
        slug = resolve_concept(state, args.concept)
        print(json.dumps({slug: state["concepts"][slug]}, indent=1, ensure_ascii=False))
        return

    if args.cmd == "list":
        items = state["concepts"].items()
        if args.sort == "relevance":
            items = sorted(items, key=lambda kv: (-kv[1]["relevance"], kv[1]["understanding"], kv[0]))
        elif args.sort == "understanding":
            items = sorted(items, key=lambda kv: (-kv[1]["understanding"], -kv[1]["relevance"], kv[0]))
        else:
            items = sorted(items)
        for slug, c in items:
            print(fmt(slug, c))
        return

    if args.cmd == "queue":
        rows = [(s, c) for s, c in state["concepts"].items() if c["relevance"] == 3 and c["understanding"] <= 2]
        rows.sort(key=lambda kv: (kv[1]["understanding"], kv[0]))
        print(f"Learning queue — relevance 3, understanding <= 2 ({len(rows)}):")
        for slug, c in rows:
            print(fmt(slug, c))
        return

    if args.cmd == "article":
        print(json.dumps(inherit(state, Path(args.path)), indent=1))
        return

    if args.cmd == "render":
        print(f"rendered {render(state)} wiki articles")
        return

    if args.cmd == "export":
        q, d = export(state)
        print(f"wrote {EXPORT_PATH.relative_to(ROOT)} — queue {q}, depth {d}, concepts {len(state['concepts'])}")
        return

    if args.cmd == "check":
        wiki = wiki_concepts()
        missing = [s for s in wiki if s not in state["concepts"]]
        orphans = [s for s, c in state["concepts"].items() if c.get("wiki") and s not in wiki]
        never = [s for s, c in state["concepts"].items() if not c["evidence"]]
        print(f"concepts {len(state['concepts'])}; wiki {len(wiki)}; missing from state: {missing or 'none'}; "
              f"state entries whose wiki vanished: {orphans or 'none'}; never assessed: {len(never)}")
        sys.exit(1 if missing or orphans else 0)


if __name__ == "__main__":
    main()
