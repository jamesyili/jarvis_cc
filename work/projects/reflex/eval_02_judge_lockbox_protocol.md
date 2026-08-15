# Eval-Integrity Protocol for the Detect Judge (Lockbox + Versioning)

**Author: James Li · 2026-08-12 · Status: proposal — needs to land before the first GEPA run on the judge**
**Audience: Chao (owner), Gideon, Janvi, Dafang. Deliver as a comment/linked doc on Chao's Detect Evaluation Proposal.**

---

*Framing note (for James, not for the doc): this is your 7/24 meeting comments — binary pass/no-pass, hold out a golden set, beware reward hacking — made executable. Post it as "concretizing what I asked for in the review," not as new requirements.*

---

At the 7/24 review I flagged three things: keep the primary label binary, hold out a golden set if we use GEPA, and watch for reward hacking. Before the first GEPA run on the judge, here's the concrete version of those asks — four rules, each about a day or less of work, all cheaper now than retrofitted.

## 1. The lockbox: a frozen holdout neither optimizer ever sees

We are about to run two coupled optimization loops: GEPA tunes the **judge** to human labels (Stage 1), then GEPA tunes the **generator/playbooks** against the judge (Stage 2). The generator will find the judge's blind spots — and a GEPA-tuned judge has *systematic* blind spots. The only measurement that stays trustworthy is one neither loop ever touched.

**Rule:** Before the first GEPA run, split the human-labeled cards: ~60–70% calibration (GEPA may use), ~30–40% **lockbox** (frozen). Lockbox cards never appear in GEPA train/val data, never as few-shot examples in any prompt, and never in Feedback-Curator pattern extraction (see rule 4). New human labels get split the same way on arrival.

**Use:** After every judge change, report judge–human agreement on **both** sets. Calibration agreement up while lockbox agreement is flat or down = we optimized noise, not judgment → revert. This is a one-line table per run, not a dashboard project.

## 2. Judge versioning: no score comparisons across judge versions

The judge is being optimized while Evolve/Stage-2 uses it as a fitness function. If the judge changes mid-experiment, score deltas are unattributable — we can't tell an improved playbook from a drifted judge.

**Rule:** Every judge prompt/model/rubric change bumps `judge_version`. Every eval result records the `judge_version` that produced it. Within one optimization run, search and the landing re-run use the **same pinned version**. Fitness comparisons across playbook generations are only valid within a judge version; when the judge upgrades, re-baseline.

(Natural home: a `judge_version` field in the EvalResult contract in Janvi's TDD — happy to write that PR. Schema drafted in `eval_03_evolve_feedback_and_contract.md` §2.2.)

## 3. Blind audits, concentrated where the judge is happiest

Reward hacks concentrate in the region the judge scores highest — that's what "hacking" means. So spot-checks sampled uniformly will miss them.

**Rule:** Each optimization cycle (or biweekly, whichever is shorter), a human grades 5–10 cards drawn mostly from the judge's **top-scored** output, blind — grader doesn't see the judge's score, and for evolved-vs-baseline comparisons doesn't know which is which. Discovered hacks become explicit negative rubric items in the next judge version (which bumps `judge_version`, per rule 2).

## 4. Contamination policy: graded cards stay out of the learning loop

The Feedback Curator folds learnings from graded cards into `quality_patterns.md`, which the agent reads next cycle. If calibration/lockbox cards feed that extraction, the system slowly memorizes its own test set and scores self-inflate without quality moving.

**Rule:** Cards used for judge calibration or the lockbox are tagged, and the Feedback Curator excludes tagged cards from pattern extraction. One filter, one sentence of policy, saves us a quietly corrupted eval later.

**Judge-as-gate corollary.** If the judge ever also acts as a live filter (only cards above a threshold surface to PMs), every downstream human label is sampled from the judge's survivors — the judge's blind spots vanish from the label distribution, recalibration then "confirms" the judge, and the loop self-seals. So this policy covers judge-as-gate, not just judge-as-scorer: a fixed fraction of human grading each cycle samples cards **judge-blind** — drawn before the gate, including cards the judge would have rejected — and lockbox refresh draws only from that pre-gate stream.

## Sizing note: what ~20 labels can and can't support

~20 PM-graded cards is a solid pilot for **measuring** judge–human agreement. It's too small to **optimize** the judge against without overfitting. Two preconditions before the first GEPA run on the judge:

- **Measure the ceiling first.** Double-grade a subset (two humans, same cards) → human–human agreement (κ). If judge–human is already near human–human, GEPA "gains" would be fitting noise — and we'd know to invest in rubric clarity instead.
- **Optimize at ~50+ labels** with the lockbox split above (or leave-one-out CV with variance reported, if we truly can't wait). Until then: run the judge uncalibrated, visualize, and accumulate labels — exactly the current plan, just with the split in place from day one.

## What I'm volunteering

- The lockbox split + tagging scheme on the current labeled set (with whoever owns the Asana grading flow).
- The `judge_version` / trial-level-scores / provenance fields as a PR to the EvalResult contract (with Janvi).
- The blind-audit sampling script (draw from top-scored, strip scores, randomize order).

None of this blocks the current plan — run the uncalibrated judge, collect labels, visualize. It just makes sure that when we do turn on GEPA, we can still trust what the numbers say.
