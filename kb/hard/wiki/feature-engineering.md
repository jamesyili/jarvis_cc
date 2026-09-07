---
concept: Feature Engineering
tags: [feature-engineering, categorical-encoding, temporal-features, data-preprocessing]
sources:
  - kb/hard/raw/aman-ai/recommendation-systems-candidate-generation.md
  - kb/hard/raw/aman-ai/applied-machine-learning-for-industry.md
  - kb/hard/raw/aman-ai/primers-data-sampling.md
  - kb/hard/raw/aman-ai/primers-splitting-datasets.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/recommendation-systems|Recommendation Systems]]"
  - "[[hard/wiki/learning-to-rank|Learning to Rank]]"
  - "[[hard/wiki/feature-stores|Feature Stores]]"
understanding: 3  # proven depth (demonstrated in dialogue/practice, or authored)
relevance: 2  # somewhat / potentially relevant
knowledge_updated: 2026-09-07
---

# Feature Engineering

Feature engineering is the process of transforming raw data into representations that ML models can learn from effectively. In recommendation systems and ranking pipelines, feature engineering sits at the foundation of model quality — a well-featured logistic regression frequently outperforms a poorly-featured deep network. Understanding the feature taxonomy, encoding decisions, and data pipeline integrity is as important as model architecture selection.

## Feature Taxonomy

Features in a recommender system fall into four categories:

**User features**: Who is asking. Demographics (age, gender, location, language), historical behavior (click history, purchase history, watch history, dwell time), long-term preference embeddings, and derived attributes (price sensitivity, category affinity). User features capture stable preferences and slow-moving patterns.

**Item features**: What is being recommended. Content metadata (title, description, tags, category), quality signals (likes, views, ratings, engagement rates), freshness (publish date, trend score), and content embeddings (image embeddings, text embeddings). Item features describe what the item is and how it performs.

**Context features**: When and where. Time of day, day of week, device type, app version, session length, user location. Context features capture situational factors that affect preference — a user's movie preferences on mobile during commute differ from preferences on TV on Sunday evening.

**Cross features**: Interactions between features. "User is female AND device is mobile AND time is evening" is a cross feature. These are second-order (or higher) feature products that capture nonlinear interactions that linear models can't represent. Google's Wide & Deep paper formalized the importance of cross features: specific feature combinations provide memorization (e.g., a user who installed Netflix is more likely to click Hulu) that DNN generalization cannot replicate.

In the Google Play Store example: first-order features are `impressed_app` and `user_installed_apps`. Their cross product `AND(user_installed_app='netflix', impression_app='hulu')` captures a specific behavioral pattern. Multiple granularities of crosses are valuable — coarse crosses (`AND(category='video', category='video')`) provide generalization while fine-grained crosses provide memorization.

## Sparse vs. Dense Features

**Sparse features**: High-dimensional, mostly-zero representations. User IDs, item IDs, categorical variables (country, device type). Represented as one-hot encoded vectors or multi-hot sets. The key transformation: map sparse inputs to dense embedding vectors via an embedding lookup table (matrix of shape V×D, where V is vocabulary size and D is embedding dimension, typically 10–300).

**Dense features**: Continuous numerical values. Watch time, click rate, price, age. Can be fed directly into models, though normalization is usually required.

**The hashing trick**: For very large or dynamic vocabularies, map IDs to a fixed-size hash table. Fast and handles unseen IDs naturally. Common functions: modulo hashing, MurmurHash, consistent hashing. Collision mitigation: concatenate multiple independent hashes.

**Embedding re-initialization for new IDs**: Expand matrix dynamically, reserve pool embeddings for unseen IDs, fall back to zero or average embedding, or warm-start via incremental fine-tuning.

## Numerical Transforms

Raw numerical features often have distributions that hurt model learning:

**Log transform**: Right-skewed distributions (count features, revenue). Compresses large values, expands small values, often makes the distribution more Gaussian.

**Normalization/standardization**: Zero-mean, unit-variance scaling. Required before feeding into models that use gradient descent — unnormalized features with different scales cause poorly conditioned optimization.

**Binning/bucketization**: Convert continuous to categorical (age → age bucket). Useful when the relationship between the feature and target is non-monotonic (e.g., CTR peaks in the 25–35 age bucket, not at the maximum age value).

**Geolocation encoding**: Raw latitude/longitude are hard for models to use (coordinate space is non-smooth relative to behavior). Airbnb takes `log(distance from center of map)` for latitude and longitude separately. Another approach: geohash bucketing — discretize coordinates into a hierarchical grid.

## Temporal Features

Time-aware features are critical in recommendation systems where content freshness and recency of user behavior matter.

**Recency weighting**: Recent interactions are more informative than old ones. User history features are often aggregated with exponential decay: `Σ interaction_i * exp(-λ * (now - time_i))`.

**Temporal splits**: Train/val/test splits should be time-ordered, not random. Using future data in training is data leakage. The standard production pattern: split at a timestamp, use data before T for training and data after T for validation. This simulates production conditions where the model is always deployed into the future.

**Sequence features**: The order of user interactions carries signal. A user who browsed `GPU → RAM → motherboard` has different intent than `GPU → GPU → GPU`. DIN (Deep Interest Network) uses attention over interaction sequences. For time-series aggregation: rolling windows of different lengths (last 1 hour, last 7 days, last 30 days) as separate features.

**Time-of-day and day-of-week**: Critical context features. Encode cyclically as `sin(2π * hour/24)` and `cos(2π * hour/24)` to preserve the circular relationship (hour 23 is close to hour 0).

## Categorical Encoding

**One-hot encoding**: Works for low-cardinality features (device type, language). Breaks down for high-cardinality features (user ID, item ID).

**Embedding lookup**: The standard for high-cardinality categoricals in neural models. Dimension typically `O(10)` to `O(100)`, often chosen as `min(50, (cardinality + 1) // 2)`. Learned jointly during training.

**Target encoding**: Replace category with its mean target value. Risk of target leakage — compute on training data only. Useful in GBDT pipelines where embedding layers aren't available.

**Feature hashing (hashing trick)**: For high cardinality or dynamic vocabularies. Deterministic hash to index. Memory-efficient, handles unseen values. Trade-off: hash collisions cause feature aliasing.

## Feature Stores and Train-Serve Consistency

The most common and damaging feature engineering failure in production is train-serve skew: features computed differently during training vs. serving. Models often still work — just worse than they should — and the gap is hard to diagnose.

**Consistency principles**: Use identical feature computation logic for training and serving (JD implemented a single C++ tokenizer with a Python wrapper, used in preprocessing, training, and serving). Use time-travel features — historical features should reflect what was known at prediction time, not future data. Pre-compute heavy features offline and store in a feature store for low-latency serving.

**Feature store pattern**: Dual-store — offline (batch, Spark/BigQuery) for training, online (Redis/DynamoDB, <10ms) for serving. Offline features periodically synced to online store. See [[hard/wiki/feature-stores|Feature Stores]] for architecture details.

## Data Sampling and Class Imbalance

Recsys datasets are heavily imbalanced — CTR is typically 1–2%.

**Negative downsampling**: Keep all positives, downsample negatives (1:10 to 1:100 ratio). Requires post-training calibration: `p_calibrated = p / (p + (1-p) / negative_sample_rate)`.

**Stratified sampling**: Preserve class distribution across splits. Critical for rare positives — random splits can leave validation sets with no positive examples.

**Hard negative mining**: Select negatives the model currently scores too highly (near-misses). Improves discrimination in embedding space. Airbnb's listing embeddings added same-region negatives because random negatives were almost always geographically distant, making training too easy.

**Focal loss**: `FL(p_t) = -α_t * (1 - p_t)^γ * log(p_t)`. Down-weights easy examples, concentrating training on hard cases. Broadly applicable to imbalanced classification.

## Train/Val/Test Splitting

**Time-based splits**: Always split by time for recommendation systems. Random splits cause data leakage — a user's future clicks correlate with past clicks, inflating offline metrics.

**Same distribution**: Dev and test sets should come from the same distribution as expected production traffic. For large datasets (>1M), 1% each (~10k) is sufficient. Smaller datasets need larger proportions for stable evaluation.

**Reproducibility**: Fixed seed before shuffling; sort data before shuffling to ensure deterministic order. Store split indices, not just data.

**Train-dev set**: When training and dev data must have different distributions (domain shift, limited labeled data), add a train-dev set from the training distribution. Train-dev vs. dev gap indicates distribution shift; train vs. train-dev gap indicates overfitting.

## Sources

- Aman.ai: [Recommendation Systems — Candidate Generation](https://aman.ai/recsys/candidate-gen/)
- Aman.ai: [Applied Machine Learning for Industry](https://aman.ai/h/handsonproject/)
- Aman.ai: [Primers — Data Sampling](https://aman.ai/primers/ai/data-sampling/)
- Aman.ai: [Primers — Splitting Datasets](https://aman.ai/primers/ai/data-split/)
