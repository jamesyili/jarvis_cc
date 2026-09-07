---
concept: A/B Testing & Experimentation
tags: [ab-testing, experimentation, causal-inference, statistical-significance]
sources:
  - kb/hard/raw/aman-ai/concepts-ab-testing.md
  - kb/hard/raw/aman-ai/concepts-causal-inference.md
  - kb/hard/raw/eugene-yan/counterfactual-evaluation-for-recommendation-systems.md
last_compiled: 2026-04-05
related: [recsys-evaluation, mlops-monitoring]
understanding: 3  # proven depth (demonstrated in dialogue/practice, or authored)
relevance: 3  # very relevant
knowledge_updated: 2026-09-07
---

# A/B Testing & Experimentation

A/B testing is the primary mechanism for causal inference in product development. It converts ML model improvements into credible business impact claims. Understanding its statistical foundations, its limitations, and when to reach for more advanced methods (counterfactual evaluation, causal inference techniques) is essential for any ML practitioner.

## Why A/B Testing (and Why It's Hard)

Most ML systems generate outcome data that is _observational_, not experimental. Users see items because the system decided to show them those items. The observed interaction data reflects a combination of the system's choices and user preferences — these can't be separated without randomization.

Recommendations in particular are _interventional problems_: different recommendations cause different user behaviors. Evaluating recommendations via offline metrics on historical data is problematic because we're measuring "how well do new recommendations match what users clicked when shown the old recommendations?" — not "how much more would users click on the new recommendations?"

A/B testing solves this by randomly assigning users to treatment (new system) and control (old system), then measuring actual behavioral differences.

## Statistical Foundations

### Core Terms

**Null hypothesis (H₀)**: No difference between treatment and control. The default assumption statistical tests try to reject.

**Alpha (significance level)**: Probability of a false positive (rejecting H₀ when it's true). Standard: 5%. Means we'll falsely claim a significant result 5% of the time when there's actually no effect.

**Beta**: Probability of a false negative (failing to detect a real effect). Standard target: 20%.

**Power (1 - Beta)**: Probability of correctly detecting a real effect. Standard target: 80%. Power increases with larger effect size, larger sample size, and lower metric variance.

**Effect size**: The magnitude of the real difference. Statistical significance tells you _whether_ an effect exists; effect size tells you _how large_ it is. A result can be statistically significant but practically irrelevant (tiny effect, massive sample size).

**P-value**: Probability of observing a result at least as extreme as the data, _assuming H₀ is true_. P < 0.05 means: if there were truly no effect, we'd see this result (or more extreme) less than 5% of the time. This is NOT the probability that H₀ is true.

**Confidence interval**: Range within which the true parameter value falls with specified probability (e.g., 95%). More informative than p-values alone because it shows the effect size and its uncertainty.

### The 5% Standard and Its Trade-offs

The 5% alpha is a balance between:
- **Type I error** (false positive): Launching a feature that doesn't actually work.
- **Type II error** (false negative): Not launching a feature that would have worked.

Setting alpha too low (e.g., 1%): miss more real effects (more false negatives). Setting alpha too high (e.g., 20%): launch more features that don't work (more false positives). The 5% convention is conventional, not sacred. High-stakes decisions warrant lower alpha; exploratory testing can tolerate higher.

### Sample Size Planning

Before launching: calculate the minimum sample size required to detect your minimum practically meaningful effect size at your target power.

```
n ≈ 2 * (z_α + z_β)² * σ² / Δ²
```

where Δ is the minimum detectable effect, σ is metric standard deviation, z_α and z_β are z-scores for alpha and power. Under-powered tests: you might miss real effects. Over-sized tests: you waste traffic and risk novelty effects.

## Designing the Experiment

### Allocation Strategies

**Simple random sampling**: Each user assigned randomly. Mitigates bias, but may not represent rare user segments adequately.

**Stratified sampling**: Divide population into meaningful strata (e.g., new vs. returning users, heavy vs. light users, mobile vs. desktop), sample each stratum independently. Produces more accurate estimates and richer segment analysis.

**Assignment unit**: User-level (consistent experience across sessions), session-level (each session randomized independently), or item-level (different items get different treatments). User-level is most common and cleanest for measuring user behavior changes.

### Success Metrics vs. Guardrail Metrics

This distinction is critical. **Success metrics** measure the desired outcome (e.g., CTR increase, conversion improvement). **Guardrail metrics** are floors that must not regress — e.g., page load time, downstream content diversity, revenue per session.

Guardrails exist because success metrics can be gamed. A ranking algorithm that maximizes CTR might crater watch time. A pricing model that maximizes short-term conversion might increase returns. Guardrails protect against these unintended consequences.

Design rule: a treatment should not be launched if it improves success metrics but violates any guardrail metric.

## Common Pitfalls

### Novelty Effect

A new feature often shows inflated positive results in the first 1-2 weeks simply because it's new. Users explore it out of curiosity, not because it's better. Allow experiments to run until novelty wears off. Don't stop early when you see a positive result.

### Network Effects and Interference

Traditional A/B tests assume user-level independence (stable unit treatment value assumption, SUTVA). This breaks in two-sided marketplaces and social networks:

**Example**: In ridesharing, showing a new algorithm to 50% of riders affects driver supply, which affects the experience of control group riders. The treatment and control groups are not independent.

**Switchback testing** addresses this for marketplace contexts. Used by Uber, Lyft, DoorDash, Amazon. Instead of user-level randomization, alternate between treatment and control at the _market_ level over time intervals. Ensures uniform treatment across the network at any given moment. Challenges: choosing interval length (capture treatment effects, minimize carryover), defining burn-in/burn-out periods at switching boundaries to avoid contamination.

### Multiple Comparisons

Running 20 A/B tests simultaneously at 5% alpha means ~1 false positive by chance. Use False Discovery Rate (FDR) correction (Benjamini-Hochberg) when running many simultaneous tests. Alternatively, pre-register primary metrics to reduce selective reporting.

### Peeking at Results

Checking results before the planned end date and stopping early when p < 0.05 inflates Type I error significantly. Use sequential testing methods (e-values, always-valid p-values) if you need to monitor continuously.

## Causal Inference: When RCTs Aren't Possible

### The Causal Ladder

**Association** (observational): "Users who see feature X have higher retention."
**Intervention** (causal): "If we show users feature X, retention will increase."
**Counterfactual**: "Would this user have retained if they had seen feature X instead?"

A/B tests live at the intervention level. Observational data analysis lives at association. Most ML model evaluation is at the association level — which is why offline metrics diverge from A/B tests.

### Correlation Is Not Causation

Three reasons observed correlations may not be causal:

1. **Confounding variables**: A third factor causes both variables. Ice cream sales and drowning incidents both increase in summer (weather confounds both).
2. **Reverse causality**: The effect might cause the cause. "Users who click recommendations buy more" — but are recommendations causing purchases, or are purchase-intent users more likely to click?
3. **Spurious correlation**: Statistical coincidence (Nicolas Cage films vs. pool drownings).

**Simpson's Paradox**: A trend that appears in subgroups reverses when data is aggregated. Classic example: University admissions data showing higher acceptance rates for men overall, but women with higher acceptance rates within each department — because women applied more to competitive departments. Aggregating without stratifying produces the opposite conclusion. Lesson: always stratify by relevant confounders.

### Causal Inference Techniques

When RCTs are infeasible (ethical, practical, or economic constraints):

**Instrumental Variables (IV)**: A variable correlated with the treatment but not directly affecting the outcome — only through the treatment. Used to estimate causal effects when treatment assignment isn't random. Example: distance to a hospital as an instrument for hospital usage.

**Difference-in-Differences (DiD)**: Compares change over time in a treated group vs. a control group. Assumes "parallel trends": both groups would have followed the same trajectory absent treatment. Common in policy evaluation (minimum wage effect on employment).

**Propensity Score Matching**: Match treated and control units by their propensity (probability of receiving treatment given observed covariates). Creates a quasi-experimental comparison by balancing covariate distributions.

**Natural experiments**: Exploit exogenous variation in treatment assignment that wasn't controlled by the researcher — e.g., a policy change that affects one region but not another, or a lottery that assigns treatment randomly.

## Counterfactual Evaluation for RecSys

The fundamental problem with offline recsys evaluation: logged interaction data reflects the _policy_ (the existing recommendation system) that generated it. We're evaluating how well new recommendations match data generated by a different policy.

### Inverse Propensity Scoring (IPS)

IPS estimates: "What reward would our new recommendation policy have gotten if deployed instead of the current policy?"

```
IPS_estimate = Σ [π_e(a|x) / π_0(a|x)] * r(x, a)
```

- `r(x, a)`: Logged reward (click/purchase) for showing item `a` in context `x`
- `π_0(a|x)`: Production policy's probability of recommending item `a` in context `x`
- `π_e(a|x)`: New (evaluation) policy's probability of recommending item `a` in context `x`
- Ratio: Importance weight — how much more/less often the new policy makes this recommendation

**Intuition**: If the new model would recommend iPhone 1.5x more often than the old model, upweight iPhone clicks in the logged data by 1.5x when estimating the new model's performance.

### IPS Variants

**Problem 1: Zero support**. If the production policy never recommended item A, its propensity is 0 and we can't compute the weight. Mitigation: exploration traffic (show random items on a small traffic slice to build a support baseline). Or ensure all eligible items have non-zero probability.

**Problem 2: High variance**. If the new policy makes very different recommendations, importance weights explode (e.g., weight of 100x for a single click). Mitigation:

- **Clipped IPS (CIPS)**: Cap importance weights at a maximum threshold (e.g., 10). Introduces bias but reduces variance.
- **Self-Normalized IPS (SNIPS)**: Divide IPS estimate by the sum of importance weights. No parameter tuning needed. Best empirical performance in benchmarks. Slightly more computation (requires weights for all observations, not just those with non-zero reward).

**Direct Method (DM)**: Train a reward model to impute missing interaction data. Works when IPS has insufficient support but biased toward the reward model's assumptions.

**Doubly Robust (DR)**: Combines IPS and DM. Consistent if either the propensity model or the reward model is correct. Best of both worlds in theory.

**Practical recommendation**: SNIPS is the best default. Requires logging recommendation probabilities (or impression counts) at serving time — build this into your serving infrastructure early.

## Offline vs. Online Metric Alignment

The holy grail: an offline metric that reliably predicts A/B test outcomes. In practice, the alignment is imperfect and task-dependent. Some principles:

- Temporal splits are closer to production than random splits for recsys.
- Metrics that measure exactly what the A/B test measures (CTR offline → CTR online) are more aligned than proxy metrics (NDCG offline → CTR online).
- Counterfactual evaluation (IPS/SNIPS) is more aligned than standard offline evaluation because it accounts for the interventional nature of recommendations.

If your offline metrics consistently diverge from your A/B results, consider: (1) switching to temporal splits, (2) implementing counterfactual evaluation, (3) auditing whether your offline metric is a good proxy for the online metric.

## Sources

- Aman.ai: [Concepts — A/B Testing](https://aman.ai/primers/ai/ABTest/)
- Aman.ai: [Concepts — Causal Inference](https://aman.ai/primers/ai/causalInference/)
- Eugene Yan: [Counterfactual Evaluation for Recommendation Systems](https://eugeneyan.com/writing/counterfactual-evaluation/)
