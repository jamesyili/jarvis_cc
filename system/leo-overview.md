# Leo — James Li's Personal Operating System

> Portable context document. Describes what Leo is, what it does, and how it was built. Intended for use in Claude Desktop or any Claude instance that doesn't have access to the Leo repo.

Last updated: 2026-04-05

---

## What Leo Is

Leo is a personal operating system built by James Li using Claude Code (Anthropic's CLI agent). It runs as a persistent, file-backed system in a git repo (`~/src/leo`) on James's PC (WSL2/Ubuntu). Leo serves as chief of staff, thinking partner, coach supplement, writer, and knowledge system operator.

Leo is not a single prompt — it's an architecture of 15+ skills, 5 agents, 4 hooks, a 2,600+ article knowledge base, and a structured context file system that gives Claude deep, persistent context about James's work, goals, relationships, and growth patterns.

## Who James Is

Senior Engineering Manager at Pinterest, Homefeed Candidate Generation team. 17 direct reports across 10 workstreams. Di DISC profile (D:88%, i:88%) — fast, direct, high-energy, vision-driven. Driving toward Director-caliber (M18) impact.

Works with two coaches: David (strategy/politics) and Rodney (mindset/emotional regulation). Core growth edges: managing a status sensor that converts comparison into identity crisis, brevity under pressure, executive presence in senior rooms.

Technically: ML/AI, recommendation systems, retrieval architecture. Builds hands-on with LLMs (PINvestigator — an agentic metrics investigation tool, and Leo itself). FIRE-ready financially — comp comparisons are status-driven, not material.

---

## System Architecture

### Context Files (`work+self/`)

Structured markdown files that Leo reads before engaging on anything substantive:

- **`goals.md`** — Ranked goals G0-G5 with bets, leading indicators, risks. G0 is inner resilience (the foundation), G1 is retention-focused business outcomes, G2 is agentic AI craft, G3 is scaling through others, G4 is executive presence, G5 is interview readiness/optionality.
- **`coaching.md`** — Full coaching session log with 8 named tools (Tai Chi base, Signal Not Truth, Three-Beat Managing Up, etc.). This is the emotional regulation playbook.
- **`communication.md`** — DISC profile, blindspots, audience playbooks, 6 speaking patterns to watch for, pre-presentation checklist.
- **`journals_and_growth.md`** — Synthesized lessons on top, chronological journal entries below. The journal is where raw experience gets processed into growth patterns.
- **`people/stakeholders.md`** — 21 stakeholder profiles with trust state, DISC, operating plans, risks.
- **`people/direct_manager.md`** — Deep relationship audit of Dylan (James's manager) — trust arc, user manual, Director gap analysis.
- **`projects/`** — Specs for UPP (unified retrieval platform), Pinsight (agentic debugger), PINvestigator, Retentive Recs, and technical references.

### Skills (24 total)

Skills are slash commands (`/skill-name`) with their own `SKILL.md` instruction files. They load only when invoked (lazy loading). Organized by function:

**Session management:**
- `/start-session` — Reads session logs + backlog, grills James on goals until aligned
- `/end-session` — Grills for capture (decisions, open items), writes session log, commits and pushes
- `/pulse` — 30-second orientation: what's on track, drifting, needs attention
- `/weekly-review` — Weekly digest with patterns and action items
- `/context-update` — Guided update of context files when information changes

**Thinking & coaching:**
- `/thinking-partner` — Strategic thought partnership
- `/grill-me` — Relentless interviewing on a plan until shared understanding
- `/coach-check` — Review a draft/situation against coaching frameworks (brevity, emotional regulation, executive presence, managing up)
- `/consult-notebook` — Query NotebookLM research notebooks

**Communication:**
- `/prep` — Pre-meeting preparation with stakeholder profiles and talking points
- `/debrief` — Post-meeting intel extraction and context updates
- `/draft-email` — Draft messages calibrated to recipient

**Knowledge base (7 skills):**
- `/kb-status`, `/kb-ingest`, `/kb-scout`, `/kb-lint`, `/kb-compile`, `/kb-merge`, `/kb-reflect`

### Agents (4)

Custom subagents in `.claude/agents/` that run as isolated subprocesses:

| Agent | Purpose |
|-------|---------|
| **Consult-Notebook** | Queries NotebookLM notebooks in isolation — keeps verbose NLM results out of main context. Spawns on keyword triggers (managing up → Wes Kao, venting → Coaching Patterns, decisions → Decisive, system design → ML notebook). Appends raw response to `notebooklm/query_log.md` as audit trail. **Rewritten 2026-04-11** to fix persistent context-synthesis bug. |
| **Karen** | Adversarial strategic advisor. Fires every ~20% context window. Challenges blind spots, names patterns James is avoiding, proposes alternatives. Maintains her own observation file. |
| **Code Planner** | Implementation architect. Grills on design decisions, then produces structured spec with task IDs and acceptance criteria. |
| **Search** | Searches across KB articles and context files with context isolation. |

### Hooks (4)

Shell scripts that fire automatically on Claude Code lifecycle events:

- **SessionStart** — Auto-loads last session context into every new conversation
- **PreCompact** — Logs context compaction events, injects recovery instructions
- **Stop (suggest-compact)** — Nudges compaction at 50+ tool calls
- **Stop (detect-corrections)** — Parses for correction patterns, prompts memory creation

### Knowledge Base (`kb/`)

Two-domain Obsidian vault:
- **Hard skills** (`kb/hard/`) — ML, recsys, systems, technical craft. 821+ articles from Aman.ai, Eugene Yan, Lilian Weng, Karpathy, Chip Huyen, Sebastian Raschka, Nathan Lambert, Simon Willison, Cameron Wolfe, Jay Alammar, Louis Wang.
- **Soft skills** (`kb/soft/`) — Leadership, comms, product, coaching. 1,556+ articles from Lenny's Podcast (thematic extractions across 272 episodes), Wes Kao, Ethan Evans, Jefferson Fisher.

Each domain has two layers:
- **Raw** — Ingested articles by source (auto-populated by scout/scraper scripts)
- **Wiki** — Compiled concept articles synthesized across sources (generated by `/kb-compile`)

Automation: `scout.py` checks 13 RSS sources, `scrape_aman.py` and `scrape_louis.py` handle full-content scraping, `kb_search.py` provides TF-IDF keyword search, `kb_lint.py` runs health checks.

### NotebookLM Integration

Four curated research notebooks queryable via MCP:

| Notebook | Domain |
|----------|--------|
| Wes Kao Frameworks | Exec comms, strategic framing, managing up |
| Coaching Patterns | Emotional regulation, executive presence, leadership |
| Decisive Framework | Decision-making, cognitive biases, strategic planning |
| ML & AI System Design | ML system design, GenAI, LLMs, RAG, RecSys |

### Memory System

Persistent file-based memory at `.claude/projects/.../memory/`. Four types:
- **User** — James's profile and preferences
- **Feedback** — Corrections and confirmed approaches (what to avoid/repeat)
- **Project** — Active decisions, priorities, strategic direction
- **Reference** — Pointers to external systems (NotebookLM IDs, repos, tools)

MEMORY.md index loads automatically into every conversation.

### Session Continuity

Individual session log files in `system/session-logs/` (one per session, named by date). 25 sessions logged since March 27, 2026. The SessionStart hook auto-loads the latest entry. `/start-session` and `/end-session` skills manage the full session lifecycle.

Unified backlog at `backlog.md` — four categories (Write, Learn, Build, Work) with priorities, progress, and time estimates.

---

## How Leo Is Actually Used (ranked by frequency and impact)

1. **Meeting prep & stakeholder comms** — Mock Q&A, talking points, stakeholder message drafting, debrief extraction. The #1 value driver.
2. **Coaching & emotional regulation** — Status sensor management, journal entries, growth pattern recognition, coaching framework application.
3. **Strategic thinking partner** — Career strategy, org dynamics, project direction, trade-off analysis.
4. **Writing & drafting** — Messages to leadership, stakeholder updates, framing for exec audiences.
5. **Technical planning** — Implementation specs via Code Planner, architecture decisions.
6. **Building Leo itself** — Skills, agents, hooks, KB infrastructure.
7. **Knowledge base operations** — Ingestion, scouting, search, compilation.

---

## Key Patterns & Frameworks

These are the coaching tools and growth patterns that come up most often:

- **Tool 8: "Signal, not truth"** — When the status sensor fires (comp comparison, promo anxiety, peer benchmarking), name it as a signal, locate it physically, redirect the energy to the internal scoreboard within 10 minutes.
- **Tai Chi Base (Tool 4)** — For absorbing external force. Return to center, don't react from the destabilized position.
- **Three-Beat Managing Up** — (1) Share what's hardest, (2) show how you're crushing it despite that, (3) enlist manager's help on what only they can unblock.
- **Internal Scoreboard** — Is PINvestigator better this week? Is the team energized? Am I learning something real? Am I recovering faster? Do I think I did good work?
- **Boring Consistency** — The behavioral shift from catalytic clarity (high heat, high light) to steady, reliable excellence (low heat, steady light). Zero instances of defensiveness or litigating the point.

---

## Current Goals (April 2026)

- **G0:** Inner foundation — emotional resilience, faster recovery from triggers
- **G1:** Retentive Recommendations — flagship retention-focused business outcome
- **G1.5:** UPP Retrieval platform — co-equal pillar with Dhruvil's ranking foundation
- **G2:** Agentic AI craft — PINvestigator, Pinsight, genuine hands-on expertise
- **G3:** Scale the org — TLs/EMs running things, EM hire in progress
- **G4:** Executive presence — brevity, calm, political fluency under pressure
- **G5:** Interview readiness — ML system design prep for optionality (not actively interviewing)

---

## What Makes Leo Different

Leo isn't a chatbot with a system prompt. It's a **persistent, file-backed operating system** where:

- Context survives across sessions via session logs, hooks, and memory files
- Skills provide specialized workflows that load only when needed
- Agents provide context isolation for expensive operations (NotebookLM queries, adversarial review)
- The knowledge base is a growing corpus that Leo can search, lint, compile, and synthesize
- Karen acts as an adversarial advisor who challenges James's blind spots and holds him accountable to his stated goals
- The coaching dimension is first-class — Leo reinforces patterns from real coaching sessions, not generic advice

The system was built incrementally over ~10 days (March 27 — April 5, 2026) through 25+ working sessions.
