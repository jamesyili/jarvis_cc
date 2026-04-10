# Backlog

> Unified backlog: everything actionable in one place. Organized by what James does, not what system it lives in. Curriculum details live in `learning/learning_agenda.md` — this file tracks what to do next.

**Last updated:** 2026-04-09 PST

---

## Write
Blog posts, technical memos, opinions — synthesis artifacts where James wrestles with material in his own words.

| Item | Why / Goal | Description / Subtasks | Rough Time | Progress | Priority |
|------|-----------|----------------------|------------|----------|----------|
| Pretrain-finetune in recsys | G1 (UPP), technical depth, interview prep | Survey the pretrain+finetune paradigm in recsys. Cover CLR architecture, what's pretrained vs fine-tuned, why this paradigm, UPP angle, predictions. See `blog/pretrain-finetune-recsys.md` | 3-4 hrs | **Not started — hard deadline 2026-04-11 (next Saturday)** | P0 |
| Retentive recs / predicted serendipity | G1 (Retentive Recs flagship) | Own the technical narrative on retention-optimized recommendations. Explore-exploit, serendipity as objective, long-term user value. See `blog/retentive-recs.md` | 3-4 hrs | Not started | P0 |
| Generative recsys survey | Technical frontier, interview prep | RecGPT, PinRec, OneRec, semantic IDs. What works in production vs paper-only. My take on hybrid future. See `blog/generative-recsys.md` | 3-4 hrs | Not started | P1 |
| EM growth in age of AI | G2 + G4, unique voice | Lived experience of using AI as EM. What changes, what can't be automated, the avoidance trap. See `blog/em-growth-age-of-ai.md` | 2-3 hrs | Not started | P1 |
| Self-improvement in AI world | Personal reflection, Karen arc | Judgment, systems thinking, collaboration. The collection trap. Honest reflection. See `blog/self-improvement-in-ai-world.md` | 2-3 hrs | Not started | P2 |

## Learn
Specific concepts to study and internalize. Full curriculum in `learning/learning_agenda.md`.

| Item | Why / Goal | Description / Subtasks | Rough Time | Progress | Priority |
|------|-----------|----------------------|------------|----------|----------|
| CLR pretraining/fine-tuning deep dive | G1 (UPP), feeds blog post #1 | Model architecture, loss functions, features, condition handling. Feynman test with Leo, then write. Use KB raw articles as reference. Track in `kb/hard/wiki/progression-log.md` | 2-3 hrs | Not started — initial assessment pending | P0 |
| Model architecture & transformers (Track 5) | G1, Tier 1 curriculum | Attention mechanisms, positional encoding, decoder-only vs encoder-decoder, scaling laws. Karpathy watch-and-code series (9 videos) added to learning agenda. See `learning/learning_agenda.md` Track 5 | Ongoing | Resources queued | P1 |
| Evals + verification checkpoints (Track 2) | G2 (Pinsight), Tier 1 curriculum | Eval-driven development, human checkpoints in agentic systems. See `learning/learning_agenda.md` Track 2 | Ongoing | Not started | P1 |
| ML system design interview prep (Track 3) | Interview optionality | End-to-end system design practice. Start with UPP + PINvestigator interview answer writeups (8+8 hrs). See `learning/learning_agenda.md` Track 3 | Ongoing | Not started — promoted to Tier 1, start April 2026 | P1 |

## Build
Leo system, KB, side projects, infrastructure.

| Item | Why / Goal | Description / Subtasks | Rough Time | Progress | Priority |
|------|-----------|----------------------|------------|----------|----------|
| First `/kb-compile` run (hard domain) | KB value unlock | Run the 3-phase wiki compiler on hard skills. | 2-3 hrs | **Done 2026-04-05** — 65 concepts compiled, 66 hard wiki articles, 2,417 docs indexed | — |
| graphify Phase 1 (graph backend) | KB value unlock, feeds Phase 2 | Build canonical graph.json at kb/.kb/graph/ via graphify. See plan at `~/.claude/plans/binary-mapping-perlis.md`. | 4-6 hrs | **Done 2026-04-08** — commits `8f8222d` + `d917b4e`. 6706 nodes / 474 hyperedges / 593 communities, god_nodes author filter, surprising.json (25 cross-community insights) | — |
| graphify Phase 2 (wire compile_wiki.py) | KB quality uplift | Rewrite `compile_wiki.py:82-170` (scan) and `:249-323` (compile) to pull candidates from `build_graph.py` god_nodes + hyperedges instead of LLM-batching raw/. A/B run against current LLM scan (Option B — diff for one cycle before cutover). Populate `related:` field from graph neighbors. Kickstart soft-domain compilation (empty today). **Demoted 2026-04-09**: tool-builder trap risk; wiki isn't load-bearing for day-to-day thinking yet. Revisit when blog posts + interview prep ladder is underway. | 3-5 hrs | Not started — demoted from P1 | P2 |
| graphify Phase 3 (search + reflection) | KB quality uplift | Add `--expand` flag to `kb_search.py` that follows graph edges. Rewrite `kb-reflect` SKILL.md to pull Leiden clusters from `communities.json` and synthesize to `kb/{domain}/reflections/` (committed, transferable). | 2-3 hrs | Not started — depends on Phase 2 | P3 |
| graphify Phase 4 (graph-aware kb_lint) | KB health | Extend `kb_lint.py` with three checks: orphans (degree 0), god concepts (degree > 2σ, candidates for splitting), coverage gaps (high-degree concepts with no corresponding wiki article). | 1-2 hrs | Not started | P3 |
| graphify refresh: fill 13 missing chunks | KB completeness | 13 chunks (mostly lennys-podcast tail files 116-123) missing from Phase 1 because the Claude Code subscription rate limit hit mid-run. Cache is empty so naive `--update` would re-extract everything. Need a strategy that only hits the missing file list — either manually stage the missing files, or pre-populate graphify's SHA256 cache from the salvaged chunk files. Revisit when Phase 2 soft-domain pass needs the coverage. | 1-2 hrs | Deferred — not a blocker | P3 |
| graphify god_nodes filter hardening | Leo quality | Current filter catches 19/20 top concepts correctly. Gap: podcast guests whose names aren't in any node's `author`/`contributor` field AND whose source filename doesn't contain their slug will slip through. Only revisit if another false positive shows up in Phase 2. | 30 min | Acceptable as-is | P4 |
| graphify HTML viz at full scale | Leo quality | graphify's `to_html` caps at 5000 nodes. Current `graph.html` is the degree≥2 subgraph (4,584 of 6,706 nodes). Consider: per-community HTML exports, or a custom viz. Gitignored anyway — low urgency. | 2-3 hrs | Not started | P3 |
| Preserve raw graphify chunks durably | Phase 3 enabler | `/tmp/graphify-phase1/graphify-out/.graphify_chunk_*.json` are the only place the raw pre-consolidation extraction lives (needed to regenerate surprising.json, and potentially for future entity-resolution experiments). If /tmp gets wiped, a full rebuild is required. Copy to `kb/.kb/graph/raw_chunks/` (gitignored) if we expect to re-run `compute-surprising` or iterate on the consolidation algorithm. | 15 min | Not started | P2 |
| Soft wiki compile | KB value unlock | Run `/kb-compile --domain soft` on 1,556 raw articles (Lenny's, Wes Kao, Ethan Evans, Jefferson Fisher). **Note:** graphify Phase 2 will likely drive this (graph-fed scan over soft raw). | 3-4 hrs | Not started — blocked on graphify Phase 2 (now P2) | P2 |
| KB lint cleanup | KB quality | Fix broken wikilinks, review near-duplicate slugs. ~~791 thin articles are RSS stubs~~ **Fixed 2026-04-05 — all stubs rescraped**. 1,432 missing tags are Lenny extractions. | 1 hr | Wikilinks + slug dedup remaining | P2 |
| YouTube transcript ingestion | KB content | 16 videos queued in `scripts/yt_backlog.json`. Script: `scripts/yt_ingest.py --retry`. 1 video has no subtitles. Run locally on-demand. | 15 min | Pipeline built, pending IP cooldown | P0 |
| Overnight KB automation | KB automation | Two remote triggers exist but disabled (cost): Daily KB Scout (`trig_017ew...`), Overnight KB Work (`trig_0132A...`). Re-enable via Leo when ready. On-demand for now. | Done | Disabled | P1 |
| Schedule cron jobs for KB scrapers | KB automation | ~~Wire `scrape_aman.py` (weekly) and `scout.py` (daily) into cron.~~ Replaced by Daily KB Scout remote trigger (currently disabled). | — | Done | — |
| Download and hook up open-source LLM | Cost savings, local inference | Find best model for James's PC, set up ollama/llama.cpp, wire into KB scripts as alternative to `claude -p`. | 2-3 hrs | Not started — need to check VRAM/RAM | P1 |
| KB semantic search fallback | KB quality | Sentence-transformer embeddings as fallback when TF-IDF confidence is low. Depends on local LLM infra. Reference: Louis Wang's `llm-knowledge-base` uses all-MiniLM-L6-v2. | 2 hrs | Not started — blocked on local LLM | P2 |
| Better context structure | Leo efficiency | Audit CLAUDE.md and context files for optimal loading. Minimize context waste. | 2 hrs | Not started | P2 |
| Recommendation system from scratch | ML craft, interview artifacts | Build recsys from first principles: embeddings → two-tower → training → eval → serving. `projects/recsys-from-scratch/` | 20+ hrs | Not started | P2 |
| Investigate kuberwastaken/claude-code | Leo improvement ideas | Explore patterns, prompt engineering, automation approaches. Cloned at `/home/james/src/claude-code-reference/` | 1-2 hrs | Not started | P3 |
| Fix consult-notebook agent live querying | Leo quality | The consult-notebook subagent is synthesizing from prior context instead of actually hitting NotebookLM via MCP. **Second confirmed instance 2026-04-09** — Coaching Patterns spawn on Roberto dynamic returned a synthesis of conversation context; verified zero calls to `mcp__notebooklm__*` tools. First instance 2026-04-07 (Coaching Patterns + Wes Kao). Bug is persistent — happens every time the consult-notebook subagent is spawned. Investigate `.claude/agents/consult-notebook.md` for MCP tool invocation + SKILL_INSTRUCTIONS wiring. | 1-2 hrs | Not started — **bumped P2 → P1 on 2026-04-09** after second confirmed instance | P1 |
| Integrate GSD for side projects | Workflow | Explore `get-shit-done` framework. Does it complement Leo? | 1 hr | Not started | P3 |
| Interview-prep mode | Career optionality | Framework for side projects that double as interview prep for OpenAI/Anthropic. Folded into Track 3 + blog posts. | 2 hrs | Subsumed by Track 3 + Write items | P3 |

## Work
Pinterest deliverables, stakeholder actions, team tasks.

| Item | Why / Goal | Description / Subtasks | Rough Time | Progress | Priority |
|------|-----------|----------------------|------------|----------|----------|
| Feed Pinsight M1 spec into work-Leo | G2 (Pinsight) | Start T-1 (scaffold) and T-2 (SQLite traces) on Monday. Spec at `work+self/projects/pinsight-m1-spec.md`. **Forward-looking roadmap at `work+self/projects/pinsight-agentic-vision.md`** (6-phase trajectory through agentic augmentation; Fork A commitment to Phase 4 simulation harness). **Darren confirmed staffing contributors + Director promo official 4/16. Dylan brokered Reflex invitation 4/09. Pinsight confirmed more urgent than PINvestigator Eval.** James targets M0 by end of week (2026-04-11), log validation by Monday (2026-04-14). | 2-3 hrs | **Active — M0 target EOW 2026-04-11** | P0 |
| Pinsight research synthesis | G2 (Pinsight) | ~~Comprehensive review of 5 agentic recsys papers + vision doc + paper summaries.~~ **Done 2026-04-05** — `work+self/projects/pinsight-agentic-vision.md`, `kb/hard/raw/AgenticRecommendations/summaries.md`. | 3 hrs | Done | — |
| Share HF funnel table schema with Alok | G2 (Pinsight) | Alok is building the logging. Needs proposed schema for alignment. | 15 min | Not started — Monday | P0 |
| Port agents/skills/hooks to work-leo | Leo deployment | Use `work-leo-setup/TRANSFER.md`. Agents are direct copies with path updates. | 1-2 hrs | Not started | P1 |
| Update work-leo CLAUDE.md | Leo deployment | Add subagent dispatch section + session log restructure. | 30 min | Not started | P1 |
