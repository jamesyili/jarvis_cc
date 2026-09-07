---
name: leo-kb-reference
description: The Leo knowledge base data model and theory as applied here - domain split, raw/wiki layers, article frontmatter, state files, TF-IDF search index, the graphify knowledge graph (nodes, hyperedges, Leiden communities, god nodes), hard/soft slug routing, and current counts/staleness. Load this when reasoning about anything under kb/ - adding or routing a source, interpreting graph or search output, judging index freshness, planning a wiki compile, or answering what is in the KB and how big is it. Keywords - kb, knowledge base, raw, wiki, graph.json, god nodes, hyperedge, Leiden, communities, surprising.json, search index, TF-IDF, HARD_SLUGS, ingested manifest, do_not_index_sources.
---

# Leo KB Reference

The data model and the concepts a zero-context maintainer needs to reason about `kb/`. Operating commands → [leo-run-and-operate]; failure triage → [leo-debugging-playbook]; automation plans → [leo-kb-automation-campaign].

## Data model

Two domains × two layers, plus a graph backend:

```
kb/
├── hard/            ML, recsys, systems, technical craft
│   ├── raw/         ingested articles, one dir per source (+ loose PDF/md drops at root)
│   └── wiki/        compiled concept articles (66 as of 2026-07-13, + _index.md/_plan.md)
├── soft/            leadership, comms, product, coaching
│   ├── raw/         incl. do_not_index_sources/ (Lenny transcripts excluded from indexing)
│   └── wiki/        EMPTY (only _index.md) — soft compile never ran
└── .kb/             search_index.json + graph/
```

Counts as of 2026-07-13 (re-verify with the provenance commands): hard raw ~797 articles in 24 source dirs; soft raw ~1,837 in 7 dirs. Backlog and older docs cite smaller numbers (2,600+, soft 1,556) — the corpus grew past its documentation.

**Article frontmatter convention** (see any file under `kb/hard/raw/eugene-yan/`): title heading, then `**Source:** URL`, `**Ingested:** date`, optional `**Re-scraped:** date`, `**Tags:** list`, then `---` and body.

**State files:** `kb/.ingested_manifest.json` (ingest dedup), `kb/.yt_manifest.json` (YouTube), per-domain `_index.md` catalogs (built by `build_index.py`), `kb/.digests/` (daily digests — **idle**: directory empty, daily mode isn't running).

**Hygiene notes:** loose personal PDFs sit at `kb/hard/raw/` root, including `Failed Anthropic Interview - James.pdf` — a personal artifact arguably misfiled in the indexable KB (flagged 2026-07-12; move is James's call). KB privacy invariant: Pinterest-internal content never enters `kb/` (instinct `pinterest-internals-not-in-kb`).

## Source routing (the trap)

Hard/soft assignment is **hardcoded slug sets duplicated in two live places**: `HARD_SLUGS`/`SOFT_SLUGS` in `scripts/ingest.py` AND inline sets in `scripts/scout.py` (plus a dead copy in `migrate.py`). They have already drifted (`simon-willison` present in some, not others). **An unregistered source silently defaults to soft.** Adding a source = update both live sets — full checklist in [leo-config-and-flags].

## Search layer

- `kb/.kb/search_index.json` (~15.6 MB) — TF-IDF index built/queried by `scripts/kb_search.py`, catalogs by `scripts/build_index.py`.
- **It never auto-invalidates.** Built 2026-04-05; the corpus has grown by hundreds of articles since. Any search without a prior `--rebuild` under-reports. This is the KB's #1 silent quality bug.

## Graph layer (`kb/.kb/graph/`, built 2026-04-08 by graphify)

| Artifact | What it is |
|---|---|
| `graph.json` (8.1 MB) | 6,706 nodes / 8,585 edges / 474 hyperedges / 593 Leiden communities; extraction 70% EXTRACTED, 30% INFERRED (avg confidence 0.76) |
| `communities.json` | Leiden cluster membership |
| `surprising.json` | 25 cross-community edges (its `chunk_dir` field points at a dead /tmp path — cosmetic) |
| `GRAPH_REPORT.md` | Build report incl. the cost record: **1,992,800 input / 415,600 output tokens for 2,688 files (~9.8M words)** — the repo's one measured LLM-sweep datapoint; use it to forecast |
| `manifest.json` | says `source: phase1-salvage` |
| `raw_chunks/` | 110 dotfile chunks — the ONLY copy of pre-consolidation extraction, gitignored; 13 chunks missing (rate-limit death — [leo-failure-archaeology] J) |
| `graph.html` | degree≥2 subgraph viz (4,584 nodes; to_html caps at 5,000), gitignored |

Committed vs not (per `.gitignore`): graph.json, communities.json, GRAPH_REPORT.md, manifest.json, surprising.json are committed; graph.html, cache/, raw_chunks/ are not.

**Concepts as applied here:**
- **Hyperedge** — a multi-node relation extracted from one passage (not just pairwise links).
- **Leiden community** — a graph cluster ≈ a topic; 593 of them; the intended feed for soft-wiki compilation and `/kb-reflect`.
- **God node** — a degree outlier ≈ core abstraction (or over-merged concept). Top: Eugene Yan (52 edges), RAG (33), Transformer Architecture (33). Author-nodes are filtered in god-node queries; filter is 19/20 correct (known podcast-guest edge case, accepted).

Driver: `~/.venvs/graphify/bin/python scripts/build_graph.py {stats|neighbors|god-nodes|communities|surprising|…}` — query commands are instant; `build` is 1–3 hours and token-heavy.

## Wiki layer

Compile flow (`scripts/compile_wiki.py`, shells `claude` CLI, model pinned `claude-sonnet-4-6`): `scan` (batches 150 articles/call → `.scan_results.json`) → `plan` (human-reviewed `_plan.md`) → `compile` (writes `wiki/*.md`, state in `.compile_state.json`, failures in `.errors/`). Hard domain compiled once (2026-04-05, 65 concepts → 66 articles). Soft never compiled.

**graphify Phase 2** (feed scan from god_nodes/hyperedges instead of LLM-batching raw/) is designed but **frozen by choice** since 2026-04-09 — the tool-builder-trap demotion, with reversal criteria recorded in backlog.md. Don't build it as a side quest; see [leo-research-methodology] on the demotion discipline.

## Learner-model layer (`kb/.kb/knowledge_state.json`, added 2026-09-07)

Per-concept **understanding** (1 little · 2 basic-assumed · 3 proven · 4 boundary) and **relevance** (0/2/3) for James, over the 65 wiki concepts + 7 extras (72). Raw articles inherit by tag/title match (understanding = min, relevance = max). Rendered into wiki frontmatter and the `_index.md` U/R columns by `build_index.py`; human view `self/learning/knowledge_state.md`. Driver: `python3 scripts/kb_knowledge_state.py {init|set|bulk|get|list|queue|article|render|export|check}` — stdlib only, Codex-portable. Written only on evidence by the `learn`, `context-update`, and `ingest` skills; full contract in the `knowledge-state` skill and `system/kb-spec.md` §Learner model. Papers James passes: `scripts/ingest_paper.py` → `kb/hard/raw/arxiv/`.

## When NOT to use this skill

- Running KB operations → [leo-run-and-operate]
- KB script failures → [leo-debugging-playbook]
- Scheduling/automation of ingestion → [leo-kb-automation-campaign]
- Slug/registry edit mechanics → [leo-config-and-flags]

## Provenance & maintenance

Authored 2026-07-13 from direct filesystem checks (2026-07-12) + GRAPH_REPORT.md. Re-verify:
- Counts: `for d in hard soft; do find kb/$d/raw -name '*.md' ! -name '_index.md' | wc -l; done`
- Wiki state: `ls kb/hard/wiki | wc -l; ls kb/soft/wiki`
- Index staleness: `stat -c '%y' kb/.kb/search_index.json; find kb -name '*.md' -newer kb/.kb/search_index.json | wc -l`
- Graph stats: `~/.venvs/graphify/bin/python scripts/build_graph.py stats`
- raw_chunks: `ls kb/.kb/graph/raw_chunks/ | wc -l` (expect 110)
- Slug drift: `grep -n 'simon-willison' scripts/ingest.py scripts/scout.py scripts/migrate.py`
