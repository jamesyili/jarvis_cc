---
name: graphify integration Phase 1 complete
description: graphify KB graph backend shipped April 2026 — canonical graph.json at kb/.kb/graph/, scripts/build_graph.py wrapper, known issues to fix before Phase 2
type: project
---

Phase 1 of the graphify integration (see `~/.claude/plans/binary-mapping-perlis.md`) shipped 2026-04-08 as commit `8f8222d`. The canonical KB graph lives at `kb/.kb/graph/graph.json` (7.8 MB, 6706 nodes / 8585 edges / 593 communities / 474 hyperedges). Built via `scripts/build_graph.py` which wraps the graphify Claude Code skill. User-facing skill is `/kb-graph` at `~/.claude/skills/kb-graph/SKILL.md`.

**Why:** Augment Leo's KB with a graph backend for better wiki compilation, graph-aware search, cross-cutting reflection, and orphan/gap detection. Augments, does not replace, the curated `kb/wiki/` layer.

**How to apply:** Before Phase 2 (wiring compile_wiki.py), fix the three known issues from the Phase 1 commit:
1. Fill in the 13 missing chunks via `python scripts/build_graph.py refresh` (needs testing — depends on graphify `--update` working correctly)
2. Add author-node filter to `god_nodes()` so Eugene Yan / Wes Kao / Lenny's Podcast don't dominate top-degree results
3. Fix `surprising_connections` which returns 0 after post-process consolidation — run it BEFORE consolidation, or teach it to detect edges that became intra-community after merges

The hyperedges are the highest-value output (e.g., "Pinterest Recommendation Stack (PinSage, ItemSage, PinnerFormer)", "Recommendation System Architecture Family" 7 nodes @ 1.00 confidence) — Phase 2's `compile_wiki scan` should feed these directly as candidate concepts.
