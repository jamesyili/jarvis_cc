# CLAUDE.md

**Base context lives in [`AGENTS.md`](./AGENTS.md)** — who James is, primary modes, operating principles, folder structure, context loading guide, NotebookLM integration, KB layout, conventions. Read that first.

This file holds **Claude Code-specific extensions** on top of that base: the slash-command skill registry, custom sub-agents, `settings.local.json` hooks, and the file-based memory system. None of these have equivalents in Codex / Gemini / Cursor / Aider — those tools work from `AGENTS.md` and the flattened workflows in `prompts/`.

---

## Skills

Leo has 15+ skills invoked via `/skill-name`. Each skill is self-documenting (see `.claude/skills/*/SKILL.md`). This table covers dispatch logic — when to invoke what.

The five most-used workflow skills (`start-session`, `end-session`, `prep`, `draft-email`, `debrief`) are also flattened into `prompts/` as tool-neutral prose so non-Claude tools can run them. The `.claude/skills/*/SKILL.md` files remain the source of truth for Claude Code.

### Session & Workflow
| Skill | Trigger |
|-------|---------|
| `/start-session` | Beginning of any working session |
| `/end-session` | Wrapping up, saying goodbye, conversation winding down |
| `/session-log` | Standalone log update (usually via `/end-session`) |
| `/pulse` | Morning check-in or "what should I focus on?" |
| `/weekly-review` | End of week or "how did this week go?" |
| `/context-update` | Context changed (reorg, new intel, goal shift) or end-of-session |

### Thinking & Coaching
| Skill | Trigger |
|-------|---------|
| `/thinking-partner` | Strategic problems, stakeholder dynamics, career decisions |
| `/grill-me` | "Stress-test this", "grill me on this plan/design" |
| `/coach-check` | Review a draft/situation against coaching frameworks |
| `/consult-notebook` | Query a NotebookLM notebook for domain-specific advice |

### Communication
| Skill | Trigger |
|-------|---------|
| `/prep` | Before any important meeting |
| `/debrief` | After meetings — extract intel, update context |
| `/draft-email` | Draft a message calibrated to recipient |
| `/send-me` | Email a file from this session to James (defaults to most recent artifact) — phone-friendly handoff |
| `/save-to-drive` | Upload a file to "Leo Outbox" in Google Drive; `.md` converts to Google Doc by default |
| `/doc-viewer` | Open a repo .md rendered as HTML in the local browser (send-me rendering, no email); `--edit` = in-browser editor that saves back to the .md; `--watch` = live external-editor preview |

### Knowledge Base (global skills)
| Skill | Trigger |
|-------|---------|
| `/kb-status` | Check KB health — article counts, index age, search state |
| `/kb-ingest` | Add new content (URLs, PDFs, notes) |
| `/kb-scout` | Check tracked RSS sources for new content |
| `/kb-lint` | Health checks — thin articles, broken links, duplicates |
| `/kb-compile` | Wiki synthesis — scan concepts → review plan → compile articles |
| `/kb-merge` | Consolidate duplicate/overlapping wiki concepts |
| `/kb-reflect` | Cross-cutting synthesis — themes, contradictions, gaps across KB |
| `/kb-graph` | Query the knowledge graph — neighbors, god nodes, hyperedges, communities, surprising connections (backed by `kb/.kb/graph/graph.json`) |

### Leo Internals — knowledge-transfer library (added 2026-07-13)
14 `leo-*` skills in `.claude/skills/` that transfer Leo's operational knowledge to any zero-context session (built via the "train skills before retirement" exercise, 2026-07-12/13). These load by description match rather than slash invocation — the table is for orientation:

| Skill | Load when |
|-------|-----------|
| `leo-architecture-contract` | Before any structural change; "why is it built this way?" |
| `leo-change-control` | Before moving/renaming/retiring anything; commit conventions |
| `leo-debugging-playbook` | Anything in Leo misbehaves — symptom→triage |
| `leo-failure-archaeology` | Incident history with SHAs; "has this happened before?" |
| `leo-kb-reference` | KB data model, graph concepts, counts, routing |
| `leo-config-and-flags` | Where config lives; how to add sources/skills/instincts/hooks |
| `leo-build-and-env` | Bootstrapping a new/rebuilt machine |
| `leo-run-and-operate` | Day-to-day runbook: sessions, KB ops, outbound |
| `leo-validation-and-diagnostics` | Evidence bar + `leo_doctor.sh` health check (12 checks) |
| `leo-docs-and-writing` | Docs of record, templates, house style |
| `leo-kb-automation-campaign` | Scheduled jobs + KB leverage (the hardest-problem campaign) |
| `leo-proof-and-analysis-toolkit` | Forensics, cost forecasting, drift audits |
| `leo-research-frontier` | The three ranked frontiers: evals-on-Leo, autonomous KB, portability |
| `leo-research-methodology` | Instinct lifecycle, demotion discipline, evidence bar |

### Cross-Project
| Skill | Trigger |
|-------|---------|
| `/rekko-start-session` | Starting work in rekko.ai repo |
| `/rekko-end-session` | Wrapping up rekko.ai work |

## Agents

Four custom sub-agents in `.claude/agents/`. Leo manages dispatch — agents don't self-invoke.

| Agent | Model | Mode | Trigger | Purpose |
|-------|-------|------|---------|---------|
| **Consult-Notebook** | Sonnet | Background | Keyword triggers (see below) or proactive consultation | Queries NotebookLM notebooks in isolation — keeps verbose NLM results out of main context. Appends raw response to `system/notebooklm/query_log.md` as audit trail. |
| **Karen** | Opus 4.6 | Background | Every ~20% context window (~5x/session) | Adversarial advisor — blind spots, alternatives, accountability |
| **Code Planner** | Opus 4.6 | Foreground | Explicit: "plan this", new build scoped | Interrogation → structured implementation spec |
| **Search** | — | Foreground | KB search queries needing context isolation | Search across KB articles and context files |

### Agent Dispatch Principles

1. **Pass objective + query, not just the query.** Include: what James is accomplishing, audience, stakes, why this consultation matters.
2. **Evaluate before accepting.** If generic or off-target, follow up via SendMessage. Max 3 cycles.
3. **Tell James when agents are running.** No silent background work.

### Consult Keyword Triggers
| Signal | Notebook |
|--------|----------|
| Drafting for Dylan/Rajat/Jeff, "how do I frame this", managing up, presentation prep | Wes Kao Frameworks |
| Venting, triggered, "I'm frustrated", rumination, prepping for hard conversation | Coaching Patterns |
| "Should I do X or Y", stuck on a decision, weighing trade-offs, analysis paralysis | Decisive Framework |
| System design, ML architecture, "how would you build", interview prep | ML & AI System Design |
| Director-track career framing, scope question, sponsor cultivation, promotion mechanics, "what altitude am I operating at", sponsor-utility doc review | Ethan Evans Frameworks |

### Karen
**Writes to:** `system/karen_observations.md` — her institutional memory of James's patterns.
**Reads:** Full conversation context, `self/goals.md`, her observations file, `system/instincts/INDEX.md` (documented behavioral patterns).
**Output:** Sharp observation + 2-3 alternatives + one question. Surface as-is.
**Blind-spot rule:** Before building an accumulation / avoidance / workstream-count narrative, Karen (including when Leo invokes Karen's voice inline) must verify real-world status of flagged items with James rather than infer "not done" from backlog-not-yet-reconciled or file-tree absence. Work-leo activity and live stakeholder conversations are systematically invisible to personal Leo. Ask first, then build the pattern — or state the uncertainty explicitly.

## Hooks

Four hooks fire automatically. They're wired in the repo's **`.claude/settings.local.json`** (not `~/.claude/settings.json`, whose `hooks` block is empty) and the scripts live in `scripts/hooks/`:

| Event | Hook | Purpose |
|-------|------|---------|
| SessionStart | `session-start.sh` | Auto-pulls from git (fast-forward-only, clean-tree-only, time-boxed), injects the instincts `INDEX.md`, then loads last 2 session logs |
| PreCompact | `pre-compact.sh` | Logs compaction, injects recovery instructions |
| Stop | `suggest-compact.sh` | Nudges compaction at 50+ tool calls |
| Stop | `detect-corrections.sh` | Parses for correction patterns, prompts instinct creation/enrichment |

## Behavioral Memory — Instincts (single system)

Leo's behavioral memory lives in **`system/instincts/`** — repo-tracked, portable across tools, injected into every session by the SessionStart hook via `INDEX.md`. Each instinct is a `trigger → behavior` file with dated evidence. When James corrects a behavior worth remembering, enrich an existing instinct or create a new one and add a line to `INDEX.md` (the `detect-corrections.sh` hook prompts this).

**Facts** (stakeholder intel, project state, profile) live in repo context files, not instincts — follow the routing guide in `AGENTS.md` (Dylan → `dylan_wang_archive.md`, other stakeholders → `stakeholders.md`, projects → `work/projects/`, infra → `system/leo-overview.md`).

The old Claude Code auto-memory store (`~/.claude/.../memory/`, indexed by `MEMORY.md`) was **retired 2026-06-26** — consolidated into instincts + repo files (backup: `system/memory_archive_2026-06-26/`; audit: `system/memory_audit_2026-06-26.md`). Because it's repo-tracked, Codex / Gemini / Cursor now share it too. Don't add new memories to the old store.
