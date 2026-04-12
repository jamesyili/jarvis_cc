---
concept: Approximate Nearest Neighbor Search
tags: [ann, faiss, hnsw, scann, lsh, vector-search]
sources:
  - kb/hard/raw/aman-ai/primers-approximate-nearest-neighbors-for-similarity-search.md
  - kb/hard/raw/aman-ai/primers-vector-databases.md
  - kb/hard/raw/eugene-yan/patterns-for-building-llm-based-systems-products.md
last_compiled: 2026-04-05
related: [two-tower-retrieval, embeddings-and-representation-learning, search-systems]
---

# Approximate Nearest Neighbor Search

Approximate Nearest Neighbor (ANN) search is the core primitive behind similarity search in production ML systems — powering recommendation retrieval, RAG document lookup, semantic search, and embedding-based candidate generation. The fundamental trade-off: exact nearest neighbor (ENN) search is accurate but O(N) in dataset size, making it unusable at scale. ANN sacrifices a small amount of recall for large gains in speed and memory efficiency.

## Why ANN Is Necessary

At billion-scale, even millisecond-per-vector comparisons become seconds of latency. ANN algorithms use prebuilt data structures — trees, hash tables, quantized codes, or graphs — to prune the search space before any exact distance computation happens. The accepted cost is that the returned results are _approximately_ the nearest neighbors, not guaranteed exact matches.

Four production requirements drive ANN adoption:

- **Scalability**: Collaborative filtering and content-based methods require pairwise comparisons that become infeasible past millions of items. ANN indexes scale sub-linearly.
- **Real-time latency**: Live feeds, e-commerce search, and streaming recommendations need results in <50ms. ANN supports this; exact search does not.
- **Diversity**: ANN's broader candidate pool allows recommenders to surface serendipitous results beyond the tightest cluster.
- **Cold start**: Metadata-derived embeddings for new items/users can be searched via ANN even with no behavioral data.

## Algorithm Families

### Tree-Based Methods

The simplest approach: recursively partition the embedding space using hyperplanes, then prune entire subtrees at query time.

**KD-Trees** split on the highest-variance dimension at each node. Fast for dimensions under ~30, but performance degrades sharply in high-dimensional spaces — the "curse of dimensionality" means nearly all leaf nodes are visited.

**Annoy (Approximate Nearest Neighbors Oh Yeah)** builds a _forest_ of binary trees using random projection hyperplanes. Each tree partitions the space differently, and candidates from all trees are merged. Key advantage: indexes are saved as memory-mapped files on disk, enabling shared access across processes with minimal RAM. Used by Spotify. The trade-off: static index — no incremental updates.

**Best for**: Moderate dimensionality (<100d), static datasets, embedded/resource-constrained environments.

### Quantization-Based Methods

Compress high-dimensional vectors into compact codes using learned codebooks, then approximate distances via lookup tables rather than full vector arithmetic.

**Product Quantization (PQ)** splits a d-dimensional vector into m sub-vectors, each quantized independently to one of k centroids. The final code is a tuple of m indices. Distance is approximated by summing precomputed per-subspace distances from a lookup table — no full vector arithmetic needed. This enables billion-scale indexes that fit in memory.

**Optimized PQ (OPQ)** learns a rotation matrix to decorrelate the input before PQ encoding, reducing quantization error. Heavier to train but significantly more accurate, especially when embedding dimensions are correlated.

**Locality Sensitive Hashing (LSH)** uses hash functions that map similar vectors to the same bucket with high probability (random hyperplane hashing for cosine similarity). Extremely fast (constant-time hash lookups), but suffers poor recall for complex high-dimensional data and is memory-intensive for large hash table counts.

**Anisotropic Vector Quantization (AVQ)** (used in ScaNN) allows quantization cell shapes to adapt to data distribution — elliptical rather than spherical Voronoi cells. Improves recall for Maximum Inner Product Search (MIPS), the key operation for dot-product similarity.

**Best for**: Billion-scale deployments where memory budget is tight; paired with IVF for production FAISS.

### Clustering-Based Methods

Partition the dataset into clusters (coarse quantization), then search only within the most relevant clusters at query time.

**Inverted File Index (IVF)** is the workhorse of production ANN systems. k-means clustering assigns each vector to one of `nlist` clusters. At query time, the top `nprobe` closest cluster centroids are identified, and only those clusters are searched. IVF dramatically narrows the search space. In practice, IVF is almost always combined with PQ compression (IVF-PQ in FAISS) — IVF for coarse partitioning, PQ for compressed storage and fast distance approximation. Key parameters: `nlist` (cluster count) and `nprobe` (clusters searched at query time — the main recall/latency knob).

**Residual Vector Quantization (RVQ)** applies multiple rounds of quantization, each encoding the residual error from the prior stage. Higher recall than single-pass PQ at the cost of more complex training and slightly higher latency.

**Best for**: Web-scale systems. IVF-PQ powers Facebook's visual search and most large-scale FAISS deployments.

### Graph-Based Methods

Build a proximity graph where each node connects to its approximate nearest neighbors. Queries navigate the graph greedily toward the query point.

**Hierarchical Navigable Small Worlds (HNSW)** is the current state of the art for high-recall, low-latency ANN. It builds a multilayer graph: upper layers have sparse long-range connections for fast coarse navigation; lower layers have dense local connections for precision. Construction parameters `M` (max edges per node) and `efConstruction` control quality. Query parameter `efSearch` controls the recall/latency trade-off. Key advantages: supports dynamic insertions without full index rebuild; achieves excellent recall at low latency across high-dimensional embedding spaces.

**Navigable Small Worlds (NSW)** is the non-hierarchical predecessor to HNSW — simpler but slower and less reliable on large datasets.

**FINGER** is an optimization layer that can be applied on top of existing NSW/HNSW graphs at query time. It approximates distances using vector projections instead of full dot products, reducing latency by 20-60% without altering the index structure.

**Best for**: Production vector databases (Pinecone, Weaviate, Milvus, Vespa all default to HNSW). Best accuracy-speed trade-off in high dimensions.

## Library Reference

| Library | Primary Method | Key Strength | Watch Out |
|---------|---------------|--------------|-----------|
| **FAISS** | IVF, PQ, HNSW variants | GPU support; billion-scale; most flexible | Requires tuning `nlist`/`nprobe`; no native persistence |
| **ScaNN** | AVQ + clustering | Best recall/latency trade-off benchmarked; excels at MIPS | Less flexible; harder to extend |
| **Annoy** | Random projection forest | Disk-based; multi-process sharing; simple | Static index; no dynamic updates |
| **hnswlib** | HNSW | Fast, clean HNSW implementation | Memory-heavy at large scale |

## Choosing an Algorithm

| Constraint | Recommended |
|-----------|-------------|
| Low dimensions (<100d), static data | Tree-based (Annoy, KD-forest) |
| Billion vectors, tight memory | IVF-PQ (FAISS) |
| Dynamic index, high recall required | HNSW |
| Latency <1ms, ok with lower recall | LSH |
| Semantic search, neural embeddings | HNSW or ScaNN (AVQ) |
| Existing HNSW, need lower latency | Add FINGER |

## Production Evaluation Metrics

When selecting an ANN index, benchmark on:

1. **Recall@k**: Fraction of exact top-k neighbors returned. Primary accuracy measure.
2. **QPS (queries per second)**: Throughput at target recall.
3. **Build time**: One-time cost to construct the index.
4. **Memory footprint**: RAM required to serve the index.
5. **Incremental update support**: Can new vectors be added without full rebuild?

ANN-Benchmarks (ann-benchmarks.com) provides standardized comparisons across datasets and distance metrics. No single library wins on all dimensions — define your requirements first, then benchmark.

## Vector Quantization and Codebooks

Both VQ and PQ rely on **codebooks** — sets of learned centroid vectors. In VQ, a single codebook covers the full vector space (one centroid per cluster). In PQ, m separate codebooks each cover one subspace. Encoding maps each vector to centroid indices; decoding reconstructs an approximate vector. The key trade-off: PQ scales to high dimensions at acceptable quantization error; VQ grows exponentially with dimension.

## Sources

- Aman.ai: [Primers — Approximate Nearest Neighbors for Similarity Search](https://aman.ai/primers/ai/ann-similarity-search/)
- Aman.ai: [Primers — Vector Databases](https://aman.ai/primers/ai/vector-dbs/)
- Eugene Yan: [Patterns for Building LLM-based Systems & Products](https://eugeneyan.com/writing/llm-patterns/) (ANN section)
