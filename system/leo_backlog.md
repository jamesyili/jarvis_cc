# Backlog

> All-purpose backlog: Leo improvements, side projects, research, learning, ideas. Prioritize ruthlessly — not everything here needs to happen.

Last updated: 2026-04-04

---

## Update work+self/org/organization.md

- [x] **Refresh the org chart** — Full leadership chain, Dylan's directs, Jeff's directs, team structure by workstream. *(done 2026-04-03)*


## Subagents to Build / Improve

- [ ] **Build `mgrep` skill** — Upgraded grep with smarter ranking, multi-term support, and relevance scoring. Once built, swap into the `search` subagent (`/Users/jamesli/code/leo/.claude/agents/search.md`) — replace the native `Grep` tool call with mgrep.

## Skills to Build

- [x] **`/prep`** — Pre-meeting preparation skill. Reads stakeholder profiles, recent context, generates talking points and watch-fors. *(done 2026-03-31)*
- [x] **`/pulse`** — 30-second landscape dashboard. Pulls goals, session log, tripwires, flags drift. Morning check-in or anytime orientation. *(done 2026-03-31)*
- [x] **`/debrief`** — Daily debrief. James dumps the day, Leo extracts signals, decisions, cross-meeting synthesis, updates context files. *(done 2026-03-29)*
- [x] **`/context-update`** — Guided update of context files when things change (reorg, new stakeholder, project pivot). Includes file index at `system/file_index.md`. *(done 2026-04-01)*

## Leo System Improvements

- [x] **Mid-session process notes** — PreCompact hook now logs compaction events and injects recovery instructions. *(done 2026-04-03)*
- [x] **End-session auto-propose context updates** — Replaced Phase 5 of end-session with `/context-update` integration. Runs after session log, scans for stale files, proposes updates, probes for gaps. *(done 2026-04-01)*
- [ ] **Better context structure** — Audit and restructure `AIContext/` for optimal loading. Questions to answer: Which files are loaded too often? Which are too large? Should CLAUDE.md be an index that points to context files loaded on-demand rather than describing everything inline? How to minimize context window waste while keeping Leo well-informed.

## Automation & Proactive Leo

- [x] **Cron scraper: aman.ai → KB** — Standalone scraper (`scripts/scrape_aman.py`) deposits into `kb/hard/raw/aman-ai/`, rebuilds index. Tested and working. *(done 2026-04-05)*
- [x] **Cron job: web scouring for James** — RSS-based scout (`scripts/scout.py`) checks all 12 tracked sources, deposits into correct `kb/{hard|soft}/raw/{slug}/`, rebuilds indexes. Tested and working. *(done 2026-04-05)*
- [ ] **Schedule cron jobs for scraper + scout** — Wire `scrape_aman.py` and `scout.py` into actual cron schedules (weekly aman, daily RSS scout). Could use Claude Code remote triggers or system cron.
- [ ] **Auto-restart extraction pipeline on frozen process detection** — The Lenny extraction pipeline kept dying from laptop lid closes. Could be improved with a smarter cron that checks CPU time delta and auto-restarts if no progress after 2 checks. Worth building into any future long-running batch scripts as a pattern.
- [ ] **Extraction second pass for promoted discovered themes** — After reviewing `learning/themes/_discovered.md` (710 passages), any themes worth promoting to seeds need a second systematic pass across all 272 episodes. Need a `--force-theme` flag or separate pass mode.

## Monetization & Side Projects

- [ ] **Integrate get-shit-done (GSD) for side projects** — Explore https://github.com/gsd-build/get-shit-done and figure out how to wire it into James's side project workflow. Questions: does it replace or complement Leo's session/backlog system? How does it fit with Claude Code? What's the right trigger for using it vs. freeform Leo sessions?
- [ ] **Interview-prep mode: OpenAI / Anthropic targeting** — Design a working style for side projects and learning that doubles as interview prep for OpenAI or Anthropic (likely PM/EM or technical leadership roles). Questions to resolve: what do these companies actually look for? What artifacts, decisions, and experiences are most signal-dense? How should James narrate his AI work (Leo, Pinvestigator, recsys) in an interview context? Build a lightweight framework Leo can apply to ongoing work — "does this compound toward the interview story?"

## Research & Investigation

- [ ] **Investigate kuberwastaken/claude-code** — Cloned to `/home/james/src/claude-code-reference/`. Explore what this project does, what patterns or ideas are worth borrowing for Leo. Look for: skill design patterns, prompt engineering techniques, automation approaches, anything that could level up Leo's architecture or workflows.
- [x] **Continue ECC deep-dive** — Remaining techniques from `system/ecc_techniques.md` not yet built: context modes (dynamic behavior switching), ~~layered CLAUDE.md rules directory~~, hook recipes (file size guards, config protection, desktop notifications), MCP context budget monitoring. Source: https://github.com/affaan-m/everything-claude-code *(done 2026-04-04)*

## Infrastructure

- [ ] **Download and hook up open-source LLM** — Find the best open-source model that fits James's PC, download it, and wire it into Leo's toolchain. Use for KB compilation, extraction, and other batch tasks to avoid burning Claude subscription tokens. Questions: which model (Llama 3, Mistral, Qwen?), what VRAM/RAM available, inference framework (ollama, vllm, llama.cpp?), how to swap between local and Claude in scripts.
- [ ] **KB semantic search fallback** — Add sentence-transformers (or local LLM) embedding-based semantic search as a fallback when TF-IDF keyword confidence is low. Depends on local LLM infra being in place. Design: keep `kb_search.py` interface stable so semantic layer slots in without changing how skills call it. Reference: Louis Wang's `llm-knowledge-base` uses all-MiniLM-L6-v2 with cosine similarity + cached embeddings.

## Learning & Craft Projects

- [ ] **Recommendation system codebase from scratch** — Create a dedicated folder where James and Leo collaboratively build a recommendation system from the ground up. Purpose: deepen James's hands-on ML craft, create interview-ready artifacts, and serve as a teaching tool. Could follow the CLR/P2P architecture James already understands but implement from first principles. Structure: `projects/recsys-from-scratch/` with progressive modules (embeddings → two-tower → training loop → eval → serving). Leo acts as pair programmer and teacher.
- [x] **NotebookLM deep integration** — Two parts: (1) Use existing notebooks more aggressively — "How to Speak" for presentation prep, "Improving Leo" for skill/prompt work. Make `/consult-notebook` a reflex, not an afterthought. (2) Create new notebooks for recsys, agentic AI, leadership. *(done 2026-04-04)*
