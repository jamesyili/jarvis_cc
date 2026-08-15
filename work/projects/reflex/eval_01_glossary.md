# Reflex Eval & Evolve — Glossary

**Purpose:** there are seven distinct datasets in the Reflex eval program, and a mechanism vocabulary shared with GEPA that does not always mean the same thing on both sides. This file fixes one canonical name per object and records every alias in the wild, so a sentence in a review comment can't quietly mean two things.

Written 2026-08-14 because the terminology collided in James's own working session — the strongest available evidence that it will collide in the group's. **Extended 2026-08-15** after the GEPA paper, the DSPy implementation, and SkillOS were read into the KB: Part A gained two objects, and Part B was added because the most dangerous collision found so far — "Pareto" — is not a dataset name at all.

**This is also the work-leo transfer artifact.** A work-leo session shares no state with this one. This file plus `eval_00_hub.md` is the intended cold-start pair.

---

# Part A — Datasets

## The two questions that separate every dataset

Every set below is fully specified by two answers. Nothing else matters for telling them apart.

1. **Where do its labels come from?** A human grading a card, or the world recording an outcome.
2. **Who is allowed to optimize on it?** A specific optimizer, or nobody.

That's it. All five objects are combinations of those two answers.

---

## The seven objects

| # | Canonical name | What it is | Labels come from | Who may optimize on it | What it catches | Status today |
|---|---|---|---|---|---|---|
| 1 | **Judge calibration set** | Cards with human labels (binary pass/no-pass + rationale) | Humans grading cards | **Chao's judge GEPA loop** | Judge-human misalignment | ~20 PM-graded cards via Asana forms |
| 2 | **Judge holdout** | Human-labeled cards withheld from judge optimization | Humans grading cards | **Nobody** — judge is scored on it | Judge overfit to the calibration set | **Does not exist** (the §B.6 gap) |
| 3 | **Evolve fixture bank** | The recorded Asana/Presto/MCP snapshots each candidate playbook runs against | n/a — inputs, not labels | **Janvi's playbook GEPA loop** | Nothing; it's the training input | Specified in the TDD |
| 4 | **Lockbox** | Human-labeled cards, frozen, entering *no* optimizer's objective — not judge GEPA, not playbook GEPA, not the Feedback Curator | Humans grading cards | **Nobody** — everything scores on it, nothing tunes on it | The whole stack fooling itself; leakage; overfit | One-pager drafted; posting unconfirmed |
| 5 | **Hindsight set** | World-at-T snapshots + the record of what actually shipped or proved out between T and T+n | **History** — outcomes, not opinions | **Nobody** — read periodically as a drift check | Construct failure: optimizing legibility instead of discovery | v0 scoped; blocked on work-side data |
| 6 | **Pattern store** (`quality_patterns.md`) | The Curator's institutional memory, read by PM/DS agents and the Skeptic each cycle | n/a — memory, not labels | **The Feedback Curator** writes it (human-merged); Detect agents consume it | Nothing directly — but it is the **third channel** by which graded-card information re-enters the system (§9) | Live; 341 lines at cycle 13, unmeasured since |
| 7 | **Curator evaluation groups** | Lineage-linked runs of *related* cycles, used to ask whether a curation decision helped a later related card | Outcomes of later cards in the same lineage | **Nobody today** — would be the Curator's fitness set if it is ever tuned | Curator accretion: patterns that are written but never help anything | **Does not exist**; §1.5's `Evidence:` cycle/card lineage is the grouping key |

### Why 6 and 7 belong in a dataset table

Object 6 has no labels, which is also true of the fixture bank — both are inputs, and the table is organized by *access rules*, not by label type. §9's contamination finding is precisely an access rule: calibration and lockbox cards must be excluded from pattern extraction, or scores self-inflate.

Object 7 is the one with a structural requirement that conflicts with the others. **Judge evaluation needs cards spread across cycles; Curator evaluation needs cards grouped within a lineage.** Lesson 6 treated cycle-clustering as a statistical nuisance that shrinks effective n; SkillOS's largest single ablation showed the same clustering *is the training signal* for curation (random task sequences cost more than removing either reward term). Both are true. They are different datasets and cannot be the same set.

### The distinction that actually matters: 4 vs 5

Both are frozen. Both are optimized on by nobody. That's why they blur. Here is the difference:

- **Lockbox: humans grade cards.** Same construct as the judge. Answers *"is this number real, or did we leak?"* → **internal validity.**
- **Hindsight set: history grades outcomes.** Different construct entirely. Answers *"is this number measuring the thing I care about?"* → **construct validity.**

A perfect lockbox score with a flat hindsight number means the loop is optimizing card legibility. The lockbox cannot detect that — it is scored by the same judge, so it reports the same construct error with a clean conscience. **This is the reason both must exist.** They are not redundant frozen sets; they catch different failures, and Lesson 6 vs Lesson 7 is exactly this split.

### 1 vs 4 — the other easy confusion

Both are human-graded cards. The difference is permission, not content: the calibration set is *training data for the judge*; the lockbox is *the sealed exam nobody studies from*. If the two are ever drawn from the same pool without an explicit split, the lockbox is already contaminated on day one.

---

## Aliases in the wild — what each source doc calls these

| Object | Appears as | Where |
|---|---|---|
| 1 — Judge calibration set | "graded cards", "human-labeled cards", "the ~20 cards", "Phase 1 labels" | Chao's proposal; session notes |
| 2 — Judge holdout | "held-out split", "leave-one-out CV" | §B.6 of the critique doc |
| 3 — Evolve fixture bank | **"case bank"**, "fixture store", "fixtures", "cases" | Janvi's TDD; §12 of the critique doc |
| 4 — Lockbox | **"ultimate holdout"** (James's notes), **"golden set"** (James, 7/24 meeting), "frozen holdout", "sealed cases" | James's notes; §E.3; the lockbox one-pager |
| 5 — Hindsight set | **"hindsight-recall case bank"**, "the anchor", "outcome anchor" | §E.4, §G of the critique doc |
| 6 — Pattern store | "quality_patterns", "institutional memory", "patterns file", **"SkillRepo"** (SkillOS's name for the same object) | Curator design doc; §9 of the critique doc; SkillOS |
| 7 — Curator evaluation groups | **"grouped task streams"** (SkillOS), "task groups", "lineage" | SkillOS §3.2.1; §1.5 `Evidence:` field |
| — | "recall gold set" — a *different* thing again: past PM roadmaps used as a recall reference. Critiqued in §B.5 and being replaced by object 5 | Chao's proposal |

---

## Live collisions to defuse

*Three found 8/14 (dataset names); three more found 8/15 (mechanism names, see Part B).*

1. **"case bank" means two different objects.** Janvi's TDD uses it for the Evolve fixture bank (object 3, optimized on). The critique doc uses it for the hindsight set (object 5, never optimized on). These have *opposite* access rules. Saying "the case bank" in the working session will be understood as object 3 by everyone who read the TDD. **Fix: retire the phrase entirely.** Use "fixture bank" and "hindsight set."

2. **"golden set" / "gold set" means two different objects, in two live documents.** James's 7/24 on-record comment — *"hold out a golden set if using GEPA"* — means the **lockbox** (object 4). Chao's proposal uses "recall gold set" for the **PM-roadmap recall reference**. Anyone reconciling the meeting notes against the proposal will merge them. **Fix: retire "gold/golden set" from all Reflex eval writing.** It is unrecoverable.

3. **"holdout" is ambiguous between objects 2 and 4.** The judge holdout is a judge-scoped test set; the lockbox is program-scoped. **Fix: never use bare "holdout" — always "judge holdout" or "lockbox."**

---

## Canonical vocabulary (use these, retire the rest)

**Use:** judge calibration set · judge holdout · Evolve fixture bank · lockbox · hindsight set · pattern store · Curator evaluation groups

**Retire:** case bank · gold set · golden set · bare "holdout" · "ultimate holdout" (→ lockbox) · "the anchor" as a standalone noun (→ "the hindsight set," describing it as the anchor) · bare **"Pareto"** (→ instance-Pareto / dimension-Pareto) · bare **"harness"** (→ agent / eval / synthesized harness)

---

## The one-paragraph version

> Humans grade cards. Some of those grades train the judge (**calibration set**); some are withheld to check the judge didn't just memorize them (**judge holdout**); and some are sealed away from every optimizer in the program so we can tell whether the whole stack is fooling itself (**lockbox**). Separately, the playbook optimizer runs candidates against recorded world-snapshots (**Evolve fixture bank**). And finally, one set is graded not by humans at all but by history — what actually shipped and proved out (**hindsight set**) — because every other number in the program is ultimately somebody's opinion of a card, and only that one can tell us whether we're finding things or just writing well.

---

# Part B — Mechanisms and terms

Added 2026-08-15. Part A fixes the *nouns for data*. This part fixes the *nouns for machinery*, because the worst collision in the program turned out to live here. Lessons 15–17 (AutoHarness, EvoHarness-RL, the two recsys papers) will add to this section.

## Collision 4 — "Pareto" means two unrelated things, in the same conversation

This is more dangerous than any collision in Part A, because both senses are live in the *same* review thread rather than in two documents read by different people.

| | **GEPA's Pareto** (paper §3.1, Alg. 2) | **Evolve's Pareto gate** (Janvi's TDD) |
|---|---|---|
| Axes are | **task instances** — one objective per case in `D_pareto` | **judge rubric dimensions** — 5 axes |
| It decides | *which parent to mutate next* — a sampling distribution | *whether a candidate is accepted* — a pass/fail gate |
| Mechanism | keep candidates that lead on ≥1 instance, prune dominated, sample ∝ instances led | require the child to no-worse-dominate the parent on all axes |
| Prevents | local optima / premature convergence | (intended) accepting a candidate that regresses a dimension |
| Axis correlation | not a hazard — more instances is a richer frontier | correlated axes make domination easy → false-accept rate rises toward 50% (item 16) |

**The fact that settles it:** GEPA's *acceptance* test is a plain scalar — average minibatch score before vs. after, accept if improved (Alg. 1 lines 13–14). Multi-objective reasoning appears nowhere in acceptance. **GEPA therefore cannot be cited in support of a Pareto acceptance gate.**

**Fix:** never write bare "Pareto." Use **"instance-Pareto (parent selection)"** or **"dimension-Pareto (acceptance gate)."**

## Collision 5 — `blame()` implies a GEPA provenance it does not have

GEPA has no `blame()`. Module selection is `SELECTMODULE` at Algorithm 1 line 8, and the policy is **round-robin**; the DSPy implementation agrees (`component_selector="round_robin"` by default, `RoundRobinReflectionComponentSelector`). Credit assignment in GEPA is *implicit* — the reflection LM reads the trace — or it is *supplied by the feedback function*, never computed by a selector.

Anyone reading the TDD will assume `blame()` is standard GEPA machinery. It is a **departure** from the configuration GEPA's published results were measured on.

**Fix:** when writing or reviewing, say **"`blame()` (Reflex-specific; GEPA's default is round-robin)"** on first use.

## Collision 6 — "harness" has three meanings in the sources now in the KB

| Sense | Used by | Means |
|---|---|---|
| The scaffold around the model — prompts, tools, loop, context management | Anthropic long-running-agent post; DSPy | everything that isn't the weights |
| **Fixture and eval infrastructure** | `louis-wang/the-harness-is-the-moat`; Reflex internal usage | the recorded-snapshot + replay plumbing |
| A **synthesized code artifact** the agent runs inside | AutoHarness, EvoHarness-RL | generated scaffolding code, the thing being optimized |

**Fix:** qualify it — "agent harness," "eval harness," or "synthesized harness." Bare "harness" in a cross-team doc will be read in whichever sense the reader last encountered.

## GEPA ↔ Reflex mapping

For reading the GEPA paper or DSPy source against the TDD.

| GEPA / DSPy | Reflex | Note |
|---|---|---|
| candidate | candidate playbook / spec version | |
| candidate pool `P`, ancestry `A` | `versions/vN.md` + version history | |
| Reflective Prompt Mutation | the mutation step | |
| `SELECTMODULE` (round-robin) | `blame()` | **not equivalent** — see Collision 5 |
| feedback function `µf` / `GEPAFeedbackMetric` | the judge, extended | `pred_name` + `pred_trace` are where per-component credit legitimately enters |
| `D_feedback` (minibatch source) | fixture bank slice per generation | |
| `D_pareto` (selection/validation set) | — | **no Reflex equivalent named** |
| minibatch improvement test (Alg. 1 L13–14) | — | Reflex uses the dimension-Pareto gate here instead |
| `candidate_selection_strategy` = `"pareto"` \| `"current_best"` | — | makes the exploration ablation a one-line config change |
| System-Aware Merge (`use_merge`) | — | not in the TDD |
| rollout budget | the 450-invocation budget | GRPO's entry ticket on IFBench was 24,000 rollouts; GEPA's was 678 |

## SkillOS ↔ Reflex mapping

| SkillOS | Reflex |
|---|---|
| frozen agent executor `π_L` | PM Agent / DS Agent |
| skill curator `π_S` | **Feedback Curator** |
| SkillRepo | `quality_patterns.md` (object 6) |
| `insert_skill` / `update_skill` / `delete_skill` | intake (§1.3.1) / conflict resolution (§1.3.2) / decay handling (§1.3.3) |
| BM25 retrieval | ranked pattern lookup (§1.3.4) |
| grouped task streams | Curator evaluation groups (object 7) |
| compression reward `r_comp` | **no equivalent** — see `eval_04_curator_measurement_proposal.md` §4.2 |
| — | lineage / audit trail (§1.3.5) — **SkillOS has no equivalent** |

## Terms to pin (Reflex-internal, no external analogue)

**fitness** — the judge's output used as the optimization objective. Always qualify with judge version; cross-generation comparisons are only valid within one judge version (§2). · **landing re-run** — re-execution of an accepted candidate before it lands. · **`never_mutable`** — glob-based protection on files; does *not* protect prose spans inside mutable files (the Lesson 4 gap). · **shadow validation** — evolved spec run beside the incumbent on the next live rotation, proposed in §12, not in the TDD. · **`is_pareto_axis`** — TDD flag defaulting to `true`, which silently promotes any new diagnostic metric into a gate axis (§11).

---

## Related

- Working state, undelivered critique, IC lane: `eval_00_hub.md`
- Lockbox protocol (for Chao): `eval_02_judge_lockbox_protocol.md`
- Evolve feedback + EvalResult v2 contract (for Janvi): `eval_03_evolve_feedback_and_contract.md` — the `case_source` field is where these distinctions become machine-enforceable
- Curator design: `reflex_feedback_curator_and_skeptic.md` (objects 6 and 7 live here)
- Curator measurement proposal (for the Curator owner): `eval_04_curator_measurement_proposal.md`
- Primary sources in the KB: `kb/hard/raw/arxiv/gepa-reflective-prompt-evolution-can-outperform-reinforcement-learning.md` · `kb/hard/raw/dspy/dspy-gepa-reflective-prompt-optimizer.md` · `kb/hard/raw/arxiv/skillos-learning-skill-curation-for-self-evolving-agents.md`
