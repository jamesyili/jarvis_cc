---
concept: RecSys Embeddings & Collaborative Filtering
tags: [embeddings, collaborative-filtering, matrix-factorization, cold-start, gnn]
sources:
  - kb/hard/raw/aman-ai/recommendation-systems-candidate-generation.md
  - kb/hard/raw/aman-ai/recommendation-systems-cold-start.md
  - kb/hard/raw/aman-ai/recommendation-systems-graph-neural-networks.md
last_compiled: 2026-04-05
related: [two-tower-retrieval, embeddings-and-representation-learning, recommendation-systems]
understanding: 3  # proven depth (demonstrated in dialogue/practice, or authored)
relevance: 3  # very relevant
knowledge_updated: 2026-09-07
---

# RecSys Embeddings & Collaborative Filtering

Recommendation systems learn dense vector representations — embeddings — for users and items. The core idea: if you can map users and items into the same vector space such that a user embedding is close to items they would engage with, you have a retrieval and ranking engine. This article covers how those embeddings are learned, from classical matrix factorization through neural collaborative filtering and graph neural networks, and how the cold start problem complicates all of it.

## Collaborative Filtering: The Foundation

Collaborative filtering (CF) makes recommendations based on the collective behavior of users — "users like you also engaged with these items." It requires no item features; it learns purely from the interaction matrix.

**User-based CF**: find similar users, recommend items they engaged with that the target user hasn't seen. Similarity is typically cosine similarity or Pearson correlation over interaction vectors.

**Item-based CF**: find similar items to those a user has engaged with, rank by similarity. More stable than user-based CF at scale because item similarity matrices change slower than user behavior.

Strengths: no domain knowledge needed, discovers cross-domain interests. Weaknesses: cold start for new users and items, struggles with niche interests where few similar users exist.

## Matrix Factorization

Matrix factorization (MF) decomposes the user-item interaction matrix R into two lower-rank matrices:

```
R ≈ U · Vᵀ    where U ∈ ℝ^(users×k), V ∈ ℝ^(items×k)
```

Each user gets a k-dimensional embedding vector; each item gets a k-dimensional embedding vector. The predicted score for user u on item i is the dot product uᵢ · vᵢᵀ. Training adjusts U and V to minimize reconstruction error on observed interactions.

**Loss function choices:**

- Squared error over observed pairs only: ignores unobserved user-item pairs, treats absence of interaction as neutral rather than negative
- Squared error over all pairs: penalizes predicted engagement on unobserved items, but computationally expensive
- Weighted combination: assigns weight w₀ < 1 to unobserved pairs, giving them a soft negative signal

**Optimization methods:**

- **SGD (Stochastic Gradient Descent)**: flexible, handles any loss function, parallelizes across features. Can fail to converge if learning rate is poorly tuned.
- **WALS (Weighted Alternating Least Squares)**: fixes U and solves for V in closed form, then alternates. Naturally handles unobserved pairs via weighting. Parallelizes efficiently across both users and items (each row/column can be solved independently), making it well-suited for distributed computation at scale.

**Variants:**

- **Non-Negative MF (NMF)**: constrains U and V to be non-negative, producing parts-based representations. Useful for interpretability.
- **Asymmetric MF**: user embeddings are derived from their interaction history rather than being free parameters. Better generalizes to users with sparse interactions.
- **SVD++**: extends MF by incorporating implicit feedback (items the user has interacted with at all, regardless of rating) as a secondary user embedding. Combines MF and asymmetric MF signals.

## Neural Collaborative Filtering (NCF)

NCF replaces the dot product with a multilayer perceptron (MLP), learning non-linear user-item interactions. The canonical architecture:

1. Embed user ID and item ID into dense vectors
2. Concatenate or element-wise multiply
3. Pass through fully connected layers
4. Final sigmoid layer predicts engagement probability

The **embedding + MLP paradigm** is ubiquitous in industry. Key design choices:

- **Pooling variable-length histories**: user behavior sequences (past watches, purchases) are variable length. Pool via mean, sum, or max into a fixed-length vector. YouTube's candidate generation uses mean pooling over watch and search embeddings.
- **Attention-weighted pooling**: Alibaba's Deep Interest Network (DIN) applies an attention layer between embedding and pooling, learning different user representations depending on the candidate item. This produced a 10% CTR gain and 3.8% RPM improvement over mean pooling.

For ranking stages, the input expands: user embedding, item embedding, cross features, contextual features (time, device), and the candidate item's score from the retrieval stage are concatenated before the MLP.

## Sequential Models

When user behavior has temporal structure, sequential models preserve that signal rather than collapsing it via pooling.

**RNN/GRU approaches**: session-based recommenders use a single GRU layer to model the sequence of items in a session. The hidden state captures a compressed representation of "what the user has been doing lately." Telefonica's GRU-based session recommender outperformed item-KNN on co-occurrence.

**Transformer-based approaches**: Alibaba's Behavioral Sequence Transformer (BST) applies a Transformer encoder block to the user's interaction history. Unlike NLP positional encodings (sinusoidal), BST uses time differences between interactions as position features, better capturing recency. BST achieved 4.5% CTR gain over mean pooling. BERT4Rec adapts BERT's masked language modeling: randomly mask items in a user's sequence, train the model to predict them, leveraging bidirectional context.

**SASRec** (Self-Attentive Sequential Recommendation) is the unidirectional analog — a GPT-style autoregressive transformer over interaction sequences — and is the standard strong baseline for sequential recommendation.

## Graph Neural Networks for RecSys

GNNs model the user-item interaction graph directly, allowing a user's embedding to incorporate signal from their neighbors and their neighbors' neighbors.

**Core operation — message passing**: each node aggregates information from adjacent nodes (neighbors), updates its own representation, and repeats across layers. After k layers, a node's embedding reflects its k-hop neighborhood.

**GCN (Graph Convolutional Network)**: applies a layer-wise propagation rule to aggregate neighbor features. Handles sparse interaction data naturally; capturing deeper topology as layers increase.

**GAT (Graph Attention Network)**: assigns learned attention weights to neighbors during message passing. Dynamically emphasizes more relevant connections, adapts to irregular graph structures, handles heterogeneous data (users, items, categories as different node types).

**GraphSAGE**: samples a fixed number of neighbors rather than aggregating all of them, making it scalable to large graphs. Inductive — generates embeddings for unseen nodes at inference time without full graph retraining. Uber Eats uses GraphSAGE on a bipartite user-dish graph with weighted edges, adopting a two-part hinge loss to account for strong vs. weak interaction edges.

**PinSage** (Pinterest): a production-scale GraphSAGE variant that learns pin (item) embeddings by aggregating from neighboring pins via random walks. Powers Pinterest's homefeed candidate generation and related item recommendations. Processes billions of nodes and edges.

**LightGCN**: removes feature transformation and activation functions from GCN, retaining only neighborhood aggregation. This simplification improves recommendation accuracy on the standard benchmarks. The intuition: for collaborative filtering, the semantic transformation is less important than propagating interaction signals.

## Cold Start

Cold start is the structural failure mode of all CF-based approaches: new users and new items have no interaction history, so CF has nothing to work with.

**New item cold start strategies:**

- **Content-based filtering**: use item features (text, images, metadata) to bootstrap an embedding. TF-IDF, BM25, Word2Vec, BERT can produce item embeddings without any interaction data. CF is then applied only to "warm" items.
- **Hybrid systems**: switch between content-based (cold) and collaborative (warm) models based on an item's interaction count threshold.
- **Feature hashing trick**: maps high-dimensional sparse features to a lower-dimensional embedding space via a hash function. Handles new items that weren't in the training vocabulary without retraining. Practical for recommender systems with hundreds of new users/items daily.

**New user cold start strategies:**

- **Demographic-based recommendations**: use user attributes (age, gender, geography) to assign new users to a demographic segment, inherit that segment's popular items.
- **Onboarding surveys (preference elicitation)**: ask the user to select preferred genres, topics, or items during registration. Spotify and Netflix both do this. Produces a sparse initial embedding.
- **Popular items fallback**: recommend globally popular items until enough interaction data accumulates. Risk: Harry Potter effect — globally popular items dominate because they co-occur with everything, creating inflated similarity.
- **Contextual bandits**: explore new items/user pairs with explicit uncertainty tracking. In the absence of interaction data, bandits can gather information through controlled exposure while minimizing regret.

GraphSAGE's inductive learning property is particularly relevant for cold start: it can generate embeddings for new nodes by applying the learned aggregation function to whatever features and neighbors are available.

## Sources

- Aman.ai — [Recommendation Systems: Candidate Generation](https://aman.ai/recsys/candidate-gen/)
- Aman.ai — [Recommendation Systems: Cold Start](https://aman.ai/recsys/cold-start/)
- Aman.ai — [Recommendation Systems: Graph Neural Networks](https://aman.ai/recsys/gnn/)
