---
concept: Two-Tower Retrieval
tags: [retrieval, two-tower, dual-encoder, candidate-generation, ann]
sources:
  - kb/hard/raw/aman-ai/chapter-6-video-recommendation-system.md
  - kb/hard/raw/aman-ai/chapter-2-youtube-video-search.md
  - kb/hard/raw/aman-ai/recsys-embeddings.md
  - kb/hard/raw/aman-ai/chapter-9-similar-listings-on-vacation-rental-platforms.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/recommendation-systems|Recommendation Systems]]"
  - "[[hard/wiki/embeddings-and-representation-learning|Embeddings and Representation Learning]]"
  - "[[hard/wiki/approximate-nearest-neighbor|Approximate Nearest Neighbor]]"
understanding: 4  # boundary pushing
relevance: 3  # very relevant
knowledge_updated: 2026-09-07
---

# Two-Tower Retrieval

The two-tower (dual encoder) architecture is the dominant pattern for candidate retrieval in large-scale recommendation and search systems. It encodes queries (users, search queries) and items (videos, products, listings) into a shared embedding space using separate neural networks, then uses approximate nearest neighbor (ANN) search to retrieve relevant candidates at serving time. The key constraint — and insight — is that the two towers cannot interact during inference, which enables pre-computation and ANN serving across billion-scale catalogs.

## Architecture

The core structure is simple: two independent encoders that each produce a fixed-dimensional embedding vector, and a similarity function (typically dot product or cosine similarity) that scores query-item pairs.

**Query tower**: Takes user features (user ID, demographics, interaction history, context) as input and produces a user embedding. In video recommendations, this might incorporate a user's watch history, language, country, and device.

**Item tower**: Takes item features (item ID, title, tags, content embeddings, metadata) and produces an item embedding. In video search (YouTube), this is a video encoder that processes both visual frames and textual metadata.

**Similarity scoring**: The dot product between query and item embeddings produces a relevance score. Cosine similarity (normalized dot product) is also common. The choice affects training dynamics — dot product rewards magnitude, cosine rewards direction.

The fundamental constraint: at inference time, query and item embeddings are computed independently, without cross-tower attention or interaction. This means you can pre-compute all item embeddings offline and store them in an ANN index. At serving time, only the query tower runs — a single forward pass — followed by ANN lookup.

## Training

**Positive pairs**: Typically constructed from observed interactions — user watched a video (YouTube), user booked a listing (Airbnb), user clicked a result (search). The signal is implicit: these pairs should have high similarity.

**Negative sampling**: The key training challenge. Without negatives, the model collapses to representing all items similarly. Two main strategies:

- **In-batch negatives (random negatives)**: Treat other items in the same training batch as negatives for a given query. Efficient — no extra data needed. But easy negatives are common, limiting the model's ability to discriminate near-misses.

- **Hard negatives**: Items that are semantically related but not the target — items the user viewed but did not interact with, items from the same category, items in the same region. Airbnb's listing embedding paper added same-region negatives explicitly because random negatives were almost always from different regions, making the learning too easy and producing embeddings that failed to distinguish similar-region alternatives.

**Contrastive loss**: The standard loss function. For a positive pair (query q, item p) and negative items (n₁, n₂, ...):
```
loss = -log( exp(q·p) / (exp(q·p) + Σ exp(q·nᵢ)) )
```
This is noise contrastive estimation (NCE) or the InfoNCE loss. It pushes the query embedding toward the positive item and away from negatives.

**Global context as training signal**: Airbnb's approach for listing embeddings is instructive. When learning embeddings from browsing sessions, they add the "eventually booked listing" as a global positive context — it remains in the positive set for every window position, not just when it's in the sliding window. This pushes embeddings toward booking-predictive similarity rather than just co-occurrence similarity.

## ANN Serving

Once item embeddings are computed offline, they are loaded into an ANN index. At serving time:
1. Query tower runs a single forward pass to produce the query embedding
2. ANN lookup retrieves top-k nearest items by approximate dot product or cosine distance
3. Candidates are passed downstream to the ranking stage

**ANN libraries**: FAISS (Facebook, optimized for batched queries), ScaNN (Google, better single-query latency), hnswlib (Hierarchical Navigable Small World graphs, graph-based). The tradeoff is recall vs. latency — ANN trades exact nearest neighbors for speed. Typical production targets are recall@100 > 0.95 with sub-10ms latency.

**Quantization**: Item embeddings are often quantized (e.g., product quantization in FAISS) to reduce memory footprint. Full-precision embeddings are stored separately in a "forward index" for feature augmentation during ranking.

**Index freshness**: New items need to be embedded and added to the index. YouTube's system handles billions of items. The standard pattern is periodic full re-embedding + continuous incremental updates for new items.

## Multi-Modal Extensions

The two-tower architecture extends naturally to multi-modal inputs:

**Video + text (YouTube search)**: The query tower processes text queries (normalized, tokenized, embedded via transformer or lookup). The item tower processes both visual frames (via CNN or frame-level model) and textual metadata (title, description, tags). The final video embedding fuses both modalities. Text and visual search results are fused in a separate layer before reranking.

**Image + text (Pinterest)**: PinnerFormer and similar models incorporate visual pin content (image embeddings) alongside textual signals and user history in transformer-based architectures.

Multi-modal item towers typically require significantly more offline compute for embedding generation, but the serving pattern remains the same: pre-compute → ANN index → query tower at inference time.

## The Cross-Tower Limitation

The inability to model query-item interactions is the core limitation of two-tower models. Because the towers are independent, the model cannot capture fine-grained interactions like "this user prefers mountains over beaches, and this specific item is in the Alps" — that interaction would require the towers to communicate. This is why two-tower is used for retrieval (recall) rather than ranking (precision): it sacrifices per-pair accuracy for the ability to scale to billions of items via ANN.

Deep interaction models (Wide & Deep, DCN, DIN) handle this at the ranking stage, operating on the small candidate set where per-pair feature computation is feasible. The [[hard/wiki/learning-to-rank|Learning to Rank]] wiki covers these architectures.

## Connection to CLR/UPP (Pinterest Context)

At Pinterest, Homefeed Candidate Generation relies on embedding-based retrieval. The CLR (Collaborative Learning to Rank) and UPP (User Preference Prediction) systems are architecturally similar to two-tower: user representations are computed independently from pin representations, and retrieval uses ANN. The key Pinterest-specific complexity is real-time user representation updates — incorporating recent user actions (saves, clicks) into the query embedding quickly enough to reflect session-level intent shifts.

## Sources

- Aman.ai: [Chapter 6 — Video Recommendation System](https://aman.ai/h/des/video-recommendation/)
- Aman.ai: [Chapter 2 — YouTube Video Search](https://aman.ai/h/des/youtube-video-search/)
- Aman.ai: [RecSys Embeddings](https://aman.ai/recsys/embeddings/)
- Aman.ai: [Chapter 9 — Similar Listings on Vacation Rental Platforms](https://aman.ai/h/des/similar-listings/)
