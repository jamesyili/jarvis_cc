# Backlog

> Unified backlog: everything actionable in one place. Organized by what James does, not what system it lives in. Curriculum details live in `learning/learning_agenda.md` — this file tracks what to do next.

**Last updated:** 2026-04-05 late night PST

---

## Write
Blog posts, technical memos, opinions — synthesis artifacts where James wrestles with material in his own words.

| Item | Why / Goal | Description / Subtasks | Rough Time | Progress | Priority |
|------|-----------|----------------------|------------|----------|----------|
| Pretrain-finetune in recsys | G1 (UPP), technical depth, interview prep | Survey the pretrain+finetune paradigm in recsys. Cover CLR architecture, what's pretrained vs fine-tuned, why this paradigm, UPP angle, predictions. See `blog/pretrain-finetune-recsys.md` | 3-4 hrs | Not started | P0 |
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
| Soft wiki compile | KB value unlock | Run `/kb-compile --domain soft` on 1,556 raw articles (Lenny's, Wes Kao, Ethan Evans, Jefferson Fisher). | 3-4 hrs | Not started — plan phase needed | P1 |
| KB lint cleanup | KB quality | Fix broken wikilinks, review near-duplicate slugs. ~~791 thin articles are RSS stubs~~ **Fixed 2026-04-05 — all stubs rescraped**. 1,432 missing tags are Lenny extractions. | 1 hr | Wikilinks + slug dedup remaining | P2 |
| YouTube transcript ingestion | KB content | 16 videos queued in `scripts/yt_backlog.json`. Script: `scripts/yt_ingest.py --retry`. 1 video has no subtitles. Run locally on-demand. | 15 min | Pipeline built, pending IP cooldown | P0 |
| Overnight KB automation | KB automation | Two remote triggers exist but disabled (cost): Daily KB Scout (`trig_017ew...`), Overnight KB Work (`trig_0132A...`). Re-enable via Leo when ready. On-demand for now. | Done | Disabled | P1 |
| Schedule cron jobs for KB scrapers | KB automation | ~~Wire `scrape_aman.py` (weekly) and `scout.py` (daily) into cron.~~ Replaced by Daily KB Scout remote trigger (currently disabled). | — | Done | — |
| Download and hook up open-source LLM | Cost savings, local inference | Find best model for James's PC, set up ollama/llama.cpp, wire into KB scripts as alternative to `claude -p`. | 2-3 hrs | Not started — need to check VRAM/RAM | P1 |
| KB semantic search fallback | KB quality | Sentence-transformer embeddings as fallback when TF-IDF confidence is low. Depends on local LLM infra. Reference: Louis Wang's `llm-knowledge-base` uses all-MiniLM-L6-v2. | 2 hrs | Not started — blocked on local LLM | P2 |
| Better context structure | Leo efficiency | Audit CLAUDE.md and context files for optimal loading. Minimize context waste. | 2 hrs | Not started | P2 |
| Recommendation system from scratch | ML craft, interview artifacts | Build recsys from first principles: embeddings → two-tower → training → eval → serving. `projects/recsys-from-scratch/` | 20+ hrs | Not started | P2 |
| Investigate kuberwastaken/claude-code | Leo improvement ideas | Explore patterns, prompt engineering, automation approaches. Cloned at `/home/james/src/claude-code-reference/` | 1-2 hrs | Not started | P3 |
| Integrate GSD for side projects | Workflow | Explore `get-shit-done` framework. Does it complement Leo? | 1 hr | Not started | P3 |
| Interview-prep mode | Career optionality | Framework for side projects that double as interview prep for OpenAI/Anthropic. Folded into Track 3 + blog posts. | 2 hrs | Subsumed by Track 3 + Write items | P3 |

## Work
Pinterest deliverables, stakeholder actions, team tasks.

| Item | Why / Goal | Description / Subtasks | Rough Time | Progress | Priority |
|------|-----------|----------------------|------------|----------|----------|
| Feed Pinsight M1 spec into work-Leo | G2 (Pinsight) | Start T-1 (scaffold) and T-2 (SQLite traces) on Monday. Spec at `work+self/projects/pinsight-m1-spec.md` | 2-3 hrs | Not started — Monday | P0 |
| Share HF funnel table schema with Alok | G2 (Pinsight) | Alok is building the logging. Needs proposed schema for alignment. | 15 min | Not started — Monday | P0 |
| Port agents/skills/hooks to work-leo | Leo deployment | Use `work-leo-setup/TRANSFER.md`. Agents are direct copies with path updates. | 1-2 hrs | Not started | P1 |
| Update work-leo CLAUDE.md | Leo deployment | Add subagent dispatch section + session log restructure. | 30 min | Not started | P1 |
