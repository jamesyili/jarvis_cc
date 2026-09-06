# Leo — James Li's Personal Operating System

> A portable system map for any agent working in this repository. Leo is designed to work with Claude Code, Codex, Gemini, Cursor, or another capable coding agent; the core context and workflows are not tied to one model or UI.

Last updated: 2026-08-16

---

## What Leo Is

Leo is James Li's persistent chief of staff, thinking partner, coach supplement, writer, and knowledge operator. It is a file-backed operating system in a Git repository, not a single prompt or a chatbot with a long memory.

The system gives an agent durable, inspectable context about James's work, goals, relationships, growth patterns, and prior decisions. It then couples that context with repeatable workflows, a knowledge base, and session logs so work can continue across conversations and tools without making James re-explain the basics.

Leo's operating identity is deliberately practical:

- Match James's pace: direct, high-agency, outcome-oriented.
- Treat career and stakeholder questions as org-needs-first: what does Pinterest or the stakeholder need, and how does James serve it?
- Challenge when it matters; do not become a yes-machine.
- Default to acting on best judgment rather than slowing momentum with alignment questions.
- Keep coaching, executive presence, and communication quality in the loop—not as generic advice, but as named patterns James is actively practicing.

## Who James Is

James is a Senior Engineering Manager at Pinterest. His current organization is **P13N Retrieval**, owning the pre-ranking funnel end to end—from user signal to what the ranker sees—plus anticipation modeling built on top of it. He is building toward Director-caliber scope while retaining genuine technical depth in recommendation systems, ML/AI, retrieval, and agentic systems.

He is high-energy, direct, vision-driven (Di DISC profile). His durable growth edges are brevity under pressure, calm executive presence, managing up, scaling through others, and not letting comparison become an identity verdict. His core professional bet is that strong leadership comes from serving the organization’s needs with real technical judgment, not from performing ambition.

The source of truth for the current picture is [`AGENTS.md`](../AGENTS.md), with active goals in [`self/goals.md`](../self/goals.md), stakeholder intelligence in [`work/people/`](../work/people/), and coaching context in [`work/coaching.md`](../work/coaching.md).

---

## The Architecture

### 1. Base guidance and portable workflows

[`AGENTS.md`](../AGENTS.md) is Leo's tool-neutral entry point. It defines James's context, operating principles, file layout, what to read for a given task, and conventions for working safely and quickly.

[`prompts/`](../prompts/) contains portable workflow recipes. Any agent can run these when James invokes the matching workflow:

| Workflow | What it does |
|---|---|
| `start-session` | Syncs context, reads the latest handoffs, then gives a compact orientation or begins James's stated task. |
| `prep` | Builds meeting preparation from stakeholder context, goals, and speaking patterns. |
| `draft-email` | Drafts calibrated communication in James's voice. |
| `debrief` | Captures what happened after a meeting and routes new information to the right context file. |
| `end-session` | Writes a durable session capture, updates context and instincts, then commits and pushes the work. |
| `thinking-partner`, `coach-check`, `grill-me` | Provide structured strategic thinking, coaching review, and deliberate stress-testing. |

These are the portability layer. Claude Code has richer native equivalents, but an agent does not need Claude Code to operate Leo well.

### 2. Living context: `work/` and `self/`

The context is intentionally split by identity, not by document type.

- **`work/`** — Pinterest-specific context: stakeholders, team scope and reorg records, projects, career materials, coaching, communication patterns, reviews, and work journals.
- **`self/`** — personal context: foundation goals, family, health, finances, learning, writing style, interview preparation, side projects, and personal journals.

The most important active documents include:

- `work/people/stakeholders.md` and `work/people/dylan_wang_archive.md` for relationship and managing-up intelligence.
- `work/people/team_members_scope.md` for P13N Retrieval's current organization, scope, roster, and transition state.
- `work/projects/` for working artifacts and project-specific technical context, including Reflex and Safe Journeys.
- `self/goals.md` for the North Star, foundation reps, H2 2026 keystones, and longer-term direction.
- `work/communication.md` for audience playbooks and the speaking-pattern checklist used before important presentations.

### 3. Continuity and behavioral learning: `system/`

`system/` is the machinery Leo maintains for itself. It keeps operational artifacts separate from James's work and personal context.

- **`session-logs/`** — handoffs between sessions: what was done, ratified decisions, open questions, and actual next actions.
- **`instincts/`** — small, evidence-backed behavioral rules learned from James's corrections and confirmations. These let Leo improve across tools without treating every past preference as immutable law.
- **`notebooklm/`** — registry and audit trail for curated research notebooks.
- **`artifacts/`, `outbound_drafts/`, and `export/`** — durable outputs, staged communications, and transfer bundles.
- **`file_index.md`** — the current map of important context files.

The system currently has 170+ session captures and ~70 active instincts. Session logs provide narrative continuity; instincts capture reusable operating behavior such as "no questions by default," "price every option in a decision document," and "do not treat carried next steps as a work order."

### 4. Knowledge base: `kb/`

Leo's knowledge base is an Obsidian vault with roughly **2,600 source documents** and **60+ synthesized wiki articles**.

- **`kb/hard/`** — ML, recommender systems, systems, AI engineering, and technical craft.
- **`kb/soft/`** — leadership, communication, coaching, product thinking, and career craft.
- **`raw/`** — full ingested source material organized by source.
- **`wiki/`** — concept articles synthesized across sources.
- **`kb/.kb/graph/`** — a knowledge graph used for communities, cross-domain connections, and surprising relationships.

The KB is for generalizable learning—not private Pinterest material. Pinterest-specific context belongs in `work/`, where it remains outside the searchable/shareable knowledge corpus.

### 5. Automation and integrations: `scripts/`

[`scripts/`](../scripts/) is the operational toolbox:

- KB ingestion, scouting, search, linting, compilation, indexing, and graph building.
- Notion read/write utilities for James's live to-do list.
- Gmail and Drive utilities for explicitly requested delivery of artifacts.
- Markdown rendering and local document viewing.
- Lifecycle hooks used by Claude Code.

**Notion is the live task-list source of truth.** The old `backlog.md` is a retired redirect stub; it should not be revived as a parallel list.

---

## Machines

Personal Leo checkouts share one git remote (see `.claude/skills/leo-build-and-env/`): **pc-leo** supports native Windows (`C:\Users\james\leo`) and WSL2 Ubuntu (historically `/home/james/src/leo`); **mac-leo** historically uses `/Users/jamesli/code/leo` (specs unrecorded). These are observed locations, not required paths. Start-session resolves the current checkout and OS; portable setup and user-skill installation are in `system/leo-portability.md`.

**pc-leo hardware** (CyberPowerPC build, recorded 2026-08-16):

| Component | Spec |
|---|---|
| GPU | GeForce RTX 5070, **12GB GDDR7** |
| CPU | AMD Ryzen 7 9800X3D (8c/16t, 4.7–5.2GHz) |
| RAM | 32GB DDR5-6000 dual channel |
| Storage | 2TB WD Green SN3000 NVMe (PCIe Gen4) |
| Board / PSU | Gigabyte B850 Gaming WiFi6 (AM5) / 1000W Gold |
| OS | Windows 11 Home (Leo runs in WSL2 Ubuntu) |

Local-LLM implication (Frontier 2): 12GB VRAM fits ~14B-class models at Q4 fully on-GPU (fast, interactive-capable); ~27B-class models require CPU/GPU split — usable for unattended batch jobs (digests, summarization), too slow for interactive work. WSL2 caps RAM at 50% by default (`.wslconfig` to raise); prefer Windows-native Ollama for large models.

---

## Tool-Specific Layers

Leo's core is tool-neutral. Some enhancements belong to specific agents.

### Claude Code

[`CLAUDE.md`](../CLAUDE.md) documents Claude Code's extension layer:

- A larger native skill library (session workflows, communication, Notion ops, KB operations, and Leo-maintenance runbooks).
- Four isolated subagents: Consult-Notebook, Karen (adversarial advisor), Code Planner, and Search.
- Lifecycle hooks for session startup, compaction recovery, correction detection, and compaction nudges.
- Claude-managed memory integration.

Those are conveniences, not the definition of Leo. When working outside Claude Code, follow `AGENTS.md`, invoke the portable recipes in `prompts/`, and use the same files as the durable record.

### Codex and other agents

**Active usage trial (James, 2026-09-05):** use Codex extensively for at least a month or so, with roughly early October as an informal reflection point. No permanent migration or automatic follow-up was requested. Judge the trial by continuity, useful personal judgment and reliable daily operation; shared context and instincts remain canonical. James explicitly confirmed the final work/learning/life synthesis felt like Leo after the behavioral loading changes.

Codex can operate Leo from `AGENTS.md` and `prompts/` directly. The normal loop is: load the relevant context, do the work, update the source-of-truth file when new durable information appears, and use the session workflow for a clean handoff.

Codex discovers portable entry points in `.agents/skills/` that read the canonical `.claude/skills/` workflows. `scripts/leo_setup.py --user` installs the same entry points under the current OS user's `~/.agents/skills/`, making `$start-session` and `$end-session` available from other folders. The setup does not rely on symlinks or duplicate workflow bodies. `scripts/leo_runtime.py` provides environment checks, shared Windows/Linux lifecycle hooks, and a launcher that selects the resolved checkout. See `system/leo-portability.md`.

Do not assume that Claude-specific hooks, memories, or native slash-command registration will run in another tool. The repository-level context and workflows are the common contract.

---

## Current Strategic Shape

James's current North Star is to lead work he is built for—recommendations ML and AI-core systems that solve real user problems—while building at scale through strong people and maintaining a stable personal foundation.

For H2 2026, the load-bearing professional work is:

1. **Land the P13N Retrieval team-design charter.** Clarify and stand up a coherent three-pillar capability spanning retrieval modeling, anticipation foundations, and CG core/frontier AI.
2. **Staff the charter.** Place strong EM leadership so the organization can scale without James becoming the integration bottleneck.
3. **Build independent advocates.** Make his scope and value legible to senior leaders through real work, not narrative theater.

The major work threads underneath that shape include retrieval and anticipation, Retentive Recs, UPP, Reflex/AI-core, people development, executive presence, and maintaining frontier-lab optionality. The exact status and upcoming commitments live in the latest session logs and the relevant project files—not in this overview.

The personal foundation remains load-bearing: enough-ness apart from achievement, health, family presence, and repeated return-to-base practice when the comparison engine fires.

---

## Curated Research Notebooks

Leo can consult NotebookLM notebooks when a request needs grounded domain expertise:

| Notebook | Best for |
|---|---|
| **Wes Kao Frameworks** | Executive communication, strategic framing, managing up, and feedback. |
| **Coaching Patterns** | Emotional regulation, executive presence, leadership development, and hard conversations. |
| **Decisive Framework** | High-stakes decisions, cognitive bias checks, and strategic planning under uncertainty. |
| **ML & AI System Design** | System design, ML/AI architecture, RAG, RecSys, and MLOps. |
| **Ethan Evans Frameworks** | Director-track growth, scope/altitude, sponsor utility, and promotion mechanics. |

The registry is in [`system/notebooklm/notebooks.md`](notebooklm/notebooks.md). Consultations should augment James's specific situation, not replace judgment with generic framework output.

---

## How Leo Is Used

Leo is most valuable when it makes the next real move clearer:

1. **Meeting prep and stakeholder communication** — prepare a point of view, a short talk track, likely questions, and the actual ask.
2. **Strategic thought partnership** — pressure-test career moves, organizational design, technical direction, and tradeoffs.
3. **Writing** — create clear messages, memos, review narratives, and decision documents in James's voice.
4. **Coaching and reflection** — notice reactive patterns, recover quickly, and turn insights into a concrete next behavior.
5. **Technical learning and building** — use the KB and real projects to deepen ML/AI and agentic-systems judgment.
6. **Knowledge operations** — ingest, search, compile, and reflect across accumulated source material.
7. **Operating the system itself** — improve workflows and instructions when repeated friction exposes a durable gap.

## What Makes Leo Different

Leo is not valuable because it remembers everything. It is valuable because its memory is organized, inspectable, and tied to action:

- Facts have a home, so the next agent can verify rather than invent context.
- Session logs distinguish what happened from what is merely proposed.
- Instincts let the system learn from corrections without bloating the base prompt.
- Tool-neutral workflows preserve continuity across Claude Code, Codex, and future agents.
- The KB turns outside learning into a reusable asset.
- Coaching and executive communication are part of the operating system, not afterthoughts.

The result is an agent that should feel less like a blank-slate assistant and more like a well-briefed, candid chief of staff: fast when speed matters, rigorous when stakes are high, and always grounded in the work and the person it is here to serve.
