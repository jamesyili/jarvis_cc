---
concept: RecSys Beyond Accuracy
tags: [diversity, novelty, serendipity, beyond-accuracy, long-tail]
sources:
  - kb/hard/raw/eugene-yan/serendipity-accuracys-unpopular-best-friend-in-recommenders.md
  - kb/hard/raw/eugene-yan/reinforcement-learning-for-recommendations-and-search.md
  - kb/hard/raw/eugene-yan/recsys-2022-keynote-is-the-juice-worth-the-squeeze.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/recommendation-systems|Recommendation Systems]]"
  - "[[hard/wiki/reranking|Reranking]]"
  - "[[hard/wiki/bandits-exploration-exploitation|Bandits & Exploration-Exploitation]]"
understanding: 3  # proven depth (demonstrated in dialogue/practice, or authored)
relevance: 3  # very relevant
knowledge_updated: 2026-09-07
---

# RecSys Beyond Accuracy

Accuracy — NDCG, MAP, AUC, recall@k — is not the only metric that matters in recommendation systems. A system that exclusively optimizes for short-term click relevance produces boring recommendations, disengages users over time, concentrates sales on a narrow set of popular items, and creates fragile business dependency. Beyond-accuracy metrics — diversity, novelty, serendipity, unexpectedness — capture qualities that determine long-term user satisfaction and platform health.

These metrics are systematically underused. Accuracy metrics are widely available in libraries; serendipity implementations are scarce. Accuracy has stronger correlation with short-term CTR; serendipity correlates with long-term retention. Offline accuracy is easier to improve. But the gap between offline accuracy and real-world user satisfaction is where beyond-accuracy metrics live.

## The Business Case

Imagine a music recommender that only recommends songs from an artist the user already loves. Offline accuracy would be high. In practice, users get bored quickly. Beyond boredom:

**Assortment health:** In e-commerce, poor recommendation diversity creates a power-law distribution where 5% of products drive 95% of sales and revenue. If those top sellers go out of stock, move to a competitor, or get banned, the platform's revenue concentration is catastrophic. Distributing recommendations more broadly across the long tail reduces this dependency and risk.

**Cold-start virtuous cycle:** Deliberately surfacing long-tail and cold-start products via exploration collects training signal on those items. More data on long-tail items improves future recommendations for them. Serendipitous recommendations generate data that accuracy-only systems never collect.

**Seller and creator ecosystem health:** On platforms with a seller or creator economy, concentrating attention on the top few starves the rest. This eventually degrades the ecosystem — fewer creators have incentives to produce, which reduces content diversity, which further concentrates attention. Exposure diversity keeps the ecosystem healthy.

The counterintuitive finding: introducing deliberate diversity/cold-start exposure can improve conversion in A/B tests even when offline metrics look bad. The offline-online gap is especially wide for serendipity.

## The Four Metrics

### Diversity

Diversity measures how narrow or wide the spectrum of recommended items is. A recommender surfacing only one artist type across all recommendations is low-diversity.

**Item-based diversity:** Measure variety in the recommendation set:
- How many distinct categories/genres are represented?
- How many distinct artists/authors/sellers?
- What is the distribution (kurtosis) of price across recommendations?
- What is the average pairwise distance between item embeddings? Higher average distance = more diverse set.

**User-based diversity:** For each recommended item, who has previously consumed it? If recommended items share a large proportion of common users, the items are likely similar. Cosine similarity between items based on user co-consumption:

$$\text{CosineSimilarity}(i, j) = \frac{\text{count(users who consumed both } i \text{ and } j)}{\sqrt{\text{count(users of } i)} \times \sqrt{\text{count(users of } j)}}$$

Low average pairwise similarity across the recommended set = high diversity.

### Novelty

Novelty measures how new or unusual the recommendations are relative to what users have been exposed to. Popular items are low-novelty by default — if an item trends on social media, your recommendation of it is not novel.

**Population-based novelty** (what others see):
$$\text{Novelty}(i) = -\log_2 \frac{\text{count(users recommended } i)}{\text{count(all users)}}$$

High novelty when few users receive the recommendation. Problem: this measures rarity of recommendation, not user-level novelty.

**Interaction-based novelty** (what others have done):
$$\text{Novelty}(i) = 1 - \frac{\text{count(users recommended } i)}{\text{count(users who have not interacted with } i)}$$

Better: reflects whether the item has been seen/consumed by the user's social context, not just whether others were recommended it.

### Unexpectedness (Surprise)

Unexpectedness measures how different a recommendation is from what the user is used to receiving. This is the user-specific component of novelty.

**Relative to previous recommendations:** Compare new recommendations against the user's prior recommendation history. Measures "how much surprise are we introducing?" — useful for tracking improvements to a serendipity feature.

**Relative to past interactions:** Compare recommendations against the user's historical consumption. Measures "how surprising given what the user has done?" — the better operationalization for user experience.

Point-wise mutual information (PMI) measures how often two items are consumed together vs. independently:

$$\text{PMI}(i, j) = -\log_2 \frac{p(i,j)}{p(i) \times p(j)} / \log_2 p(i,j)$$

Alternatively, cosine similarity between recommended items (I) and historical items (H):
$$\text{Unexpectedness}(I, H) = \frac{1}{|I|} \sum_{i \in I} \sum_{h \in H} \text{CosineSimilarity}(i, h)$$

Lower cosine similarity = higher unexpectedness.

### Serendipity

Serendipity combines unexpectedness with relevance. An unexpected recommendation that the user ignores is just noise. An unexpected recommendation that the user engages with is serendipitous.

$$\text{Serendipity}(i) = \text{Unexpectedness}(i) \times \text{Relevance}(i)$$

Where relevance(i) = 1 if the user interacted with item i, else 0.

Aggregate over all users and recommended items:
$$\text{Serendipity} = \frac{1}{|U|} \sum_{u \in U} \sum_{i \in I} \frac{\text{Serendipity}(i)}{|I|}$$

**Implementation challenge:** If you deliberately introduce long-tail cold-start products, offline relevance metrics will look bad — you don't have interaction data for those items. This doesn't mean the recommendations are bad; it means the offline metrics are misleading. The right validation is an A/B test. Don't let poor offline serendipity metrics dissuade you from testing in production.

## RL as a Beyond-Accuracy Mechanism

Reinforcement learning addresses beyond-accuracy goals directly — it can optimize for long-term rewards (user activeness, session length, return rate) rather than immediate click probability.

**Contextual bandits:** The entry point for exploration in production recsys. Balance exploration (trying new items to learn their value) and exploitation (serving items known to perform well). Contextual bandits personalize this balance using user and context features. Netflix used contextual bandits to personalize movie artwork — a system that continuously explores and learns the best image per user, rather than a batch system that trains periodically and doesn't learn during the gap.

Yahoo demonstrated contextual bandits for news recommendation, using user-article cross features (the outer product of 6-dim user and article projections = 36-dim vector) to enable transfer learning across articles.

**Deep Q-Networks (DQN):** Value-based RL that learns a Q-function mapping state-action pairs to long-term value. JD.com used DQN with separate state components for positive interactions (clicked/purchased) and negative interactions (skipped) — the model should recommend items similar to what the user clicked but different from what they skipped. Microsoft incorporated a long-term user activeness reward (via survival models) alongside click reward — though weighted at only 0.05, this is the right conceptual move.

**Policy gradient (REINFORCE):** Google's YouTube uses REINFORCE for recommendations, with separate behavioral policy estimation to enable off-policy correction. The model encodes user history via RNN, predicts action probabilities via softmax over millions of videos, and uses ANN for efficient serving. Boltzmann exploration balances exploring new videos against known preferences — random epsilon-greedy would produce inappropriate recommendations.

**Off-policy evaluation is the key challenge.** Historical data was collected under a different policy (whatever was in production at the time). Naive offline evaluation is biased — you're evaluating your new policy on data that was never collected under it. Inverse propensity scoring and counterfactual evaluation techniques address this, but carefully.

**Long-term vs. short-term reward tradeoff:** RL for recsys is motivated by exactly this tension. Click-optimizing systems sacrifice long-term engagement. Directly optimizing for user return rate, session diversity, or subscription continuation requires RL's ability to credit-assign across delayed rewards.

## Measurement Guidelines

| Goal | Metric | When to Use |
|---|---|---|
| How different are the recommended items? | Item-feature diversity | Want variety in content type, category, creator |
| How much cross-pollination between communities? | User-overlap diversity | Measuring community mixing in social contexts |
| Different from what other users see? | Population-based novelty | Personalization differentiation |
| Different from what the user's context has seen? | Interaction-based novelty | Avoiding already-saturated recommendations |
| Different from what the user usually sees? | Unexpectedness vs. prior recs | Tracking serendipity feature improvement |
| Different from what the user has consumed? | Unexpectedness vs. past interaction | Best proxy for user-perceived surprise |
| Unexpectedly good? | Serendipity | Full evaluation of serendipity quality |

## Practical Deployment Advice

**Combine accuracy and beyond-accuracy in a single objective.** Pure serendipity without relevance is random noise. Pure accuracy without diversity is a filter bubble. Production rerankers typically blend accuracy-based scores with diversity or novelty penalties — slot k+1 should be from a different category than slot k, for example.

**Use offline metrics to compare candidates, not as absolute benchmarks.** If serendipity offline metrics are all bad but one system is less bad than another, that's useful signal. Don't gate on absolute thresholds.

**Test in A/B.** The offline-online gap is particularly wide for beyond-accuracy metrics. The only trustworthy signal is a controlled experiment. A system that looks worse offline on relevance but better online on engagement or return rate should win.

**Track assortment health metrics as business KPIs.** Concentration of clicks/purchases in the top N% of items is a business risk metric. Product teams and leadership should care about this, not just the ML team.

## Sources

- Eugene Yan. *Serendipity: Accuracy's Unpopular Best Friend in Recommenders* — why serendipity matters, diversity/novelty/unexpectedness/serendipity metrics, formulas, implementation guidance
- Eugene Yan. *Reinforcement Learning for Recommendations and Search* — contextual bandits, DQN, REINFORCE, off-policy evaluation, long-term reward optimization
- Eugene Yan. *RecSys 2022 Keynote: Is the Juice Worth the Squeeze?* — online vs. batch recommenders, responsiveness, cold-start, context-awareness, Amazon Books case studies
