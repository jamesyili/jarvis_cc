# 06 — Evaluation, Simulation & Validity

> **Bridge:** Per your own study plan, *"eval IS half of integrity work"* — and it's where your Anthropic loop and the Integrity seat both live. You have an unusually strong hand: your preranking paper is *literally a method for making an offline metric predict online lift*, the UPP P2P stall is a live "is the metric even right?" problem, and RR's program-level holdout is a textbook validity story. Most candidates can recite metrics; you can talk about whether a metric is *valid*.
> **Book:** Ch 23 (designing an eval), Ch 24 (benchmarks), Ch 25 (validity/contamination) — all Tier 1 for you.

---

## 1. The core idea

A model is only as good as your ability to *measure* it, and the deepest failures are not "the model is wrong" but "**the eval lied to us.**" Evaluation has three jobs, in increasing difficulty:
1. **Measure** — compute a number (the easy part).
2. **Correlate** — make the offline number predict the thing you actually care about online (hard).
3. **Validate** — make sure the eval keeps predicting reality as the world shifts and as people optimize against it (hardest; this is where contamination, Goodhart, and distribution shift live).

The senior framing: *"I don't trust a metric until I've shown it predicts the outcome I care about and I understand how it can be gamed or go stale. Most eval debates are actually validity debates wearing a metrics costume."*

---

## 2. The metrics floor (be fluent, don't over-index)

### Classification (integrity / safety / quality)
- **Precision / Recall / F1**; **ROC-AUC** vs **PR-AUC** — *PR-AUC is the one for rare positives* (harm, fraud) because ROC-AUC is optimistic under heavy class imbalance. Saying this unprompted signals you've shipped imbalanced classifiers.
- **The FP/FN trade-off is the answer to most safety questions** — lead with "who pays the false-positive cost vs the false-negative cost," not the AUC. (Your Snap Discover two-tier-demotion story is the worked example.)
- **Calibration** (O/E, ECE) — a score must mean what it says (guide 04).

### Ranking / retrieval
- **Recall@K, MRR, NDCG, MAP, Group-AUC**; **overlap@K / penetration@K** (your preranking metrics). NDCG = position-weighted relevance; Group-AUC = per-user AUC (the right one for personalization).

### LLM / generation
- **Perplexity** (intrinsic, weak), **benchmarks** (MMLU, GSM8K, HumanEval, safety/agentic suites — know the names, Ch 24), **LLM-as-judge** (scalable but biased — position bias, verbosity bias, self-preference), **human eval** (gold but slow/expensive).

---

## 3. The three hard problems (where you're strong)

### (a) Offline → online correlation — *your paper solves this*
The recurring recsys/ML pain: offline metric goes up, online A/B is flat or negative. Your preranking paper's whole thesis: **calibrate the offline score by regressing online lift on it** (positive linear regression on (M_align, M_acc)), and *choose metrics the theory says should correlate* (overlap on unimpressed) over convenient ones (PR-AUC, which in your Table 1 predicted winner direction **incorrectly**). The transferable lesson: *an offline metric is a hypothesis about online behavior; validate it like one.*

### (b) Validity / "is the metric even right?" — *your UPP P2P stall*
When cross-surface pretraining is "not hurting but not clearly helping," the **first fork is methodological**: is the offline eval measuring transfer at all? **If the metric is the bottleneck, more engineers won't fix it — it's a careful eval-design problem, not a sprint.** That sentence is a Director-altitude eval insight: knowing when a result is a measurement artifact vs a real negative. Most people throw bodies; you diagnose the eval first.

### (c) Contamination & Goodhart — *the LLM-eval frontier*
- **Train-test contamination:** if benchmark data leaked into pretraining, the score is fiction. Dedup, canary strings, temporal holdouts (your preranking paper's *forward test set* — train on Jul–Dec, test on Mar–Apr — is exactly this discipline).
- **Goodhart / optimizing the eval:** once a metric is a target it stops being a good metric (reward hacking, guide 05). Mitigate with held-out evals, rotating sets, adversarial/red-team evals.
- **Real-world validity:** does the benchmark predict deployed behavior? Safety evals especially must be *adversarial and distribution-shifted*, or they pass right up until someone attacks the system.

---

## 4. Simulation & online testing

- **Offline policy evaluation / replay:** estimate a new policy's value from logged data without shipping it (counterfactual / off-policy eval). The honest caveat: logged data only covers actions the old policy took — coverage limits validity.
- **Simulation before live = Reflex's "Simulate" stage** — estimate impact offline before live experimentation, and the **BuildValidator evaluates generated code against *real merged PRs*** (ground-truth replay). That's eval-against-reality, not eval-against-a-proxy.
- **Online: A/B tests** with **guardrail metrics** (your preranking A/B held WAU, hide, report neutral across every arm — *you don't ship an engagement win that moves a harm guardrail*), novelty effects (new things spike then regress — run long enough), interleaving for ranking, shadow/canary for risk.
- **RR program-level holdout:** the holy-grail validity proof — a *program-level* holdout showing topline **WAU lift in the largest market**, when "moving WAU via ranking is historically rare." The lesson: *isolate the metric that's hard to move and hold it out at the program level, or you'll attribute noise.*

---

## 5. The frontier-lab connection

- **For an Integrity/safety EM, this guide *is* the job.** Eval design, benchmark curation, contamination handling, adversarial validity — Ch 23–25 are your Tier 1 because the seat's day-to-day is "is our harm classifier actually catching harm in the wild, or just on our test set?"
- **The Reflex Skeptic is a self-validating evaluator:** it reads its own `verdict_log` to track precision (human-agreed rate) and recalibrates — an eval that monitors its own validity against fresh labels. Great answer to "how do you keep an automated evaluator honest."
- **LLM-as-judge** for scaling eval ties straight to RLAIF/constitutional (guide 05): the same model-grades-model machinery, with the same bias caveats.

---

## 6. Interview-portable (90 seconds)

> *"My strong opinion on eval is that the hard part isn't computing a metric, it's validity — does the number predict what I care about, and how does it lie. I co-authored a paper that's essentially this: offline preranking metrics that historically didn't predict online lift — PR-AUC literally predicted the winner *backwards* — so we derived which metrics the serving objective says should correlate, then calibrated them against online lift directly, and got to 80% winner prediction with a forward-in-time test set to guard against distribution shift. The same instinct shows up when a result is ambiguous: if cross-surface transfer looks flat, the first question isn't 'add engineers,' it's 'is the eval even measuring transfer' — because a measurement problem and a real negative have opposite fixes. And for anything safety-adjacent, evals have to be adversarial and distribution-shifted, with guardrail metrics that a win is not allowed to move — we hold WAU, hide, and report neutral across every experiment arm."*

**Likely probes:**
- "ROC-AUC vs PR-AUC?" → PR-AUC for rare positives; ROC-AUC optimistic under imbalance.
- "Offline up, online flat — debug it." → offline/online correlation; validate the metric against online lift; check distribution mismatch (your paper).
- "How do you eval an LLM / a safety classifier?" → benchmarks + LLM-judge + human, contamination control, adversarial/red-team, real-world validity, guardrails.
- "How do you know a benchmark isn't contaminated?" → temporal holdout, canaries, dedup; your forward-test-set discipline.
- "When do you trust an offline win enough to ship?" → calibrated correlation + guardrails + a holdout sized to the metric's variance.

---

## 7. Self-test (out loud, from memory)

1. ROC-AUC vs PR-AUC — when does each lie, and which for harm detection?
2. Your offline metric improved, online didn't. Give the three most likely causes and how you'd distinguish them.
3. What is eval *validity* vs eval *measurement*? Use the UPP P2P case.
4. What is contamination, and three controls? How does a forward-in-time test set help?
5. Why hold guardrail metrics neutral, and which ones for a recsys vs a safety system?
6. What makes a *safety* eval different from a capability eval?
7. How does the Reflex Skeptic keep itself calibrated?

*This is half the Integrity seat — drill it. Hoang Ch 23–25 deeply; the anchors are your own preranking, UPP, and RR docs.*
