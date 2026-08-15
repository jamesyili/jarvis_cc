# Reflex Eval — Hub

**What this is:** my working state for the Reflex eval program — where things stand, what's open, what I've critiqued but not yet delivered, and my IC lane. Everything here is for me. The four docs below are for other people.

**Reorganized 2026-08-15.** This replaces `eval_critique_and_ic_lane_2026-08-11.md`, which had grown to nine sections across seven genres. The rule that keeps it from re-tangling: **critique lives here until it becomes a deliverable; then it moves out and this file keeps a pointer.**

## 1. The five docs and who each is for

| Doc | For | Contents |
|---|---|---|
| **`eval_00_hub.md`** | me | this file — state, open items, undelivered critique, IC lane, curriculum index |
| **`eval_01_glossary.md`** | shared reference | 7 dataset objects, 6 name collisions, GEPA↔Reflex and SkillOS↔Reflex mappings. **Also the work-leo cold-start artifact** — pair it with this file |
| **`eval_02_judge_lockbox_protocol.md`** | **Chao** (Gideon, Janvi, Dafang) | 4 rules that must land before the first GEPA run on the judge |
| **`eval_03_evolve_feedback_and_contract.md`** | **Janvi** | 8 design suggestions + the EvalResult v2 schema and gate implementation |
| **`eval_04_curator_measurement_proposal.md`** | **Andrew / Dylan** (Curator owner) | making the Feedback Curator measurable; 3 design deltas |

Not part of this set: `seam_message_drafts_2026-08-12.md` (Shifu comms), `sources/` (verbatim inputs), `reflex_feedback_curator_and_skeptic.md` (the Curator design doc `eval_04` builds on).

---

## 2. State of play (8/15)

| Workstream | Owner | Status |
|---|---|---|
| Detect Eval proposal (metrics phases 0–3) | Chao Wang | Draft 7/9, in review (Gideon, Rahul, Karim, Dafang, Chi) |
| Phase 0 task performance (cycle_log.jsonl, cost/token, S3, audit dashboard) | Gideon Kim | Building; form-based expert review tooling in progress |
| Phase 1 LLM judge + human calibration | Chao Wang (GEPA consultant: Raghav Jindal) | **Judge V1 built (PR#63).** Next: run judge uncalibrated + visualize, collect ~20 PM-graded cards via Asana forms, then GEPA-optimize the judge |
| Evolve TDD (GEPA loop, EvalResult contract, Pareto gate, human gate) | Janvi Palan | Draft 8/4, in review — I'm a named reviewer |
| Feedback Curator + Skeptic | unresolved (flagged for Andrew + Dylan) | design doc exists; unmeasured |
| My on-record positions (7/24 meeting) | — | Binary pass/no-pass over 5-dim composite; curate + hold out a golden set if using GEPA; beware reward hacking |

**Time-critical dependency:** the lockbox protocol (`eval_02`) must land before Chao's GEPA-on-~20-cards run.

**Attribution note:** the repo's 8/10 record says the Evolve design came from "a senior Ads MLE"; the TDD's author of record is **Janvi Palan** (who owns the Evolution stage per Tim's July notes), with Ads folks (Jacob Gao, Dinesh Govindaraj, Helen Xu) as reviewers and the Ads Build Agents as the Build-stage eval source. Get this right before citing the collaboration upward.

---

## 3. Open items (ranked, 8/15)

**Time-critical**

1. **Post the lockbox note on Chao's doc.** Drafted 8/12 as `eval_02`. Posting has never been independently confirmed — carried 5×. It needs to land before the GEPA run on the judge.
2. **Ask Chao for the 5×5 judge-dimension correlation matrix.** Cheapest high-value move open: computable today from existing judge V1 output, no new labels, no new runs. It sets the Evolve gate design (see `eval_03` §1).

**Deliverables ready to go out**

3. **`eval_03` to Janvi** — 8 suggestions + contract. The `is_pareto_axis` contradiction between the 8/12 schema and the 8/15 feedback is resolved inside it; don't circulate the old schema separately.
4. **`eval_04` to whoever owns the Curator.** Ownership was flagged for Andrew + Dylan and I don't believe it was resolved.
5. **Name the Stage-2 ≡ Evolve-adapter seam** — one conversation with Chao + Janvi (+ Dafang). Chao owns judge + calibration (the fitness function), Janvi owns the loop, Chao's Stage 2 collapses into the Evolve Detect adapter. Status unknown. Also raise EvalHub (build on it, or write the why-not paragraph).

**Cheap measurements, fully specified, none started**

6. The 5×5 dimension correlation matrix (item 2 above).
7. Per-criterion score variance, to prune non-discriminative metrics (Lesson 9).
8. The blind test — run Detect with Presto/Asana disabled; whatever it still produces is testing Claude's recsys priors, not discovery (Lesson 10).
9. `quality_patterns.md` growth curve — 341 lines at cycle 13, archive now at 66. No labels, no runs (`eval_04` §3.1).

**The IC build (never started)**

10. **EvalResult v2 + the paired-bootstrap dominance gate.** Both specified in `eval_03`. This is the only artifact on the list nobody else will produce, and it's the prerequisite for the gate redesign.
11. **Hindsight-recall case bank v0** — blocked on work-side data (§7 below).

**Curriculum**

12. Lessons **11** (κ/ρ ceilings), **15** (AutoHarness), **16** (EvoHarness-RL), **17** (Google/YouTube self-evolving recsys + EvoRec) remain. Lesson 16 bears directly on the open "should Reflex consider RL/finetuning" question — provisional answer today is no, on rollout arithmetic (§9).

---

## 4. Structural findings (cross-doc — the highest-order ones)

**1. Chao's Stage 2 and Janvi's Evolve are the same work, described in two docs with two owners.**
Chao's Phase 1 plan Stage 2 = "run calibrated judge in the detect cycle, connect card quality back to playbooks, use GEPA to optimize playbook prompts." Janvi's Evolve Detect adapter = exactly that, with better machinery (Pareto gate, human gate, versioning). If both proceed, you get two GEPA-on-playbooks pipelines by October. The seam should be named now: **Chao owns the judge + calibration (Evolve's fitness function); Janvi owns the optimization loop; Chao's Stage 2 collapses into the Evolve Detect adapter.** This is a one-conversation fix this week.

**2. The EvalResult contract is the right keystone but is missing uncertainty and provenance.**
`MetricScore` carries name/value/bounds/direction/weight — good, rubric lives in values not code. Missing:
- **Trial-level scores or variance.** K trials produce a distribution; the contract passes a scalar. Pareto dominance on noisy means with small K selects on noise. The gate should require dominance with statistical margin (paired bootstrap over cases; CI excluding zero on ≥1 axis).
- **Judge version + fixture snapshot ID.** The judge is itself being GEPA-optimized (Chao Stage 1) while Evolve uses it as fitness. If judge version isn't pinned per run and recorded per EvalResult, score deltas across generations are unattributable. Rule needed: search and landing re-run use the same judge version; cross-generation fitness comparisons only within judge version.

**3. Neither doc answers the EvalHub question.**
Chao's own references list EvalHub — Pinterest's internal offline agent-eval platform (register agents, upload datasets, run simulations, LLM/code graders). Building Reflex eval beside it without a stated reason invites the same platform-consolidation pressure Shifu is applying at the system level. Either build on it or write the paragraph on why not. Adopting it also makes Reflex's eval legible org-wide — strategic value, not just hygiene.

---

## 5. Detect Eval proposal (Chao) — critique, not yet delivered

**4. Metric sprawl; observability and evaluation are conflated.** ~20 metrics across Phases 0–3. Token usage, MCP count, tool calls are telemetry, not evals. Every retained eval metric needs: an owner, a threshold, and the decision it drives. Prune to the ones something acts on.

**5. The recall gold set measures redundancy, not discovery.** Building "recall of hypothesis" against past PM roadmaps scores the agent on rediscovering what humans already found — survivorship bias; the highest-value Reflex cards are the ones humans missed, which by construction can't be in that set. Better: **hindsight replay** — snapshot the world at time T, run Detect, score against what was shipped/proven between T and T+n. The 66-cycle archive + shipped-experiment record makes this buildable today, and it directly answers the "recall is harder than precision" gap Rahul named.

**6. GEPA-optimizing the judge on ~20 labels will overfit.** 20 cards is a fine pilot for *measuring* judge-human agreement; it cannot support *optimizing* the judge prompt. First measure the ceiling: multiple raters on a subset → human-human agreement (Cohen's κ / Spearman ρ); if judge-human is already near that ceiling, GEPA "gains" are fitting noise. Optimize only when ~50+ labels exist, with a held-out split — or leave-one-out CV with variance reported. James's 7/24 meeting comments (binary primary label; hold out a golden set; fear reward hacking) are the right instincts — they should be promoted from meeting notes to requirements in the doc.

**7. Binary-primary, dimensions-as-diagnostics.** Collect binary pass/no-pass + mandatory rationale from humans (cheap, reliable, Netflix precedent already cited). Judge emits dimension scores calibrated to predict the binary; judge quality is measured on binary agreement; dimensions feed the textual gradient only. Never optimize the 5-dim composite — the weights are arbitrary and GEPA will exploit weight artifacts.

**8. Two coupled GEPA loops = systematic reward hacking.** Stage 1 tunes the judge to humans; Stage 2 tunes the generator to the judge. The generator will find the judge's blind spots, and a GEPA-tuned judge has *systematic* blind spots. Mitigations: a **frozen lockbox** of human-labeled cards never seen by either optimizer; periodic blind human audits concentrated on the judge's *highest-scored* cards (hacks concentrate where the judge is happiest); negative rubrics for discovered hacks; cross-model judge spot-checks.

**9. Contamination seam nobody owns.** The Feedback Curator folds learnings from graded cards into quality_patterns.md — which the graded agent reads next cycle. Calibration/gold cards must be excluded from pattern extraction, or scores self-inflate. One sentence of policy now avoids a quietly corrupted eval later.

**10. Phase 3 business metrics are program KPIs, not eval signals.** Funnel survival and shipped-experiment counts are confounded by Presto availability, review bandwidth, and org priorities (the doc says so itself). Report them; never feed them to an optimizer.

**Not yet a deliverable.** When it becomes one it moves to its own doc and this section becomes a pointer — the way §C did on 8/15 when it became `eval_03`.

> **Evolve TDD critique (was §C, items 11–18):** moved to **`eval_03_evolve_feedback_and_contract.md`**. Do not re-add it here.

---

## 6. My IC lane

Recommendation: **own the eval-integrity layer + the hindsight case bank.** Four concrete artifacts, all IC-shaped (schema, module, protocol, dataset), none colliding with Chao (judge), Gideon (task performance), or Janvi (loop):

1. **EvalResult v2** (co-authored with Janvi + Chao): add trial-level scores/variance, `judge_version`, `fixture_snapshot_id`, case provenance. Small PR, load-bearing forever.
2. **The significance-aware gate**: paired-bootstrap dominance test module Evolve calls instead of raw mean comparison. ~a day of real IC work, removes the biggest silent failure mode.
3. **The lockbox protocol**: frozen held-out set + judge-versioning rule + blind-audit cadence + the contamination policy (§9). This is James's own 7/24 warning, made executable.
4. **The hindsight-recall case bank** (flagship): world-at-T snapshots from the cycle archive scored against T→T+n shipped outcomes, seeded with his own historical catches (Following CG cycle 4, INTEREST.prod, VLM gap cycle 9). He is the only person who holds these labels; it converts "recall is hard" from a known gap into a measured number.

Timing: Chao's next step is GEPA-optimizing the judge on ~20 cards — the lockbox (#3) needs to land **before** that run, i.e., this week. Strategic kicker: the agent-agnostic contract + case bank is precisely the "eval/improvement layer applied to agent output on both sides" the V2 Shifu message offers — this IC work is what makes that offer real.

---

## 7. Hindsight-recall case bank — v0 scope (needs work-side data to build)

**Claim it measures:** discovery, not redundancy — did Detect surface what later proved out, *before* humans did? Replaces the PM-roadmap gold set (§B.5).

**Case format (straw):**
- `world_at_T/` — the fixture snapshot as of date T: the same recorded Asana/Presto/MCP surfaces Evolve already snapshots (reuse Janvi's fixture format — one snapshot standard for both systems, and the `fixture_snapshot_id` field in EvalResult v2 is the join key).
- `outcomes_T_to_Tn.md` — what was shipped/proven between T and T+n (experiment results, launches, reverted bets), each tagged discoverable-at-T: yes/no/partial. This tag is the labor-intensive part and the part only someone with the historical context can do.
- `scoring.md` — hindsight-recall = fraction of discoverable-at-T outcomes the run's cards cover (LLM-assisted matching, human-verified in v0); plus a novelty ledger for cards that match nothing (not penalized — investigated).

**v0 sizing:** 2–3 snapshots (T spaced ≥ a quarter apart), ~30 outcome cases total. Seeds: James's own historical catches — Following CG cycle 4, INTEREST.prod, VLM gap cycle 9 — as the first discoverable-at-T positives; he holds labels nobody else has.

**Where it lives:** beside Evolve's fixture store with `case_source: "lockbox"` semantics — never enters any GEPA loop; it's a measurement set, not training material.

**Blocked on (work-side, invisible from here):** the 66-cycle archive locations, the shipped-experiment record for the outcome window, and picking the 2–3 T dates. First concrete step at work: pull the cycle list, pick T₁, and hand-label ten outcomes as a calibration of effort-per-case.

---

## 8. KB resources and sources

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
---

## 9. Curriculum index

Full lesson content is in my own notes, not here. This records what each lesson was, and what it changed.

| # | Lesson | Date | What it produced |
|---|---|---|---|
| 1 | Vocabulary — eval vs harness vs eval harness; eval (offline, measures) vs guardrail (online, acts) | 8/12 | framing |
| 2 | Evals are training data — anything an optimizer hill-climbs on becomes training data, flaws included | 8/12 | the lockbox argument |
| 3 | GEPA mechanics — evaluate → reflect → propose → accept; Reflex's two coupled loops | 8/12 | — |
| 4 | Guarded-evaluator safety model — four controls; score is subordinate to policy | 8/12 | the "protected sentences" idea — **superseded** by `eval_03` §7 (change the container, not the guard) |
| 5 | Matched-budget baseline — better-artifact vs more-attempts; pass@5-not-pass@1 as the fingerprint | 8/12 | `eval_03` §4 |
| 6 | Statistics for evals — SE/n, clustering, pairing, power, where the CLT breaks | 8/14 | critique items 16, 17 → `eval_03` §2 |
| 7 | Validity — internal vs construct; sampling noise shrinks as 1/√n, construct error is flat in n | 8/14 | reframed the hindsight set as the program's **only construct-valid measurement** |
| 8 | Credit assignment — GEPA has no `blame()`; module selection is round-robin | 8/15 | item 13 rewritten, item 18 added → `eval_03` §1, §3 |
| 9 | Rubric design — implicit aggregation beats explicit weights; veto criteria, negative rubrics | 8/14 | dissolves item 16 → `eval_03` §1 |
| 10 | Set curation — the blind test; MMLU-Redux 6.49% audit; GPQA two-stage validation | 8/14 | open item 8 |
| 11 | κ/ρ ceilings — judge-human ≥ human-human is the ceiling | **not delivered** | — |
| 12 | Replay validity — hindsight recall's unsupported region; the survivorship flaw one level deeper | 8/14 | salience stratification, novelty ledger, exploration budget |
| 13 | Anthropic long-running-agent harness | 8/15 | thin source. Two usable items → `eval_03` §6, §7 |
| 14 | SkillOS — the curator is the bottleneck | 8/15 | `eval_04` entire; compression objective → `eval_03` §5 |
| 15–17 | AutoHarness · EvoHarness-RL · Google/YouTube + EvoRec | pending | — |

**Positions I now hold (derived in session, not just read):**
- *Every channel that folds graded-card information back into the system is an optimizer, and each must be explicitly fed or fenced.* Channels: judge GEPA, playbook GEPA, Feedback Curator.
- **Judge-as-gate is the worse leak** than judge-as-scorer — survivor-sampled labels mean blind spots vanish from the label distribution and recalibration self-confirms. Fix is in `eval_02` rule 4's corollary.
- **Finite holdouts wear out under reuse** — the accept/reject bit leaks one bit per generation. No access rule fixes it; the fixes are temporal (rotation, shadow validation).
- **RL/finetuning is not a live option for Reflex** (8/15). GEPA reached 38.61% on IFBench in 678 rollouts; GRPO needed 24,000 for 35.88%. Evolve's whole budget is 450 invocations. The blocker underneath the arithmetic is that the reward — the judge — is uncalibrated and concurrently being optimized. Ladder: trustworthy fitness signal → prompt/harness optimization → weight optimization. We have not cleared rung one, and rung one is my IC lane. Revisit after Lesson 16.

**Comms decision (8/12, still standing):** no standalone terminology/basics doc for the group — professor-mode risk, third-doc-beside-two problem. `eval_01` exists as an internal artifact and the work-leo transfer vehicle. Whether any of it circulates is still open.

**Checks I owe:** 1–2 (Lessons 4–5) deprioritized 8/14. Open: 3–4 (Lesson 6), 5–6 (Lesson 8), Lesson 10's blind-test check.

---

## 10. Carried context

- My IC-not-EM intent for this area is explicit.
- V2 Shifu Slack message (inbox 8/11 AM, msg_id 19ff2023aadb5119) promises the eval layer cross-org — check whether it went out and what Roberto's reaction was. The agent-agnostic contract + case bank is what makes that offer real.
