# Reflex Redesign — Process & Deliberation Log

**Purpose:** Capture the reasoning, branches considered, pushback absorbed, and decisions made during the Reflex redesign thinking sessions. Companion to `reflex_redesign.md` (target state) and `reflex_next_steps.md` (observations). This doc is the *journey*; the redesign doc is the *destination*.

---

## Session 1 — 2026-04-19 (Sunday morning, with Leo in thinking-partner mode)

**Context entering the session:** James had landed Steps 1-5 of viral_remix the prior day (2026-04-18d). Reflex Curator/Skeptic PR was scheduled to pre-share with Andrew + Dylan ~noon today. James opened this session by asking for a "strong technical plan for improving Reflex," grounded in `reflex_next_steps.md`, `pm_agent.md`, `ds_agent.md`, `quality_patterns.md` (1564 lines, 66 cycles).

### Initial problem framing

James's stated entry points:
- Reflex feels structurally inefficient, token-wise
- The codebase is confusing to navigate
- Wants mental clarity on what the system *should* ultimately look like before tackling how to propose it politically

Two framings were considered:
1. **Tactical plan** — absorb `reflex_next_steps.md`'s recommendations (CLAUDE.md fix, file split, retired playbooks) + sequence them.
2. **Structural redesign** — step back and ask if the whole architecture is the right shape.

James picked (2). The rest of the session operated in structural-redesign mode.

### Blind spots surfaced in `reflex_next_steps.md`

Leo's pushback on the existing doc — four gaps the doc didn't name:

| Gap | Why it matters | Doc's treatment |
|---|---|---|
| **A. No eval harness for Skeptic** | "Dry-run against 3 cards" is smoke test, not eval. Regressions go silent. | Listed as a must-do dry-run, not as a harness |
| **B. Open learning loop at the outcome end** | quality_patterns.md compounds on *comments*, zero trace to *shipped-experiment outcomes*. Gap 2 from 2026-04-18c. | Not mentioned |
| **C. Playbook rotation is allocation waste** | 66 cycles of conversion-rate signal exist; rotation ignores it. Dry wells get same share as high-converters. | Not mentioned |
| **D. Coverage is ad-hoc, not a portfolio concern** | PM Agent's Phase 0b checks surface balance per-cycle; a Cartographer agent would operate at portfolio level. | Not mentioned |

### Ranking pushback

`reflex_next_steps.md` calls the `quality_patterns.md` split the "highest-leverage structural change" (72% context reduction).

Leo pushed back: **eval harness is higher leverage.** Split is a one-time 72% win. Eval is a forever-win that protects every future change. Ranking revised:

1. Skeptic eval harness (forever-win)
2. quality_patterns.md split (one-time 72% win)
3. Typed contracts (correctness ratchet)
4. Outcome Learner (closes Gap 2)

### Pre-PR call-out (time-sensitive)

One change flagged as cheap and critical to include **before noon send today**:

**Skeptic must log every verdict in structured form from Cycle 67** — PASS/FAIL/NEEDS-HUMAN, per-check outcomes, fail reasons, confidence — not just annotations on the Asana card. Without structured verdict logs from day 1, Skeptic precision/recall can't be computed by Cycle 77, and the "block vs. advisory" question can't be answered with data. Cheapest, highest-leverage 20-minute pre-PR change.

*(Status as of doc write: flagged to James; he was evaluating whether to add before send.)*

### 3-tier plan emerged

Three tiers by cost and payoff horizon:

- **Tier 0 (this week):** verdict logging, cost ledger, CLAUDE.md reconcile, delete retired playbook files, placeholder-table discovery pass
- **Tier 1 (1-2 weeks):** Skeptic eval harness, quality_patterns.md split, retrieval over patterns, typed pydantic contracts
- **Tier 2 (2-4 weeks):** Outcome Learner, Cartographer, playbook bandit, Skeptic↔Curator mutual audit

### Pivot: "when do playbooks get called?"

James asked the concrete question. Answer delivered:
- PM Agent, Phase 2
- Reads `Playbook Rotation Tracker` (free text at bottom of `quality_patterns.md`)
- Picks next 3 from queue, can sub up to 1 for coverage gaps
- Loads the full text of those 3 playbook files (~100-240 lines each)
- 18 playbooks × 3 per cycle = 6-cycle rotation

**Are playbooks like skills?** Same *shape* (frontmatter + when-to-use + body) but **different invocation** — playbooks are prompt fragments the PM Agent reads and executes in-context, not independently callable tools. Better analogy: cookbook recipes. The PM Agent is the cook; playbooks are recipes on the shelf; 3 recipes per meal, 18 on the shelf.

### The inefficiency diagnosis

Per-cycle prompt budget decomposition:

```
~2700-3100 lines total
├─ Agent prompt (330)        ← orchestration + all-18-list mixed
├─ detect/CLAUDE.md (154)    ← static
├─ board_setup.md (320)      ← static
├─ quality_patterns.md (1564) ← 58% of budget, loaded regardless
├─ schemas (60-140)          ← static
└─ 3 playbooks (300-720)     ← the only actually dynamic part
```

The 58% spent on `quality_patterns.md` is the headline waste. Loaded every cycle in full even though most patterns don't apply to the 3 playbooks running.

### The navigation diagnosis — four tangled concerns

Four concerns live in the same files:

| Concern | Today | Should be |
|---|---|---|
| Orchestration (phases, decisions) | Inside agent prompts | Thin `agents/{a}/flow.md` |
| Domain knowledge (playbooks, patterns) | 18 files + 30+ prose entries | `capabilities/` with registries |
| Accumulated learning (patterns + dead ends) | One 1564-line file | Indexed pattern store, retrievable |
| Runtime state (rotation, logs, board) | Free-text in `quality_patterns.md` | Typed state files |

### Four-concern framework for every agent

Instead of one-file-per-agent that mashes everything together, every agent is built from four separable things:

1. **Role** — identity + I/O contract + invariants
2. **Capabilities** — named "moves" the agent can execute
3. **State** — what it reads/writes in shared world
4. **Flow** — phased execution of a run

This is the mental model that unlocks everything downstream. The current system's defining mistake is smashing all four into one or two big markdown files. The redesign separates them cleanly.

### Political framing — briefly considered, explicitly deferred

Leo asked: Andrew owns this? You own this? Fork locally? Three paths named:
1. You propose, Andrew owns, lands over multiple PRs
2. You ship the refactor as Phase 2 of your Reflex contribution
3. Fork structure locally for Skeptic/Curator only; demonstrate before asking

James's response: **"I will propose this to him in the right way (softly), and nudge, let's just focus on doing the right thing and writing down the rationale behind the redesign as clearly as possible along the way. Right now I lack the mental clarity of what this should ultimately look like, so I want to attain that first."**

Decision: politics parked. Focus on mental clarity first. Politics handled in a separate session once the target architecture is locked.

### Invariant ordering — the load-bearing decision

Leo offered three candidate invariants for the redesign to preserve:
- **A. Observability** — Reflex cycles can never fail silently
- **B. Discoverability** — playbooks/patterns queryable without reading prose
- **C. Correctness** — every stage hands off a validated typed artifact

James chose: **A > C > B.**

**What this ordering implies (named after the choice, not before):**

- Reflex becomes a *measurable* system. With typed logs (A) + validated boundaries (C), you can compute Skeptic precision/recall, cost per card, playbook conversion rate, Curator merge rate. That turns Reflex from "runs cycles" into "improves over cycles."
- A+C are the Gap 2 prerequisite. Without them, the Outcome Learner we'd eventually build has nothing to learn from.
- Migration sequence follows naturally: **state + schemas first, agent refactor second, capability registries last.** B-work can wait — no value in discoverability over a system that can't tell you what it did last cycle.

### What got written

- `reflex_redesign.md` — target architecture, invariants, state/schema layer, migration sketch. Lives as the destination doc.
- `reflex_redesign_process.md` — this doc. Lives as the deliberation log.

---

## Branches explored but not taken (as of Session 1)

### Skills-as-playbooks full rewrite

Considered making each playbook a proper Claude Code skill (with Skill tool invocation). **Rejected for now** because:
- Reflex runs inside Andrew's harness, not Claude Code directly
- The value of the 4-concern separation (role/capabilities/state/flow) can be captured with markdown frontmatter alone
- Skill-ification is a B-layer concern (discoverability) which James de-prioritized

May revisit if Reflex ever runs under a Claude Code-style harness.

### Blocking Skeptic vs. advisory Skeptic

Raised: Skeptic as designed is blocking with a 2-round cap. In the 10-hypothesis Presto bottleneck state, this might burn extra DS enrichment passes without catching proportional errors.

**Decision: keep blocking.** But start logging structured verdicts from Cycle 67 so precision/recall can be computed by Cycle 77, and the blocking vs. advisory question can be answered with data rather than intuition.

### Cartographer agent

Proposed as a portfolio-level coverage agent (Gap D). **Deferred to Tier 2** — not foundational. Phase 0b of PM Agent handles coverage-as-a-phase adequately for now.

### Outcome Learner

Proposed as the Gap 2 closer — reads Build/Simulate/Prove outcomes, feeds quality_patterns. **Deferred to Tier 2.** Preconditions: typed `OpportunityCard.gid` joinable to shipped-experiment outcomes, which requires Phase 1-2 of the migration first.

### Playbook bandit

Proposed to replace rotation with Thompson sampling over playbooks. **Deferred to Tier 2.** Precondition: `state/rotation.yaml:playbook_stats` populated from structured cycle logs. Phase 1 of migration enables it.

---

## Open threads for future sessions

1. **Backfilling `human_agreed` on verdict logs** — what's the UX for James marking "Skeptic was right" vs. "Skeptic was wrong"? This is the signal the eval harness runs on. Options: Asana tag, separate reviewer notes field, implicit signal from whether James merged or reverted the card.

2. **Migration cycle ports** — cycles 1-66 of Cycle Learnings prose. Keep as archive, selectively port to typed patterns, or drop? Leans toward archive + one-time port of Analytical Approaches and Known Dead Ends as seed corpus.

3. **Where Build/Simulate/Prove plug in** — Reflex's Detect → Build handoff. Out of scope today but the state layer should be extensible. Andrew's architectural decision.

4. **How to propose this to Andrew + Dylan** — deferred politics. Once `reflex_redesign.md` stabilizes, consult Wes Kao notebook for framing; likely a soft pre-share of the mental model doc, not the migration plan.

5. **Does Andrew's `detect/CLAUDE.md` become `docs/architecture.md`?** Implied by the redesign. Andrew's call.

6. **Curator proposal review UX** — today `quality/proposed/` is a staging directory. Is that the right interface for James's review, or should it be Asana tasks? Minor but affects Phase 1.

7. **Cost ledger alerting thresholds** — once cost tracking is in, what's the daily/weekly spend alarm? Not urgent but should be set before bandit scheduler lands.

---

## Process observations (meta)

- **The 4-concern framework was the unlock.** Before naming role/capabilities/state/flow as separable, the redesign felt like "many small fixes." After naming them, it became "one structural reshape." Worth reusing as a diagnostic for any tangled agent system.
- **Forcing questions worked.** "Pick one — PR quality, compounding speed, or altitude" — forced clarity. "Which invariant is load-bearing?" — forced the A > C > B ordering, which reshaped the migration sequence immediately.
- **James parked politics deliberately.** Strong move. Mental clarity first means the eventual political framing will be defending a well-thought-out design, not improvising under pressure. Note for future: do this more often.
- **Doc-first persistence is the right move here.** Both `reflex_redesign.md` and this process log are checked-in artifacts that can be iterated, shared, and returned to. No risk of the thinking evaporating.

---

## Session 1 continuation — 2026-04-19 (three cumulative reframes)

After the invariant ordering was set, James stacked three additional reframes that together transformed the scope and priorities of the redesign.

### Reframe 1: Expert labeling must compound (I-0)

**James's framing:** Andrew and Dylan wield considerable resources. High-quality expert labeling on Reflex cards is coming from the RLHF meeting roster (Anna K, Matt Chun, Tim Chu, Dhruvil, Rahul Goutam, James, Dylan, Andrew). Capturing that labeling meaningfully is top of mind for both Andrew and James. System must be designed quickly to leverage that information.

**What this changed:** A new top-priority invariant was elevated above the three already agreed:

**I-0. Expert labeling must compound.** Every expert-minute produces a structured, attributable, queryable, durable unit of knowledge.

I-1 (observability), I-2 (correctness), I-3 (discoverability) became *enablers* of I-0, not ends in themselves.

**Architectural consequences:**
- Curator becomes the center of gravity, not a supporting actor
- New schemas required: `ExpertJudgment`, `PatternProvenance`, `PatternValidation`, `Disagreement`
- Inter-expert disagreement becomes first-class signal (today it's averaged away / ignored)
- Experts get feedback loops — when their labeled pattern gets contradicted by outcomes, they know
- Ergonomics rule: experts keep writing prose; the *agent* does the structuring work

**Why this was the right elevation:** Expert labeling is the scarcest resource in the system by orders of magnitude — more than compute, more than agent polish, more than playbook coverage. If expert time evaporates into Asana prose without compounding, Reflex is generating cost without compounding. The whole purpose of the system is to retain expert judgment at scale.

### Reframe 2: Implementation agents + velocity as primary metric

**James's framing:** Many hypotheses are blocked on A/B test results because the landscape keeps changing. Implementation agents that reliably handle smaller tasks — so humans only have to test and start experiments — can meaningfully reduce bottlenecks and increase velocity. Also: Reflex must be measurable. Track time from idea → analysis → implementation → learning → launch today versus how quickly the system improves it later. Keep velocity as one of the most important metrics to optimize for.

**What this changed:**

1. **Scope expanded from Detect-only to Detect + Build.** Implementation agents live in Build. This aligns with Dylan's "config-change wins before model-config agents" framing from the 2026-04-16 DM.
2. **Velocity distinguished from invariants.** Invariants are design properties that must be true. Velocity is the *outcome* metric we measure continuously. Separate concepts; previously conflated.

**First-wave implementation agents (narrow, reliable):**
- `ConfigAgent` — opens PRs for bounded config changes (CG quotas, utility weights, thresholds)
- `ExperimentSetupAgent` — converts approved `OpportunityCard` into experiment config
- `PlaybookMaintenanceAgent` — placeholder-table discovery, pattern-file maintenance

Reliability bar: deterministic output, strict CI validation, explicit blast-radius scoping, every PR traces to an `OpportunityCard.gid`. Humans test and launch; agents draft.

**Velocity as primary metric:**
- Cycle-time decomposition: t0 (idea) → t1 (enriched) → t2 (reviewed) → t3 (approved) → t4 (PR) → t5 (running) → t6 (result) → t7 (learned)
- Headline: median idea-to-launch days
- Target framing: "Reflex cycle time: 47 → 32 → 18 days" as the one-number system-health summary Andrew, Dylan, and Rajat can rally around
- Decomposable for bottleneck analysis

**Forcing question raised (not yet resolved):** Tight blast radius (allowlisted config files only) vs. wide (any config change in OpportunityCard scope). Leaned tight for v1.

### Reframe 3: Pinsight as offline canary / Simulate stage

**James's framing:** Pinsight feeds into this as a data substrate — supplements engineering team's ability to reason about code, provides direct anecdotal evidence at scale. Pinsight can serve as an offline canary system parallel to online A/B tests (which cost implementation checking, experimental budget, etc.). Pinsight can offer just as rich data from a different source.

**What this changed:**

1. **Scope expanded to include Simulate stage** — Pinsight fills Andrew's Simulate. James now structurally contributes to 3 of 4 stages in Andrew's 4-stage pipeline (Curator/Skeptic in Detect, Pinsight in Simulate, future Outcome Learner closing Prove→Detect).
2. **New stage between Detect and Build:** Pinsight offline canary pre-screens opportunity cards before they consume A/B budget.

**Velocity math (back-of-envelope):**
- If Pinsight pre-screens 80% of cards offline → Build budget concentrates on the 20% with strongest pre-signal
- The 80% that would have failed online fail offline in ~10 days instead of ~35
- A/B budget frees up to run more survivors in parallel

**Architectural additions:**
- New schema: `PinsightInvestigation` — structured PINvestigator output
- New schema: `OfflineCanaryResult` — verdict attached to `OpportunityCard.offline_validation`
- New agent: `PinsightCanaryAgent` — orchestrates Pinsight queries for approved cards
- Human override of canary verdict is itself a `ExpertJudgment` with source=`canary_override`

**Forcing question raised (not yet resolved):** Loosely coupled (Pinsight stays its own system, Reflex calls via API, results are refs) vs. tightly integrated (unified `ExpertJudgment` store across both). Leaned loosely-coupled for v1 — tight integration is a Q3+ conversation once both systems are independently stable.

### Cumulative effect of the three reframes

The redesign went from "fix the structural tangling in Reflex Detect" to:

- **A full research-to-launch system** spanning Detect → Simulate → Build (and eventually Prove→Detect)
- **With expert labeling as the organizing invariant** — every expert-minute compounds
- **Measured on end-to-end velocity** — single-number system-health summary
- **Anchored on Pinsight** as the offline validation layer that makes online A/B budget efficient
- **With implementation agents** closing the implementation-latency gap

This is a dramatically larger and more ambitious system than what `reflex_next_steps.md` described. It's also the Phase 4 positioning from 2026-04-18c coming home — James as system-completeness architect, not feature contributor.

### Implications noted but parked

- **Political framing will need to be careful.** The scope now touches Andrew's Detect, Andrew's Simulate (via Pinsight), and Dylan's Build ambitions. The sequencing of proposals and the attribution of contributions matter — James deliberately parked politics; pick up separately once the target doc stabilizes.
- **Urgency is real.** The RLHF meeting generates high-volume expert labeling imminently. Minimum-viable labeling capture (`ExpertJudgment` schema + append-only log + Curator parsing Asana comments) should ship in days, not weeks.
- **Dependencies compound.** Velocity metric requires `CycleTimeRecord` schema → requires state layer → Phase 1 of migration. Implementation agents require `OpportunityCard` pydantic contract → Phase 2. Pinsight canary requires `OfflineCanaryResult` → Phase 2. This means **Phases 1 and 2 of the migration are on the critical path for everything** the new scope cares about.

---

## Change log

- **2026-04-19 (Session 1):** Initial process log. Mental model crystallized (pipeline + 4-concern framework). Invariants ordered A > C > B. Migration sketched as 6 phases. Political framing parked. Target doc `reflex_redesign.md` seeded.
- **2026-04-19 (Session 1 continuation):** Three cumulative reframes captured:
  1. Expert labeling elevated to I-0 (top-priority invariant); Curator becomes center of gravity; new schemas `ExpertJudgment` / `PatternProvenance` / `PatternValidation` / `Disagreement` added to state layer.
  2. Scope expanded to Build via implementation agents (`ConfigAgent`, `ExperimentSetupAgent`, `PlaybookMaintenanceAgent`); velocity distinguished as primary optimization target (not an invariant) with decomposed cycle-time measurement.
  3. Scope expanded to Simulate via Pinsight as offline canary; new schemas `PinsightInvestigation` / `OfflineCanaryResult`; `PinsightCanaryAgent` added. James now contributes structurally to 3 of 4 stages in Andrew's pipeline.
  Cumulative scope: full Detect → Simulate → Build system organized around compounding expert labeling, measured on end-to-end velocity, with Pinsight as the offline validation layer. Dependencies compound on Phases 1-2 of migration (state layer + typed schemas) — those are the critical path.

- **2026-04-19 (Session 1 — Build blast radius decided):** Implementation agent blast radius resolved. **Allowlist-only** for v1. Growth path is engineer-adoption-driven: each engineering team that wants Reflex implementation agents touching its config opts in by adding allowed paths with team-lead + Reflex-owner sign-off. Organic buy-in over top-down rollout. Respects team sovereignty. Trust ladder built into extension protocol (narrow scope → proven reliability → wider scope). `state/build/allowlist.yaml` schema defined; three validation fire-points (pre-write, pre-commit CI, post-merge audit). Section 6.9 added to redesign doc.

  *Rationale worth preserving:* this decision isn't just a safety call — it's a political design. By making the allowlist engineer-opt-in rather than agent-default-allowed, James avoids the organizational blowback pattern where agentic systems get halted because one team felt railroaded. The narrow-first approach converts "who's authorized to ship this" into "which teams want to opt in" — a much easier conversation to have at each expansion step.

- **2026-04-19 (Session 1 — Pinsight coupling decided):** Resolved: **loose coupling** for v1. Pinsight stays its own system; Reflex calls via API boundary; Pinsight results stored in Reflex as refs, not copies; no shared internals. Each system retains independent deploys, tests, on-call rotation. `ExpertJudgment` stores remain separate (unified store is a Q3+ consideration).

  *Rationale worth preserving:* loose coupling v1 protects both systems' independent evolution. Pinsight can refactor without breaking Reflex; Reflex can refactor without breaking Pinsight. It also protects the attribution line politically — Pinsight is clearly James's system, Reflex is clearly Andrew's system, and the API boundary makes the collaboration explicit and demonstrable rather than entangled. Tight integration done later is a *choice*; tight integration done prematurely is a *constraint*. Delay the decision until both systems have earned independent stability.
