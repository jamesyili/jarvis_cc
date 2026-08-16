# Evolve TDD — design feedback

**For:** Janvi's Evolve TDD (draft 8/4) · **From:** James Li, named reviewer · **Date:** 2026-08-15

Eight suggestions, ordered by how much they change. Each states the concrete change, the reason, and what it costs. Grounded in the GEPA paper (arXiv 2507.19457v2, ICLR 2026 Oral), its reference implementation in DSPy, SkillOS, and AI2/UW 2607.12227 — all now in the KB, cited by line where it matters.

Context this is written against: the TDD is the strongest doc in the eval program. Typed contract, one-component mutations, un-bypassable human gate, landing re-run, version history, success criteria with healthy/broken bands. Everything below is at the margins — but the margins are where the loop either measures something or doesn't.

**Part 1** is the design suggestions. **Part 2** is the concrete contract: the EvalResult v2 schema and the gate implementation, drafted 8/12 against TDD §3.2/§3.3.5 and revised 8/15 to match suggestion 1. Part 2 supersedes the standalone straw-schema doc that circulated on 8/12 — if you have that version, this one replaces it, and the difference is called out in §2.4.

---

# Part 1 — Design suggestions

---

## 1. Separate acceptance from parent selection

**Suggestion.** Split the two jobs the Pareto machinery is currently doing at once.

- **Acceptance:** a single aggregate score plus a statistical margin. Accept a candidate only if a paired bootstrap over the fixture cases puts the CI on the per-case difference clear of zero.
- **Parent selection:** instance-Pareto over fixture *cases* — retain candidates that lead on at least one case, prune strictly dominated ones, sample the next parent with probability proportional to the number of cases it leads.
- **The five rubric dimensions** become diagnostics, plus optional hard-floor **veto criteria**. They stop being gate axes. Retire `is_pareto_axis`; replace it with `is_veto_axis` defaulting to **false** and `is_diagnostic` defaulting to true.

**Why.** GEPA runs exactly this split, and it's easy to miss because both halves are called Pareto. Its frontier (Alg. 2) is over task instances and decides *which parent to mutate next*. Its acceptance test (Alg. 1, lines 13–14) is a plain scalar: average minibatch score before vs. after, accept if improved. Multi-objective reasoning appears nowhere in acceptance.

The current design does the opposite — dimension-Pareto for acceptance, nothing for parent diversity — and that inherits both known failure modes. Strict dominance over five noisy axes is not a strict gate, it's a high-variance one, and where it sits depends entirely on the judge's inter-dimension correlation, which has not been measured. If the dimensions were independent, a candidate genuinely identical to its parent passes on noise alone about 3% of the time, and a candidate that is truly better on one axis and neutral on the rest passes only ~5% of the time — the gate discards ~95% of real single-axis improvements. If the dimensions are strongly correlated, which is the common outcome for LLM-judge rubrics, the noise-accept rate rises toward 50% and the gate stops filtering at all. The true number is somewhere between, and nobody knows where.

Three independent lines land on the same recommendation: GEPA's own acceptance is scalar; the rubric literature finds implicit aggregation beats explicit weighted dimensions; and the false-accept arithmetic above is undefined until someone measures the correlation matrix. Meanwhile the loop loses nothing, because the diversity that dimension-Pareto was implicitly providing is exactly what instance-Pareto provides deliberately and better.

**Cost.** The largest change here. Requires the bootstrap module (§2) to exist first, and requires agreeing that a single aggregate is defensible — which is easier if the aggregate is the judge's calibrated score rather than a weighted sum of five arbitrary weights.

---

## 2. Give the gate a statistical margin, and the contract the fields to support it

**Suggestion.** Three pieces, in order:

1. **EvalResult v2 carries trial-level scores, not just a scalar mean** — plus `judge_version` and `fixture_snapshot_id` per result.
2. **The dominance test becomes a paired bootstrap module** that Evolve calls, rather than a raw mean comparison. Same cases both arms; build the interval on the per-case difference; require it to exclude zero.
3. **§5 states the fixture bank's minimum detectable effect.** `n ≈ (z_{α/2}+z_β)²·Var(d)/δ²`. With a realistic disagreement profile — agree on 80% of cases, 15% evolved-wins, 5% incumbent-wins, so `Var(d) ≈ 0.19` — detecting a **10-point** improvement needs about **150 paired cases**. A 30-case bank resolves roughly a 22-point swing; 20 cases, about 27 points.

**Why.** Without the margin, "evolved spec dominates on 4 of 5 axes, +6 points net fitness" is not a result — it is a number with an unstated error bar, and at plausible bank sizes +6 is not resolvable at all. Without `judge_version` pinned per run and recorded per result, score deltas across generations are unattributable, because the judge is itself being GEPA-optimized on the other side of the program. And below roughly 100 datapoints the CLT intervals are systematically too narrow and degenerate to zero width when a run passes or fails everything — which is precisely what a small curated bank does. At this program's sample sizes the honest tools are bootstrap or Beta-Binomial, not `mean ± 1.96·SE`.

One free win regardless of the rest: **pair everything.** Running both arms on identical cases makes the positive score correlation a variance reduction that costs nothing, and comparing two overlapping CIs is the wrong test.

**Cost.** About a day of IC work for the module. I'd like to own this piece — it is the same object as EvalResult v2, and it removes the biggest silent failure mode in the loop. **The schema and the gate implementation are in Part 2** — this suggestion is the argument, Part 2 is the code.

**Prerequisite that costs nothing:** the 5×5 dimension correlation matrix is computable today from Chao's existing judge V1 output over already-graded cards. No new labels, no new runs. It sets the design of everything above.

---

## 3. Ablate `blame()`, and consider replacing it with per-component feedback at scoring time

**Suggestion.** Add an ablation arm to §5: `blame()` vs. round-robin component selection, matched budget, same fixture slice, compare net fitness delta *and* the per-component mutation distribution. Kill criterion stated up front: if `blame()` does not beat round-robin by a margin the bank can actually resolve, drop it.

Separately and better: **extend the judge's output contract to emit per-component feedback text at scoring time** — a `feedback` field scoped to the component being evaluated, carried in EvalResult v2 alongside the score.

**Why.** GEPA has no `blame()`. Module selection is `SELECTMODULE` at Algorithm 1 line 8, and the policy is round-robin; the reference implementation agrees, defaulting `component_selector="round_robin"`. So `blame()` is a departure from the configuration GEPA's published results were measured on, which puts the burden of proof on it rather than on the ablation. The ablation is also nearly free: `blame()` is structurally a custom `ReflectionComponentSelector`, so the control arm is one config value, not a build.

The deeper reason to prefer per-component feedback: `blame()` re-reads judge rationales — text written to *justify a score*, not to *locate a fault* — and inherits every rationale bias into the choice of what to mutate. These biases are measured, and they are not small: in the MT-Bench study, **verbosity bias made evaluators prefer the longer response more than 90% of the time**, position bias ran 50–70% depending on model, and self-enhancement bias gave evaluators a 10–25% win-rate bump on their own outputs. A `blame()` reading rationales carrying a verbosity bias that strong will systematically point at whichever component emits the most text — a mutation-targeting bias with no relationship to fault. It is reconstructing, after the fact, information the judge already had and discarded when it collapsed its reasoning into five numbers. GEPA's actual innovation on this axis is the opposite move: extend the metric `µ` into a feedback function `µf` that captures the **evaluation trace** — what the environment produced on the way to the score — and hands it to reflection. DSPy exposes this directly: the feedback metric receives `pred_name` and `pred_trace` and may return a score *and* feedback for that specific predictor. If it returns nothing, reflection receives the string `"This trajectory got a score of {score}."` and nothing else.

A misdirected mutation is not neutral. It burns rollouts from a 450-invocation budget that §2 above already shows is too small to resolve small effects.

**Cost.** Ablation: one config value plus the runs. Per-component feedback: a judge change, so it depends on whether V1 can carry it or it waits for V2. Worth asking Chao rather than assuming.

---

## 4. Add a matched-budget baseline arm to the success criteria

**Suggestion.** Before crediting the evolution loop with a gain, run the incumbent spec with K-sample selection at the **same** invocation budget. Report pass@1 and pass@k separately.

**Why.** AI2/UW compared automatic harness evolution against matched-budget test-time scaling on Terminal-Bench 2.1. Evolution did not consistently beat parallel sampling or sequential refinement; its gains appeared in pass@5 but not pass@1 — that is, they came from taking more attempts, not from a better harness. Harnesses evolved on a training split also transferred almost nothing to held-out tasks, +0.6 pass@1 on average.

The honest counter-argument in Evolve's favor is that Terminal-Bench is harness-*insensitive* — a shell tool and a basic prompt suffice — while Reflex playbooks are harness-*dominant*, since the domain strategy lives in the spec. That is a real difference, and it is also exactly the claim the baseline arm would prove rather than assume. Adding the arm is what makes a positive result defensible instead of attackable.

**Cost.** One extra arm per evaluation, at the same budget. It roughly doubles the cost of a success claim and removes the strongest available objection to it.

---

## 5. Put parsimony pressure on the spec

**Suggestion.** Track spec token length per generation and make growth cost something. Minimum: record it and report it in the version history. Better: require an accepted mutation that increases spec length to clear a larger margin than one that holds length flat or reduces it.

**Why.** This is the mechanism-level reconciliation of the two pieces of evidence above, and it is the reason I'd not read the AI2/UW result as fatal.

Their qualitative diagnosis of why evolution underperformed was that meta-agent edits "memorize fixes rather than distilling strategies." SkillOS names the identical failure and builds an explicit objective term against it — a compression reward penalizing repository size against the curator's input context, whose stated purpose is to discourage verbatim trajectory copying and force distillation into reusable rules. Removing that term measurably hurt performance (ALFWorld success rate 61.2 → 60.0, with the full ablation set showing content-quality at 58.6 and ungrouped training at 57.3).

Two independent papers, the same failure mode, and one of them has the counter-mechanism. That reframes the negative result: it may be a finding about self-evolution run *without* a compression objective, rather than about self-evolution. An Evolve loop with no length pressure is running the configuration that failed.

**Cost.** Recording length is free. The margin rule is a gate parameter, and it needs the margin from §2 to exist first.

---

## 6. Pre-flight the incumbent before each generation

**Suggestion.** At the start of each generation, re-run the incumbent spec on a small fixed canary slice of the fixture bank. Record `incumbent_canary_score` per generation. If it deviates beyond tolerance from the prior generation's recorded value, halt and flag rather than proceeding.

**Why.** Fixtures go stale — tables deprecate, experiments conclude, strategy docs move — and the judge is being optimized concurrently. Either can move the fitness scale underneath a generation. When that happens without a canary, the drift is silently attributed to the mutation, and every number that generation produces is unattributable after the fact. A canary converts a forensics problem into a halt condition.

**Cost.** A handful of invocations per generation, and it pays for itself the first time it fires.

---

## 7. Protect verification rules by changing their container, not by guarding prose

**Suggestion.** Move the playbooks' verification rules — the "verify against Presto before citing a metric" class — out of prose and into a structured block within the playbook, where only designated fields are mutable. `never_mutable` then has something it can actually protect.

**Why.** `never_mutable` globs operate on files. Reflex playbooks embed checks as prose *inside* mutable sections, so the glob can't reach them and structural validation can't see them. A GEPA mutation that softens "verify against Presto before including a metric" into "include metrics with a confidence note" passes every existing control, and there is no point in the current design where a human is guaranteed to catch it.

The obvious fix is a new mechanism — protected prose spans. There is a cheaper one. Anthropic hit the same problem building long-running agents: they tried strongly-worded prose instructions against editing a test manifest, found it insufficient, and solved it by changing the file format, reporting that the model is measurably less likely to inappropriately modify JSON than Markdown. One field mutable, the rest structurally inert. A mutation that cannot find a prose sentence to soften cannot soften it.

**Cost.** A playbook format change, which is a migration. But it needs no new enforcement machinery and it degrades gracefully.

---

## 8. Close the two open gaps in security and rollback

**Suggestion.** Two paragraphs the doc currently doesn't have:

- **Fixture content is untrusted.** Fixtures contain Asana comments and other user-authored text that will be fed into headless agent runs. State that fixture content is data and never instructions — delimit it, instruct the agent explicitly to ignore imperatives inside it, and screen new fixtures at intake for instruction-shaped content.
- **The revert procedure, written down.** Rollback exists implicitly via `versions/vN.md`. Make it explicit: what triggers a revert, who may execute one, and what happens to fixtures and results added since the reverted version landed.

**Why.** These were named as the thin sections on 8/10 and are still open. The prompt-injection path in particular is the one failure in this list that is not a measurement problem — it's a live surface, and the mutation loop makes it worse by construction, since a successful injection can persist into an accepted spec.

**Cost.** Writing time, not build time.

---

---

# Part 2 — The contract

Drafted 2026-08-12 against TDD §3.2/§3.3.5 as written 8/4 (`sources/janvi_evolve_tdd_2026-08-04.pdf`); revised 8/15. Target: `evolve/infra/schemas/eval_result.py`.

The TDD's contract design is right: rubric lives in the values, EvalResult is the sole coupling point, `contract_version` asserted at startup. v2 adds the fields that make scores *trustworthy over time* — uncertainty, judge provenance, fixture provenance — plus the axis-declaration change. Everything is additive except that one flip.

## 2.1 MetricScore

```python
class MetricScore(BaseModel):
    name: str
    value: float                              # aggregate over trials (mean unless noted)
    trial_values: list[float] | None = None   # NEW — per-trial raw scores, len == n_trials
    scale_min: float = 0.0
    scale_max: float = 1.0
    direction: Direction = "maximize"
    weight: float = 0.0
    is_diagnostic: bool = True                # NEW — reported, never gates
    is_veto_axis: bool = False                # REPLACES is_pareto_axis — a hard floor, not a Pareto axis
    rationale: str | None = None
```

**Why `trial_values`:** K trials produce a distribution; passing only the scalar mean forces the gate to compare noisy point estimates, and with small K it selects on noise. Trial-level scores also let Evolve compute Pass@K / Pass^K itself instead of each adapter pre-aggregating differently. **Nothing else in Part 2 works without this field.**

**Why `is_veto_axis` replaces `is_pareto_axis`:** see §2.4.

## 2.2 EvalResult

```python
class EvalResult(BaseModel):
    contract_version: str                 # existing — bump to 2.0
    scores: dict[str, MetricScore]        # existing, unchanged shape
    feedback: str                         # existing — the reflective gradient
    n_trials: int                         # existing per TDD §3.3.5

    # NEW — judge provenance
    judge_version: str                    # bumps on ANY judge prompt/model/rubric change
    judge_model: str | None = None        # convenience; version is the contract

    # NEW — world provenance
    fixture_snapshot_id: str              # which frozen world produced this result
    fixture_created_at: datetime          # feeds a staleness gate (refuse/warn past max age)

    # NEW — case provenance
    case_id: str
    case_source: Literal["rotation", "calibration", "lockbox", "synthetic"]

    # NEW — per-component feedback (suggestion 3)
    component_feedback: dict[str, str] | None = None
```

**`judge_version`** — the judge is itself being GEPA-optimized (Chao's Stage 1) while Evolve uses it as fitness. Unversioned, a score delta across generations is unattributable: improved playbook, or drifted judge? Rules the field enables, enforced in the runner rather than the schema: search and landing re-run pin the same version; cross-generation fitness comparisons only within a version; a judge upgrade means re-baseline.

**`fixture_snapshot_id` + `fixture_created_at`** — an edit that dominates on stale fixtures can regress live. The snapshot ID makes "same world" checkable; the timestamp makes staleness a gate instead of a hope. This is also the join key to the hindsight case bank, which reuses the same snapshot format.

**`case_source`** — makes the contamination policy enforceable rather than aspirational. The runner refuses `lockbox` cases in any GEPA loop, and the Feedback Curator filters `calibration` and `lockbox` out of pattern extraction. One enum, three protections.

**`component_feedback`** — the carrier for suggestion 3. If the judge can emit per-component feedback at scoring time, this is where it lands, and it is what reflection reads instead of a reconstructed attribution.

## 2.3 The gate

Replaces raw mean comparison in TDD §3.3.6.5. **Primary form**, matching suggestion 1 — accept on a single aggregate with a margin, with hard floors as vetoes:

```python
def accepts(parent: list[EvalResult], candidate: list[EvalResult],
            aggregate: str, veto_axes: list[str],
            alpha: float = 0.05, B: int = 10_000) -> GateVerdict:
    """Paired bootstrap over shared cases (pairing removes case-difficulty variance).

    1. Veto: for each axis in veto_axes, reject if the candidate falls below its
       declared floor. Floors are absolute, not relative to the parent.
    2. Accept: per-case delta on `aggregate` = mean(candidate trials) - mean(parent trials);
       resample cases with replacement B times -> CI on the mean delta;
       accept iff the CI lies entirely above zero.

    Verdict carries the delta, the CI, n, and the number of case clusters, so the
    proposal record shows *why* — and so an underpowered comparison is visible
    rather than silent.
    """
```

**Fallback form**, if suggestion 1 isn't adopted and per-dimension acceptance stays: keep dominance, but make it significance-aware — candidate survives iff **not significantly worse on any declared axis and significantly better on at least one**, same paired bootstrap per axis. That is strictly better than comparing means, and it is the version drafted on 8/12.

Either way: ~a day of work including tests, a pure function of the v2 fields, living in `evolve/infra/gates/`. It is also what makes the "held-out regression catch" success criterion in TDD §5 statistically meaningful rather than anecdotal.

## 2.4 What changed since the 8/12 draft, and why

The straw schema I circulated on 8/12 proposed keeping `is_pareto_axis` and flipping its default from `True` to `False`, so that gate axes became opt-in rather than a side effect of logging a metric. That fixed axis accumulation but left dimension-level acceptance in place.

After reading the GEPA paper and its implementation on 8/15, I'd go further, and the two proposals shouldn't both be live. **Suggestion 1 retires the concept**: if acceptance moves to a single aggregate with a margin, there are no gate axes to opt into, and the dimensions become diagnostics plus optional hard floors. `is_pareto_axis` is therefore replaced by `is_diagnostic` (default true) and `is_veto_axis` (default false).

If suggestion 1 doesn't land, the 8/12 proposal is the fallback: keep `is_pareto_axis`, default it to `False`, and use the fallback gate in §2.3.

## 2.5 Migration

v1 adapters keep working behind a shim: `trial_values=None` means the gate falls back to means with a loud `UNPOWERED_COMPARISON` warning written into the proposal record. The only true break is the axis-declaration change — a one-line explicit declaration in each existing target YAML, grep-able, done in minutes.

---

## What I'm not raising

**`is_pareto_axis` defaulting to true as a standalone ask.** Any diagnostic metric a stage adds silently becomes a gate axis, and with four or more axes no-worse-everywhere approaches unsatisfiable. This is real, but suggestion 1 dissolves it and §2.4 handles the fallback, so it isn't raised separately.

## Sources

- GEPA: `kb/hard/raw/arxiv/gepa-reflective-prompt-evolution-can-outperform-reinforcement-learning.md` — Alg. 1 (loop, scalar acceptance at L13–14), Alg. 2 (instance-Pareto selection), §3 (reflective mutation, evaluation traces), §3.1 (Pareto illumination)
- DSPy implementation: `kb/hard/raw/dspy/dspy-gepa-reflective-prompt-optimizer.md` — `GEPAFeedbackMetric` (`pred_name`, `pred_trace`), `component_selector`, `candidate_selection_strategy`
- SkillOS: `kb/hard/raw/arxiv/skillos-learning-skill-curation-for-self-evolving-agents.md` — compression reward, ablation table
- Harness-evolution evaluation: `sources/arxiv_2607.12227_rethinking-harness-evolution-evals.pdf`
- Long-running agent harnesses: `kb/hard/raw/anthropic/effective-harnesses-for-long-running-agents.md` — format-as-guard
- Statistics: `kb/hard/raw/cameron-wolfe/applying-statistics-to-llm-evaluations.md` (over Miller 2024, Bowyer 2025)
- Working state and undelivered critique: `eval_00_hub.md` · terminology: `eval_01_glossary.md`
