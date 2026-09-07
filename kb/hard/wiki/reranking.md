---
concept: Reranking & Multi-Objective Optimization
tags: [reranking, multi-objective, diversity, fairness, moo]
sources:
  - kb/hard/raw/aman-ai/recommendation-systems-re-ranking.md
  - kb/hard/raw/aman-ai/recommendation-systems-multi-objective-optimization.md
  - kb/hard/raw/aman-ai/recommendation-systems-bias.md
last_compiled: 2026-04-05
related: [recommendation-systems, bandits-exploration-exploitation, learning-to-rank]
understanding: 3  # proven depth (demonstrated in dialogue/practice, or authored)
relevance: 3  # very relevant
knowledge_updated: 2026-09-07
---

# Reranking & Multi-Objective Optimization

Reranking is the final stage of a recommendation pipeline. After retrieval narrows millions of items to hundreds, and a ranker scores them on a primary objective (typically relevance or predicted engagement), reranking makes a second pass to apply constraints and secondary objectives that are difficult to express in the scoring model. The goal is a ranked list that is not just relevant but also diverse, fresh, fair, and aligned with business and platform health requirements.

## Why Reranking Exists

Scoring models are trained to maximize a single objective — watch time, CTR, engagement probability. Optimizing a single objective at scale produces pathological outcomes: the feed becomes monotonous, fresh content gets starved, popular items dominate, and underrepresented groups get worse recommendations. Reranking is where these trade-offs get explicitly managed.

Methods fall into three categories:

1. **Hard filters** — exclude items from the pool entirely (e.g., a separate clickbait classifier that removes low-quality videos before the list is assembled).
2. **Score adjustments** — modify the ranking score directly (e.g., multiplying by a freshness decay factor, subtracting a popularity penalty).
3. **Reordering** — apply a global algorithm over the entire list to optimize a composite objective (e.g., diversity-aware reranking via determinantal point processes or greedy slot filling by category).

## Key Reranking Signals

**Freshness / Novelty** — surface newer content ahead of older content with similar relevance scores. Bayesian Personalized Ranking (BPR) and time-decay functions are common mechanisms. Critical for news feeds and social platforms where stale content degrades experience.

**Diversity** — prevent the list from being a cluster of near-identical items. Concrete strategies: train multiple candidate generators on different sources (genre, topic, creator type), train multiple rankers with different objective functions, and apply genre/metadata-aware slot filling in the reranker. YouTube's risk of showing only owl videos if the ranker is pure nearest-neighbor in embedding space illustrates the failure mode.

**Popularity / Trending** — a popularity boost is legitimate when it de-risks recommendations (validated content) or serves cold-start users. The risk is feedback loops: popular items accumulate impressions, get more signal, rank higher. Common mitigations include normalizing popularity scores over time windows and penalizing items with over-representation across the user base.

**Seasonality** — time-based features (holiday flags, day of week, time of day) let the reranker surface contextually appropriate content. A user checking their phone at 7am gets different content than the same user on a Saturday afternoon, even with identical long-term preferences.

**Fairness / Demographic equity** — reranking can enforce equitable representation across demographic groups or item categories. Techniques include developing separate calibration models for underserved groups, monitoring metrics (accuracy, absolute error) across demographics, and constraining the fraction of recommendations from any single category.

## Multi-Objective Optimization (MOO)

MOO addresses the structural problem: there is no single "optimal" ranking when objectives conflict. Instead, MOO identifies a **Pareto front** — the set of solutions where improving one objective requires sacrificing another. Practitioners then select a point on the front based on business priorities.

**LinkedIn's Feed** uses a linear combination of passive consumption probability and active engagement probability:

```
score = α·P(passive consumption) + (1-α)·P(active consumption)
```

The weight α is tuned automatically via Bayesian optimization rather than hand-tuned, scanning for configurations that satisfy guardrail metric thresholds while maximizing primary metrics.

**LinkedIn's Notifications** uses a more general form, combining separate models for CTR and sessions:

```
M_x = M₁ + x₁·M₂ + x₂·M₃ + ... + x_{n-1}·M_n
```

Different values of the combination vector x generate different points on the Pareto front. Online A/B testing determines which point satisfies the guardrail constraints while maximizing the primary objective.

### MOO vs Multi-Armed Bandits

These are different tools for different problems. MOO operates in a mostly static setting: given a pool of candidates and fixed objectives, find the optimal trade-off surface. It does not learn dynamically from outcomes.

MABs (see [[hard/wiki/bandits-exploration-exploitation|Bandits & Exploration-Exploitation]]) operate in sequential decision-making settings: the agent selects an action, observes a reward, and updates its policy. MABs minimize regret over time and adapt to changing user preferences. Contextual bandits extend this by conditioning on observable context before each action.

In practice, MOO and MABs are complementary. MOO designs the scoring function and identifies trade-off weights; bandits tune those weights over time as the distribution of user behavior shifts.

## Score Calibration in Reranking

Raw model outputs are often poorly calibrated — a model predicting 0.7 click probability does not mean a 70% chance of a click. Calibration matters because reranking uses scores to compare items across different models trained with different objectives.

Three methods:

- **Platt Scaling** — fits a logistic regression to the raw model output: `P(y=1|x) = 1/(1+exp(A·f(x)+B))`. Simple, works well for SVMs and similar classifiers. Assumes a sigmoid shape.
- **Isotonic Regression** — non-parametric; fits a piecewise monotone function via the pool-adjacent-violators (PAV) algorithm. More flexible but prone to overfitting with small calibration sets.
- **Bayesian Calibration** — bins scores into quantiles and applies a Dirichlet prior. Handles uncertainty better, reduces overfitting, but requires prior specification and is computationally expensive.

Platt scaling also addresses **single-interest bias** — the tendency for a model trained on skewed behavior data to concentrate predictions on the user's most frequent interest, underrepresenting their other preferences. The KL divergence between the predicted probability distribution and the true interest distribution measures calibration quality.

## Practical Design Considerations

**When to add reranking:** Add a reranking pass whenever you observe that your ranking model's top-k output is monotone in any non-engagement dimension: too many items from the same category, no fresh content, no long-tail exposure.

**What not to do:** Using reranking as a patch for a broken ranking model. If diversity is consistently collapsing, the root cause is usually in the candidate generator (e.g., a single-tower retrieval model with no diversity pressure) or the ranker's training data distribution. Fix upstream, then use reranking for the residual.

**Interaction with position bias:** Reranking changes item positions, and position bias (see [[hard/wiki/recsys-evaluation|RecSys Evaluation & Bias]]) means users engage more with top positions regardless of relevance. A reranker that moves items around to increase diversity will also shift their engagement probability, which then feeds back into training data. Jointly modeling position bias and reranking objectives is an active area.

## Sources

- Aman.ai — [Recommendation Systems: Re-ranking](https://aman.ai/recsys/re-ranking/)
- Aman.ai — [Recommendation Systems: Multi-Objective Optimization](https://aman.ai/recsys/multi-objective-optimization/)
- Aman.ai — [Recommendation Systems: Bias](https://aman.ai/recsys/bias/)
