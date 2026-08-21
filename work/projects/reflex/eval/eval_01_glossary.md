# Reflex Eval & Evolve — Glossary

**Purpose:** there are seven distinct datasets in the Reflex eval program, and a mechanism vocabulary shared with GEPA that does not always mean the same thing on both sides. This file fixes one canonical name per object and records every alias in the wild, so a sentence in a review comment can't quietly mean two things.

Written 2026-08-14 because the terminology collided in James's own working session — the strongest available evidence that it will collide in the group's. **Extended 2026-08-15** after the GEPA paper, the DSPy implementation, and SkillOS were read into the KB: Part A gained two objects, and Part B was added because the most dangerous collision found so far — "Pareto" — is not a dataset name at all. **Revised 2026-08-16** (synced to repo 8/20 from `reflex_eval_evolve_notes_0816.html`): objects renumbered (pattern store → 5, Curator evaluation groups → 6), object 7 renamed **Record of System Launches** (was "Hindsight set", now an alias), the **2-vs-4** section added (James's question), and Part B reworked — the Pareto collision expanded into the load-bearing argument for `eval_03` §1–2, and `blame()` upgraded from a naming fix to an **open design question for Janvi and Chao**.

**This is also the work-leo transfer artifact.** A work-leo session shares no state with this one. This file plus `eval_00_hub.md` is the intended cold-start pair.

---

# Part A — Datasets

## The two questions that separate every dataset

Every set below is fully specified by two answers. Nothing else matters for telling them apart.

1. **Where do its labels come from?** A human grading a card, or the world recording an outcome.
2. **Who is allowed to optimize on it?** A specific optimizer, or nobody.

That's it. All seven objects are combinations of those two answers.

---

## The seven objects

| # | Canonical name | What it is | What it catches | Who may optimize on it | Labels come from | Status today |
|---|---|---|---|---|---|---|
| 1 | **LLM Judge calibration set** | Cards with human labels (binary pass/no-pass + rationale) | Judge-human misalignment | **LLM judge GEPA loop** (Chao's) | Humans grading cards | ~20 PM-graded cards via Asana forms |
| 2 | **LLM Judge holdout** | Human-labeled cards withheld from judge optimization | Judge overfit to the calibration set | **Nobody** — the LLM judge is scored on it | Humans grading cards | Needs to be built (the §B.6 gap) |
| 3 | **Evolve fixture bank** | The recorded Asana/Presto/MCP snapshots each candidate playbook runs against | Nothing; it's the training input | **Janvi's playbook GEPA loop** | n/a — inputs, not labels | Specified in the TDD |
| 4 | **Ultimate holdout / Lockbox** | Human-labeled cards, frozen, entering *no* optimizer's objective — not judge GEPA, not playbook GEPA, not the Feedback Curator | The whole stack fooling itself; leakage; overfit | **Nobody** — everything scores on it, nothing tunes on it | Humans grading cards (ideally periodically refreshed) | Needs to be built |
| 5 | **Pattern store** (`quality_patterns.md`) | The Curator's institutional memory, read by PM/DS agents and the Skeptic each cycle | Nothing directly — but it is the **third channel** by which graded-card information re-enters the system (§9) | **The Feedback Curator** writes it (human-merged); Detect agents consume it | n/a — memory, not labels | Live; 341 lines at cycle 13, unmeasured since |
| 6 | **Curator evaluation groups** | Lineage-linked runs of *related* cycles, used to ask whether a curation decision helped a later related card | Curator accretion: patterns that are written but never help anything | **The Feedback Curator** | Outcomes of related cards | Needs to be built, ideally with some notion of cycle / card lineage to help define "relatedness" |
| 7 | **Record of System Launches** | World-at-T snapshots + the record of what actually shipped or proved out between T and T+n | Construct failure: optimizing legibility instead of discovery | **Nobody** — read periodically as a drift check | History: system-level outcome snapshots to help ensure construct validity | Needs to be built in a way that keeps track recurringly (e.g. monthly) of what ended up shipping |

### Why 5 and 6 belong in a dataset table

**Object 5 (pattern store)** has no labels, which is also true of the fixture bank — both are inputs, and the table is organized by *access rules*, not by label type. §9's contamination finding is precisely an access rule: calibration and lockbox cards must be excluded from pattern extraction, or scores self-inflate.

**Object 6 (Curator evaluation groups)** is the one with a structural requirement that *conflicts* with the others. Judge evaluation needs cards spread *across* cycles; Curator evaluation needs cards grouped *within* a lineage. Lesson 6 treated cycle-clustering as a statistical nuisance that shrinks effective n; SkillOS's largest single ablation showed the same clustering is the *training signal* for curation (random task sequences cost more than removing either reward term). Both are true. They are different datasets and cannot be the same set.

### The distinction that actually matters: 4 vs 7

Both are frozen. Both are optimized on by nobody. That's why they blur. Here is the difference:

- **Ultimate holdout / Lockbox (4):** *humans* grade cards. Same construct as the judge. Answers "is this number real, or did we leak?" → **internal validity**.
- **Record of System Launches (7):** *history* grades outcomes. Different construct entirely. Answers "is this number measuring the thing I care about?" → **construct validity**.

A perfect lockbox score with a flat launch-record number means the loop is optimizing card legibility. The lockbox cannot detect that — it is scored by the same judge, so it reports the same construct error with a clean conscience. This is the reason both must exist. They are not redundant frozen sets; they catch different failures, and Lesson 6 vs Lesson 7 is exactly this split.

### 2 vs 4 — LLM Judge holdout vs Ultimate holdout (James's question, answered 8/16)

Both are human-labeled cards that nobody optimizes on, and both are scored against, never tuned on. So why two objects? Because they answer to **different optimizers** and therefore catch different failures — the difference is *scope*, not content:

- **LLM Judge holdout (2)** is **judge-scoped**. It is withheld from the judge's GEPA loop *only*. Its single job: detect whether the judge overfit its calibration set — i.e. whether the judge memorized the ~20 calibration cards rather than learning to grade. It is silent about everything downstream of the judge.
- **Ultimate holdout / Lockbox (4)** is **program-scoped**. It is withheld from *every* optimizer in the program — judge GEPA, playbook GEPA, and the Feedback Curator. Its job: detect whether the whole stack is fooling itself, including the failure the judge holdout structurally cannot see — the coupled-loop leak where the playbook generator learns to exploit the judge's blind spots, or the Curator folds test cards back into `quality_patterns.md`.

The sharpest way to hold it: **a card can pass the judge holdout and still be poisoning the lockbox.** If the judge is well-calibrated (holdout clean) but the playbook optimizer has discovered the judge's systematic blind spots, judge-scoped tests all look healthy while program quality rots — exactly what only the lockbox catches. The judge holdout guards one optimizer; the lockbox guards the *interaction* of all of them. Draw them from the same human-labeled pool with an explicit split, or they contaminate each other on day one.

### 1 vs 4 — the other easy confusion

Both are human-graded cards. The difference is **permission, not content**: the calibration set is training data for the judge; the lockbox is the sealed exam nobody studies from. If the two are ever drawn from the same pool without an explicit split, the lockbox is already contaminated on day one.

---

## Candidate object 8 — World Store + Launch Records (proposal stage, 8/20 — James's build, not yet circulated)

Two-layer store produced by the LR-doc connector (crawl: Reflex → Helix → Glean MCP, run under Claude Code):
- **Launch Records (raw layer):** append-only, full provenance — hypothesis → intervention-as-code → metric movement → decision, extracted per launch per surface. Never compressed, never edited. Seeds the attempts store (the "candidate object 8" note in `eval_05` Related refers to this layer).
- **World Store (distilled layer):** current-world facts (what exists, what's deprecated, what replaced what), canonical + compressed, with supersession. Successor to the hand-drafted `context.md` the Skeptic depends on.

**Who writes:** the connector (raw, auto-ingest); the Curator distills raw → world facts, human-merged — one Curator, two repositories (`quality_patterns.md` stays separate; decision 8/20). **Who optimizes on it:** nobody. **Consumers (v0 = the first):** Detect agents at card-writing time (must *engage* prior attempts in the card, never silently drop ideas); later the Skeptic's context/already-tried checks, the Curator's decay flags, Chao's precision-against-reality.

**Evolve coupling rules (8/20):** the store is world → snapshotted + versioned, one version pinned per Evolve run (`world_store_version` in EvalResult v2 provenance); ingests land between runs, store bump = re-baseline; Evolve mutates playbooks (including how they query the store), never store content; the Curator never touches playbooks; card-linked records inherit calibration/lockbox exclusion tags; LR prose = untrusted content, screened at intake.

---

## Aliases in the wild — what each source doc calls these

| Object | Appears as | Where |
|---|---|---|
| 1 — Judge calibration set | "graded cards", "human-labeled cards", "the ~20 cards", "Phase 1 labels" | Chao's proposal; session notes |
| 2 — Judge holdout | "held-out split", "leave-one-out CV" | §B.6 of the critique doc |
| 3 — Evolve fixture bank | **"case bank"**, "fixture store", "fixtures", "cases" | Janvi's TDD; §12 of the critique doc |
| 4 — Lockbox | **"ultimate holdout"** (James's notes), **"golden set"** (James, 7/24 meeting), "frozen holdout", "sealed cases" | James's notes; §E.3; the lockbox one-pager |
| 5 — Pattern store | "quality_patterns", "institutional memory", "patterns file", **"SkillRepo"** (SkillOS's name for the same object) | Curator design doc; §9 of the critique doc; SkillOS |
| 6 — Curator evaluation groups | **"grouped task streams"** (SkillOS), "task groups", "lineage" | SkillOS §3.2.1; §1.5 `Evidence:` field |
| 7 — Record of System Launches | **"hindsight set"** (accepted shorthand), **"hindsight-recall case bank"**, "the anchor", "outcome anchor" | §E.4, §G of the critique doc; `eval_00` §7 |
| — | "recall gold set" — a *different* thing again: past PM roadmaps used as a recall reference. Critiqued in §B.5 and being replaced by object 7 | Chao's proposal |

---

## Live collisions to defuse

*Three found 8/14 (dataset names); more found 8/15 (mechanism and metric names, see Part B).*

1. **"case bank" means two different objects.** Janvi's TDD uses it for the Evolve fixture bank (object 3, optimized on). The critique doc uses it for the Record of System Launches (object 7, never optimized on). These have *opposite* access rules. Saying "the case bank" in the working session will be understood as object 3 by everyone who read the TDD. **Fix: retire the phrase entirely.** Use "fixture bank" and "Record of System Launches" (shorthand: the hindsight set).

2. **"golden set" / "gold set" means two different objects, in two live documents.** James's 7/24 on-record comment — *"hold out a golden set if using GEPA"* — means the **lockbox** (object 4). Chao's proposal uses "recall gold set" for the **PM-roadmap recall reference**. Anyone reconciling the meeting notes against the proposal will merge them. **Fix: retire "gold/golden set" from all Reflex eval writing.** It is unrecoverable.

3. **"holdout" is ambiguous between objects 2 and 4.** The judge holdout is judge-scoped; the lockbox is program-scoped — full treatment in the **2 vs 4** section above. **Fix: never use bare "holdout" — always "judge holdout" or "lockbox."**

---

## Canonical vocabulary (use these, retire the rest)

**Use:** judge calibration set · judge holdout · Evolve fixture bank · lockbox · pattern store · Curator evaluation groups · Record of System Launches (shorthand: the hindsight set)

**Retire:** case bank · gold set · golden set · bare "holdout" · "ultimate holdout" (→ lockbox) · "the anchor" as a standalone noun (→ "the Record of System Launches," describing it as the anchor) · bare **"Pareto"** (→ instance-Pareto / dimension-Pareto) · bare **"harness"** (→ agent / eval / synthesized harness)

---

## The one-paragraph version

> Humans grade cards. Some of those grades train the judge (**calibration set**); some are withheld to check the judge didn't just memorize them (**judge holdout**); and some are sealed away from every optimizer in the program so we can tell whether the whole stack is fooling itself (**lockbox**). Separately, the playbook optimizer runs candidates against recorded world-snapshots (**Evolve fixture bank**). And finally, one set is graded not by humans at all but by history — what actually shipped and proved out (the **Record of System Launches**) — because every other number in the program is ultimately somebody's opinion of a card, and only that one can tell us whether we're finding things or just writing well.

---

# Part B — Mechanisms and terms

*Added 2026-08-15; reworked 2026-08-16.* Part A fixes the nouns for **data**. This part fixes the nouns for **machinery and measurement**, because the sharpest ambiguities in the program turned out to live here.

## Clarifying Pareto meaning

"Pareto" is the most dangerous word in the Evolve review, because it names **two unrelated mechanisms that are both live in the same conversation** — not, as with most terminology drift, in two documents read by different people. One is a parent-selection distribution borrowed from the GEPA paper; the other is an acceptance gate invented in Janvi's TDD. They share a name and nothing else: different axes, different job, different math, and — critically — opposite exposure to a hazard nobody has measured yet. If a review comment says "the Pareto step," half the room hears selection and half hears the gate, and the disagreement that follows is real but invisible.

### The two things "Pareto" refers to

| | **Instance-Pareto** — GEPA's selection frontier (paper §3.1, Alg. 2; DSPy `candidate_selection_strategy="pareto"`) | **Dimension-Pareto** — Evolve's acceptance gate (Janvi's TDD) |
|---|---|---|
| **Axes are** | *task instances* — one objective per case in the selection set D_pareto (30 cases → a 30-dimensional frontier) | *judge rubric dimensions* — the 5 quality scores (clarity, evidence, rigor, actionability, novelty) |
| **What it decides** | *which parent to mutate next* — a sampling distribution over the candidate pool, not a yes/no | *whether a mutated candidate is kept* — a pass/fail admission test |
| **Mechanism** | keep every candidate that leads on ≥1 instance (the frontier), prune the strictly dominated, sample the next parent ∝ the number of instances it leads | require the child to no-worse-dominate the parent — ≥ on all 5 dimensions and > on at least one |
| **What it's for** | **exploration** — stops the search collapsing onto one lineage, preserving candidates good on only a few cases so their strengths can recombine (GEPA's "illumination") | **quality control** — the intent is to refuse any candidate that regresses a dimension, even if its average went up |
| **Axis correlation** | *not a hazard.* More instances = a richer frontier; correlation between cases just means fewer distinct leaders, which is fine | **the central hazard.** The 5 judge dimensions are almost certainly correlated (LLM rubrics usually are), and correlation makes "dominate on all 5" easy to pass on noise — false-accept rate climbs toward 50% as correlation → 1 |

### The fact that settles the confusion

**GEPA's acceptance test is a plain scalar.** In Algorithm 1 (lines 13–14) a mutated candidate is accepted iff its *average minibatch score* improved over the parent's — one number, before vs. after. Multi-objective reasoning appears nowhere in GEPA's acceptance; the only place GEPA is multi-objective is parent selection (Alg. 2), and there the objectives are task instances, never rubric dimensions. So:

**GEPA cannot be cited in support of a dimension-Pareto acceptance gate.** The paper's Pareto machinery is doing the opposite job (selection, not admission) over different axes (instances, not dimensions). Reflex's gate is a genuine Reflex invention, and it inherits a correlation-driven failure mode that GEPA's design never had to reason about.

This matters beyond vocabulary: the case for the dimension-Pareto gate leans on "GEPA does Pareto," and that support evaporates once the two senses are separated. **It's the load-bearing argument in `eval_03` §1** (separate acceptance from parent selection) **and §2** (give the gate a statistical margin) — both follow directly from the table above.

### The fix

Never write bare "Pareto." Use:
- **"instance-Pareto (parent selection)"** — GEPA's frontier over cases; the exploration mechanism Reflex should adopt and currently lacks.
- **"dimension-Pareto (acceptance gate)"** — Reflex's rubric-dimension admission test; the thing under scrutiny, and the thing GEPA does not do.

## Open question for Janvi and Chao: what is `blame()` for?

This one isn't a naming collision to legislate away — it's a **design question I don't think has an owner's answer yet**, and it should be asked directly rather than resolved unilaterally in a glossary.

**The factual starting point: `blame()` is not standard GEPA.** GEPA selects which component to mutate with `SELECTMODULE` (Algorithm 1, line 8), and the policy is **round-robin** — it just cycles through the components in order. The DSPy reference implementation agrees: `component_selector="round_robin"` by default (`RoundRobinReflectionComponentSelector`). GEPA never computes which component is at fault; credit assignment is either *implicit* (the reflection LM reads the execution trace and figures out what to change) or *supplied by the feedback function* (µf returns component-scoped feedback). A named `blame()` selector that picks the component to mutate is therefore a Reflex-specific departure from the configuration GEPA's published results were measured on. Anyone reading the TDD will assume it's stock GEPA; it isn't.

**My best reconstruction of the rationale** (from where `blame()` appears in the TDD, not from a stated design note — so this is inference, flag it as such when raising it): the intent seems to be **efficiency under a tiny budget**. Evolve has ~450 invocations total; round-robin spends mutations on components that may be fine, and `blame()` looks like an attempt to spend the budget only on the component actually responsible for a low score — a targeted alternative to round-robin's blind cycling. That is a reasonable instinct. The concern is *how it locates the culprit*: if `blame()` works by re-reading the judge's rationales to decide what to mutate, it inherits every rationale bias into the targeting decision — and those biases are large and measured (verbosity bias made MT-Bench evaluators prefer the longer answer >90% of the time; position bias 50–70%; self-enhancement 10–25%). A `blame()` that reads rationales carrying a >90% verbosity bias will systematically point at whichever component emits the most text, regardless of fault. It would also be reconstructing, after the fact, information the judge already had and threw away when it collapsed its reasoning into five numbers — where GEPA's actual move is the opposite: extend the metric into a feedback function µf that captures the evaluation trace *at scoring time* (DSPy: `pred_name` + `pred_trace`) and hands it straight to reflection.

**The questions to put to them, in order:**
1. What is `blame()` actually designed to do — pick the single component to mutate (a `SELECTMODULE` replacement), or weight/prioritize among components? Confirm the mechanism, because the rest depends on it.
2. What signal does it read — judge rationales, raw scores, execution traces, or something else? If rationales, the bias problem above is live.
3. Was round-robin considered and rejected, or just not adopted? If there's a reason round-robin fails for Reflex specifically, it should be written down; if not, round-robin is the proven default and `blame()` carries the burden of proof.

**Why alignment here matters** (the part worth stressing to them): the judge is itself being GEPA-optimized by Chao *while* Evolve uses it as the fitness signal. If `blame()` reads the judge's output to decide what to mutate, then a judge blind spot doesn't just mis-score a candidate — it **mis-targets the entire search**, steering mutation budget toward the wrong component generation after generation. That couples Chao's judge work and Janvi's loop far more tightly than either doc acknowledges, and it's exactly the seam (`eval_00` structural finding 1) where two people's work silently interacts. The cheap resolution is `eval_03` §3: ablate `blame()` against round-robin (one config value, since it's structurally a custom `ReflectionComponentSelector`) and keep it only if it beats round-robin by a margin the fixture bank can resolve — and, better, move component-scoped feedback to scoring time so reflection reads the trace, not a reconstructed attribution.

## Proposed terminology for "harness"

"Harness" carries three distinct meanings across the sources now in the KB, so bare "harness" in a cross-team doc gets read in whichever sense the reader last encountered. Rather than police the word, here's the qualified vocabulary to adopt — pick the specific term and the ambiguity disappears:

| Use this term | Means | Where the sense comes from |
|---|---|---|
| **agent harness** | the scaffold around the model — prompts, tools, the loop, context management; everything that isn't the weights | Anthropic long-running-agent post; DSPy |
| **eval harness** | the fixture-and-evaluation infrastructure — the recorded-snapshot + replay plumbing that scores a candidate | louis-wang/the-harness-is-the-moat; Reflex internal usage |
| **synthesized harness** | a generated code artifact the agent runs inside — scaffolding the system writes and then optimizes | AutoHarness, EvoHarness-RL |

The three are easy to conflate in Reflex specifically because it has all three at once: the agent harness (the PM/DS prompts + tools), the eval harness (the fixture bank + judge), and — if Evolve ever synthesizes playbook scaffolding — a synthesized harness. When in doubt, say which one; "the harness is the moat" is about the *eval* harness, whereas AutoHarness/EvoHarness-RL results are about the *synthesized* harness, and the two don't transfer to each other.

## GEPA ↔ Reflex mapping

For reading the GEPA paper or DSPy source against the TDD.

| GEPA / DSPy | Reflex | Note |
|---|---|---|
| candidate | candidate playbook / spec version | |
| candidate pool P, ancestry A | `versions/vN.md` + version history | |
| Reflective Prompt Mutation | the mutation step | |
| `SELECTMODULE` (round-robin) | `blame()` | **not equivalent** — see "what is `blame()` for?" above |
| feedback function µf / `GEPAFeedbackMetric` | the judge, extended | `pred_name` + `pred_trace` are where per-component credit legitimately enters |
| D_feedback (minibatch source) | fixture bank slice per generation | |
| D_pareto (selection/validation set) | — | no Reflex equivalent named |
| minibatch improvement test (Alg. 1 L13–14) | — | Reflex uses the dimension-Pareto gate here instead |
| `candidate_selection_strategy` = `"pareto"` \| `"current_best"` | — | makes the exploration ablation a one-line config change |
| System-Aware Merge (`use_merge`) | — | not in the TDD |
| rollout budget | the 450-invocation budget | GRPO's entry ticket on IFBench was 24,000 rollouts; GEPA's was 678 |

## SkillOS ↔ Reflex mapping

| SkillOS | Reflex |
|---|---|
| frozen agent executor π_L | PM Agent / DS Agent |
| skill curator π_S | Feedback Curator |
| SkillRepo | `quality_patterns.md` (object 5) |
| `insert_skill` / `update_skill` / `delete_skill` | intake (§1.3.1) / conflict resolution (§1.3.2) / decay handling (§1.3.3) |
| BM25 retrieval | ranked pattern lookup (§1.3.4) |
| grouped task streams | Curator evaluation groups (object 6) |
| compression reward r_comp | **no equivalent** — see `eval_04_curator_measurement_proposal.md` §4.2 |
| — | lineage / audit trail (§1.3.5) — SkillOS has no equivalent |

## "Agreement" — always say percentage-agreement or Cohen's κ

Not a Reflex-invented collision, but it will decide a real call, so it belongs here. **Percentage agreement** is the raw fraction of cards two raters scored the same. **Cohen's κ** is the same comparison corrected for chance agreement. They diverge enough to reverse a conclusion: one published evaluator scored 80% percentage agreement and κ = 0.62; across studies judges have appeared to *beat* the human ceiling on percentage agreement (85% vs. 81%) while sitting well *below* it on κ (0.84 vs. 0.97) for comparable tasks. Correlation metrics (Spearman's ρ, Kendall's τ) also don't correct for chance and run high — one study reported κ of 0.3–0.5 where τ/ρ were 0.8–0.9 on the same data.

**Fix:** never write bare "agreement" or bare "the ceiling." Write **"human–human κ"** and **"judge–human κ"**, and state the metric on every number. Reflex's grading is binary, which is exactly the case where κ is the right tool (see `eval_02` sizing note).

## Terms to pin (Reflex-internal, no external analogue)

**fitness** — the judge's output used as the optimization objective. Always qualify with judge version; cross-generation comparisons are only valid within one judge version (§2). · **landing re-run** — re-execution of an accepted candidate before it lands. · **`never_mutable`** — glob-based protection on files; does not protect prose spans inside mutable files (the Lesson 4 gap). · **shadow validation** — evolved spec run beside the incumbent on the next live rotation, proposed in §12, not in the TDD. · **`is_pareto_axis`** — TDD flag defaulting to true, which silently promotes any new diagnostic metric into a gate axis (§11).

---

## Related

- Working state, undelivered critique, IC lane: `eval_00_hub.md`
- Lockbox protocol (for Chao): `eval_02_judge_lockbox_protocol.md`
- Evolve feedback + EvalResult v2 contract (for Janvi): `eval_03_evolve_feedback_and_contract.md` — the `case_source` field is where these distinctions become machine-enforceable
- Curator design: `feedback_curator_and_skeptic.md` (objects 5 and 6 live here)
- Curator measurement proposal (for the Curator owner): `eval_04_curator_measurement_proposal.md`
- The 8/16 consolidated notes export this file was synced against: `reflex_eval_evolve_notes_0816.html`
- Primary sources in the KB: `kb/hard/raw/arxiv/gepa-reflective-prompt-evolution-can-outperform-reinforcement-learning.md` · `kb/hard/raw/dspy/dspy-gepa-reflective-prompt-optimizer.md` · `kb/hard/raw/arxiv/skillos-learning-skill-curation-for-self-evolving-agents.md`
