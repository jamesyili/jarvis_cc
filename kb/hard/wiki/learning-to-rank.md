---
concept: Learning to Rank
tags: [ranking, ltr, pointwise, pairwise, listwise, ml-system-design]
sources:
  - kb/hard/raw/aman-ai/chapter-7-event-recommendation-system.md
  - kb/hard/raw/aman-ai/chapter-10-personalized-news-feed.md
  - kb/hard/raw/aman-ai/chapter-11-people-you-may-know.md
  - kb/hard/raw/aman-ai/distilled-ad-click-prediction-recsys-design.md
  - kb/hard/raw/aman-ai/distilled-rental-search-ranking.md
  - kb/hard/raw/aman-ai/chapter-9-similar-listings-on-vacation-rental-platforms.md
  - kb/hard/raw/aman-ai/recommendation-systems.md
  - kb/hard/raw/aman-ai/recommendation-systems-popular-architectures.md
  - kb/hard/raw/aman-ai/recommendation-systems-calibration.md
last_compiled: 2026-04-05
related: [recommendation-systems, two-tower-retrieval, feature-engineering, embeddings-and-representation-learning]
---

# Learning to Rank

Learning to Rank (LTR) is the application of supervised ML to ordering problems: given a query and a candidate set, produce the ordering that maximizes some relevance objective. It sits at the heart of every production recommendation and search system — after [[hard/wiki/two-tower-retrieval|retrieval]] narrows millions of candidates to hundreds, LTR is what determines what the user actually sees.

## The Three Paradigms

### Pointwise
Each item is scored independently against the query. In practice this means a binary or regression model predicting P(click | user, item) or P(booking | user, listing). The final ranking is just a sort on predicted scores.

**Why it dominates production systems:** It's easy to frame as a standard classification problem, maps directly to existing data (impressions → labels), and scales cleanly. The news feed system (chapter 10) computes separate probabilities for click, like, share, comment, then blends them: `engagement_score = Σ weight_i × P(reaction_i)`. The event recommendation system (chapter 7) uses a single binary classifier for registration probability. The rental search ranking system frames booking likelihood as binary classification and sorts on that score.

**The tradeoff:** Pointwise treats each item in isolation, so the model has no awareness of how items compare. It can produce well-calibrated individual scores that generate a poor relative ordering.

### Pairwise
The model takes two items and predicts which is more relevant. Loss functions operate on pairs: **RankNet** uses cross-entropy on pairwise preferences; **LambdaRank** adds gradient weighting by the NDCG gain from swapping the pair; **LambdaMART** combines LambdaRank with gradient-boosted trees.

The key insight of LambdaRank: you don't need a well-defined loss to train a ranker — you only need gradients. By weighting gradients by |ΔNDCG|, the model focuses learning on swaps that matter most for ranking quality. This makes it more metric-aware than raw cross-entropy without requiring a differentiable NDCG formulation.

### Listwise
The model operates on the entire ranked list at once. SoftRank directly optimizes a smooth approximation to NDCG. ListNet models the probability of a permutation. AdaRank is a boosting approach that directly maximizes IR metrics.

Listwise is the most theoretically sound but hardest to implement and most expensive to train. Pairwise methods like LambdaMART routinely match or beat listwise approaches on benchmarks while being significantly more practical.

**Interview heuristic:** Default to pointwise in system design. Justify pairwise/listwise only when you can explain the gradient formulation or the training cost is worth it for your scale.

## Deep Ranking Model Architectures

The evolution of ranking models is a story of progressively better feature interaction modeling. The central challenge: given hundreds of sparse categorical features (user ID, item ID, categories, device type), how do you capture the interactions that drive clicks without manual feature engineering?

### Wide & Deep (Google, 2016)
The wide component is a linear model over manually crafted cross features — `AND(user_installed=Netflix, impressed_app=Hulu)` — capturing memorization of specific co-occurrence patterns. The deep component is an MLP over learned embeddings, capturing generalization. Both are trained jointly. Wide & Deep improved app acquisitions on Google Play by ~1% over deep-only — small percentage, massive revenue at scale. The insight: memorization and generalization are complementary, not competing.

### Deep & Cross Networks (DCN, 2017; DCN v2, 2020)
DCN replaces the manual wide component with a cross network that applies explicit feature crosses iteratively: each cross layer computes `x_0 × x_l^T × w + x_l`, preserving the original input and accumulating higher-order interactions. The cross network and DNN run in parallel; their outputs are concatenated for final prediction. DCN automates cross feature generation to bounded polynomial degree, removing the need for manual feature engineering. DCN v2 uses a full-rank matrix instead of a vector per cross layer and introduces a Mixture of Experts structure for scalability.

### DeepFM (2017)
Combines Factorization Machines for second-order feature interactions with an MLP for higher-order interactions, sharing the same embedding layer between both components. FM captures pairwise interactions efficiently; the deep component handles non-linear combinations. DeepFM requires no manual feature engineering and outperforms Wide & Deep on CTR benchmarks.

### DIN (Deep Interest Network)
Introduces an attention mechanism over a user's historical interactions to model interest diversity. Instead of summing all past interactions into a single vector, DIN weights historical items by their relevance to the target item. This captures the fact that users have diverse interests, and only a subset is relevant for any given candidate.

### DHEN (2022)
Introduces a hierarchy of interaction types — dot products, self-attention (AutoInt-style), convolution, linear processing, and DCN-style crossing — applied together rather than choosing one. DHEN is not incremental over DLRM; it replaces DLRM's single dot product with a comprehensive interaction hierarchy, achieving state-of-the-art CTR on Criteo benchmarks.

### Architecture Selection in Interviews
- Simple baseline: logistic regression or GBDT (fast to train, interpretable, no embedding infrastructure required)
- Standard production: Deep & Cross or DeepFM (automatic feature interactions, embedding-based)
- High-quality production: DCN v2 or DHEN (more expressive, but harder to justify without scale)
- When you need continual learning: neural networks over GBDT — GBDT requires full retraining; NNs support fine-tuning on new data

## Feature Engineering for Rankers

Features fall into four categories. What distinguishes good rankers from mediocre ones is usually feature quality, not model architecture.

**User features:** Demographics (age, gender, location), account age, historical engagement rates by category, contextual signals (device, time of day, session recency). Passive users are a special case — for news feeds, dwell time and skip signals capture engagement without explicit reactions.

**Item features:** Content embeddings (BERT for text, ResNet/CLIP for images), engagement statistics (total likes, share rate, impression-to-click ratio), recency/age. Items degrade differently: events expire; listings stay fresh longer; social posts decay within hours.

**Cross features (user × item):** Cosine similarity between user interest vector and item embedding, user × item category affinity, user × price bucket historical preference. These are the most predictive features and the hardest to engineer at scale. Wide & Deep formalized the value of explicit cross features; DCN automates their generation.

**Context features:** Location distance, time remaining to event, travel time, day-of-week match against user's historical attendance pattern. Location-based systems (event recommendation, rental search) rely heavily on distance features — raw lat/long is poorly behaved; log-distance-from-center or bucketized distance categories work better.

**Social features:** Number of friends registered for an event, friend-attended ratio, whether the host is a friend — these are among the most predictive signals for event and social content ranking (chapter 7). Mutual connections (PyMK chapter 11) are particularly strong for connection prediction: 92% of new friendships form via friends-of-friends.

## Multi-Objective Ranking

Real systems don't optimize a single signal. The news feed system (chapter 10) blends click, like, comment, share, hide, block, and dwell time with learned or hand-tuned weights. Key decisions:

- **Which signals to include:** Implicit (clicks, dwell time) have more data but weaker signal; explicit (likes, shares) are stronger but sparse. Blend both.
- **How to weight them:** Weights can be hand-tuned to business objectives (a hide should negatively outweigh a click) or learned via constrained optimization.
- **What you're implicitly optimizing:** Optimizing purely for engagement metrics can surface clickbait. Add quality signals (hide rate, block rate) as negative terms or constraints.
- **Multi-task learning:** Train separate heads for each reaction on a shared representation — reduces training cost, shares signal across sparse tasks, and prevents the model from over-indexing on frequent reactions at the expense of rarer but higher-value ones (e.g., shares vs. clicks).

## Position Bias and Debiasing

Users click items in higher positions at higher rates regardless of quality. Training on click data without correction creates a feedback loop: items ranked high get more clicks → model learns they're relevant → ranks them higher.

**Two-tower debiasing:** A separate "bias tower" learns position-related signals (position, device type, page context) while the main tower learns relevance. Outputs are combined multiplicatively or additively so the bias is factored out from the relevance score at serving time. Huawei's PAL model uses multiplicative combination; YouTube's Watch Next uses additive. Both show significant quality improvements.

**Inverse propensity weighting:** Re-weight training examples by 1/P(observed | position) to correct for the examination bias. Requires a propensity model to estimate P(examination).

**Intervention harvesting:** A/B test positions to collect unbiased click data. Expensive but ground truth.

## Evaluation Metrics

**Offline (ranking quality):**
- **NDCG@K** (Normalized Discounted Cumulative Gain): Measures gain of retrieved items discounted by position. Works for graded relevance. The standard metric for ranking quality across most system design contexts. Rental search (distilled-rental-search-ranking) uses DCG/NDCG explicitly.
- **MAP** (Mean Average Precision): Average precision across recall levels. Works for binary relevance — good fit for event recommendation where a user either registered or didn't.
- **MRR** (Mean Reciprocal Rank): Position of the first relevant item. Use when there's a single right answer (search with one correct result). Avoid for multi-relevant recommendation scenarios.
- **HR@K** (Hit Rate): Whether any relevant item appears in top K. Simple but useful for retrieval-stage evaluation.

**Why Precision@K and Recall@K are weak:** They ignore ranking order. NDCG, MAP, and MRR all account for position; Precision@K does not.

**Online:**
- CTR, conversion rate, session book rate (rentals), registration rate (events), accepted connection rate (PyMK)
- Revenue lift is the ultimate business metric but requires A/B tests and has high variance
- Engagement blends (total time spent, reaction rates) for feed systems where implicit signals matter

**Ad prediction special case:** Normalized Cross-Entropy (NCE) divides predictive log-loss by the cross-entropy of the background CTR, making the metric insensitive to CTR base rate. Useful when CTR varies by product surface.

## Production Considerations

**Latency:** Ranking happens after retrieval and must complete within 50-200ms total. Practical limits: feature computation (static features from feature store <10ms, dynamic features computed in real-time add latency), model inference (GBDT is faster than DNN; quantized DNNs are faster than full precision). Aggregator pattern: distribute candidate list to parallel ranking workers, collect and merge results.

**Calibration:** Predicted scores are used downstream for blending, thresholding, and business decisions — they need to be true probabilities, not just ordinal scores. Platt scaling (fits a sigmoid to raw scores) is the simplest approach and works well when the calibration curve is approximately sigmoidal. Isotonic regression (non-parametric, monotone) fits more complex curves but overfits with limited data. Bayesian calibration (bins scores, uses Dirichlet prior) handles uncertainty explicitly. For CTR models, calibration drift with distribution shift is a persistent operational problem — monitor calibration metrics (reliability diagrams, Expected Calibration Error) continuously.

**Continual learning:** User interests shift; event inventories turn over hourly. GBDT requires full retraining — expensive and slow. Neural networks support fine-tuning on new data incrementally. For highly dynamic systems (event recommendation, ad ranking), architecture choice directly constrains your retraining velocity.

**Class imbalance:** CTR in ads is ~1-2%; registration rates in events are similarly low. Strategies: downsample the negative class (keep training distribution manageable), use focal loss (down-weight easy negatives), or class-balanced loss. Never downsample the validation/test set — metrics must reflect true production distribution.

**Feature store:** Static features (user demographics, item metadata) are pre-computed and served with <10ms lookup from Redis/DynamoDB. Dynamic features (real-time interaction counts, live event capacity) are computed at request time from stream processors. Separating these is standard architecture: static store + streaming feature pipeline.

## Sources
- [[kb/hard/raw/aman-ai/chapter-7-event-recommendation-system|Chapter 7 – Event Recommendation System]]
- [[kb/hard/raw/aman-ai/chapter-10-personalized-news-feed|Chapter 10 – Personalized News Feed]]
- [[kb/hard/raw/aman-ai/chapter-11-people-you-may-know|Chapter 11 – People You May Know]]
- [[kb/hard/raw/aman-ai/distilled-ad-click-prediction-recsys-design|Distilled – Ad Click Prediction RecSys Design]]
- [[kb/hard/raw/aman-ai/distilled-rental-search-ranking|Distilled – Rental Search Ranking]]
- [[kb/hard/raw/aman-ai/chapter-9-similar-listings-on-vacation-rental-platforms|Chapter 9 – Similar Listings on Vacation Rental Platforms]]
- [[kb/hard/raw/aman-ai/recommendation-systems|Recommendation Systems (overview)]]
- [[kb/hard/raw/aman-ai/recommendation-systems-popular-architectures|Recommendation Systems – Popular Architectures]]
- [[kb/hard/raw/aman-ai/recommendation-systems-calibration|Recommendation Systems – Calibration]]
