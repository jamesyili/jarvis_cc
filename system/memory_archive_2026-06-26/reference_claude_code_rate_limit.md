---
name: Claude Code subscription rate limit
description: The Claude Code subscription has a rate limit that resets at 7pm Pacific. Long-running `claude -p` subprocess runs (like the graphify skill over 2600+ files) can hit it mid-run. Check the clock before starting, and build salvage paths for interrupted runs.
type: reference
---

Claude Code's subscription has a rolling rate limit that resets at **7pm America/Los_Angeles** (observed 2026-04-08). When it hits, `claude -p` subprocesses exit with code 0 and a plaintext message like `"You've hit your limit · resets 7pm (America/Los_Angeles)"` — which means exit-code checks alone can't distinguish success from rate-limit abort.

**Observed impact:** Phase 1 of the graphify integration ran `/graphify kb --mode deep` as a subprocess at ~16:44 PT. It dispatched 115 of 123 extraction subagents over 56 minutes before hitting the limit at ~18:50 PT, with Step 4 (merge/cluster/export) never running. 13 chunks (mostly lennys-podcast tail) were lost.

**How to apply:**
1. **Before kicking off long `claude -p` subprocess runs**, check local time vs 7pm PT. If less than 2 hours of runway remain, either wait for reset or scope the run smaller.
2. **Always preserve intermediate outputs.** The graphify skill writes per-chunk `.json` files to `graphify-out/` during Step 3, which made salvage possible after the rate limit hit. Verify any long-running external tool writes progress incrementally before running at scale.
3. **Exit code 0 is not sufficient.** Always tail the run log for rate-limit messages or check whether the expected final artifacts (e.g. `graph.json`, `GRAPH_REPORT.md`) exist.
4. **Build salvage paths.** For graphify specifically, `compute-surprising` in `build_graph.py` was added to rebuild from chunk files without re-running extraction — this pattern is useful when an external tool's post-processing step fails but its intermediate outputs survived.
