# Reflex Eval — WORKING DOC: proposal critique, IC lane, pick-up plan

**Status: living working file for the Reflex Eval workstream. Started 2026-08-11 (technical session). Next session picks up from §F.**

Inputs: Chao Wang's *Detect Evaluation Proposal* (7/9, + Gideon's Phase 0 doc 7/16, + Chao's Phase 1 LLM-judge plan 7/23, judge V1 built PR#63) and Janvi Palan's *Evolve for Reflex* TDD (8/4). KB sweep: 13 articles ranked (see §D).

Source docs (verbatim PDFs, filed 8/12 from the 8/11 session uploads): `sources/chao_detect_eval_proposal_2026-07-09.pdf` · `sources/janvi_evolve_tdd_2026-08-04.pdf`.

## State of play (as of 8/11)

| Workstream | Owner | Status |
|---|---|---|
| Detect Eval proposal (metrics phases 0–3) | Chao Wang | Draft 7/9, in review (Gideon, Rahul, Karim, Dafang, Chi) |
| Phase 0 task performance (cycle_log.jsonl, cost/token, S3, audit dashboard) | Gideon Kim | Building; form-based expert review tooling in progress |
| Phase 1 LLM judge + human calibration | Chao Wang (GEPA consultant: Raghav Jindal) | **Judge V1 built (PR#63).** Next 1–2 wks from 7/24: run judge uncalibrated + visualize, collect ~20 PM-graded cards via Asana forms, then GEPA-optimize the judge |
| Evolve TDD (GEPA loop, EvalResult contract, Pareto gate, human gate) | Janvi Palan | Draft 8/4, in review — James is a named reviewer |
| James's on-record positions (7/24 meeting) | — | Binary pass/no-pass over 5-dim composite; curate + hold out a golden set if using GEPA; beware reward hacking |

Time-critical dependency: **the lockbox/holdout protocol (§E.3) must land before Chao's GEPA-on-~20-cards run.**

Note on attribution: the repo's 8/10 record says the Evolve design came from "a senior Ads MLE"; the TDD's author of record is **Janvi Palan** (who owns the Evolution stage per Tim's July notes), with Ads folks (Jacob Gao, Dinesh Govindaraj, Helen Xu) as reviewers and the Ads Build Agents as the Build-stage eval source. Worth getting the credit right before citing the collaboration upward.

---

## A. Structural critique (cross-doc — the highest-order findings)

**1. Chao's Stage 2 and Janvi's Evolve are the same work, described in two docs with two owners.**
Chao's Phase 1 plan Stage 2 = "run calibrated judge in the detect cycle, connect card quality back to playbooks, use GEPA to optimize playbook prompts." Janvi's Evolve Detect adapter = exactly that, with better machinery (Pareto gate, human gate, versioning). If both proceed, you get two GEPA-on-playbooks pipelines by October. The seam should be named now: **Chao owns the judge + calibration (Evolve's fitness function); Janvi owns the optimization loop; Chao's Stage 2 collapses into the Evolve Detect adapter.** This is a one-conversation fix this week.

**2. The EvalResult contract is the right keystone but is missing uncertainty and provenance.**
`MetricScore` carries name/value/bounds/direction/weight — good, rubric lives in values not code. Missing:
- **Trial-level scores or variance.** K trials produce a distribution; the contract passes a scalar. Pareto dominance on noisy means with small K selects on noise. The gate should require dominance with statistical margin (paired bootstrap over cases; CI excluding zero on ≥1 axis).
- **Judge version + fixture snapshot ID.** The judge is itself being GEPA-optimized (Chao Stage 1) while Evolve uses it as fitness. If judge version isn't pinned per run and recorded per EvalResult, score deltas across generations are unattributable. Rule needed: search and landing re-run use the same judge version; cross-generation fitness comparisons only within judge version.

**3. Neither doc answers the EvalHub question.**
Chao's own references list EvalHub — Pinterest's internal offline agent-eval platform (register agents, upload datasets, run simulations, LLM/code graders). Building Reflex eval beside it without a stated reason invites the same platform-consolidation pressure Shifu is applying at the system level. Either build on it or write the paragraph on why not. Adopting it also makes Reflex's eval legible org-wide — strategic value, not just hygiene.

## B. Detect Eval proposal (Chao) — specific critique

**4. Metric sprawl; observability and evaluation are conflated.** ~20 metrics across Phases 0–3. Token usage, MCP count, tool calls are telemetry, not evals. Every retained eval metric needs: an owner, a threshold, and the decision it drives. Prune to the ones something acts on.

**5. The recall gold set measures redundancy, not discovery.** Building "recall of hypothesis" against past PM roadmaps scores the agent on rediscovering what humans already found — survivorship bias; the highest-value Reflex cards are the ones humans missed, which by construction can't be in that set. Better: **hindsight replay** — snapshot the world at time T, run Detect, score against what was shipped/proven between T and T+n. The 66-cycle archive + shipped-experiment record makes this buildable today, and it directly answers the "recall is harder than precision" gap Rahul named.

**6. GEPA-optimizing the judge on ~20 labels will overfit.** 20 cards is a fine pilot for *measuring* judge-human agreement; it cannot support *optimizing* the judge prompt. First measure the ceiling: multiple raters on a subset → human-human agreement (Cohen's κ / Spearman ρ); if judge-human is already near that ceiling, GEPA "gains" are fitting noise. Optimize only when ~50+ labels exist, with a held-out split — or leave-one-out CV with variance reported. James's 7/24 meeting comments (binary primary label; hold out a golden set; fear reward hacking) are the right instincts — they should be promoted from meeting notes to requirements in the doc.

**7. Binary-primary, dimensions-as-diagnostics.** Collect binary pass/no-pass + mandatory rationale from humans (cheap, reliable, Netflix precedent already cited). Judge emits dimension scores calibrated to predict the binary; judge quality is measured on binary agreement; dimensions feed the textual gradient only. Never optimize the 5-dim composite — the weights are arbitrary and GEPA will exploit weight artifacts.

**8. Two coupled GEPA loops = systematic reward hacking.** Stage 1 tunes the judge to humans; Stage 2 tunes the generator to the judge. The generator will find the judge's blind spots, and a GEPA-tuned judge has *systematic* blind spots. Mitigations: a **frozen lockbox** of human-labeled cards never seen by either optimizer; periodic blind human audits concentrated on the judge's *highest-scored* cards (hacks concentrate where the judge is happiest); negative rubrics for discovered hacks; cross-model judge spot-checks.

**9. Contamination seam nobody owns.** The Feedback Curator folds learnings from graded cards into quality_patterns.md — which the graded agent reads next cycle. Calibration/gold cards must be excluded from pattern extraction, or scores self-inflate. One sentence of policy now avoids a quietly corrupted eval later.

**10. Phase 3 business metrics are program KPIs, not eval signals.** Funnel survival and shipped-experiment counts are confounded by Presto availability, review bandwidth, and org priorities (the doc says so itself). Report them; never feed them to an optimizer.

## C. Evolve TDD (Janvi) — specific critique

The strongest doc of the set: typed contract, one-component mutations, un-bypassable human gate, landing re-run, version history, success criteria with healthy/broken bands. Critique is at the margins but the margins matter:

**11. Strict Pareto dominance will starve as axes accumulate.** `is_pareto_axis: true` by default means any diagnostic metric a stage adds silently becomes a gate axis; with 4+ axes, no-worse-everywhere approaches unsatisfiable and runs burn the 450-invocation budget producing nothing. Default the flag to false (opt-in axes), and consider epsilon-dominance or tiered gates (primary axes strict, secondary within tolerance).

**12. Fixture staleness + case-bank overfitting across generations.** Tables deprecate, experiments conclude, strategy docs move; an edit that dominates on stale fixtures can regress live. And since vN+1 becomes the next candidate against a finite bank, repeated evolution is slow training-on-the-test-set — the validation split leaks over generations. Needed: fixture age gate + refresh cadence; new cases flow in from each rotation, oldest retire; a rotating lockbox slice; and ideally one **shadow validation** (evolved spec runs beside incumbent on the next live rotation) before landing.

**13. blame() deserves an ablation — and after reading the paper (8/15), it deserves more than that: it carries the burden of proof.** Credit assignment from judge rationales to components is the hardest part of GEPA here, and rationale biases (verbosity, position) can systematically misdirect mutation. Cheap test: blame() vs. random component selection over a few runs — if blame() doesn't beat random, simplify.
- **Upgraded 8/15 (GEPA paper + DSPy source now ingested).** GEPA has no `blame()`. Algorithm 1 line 8 is `j ← SELECTMODULE(Φk)` and the paper states the policy plainly: **round-robin.** The reference implementation agrees — `dspy.GEPA(component_selector=...)` defaults to `"round_robin"` (`RoundRobinReflectionComponentSelector`), with `"all"` as the only other built-in. GEPA's credit assignment is *implicit*: it does not compute which module was at fault, it hands the reflection LM the module's inputs/outputs/reasoning plus the feedback text and lets attribution happen inside the prompt.
- So the framing flips. `blame()` is not GEPA's hard part that Evolve must implement — it is a **departure from GEPA's default**, and the paper's headline results were obtained *without* it. The reviewer question is no longer "does blame() work" but "what does blame() buy over the round-robin the results were measured on?"
- **The ablation is now one config flag, not a build.** In DSPy terms `blame()` is a custom `ReflectionComponentSelector` (documented extension point: `__call__(state, trajectories, subsample_scores, candidate_idx, candidate) -> list[str]`), so the control arm is literally `component_selector="round_robin"`. Any cost objection to running the ablation is gone.
- **Where per-module credit legitimately does live in GEPA: the feedback function, not the selector.** `GEPAFeedbackMetric.__call__` receives `pred_name` and `pred_trace` — the predictor currently being optimized and its sub-trace — and may return `dspy.Prediction(score, feedback)` *for that predictor*. If it doesn't, GEPA falls back to program-level feedback; if there's none at all, the reflection prompt gets the string `"This trajectory got a score of {score}."` and nothing else. That is the real design question for Evolve: **can the Reflex judge emit per-component feedback at scoring time?** If yes, that beats a post-hoc `blame()` heuristic, because the attribution comes from the evaluator rather than from re-reading rationales. If no, the reflection LM is working from a scalar and a trace, and a `blame()` layered on top of that is a heuristic on top of a heuristic.

**14. Security and rollback remain the thin sections.** Fixtures contain untrusted text (Asana comments → prompt injection into a headless Claude run). `never_mutable` globs protect specs, but nothing stated protects the fixture store or screens fixture content. Rollback exists implicitly via `versions/vN.md`; write the explicit revert procedure. (These were the named gaps on 8/10; still open.)

**15½. The missing baseline arm (new 8/12, from arXiv 2607.12227 — read after James supplied it).** AI2/UW compared automatic harness evolution against matched-budget test-time scaling on Terminal-Bench 2.1: evolution did **not** consistently beat parallel sampling or sequential refinement; its gains appeared in pass@5 but not pass@1 (i.e., they came from taking more attempts, not from a better harness); and harnesses evolved on a training split transferred almost nothing to held-out tasks (+0.6 pass@1 avg). Their qualitative read — meta-agent edits "memorize fixes rather than distilling strategies" — is §12's overfitting concern observed in the wild. Implications for Evolve: (a) the success criteria need a **matched-budget baseline arm**: run the incumbent spec with K-sample selection at the same compute before crediting the evolution loop; (b) the honest counter-argument in Evolve's favor is that Terminal-Bench is harness-*insensitive* (a shell tool + basic prompt suffices) while Reflex playbooks are harness-*dominant* (the domain strategy lives in the spec) — but that's exactly the claim the baseline arm would prove rather than assume. Raise as a review comment on the TDD's §5 success criteria.

**15. Add the ultimate anti-Goodhart control:** periodic blind human A/B — baseline vs. evolved outputs, rater doesn't know which is which. Net-fitness-delta can drift upward on judge drift alone; blind A/B is the only signal that can't.

**16. The Pareto gate has two error rates, both unmeasured, and one cheap measurement sets both (new 8/14, from Lesson 6).** Strict dominance over 5 noisy axes is not a "strict" gate — it's a *high-variance* gate, and where it sits depends entirely on how correlated the judge's 5 dimensions are, which nobody has measured.
- If the axes were independent, a candidate genuinely identical to its parent passes by noise alone with probability ≈ 0.5⁵ ≈ **3%** — and a candidate that's truly better on one axis and neutral on the rest passes only ~5% of the time. That's §11's starvation, quantified: the gate discards ~95% of real single-axis improvements.
- If the axes are near-perfectly correlated (all five dims are really one "is this card good" factor wearing five hats — the common outcome for LLM-judge rubrics), the noise-accept rate rises toward **50%** and the gate stops filtering at all.
- The true rate is somewhere between 3% and 50%, and **the 5×5 correlation matrix of judge dimension scores decides it**. That matrix is computable today from Chao's judge V1 outputs over already-graded cards — no new labels, no new runs.
- Multiple-comparisons corollary: whatever the per-candidate false-accept rate is, it compounds over the run. Across ~100 candidate mutations in a 450-invocation budget, even the optimistic 3% yields ~3 accepted-on-noise edits per campaign, each of which becomes the parent for the next generation. This is the same leak as §12's holdout wear-out, in its statistical clothing — repeated testing against a fixed bank.
- Ask: measure the correlation matrix, then set the gate from it — strict dominance only on axes that are actually independent, tolerance/epsilon bands on the correlated cluster, and a paired-bootstrap margin (§E.2) rather than raw mean comparison.

**17. Effective sample size, not sample size, is what the calibration set has (new 8/14).** Applies to Chao's ~20 cards and to Evolve's case bank equally.
- **Clustering.** Cards drawn from a handful of Detect cycles are not IID — same surface, same fixture snapshot, same playbook version. With ~4 cycles × 5 cards and moderate intra-cluster correlation (ρ≈0.5), the design effect is 1 + (m−1)ρ = 3: **effective n ≈ 7, and standard errors inflate ~1.7×.** Miller's paper documents a real case where clustering tripled the SE. Report *n and the number of clusters*, and use a clustered SE.
- **What 20 cards can actually resolve.** Judge-human agreement measured at 80% on n=20 carries a 95% CI of roughly [63%, 98%] — *before* the clustering inflation, and before the small-n caveat below. That interval spans "judge is at the human ceiling" and "judge is far below it." It cannot distinguish them, so it cannot supervise a GEPA run (§6).
- **Minimum detectable effect.** Paired comparison of two playbook versions on the same bank: n ≈ 7.84·Var(d)/δ². With a realistic disagreement profile (agree on 80% of cases, 15% evolved-wins, 5% incumbent-wins → Var(d) ≈ 0.19), detecting a **10-point** improvement needs **~150 cases**; the v0 hindsight bank at ~30 cases (§G) resolves only a ~22-point swing; 20 cards, only ~27 points. Halving the effect you want to see costs 4× the cases — this is the number that should set case-bank sizing, not intuition.
- **Below n≈100 the CLT itself fails** (Bowyer et al. 2025): CLT intervals are systematically *too narrow* in exactly this regime, and they degenerate to zero width when a run passes or fails everything — which is precisely what a small curated bank does. At Reflex's sample sizes the honest tools are Bayesian (Beta-Binomial) intervals or bootstrap, not `mean ± 1.96·SE`.
- Free wins available today: **pair everything** (same cases both arms — the positive score correlation is a variance reduction that costs nothing, and separate overlapping CIs are the wrong test; build the CI on the *difference* and check whether it excludes zero), and **resample K trials per case**, choosing K so within-case variance is small relative to across-case variance. Do **not** lower judge temperature to buy stability — that changes the distribution being measured, i.e. a different judge.

**18. "Pareto" means two different things in this program, and conflating them in a review comment would be a visible error (new 8/15, from the GEPA paper — this was the open verification item).** Verified against Algorithm 1 and Algorithm 2 of arXiv 2507.19457 and against the DSPy implementation. They are different objects at every level:

| | **GEPA's Pareto** (paper §3.1, Alg. 2) | **Evolve's Pareto gate** (Janvi's TDD) |
|---|---|---|
| What the axes are | **task instances** — one objective per case in `D_pareto` | **judge rubric dimensions** — 5 axes |
| What it decides | *which parent to mutate next* — a sampling distribution | *whether a candidate is accepted* — a pass/fail gate |
| How it's used | build per-instance best-score sets, prune strictly dominated candidates, sample ∝ how many instances a candidate leads | require the child to no-worse-dominate the parent on all axes |
| Failure it prevents | local optima / premature convergence (Mouret & Clune "illumination") | (intended) accepting a candidate that regresses a dimension |
| Effect of axis correlation | more instances = a richer frontier; correlation is not a hazard | correlated dims make domination easy → false-accept rate rises toward 50% (**item 16**) |
| Reference implementation | `candidate_selection_strategy: Literal["pareto","current_best"] = "pareto"` | no counterpart in GEPA |

- **The load-bearing consequence: GEPA's acceptance test is a plain scalar.** Algorithm 1 lines 13–14 — compute `σ, σ′` = average minibatch score before and after, accept `if σ′ improved`. Multi-objective reasoning appears *nowhere* in acceptance. Only after a candidate is accepted on that scalar is it evaluated on `D_pareto`, and that evaluation feeds **parent selection**, not admission.
- So **GEPA cannot be cited in support of a Pareto acceptance gate.** If anything it is evidence for the opposite: the paper's results come from single-scalar acceptance plus Pareto-diverse *exploration*. Saying "we use a Pareto gate, like GEPA" in a doc comment is the kind of error a reader who has read the paper will catch.
- **This independently converges with Lesson 9's rubric finding.** Implicit aggregation (one score) beat explicit weighted rubrics in the rubric literature; GEPA accepts on one aggregate score; and item 16 showed the 5-axis gate's false-accept rate is undefined until the correlation matrix is measured. Three separate paths to the same recommendation: **accept on one number, and spend the multi-objective machinery on keeping the search diverse instead.**
- **Constructive version of the review comment** (the shape that improves the TDD rather than scoring a point): keep the axes as *diagnostics and as parent-selection diversity*, move *acceptance* to a single aggregate with a paired-bootstrap margin (IC artifact #2), and note that GEPA's own `"current_best"` vs `"pareto"` flag makes the exploration half a one-line ablation too.

## D. KB resources (ranked; full sweep in session notes)

**Tier 1 — read before finalizing the design:**
1. `kb/hard/raw/cameron-wolfe/rubric-based-rewards-for-rl.md` — rubric design, implicit vs explicit aggregation, negative rubrics for discovered hacks. Directly applicable to the 5-dim rubric question.
2. `kb/hard/raw/cameron-wolfe/applying-statistics-to-llm-evaluations.md` — CIs, paired analysis, power. Fixes both the 20-sample problem and the Pareto-on-noise problem. **READ 8/14 → Lesson 6 (§H) + critique items 16–17.** Primary sources behind it: Miller 2024 (arXiv 2411.00640, Anthropic — SEs on evals, clustered SEs, paired differences, power/sample-size formula); Bowyer et al. 2025 (arXiv 2503.01747 — don't use the CLT under a few hundred datapoints).
3. `kb/hard/raw/cameron-wolfe/the-anatomy-of-an-llm-benchmark.md` — golden-set audits (MMLU-Redux removed 6.5% of items), contamination control, saturation. The case-bank curation playbook.
4. `kb/hard/raw/cameron-wolfe/reward-models.md` + `kb/hard/raw/lilian-weng/reward-hacking-in-reinforcement-learning.md` — the coupled-optimizer hazard in §8, from first principles.
5. `kb/hard/wiki/llm-evaluation.md` — eval taxonomy + EDD framing ("evals are specifications").

**Tier 2:** `eugene-yan/evaluating-the-effectiveness-of-llm-evaluators` (κ/ρ targets: judge-human ≥ human-human is the ceiling; bias catalog), `wiki/counterfactual-evaluation.md` (replay math, IPS/DR, insufficient-support — the formal frame for §12), `cameron-wolfe/online-versus-offline-rl-for-llms.md` (where offline optimization fails: OOD), `louis-wang/the-harness-is-the-moat` (fixture infra as the durable asset — validates Evolve's core bet).

**KB gap — CLOSED 8/15.** Both now in the KB proper (full text, not summaries):
- `kb/hard/raw/arxiv/gepa-reflective-prompt-evolution-can-outperform-reinforcement-learning.md` — arXiv 2507.19457v2, ICLR 2026 Oral. Main body + references + appendices A–J and N. Appendices K/L/M (raw evolved-prompt dumps, ~4.9k lines) omitted by design; note in the file. **Read for:** Algorithm 1 (the loop, and the scalar acceptance test at lines 13–14), Algorithm 2 (instance-wise Pareto selection), §3 Reflective Prompt Mutation + evaluation-traces-as-diagnostic-signal, §3.1 Pareto illumination, Appendix C (the actual meta-prompt), Appendix D.1 (system-aware merge).
- `kb/hard/raw/dspy/dspy-gepa-reflective-prompt-optimizer.md` — new `dspy` source slug. The two docs pages plus `dspy/teleprompt/gepa/gepa.py` in full, since the published pages are mkdocstrings stubs. **Read for:** the `GEPAFeedbackMetric` protocol (`pred_name` / `pred_trace` — where per-component credit actually enters), `component_selector` (round-robin default), `candidate_selection_strategy` (`"pareto"` vs `"current_best"`), `instruction_proposer`, `DspyGEPAResult`, and the merge/budget knobs.
- Fallout: critique item **13** upgraded and item **18** added (both below/above). Routing fix: `arxiv`, `anthropic`, `dspy` added to `HARD_SLUGS` in `scripts/ingest.py`, which had been silently routing them to `soft`.

**Project sources folder (`sources/`, James-supplied links filed 8/12):**
- `pydantic_gepa_prompt_optimization_2026-02-02.md` — worked GEPA+evals pipeline; adapter pattern, train/val split, "evaluator blind spots get exploited," budget guidance (start 20–50 calls). Closest public analog to Chao's Stage 1.
- `superagentic_gepa_omni_superqode_2026-07-26.md` — GEPA Omni multi-engine harness optimization with a guarded evaluator: mutation-surface enforcement, non-regression audit, sealed held-out cases, staged adoption. The safety model maps directly onto Evolve's human gate + `never_mutable`.
- `deepeval_what_is_an_eval_harness.md` — eval-harness taxonomy; evals vs guardrails distinction.
- `langchain_better_harness_hill_climbing_2026-04-08.md` — "evals are training data for agents"; sourcing from production traces, holdout-as-generalization-proxy, agents as "famous cheaters" → supports the lockbox argument.
- `harness_evals_github_readme.md` — open-source eval framework (normalized 0–1 Score + threshold); EvalHub-adjacent comparison point for the build-vs-adopt paragraph.
- `arxiv_2607.12227_rethinking-harness-evolution-evals.pdf` — "Rethinking the Evaluation of Harness Evolution for Agents" (Wang et al., AI2/UW, 13 pp) — directly on how to evaluate the kind of loop Evolve is.
- Plus the two source proposals themselves: `chao_detect_eval_proposal_2026-07-09.pdf`, `janvi_evolve_tdd_2026-08-04.pdf`.

## E. James's IC lane

Recommendation: **own the eval-integrity layer + the hindsight case bank.** Four concrete artifacts, all IC-shaped (schema, module, protocol, dataset), none colliding with Chao (judge), Gideon (task performance), or Janvi (loop):

1. **EvalResult v2** (co-authored with Janvi + Chao): add trial-level scores/variance, `judge_version`, `fixture_snapshot_id`, case provenance. Small PR, load-bearing forever.
2. **The significance-aware gate**: paired-bootstrap dominance test module Evolve calls instead of raw mean comparison. ~a day of real IC work, removes the biggest silent failure mode.
3. **The lockbox protocol**: frozen held-out set + judge-versioning rule + blind-audit cadence + the contamination policy (§9). This is James's own 7/24 warning, made executable.
4. **The hindsight-recall case bank** (flagship): world-at-T snapshots from the cycle archive scored against T→T+n shipped outcomes, seeded with his own historical catches (Following CG cycle 4, INTEREST.prod, VLM gap cycle 9). He is the only person who holds these labels; it converts "recall is hard" from a known gap into a measured number.

Timing: Chao's next step is GEPA-optimizing the judge on ~20 cards — the lockbox (#3) needs to land **before** that run, i.e., this week. Strategic kicker: the agent-agnostic contract + case bank is precisely the "eval/improvement layer applied to agent output on both sides" the V2 Shifu message offers — this IC work is what makes that offer real.

---

## F. Pick-up plan — next session (Tue 8/12 AM target)

**Status 8/12 AM: items 1–3 drafted → `lockbox_protocol_2026-08-12.md` · `seam_message_drafts_2026-08-12.md` · `evalresult_v2_straw_schema_2026-08-12.md` (schema grounded in the TDD PDF, now filed under `sources/`). Item 4 scoped in §G below. Item 5 superseded: James supplied 6 links (GEPA/harness-eval focused), all captured verbatim into `sources/` (see §D) — the GEPA paper itself + DSPy docs remain un-ingested into the KB proper. Item 6 still open.**

**Status 8/12 PM (evening teaching session — full log in §H): lockbox one-pager updated with the judge-as-gate corollary; seam drafts file now carries the merged V2 message as the recommended send; arXiv paper read → critique §15½ added. Wed 8/13 AM pick-up: (1) post the lockbox note on Chao's doc — still the time-critical move; (2) send seam V2 (Dafang heads-up first); (3) James answers the two open exercises in §H before posting the TDD review comments; (4) then the TDD reviewer-comment pack (§C items + §15½ baseline arm + schema offer — Leo drafts on request); (5) items 5–6 of the 8/12 AM list still open.**

**Status 8/14 (teaching session cont.): Lesson 6 delivered — statistics for evals (§H). Produced critique items 16 (Pareto-gate error rates are a function of the unmeasured judge-dimension correlation matrix) and 17 (effective n / MDE — the numbers that size both the calibration set and the case bank). Item 16's ask is the cheapest high-value move now open: request the 5×5 dimension correlation matrix from Chao's judge V1 outputs — no new labels, no new runs, and it sets the Evolve gate design. Exercises 1–2 still owed; checks 3–4 added. Lockbox note posting status still unconfirmed (carried 5×).**

Ranked. Items 1–2 are time-critical relative to Chao's GEPA run; 3–4 are the IC build; 5–6 are cheap parallel moves.

1. **Draft the lockbox protocol one-pager** (frozen human-labeled holdout untouched by both GEPA loops; judge-versioning rule — same judge for search + landing re-run, comparisons only within judge version; blind-audit cadence concentrated on highest-scored cards; contamination policy: calibration cards excluded from Feedback-Curator pattern extraction). Deliver as a comment on Chao's living doc or a short doc he can absorb — the framing is "making my 7/24 asks concrete," not new requirements.
2. **Name the Stage-2 ≡ Evolve-adapter seam** — one message or live conversation with Chao + Janvi (+ Dafang for the TL blessing): Chao owns judge + calibration (the fitness function), Janvi owns the loop, Chao's Stage 2 becomes the Evolve Detect adapter. Also raise the EvalHub question (build on it or write the why-not paragraph).
3. **Write the EvalResult v2 straw schema** (trial-level scores/variance, judge_version, fixture_snapshot_id, case provenance) + sketch the paired-bootstrap dominance gate. This is the first real IC artifact — a PR-shaped contribution into Janvi's `evolve/infra/schemas/`.
4. **Scope the hindsight-recall case bank**: pick 2–3 archive cycles with known outcomes, define the world-at-T snapshot format, seed with James's historical catches (Following CG cycle 4, INTEREST.prod, VLM gap cycle 9). Decide v0 size (~30 cases) and where it lives.
5. **Ingest GEPA paper + DSPy docs into the KB** (`/kb-ingest`) — gap found in the sweep; two workstreams depend on the technique.
6. **Read Tier-1 KB articles** if not yet: rubric-based-rewards, applying-statistics, anatomy-of-a-benchmark (paths in §D).

Carried context for the picker-upper: Evolve attribution flag (repo said "Ads MLE," TDD author is Janvi Palan — fix the program-state record when citing upward); James's IC-not-EM intent for this area is explicit; V2 Shifu Slack message (sent to James's inbox 8/11 AM, msg_id 19ff2023aadb5119) promises the eval layer cross-org — check whether it went out and what Roberto's reaction was.

---

## G. Hindsight-recall case bank — v0 scope (drafted 8/12, needs work-side data to build)

**Claim it measures:** discovery, not redundancy — did Detect surface what later proved out, *before* humans did? Replaces the PM-roadmap gold set (§B.5).

**Case format (straw):**
- `world_at_T/` — the fixture snapshot as of date T: the same recorded Asana/Presto/MCP surfaces Evolve already snapshots (reuse Janvi's fixture format — one snapshot standard for both systems, and the `fixture_snapshot_id` field in EvalResult v2 is the join key).
- `outcomes_T_to_Tn.md` — what was shipped/proven between T and T+n (experiment results, launches, reverted bets), each tagged discoverable-at-T: yes/no/partial. This tag is the labor-intensive part and the part only someone with the historical context can do.
- `scoring.md` — hindsight-recall = fraction of discoverable-at-T outcomes the run's cards cover (LLM-assisted matching, human-verified in v0); plus a novelty ledger for cards that match nothing (not penalized — investigated).

**v0 sizing:** 2–3 snapshots (T spaced ≥ a quarter apart), ~30 outcome cases total. Seeds: James's own historical catches — Following CG cycle 4, INTEREST.prod, VLM gap cycle 9 — as the first discoverable-at-T positives; he holds labels nobody else has.

**Where it lives:** beside Evolve's fixture store with `case_source: "lockbox"` semantics — never enters any GEPA loop; it's a measurement set, not training material.

**Blocked on (work-side, invisible from here):** the 66-cycle archive locations, the shipped-experiment record for the outcome window, and picking the 2–3 T dates. First concrete step at work: pull the cycle list, pick T₁, and hand-label ten outcomes as a calibration of effort-per-case.

---

## H. Teaching session log (8/12 evening) — where James's understanding is, and what's open

James asked to be taught the concepts behind the six sources before acting on them. Five-lesson curriculum delivered, interactive. This section is the pick-up state for tomorrow.

**Lessons delivered:**
1. **Vocabulary** (deepeval): eval = dataset + task + scoring rule; harness = everything around the model; eval harness = the infra that runs evals end to end; **eval (offline, measures) vs guardrail (online, acts)** — same scorer, different role.
2. **Evals are training data** (langchain): any signal an optimizer hill-climbs on becomes training data, flaws included (Goodhart; recsys clickbait analog). Corollaries: need a test set the optimizer never touches (= the lockbox); eval-design quality must exceed optimizer strength.
3. **GEPA mechanics** (pydantic): evaluate → reflect (failures + rationales = "textual gradient") → propose (LLM writes targeted edit) → accept/reject (Evolve: Pareto-dominate parent). Three danger-relevant properties: pure selection pressure against the scorer; only sees what's in its dataset (data flow = the security model); Reflex has **two coupled loops** (judge→humans, playbooks→judge) = actor-critic with a critic-in-training.
4. **Guarded-evaluator safety model** (SuperQode/GEPA Omni), expanded on request: four controls — structural validation / mutation-surface enforcement (**score is subordinate to policy**) / non-regression + policy audit / staged adoption — plus Actionable Side Information (diagnostics beyond the scalar). Honest citation guidance: cite the architecture, not the tiny experiment (3+2 cases, 24 evals). Thesis: prevent "the search process redefining what counts as success."
5. **The matched-budget baseline argument** (arXiv 2607.12227 → §15½): better-artifact vs more-attempts; pass@5-not-pass@1 as the fingerprint of resampling; generalization split; Terminal-Bench harness-insensitivity caveat = the honest pro-Evolve counter that the baseline arm would prove rather than assume.

**James's demonstrated understanding (evidence, not vibes):**
- Correctly classified judge-over-graded-cards = eval, judge-as-live-threshold = guardrail.
- Derived lockbox gap #1 himself: frozen against **both** GEPA loops + the Feedback Curator as a third channel. General rule he now holds: *every channel that folds graded-card information back into the system is an optimizer, and each must be explicitly fed or fenced.*
- Honest flag "I don't know enough about GEPA to rank the leak dangers" → taught, then derived together: **judge-as-gate is the worse leak** (survivor-sampled labels → blind spots vanish from label distribution → recalibration self-confirms → loop self-seals; recsys serve→log→train feedback loop; counterfactual-eval "lost support"). Fix: judge-blind grading sample drawn pre-gate + lockbox refresh from the pre-gate stream — **now written into the lockbox one-pager (rule 4 corollary)**.
- Taught gap #2 (he hadn't found it): **finite holdouts wear out under reuse** — the accept/reject bit leaks one bit per generation (Kaggle public-leaderboard analogy); no access rule fixes it; fixes are temporal (lockbox rotation, shadow validation on next live rotation). This is the *why* behind §12.

**Comms decision made (James's call after Leo rec):** NO standalone terminology/basics doc — professor-mode risk, third-doc-beside-two problem, and terminology confusion is a symptom of the unnamed seam. Vehicle = inline doc comments + the 30-min working session; a glossary only if the group asks afterward (demand-pull, co-credited). James's draft opener recalibrated (specific credit over generic praise; terminology demoted from headline to symptom) → merged **V2 message now the recommended send in `seam_message_drafts_2026-08-12.md`**.

**New idea to float to Janvi (from Lesson 4's gap):** Reflex playbooks embed *checks as prose* ("verify against Presto before citing") inside mutable sections — mutation-surface enforcement can't protect them, structural validation can't see them. Proposal: **"protected sentences"** — a `never_mutable` for prose spans — plus the existing backstops (blind audits on top-scored output, negative rubrics).

**Open exercises James owes (answer before posting TDD review comments):**
1. *Lesson 4 check:* a GEPA mutation softens "verify against Presto before including a metric" into "include metrics with a confidence note." Walk it through the four controls — which pass it, and where in the current TDD design does a human first get a chance to catch it?
2. *Lesson 5 exercise:* draft the 2–4 sentence matched-budget baseline-arm reviewer comment for the TDD's §5 (name the confound; the control arm in Evolve's own terms — the 450-invocation budget; framed as making her result more defensible). Leo red-lines it against the paper before it ships. **Upgraded 8/14:** Lesson 6 gives this comment teeth — the baseline arm is only interpretable if the bank can resolve the difference at all, so the comment should carry the MDE number (§17).

---

### Lesson 6 (8/14) — Statistics for evals: how big does the number have to be before it means anything

Source: `applying-statistics-to-llm-evaluations` (Wolfe, over Miller 2024 + Bowyer 2025 + Madaan 2024 + Heineman 2025). Taught because it is the direct input to IC artifact #2 (the significance-aware gate) and it is the argument that settles §6 (GEPA-on-20-labels).

**The frame:** an eval score is not a measurement of your system, it's a *sample* from a super-population of things the system could be asked. Two sources of randomness stack — which cases you happened to pick (`Var(x)`), and the stochasticity of generation + judging on each case (`E[σᵢ²]`). `Var(mean) = (Var(x) + E[σᵢ²/K]) / n`. Every intervention below is an attack on one term.

**The five moves:**
1. **Report SE and n with every mean.** Costs one line of code. Without it, "68% → 74%" is not a claim, it's a number.
2. **Cluster-adjust when cases aren't independent.** Cases from the same cycle/surface/playbook are correlated → effective n is smaller than n. Report clusters C alongside n.
3. **Pair, and resample.** Same cases both arms → build the interval on the per-case *difference*, not on two separate means (comparing overlapping CIs is the wrong and over-conservative test). Positive correlation between arms makes this a free variance reduction. Then raise K until within-case variance is small next to across-case variance. Never buy stability by lowering temperature — that measures a different system.
4. **Power-analyze *before* running.** `n ≈ (z_{α/2}+z_β)²·Var(d)/δ²`. Rearranged, it gives the minimum detectable effect of a bank you already have — i.e. whether an eval is worth running at all. Sample size scales with 1/δ²: half the effect, four times the cases.
5. **Know where the CLT breaks.** Under ~100 datapoints, CLT intervals are too narrow and get worse at the ceiling/floor. Use Bayesian or bootstrap intervals in Reflex's regime.

**Honest tension surfaced (worth holding, not resolving yet):** the variance literature (Madaan, Heineman) finds *continuous* scores — token probabilities, log-likelihood — give far better signal-to-noise than binary correctness, which appears to cut against James's on-record binary-primary position (§7). The reconciliation: binary is right for the **human** label (cheap, reliable, high inter-rater agreement); continuous is right for the **measurement** (lower variance). So — humans grade binary, the judge emits a calibrated continuous score, judge *quality* is scored on binary agreement, and the continuous score is what the gate does statistics on. That is a sharper version of §7, not a retreat from it.

**Where it lands in the Reflex docs:** critique items **16** (Pareto gate error rates ← inter-dimension correlation; the cheap measurement) and **17** (effective n, the 20-card resolution limit, the ~150-cases-for-10-points number, small-n CLT failure). Item 16 is a genuinely new finding — not present in either source doc, not in Chao's or Janvi's review comments to date.

**Checks James owes on Lesson 6:**
3. Chao's judge V1 has already scored cards on 5 dimensions. Before any GEPA run: what single artifact would you ask him for, and what would you do with it? (Answer shape: the 5×5 dimension correlation matrix — and it sets the Pareto gate's design, per item 16.)
4. Evolve reports "evolved spec dominates on 4 of 5 axes, +6 points net fitness, n=40 cases." Name the three questions you'd ask before believing it. (Candidates: how many clusters do those 40 cases span; is that a paired comparison on identical cases; what's the MDE at n=40 — is +6 even resolvable.)

---

### Lesson 8 (8/15) — Credit assignment: what `blame()` is for, and what GEPA actually does instead

Sources: the GEPA paper and DSPy implementation, both ingested today (§D). Taught because §13 has been sitting open since 8/11 as "blame() deserves an ablation," and the review comment could not be written honestly without knowing what the paper does.

**The problem.** A compound system has N modules. A rollout produces one score. Something went wrong; which module do you edit? That is credit assignment, and it is the same problem RL solves with value functions and advantage estimates — except here the "gradient" is text, so the attribution has to be done in language.

**Four places the answer can come from, cheapest to most expensive:**
1. **Don't attribute — rotate.** Round-robin over modules. This is GEPA's default and what the headline numbers were measured on.
2. **Attribute at scoring time, from the evaluator.** The feedback function is handed `pred_name` + `pred_trace` and returns a score *and* text feedback for that specific module. Attribution comes from the thing that knows why the score was what it was.
3. **Attribute at reflection time, implicitly.** Hand the LM the trace, the score, and the feedback, and let it work out what went wrong inside the prompt. GEPA does this on top of (1) and (2) — it's the "implicit credit assignment" the paper names.
4. **Attribute explicitly, post hoc, from judge rationales.** Parse rationales, map complaints to components, pick the culprit. This is `blame()`. It is the only one of the four that GEPA does not do.

**Why the ordering matters.** Each step down adds a place for error to enter. (4) is the worst position: it re-reads a text artifact that was written to *justify a score*, not to *locate a fault*, and it inherits every rationale bias — verbosity, position, self-consistency — into the mutation target. And a misdirected mutation isn't neutral; the wasted rollout is charged against a budget that item 17 already showed is too small to resolve small effects.

**The reframe James should take into the review.** Not "prove blame() works." Rather: *GEPA got its results with round-robin; what does blame() buy over that, and is it measured?* That is a fairer question and a harder one to wave off. And because `blame()` is structurally a custom `ReflectionComponentSelector`, the control arm is a single config value — so "we don't have time to ablate it" isn't available as an answer.

**The constructive move underneath it** (the thing that would actually make Evolve better): push credit assignment *up* to option (2). If the Reflex judge can emit per-component feedback at scoring time, that dominates any post-hoc `blame()`, because the attribution is produced by the evaluator with the trace in hand rather than reconstructed from prose afterward. Whether it can is a real open question about Chao's judge, and it is a good thing to ask him rather than assert.

**Where it lands:** critique item **13** rewritten (burden of proof flipped, ablation cost collapsed to a flag, feedback-function path named), and item **18** added — see §C.

**Checks James owes on Lesson 8:**
5. Evolve runs with `blame()` and the mutation rate on one particular component is 4× the others. Give two readings of that — one where `blame()` is working, one where it's broken — and name the artifact that distinguishes them.
6. You get option (2): the judge can emit per-component feedback. Name the new failure mode this creates that round-robin didn't have. (Hint: what is the judge now jointly optimizing, and against which of the two coupled loops from Lesson 3?)
