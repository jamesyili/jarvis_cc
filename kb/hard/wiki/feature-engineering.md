---
concept: Feature Engineering for ML Systems
tags: [feature-engineering, features, data-preprocessing, ml-pipeline, normalization, recsys, ranking]
sources:
  - kb/hard/raw/aman-ai/chapter-1-introduction-and-overview.md
  - kb/hard/raw/aman-ai/distilled-ad-click-prediction-recsys-design.md
  - kb/hard/raw/aman-ai/distilled-rental-search-ranking.md
  - kb/hard/raw/aman-ai/chapter-7-event-recommendation-system.md
  - kb/hard/raw/aman-ai/chapter-10-personalized-news-feed.md
  - kb/hard/raw/aman-ai/primers-standardization-vs-normalization.md
  - kb/hard/raw/aman-ai/primers-splitting-datasets.md
  - kb/hard/raw/aman-ai/recommendation-systems.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/recommendation-systems|Recommendation Systems]]"
  - "[[hard/wiki/learning-to-rank|Learning to Rank]]"
  - "[[hard/wiki/two-tower-retrieval|Two-Tower Retrieval]]"
  - "[[hard/wiki/embeddings-and-representation-learning|Embeddings and Representation Learning]]"
---

# Feature Engineering for ML Systems

Feature engineering is the process of selecting raw signals, transforming them into model-ready representations, and structuring the pipeline so those representations are reproducible and consistent between training and serving. It is arguably the highest-leverage step in applied ML — model choices matter, but the quality and expressiveness of features usually determine the ceiling.

## Feature Taxonomy

Production ML systems typically group features into four buckets:

- **User features** — demographics (age, gender, country, language, time zone), session context (device, time of day, current location), and behavioral history (click rates, watch time, past bookings, social graph).
- **Item features** — content attributes (category, price, description, tags), item-level engagement signals (total impressions, conversion rate, number of registered users), and item age or recency.
- **Context features** — request-level signals that are neither user nor item: geolocation, remaining time until an event, query text in search, estimated travel time to a venue.
- **Cross / interaction features** — derived from the relationship between user and item: "user's average walk score of past events" minus "this event's walk score" (similarity delta), the like/comment/share rate a user has with a specific author, the ratio of registered friends to total friends for a given event. These affinity and similarity features are consistently among the most predictive.

A useful design principle: for each raw attribute, ask (a) what does the raw value mean? (b) what transformation makes it model-learnable? (c) can you create a *similarity* version that encodes how this item compares to the user's history? The similarity deltas (distance similarity, price similarity, registered-user similarity) appear across ad click, rental search, event recommendation, and news feed systems because they compress a meaningful personalization signal into a single number.

## Numerical Features

Raw numerical values rarely go straight into a model. Common transformations:

- **Normalization (min-max scaling)** — rescales to [0, 1]: `z = (x − min) / (max − min)`. Preserves the shape of the distribution but squashes outliers; sensitive to extreme values. Good fit for bounded features like scores or rates.
- **Standardization (z-score)** — centers to mean 0, std 1: `z = (x − μ) / σ`. Preferred when outliers exist or when the algorithm depends on distance/gradient (neural networks, SVMs, KNN, logistic regression). More robust than min-max in practice.
- **Log scaling** — `z = log(x)`. Reduces right skew (e.g., raw impression counts, salaries, population density). Helps gradient descent converge faster on heavy-tailed distributions.
- **Discretization / bucketization** — converts continuous values into categorical buckets, then one-hot encodes them. Used heavily in recsys: post age (< 1h, 1–5h, 5–24h, …), event price (free, $1–99, $100–499, …), distance (< 1 mile, 1–5 miles, …), walk score (five tiers). Bucketization lets the model learn step-function behavior without assuming linearity across a wide range.

**When to use what:** Distance-based and gradient-based algorithms (KNN, SVM, neural nets, logistic regression) require feature scaling; tree-based models (GBDT, random forests, decision trees) do not — they split on thresholds and are scale-invariant.

## Categorical Encoding

- **Integer encoding** — assign an ordinal integer to each category. Only valid when there is a genuine ordering (e.g., satisfaction: bad=1, neutral=2, good=3). Misleads models when no ordering exists.
- **One-hot encoding** — creates a binary feature per unique value. Best for low-cardinality features (gender, country bucket, day of week). Produces vectors that are too large when cardinality is high (> a few hundred unique values).
- **Feature hashing (hashing trick)** — maps high-cardinality or open-vocabulary features (hashtags, user IDs in ad logs) to a fixed-size vector using a hash function. Handles unseen values at serving time at the cost of hash collisions.
- **Embedding learning** — maps each category to a dense *n*-dimensional vector learned during training. Required when cardinality is very large (item IDs, user IDs, zip codes). See [[hard/wiki/embeddings-and-representation-learning|Embeddings and Representation Learning]].

## Temporal Features

Time is almost always predictive in production systems. Key patterns:

- **Recency / item age**: post age, time since last booking, days since a listing was created. Typically bucketized then one-hot encoded. Users engage more with fresh content.
- **Remaining time**: for ephemeral items (events), time until the item expires is often more predictive than item age. Bucketize and encode: < 1h, 1–2h, 2–4h, ..., > 7 days.
- **Periodicity**: user preferences vary by day of week and hour of day. Build a per-user profile: a 7-element vector counting historical event attendance per weekday (normalized to rates). The same pattern applies per-hour for intra-day periodicity.
- **Similarity deltas on time**: for any temporal feature, compute (this item's value) − (user's historical average). These "remaining time similarity" features capture personal tolerance for lead time.

## Social and Cross Features

Social signals drive strong personalization in two-sided platforms:

- Number of friends attending (or who registered for) an event
- Ratio of registered friends to total friends
- Whether the event host is a friend (binary)
- User-author affinity: like rate, comment rate, share rate, length of friendship in days, close-friend/family flag
- Number of people who invited the user to this specific event

These are generally sparse but high-precision signals — a high like-rate with an author is a strong predictor of future engagement. They are among the most important features in news feed ranking systems.

## Handling Missing Values

Two strategies:

- **Deletion** — row deletion (drop data points with many missing values) or column deletion (drop features with too many missing values). Reduces training data; use with care.
- **Imputation** — fill with default, mean, median, or mode. Can introduce noise; the right fill value is domain-specific. No technique is perfect — both strategies have trade-offs.

## Geolocation Features

Raw lat/lng are difficult to model — the feature distribution is unsmooth. Alternatives:

- Log-transform of distance from a reference point (e.g., map center)
- Encode location as a cell in a 2D grid (then learn an embedding over cells)
- Use external APIs (Google Maps, OpenStreetMap) to derive derived signals: walk score, transit score, bike score, estimated travel time — then bucketize
- Binary features: same city? same country?

## Encoding Unstructured Content

Text, images, and video are unstructured. Standard approaches:

- **Text**: TF-IDF or word2vec for short phrases (hashtags, keywords); BERT or similar context-aware language model for longer descriptions; tokenization algorithms (Viterbi) to split compound hashtag strings
- **Images/video**: pre-trained CNNs (ResNet) or multimodal models (CLIP) to produce embedding vectors
- Once embedded, treat as dense numerical inputs to the model

For hashtags specifically: use feature hashing for the vocabulary lookup (handles unseen tags at inference), then TF-IDF or word2vec for the vectorization — transformer-based models are overkill for single-word hashtags.

## Train / Validation / Test Splitting

**For standard ML**: stratified random split (80/10/10 is common). Use a fixed random seed for reproducibility. Shuffle before splitting to avoid label skew from ordering effects. Dev and test sets must come from the same distribution.

**For recsys and ranking (critical)**: split by time, not randomly. Training data = records before date T; validation data = records in [T, T+delta]; test data = records after T+delta. This mimics production: you predict future events based on past behavior. Random splitting causes data leakage — future engagement signals contaminate training.

In ad click prediction and rental search ranking, this temporal split is a hard requirement. Using the next day after training cutoff as the validation window is a common pattern. Experiment with multiple time windows to find the right balance between training volume and model freshness.

## Feature Stores and Real-Time vs. Batch Features

In production, features fall into two categories:

- **Batch / static features** — precomputed offline and stored in a feature store (MySQL Cluster, Redis, DynamoDB). Examples: user demographics, item metadata, precomputed embeddings, historical interaction rates. Accessed at inference with < 10ms latency SLA.
- **Online / dynamic features** — computed in real time from a stream (Kafka) at request time. Examples: current location, real-time bid price, number of registered users in the last 5 minutes. A stream data prep pipeline processes these and writes to key-value storage for low-latency downstream access.

The feature store is a critical infrastructure component: it guarantees training-serving consistency — both the offline training pipeline and the online ranking service read features from the same store, preventing training-serving skew.

## Class Imbalance

Imbalanced label distributions are the norm in production recsys:

- CTR in ad systems is typically < 1–2%
- Bookings per search session are much rarer than non-bookings
- Event registrations are much rarer than event impressions

Mitigation:
- **Downsample the majority class** — keep all positives, randomly subsample negatives. Leave validation and test sets untouched to preserve accurate performance estimates.
- **Focal loss or class-balanced loss** — upweight minority-class errors in the loss function, forcing the model to learn rare classes more aggressively.

## Domain-Specific Patterns

**Ad CTR prediction**: Features include user profile, ad metadata, context. Negative downsampling is essential. Normalized Cross Entropy (NCE) accounts for background CTR variation. Temporal split by day; validate on the following day.

**Search ranking (rental/e-commerce)**: Geolocation features need smoothing (log of distance from map center, cell grid + embedding). Temporal split to mimic production traffic. Booking signal is the label; impressions without booking are negatives.

**Event recommendation**: Heavy emphasis on location, time, and social features because events are ephemeral — cold start is the default state, not an edge case. Similarity deltas (walk score similarity, remaining time similarity, price similarity) encode personalization relative to the user's history. Feature engineering effort compensates for sparse interaction data.

**News feed ranking**: Post features (text embedding, image embedding, reaction counts, hashtags, age), user features (demographics, device, time), and user-author affinity features (like rate, comment rate, friendship duration). Multi-task models predict multiple reactions simultaneously; passive user signals (dwell time, skip) require implicit reaction features.

## Feature Selection and Importance

Feature importance can be assessed through:
- Model weights (logistic regression) — direct interpretability
- Tree-based importance (GBDT/XGBoost) — impurity reduction per feature
- Ablation studies — train with and without a feature and compare offline metrics
- A/B experiments — deploy with and without a feature and compare online metrics

In practice, domain knowledge drives initial feature selection; experiments confirm or eliminate hypotheses. Noisy features (e.g., free-text event descriptions written by hosts) should be validated empirically before including in production models.

## Sources
- aman.ai: Chapter 1 — Introduction and Overview
- aman.ai: Distilled — Ad Click Prediction RecSys Design
- aman.ai: Distilled — Rental Search Ranking
- aman.ai: Chapter 7 — Event Recommendation System
- aman.ai: Chapter 10 — Personalized News Feed
- aman.ai: Primers — Standardization vs. Normalization
- aman.ai: Primers — Splitting Datasets
- aman.ai: Recommendation Systems
