---
concept: RecSys Evaluation & Bias
tags: [evaluation, ndcg, position-bias, calibration, offline-online]
sources:
  - kb/hard/raw/aman-ai/recommendation-systems-eval-metrics-and-loss.md
  - kb/hard/raw/aman-ai/recommendation-systems-calibration.md
  - kb/hard/raw/eugene-yan/how-to-measure-and-mitigate-position-bias.md
last_compiled: 2026-04-05
related: [recommendation-systems, learning-to-rank, a-b-testing]
understanding: 3  # proven depth (demonstrated in dialogue/practice, or authored)
relevance: 3  # very relevant
knowledge_updated: 2026-09-07
---

# RecSys Evaluation & Bias

Evaluation is where recommendation systems live or die. Offline metrics measure model quality on historical data before deployment; online metrics measure real-world impact after deployment. Biases in both data and system design corrupt both. Calibration ensures that model scores mean what they claim to mean. This article covers the full evaluation stack and the major bias failure modes.

## Offline Evaluation

Offline evaluation uses historical interaction data to compare model versions before shipping anything to users. The workflow: hold out a test set (typically temporal — train on earlier data, test on later data), train the model, evaluate on the held-out set.

**For candidate generation (retrieval):**

- **Recall@K** — what fraction of the items a user actually engaged with appear in the top K candidates? If the ranker can only see what the retriever surfaced, recall is the ceiling on overall system quality.
- **Diversity** — average pairwise dissimilarity across recommended items. Catches retrieval models that return homogeneous clusters.
- **Novelty** — fraction of recommended items the user hasn't seen before.
- **Serendipity** — measures whether recommended items are both unexpected and positively surprising (difficult to compute offline; often approximated).

**For scoring and ranking:**

- **RMSE / MAE** — regression metrics for explicit rating prediction. Less common in modern systems that optimize engagement rather than rating.
- **Precision@K** — of the K items shown, how many did the user engage with?
- **Recall@K** — of all items the user would have engaged with, how many appear in the top K?
- **AP@N (Average Precision at N)** — averages precision over all recall cut-offs up to N. Accounts for rank position — relevant items appearing higher contribute more.
- **MAP@N (Mean Average Precision)** — averages AP@N across all users.
- **NDCG (Normalized Discounted Cumulative Gain)** — the most widely used ranking metric. Assigns graded relevance scores to items and applies a logarithmic discount based on rank position. Normalized against the ideal ordering (IDCG) to produce a [0, 1] score:

```
DCG = Σ(relevanceᵢ / log₂(i+1))
NDCG = DCG / IDCG
```

A score of 1.0 means the ranker produced the ideal ordering; lower scores indicate relevant items ranked too low.

- **MRR (Mean Reciprocal Rank)** — average of the reciprocal of the rank of the first relevant item across users. Useful when only one relevant item matters (e.g., PYMK, where you want the most relevant connection at position 1).

**Loss functions for training (not evaluation):** binary cross-entropy for classification objectives, margin loss for pairwise ranking, fairness loss to penalize differences in predicted scores across demographic groups, diversity loss to penalize clustering of predicted scores.

## Online Evaluation

Online metrics measure real user behavior after deployment, typically via A/B testing.

**A/B testing setup:** assign users to control (existing system) and treatment (new system) via a deterministic hash function. Run until sufficient statistical power. Common pitfalls: novelty effects (users explore treatment simply because it's new), carryover effects between user groups, and metric selection bias (optimizing for an easy-to-move metric instead of the real business objective).

**Common online metrics:**

- **CTR (Click-Through Rate)**: clicks / impressions. Simple but gameable — clickbait inflates CTR without improving user satisfaction.
- **Conversion Rate (CVR)**: conversions / clicks. Relevant for e-commerce and event registration systems.
- **Dwell time / session length**: time spent engaged with recommended content. Stronger signal for quality than clicks.
- **DAU/WAU/MAU**: platform-level active user metrics. The ultimate health signal, but slow to move and noisy.

## Position Bias

Position bias is the distortion caused by users engaging more with items at the top of a list regardless of their actual relevance. On Google Search, users click on position 1 roughly 10x more than position 10. In recommendation carousels, users scan left to right.

The problem is self-reinforcing: items shown at the top get more clicks, which makes them look more relevant, which keeps them at the top. Systems trained on biased logged data perpetuate the bias.

**Measuring position bias:**

- **Randomization (RandN/RandTopN)**: randomly shuffle top-ranked items for a subset of users. Any engagement difference can be attributed to position, not relevance. Most accurate method, but degrades user experience and is costly at scale.
- **Exploiting inherent randomness**: multiple rankers in production or frequent ranker updates create natural variation in item positions across contexts. Use this variation to estimate bias from logged data without active intervention.
- **FairPairs**: swap items at positions k and k+1 to introduce minimal randomness. Less disruptive than full randomization.
- **RandPair**: swap the first item with a randomly selected item at position k. More aggressive; can degrade experience for large k.
- **Expectation Maximization (EM)**: model the click probability as a product of examination probability (depends only on position) and relevance probability (depends only on item and context). Infer position bias from click logs without active experiments.

**Mitigating position bias:**

- **Inverse Position Weighting (IPW)**: upweight training examples at lower positions by `w_i = 1/position_bias(i)`. Items shown lower get more weight during training, so the model learns to consider them more fairly.
- **Positional features (Google Rule 36)**: include the item's position as a feature during training so the model learns how position affects engagement. At inference, set all positional features to a fixed neutral value (e.g., -1) to negate position's influence on predictions.
- **Propensity scoring (IPS)**: weight each user-item interaction by the inverse probability that the user was shown that item. Correct for both position and selection bias simultaneously.

## Bias Taxonomy

Beyond position bias, recommender systems suffer from a cluster of related failure modes:

**Popularity bias** — popular items receive disproportionate recommendations because they accumulate more interactions, which generates more training signal, which drives further recommendations. Mitigation: logit adjustment — subtract `log(P(item))` from the item's raw logit, penalizing items proportional to their historical interaction probability. Reduces over-recommendation of popular items without eliminating them.

**Selection bias / feedback loops** — the training data only reflects items that were shown. Items never exposed get no interactions, so the model never learns about them. IPS/IPW corrects by reweighting based on the propensity of each item being shown.

**Duration bias** — watch-time models favor long videos because they have higher cumulative watch time. Mitigation: quantile-based watch-time prediction. Bucket videos by duration, then bucket watch times within each duration bucket. Train the model to predict watch quantile rather than absolute watch time, removing the confound between content quality and video length.

**Clickbait bias** — optimizing for clicks rewards misleading thumbnails/titles. Mitigation: weighted logistic regression, where the weight for a positive example is `watch_time(u,v) / (click(u,v) + 1)`. This down-weights clicks not followed by sustained engagement.

**Single-interest bias** — models trained on skewed interaction data over-represent the user's dominant interest. Mitigation: Platt scaling calibration adjusts predicted probabilities to better reflect the full distribution of user interests.

## Calibration

Calibration is the property that a model predicting 0.7 engagement probability is correct 70% of the time. Poor calibration is common when using raw logits from deep learning models.

**Why it matters:** downstream reranking and multi-objective scoring (see [[hard/wiki/reranking|Reranking & Multi-Objective Optimization]]) blend scores from multiple models. If those scores are miscalibrated, the blending weights lose their intended meaning. A model with poor calibration also makes unreliable threshold decisions (e.g., "send this push if P(engagement) > 0.05").

**Platt Scaling**: fits a sigmoid `P(y=1|s) = 1/(1+exp(As+B))` to the raw model output. Two parameters, fast to fit. Assumes the calibration curve is sigmoid-shaped.

**Isotonic Regression**: non-parametric; fits a piecewise monotone function via the PAV algorithm. More flexible than Platt, but prone to overfitting on small calibration sets and computationally expensive on large ones.

**Bayesian Calibration (BBQ)**: bins scores into quantiles, applies a Dirichlet prior to estimate posterior probabilities per bin. Handles uncertainty in the calibration process and reduces overfitting through priors, at the cost of complexity and computational overhead.

**Measuring calibration quality:** the observed-to-expected ratio — actual positive rate divided by the sum of predicted probabilities for all test samples. A ratio of 1.0 is ideal. LinkedIn uses this metric to ensure their notification recommendation model isn't systematically over- or under-sending pushes.

## Offline vs Online Metric Alignment

The most dangerous situation is when offline metrics improve but online metrics do not. Common causes:

- The test set doesn't represent the true distribution of future requests (temporal leakage, covariate shift)
- The offline metric doesn't capture what users actually care about (NDCG scores improve but CTR and session length don't)
- Position bias in training data inflates offline metrics for models that learn to exploit the bias rather than improve relevance

Recommendation: always run online A/B tests before shipping, and maintain a held-out evaluation set that mirrors production conditions as closely as possible.

## Sources

- Aman.ai — [Recommendation Systems: Eval, Metrics and Loss](https://aman.ai/recsys/metricsHidden/)
- Aman.ai — [Recommendation Systems: Calibration](https://aman.ai/recsys/callibration/)
- Eugene Yan — [How to Measure and Mitigate Position Bias](https://eugeneyan.com/writing/position-bias/)
