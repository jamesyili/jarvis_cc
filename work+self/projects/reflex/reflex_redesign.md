# Reflex Redesign — Architecture & Rationale

**Owner:** James Li
**Status:** Living design doc — iterated conversationally with Leo
**Started:** 2026-04-19
**Companion docs:** `reflex_next_steps.md` (observations), `reflex_feedback_curator_and_skeptic.md` (Curator/Skeptic design), `pinsight-agentic-vision.md` (Phase 4 positioning)

---

## 1. Purpose

Reflex today is tactically functional but structurally tangled. PM Agent, DS Agent, quality_patterns.md, playbooks/, and the rotation tracker all mix four different concerns into the same files — making the system expensive to run (2700-3100 prompt lines per cycle, ~58% of which is `quality_patterns.md` loaded regardless of which playbooks are running) and hard to reason about (no single entry point, no typed contracts, no structured logs).

This doc captures the target architecture the system should evolve toward. It is **not** a migration plan — that comes after the mental model locks. The goal of this doc is mental clarity: if someone asked "explain Reflex's architecture on a whiteboard in 3 minutes," the answer should be crisp, inspectable, and measurable.

This redesign covers **three stages** of Andrew's 4-stage pipeline: **Detect**, **Simulate** (via Pinsight as offline canary), and **Build** (via implementation agents). Scope extended 2026-04-19 to include:

- Implementation agents — narrow, reliable agents that convert approved opportunity cards into PRs and experiment configs, reducing the A/B test drafting bottleneck
- Pinsight as offline canary — pre-screens opportunity cards before they consume online A/B budget; serves as rich data substrate for reasoning about code and mechanisms at scale

Prove (and closing the Prove→Detect feedback via Outcome Learner) remains a Tier 2 concern but schemas are designed to extend cleanly.

**Primary optimization target:** end-to-end idea-to-launch cycle time, measured continuously with per-stage decomposition. See Section 11 for the headline metric and how it's measured.

---

## 2. Current-state problems this resolves

| Problem | Root cause | Cost |
|---|---|---|
| 58% of per-cycle budget is `quality_patterns.md` (1564 lines) loaded in full | State, patterns, rotation tracker, and cycle learnings all live in one file | Token waste; scaling wall at ~3000 lines per current growth rate |
| "How does Reflex run?" requires reading pm_agent.md + 18 playbooks + quality_patterns.md + detect/CLAUDE.md (~4000 lines) | No entry point; no layered architecture doc | Onboarding friction for new agents and humans |
| Skeptic regressions will be invisible | No structured verdict log; "dry-run against 3 cards" is smoke test not eval | Prompt drift; silent quality decay |
| Cost is untracked (`detect/CLAUDE.md` line 102) | No cost ledger | Unbounded API spend as agent count grows |
| Cycle-over-cycle compounding is unmeasurable | No structured cycle log; learnings are prose entries | Can't answer "is Reflex getting better?" |
| Malformed cards break downstream agents | No typed contracts at stage boundaries | Silent failures; brittle handoffs |
| Playbook selection is rotation-not-signal | 66 cycles of conversion-rate data exists but is unindexed | Cycle cost wasted on dry wells |

---

## 3. Load-bearing invariants (ordered by priority)

Every design decision in this doc is made to preserve these invariants, in this order. When they conflict, earlier wins.

### I-0. Expert labeling must compound

Every expert-minute spent on Reflex (Andrew, Dylan, Anna, Matt, Tim, Dhruvil, Rahul, James) must produce a structured, attributable, queryable, durable unit of knowledge that makes future cards better.

This is the *top* invariant because it's the system's actual purpose. Cards are artifacts; patterns are intermediate state. The thing Reflex exists to retain is **expert judgment at scale**. If expert time evaporates into Asana prose that never structurally improves subsequent cards, Reflex is generating cost without compounding. Expert labeling is the scarcest and most valuable resource in the system by orders of magnitude — more than compute, more than playbook coverage, more than agent polish.

I-1, I-2, I-3 below are *enablers* of I-0, not ends in themselves:
- I-1 (observability) provides the audit trail expert judgments need to be attributable
- I-2 (correctness) ensures judgments don't get corrupted at stage boundaries
- I-3 (discoverability) lets judgments be found and propagated to relevant future cards

**Operational meaning:**
- Every expert interaction with a card produces an `ExpertJudgment` record (typed, attributed, timestamped, cross-referenced)
- Inter-expert disagreement is detected and preserved as first-class signal, not averaged away
- Every `Pattern` has a `PatternProvenance` tracing to the `ExpertJudgment`(s) that produced it
- Every `Pattern` has a `PatternValidation` status that updates as experiment outcomes land
- Experts get feedback when their labeled patterns get validated or contradicted by outcomes

### I-1. Observability — no silent failures

Every agent run produces a structured record. Every Skeptic verdict is a typed artifact. Every Curator proposal is logged. Every API call hits a cost ledger. The system can always answer *"what did I do last cycle, why, and at what cost?"*

This is the load-bearing invariant because without it:
- Skeptic regressions are invisible
- Eval harnesses have no data to run on
- Outcome Learner (future) has no training signal
- Nobody can answer "is Reflex compounding?"

**Operational meaning:** No markdown-only state. Every state write goes through a typed schema. Every agent run appends to `cycle_log.jsonl`. Every API call appends to `cost_ledger.jsonl`.

### I-2. Correctness — typed handoffs at every stage boundary

Every stage produces a validated pydantic artifact the next stage consumes. Malformed output fails at the producer's boundary, not in the consumer's parsing logic.

This is the second invariant because without it:
- Observability logs become unparseable free text
- Regression detection is best-effort
- Agents silently break each other when prompts drift

**Operational meaning:** `HypothesisCard`, `OpportunityCard`, `SkepticVerdict`, `CuratorProposal` are pydantic models. Agents validate on read and on write. Validation failures are first-class events in `cycle_log.jsonl`.

### I-3. Discoverability — registries over prose

Playbooks, patterns, and checks are indexed and queryable by tag (surface, pillar, applicability). A human or agent can answer "which playbooks cover Search?" without reading 18 files.

This is the third invariant because without it:
- Agents load more context than they need
- Humans struggle to navigate
- New playbooks and patterns don't integrate cleanly

Lower priority because it's a navigability win, not a correctness or observability win. Nice to have; not load-bearing.

**Operational meaning:** Each playbook and pattern gets YAML frontmatter (`surface`, `pillar`, `detection_method`, `historical_conversion`). A `registry.yaml` is auto-built from frontmatter. Agents query the registry to decide what to load.

---

## 4. The mental model

### Reflex is a specialist pipeline across Detect → Simulate → Build

```
┌─ Detect ──────────────────┐  ┌─ Simulate ─┐  ┌─ Build ────────┐  ┌─ Online ─┐  ┌─ Prove ─┐
│                           │  │            │  │                │  │          │  │         │
│ PM ─▶ DS ─▶ Skeptic ─▶    │─▶│ Pinsight   │─▶│ Implementation │─▶│ A/B Test │─▶│ Outcome │
│              │  Human     │  │ offline    │  │ agents         │  │ running  │  │ Learner │
│              ▼  Expert    │  │ canary     │  │ (config PR /   │  │          │  │         │
│           Curator ◀──     │  │            │  │  experiment    │  │          │  │         │
│           judgments       │  │            │  │  setup)        │  │          │  │         │
│              ▲            │  │            │  │                │  │          │  │         │
└──────────────┼────────────┘  └────────────┘  └────────────────┘  └──────────┘  └─────────┘
               │                      │                                                  │
               │                      └──── PinsightInvestigation ───────────┐           │
               │                                                             ▼           ▼
               └──────────────── ExpertJudgment ◀──── all stages feed ◀── Outcome data ──┘
                                                          into labeling
```

**Detect stages (synchronous cycle):**
1. **PM Agent** — generates hypothesis cards from signal (playbooks, prior cards, rough ideas)
2. **DS Agent** — enriches hypothesis into opportunity (quantifies, sizes, scores)
3. **Skeptic** — gates opportunity cards before human time is spent
4. **Human Expert** — reviews, comments, approves (produces `ExpertJudgment`s)

**Simulate stage (triggered by approval):**
5. **PinsightCanaryAgent** — takes approved `OpportunityCard`, runs Pinsight investigations, writes `OfflineCanaryResult`. Cards with negative/inconclusive offline signal can be killed before burning online budget. Human can override.

**Build stage (triggered by positive canary or override):**
6. **Implementation agents** — narrow and reliable:
   - `ConfigAgent` — opens PR for bounded config changes (CG quota, utility weights, thresholds)
   - `ExperimentSetupAgent` — converts `OpportunityCard` into experiment config
   - `PlaybookMaintenanceAgent` — placeholder-table discovery, pattern-file maintenance, other low-risk engineering chores
7. **Human engineer** — reviews PR, launches experiment

**Async observers:**
- **Curator** — triggered by any expert interaction (Asana comments, Pinsight findings, meeting decisions); shapes feedback into `ExpertJudgment` records and pattern proposals
- **VelocityAgent** — passively measures end-to-end cycle time per card; writes dashboard
- **Outcome Learner (future)** — triggered by A/B test results; validates patterns against outcomes, writes `PatternValidation`, closes the Prove→Detect loop

### Every agent is built from four concerns

| Concern | Definition | Current state | Target state |
|---|---|---|---|
| **Role** | Identity + I/O contract + invariants | Top of agent prompt | `agents/{agent}/role.md` (~60 lines) |
| **Capabilities** | Named "moves" the agent can execute | PM: 18 playbook files. DS: 30+ prose patterns in quality_patterns.md. Skeptic: 5 checks embedded in prompt. Curator: ops embedded in prompt. | `capabilities/{agent}/` with frontmatter + registry |
| **State** | What the agent reads from / writes to the shared world | Four kinds of state in quality_patterns.md + board | `state/` directory, typed schemas |
| **Flow** | Phased execution of a run | Mixed into agent prompt | `agents/{agent}/flow.md` (~80 lines) |

The current system's defining mistake is smashing all four into one or two files per agent. The redesign separates them cleanly, so each question has one answer location and each agent's per-cycle load is bounded.

---

## 5. Target directory structure

```
reflex/detect/
├── agents/                          # orchestrators — THIN
│   ├── pm/
│   │   ├── role.md                  # identity + I/O contract + invariants
│   │   └── flow.md                  # phase-by-phase execution
│   ├── ds/
│   │   ├── role.md
│   │   └── flow.md
│   ├── skeptic/
│   │   ├── role.md
│   │   └── flow.md
│   └── curator/
│       ├── role.md
│       └── flow.md
│
├── capabilities/                    # named "moves" each agent can call
│   ├── playbooks/                   # PM's moves (18 files)
│   │   ├── registry.yaml            # auto-built index: name, surface, pillar, historical_conversion
│   │   ├── market_cg_performance.md
│   │   └── ...
│   ├── analytical_checks/           # DS's moves (~30 checks)
│   │   ├── registry.yaml
│   │   ├── cg_decomposition.md
│   │   ├── vlm_verification.md
│   │   └── ...
│   ├── skeptic_checks/              # Skeptic's 5 checks
│   │   ├── registry.yaml
│   │   ├── pattern_check.md
│   │   ├── context_check.md
│   │   ├── evidence_check.md
│   │   ├── internal_consistency.md
│   │   └── novelty_check.md
│   └── curator_ops/                 # Curator's operations
│       ├── registry.yaml
│       ├── shape_feedback.md
│       ├── detect_conflict.md
│       └── detect_decay.md
│
├── state/                           # typed shared state — SEPARATE from prompts
│   ├── board.yaml                   # current opportunities + hypotheses
│   ├── rotation.yaml                # playbook tracker
│   ├── dead_ends.yaml               # typed Known Dead Ends (not prose)
│   ├── cycle_log.jsonl              # structured, one line per cycle
│   ├── cost_ledger.jsonl            # one line per agent call
│   ├── verdict_log.jsonl            # one line per Skeptic verdict
│   └── proposal_log.jsonl           # one line per Curator proposal
│
├── infra/                           # stable references every agent reads
│   ├── board_setup.md               # Asana ops reference
│   ├── mcp_conventions.md           # Presto/Experiments/Knowledge conventions
│   └── schemas/                     # pydantic models (correctness invariant lives here)
│       ├── hypothesis_card.py
│       ├── opportunity_card.py
│       ├── skeptic_verdict.py
│       ├── curator_proposal.py
│       ├── cycle_log_entry.py
│       └── cost_ledger_entry.py
│
└── docs/
    ├── architecture.md              # the mental model (this doc, trimmed)
    ├── handoff_protocol.md          # who hands what to whom
    └── change_log.md                # architectural decisions
```

### What each layer does NOT contain

- **Agents** do not contain playbook text, pattern descriptions, or state. They orchestrate and invoke.
- **Capabilities** do not contain state or phase logic. They are domain knowledge: "here's how to do this specific thing."
- **State** does not contain prose. Everything is typed. Prose capture lives in capabilities or docs.
- **Infra** does not contain agent-specific logic. It's the common substrate.

---

## 6. The state layer (observability-first)

This layer is implemented first because I-1 is the load-bearing invariant. Nothing else works without it.

### 6.1 `state/cycle_log.jsonl`

One line per agent cycle. Structured, append-only, never edited.

```python
# infra/schemas/cycle_log_entry.py
class CycleLogEntry(BaseModel):
    cycle_id: int
    timestamp: datetime
    agent: Literal["pm", "ds", "skeptic", "curator"]
    duration_s: float
    inputs: dict                    # what the agent read
    outputs: dict                   # what the agent produced
    capabilities_invoked: list[str] # which playbooks/checks ran
    errors: list[str]               # structured errors
    validation_failures: list[str]  # boundary check failures
```

Example — PM Agent cycle 67:
```json
{
  "cycle_id": 67,
  "timestamp": "2026-04-19T12:34:56Z",
  "agent": "pm",
  "duration_s": 1847,
  "inputs": {
    "rough_ideas_count": 2,
    "unresponded_comments": 3,
    "board_hypothesis_count": 12,
    "rotation_position": "9/10"
  },
  "outputs": {
    "hypotheses_created": 4,
    "hypotheses_strengthened": 2,
    "hypotheses_retired": 1,
    "dedup_skipped": 0,
    "patterns_updated": ["topline_impact_sizing"]
  },
  "capabilities_invoked": ["market_cg_performance", "relevance_gaps", "experiment_review"],
  "errors": [],
  "validation_failures": []
}
```

### 6.2 `state/cost_ledger.jsonl`

One line per API call (not per cycle). Enables cost/card, cost/playbook, cost/cycle analysis.

```python
class CostLedgerEntry(BaseModel):
    timestamp: datetime
    cycle_id: int
    run_id: str                     # UUID, groups calls within one cycle
    agent: str
    model: str
    operation: str                  # "playbook_execution" | "enrichment" | "verdict" | etc.
    capability: str | None          # which playbook/check, if applicable
    input_tokens: int
    output_tokens: int
    cached_tokens: int
    cost_usd: float
```

### 6.3 `state/verdict_log.jsonl`

One line per Skeptic verdict. **Critical for the eval harness** — without this, Skeptic quality drifts silently.

```python
class VerdictLogEntry(BaseModel):
    timestamp: datetime
    cycle_id: int
    card_gid: str
    card_title: str
    verdict: Literal["PASS", "FAIL", "NEEDS_HUMAN"]
    checks: dict[str, Literal["PASS", "FAIL", "N/A"]]  # per-check outcome
    fail_reasons: list[str]         # specific, with pattern refs
    patterns_cited: list[str]       # which quality patterns drove the verdict
    revision_round: int             # 0 = first review, 1-2 = after DS revisions
    confidence: float               # 0.0-1.0
    human_reviewed: bool | None     # backfilled once human reviews
    human_agreed: bool | None       # backfilled — critical for eval
```

The `human_reviewed` / `human_agreed` fields are what the Skeptic eval harness computes precision/recall from.

### 6.4 `state/proposal_log.jsonl`

One line per Curator proposal. Tracks merge rate over time.

```python
class ProposalLogEntry(BaseModel):
    timestamp: datetime
    cycle_id: int
    comment_gid: str
    comment_author: str
    proposal_type: Literal["new_pattern", "update_pattern", "retire_pattern", "conflict_report"]
    proposal_path: str              # quality/proposed/*.md
    conflict_detected: bool
    confidence: float
    human_merged: bool | None       # backfilled
    human_edits_required: bool | None  # backfilled
```

### 6.5 `state/board.yaml`

Current state of the Asana board, synced each cycle. Typed, not free-form.

```yaml
opportunities:
  - gid: "1210..."
    title: "Per-state utility weights"
    surface: [homefeed]
    pillar: [4.1]
    composite_score: 4.8
    impact: 5
    feasibility: 4
    alignment: 5
    last_updated: "2026-04-17"
    origin_playbook: "surface_transfer"
    skeptic_verdict_gid: "verdict_log:1820..."
hypotheses:
  - ...
```

### 6.6 `state/rotation.yaml`

Playbook rotation tracker. Replaces the free-text note at the bottom of `quality_patterns.md`.

```yaml
current_rotation: 9
full_rotations_completed: 8
last_cycle: 66
last_ran: [market_cg_performance, relevance_gaps, experiment_review]
next_up: [engagement_decomposition, follow_graph_health, ranking_feature_performance]
playbook_stats:
  market_cg_performance:
    cycles_run: 18
    hypotheses_generated: 14
    promoted_to_opportunities: 14
    conversion_rate: 1.00
    avg_quality: 4.5
  team_roadmap_gaps:
    cycles_run: 6
    hypotheses_generated: 2
    promoted_to_opportunities: 0
    conversion_rate: 0.00
    avg_quality: 0
```

This is the data a future bandit-over-playbooks scheduler would consume.

### 6.7 `state/dead_ends.yaml`

Known Dead Ends as typed data, not prose entries. Skeptic queries this directly.

```yaml
- id: datestr_vs_date
  category: table_columns
  pattern: "datestr"
  correct: "date"
  tables: ["finops.northstar_user_ge_metrics"]
  discovered: "cycle_19"
  severity: "auto_fail"
- id: curl_to_localhost_19193
  category: mcp_usage
  pattern: "curl.*localhost:19193"
  correct: "use native mcp__presto__* tool calls"
  severity: "auto_fail"
```

---

## 6.8 Expert labeling layer (I-0 substrate)

The state artifacts that make expert judgment compound.

### `state/expert_judgments.jsonl`

One line per expert-card interaction. Curator produces these by parsing Asana comments (and eventually other inputs — Slack DMs, 1:1 notes, meeting transcripts).

```python
class ExpertJudgment(BaseModel):
    timestamp: datetime
    expert: str                     # canonical ID (e.g., "anna_k", "dylan_wang", "andrew_y")
    expert_role: str                # "pm_retentive", "em_hf_cg", "sr_director_product"
    card_gid: str
    cycle_id: int
    judgment_type: Literal[
        "agree",
        "disagree",
        "reframe",          # recasts the hypothesis
        "extend",           # adds a new analytical angle
        "retire",           # argues the card should die
        "new_info",         # brings evidence not in the card
        "question",         # asks for clarification
    ]
    claim_targeted: str | None      # specific claim the judgment is about, not the whole card
    rationale: str                  # expert's own words, preserved
    rationale_summary: str          # Curator's compression
    confidence: Literal["low", "medium", "high"] | None
    cross_card_propagation: list[str]  # other card gids this judgment should apply to
    source: Literal["asana_comment", "slack_dm", "one_on_one", "meeting", "direct_input"]
    source_ref: str                 # URL or identifier
    preserves_original: bool        # did Curator preserve verbatim prose?
```

### `state/pattern_provenance.jsonl`

Every pattern in quality_patterns.md traces to the `ExpertJudgment`s that produced it. Preserves attribution and multiplicity.

```python
class PatternProvenance(BaseModel):
    pattern_id: str                 # FK to patterns/*.md
    pattern_created_cycle: int
    source_judgments: list[str]     # FK to expert_judgments.jsonl row IDs
    contributors: list[str]         # experts whose judgments informed this pattern
    consensus_score: float          # 0.0-1.0, inverse of disagreement across sources
    last_reinforced_cycle: int      # most recent cycle where a judgment cited this pattern
```

### `state/pattern_validation.jsonl`

Does the pattern survive contact with reality? Updated by the Outcome Learner when Build/Simulate/Prove results land.

```python
class PatternValidation(BaseModel):
    pattern_id: str
    cycle_checked: int
    outcome_signal: Literal["validated", "contradicted", "inconclusive", "no_data"]
    evidence_gid: str               # shipped experiment, simulation result, etc.
    confidence: float
    notes: str                      # why validated or contradicted
```

### `state/disagreements.jsonl`

When two or more experts render conflicting judgments on the same card or claim, Curator writes a structured disagreement record. This is *signal*, not noise — it's where deep discussion is warranted.

```python
class Disagreement(BaseModel):
    card_gid: str
    claim_targeted: str
    cycle_id: int
    positions: list[ExpertPosition]  # each has expert, position, rationale
    detected_by: Literal["curator_auto", "skeptic_flag", "explicit_tag"]
    resolution: Literal["open", "resolved_by_data", "resolved_by_seniority", "parked"] | None
    resolution_cycle: int | None
    resolution_notes: str | None
```

Open disagreements are surfaced to experts as "this needs a discussion" — not hidden in prose.

### Why this layer is architecturally distinct

Expert-labeling artifacts are fundamentally different from cards and cycle logs:
- **Attribution is structural, not optional.** Cards can be anonymous; judgments cannot.
- **Multiplicity is the default.** One card can attract 10 judgments from 4 experts.
- **Disagreement is preserved.** Cards get consolidated; judgments never do.
- **Temporal decay matters.** A judgment from cycle 10 may be contradicted by cycle 40 data; both are preserved.
- **Cross-card propagation is explicit.** A judgment about "per-state weights don't survive RL retraining" should auto-propagate to every per-state card the PM generates, not just the one it was written on.

---

## 6.9 Implementation agent allowlist (Build safety rail)

Implementation agents (`ConfigAgent`, `ExperimentSetupAgent`, `PlaybookMaintenanceAgent`, future additions) never write outside an explicit allowlist. This is the blast-radius contract.

### Decision (2026-04-19)
**Allowlist-first, gradually expanded as engineering teams opt in their own config files over time.** Growth path is engineer-adoption-driven, not agent-capability-driven. Each engineering team that wants Reflex implementation agents touching its config adds its own allowed paths — organic buy-in beats top-down rollout and naturally respects team ownership boundaries.

### `state/build/allowlist.yaml`

```yaml
# The only paths implementation agents may write to.
# Extensions require sign-off from the engineering team lead + Reflex owner (Andrew).
agents:
  config_agent:
    hf_cg_team:                    # team that opted in
      approved_by: [dylan_wang, james_li]
      approved_date: "2026-04-24"
      paths:
        - "services/homefeed/candidate_generation/config/cg_quotas.yaml"
        - "ml_resources/mlenv/homefeed/l2_utility/constants.py"   # specific file
      keys_allowed:                # within a file, only these top-level keys
        cg_quotas.yaml: ["quotas", "thresholds"]
      max_diff_lines: 50           # PRs exceeding this → fail loud, require human
  experiment_setup_agent:
    hf_cg_team:
      paths:
        - "experiments/configs/homefeed/*.yaml"
      ...
  playbook_maintenance_agent:
    reflex_internal:
      approved_by: [andrew_y, james_li]
      paths:
        - "services/reflex/detect/capabilities/playbooks/*.md"
        - "services/reflex/detect/state/dead_ends.yaml"
```

### Validation fires at three points

1. **Before writing:** Agent checks target path against allowlist. Path not listed → fail loud, surface to human.
2. **Pre-commit:** CI validates every implementation-agent PR against `allowlist.yaml`. Out-of-scope file touched → CI fails.
3. **Post-merge audit:** `state/cycle_log.jsonl` records every agent-authored PR with allowlist-match evidence. Retroactive audit possible.

### Extension protocol

New path → new team → agent → trust. Expansion requires:
1. Engineering team lead formally requests (PR to `allowlist.yaml`)
2. Co-approval from Reflex owner (Andrew) and James
3. At least 1 cycle of successful narrow-scope PRs from that agent first (trust ladder)
4. Extension logged in `state/build/allowlist_history.jsonl`

### Why this architecture

- **Engineers retain sovereignty.** No team wakes up to find an agent touching its code without opt-in.
- **Trust ladder.** Start narrow, prove reliability, expand. Mirrors how human engineering teams grant each other code ownership.
- **Political neutrality.** James isn't pushing agent-owned changes onto unwilling teams. The agents serve teams that ask; they don't solicit.
- **Audit by default.** Every expansion and every PR traces cleanly.

---

## 7. The schemas layer (correctness-first)

Every stage handoff is a typed artifact. Validation fires at the boundary.

### 7.1 Boundary diagram

```
PM ──HypothesisCard──▶ DS ──OpportunityCard──▶ Skeptic ──SkepticVerdict──▶ Human
 ▲                                                                            │
 │                                                                            ▼
 └────────────────────── CuratorProposal ◀── Curator ◀── AsanaComment ───────┘
```

### 7.2 Schema sketches

```python
# infra/schemas/hypothesis_card.py
class HypothesisCard(BaseModel):
    gid: str | None                 # None before Asana creation
    title: str                      # opportunity-framed, not crisis-framed
    surface: list[Surface]          # validated enum
    pillar: list[Pillar]            # validated enum
    hypothesis_statement: str
    evidence: list[Evidence]        # each has source, query, timestamp
    signal_strength: int            # 1-5
    analytical_hooks: list[str]     # hints for DS Agent
    origin_playbook: str            # must exist in playbook registry
    cycle_created: int
    cycle_last_strengthened: int | None

# infra/schemas/opportunity_card.py
class OpportunityCard(HypothesisCard):
    impact_estimate: ImpactEstimate  # must bridge to SSv2 minimum
    feasibility_score: int          # 1-5
    alignment_score: int            # 1-5
    composite_score: float          # derived: Impact*0.5 + Feas*0.3 + Align*0.2
    experiment_cross_refs: list[ExperimentRef]
    vlm_verified_pins: list[PinStory]  # ≥ 3 required (validation fires)
    inline_chart_attachment_gid: str   # validation fires if missing
    contradiction_test: ContradictionTest
    promoted_cycle: int
```

### 7.3 Where validation fires

- **PM → DS boundary:** `HypothesisCard.model_validate()` on DS read. Invalid cards stay in Hypotheses section with a validation error comment.
- **DS → Skeptic boundary:** `OpportunityCard.model_validate()` on Skeptic read. Invalid cards block promotion and log to `cycle_log.jsonl`.
- **Skeptic → Human boundary:** `SkepticVerdict.model_validate()` on write. Every verdict must have structured `checks` and `fail_reasons`.
- **Human → Curator boundary:** Asana comment stays unstructured (humans write prose), but `CuratorProposal` on write is typed.

### 7.4 What validation enables

- **Skeptic eval harness** can compute `precision = (human_agreed_FAIL) / (total_FAIL)` from typed verdict logs.
- **Cost regression detection** can flag when a playbook's cost/card jumps above historical mean.
- **Playbook bandit** (future) can consume `rotation.yaml:playbook_stats` directly.
- **Outcome Learner** (future) can join shipped-experiment outcomes to `opportunity_card.gid` directly.

---

## 8. The agents layer (thin orchestrators)

Each agent's total prompt = `role.md` + `flow.md`. That's it. No playbook text, no pattern descriptions, no state inlined.

### Example: `agents/pm/role.md` (~60 lines)

```markdown
# PM Agent — Role

## Identity
Generate hypothesis cards from signal across Pinterest's discovery stack.

## Inputs (reads)
- `state/rotation.yaml` — which playbooks to run this cycle
- `state/board.yaml` — current board composition
- `capabilities/playbooks/{selected}` — 3 playbook files per cycle
- `capabilities/analytical_checks/registry.yaml` — for quality-pattern hints
- Asana (via `infra/board_setup.md`) — Rough Ideas + unresponded comments

## Outputs (writes)
- Asana Hypotheses section — new/strengthened cards
- `state/cycle_log.jsonl` — one entry summarizing the cycle
- `state/cost_ledger.jsonl` — one entry per API call
- `state/rotation.yaml` — updated tracker

## Invariants
- Minimum 2 new hypotheses per cycle
- Every card passes `HypothesisCard.model_validate()` before Asana write
- Every cycle ends with a `cycle_log.jsonl` entry, even on failure
- Never modify `state/dead_ends.yaml` directly (Curator's responsibility)
```

### Example: `agents/pm/flow.md` (~80 lines)

```markdown
# PM Agent — Execution Flow

Phases are sequential. Log each phase's outcome to `cycle_log.jsonl`.

## Phase 0: Human feedback (HIGHEST PRIORITY)
1. Fetch Rough Ideas → process each per `capabilities/pm_ops/rough_ideas.md`
2. Fetch unresponded comments → respond per `capabilities/pm_ops/comment_response.md`
3. If feedback reveals a pattern, write to `quality/proposed/` (Curator reviews)

## Phase 1: Select playbooks
1. Read `state/rotation.yaml:next_up` → pick 3 playbooks
2. Check `state/board.yaml` for surface coverage gaps → optional sub 1
3. Load selected playbook files only

## Phase 2: Run playbooks
For each selected playbook:
1. Execute per playbook instructions
2. Apply relevant analytical checks from `capabilities/analytical_checks/` (query registry by surface/playbook tag)
3. Draft `HypothesisCard` — validate with pydantic before Asana write

## Phase 3-5: ...
```

Compared to today's `pm_agent.md` (333 lines), this is ~140 lines total. The other ~190 lines moved to capabilities and state, where they're loaded only when needed.

---

## 9. The capabilities layer (domain knowledge)

### 9.1 Playbooks (PM's capabilities)

Each playbook gets YAML frontmatter:

```markdown
---
name: market_cg_performance
surface: [homefeed, search]
pillar: [2.3]
detection_method: market_cg_decomposition
required_tools: [presto, experiments]
output_schema: hypothesis_card_v1
historical_conversion: 1.00
historical_avg_quality: 4.5
---

# market_cg_performance — When to run
...
```

`capabilities/playbooks/registry.yaml` is auto-built from frontmatter via a pre-commit hook. PM Agent queries the registry to find playbooks by tag; it does not hardcode the roster.

### 9.2 Analytical checks (DS's capabilities)

Each pattern from today's `quality_patterns.md` becomes a typed check file:

```markdown
---
name: cg_source_decomposition
applies_to: [homefeed, related_pins]
playbooks: [market_cg_performance, relevance_gaps, retention_decomposition]
mandatory_when: "hypothesis involves a CG"
discovered_cycle: 2
---

# CG source decomposition
Slice by `reason_to_choose` to turn vague relevance gaps into CG-level problems.
[specifics...]
```

DS Agent does not read all 30+ checks every cycle. It queries `capabilities/analytical_checks/registry.yaml` for checks matching the current card's surface/playbook and loads only those.

### 9.3 Skeptic checks, Curator ops

Same pattern — each of Skeptic's 5 checks is a file, each of Curator's operations is a file, with frontmatter declaring when to fire.

---

## 10.5 Velocity measurement (primary optimization target)

End-to-end idea-to-launch cycle time is the system's headline metric. Every card that completes the journey writes one `CycleTimeRecord`; the `VelocityAgent` rolls these into a continuously-updated dashboard.

### `state/velocity/cycle_times.jsonl`

```python
class CycleTimeRecord(BaseModel):
    card_gid: str
    card_title: str
    surface: list[str]
    pillar: list[str]
    stage_timestamps: dict[str, datetime]   # keyed by stage name
    # Expected keys:
    # - t0_hypothesis_created
    # - t1_enriched_to_opportunity
    # - t2_skeptic_verdict
    # - t3_expert_approved
    # - t4_offline_canary_start
    # - t5_offline_canary_result  (may be same as t6 if skipped)
    # - t6_implementation_pr_opened
    # - t7_experiment_running
    # - t8_result_in
    # - t9_learning_written
    terminal_stage: str                      # how far the card got
    terminal_reason: str | None              # killed_by_canary | killed_by_expert | shipped | etc.
    total_days: float | None
```

### `state/velocity/dashboard.yaml`

Continuously refreshed by `VelocityAgent`:

```yaml
as_of: "2026-04-19T18:00:00Z"
global:
  median_idea_to_launch_days: 35
  p75_idea_to_launch_days: 52
  p95_idea_to_launch_days: 89
  cards_completing_per_week: 1.8
by_stage_median_days:
  hypothesis_to_opportunity: 3
  opportunity_to_approval: 9
  approval_to_canary_result: 1.5
  canary_to_implementation_pr: 4
  pr_to_experiment_running: 3
  experiment_to_result: 18
  result_to_learning: 2
killed_at_stage:
  skeptic: "12% of hypotheses"
  expert_review: "35% of opportunities"
  pinsight_canary: "48% of approved cards"   # the big velocity saver
  a_b_test: "17% of implementations"
trend_30d:
  median_cycle_time_delta: "-7 days"
  cards_completing_delta: "+0.6/week"
```

### Why velocity is the primary metric

- **Single-number system-health.** "Reflex cycle time: 47 → 32 → 18 days" is what Andrew, Dylan, and Rajat rally around.
- **Decomposable.** Bottleneck analysis is immediate — which stage has the longest median.
- **Ties to business value.** Shorter cycle time = more hypotheses tested per quarter = more shipped wins per headcount.
- **I-0 materializes here.** Expert labeling compounds = fewer bad cards reach Build = velocity goes up. Velocity is how you *prove* the labeling is compounding.

---

## 10. What this unlocks

Once A (observability) and C (correctness) are in place, the following become possible — none of which work in the current architecture:

| Unlock | Requires | Payoff |
|---|---|---|
| **Skeptic eval harness** | `verdict_log.jsonl` with `human_agreed` backfill | Regression detection on every prompt change |
| **Cost dashboards** | `cost_ledger.jsonl` | Per-playbook, per-card, per-cycle cost attribution |
| **Playbook bandit scheduler** | `rotation.yaml:playbook_stats` populated | 30-50% cycle cost savings by concentrating on high-conversion playbooks |
| **Outcome Learner** (Gap 2) | Typed `OpportunityCard.gid` joinable to shipped-experiment outcomes | Patterns compound on what moved metrics, not what got commented on |
| **Retrieval over patterns** | `analytical_checks/registry.yaml` with tags | Per-cycle context drops from 1564 lines to ~200 lines |
| **Dynamic pattern assembly** | Registry + per-card tag matching | Each card sees only relevant patterns, not the full 1564-line file |
| **System health dashboard** | `cycle_log.jsonl` timeseries | Answer "is Reflex compounding?" in 1 query |

None of these are mystical. They're all standard observability + typed-boundary dividends. The current architecture precludes all of them.

---

## 11. Migration sketch (phases, not dates)

Rough sequencing — actual scoping happens after this doc is agreed. Each phase is independently valuable; the system improves monotonically.

**Phase 1 — State layer primitives (I-1 first).**
Introduce `state/` directory with JSONL logs + YAML typed state. Agents append structured logs; Curator still uses today's `quality_patterns.md` for now. Cheap to add, immediately unlocks cost tracking and verdict logging. Does not change agent prompts.

**Phase 2 — Pydantic schemas at boundaries (I-2).**
Add `infra/schemas/`. Agents validate cards on read and write. Invalid handoffs surface in `cycle_log.jsonl:validation_failures`. Low risk; catches regressions immediately.

**Phase 3 — Thin agents.**
Split each agent prompt into `role.md` + `flow.md`. Playbook text stays where it is; orchestration logic extracts. Per-agent prompt size drops ~60%.

**Phase 4 — Capability registries (I-3).**
Add frontmatter to playbooks and checks. Generate registries. Agents query by tag instead of hardcoded lists. Per-cycle context drops further.

**Phase 5 — Retrieval over patterns.**
Embed patterns; retrieve top-K per card. Drops `quality_patterns.md` load from 1564 lines to ~200.

**Phase 6 — Playbook bandit + Outcome Learner.**
Both are greenfield builds on the typed state layer from Phase 1.

---

## 12. Open questions

- **Do we migrate cycles 1-66 of learnings to the new schema, or start fresh at cycle 67?** Leans toward "start fresh at 67 + one-time port of the Analytical Approaches and Known Dead Ends sections as the seed corpus." Cycle Learnings section probably stays as archive.
- **What's the right split for `quality_patterns.md` cycle learnings?** Keep as prose archive, or decompose into typed pattern deltas per cycle? Leans toward archive — retrieval isn't the bottleneck for historical learnings.
- **Do playbooks stay as prose files or become something more structured?** Prose is fine for the body; frontmatter handles discoverability. Avoid over-structuring the body — it's legitimately instructional prose for the agent to read.
- **How does this coexist with Andrew's `detect/CLAUDE.md`?** The redesign implies `detect/CLAUDE.md` becomes `docs/architecture.md` + a thin pointer. Andrew owns that decision.
- **Pinsight coupling tightness.** ~~Open~~ **Decided 2026-04-19: loose coupling.** Pinsight stays its own system. Reflex calls it via API boundary. Results in Reflex are stored as refs to Pinsight artifacts, not copies. No shared internals. Each system keeps independent deploys, tests, and on-call. `ExpertJudgment` stores remain separate. Tight integration (unified `ExpertJudgment` store across both systems, direct trace sharing) is a Q3+ conversation once both systems are independently stable and the benefit of unification is demonstrable.
- **Implementation agent blast radius.** ~~Open~~ **Decided 2026-04-19:** allowlist-only to start; gradually expand as engineering teams opt in their own config files over time. Growth path is engineer-adoption-driven, not agent-capability-driven — each new engineering team adds its own allowed paths when it wants Reflex implementation agents touching its config. See Section 6.9 for the allowlist mechanism.
- **Expert-labeling capture deadline.** RLHF meeting generates high-volume labeling imminently. Minimum-viable version (`ExpertJudgment` schema + append-only log + Curator parsing Asana comments) should ship in days, not weeks, to avoid losing that signal.
- **Outcome Learner timing.** Deferred to Tier 2 originally; under I-0 becomes load-bearing for the feedback loop. Timing depends on when Build/Simulate/Prove artifacts become structured enough to join on.

---

## 13. Invariants that must never break during migration

If any of these break during migration, pause and fix before continuing:

- Every cycle still produces at least 2 new hypotheses (PM invariant)
- Every opportunity card still has VLM-verified pins + inline chart + topline impact (DS invariant)
- Every human comment still gets responded to within 1 cycle (RLHF invariant)
- No autonomous modifications to `quality_patterns.md` equivalent (Curator invariant — humans merge)
- Every agent run still logs to `cycle_log.jsonl`, even on failure (observability invariant)

---

## Change log

- **2026-04-19:** Doc initialized. Mental model locked (pipeline + 4-concern framework). Invariants ordered: I-1 (observability) > I-2 (correctness) > I-3 (discoverability). Migration sketched as 6 phases; no dates committed.
