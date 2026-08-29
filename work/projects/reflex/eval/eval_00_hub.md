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
| **`eval_05_verifiability_and_attempts_store.md`** | me, pre-circulation | program strategy: partition card failures by verifiability, and build a store of what was tried. **New 8/15** |
| **`eval_09_paper_learnings_plain.md`** | James (reading doc) | the eight papers behind the Curator/Skeptic work in plain language — built / found / means — ending in the six recurring ideas that are the menu for the improvement grill. **Read before `eval_08`.** New 8/28, emailed |
| **`eval_08_memory_literature_vs_curator_skeptic.md`** | me → Andrew (Detect: DS Agent ledger, keyed Skeptic retrieval, schema fields), Curator owner (store properties), Janvi (Evolve rejection ledger + A/A run), Chao (measurements) | the twelve papers against the Curator/Skeptic as built: write side ahead of the literature, read side where every large number is. Five findings, six store properties, seven-step order. **New 8/28** |
| **`eval_07_world_store_proposal.md`** | me → then Andrew/Dylan (homing), Janvi (contract), Chao (eval consumer) | the World Store + LR Connector proposition — Detect-stage memory closing the Prove→Detect gap; executes the corpus half of `eval_05`. **New 8/20, grilled + ratified in-session** |

Not part of this set: `../messaging/seam_message_drafts_2026-08-12.md` (Shifu comms), `../research/sources/` (verbatim inputs), `feedback_curator_and_skeptic.md` (the Curator design doc `eval_04` builds on), `reflex_eval_evolve_notes_0816.html` (the 8/16 consolidated working-notes export from the work side — the iteration record these docs were synced against on 8/20), and **`feedback_curator_skeptic_deepdive_0828.md`** (work-side walkthrough of the Skeptic + Curator as built — prompts, schemas, the two hero traces; dropped by James 8/28; the ground truth `eval_08` is written against).

---

## 2. State of play (8/15)

**Update 8/28 — the memory set landed.** James supplied four sources (Recuris, WikiSkill, Scroll, Perplexity Brain) and the work-side **Curator/Skeptic deep-dive** (`feedback_curator_skeptic_deepdive_0828.md` — prompts, schemas, hero traces as of 8/28). Filed: all four in the KB (`perplexity` slug added), entries 9–12 in `eval_06` Part 1b, and **`eval_08`** — the synthesis. Headline: the Curator (write side) is ahead of all twelve papers; the read side is unbuilt — no Progress ledger in the DS Agent (Recuris: +23.9 for working state vs +2.0 for skills), the Skeptic reads the store wholesale and decides what applies (the regime Recuris measures below *no skills*), and `verdict_log.jsonl` can't say which memory component failed (attribution 13% from outcome alone vs 64.8% from a structured trace). Open item 14 now has a spec (`eval_08` §2.1). Every proposed change is prompt-and-schema and measurable on existing logs; first check is the `human_agreed` backfill rate.

**Update 8/20 — the 8/16 consolidated notes landed** (`reflex_eval_evolve_notes_0816.html`, dropped into `eval/` by James; the work-side iteration record — glossary + eval_02–05 + a references section, one day newer than this folder's 8/15 state). Repo synced to it 8/20:
- **`eval_01` revised to the 8/16 state:** objects renumbered (pattern store → 5, Curator groups → 6), object 7 renamed **Record of System Launches** (hindsight set now the shorthand alias), new **2-vs-4** section (judge-scoped vs program-scoped holdout — James's question), and Part B reworked — the Pareto collision expanded into the load-bearing argument for `eval_03` §1–2, and **`blame()` upgraded from a naming fix to an open design question for Janvi and Chao** (three ordered questions in `eval_01` Part B: mechanism? signal? was round-robin considered?). Raise it in the same conversation as open item 5's seam naming — it's the same seam (judge blind spots would mis-target Evolve's entire search).
- **Lesson 17 closed** (see §9 row 17) — the notes' references section carries full readings of the YouTube paper and EvoRec.
- **Canonical Google-Doc links for Chao's proposal and Janvi's TDD** are now on record (§8) — they existed nowhere in the repo before this drop.
- **Later same day: `eval_07_world_store_proposal.md` written** — James's new build (the LR Connector + World Store, Detect-homed, Curator as dual-store custodian). Decisions D1–D5 ratified in-session; glossary candidate object 8 filed. First move is Phase 0 verification at work (Helix→Glean access, the §7.5 slice query). Supersedes nothing — it *executes* `eval_05` §5's corpus half and forces the Curator-ownership resolution productively.

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
10. **Classify existing rejected cards by failure type** — the fraction that are mechanically adjudicable rather than judgment calls. In chess it was 78%, and that number is why AutoHarness worked. Gates all of `eval_05`. An afternoon, no new data. **Probably the highest value-per-hour item on this list.**

**The IC build (never started)**

11. **EvalResult v2 + the paired-bootstrap dominance gate.** Both specified in `eval_03`. This is the only artifact on the list nobody else will produce, and it's the prerequisite for the gate redesign.
12. **Hindsight-recall case bank v0** — blocked on work-side data (§7 below).

**Curriculum**

13. ~~Lesson **17** (Google/YouTube self-evolving recsys + EvoRec) remains~~ — **closed 8/16** (per the consolidated notes' references section). **All seventeen lessons are now closed.**
14. **Check whether Detect maintains anything like Belief or Progress** (§9, Lesson 16). ~~A code question~~ — **answered from the 8/28 deep-dive:** Experience = `quality_patterns.md` + `analytical_checks/` + `dead_ends.yaml`; Belief = `context.md` (hand-maintained summary, no provenance — the World Store is the fix); **Progress = nothing** (`cycle_log.jsonl` phases are post-hoc, written for the auditor, never read back mid-investigation). Spec for the missing ledger in `eval_08` §2.1.

**From `eval_08` (8/28) — cheap, on existing logs, none started**

15. **`human_agreed` backfill rate** in `verdict_log.jsonl`. Gates every Skeptic measurement below; if mostly null, the finding is process, not schema.
16. **Claimed-but-not-executed share** of `fail_reasons` — cards asserting a VLM check / chart / query they can't show. Decides whether the DS Agent's Progress ledger is the first build or the third (`eval_08` §2.1).
17. **Skeptic precision under wholesale vs keyed retrieval** — needs the `patterns_applicable` field first (`eval_08` §2.2–2.3).
18. **The schema PR** — `card_type`, `patterns_applicable`, `disconfirm_queries` on `SkepticVerdict`; `summary`, `kind` (domain fact vs model workaround), `motivated_by` on registry/dead-end entries; `consulted_patterns` on DS card output. Same class as EvalResult v2 (`eval_08` §2.3, §2.5).
19. **Evolve rejection ledger + A/A run** → Janvi as an `eval_03` addendum (`eval_08` §2.4). Recuris: a 12-case dev slice at K=4 couldn't resolve +12 points; Evolve's 450-invocation budget buys about that.

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

**19. The attempts store — the rigorous version of Phase 3 (new 8/15, from Lesson 15 → `eval_05`).** Phase 3 proposes *shipped-experiment counts* as a business metric, which item 10 dismisses as a confounded program KPI. It is confounded — but the instinct underneath it is right, and the fix is to stop counting and start joining. Take the experiment platform (every experiment that ran, including the ones nobody wrote up) and LR docs (which by construction record only what worked), join both to the hypothesis that motivated them, and you have a corpus that supports a measurement the program currently cannot make: **Detect's precision against reality** — of the things Detect proposed, how many were tried, and how many failed. Today a Detect card that was pursued and didn't pan out is invisible; it looks identical to a card nobody read.
- **LR docs are the numerator, the experiment platform is the denominator, and the gap between them is the negative-results corpus nobody wrote down.** That gap is the highest-value content and it already exists — it has just never been read as a corpus.
- **Ownership splits.** The eval framing is Chao's — it is his Phase 3, made non-confounded. The LR/Helium integration is data engineering and sits closer to Gideon's logging and infra lane. Handing the whole thing to Chao attaches a quarter-scale data project to the person on the critical path for judge calibration, which is the first thing that would slip.
- **The seam to name in the ask, not after:** this is the *same join* as my hindsight case bank (§7). The hindsight bank joins the cycle archive to the shipped-experiment record with outcome labels; the attempts store joins the experiment platform to LR docs with hypothesis labels. The expensive half — tying experiments to hypotheses — is common to both. Propose it as **one join, two consumers**, or this repeats item 1 exactly: two people building the same pipeline under two names, discovered in October.
- **One distinction to keep explicit**, since collapsing it invites a scope-creep rejection: the store *as an eval source* (precision against reality) is Chao's; the store *as a retrieval corpus at card-generation time*, so Detect stops re-proposing tried things, is agent capability — the Skeptic, Andrew's surface. Same corpus, two consumers, different owners, only the first is eval.
- Design constraints that must travel with the ask: mechanism-of-failure is a required field (an underpowered null and a real negative are opposite lookups); the store is time-indexed and a run anchored at T may read only decisions before T, or it leaks the answers into the hindsight measurement; and "already tried" annotates, never rejects. Full treatment in `eval_05_verifiability_and_attempts_store.md` §5.

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

**Added 8/28 — the memory and curation set** (James-supplied links; full text in the KB, entries 9–12 in `eval_06` Part 1b, synthesis in `eval_08`):
- `kb/hard/raw/arxiv/recursive-experiential-working-memory-evolution-for-long-horizon-agent-harnesses.md` — Recuris, arXiv 2608.24876 (NUS / Stanford / Oxford / Princeton).
- `kb/hard/raw/arxiv/wikiskill-compiling-agent-experience-into-persistent-knowledge-for-skill-evolution.md` — WikiSkill, arXiv 2608.27454 (Google Research / Virginia Tech). **Read for:** §3.1 the three-layer split (traces / wiki / skills), §3.2.4 the harness-written `skill-impact.md` rejection ledger, Table 3 the executor-walled-off-from-wiki ablation, Table 4 create-vs-edit counts, Appendix E the Maintainer and Proposer prompts.
- `kb/hard/raw/arxiv/context-as-an-environment-programmatic-context-management-for-long-horizon-agents.md` — Scroll, arXiv 2608.21690 (Alibaba / Columbia). **Read for:** Table 3 (the only controlled comparison — compaction vs variable-binding at 128K→256K), Fig. 3 ablations, §2.4 headlines-as-Progress, Appendix D failure annotations (D.2 disconfirming query, D.3 framing-before-retrieval, D.4 head-and-tail sampling).
- `kb/hard/raw/perplexity/brain-agentic-memory-as-a-knowledge-wiki.md` — Perplexity Brain product post, **reconstructed from secondary coverage** (the post is Cloudflare-walled from this network; replace with verbatim when fetchable). New `perplexity` slug added to `HARD_SLUGS`.

**Project sources folder (`sources/`, James-supplied links filed 8/12):**
- `pydantic_gepa_prompt_optimization_2026-02-02.md` — worked GEPA+evals pipeline; adapter pattern, train/val split, "evaluator blind spots get exploited," budget guidance (start 20–50 calls). Closest public analog to Chao's Stage 1.
- `superagentic_gepa_omni_superqode_2026-07-26.md` — GEPA Omni multi-engine harness optimization with a guarded evaluator: mutation-surface enforcement, non-regression audit, sealed held-out cases, staged adoption. The safety model maps directly onto Evolve's human gate + `never_mutable`.
- `deepeval_what_is_an_eval_harness.md` — eval-harness taxonomy; evals vs guardrails distinction.
- `langchain_better_harness_hill_climbing_2026-04-08.md` — "evals are training data for agents"; sourcing from production traces, holdout-as-generalization-proxy, agents as "famous cheaters" → supports the lockbox argument.
- `harness_evals_github_readme.md` — open-source eval framework (normalized 0–1 Score + threshold); EvalHub-adjacent comparison point for the build-vs-adopt paragraph.
- `arxiv_2607.12227_rethinking-harness-evolution-evals.pdf` — "Rethinking the Evaluation of Harness Evolution for Agents" (Wang et al., AI2/UW, 13 pp) — directly on how to evaluate the kind of loop Evolve is.
- Plus the two source proposals themselves: `chao_detect_eval_proposal_2026-07-09.pdf`, `janvi_evolve_tdd_2026-08-04.pdf`.

**Canonical internal doc links (filed 8/20 from the 8/16 notes):**
- Reflex Detect Eval — Chao Wang: https://docs.google.com/document/d/1mIFj1vzClSwXegocdkYwAdzBxXpMiT3mr9PDXQ9z6mE
- Reflex Evolve TDD — Janvi Palan: https://docs.google.com/document/d/1IyTAM2xXOfnOFVEovkasPFNcvW1Oj5EleW1yJB21lpY/edit?tab=t.0
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
| 11 | Reliability ceiling — the ceiling is a number *plus a metric*; κ vs percentage agreement reverses conclusions | 8/15 | `eval_02` sizing note rewritten (3-branch decision table + the disagreement-set ask); rationale-bias numbers → `eval_03` §3; collision 7 → `eval_01` |
| 12 | Replay validity — hindsight recall's unsupported region; the survivorship flaw one level deeper | 8/14 | salience stratification, novelty ledger, exploration budget |
| 13 | Anthropic long-running-agent harness | 8/15 | thin source. Two usable items → `eval_03` §6, §7 |
| 14 | SkillOS — the curator is the bottleneck | 8/15 | `eval_04` entire; compression objective → `eval_03` §5 |
| 15 | AutoHarness — harness beats model size when the critic can't lie; credit assignment from the error signature | 8/15 | `eval_05` entire; §15½ reconciliation (both papers agree evolution works within-task, not across); third parent-selection strategy |
| 16 | EvoHarness-RL — BPE harness state; structure is cheap, training is expensive; harness annealing | 8/15 | the verifiable-signal reframe and the RL sequencing argument (above); BPE gap → open item 14; annealing as a Curator health metric → `eval_04` |
| 17 | Google/YouTube self-evolving recsys + EvoRec — the two production existence proofs | 8/16 | YouTube: the two-loop split (cheap fast proxy / expensive slow truth); Reflex has the fast loop (judge) and **is missing the Slow Loop** (experiment journal → live experiments → north-star feedback) — another argument for the attempts store + Record of System Launches; guardrails-as-explicit-constraints → veto criteria. EvoRec: **the single most useful citation for arguing the Curator deserves investment** (+1.85% revenue from distilling methodology out of past experiments); curation is a first-class component, not plumbing |
| 18 | The memory set — Recuris, WikiSkill, Scroll, Perplexity Brain — read against the Curator/Skeptic as built | 8/28 | `eval_06` entries 9–12; `eval_08` entire. Write side ahead of the literature; read side unbuilt: Progress ledger (Recuris WM-only +23.9† vs EM-only +2.0), keyed vs wholesale retrieval (65.6 vs 83.6, below no-skills 82.0), component attribution (13.0 → 64.8%), Evolve rejection ledger (WikiSkill `skill-impact.md`), A/A before the gate (±7 points on 86 tasks). Open item 14 closed; items 15–19 opened |

**Positions I now hold (derived in session, not just read):**
- **The memory layer has a write side and a read side; Reflex built the write side and the numbers are on the read side** (8/28, Lesson 18). Capture, provenance, conflict reports, never-silent retirement — ahead of all twelve papers. What's missing: a working-state ledger in the investigating agent (the largest single number in the literature, and worth more than the skills it would sit beside), keyed retrieval into the Skeptic (the same store read wholesale measures *below* having no store), and logs that name the component that failed. Corollary for the standing "growing patterns file = immature" position: it holds **when the consumer reads wholesale** — Recuris's 51/2/0 store cost nothing because invocation was gated. Fix the read side and growth becomes cheap.
- *Every channel that folds graded-card information back into the system is an optimizer, and each must be explicitly fed or fenced.* Channels: judge GEPA, playbook GEPA, Feedback Curator.
- **Judge-as-gate is the worse leak** than judge-as-scorer — survivor-sampled labels mean blind spots vanish from the label distribution and recalibration self-confirms. Fix is in `eval_02` rule 4's corollary.
- **Finite holdouts wear out under reuse** — the accept/reject bit leaks one bit per generation. No access rule fixes it; the fixes are temporal (rotation, shadow validation).
- **The verifiable-signal reframe — the standing position on where this program's leverage is** (8/15, after Lessons 14–16). Every technique in this literature optimizes against a reward that cannot lie: SkillOS on task success, AutoHarness on legal-move validity checked by the environment, EvoHarness-RL on task-solved. Three labs, three techniques, one shared precondition. **Reflex cannot run any of these playbooks — not because it is generally immature, but because of one specific missing thing: a critic you can trust.** That is the eval-integrity layer plus the verifiability partition in `eval_05`. Say it this way, not the other way:
  - ~~"We're too early for the fancy stuff, we have basics to do first."~~ — sounds like hygiene, gets deprioritized.
  - **"Every technique in this literature runs on a verifiable signal. We don't have one. Building it is the unlock, not the chore that precedes the unlock."** — which is also the more accurate reading of the evidence, and the answer to why a senior engineer is spending IC time on schemas and holdout protocols.
- **RL/finetuning: not yet, and the sequencing argument is better than the cost argument** (8/15, revised after Lesson 16). The cost argument still holds — GEPA reached 38.61% on IFBench in 678 rollouts where GRPO needed 24,000 for 35.88%, against Evolve's whole 450-invocation budget. But the sharper point is sequencing: in EvoHarness-RL, RL buys exactly one thing, a **coordination policy** over externalized state, and **you cannot learn a policy over state you have not externalized.** Ladder: trustworthy fitness signal → externalized harness state → prompt/harness optimization → weight optimization. We have not cleared rung one, and rung one is my IC lane.
- **Structure is cheap; training is expensive; most of the value is in the structure** (8/15, Lesson 16). On ALFWorld's unseen split: base ReAct 50.0% → **BPE harness at prompt time with zero training 77.6%** → SFT 69.4% (*worse than prompt-time*) → cost-aware GRPO 86.6%. The untrained structure captured **27.6 of 36.6 points**. The same harness lifted GPT-4.1 by +22.1, GPT-5 by +25.7, and pushed Claude Opus 4.5 to 98.5% — so it is not a small-model crutch. Third consecutive paper where **structure beat scale**. Corollary worth holding: SFT made generalization *worse* than doing nothing, because imitating good harness use is not the same as learning when use is worthwhile.
- **BPE — the harness-state abstraction, and what Reflex is missing.** EvoHarness-RL externalizes three policy-facing states: **Belief** (task-relevant facts inferred from interaction), **Progress** (task decomposition as `(subgoal, status)` records), **Experience** (cross-episode skills, failure modes, priors), with meta-actions `track` / `commit` / `recall` / `note`. Mapping to Reflex: **Experience = `quality_patterns.md`** (exists); **Belief** possibly `context.md` — *needs checking against the code, not assumed*; **Progress — nothing I am aware of.** The ablations sharpen why that matters: removing Experience produced the lowest overall score (48.6%), and removing Progress "disproportionately degrades performance on long-horizon tasks with dependent subgoals." A Detect investigation *is* a long-horizon task with dependent subgoals — hypothesis, check a surface, pull a metric, verify against another source, decide whether to continue. If no committed subgoal record exists, this literature predicts failures concentrate there, and that is testable against existing cycle logs.
- **Maturity looks like *less* interaction with external state** (8/15, two independent papers). After RL, EvoHarness-RL's harness calls drop to roughly one per episode — the policy internalizes routine scaffold use and reserves external access for when expected benefit exceeds step cost. SkillOS's trained curator shifted from `insert`-dominant to `update`-dominant and used *fewer* skills per example while scoring better. Same shape twice. **A patterns file that grows, and cards that retrieve more patterns over time, is the signature of an immature system, not a learning one.**

**Comms decision (8/12, still standing):** no standalone terminology/basics doc for the group — professor-mode risk, third-doc-beside-two problem. `eval_01` exists as an internal artifact and the work-leo transfer vehicle. Whether any of it circulates is still open.

**Checks I owe:** 1–2 (Lessons 4–5) deprioritized 8/14. Open: 3–4 (Lesson 6), 5–6 (Lesson 8), Lesson 10's blind-test check, 14 (Lesson 15). Answered 8/15: 11–12 (Lesson 11), 13 (Lesson 15 → became `eval_05` §2).

**Two more positions, from Lesson 11's checks (8/15):**
- **At a low human–human κ, the artifact to ask for is the disagreement set with both rationales — not more calibration cards.** Scaling a measurement that doesn't agree with itself buys noise. The rationales separate the two failure modes, which need different fixes: raters interpreting the same criterion differently is a rubric problem and is writable-around; raters holding genuinely different views of what a good card is is an unresolved question about what Detect is *for*, and has to be adjudicated by someone with authority over that.
- **A high human–human κ raises the value of the frozen sets, not lowers it.** Agreement is reliability, not validity — a panel can agree consistently and still be consistently wrong about what makes a card valuable. High κ also means the judge can be fit tightly to the humans, so overfitting the calibration set gets *easier*. The **lockbox** catches the leak (internal validity); the **hindsight set** is the one that answers "are we converging on something meaningful, or just agreeing with each other" (construct validity). Don't conflate them — see `eval_01` §4-vs-7.

---

## 10. Carried context

- My IC-not-EM intent for this area is explicit.
- V2 Shifu Slack message (inbox 8/11 AM, msg_id 19ff2023aadb5119) promises the eval layer cross-org — check whether it went out and what Roberto's reaction was. The agent-agnostic contract + case bank is what makes that offer real.
