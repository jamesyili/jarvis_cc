---
concept: Two-Tower Retrieval
tags: [retrieval, two-tower, dual-encoder, embeddings, ann, candidate-generation]
sources:
  - kb/hard/raw/aman-ai/chapter-2-visual-search.md
  - kb/hard/raw/aman-ai/chapter-2-youtube-video-search.md
  - kb/hard/raw/aman-ai/chapter-6-video-recommendation-system.md
  - kb/hard/raw/aman-ai/chapter-7-event-recommendation-system.md
  - kb/hard/raw/aman-ai/chapter-9-similar-listings-on-vacation-rental-platforms.md
  - kb/hard/raw/aman-ai/recsys-embeddings.md
  - kb/hard/raw/aman-ai/recommendation-systems.md
last_compiled: 2026-04-05
related: [recommendation-systems, embeddings-and-representation-learning, learning-to-rank, feature-engineering]
---

# Two-Tower Retrieval

Two-tower (also called dual encoder) retrieval is the dominant architecture for first-stage candidate generation at scale. The core insight: instead of scoring query-item pairs jointly (expensive, requires both at query time), encode each side independently into a shared embedding space, then retrieve via nearest neighbor search. The similarity score — typically dot product — stands in for relevance.

## Architecture

Two encoders operate in parallel. The **query tower** takes whatever defines the request — a user profile, a text query, a currently-viewed item — and maps it to an embedding vector. The **item tower** takes item features and maps each item to an embedding in the same space. Similarity is computed as:

```
score(q, i) = dot(encoder_query(q), encoder_item(i))
```

The towers are independent at inference, which is the key architectural property that makes this tractable: item embeddings can be precomputed and indexed offline, so query-time cost reduces to a single encoder forward pass plus an ANN lookup.

In video recommendation (YouTube-style systems), the user tower ingests demographics, watch history, search history, and contextual signals; the video tower ingests video ID, duration, language, and title/tag embeddings. The towers can be shallow MLPs or deep transformer stacks depending on compute budget and feature complexity (aman-ai/chapter-6-video-recommendation-system).

For visual search, the same architecture extends to cross-modal retrieval: a text encoder (BERT or similar) produces query embeddings; a video/image encoder (ViT or frame-level model) produces item embeddings. Training aligns them via contrastive loss so that a text query for "dogs playing indoor" maps close to relevant videos in the shared space (aman-ai/chapter-2-youtube-video-search).

## Training: Contrastive Loss and Negative Sampling

The standard training objective is contrastive: pull embeddings of positive pairs together, push negative pairs apart. The loss over a session or batch:

```
loss = Σ(c,p)∈D_pos  log sigmoid(e_c · e_p)
     + Σ(c,n)∈D_neg  log sigmoid(-e_c · e_n)
```

Where `e_c` is the central/query embedding, `e_p` is a positive item, and `e_n` is a negative item (aman-ai/chapter-9-similar-listings-on-vacation-rental-platforms).

**In-batch negatives** are the standard efficiency trick: within a mini-batch of B positive pairs, each query uses the other B-1 items as negatives at no extra cost. This is how YouTube's DNN-for-recommendations paper scales contrastive training to billions of examples.

**Hard negatives** matter more than random negatives at the margin. Airbnb's listing embedding work demonstrates this concretely: randomly sampled negatives are usually from different cities, making the task trivially easy. Adding same-city negatives (listings that didn't co-occur but are geographically similar) sharpens the decision boundary and improves booking prediction (aman-ai/chapter-9). The updated loss includes a fourth term `Σ(c,n)∈D_hard` for same-region negatives.

**Global context as a positive signal**: Airbnb also treats the eventually-booked listing as a global context during training — it stays in the positive set for every window position in a session, not just when it's in the local window. This biases learned embeddings toward booking intent rather than just click co-occurrence.

For two-tower models trained on user-item pairs with binary labels (relevant/not-relevant), binary cross-entropy is the standard loss function with the dot product similarity passed through a sigmoid (aman-ai/chapter-6-video-recommendation-system).

## ANN Serving: FAISS, ScaNN, HNSW

At serving time, candidate generation is a k-nearest-neighbor lookup in embedding space. With 5M–10B items, exact cosine/dot-product search is O(N·d) per query — infeasible at production latency. Approximate nearest neighbor (ANN) algorithms trade recall for speed.

The canonical production pattern:
1. After each training cycle, run the item tower over the full item catalog to produce embeddings.
2. Index those embeddings in an ANN index (FAISS, ScaNN, or HNSW).
3. At query time, run the query tower once, then call the ANN service to retrieve top-K candidates in milliseconds.

Key latency trade-offs across ANN methods:
- **HNSW** (Hierarchical Navigable Small World graphs): excellent recall at low latency, higher memory footprint due to graph structure.
- **FAISS** (Facebook AI Similarity Search): highly configurable; IVF-PQ (inverted file index + product quantization) compresses vectors to reduce memory while maintaining reasonable recall.
- **ScaNN** (Google): optimized for dot product similarity specifically; used in production at Google for YouTube retrieval.

The Airbnb system illustrates the indexing pipeline pattern clearly: embeddings are precomputed and stored in an index table; an **indexing pipeline** updates the table when new listings are added or when a retrained model produces new embeddings. The **embedding fetcher service** at query time either retrieves the stored embedding (if the item was seen during training) or falls back to a heuristic — e.g., using the embedding of a geographically nearby listing for new cold-start items (aman-ai/chapter-9-similar-listings).

## Two-Tower vs. Matrix Factorization

Matrix factorization is the degenerate case of two-tower: the item tower is just an embedding lookup (item ID → embedding vector), with no feature inputs. This makes MF fast to train (WALS converges faster than SGD) and fast at serving (embeddings are static). But it can't handle new users (no interaction history → no embedding), and it can't incorporate rich features like language, duration, or demographics (aman-ai/chapter-6-video-recommendation-system).

| Property | Matrix Factorization | Two-Tower NN |
|---|---|---|
| Training cost | Lower (WALS/ALS) | Higher |
| Inference speed | Faster (static embeddings) | Slightly slower (query tower runs live) |
| Cold start (new users) | Fails | Handles via user features |
| Feature richness | ID-only | Arbitrary features |
| Recommendation quality | Lower | Higher |

Two-tower wins on quality and flexibility at the cost of compute. In practice, MF is used as a fast baseline or for serving environments with extreme latency constraints.

## Multi-Modal Extensions

The architecture extends naturally to multi-modal retrieval by changing encoder inputs:

- **Text + visual content** (YouTube video search): text encoder on the query; video encoder (ViT frame-level model → mean-pooled frame embeddings) on the item. Both towers trained jointly via contrastive loss so text and video embeddings align in the same space (aman-ai/chapter-2-youtube-video-search).
- **User context tower**: the query tower ingests not just the immediate query but also historical signals — liked items, watch history, search history — each encoded independently and aggregated (e.g., averaged embeddings over variable-length history lists). This is how YouTube's homepage recommendation encodes long-term interest into the user embedding.
- **Session-aware towers**: for session-based recommendation (Airbnb similar listings), the "query" is not a user profile but a currently-viewed item. The item tower and the context tower collapse into one: embed the current listing, retrieve similar listings.

## Industry Applications

**YouTube (DNN for Recommendations)**: Two-stage design — two-tower model as the candidate generator (narrows 10B videos to ~hundreds), then a separate ranking model scores candidates with richer features. The two-tower candidate generator prioritizes recall and speed over precision. Multiple candidate generators are used in parallel to diversify: one for relevance, one for trending, one for geographically relevant content (aman-ai/chapter-6-video-recommendation-system).

**Airbnb (Listing Embeddings)**: Session-based embedding model using a Word2Vec-inspired objective. Listings that co-occur in browsing sessions are trained to have similar embeddings; the eventually-booked listing and same-region hard negatives refine the embedding space. At serving time, the nearest neighbor service retrieves listings similar to the one currently being viewed. The training pipeline runs daily to incorporate new listings and new interaction data (aman-ai/chapter-9-similar-listings).

**Visual Search / Multi-modal**: The two-tower structure naturally handles cross-modal retrieval where query and item live in different modalities. The training objective forces both modalities into a shared semantic space, enabling a text query to retrieve visually and semantically relevant videos (aman-ai/chapter-2-youtube-video-search).

## Critical Limitation: No Cross-Tower Feature Interaction

The defining weakness of two-tower retrieval is that the query and item encoders never see each other during inference. Any feature that requires knowing both simultaneously — "does this user's watch history match this video's content?" — cannot be computed in the retrieval stage.

This is why two-tower is always stage one in a multi-stage pipeline. The retrieval stage optimizes for recall: get relevant items into the candidate set. A separate ranking model (typically a pointwise or listwise LTR model with cross-attention or feature crossing between query and item) then scores the smaller candidate set with full cross-feature interaction. You get the speed of independent encoding at retrieval scale, and the accuracy of joint scoring at ranking scale.

In ad click prediction (aman-ai/chapter-2-visual-search), this distinction is explicit: the two-tower architecture is noted as an option for candidate generation, but Deep & Cross Networks (DCN) or DeepFM — which explicitly model query-item feature interactions — are used for the ranking stage.

## Connection to Pinterest CLR / UPP Architecture

Pinterest's Homefeed Candidate Generation (CLR/P2P) extends the two-tower pattern for multi-surface personalization. The architecture introduces:
- A **shared user context tower** (UPP — User Preference Profile) that encodes long-term user interest signals once and reuses across surfaces.
- A **condition tower** that encodes the surface context (Homefeed vs. Search vs. Related Pins).
- **Surface-specific item towers** that encode candidates differently depending on the surface.

This decomposes the classic two-tower into three encoders, allowing user context to be computed once (amortized across surfaces) while surface-specific signals are handled by the condition + item towers. The ANN retrieval pattern at serving time is identical.

## Evaluation

**Offline metrics for retrieval (candidate generation quality)**:
- **Recall@K**: did the relevant item appear in the top K? The primary metric — retrieval is useless if it misses relevant items.
- **MRR (Mean Reciprocal Rank)**: rewards ranking the relevant item higher. More informative than Recall@K when K is large.
- **Average rank of eventually-booked listing** (Airbnb): domain-specific metric that directly measures whether the embedding space predicts booking intent.

Precision@K is generally less informative at the retrieval stage — you expect a high false positive rate and tolerate it because the ranking stage will filter.

**Online metrics** depend on the downstream application: CTR, total watch time, session book rate, conversion rate. The retrieval model's contribution is indirect — it sets the ceiling on what the ranker can achieve.

## Sources

- [[kb/hard/raw/aman-ai/chapter-2-youtube-video-search|Chapter 2: YouTube Video Search]]
- [[kb/hard/raw/aman-ai/chapter-2-visual-search|Chapter 2: Visual Search / Ad Click Prediction]]
- [[kb/hard/raw/aman-ai/chapter-6-video-recommendation-system|Chapter 6: Video Recommendation System]]
- [[kb/hard/raw/aman-ai/chapter-7-event-recommendation-system|Chapter 7: Event Recommendation System]]
- [[kb/hard/raw/aman-ai/chapter-9-similar-listings-on-vacation-rental-platforms|Chapter 9: Similar Listings on Vacation Rental Platforms]]
- [[kb/hard/raw/aman-ai/recsys-embeddings|RecSys Embeddings]]
- [[kb/hard/raw/aman-ai/recommendation-systems|Recommendation Systems Overview]]
