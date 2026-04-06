---
concept: Recommendation Systems
tags: [recsys, ml-system-design, retrieval, ranking, personalization]
sources:
  - kb/hard/raw/eugene-yan/system-design-for-recommendations-and-search.md
  - kb/hard/raw/eugene-yan/real-time-machine-learning-for-recommendations.md
  - kb/hard/raw/eugene-yan/patterns-for-personalization-in-recommendations-and-search.md
  - kb/hard/raw/eugene-yan/how-to-measure-and-mitigate-position-bias.md
  - kb/hard/raw/aman-ai/recommendation-systems-introduction.md
  - kb/hard/raw/aman-ai/recommendation-systems.md
  - kb/hard/raw/aman-ai/recommendation-systems-system-design.md
  - kb/hard/raw/aman-ai/chapter-6-video-recommendation-system.md
  - kb/hard/raw/aman-ai/chapter-10-personalized-news-feed.md
  - kb/hard/raw/aman-ai/chapter-7-event-recommendation-system.md
  - kb/hard/raw/aman-ai/chapter-11-people-you-may-know.md
  - kb/hard/raw/aman-ai/ml-system-design-questions.md
last_compiled: 2026-04-05
related: [two-tower-retrieval, learning-to-rank, embeddings-and-representation-learning, bandits-exploration-exploitation, feature-engineering]
---

# Recommendation Systems

Recommendation systems (RecSys) are the core ML infrastructure of most consumer internet products — YouTube, Netflix, Pinterest, LinkedIn, Amazon. They solve a single underlying problem: given a user (or query) and a very large corpus of items, surface the small subset the user is most likely to value. The architecture challenge is doing this accurately, in under 200ms, at billions-of-users scale.

---

## The Funnel Architecture

The defining structural pattern is the **multi-stage funnel**: progressively narrowing a massive item corpus down to the final ranked list, trading off precision for speed at each stage.

### 2-Stage Model (Eugene Yan's 2×2)

Eugene Yan's canonical framing organizes the system along two axes:
- **Environment**: offline vs. online
- **Process**: candidate retrieval vs. ranking

The **offline environment** runs batch jobs: training models, computing item embeddings, building ANN (approximate nearest neighbor) indices, populating feature stores. The **online environment** handles live requests: it uses the artifacts produced offline to execute retrieval then ranking in sequence.

### 4-Stage Model (NVIDIA's 2×4)

Extends the 2×2 with explicit filtering and ordering steps:

1. **Retrieval** — Generate a pool of O(thousands) candidates from O(millions/billions) items using scalable methods (matrix factorization, [[hard/wiki/two-tower-retrieval|two-tower models]], ANN). Prioritize speed over precision; false positives are acceptable here.
2. **Filtering** — Apply deterministic business rules: remove out-of-stock items, region-restricted content, already-seen items, items that violate safety policies. This stage keeps business logic out of the ML models.
3. **Scoring / Ranking** — Score the filtered candidates using a heavyweight model with rich features (user context, item metadata, cross features). Feasible here because the candidate set is small. Prioritize precision.
4. **Ordering / Re-ranking** — Apply post-hoc adjustments for diversity, freshness, fairness, business objectives, or safety signals. A separate lightweight model or rule set.

This pattern appears across YouTube (two-stage DNN), Instagram's Explore, Netflix, and LinkedIn's PYMK systems.

---

## Retrieval: Candidate Generation

The retrieval stage must handle billions of items in milliseconds. Three main approaches:

### Matrix Factorization
Decomposes the user-item interaction matrix into two lower-dimensional embedding matrices — one for users, one for items. At inference, relevance is the dot product between a user embedding and an item embedding. Pre-computing item embeddings offline makes serving fast.

**Loss function nuance**: Optimizing only on observed (positive) pairs leads to poor embeddings because the model is never penalized for false positives on unobserved pairs. The standard fix is a **weighted combination of observed and unobserved pairs** — a hyperparameter `w` balances the two. **WALS** (Weighted Alternating Least Squares) is the preferred optimizer because it converges faster and is parallelizable.

Limitations: only uses interaction history (no side features), struggles with new users/items (cold start).

### Two-Tower Neural Networks
Two separate encoder networks — a user tower and an item tower — map their respective inputs into a shared embedding space. Relevance is the distance between embeddings. Unlike matrix factorization, two-tower models accept arbitrary side features (user age, language, item metadata), enabling:
- Better handling of new users (use demographic features instead of interaction history)
- Richer personalization

At serving time, item embeddings are pre-computed offline and stored in an ANN index. The user embedding is computed at query time (slight latency cost), then ANN lookup retrieves the top-K nearest items. Used for both content-based and collaborative filtering depending on what the towers encode.

**See**: [[hard/wiki/two-tower-retrieval|Two-Tower Retrieval]]

### Multiple Candidate Generators
In practice, running multiple parallel candidate generators improves recall. YouTube, for example, combines CF-based retrieval (captures collaborative signals) with content-based retrieval (captures item features), trending/popularity generators, and context-specific generators (location, time of day). Each generator contributes a different slice of relevant items, reducing the chance of systematic misses.

---

## Ranking: Scoring and Learning to Rank

Once the candidate set is O(hundreds–thousands), a heavier model can afford to use more features and make finer-grained relevance predictions.

### Pointwise, Pairwise, Listwise LTR

| Approach | What it predicts | Common algorithms |
|---|---|---|
| **Pointwise** | Relevance score for each item independently | Logistic regression, DNN, GBDT |
| **Pairwise** | Which of two items is more relevant | RankNet, LambdaRank, LambdaMART |
| **Listwise** | Optimal ordering of the full list | SoftRank, ListNet, AdaRank |

Pairwise and listwise methods generally produce better rankings but are harder to implement. Pointwise is the most common starting point in production — frame it as binary classification (will the user engage?) and sort by predicted probability.

### Multi-Task Learning for Ranking
A single user–item interaction produces multiple signals: click, like, comment, share, watch time, skip. Training separate models for each is compute-intensive and data-hungry for sparse signals. **Multi-task DNNs** share a common representation across tasks with task-specific output heads, improving sample efficiency and enabling the model to learn from implicit signals (dwell time, scroll depth) alongside explicit ones.

For the news feed case (Aman AI chapter 10), engagement score is a weighted sum of predicted probabilities across reaction types, with weights assigned by business logic:
```
engagement_score = w_click * P(click) + w_like * P(like) + w_comment * P(comment) + ...
```

This lets the system optimize for the business's definition of engagement, not just CTR.

### Deep Learning Architectures
Beyond simple DNNs, common production architectures include:
- **Wide & Deep**: Memorization (wide linear component) + generalization (deep component)
- **DCN v2 / DeepFM**: Explicit feature interaction modeling via cross networks or factorization machines
- **DLRM**: Facebook's architecture for recommendation with large embedding tables
- **Transformers (PinnerFormer, ItemSage)**: Sequential modeling of user history

---

## Feature Engineering

Features divide into three buckets:

**Item features**: ID (as embedding), duration/price, language, category/tags (embedding via CBOW or BERT), content embeddings from pre-trained vision/language models.

**User features**: Demographics (age, gender, location — categorical, use embeddings), contextual signals (time of day, device, day of week), historical interaction sequences (liked/watched/clicked items — average embeddings of the sequences).

**User–item affinity features**: Click/like/share rates per item category, engagement rates with the specific author/creator, mutual connections (for social graphs), recency-weighted signals. Per Aman AI's news feed chapter, affinity features (connection strength between user and post author) are among the strongest predictors of engagement on social platforms.

**Key practical considerations**:
- Use embedding layers for high-cardinality categoricals rather than one-hot encoding
- Average sequence embeddings to create fixed-size representations of variable-length histories
- Bucketize continuous variables (age of post, distance, price) and apply one-hot encoding
- For social graphs, extract structural features: mutual connections, FOF count, time-discounted connection strength

---

## Production Considerations

### Cold Start
**New users**: No interaction history. Mitigation strategies:
- Two-tower models can rely on demographic features (age, location, language) even with zero interactions
- Prompt for explicit onboarding preferences
- Fall back to popularity-based or trending recommendations

**New items**: No engagement data. Mitigation:
- Content-based retrieval uses item features immediately
- Heuristics: show to a random sample, collect enough interactions to bootstrap collaborative signals
- Event recommendation systems face a *constant* cold start because each event is inherently new; feature-heavy models with rich event attributes are the primary mitigation

### Latency
- Offline: pre-compute item embeddings, build ANN indices, populate feature stores
- Online: compute user embedding at request time → ANN lookup → scoring on small candidate set
- Target: <200ms end-to-end for typical consumer products
- Batch-then-fetch: For PYMK-style features, pre-compute recommendations for all active users in batch and serve from a database, refreshed periodically

### Real-Time vs. Batch Features
The funnel requires a feature store architecture with two tiers:
- **Batch/static features**: User demographics, pre-computed item embeddings, historical aggregates — updated on a schedule
- **Real-time features**: Recent interactions (last 5 clicks), current context (session, device), in-flight signals — require a streaming pipeline feeding a low-latency store

Real-time recency signals matter because user intent changes within a session. A user searching for pizza recommendations wants pizza content *now*, not based on their 30-day history. China's recommendation systems (Alibaba, ByteDance) have led on real-time feature adoption; US companies have been catching up.

### Position Bias
Training data comes from impressions, but users are more likely to interact with items shown higher in the list — not because those items are inherently better, but because of their position. If you train a ranking model naively on click data, you're training it to replicate position effects, not true relevance.

**Mitigation strategies**:
- **Inverse propensity weighting**: Downweight training examples from high positions
- **Propensity-aware models**: Add a position feature during training, remove it at inference
- **Randomization**: Periodically inject random orderings to generate unbiased training signal
- **Two-tower with position tower**: Treat position as a separate input that the model learns to debias

**See**: [[hard/wiki/bandits-exploration-exploitation|Bandits and Exploration–Exploitation]]

### Diversity, Freshness, and Filter Bubbles
Pure relevance ranking creates filter bubbles — users only see what they already like, reducing discovery. Re-ranking addresses this:
- Diversity: penalize similarity between recommended items (e.g., maximal marginal relevance)
- Freshness: boost newer items to prevent stale content dominating
- Novelty: de-rank items the user has already seen or similar items
- Multiple candidate generators inherently increase diversity by sourcing from different signal spaces

---

## Evaluation

### Offline Metrics
| Metric | Use case |
|---|---|
| **Precision@K** | What fraction of the top-K recommendations were relevant |
| **Recall@K** | What fraction of all relevant items appeared in the top-K |
| **MAP (Mean Average Precision)** | Ranking quality when relevance is binary |
| **NDCG** | Ranking quality when relevance is graded/continuous |
| **MRR (Mean Reciprocal Rank)** | When only one relevant item matters (e.g., first result) |
| **Diversity** | Average pairwise similarity within recommendation lists |
| **AUC-ROC** | Binary classification quality for click/conversion prediction |

For event recommendation (binary register/not register), MAP is preferred over NDCG. For video recommendation with graded watch-time relevance, NDCG is a better fit.

**Offline–online mismatch** is a persistent problem: models that look good offline (high MAP) may not improve business metrics in A/B tests. Common culprits: position bias in training data, feedback loops, or proxy metric misalignment with true business objectives.

### Online Metrics
| Metric | What it captures |
|---|---|
| **CTR** (click-through rate) | Engagement breadth; susceptible to clickbait |
| **Conversion rate** | Deeper engagement (purchase, registration, watch-to-completion) |
| **Total watch time / time spent** | Value delivered to passive users |
| **Explicit reaction rates** (like, share, comment) | User satisfaction quality signal |
| **Connection request acceptance rate** | For social graph recommendations |
| **Revenue lift** | Ultimate business objective |

The canonical video recommendation objective is maximizing **relevant videos** rather than maximizing clicks or completions — because clicks incentivize clickbait and completions favor short videos. Defining relevance via a combination of explicit (like, >50% watch) and implicit (click, watch time) signals gives more control.

### Long-Term Metrics
Short-term CTR can be gamed. Healthy RecSys track longer-horizon metrics: user retention over 30/90 days, satisfaction surveys, diversity of content consumed. These require holdout-based experimentation or observational causal inference, not just standard A/B tests.

---

## Model Selection Tradeoffs

| Model | Strengths | Weaknesses |
|---|---|---|
| **Matrix Factorization** | Fast training, fast inference (pre-computed embeddings) | No side features, cold start, limited expressiveness |
| **Two-Tower DNN** | Side features, handles cold start, flexible | Slower inference (user embedding at runtime), costlier training |
| **GBDT / XGBoost** | Fast to implement, works well on structured features, interpretable | No continual learning, poor on unstructured data |
| **Multi-Task DNN** | Efficient use of sparse signals, learns shared representations | Complex to train, architecture choices require experimentation |
| **GNN (for social graphs)** | Captures structural neighborhood signals, edge prediction | Computationally intensive, requires graph infrastructure |

The typical production path: start with matrix factorization or GBDT as a fast baseline, then iterate toward two-tower for retrieval and DNN/multi-task for ranking.

---

## Industry Case Studies

**YouTube** (DNN for Recommendations, 2016): Two-stage architecture — CF-based two-tower for candidate generation, content-based DNN for ranking. Incorporates watch history as a sequence of video embeddings. One of the foundational papers in production RecSys.

**Instagram Explore**: Multi-stage design — account-level interest modeling for retrieval, then two ranking passes with progressively heavier models.

**LinkedIn PYMK**: Uses GNNs for edge prediction on the social graph. Pre-computes recommendations in batch for all active users via FOF-filtered candidate generation, serving from a database. 92% of new connections form via friends-of-friends (FOF), justifying using the 2-hop neighborhood to constrain the candidate set.

**Facebook News Feed**: Pointwise LTR with multi-task learning across reaction types. Affinity features (user–author connection strength) are among the strongest signals. Passive user engagement (dwell time, scroll speed) requires dedicated tasks beyond click/like prediction.

**Pinterest (Homefeed / Candidate Generation)**: Two-tower retrieval (PinnerFormer for sequential user modeling, ItemSage for item representations), multi-stage ranking with business-rule re-ranking for diversity and freshness. Candidates come from multiple generators: interest-based, board-based, trending, social.

---

## Sources

- [[kb/hard/raw/eugene-yan/system-design-for-recommendations-and-search.md|Eugene Yan — System Design for Recommendations and Search]]
- [[kb/hard/raw/eugene-yan/real-time-machine-learning-for-recommendations.md|Eugene Yan — Real-time ML for Recommendations]]
- [[kb/hard/raw/eugene-yan/patterns-for-personalization-in-recommendations-and-search.md|Eugene Yan — Patterns for Personalization]]
- [[kb/hard/raw/eugene-yan/how-to-measure-and-mitigate-position-bias.md|Eugene Yan — How to Measure and Mitigate Position Bias]]
- [[kb/hard/raw/aman-ai/recommendation-systems-introduction.md|Aman AI — Recommendation Systems Introduction]]
- [[kb/hard/raw/aman-ai/recommendation-systems.md|Aman AI — Recommendation Systems]]
- [[kb/hard/raw/aman-ai/recommendation-systems-system-design.md|Aman AI — Recommendation Systems System Design]]
- [[kb/hard/raw/aman-ai/chapter-6-video-recommendation-system.md|Aman AI — Chapter 6: Video Recommendation System]]
- [[kb/hard/raw/aman-ai/chapter-10-personalized-news-feed.md|Aman AI — Chapter 10: Personalized News Feed]]
- [[kb/hard/raw/aman-ai/chapter-7-event-recommendation-system.md|Aman AI — Chapter 7: Event Recommendation System]]
- [[kb/hard/raw/aman-ai/chapter-11-people-you-may-know.md|Aman AI — Chapter 11: People You May Know]]
- [[kb/hard/raw/aman-ai/ml-system-design-questions.md|Aman AI — ML System Design Questions]]
