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

**13. blame() deserves an ablation.** Credit assignment from judge rationales to components is the hardest part of GEPA here, and rationale biases (verbosity, position) can systematically misdirect mutation. Cheap test: blame() vs. random component selection over a few runs — if blame() doesn't beat random, simplify.

**14. Security and rollback remain the thin sections.** Fixtures contain untrusted text (Asana comments → prompt injection into a headless Claude run). `never_mutable` globs protect specs, but nothing stated protects the fixture store or screens fixture content. Rollback exists implicitly via `versions/vN.md`; write the explicit revert procedure. (These were the named gaps on 8/10; still open.)

**15½. The missing baseline arm (new 8/12, from arXiv 2607.12227 — read after James supplied it).** AI2/UW compared automatic harness evolution against matched-budget test-time scaling on Terminal-Bench 2.1: evolution did **not** consistently beat parallel sampling or sequential refinement; its gains appeared in pass@5 but not pass@1 (i.e., they came from taking more attempts, not from a better harness); and harnesses evolved on a training split transferred almost nothing to held-out tasks (+0.6 pass@1 avg). Their qualitative read — meta-agent edits "memorize fixes rather than distilling strategies" — is §12's overfitting concern observed in the wild. Implications for Evolve: (a) the success criteria need a **matched-budget baseline arm**: run the incumbent spec with K-sample selection at the same compute before crediting the evolution loop; (b) the honest counter-argument in Evolve's favor is that Terminal-Bench is harness-*insensitive* (a shell tool + basic prompt suffices) while Reflex playbooks are harness-*dominant* (the domain strategy lives in the spec) — but that's exactly the claim the baseline arm would prove rather than assume. Raise as a review comment on the TDD's §5 success criteria.

**15. Add the ultimate anti-Goodhart control:** periodic blind human A/B — baseline vs. evolved outputs, rater doesn't know which is which. Net-fitness-delta can drift upward on judge drift alone; blind A/B is the only signal that can't.

## D. KB resources (ranked; full sweep in session notes)

**Tier 1 — read before finalizing the design:**
1. `kb/hard/raw/cameron-wolfe/rubric-based-rewards-for-rl.md` — rubric design, implicit vs explicit aggregation, negative rubrics for discovered hacks. Directly applicable to the 5-dim rubric question.
2. `kb/hard/raw/cameron-wolfe/applying-statistics-to-llm-evaluations.md` — CIs, paired analysis, power. Fixes both the 20-sample problem and the Pareto-on-noise problem.
3. `kb/hard/raw/cameron-wolfe/the-anatomy-of-an-llm-benchmark.md` — golden-set audits (MMLU-Redux removed 6.5% of items), contamination control, saturation. The case-bank curation playbook.
4. `kb/hard/raw/cameron-wolfe/reward-models.md` + `kb/hard/raw/lilian-weng/reward-hacking-in-reinforcement-learning.md` — the coupled-optimizer hazard in §8, from first principles.
5. `kb/hard/wiki/llm-evaluation.md` — eval taxonomy + EDD framing ("evals are specifications").

**Tier 2:** `eugene-yan/evaluating-the-effectiveness-of-llm-evaluators` (κ/ρ targets: judge-human ≥ human-human is the ceiling; bias catalog), `wiki/counterfactual-evaluation.md` (replay math, IPS/DR, insufficient-support — the formal frame for §12), `cameron-wolfe/online-versus-offline-rl-for-llms.md` (where offline optimization fails: OOD), `louis-wang/the-harness-is-the-moat` (fixture infra as the durable asset — validates Evolve's core bet).

**KB gap:** nothing on GEPA/DSPy specifically — worth ingesting the GEPA paper + DSPy docs this week since two workstreams now depend on it.

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
