# Reflex Codebase Guide

**Last updated:** 2026-05-10
**Branch:** james/detect-structured-state

---

## What Reflex Is

Reflex is a **self-healing discovery stack** for Pinterest's Homefeed (and broader discovery surfaces). It's a 4-stage pipeline where AI agents continuously Detect opportunities, Build fixes, Simulate impact, and Prove results. Humans shift from manual ML iteration to system supervision: defining "good," setting guardrails, and improving the meta-system.

The key architectural decision: **Claude Code sessions ARE the agents.** There's no custom orchestrator, no agent framework, no LLM SDK. Each agent is a `.md` prompt file. You dispatch by opening Claude Code in the `reflex/` directory and telling it to run an agent. The repo itself is the system state. Git is the audit trail.

---

## Pipeline Stages

```
Detect ──→ Build ──→ (Simulate) ──→ (Prove)
  │           │
  │ Asana     │ Code edits
  │ cards     │ in target repos
  ▼           ▼
Prioritized   Validated
backlog       experiments
```

| Stage | Status | What it does |
|-------|--------|-------------|
| **Detect** | Mature (67+ cycles) | Continuously finds opportunities across Pinterest's discovery stack. Produces a prioritized Asana backlog. |
| **Build** | Working (1 agent, 1 started) | Consumes opportunities and generates validated code edits in target repos (Optimus, Pinboard, Pinconf). |
| **Simulate** | Future | Offline evaluation to estimate impact before live experimentation. |
| **Prove** | Future | Manages live experiments, monitors metrics, decides ship/revert. |

---

## Repository Structure

```
reflex/
├── infra/                         Shared schemas + JSONL I/O
│   ├── __init__.py
│   ├── log_append.py              Append-only JSONL persistence (33 lines)
│   └── schemas/
│       ├── __init__.py
│       ├── cycle_log.py           CycleLogEntry model
│       └── cost_ledger.py         CostLedgerEntry model
├── detect/                        Stage 1: Find opportunities
│   ├── agents/                    Agent prompts (PM, DS, Skeptic, Curator)
│   ├── playbooks/                 19 detection playbooks (16 active)
│   ├── capabilities/
│   │   └── analytical_checks/     36 named checks + registry
│   ├── state/                     Structured state (rotation, dead ends, logs)
│   ├── schemas/                   Card writing guides
│   ├── infra/                     Detect-specific schemas
│   ├── quality/                   Audit logs + proposed patterns
│   ├── queries/                   Discovered Presto tables
│   ├── CLAUDE.md                  Detect-specific instructions
│   ├── board_setup.md             Asana API reference
│   └── quality_patterns.md        Read-only archive of historical patterns
├── build/                         Stage 2: Generate validated code
│   ├── agents/                    Build agent prompts (CG Sizer, Blender Utility)
│   ├── infra/                     BuildValidator + Allowlist
│   ├── references/                Domain reference docs (542-line sizer pattern)
│   ├── state/                     Allowlist YAML + eval reports
│   ├── tests/                     Unit tests + eval scripts
│   └── scripts/                   Validation scripts
├── docs/                          Vision, architecture, references
│   ├── reflex-vision-two-pager.md The pitch document
│   ├── architecture.md            System architecture
│   ├── Detect_spec.md             Original Detect design brief
│   ├── setup.md                   Developer setup guide
│   ├── cg_reference.md            CG domain reference
│   ├── blender_reference.md       Blender pipeline reference
│   ├── blender_utility_reference.md  Utility weight config reference
│   ├── full_funnel_reference.md   Full funnel reference
│   ├── anticipation-p13n-vision-2026.md  Anticipation team vision
│   └── diagrams/                  7 Excalidraw iterations + PNGs
├── config.yaml                    Target repo paths + model config
├── pyproject.toml                 Python package definition
├── .claude/settings.local.json    ASANA_PAT (gitignored)
└── target_repos/                  Symlinks to optimus, pinboard, pinconf (gitignored)
```

---

## Shared Infrastructure (`infra/`)

The thinnest possible persistence layer — 3 files, ~55 lines total.

### `log_append.py`

```python
append_jsonl(path, entry)   # Serialize Pydantic model → append one line
read_jsonl(path, model)     # Read all lines → list of typed models
iter_jsonl(path, model)     # Lazy iterator over lines
```

### `schemas/cycle_log.py` — CycleLogEntry

Per-agent-run telemetry:
- `agent`: Literal["pm", "ds", "skeptic", "curator", "build_validator"]
- `run_id`: UUID for correlating with cost ledger entries
- `duration_s`: Wall-clock time
- `inputs`/`outputs`: Freeform dicts (agent-specific)
- `errors`, `validation_failures`: Lists for debugging

### `schemas/cost_ledger.py` — CostLedgerEntry

Per-LLM-call cost tracking:
- `agent`, `run_id`, `model`, `operation` (semantic op type)
- `capability` (which playbook/check was active)
- `input_tokens`, `output_tokens`, `cached_tokens`, `cost_usd`

---

## Detect Stage — Detailed Breakdown

### How It Works (The Reinforcement Loop)

```
Human drops a Rough Idea or Comment on Asana
        ↓
PM Agent (cycle N): reads feedback → researches → generates hypothesis cards
        ↓
DS Agent (cycle N): enriches → sizes impact → adds VLM verification → scores
        ↓
Skeptic: red-teams against known patterns → PASS/FAIL/NEEDS_HUMAN
        ↓
Human reviews the opportunity card → leaves feedback
        ↓
Feedback Curator: structures feedback → updates dead_ends, analytical_checks, rotation stats
        ↓
PM Agent (cycle N+1): reads updated state → runs better playbooks → generates better hypotheses
```

Every human correction becomes a permanent system pattern that prevents the same mistake from recurring. This is why the system compounds.

### Agents (`detect/agents/`)

#### PM Agent (`pm_agent.md`, ~380 lines)

The discovery engine. Execution flow:
1. **Phase 0** — Human feedback first (HIGHEST PRIORITY). Process Rough Ideas, respond to all reviewer comments, read structured state files.
2. **Phase 1** — Strengthen existing hypotheses in queue.
3. **Phase 2** — Run exactly 3 playbooks (rotating through 16 active). Check `rotation.yaml` for next-up.
4. **Phase 3** — Enrich findings with Knowledge MCP context.
5. **Phase 4** — Deduplicate (title AND thematic level) against existing board.
6. **Phase 5** — Create hypothesis tasks on Asana. Re-prioritize the queue.
7. **Phase 6** — Reflect. Update rotation.yaml, evolve playbooks, update analytical checks.
8. **Phase 6b** — Full playbook audit every 6th cycle (after complete rotation).
9. **Phase 7** — Cycle summary.
10. **Phase 8** — Append structured cycle log entry.

Key constraints: minimum 2 new hypotheses per cycle, never reduce cycle frequency, cover all 5 surfaces (Homefeed, Search, Related Pins, Notifications, Landing Pages).

#### DS Agent (`ds_agent.md`, ~350 lines)

The enrichment engine. Takes hypotheses → matures to opportunities:
- Phase 0: Human feedback on Opportunities section (same RLHF priority)
- Reads structured state (analytical checks registry, dead ends)
- Quantifies impact in SSv2/DAU terms
- Runs VLM verification on pin examples (transformed quality — pins actually show what's claimed)
- Designs contradiction queries to disprove hypotheses
- Cross-references experiment history
- Scores: Signal * 0.4 + Impact * 0.4 + Readiness * 0.2
- Transitions to Opportunities section with proper tags

#### Skeptic (`skeptic.md`, ~200 lines)

Adversarial pre-review gate. 6 check taxonomy:
1. Pattern Check — against analytical_checks registry
2. Context Check — against dead_ends, known failing approaches
3. Evidence Check — are claims properly supported?
4. Internal Consistency — do sections contradict each other?
5. Novelty — does this add something the board doesn't have?
6. (Composite) — architectural principles, prior Curator corrections

Emits structured `SkepticVerdict` (PASS/FAIL/NEEDS_HUMAN) with per-check outcomes.

Self-calibrates: reads its own verdict_log.jsonl to check precision (human_agreed rate) and adjust confidence levels.

#### Feedback Curator (`feedback_curator.md`, ~200 lines)

Institutional memory custodian. Triggered by:
- New Asana comments on Opportunity/Build tasks
- Skeptic overrides (human approved what Skeptic failed)
- Scheduled audit (every 6 cycles)
- Direct invocation

Outputs:
- Proposed pattern entries (→ analytical_checks/ or dead_ends.yaml)
- Conflict reports (when patterns contradict)
- Decay flags (when patterns reference changed systems)

Key principle: does NOT generate new patterns on own initiative. Only shapes human-surfaced corrections into structured entries.

### Playbooks (`detect/playbooks/`)

19 files, 16 active in rotation. Each playbook is a structured detection routine defining:
- What to detect and why
- Data sources and specific queries
- Interpretation thresholds
- How to formulate the hypothesis

**Data-driven (10 active):**
| Playbook | What it finds |
|----------|--------------|
| `metric_anomaly` | Declining DAU/MAU, WAU, SSv2, pRelevance by market/segment |
| `relevance_gaps` | pRelevance gaps by segment x market x surface x query class |
| `market_cg_performance` | Market engagement decline decomposed by CG source vs US baseline |
| `engagement_decomposition` | SSv2 sub-action decomposition, user engagement profiles, session patterns |
| `explicit_signals` | Hides, reports, "see more/less", search refinements, unfollows |
| `ranking_feature_performance` | Ranking feature calibration, utility weights, pinnability thresholds |
| `filter_bubble` | Explore/exploit imbalances by segment |
| `supply_gaps` | Content supply gaps by query class x market |
| `follow_graph_health` | Input signal freshness: stale follows, boards, interests |
| `retention_decomposition` | Good relevance but poor retention: growth accounting, churn velocity |

**Experiment-driven (3 active):**
| Playbook | What it finds |
|----------|--------------|
| `experiment_review` | Recently completed experiments: unported wins, failures with learnings |
| `experiment_doubledown` | Deep-read winners, trace idea source, find expansion vectors |
| `surface_transfer` | Cross-surface transfer debt (features on one surface but not others) |

**Qualitative (1 active, 2 retired):**
| Playbook | Status | What it finds |
|----------|--------|--------------|
| `internal_feedback` | Active | Slack channels: expert observations, recurring complaints |
| `external_feedback` | RETIRED | No external data access (Reddit, App Store) |
| `research_frontier` | RETIRED | No research literature access |

**Strategic (3 active):**
| Playbook | What it finds |
|----------|--------------|
| `team_roadmap_gaps` | Gaps between team plans/PRDs and data-driven priorities |
| `codebase_analysis` | Source code analysis: hardcoded params, config asymmetries, disabled features |
| `ranker_calibration_audit` | Per-segment O/E ratios for 8 production ranker heads (newest, added by Sam) |

### Analytical Checks (`detect/capabilities/analytical_checks/`)

36 named checks — the system's accumulated "quality antibodies." Discovered organically across 67+ cycles of operation.

**Registry (`registry.yaml`):** Master index. Each entry has:
- `id`, `name`, `verdict` (mandatory / high_value / standard)
- `mandatory_when` (condition that triggers this check)
- `applies_to` (which surfaces)
- `discovered_cycle`

**Verdict levels:**
- **Mandatory (10):** Must apply when condition is met. Examples: VLM verification (ALWAYS), contradiction testing (every task), experiment holdout status check (any CG task), CG decomposition normalization.
- **High-value (24):** Should apply when relevant. Examples: CG source decomposition, user state decomposition, market x CG decomposition, O/E calibration analysis, wiki currency verification.
- **Standard (2):** Apply when relevant. Examples: gate-vs-ranking distinction, experiment holdout closure.

Each check has a full `.md` file with methodology steps, gotchas, and provenance. Example (`observed_expected_calibration.md`):
- Method: reliability table (decile-binned), global O/E, ECE, segment cuts, sizing
- Gotchas: apply contradiction_testing, check both raw and post-overlay scores
- Applied to: ranker_calibration_audit (cycle 68+)

### State Files (`detect/state/`)

| File | Format | Records | Purpose |
|------|--------|---------|---------|
| `rotation.yaml` | YAML | — | Playbook rotation tracker. Current pointer (position 6/16), per-playbook stats (cycles_run, hypotheses_generated, promoted_to_opportunities, conversion_rate, role description), next_up queue, retired list, board snapshot. |
| `dead_ends.yaml` | YAML | 23 entries | Typed registry of approaches that fail. Categories: table_columns (10), table_joins (3), asana_api (4), mcp_usage (1), analytical_proxy (2), experiment_status (1), structural (3). Each has: pattern, why_it_fails, correct approach, severity (auto_fail/warn). |
| `cycle_log.jsonl` | JSONL | 6 entries | Run telemetry. Cycles 66-67 + early config_agent attempts. |
| `cost_ledger.jsonl` | JSONL | — | Per-LLM-call cost records. |
| `verdict_log.jsonl` | JSONL | — | Skeptic verdicts with human_agreed backfill. |
| `expert_judgments.jsonl` | JSONL | 9 entries | Curator-structured expert feedback. |
| `disagreements.jsonl` | JSONL | — | Expert disagreements on specific claims. |
| `pattern_provenance.jsonl` | JSONL | — | Where patterns originated. |

### Detect-Specific Schemas (`detect/infra/schemas/`)

| Model | Fields | Purpose |
|-------|--------|---------|
| `SkepticVerdict` | card_gid, verdict (PASS/FAIL/NEEDS_HUMAN), checks[], fail_reasons[], confidence, human_agreed | Structured critique output |
| `ExpertJudgment` | expert, card_gid, judgment_type (agree/disagree/reframe/extend/retire/new_info/question/approve), rationale_verbatim, confidence, source | Curator captures expert input |
| `Disagreement` | card_gid, claim_targeted, positions[] (min 2 distinct experts), resolution state | When experts disagree |
| `PatternProvenance` | — | Tracks where patterns came from |

### Expert Registry (`detect/infra/experts.yaml`)

8 canonical experts with role mapping:
- james_li (em_hf_cg), andrew_y (sr_director_product), dylan_wang (em_hf_ranking_retrieval)
- anna_k (pm_retentive_recs), matt_chun (pm_upp), tim_chu (em_homefeed_infra)
- dhruvil_badani (em_homefeed_peer), rahul_goutam (em_blending_hf)

Curator normalizes Asana commenter names/GIDs to canonical IDs.

### Quality System (`detect/quality/`)

**Audit logs** (`audit-logs/`): 7 historical logs documenting Skeptic backfills (v1, v2, v3) and Curator runs (v3, v4). The latest (2026-05-03_curator-v4.md) shows: 56 tasks scanned, 9 new human comments processed, 9 ExpertJudgments written, 2 dead ends added.

**Proposed patterns** (`proposed/`): 5 patterns awaiting human approval:
- board-state-desync-detection
- duplicate-abandoned-experiment-pattern
- non-activation-as-revealed-preference
- trust-safety-hidden-pins-dec-not-ghost
- utility-weight-path-correction

### Other Detect Files

**`board_setup.md`** — Complete Asana REST API reference: project GID, section GIDs, tag GIDs, curl command templates for every operation (list tasks, create task, move to section, add tag, read comments, upload attachment).

**`quality_patterns.md`** — Read-only archive. Historical cycle learnings (cycles 1-65), task quality rankings (star ratings for each opportunity card), presentation patterns. This was the original "god file" before being decomposed into structured state.

**`queries/README.md`** — 12+ discovered Presto tables documented in detail (key columns, gotchas, correct usage, how they were found). Tables include: northstar_user_ge_metrics, core_successful_sessions_user_agg_v2, hf_relevance_survey_responses_2025, engagement_stats, and more.

---

## Build Stage — Detailed Breakdown

### How It Works

```
Opportunity card on Asana (scored, prioritized, Skeptic-passed)
        ↓
Human dispatches Build Agent with card URL/GID
        ↓
Agent: fetches card → clarifies spec (PM subagent) → presents proposal
        ↓
Human approves proposal
        ↓
Agent: reads references → reads target files → generates edits
        ↓
BuildValidator: checks allowlist → enforces diff cap → applies (or dry-run)
        ↓
Output: validated code ready for PR
```

### Agents (`build/agents/`)

#### CG Sizer Build Agent (`cg_sizer_build_agent.md`, ~200 lines)

The most developed Build agent. Generates CG (Candidate Generation) sizer experiment code in Optimus (Java).

Workflow:
1. **Parse task GID** from Asana URL or raw GID
2. **Move card to Build column** (board state tracking)
3. **Fetch card content + comments** via Asana REST API
4. **Extract known fields:** CGs, budget direction, target segment/market, experiment type, metric target, prior experiments
5. **Identify gaps** for code generation (FeedSourceIdentifier constants, budget semantics, market gating, pattern type A-F, post-LWS placement, ANN cap coordination, parent experiment)
6. **Clarify with PM subagent** (dispatches a Claude Code subagent with domain context)
7. **Present concrete proposal** for human approval
8. **Read references** (`cg_sizer_pattern.md`, `cg_pipeline_overview.md`)
9. **Read target files** from `target_repos/optimus`
10. **Generate edits** following the pattern reference
11. **Validate through BuildValidator** (allowlist + diff cap)

Supports:
- **Tier 1:** Single-file changes (SizerExperiments.java only)
- **Tier 2+:** Multi-file (SizerExperiments.java + Sizer.java + HomefeedExperimentUtils.java), post-LWS placement, ANN cap overrides, shopping learned retrieval utils

#### Blender Utility Build Agent (`blender_utility_agent.md`, ~100 lines)

Generates blender utility weight experiment configs in Pinconf (JSON).

Workflow:
1. Load `blender_utility_reference.md` (config loading mechanism, weight structure, PinTag hierarchy, contextual overrides, weight catalog, format examples)
2. Read current production config from `target_repos/pinconf`
3. Generate experiment config with modified weights
4. Validate through BuildValidator

### BuildValidator (`build/infra/validator.py`, 185 lines)

The guardrails layer. Entry point: `validate_and_apply(rel_path, new_content)`

What it does:
1. **Allowlist check** — Is this path permitted? (raises `AllowlistViolation` if not)
2. **Read current file** — Gets the original content from target repo
3. **Diff size check** — Counts changed lines via `difflib.unified_diff`. Enforces per-team cap.
4. **Apply** — Writes the file (unless dry_run=True)
5. **Cycle logging** — `emit_cycle_log()` writes a CycleLogEntry

Also provides:
- `read_file(rel_path)` — Public method for subagents to read target repo files
- `load_references()` — Concatenates all `build/references/*.md` files

### Allowlist (`build/infra/allowlist.py`, 83 lines)

Blast-radius contract. Loads from `build/state/allowlist.yaml`.

Features:
- Exact path matching AND glob patterns (`fnmatch`)
- Per-team diff caps (different teams can have different limits)
- Approval tracking (who approved, when)

Current allowlist (`build/state/allowlist.yaml`):
- **Team:** hf_cg_team
- **Approved by:** james_li, andrew_y (2026-05-08)
- **6 paths:** SizerExperiments.java, Sizer.java, HomefeedExperimentUtils.java, HomefeedExperimentUtils (Unity-side), MuseConditionalEmbeddingsToWebPinsUtils.java, HomefeedShoppingLearnedRetrievalUtils.java, Pinconf utility configs, Pinboard L2 utility
- **Max diff:** 150 lines per file

### References (`build/references/`)

**`cg_sizer_pattern.md` (542 lines)** — The definitive guide for CG sizer code generation:
- File locations and roles (SizerExperiments.java, Sizer.java, HomefeedExperimentUtils.java)
- Java patterns: experiment group parsing, token extraction, budget override mechanics
- All 6 experiment pattern types (A through F)
- Post-LWS placement guide (exact retrieval counts vs pre-overfetch values)
- ANN cap override coordination for CLR experiments
- Naming conventions and stats emission patterns
- Real PR examples cited (#162579, #163055, #164917)

**`cg_pipeline_overview.md`** — How CG sizing fits in the overall Homefeed serving pipeline.

### Tests (`build/tests/`)

| File | Type | What it tests |
|------|------|--------------|
| `test_build_validator.py` (241 lines) | Unit | Allowlist loading, path validation (exact + glob), diff size enforcement, cycle log emission, diff counting (including insertion edge case) |
| `test_sizer_tier1.py` | Manual eval | Validates single-file sizer edits |
| `test_sizer_tier2.py` | Manual eval | Validates multi-file Tier 2 edits (3 files) against BuildValidator |
| `eval_tier2_graphsage_to_plp.py` | Eval | Validates against real PR #163055 (GraphSage-to-PLP budget) |
| `eval_tier2_shopping_holdout.py` | Eval | Validates against real PR #164917 (Shopping holdout) |

### Eval Reports (`build/state/eval_reports/`)

- `2026-04-28-graphsage-to-plp.md` — Results of evaluating generated code against the real PR
- `2026-04-28-shopping-holdout.md` — Results of evaluating generated code against shopping holdout PR

---

## Documentation (`docs/`)

### Vision & Strategy

| Doc | Purpose | Key content |
|-----|---------|-------------|
| `reflex-vision-two-pager.md` | The pitch | Industrial revolution metaphor. Detect→Build→Simulate→Prove. "100x lever on quality improvement." April 2026 update with PoC results. |
| `anticipation-p13n-vision-2026.md` | Team context | Anticipation team's personalization vision. Workstreams that Reflex opportunities tie to. |
| `Detect_spec.md` | Original design | James's initial Detect specification (Kanban board, two agents, continuous operation). |

### Architecture & Setup

| Doc | Purpose |
|-----|---------|
| `architecture.md` | Pipeline stages, agent inventory, data flow (Mermaid), shared infra, external systems, state files |
| `setup.md` | Full developer setup: clone repos, symlinks, Python env, Asana PAT, verification commands |

### Domain References

| Doc | Purpose |
|-----|---------|
| `cg_reference.md` | CG (Candidate Generation) domain knowledge |
| `blender_reference.md` | Post-Stage-13 blender pipeline (presort → diversity → SSD → final chunk) |
| `blender_utility_reference.md` | Utility weight structure, PinTag hierarchy, config format, weight catalog |
| `full_funnel_reference.md` | Full discovery funnel reference |

### Diagrams (`docs/diagrams/`)

7 iterations of system architecture diagrams (Excalidraw source + rendered PNG):
- v1: humans-supervise
- v2: self-improvement-loop
- v3: agents-as-roles
- v4: end-to-end-pipeline
- v5: system-overview
- v6: systems-pipeline
- v7: self-improvement-loop (refined)

Plus `ideal.jpg` — target state visualization.

---

## External Systems Integration

| System | How accessed | Used by |
|--------|-------------|---------|
| **Asana** | REST API via curl + $ASANA_PAT | All agents (Kanban board management) |
| **Presto** | `mcp__presto__*` MCP tools | PM Agent, DS Agent (analytical queries) |
| **Experiments** | `mcp__experiments__*` MCP tools | PM Agent, DS Agent (experiment lookup) |
| **Knowledge** | `mcp__knowledge__*` MCP tools | PM Agent, DS Agent (internal docs) |
| **Slack** | `mcp__slack__*` MCP tools | PM Agent (internal_feedback playbook) |
| **Target repos** | Symlinks at `target_repos/` | Build agents (read/write code) |

**Note:** Asana MCP (`mcp__asana__*`) has persistent DNS failures — never used. All Asana operations go through curl.

---

## Key Design Principles

1. **Claude Code IS the runtime.** No custom orchestrator, no agent framework, no SDK dependency. Agents are prompts. The LLM is the execution engine.

2. **The repo IS the database.** rotation.yaml, dead_ends.yaml, cycle_log.jsonl — all state lives in version-controlled files. No external database.

3. **Git IS the audit trail.** Every agent run produces a commit showing what changed in state files.

4. **Human feedback is first-class (RLHF).** Every agent cycle processes human comments BEFORE doing automated work. Rough Ideas = strategic intent. Comments = correction signal. Both feed back into structured state permanently.

5. **Compounding intelligence.** Every cycle makes the next cycle better: new analytical checks, updated dead ends, evolved playbooks, sharper rotation stats. The system's quality floor rises monotonically.

6. **Blast-radius control.** Build agents can only write to explicitly approved paths with enforced diff caps. Extensions require sign-off.

7. **Append-only state.** JSONL logs are never edited in place (lesson learned — see Sam's review of cycle_log.jsonl deletion).

8. **Cover the full discovery stack.** Not just Homefeed — Search, Related Pins, Notifications, Landing Pages. Every card gets surface tag(s).

9. **Never reduce cycle frequency.** More cycles = more signal = better outcomes. A "mature" board is a higher baseline, not a reason to slow down.

---

## Current Operational Stats

- **Detect cycles completed:** 67+
- **Full rotations completed:** 9
- **Active playbooks:** 16 (2 retired, 1 new)
- **Analytical checks:** 36 (10 mandatory, 24 high-value, 2 standard)
- **Dead ends catalogued:** 23
- **Expert judgments captured:** 9
- **Board state:** ~47 opportunities, ~69 hypotheses (as of cycle 66)
- **Experts in rotation:** 8
- **Build agents:** 2 (CG Sizer operational, Blender Utility started)
- **Approved build paths:** 6 file patterns
- **Contributors:** James Li, Sam Owens (PR reviewer, ranker_calibration_audit author)

---

## What's In Flight (observed from branches)

| Branch | Purpose |
|--------|---------|
| `james/detect-structured-state` | Current branch — structured state decomposition, Tier 2+ Build Agent expansion |
| `add-pr-reviewer-skill` | PR reviewer skill for Reflex |
| `build/pinboard-pr-reviewer` | Pinboard-specific PR reviewer |
| `pr-reviewer/entry-points` | PR reviewer entry points |
| `pr-reviewer/lint-engine` | PR reviewer lint engine |
| `pr-reviewer/rules-library` | PR reviewer rules library |
| `detect-methodology-embed` | Detect methodology embedding |
