---
concept: Search Systems
tags: [search, query-understanding, bm25, dense-retrieval, hybrid-search]
sources:
  - kb/hard/raw/aman-ai/recommendation-systems-search.md
  - kb/hard/raw/eugene-yan/search-query-matching-via-lexical-graph-and-embedding-methods.md
  - kb/hard/raw/aman-ai/chapter-2-youtube-video-search.md
last_compiled: 2026-04-05
related: [retrieval-augmented-generation, learning-to-rank, approximate-nearest-neighbor]
understanding: 2  # basic understanding (assumed where James's background applies)
relevance: 2  # somewhat / potentially relevant
knowledge_updated: 2026-09-07
---

# Search Systems

Search is recommendations with a query as extra context. The query is both a boon (extra signal about intent) and a bane (users now hold the system to higher precision expectations). A production search system is an orchestration of multiple retrieval strategies — lexical, semantic, and graph-based — combined with query understanding, candidate fusion, and ranking.

## The Retrieval Stack

Modern search systems have three conceptual layers:

1. **Query understanding**: Transform the raw query string into something the retrieval systems can match against effectively.
2. **Candidate generation**: Retrieve thousands of candidate documents from potentially billions, using multiple retrieval methods in parallel.
3. **Ranking**: Score and order candidates for final presentation, optimizing for the user's true intent.

This article focuses on query understanding and candidate generation. See [[hard/wiki/learning-to-rank|Learning to Rank]] for the ranking layer.

## Lexical Retrieval: The Bedrock

Lexical methods match documents to queries based on token overlap. **BM25** (Best Match 25) is the industry standard — it scores documents by TF-IDF-like weighting with length normalization, implemented efficiently via an inverted index. BM25 is the default in Elasticsearch and Lucene.

### Query Processing Pipeline

Before retrieval, raw queries are preprocessed:

- **Normalization**: Lowercasing, unicode standardization, accent removal, stemming (e.g., "hiking boots" → "hike boot").
- **Spell correction**: Using algorithms like Symmetric Delete or edit-distance approaches. DoorDash found they needed to _defer_ spell correction — if the original query returns no results, _then_ correct; aggressive correction can corrupt valid brand names.
- **Query expansion**: Add synonyms and abbreviations to broaden recall (e.g., "handphone OR mobile phone OR cellphone"). Yahoo used a text-translation model trained on bipartite click graphs (queries ↔ clicked documents) to translate tail queries into head queries — matching cold-start queries against richer click data.
- **Query relaxation**: Remove tokens to increase recall. For product search: drop color, size, model number, and other entity modifiers. "acme gold iphone charger i012e large" → "iphone charger".
- **Query rewriting**: Canonical form standardization. DoorDash maps "KFZ", "Poulet Frit Kentucky", and "KFC" all to "kfc" via synonym dictionaries.

### Pitfalls of Pure Lexical Search

- **Vocabulary mismatch**: "California rolls" retrieves Mexican restaurants because "California" and "roll" appear in Mexican menus — the system doesn't understand intent.
- **Hypernyms/synonyms**: "hat" won't retrieve "beret" unless explicitly mapped. "burgundy dress" won't match "red dress".
- **Antonyms**: "latex gloves" and "latex free gloves" share tokens but are opposites.
- **Morphological variants**: "woman" vs "women" unless stemming handles it correctly.
- **Misspellings**: ~10% of queries are misspelled; spell correction is imperfect.

## Graph-Based Retrieval: Adding Concept Structure

Knowledge graphs connect entities (foods, cuisines, restaurants, categories) via typed relationships, enabling query expansion at the concept level.

**Uber Eats** built a food ontology with `countryOfOrigin` and `subCategoryOf` edges. Querying "Udon" expands to "Ramen", "Soba", "Japanese". **DoorDash** built a Neo4j graph with store, food category, and food tag nodes. "KFC" expands to `chicken_cat`, then to `fried_chicken_tag` and `wings_tag`, returning similar restaurants. "Asian" expands to `thai_cat`, `chinese_cat`, and their associated stores.

Knowledge graphs are expensive to build and maintain — requiring ontology design, multi-source data ingestion, node deduplication, and continuous quality checks. They also must tag offline catalog items and expand queries in real-time online. The payoff is improved recall on head queries and hierarchical expansion that pure lexical matching can't do.

## Embedding-Based (Dense) Retrieval

Representation learning encodes queries and documents into dense vectors where semantic similarity is captured by distance in embedding space. This handles vocabulary mismatch, synonymy, and morphological variation that lexical methods can't.

### Self-Supervised Approaches

**Uber** applied GloVe to query co-occurrence: two queries "share context" if both lead to orders from the same restaurant. The resulting query embeddings enable expansion via ANN — "tan tan noodle" expands to "Little Szechuan", "Chinese", "Spicy Food". **GrubHub** used word2vec-style skip-gram on query sessions, with nearest-neighbor results closely matching a reference food knowledge graph.

### Supervised Two-Tower Models

The dominant paradigm for production embedding-based retrieval is the **bi-encoder (two-tower)** architecture:

- **Query tower**: Encodes the query string into a dense vector.
- **Document/item tower**: Encodes the document (title, description, attributes) into a dense vector.
- **Similarity**: Cosine similarity or dot product between the two vectors.
- **Training objective**: Contrastive loss (triplet loss or InfoNCE) — bring positive query-doc pairs together, push negatives apart.

**Amazon's semantic product search**: Shared query/product embeddings with character tri-grams + word n-grams (for spelling robustness). Introduced a three-part hinge loss: positives (purchased), negatives (impressed but not clicked), and hard negatives (random) — better separation of score distributions.

**Facebook's embedding-based search**: Separate towers for queries and documents. Used triplet loss. Found that _random negatives_ outperformed impressed-but-not-clicked negatives (unlike Amazon) — hypothesis: non-click impressions bias training toward hard cases unrepresentative of the actual retrieval distribution.

**JD's multi-head query tower**: K separate query encoders, each learning a different "aspect" of the query (e.g., different popular brands for "cellphone"). Similarity = weighted sum of all K inner products. Enables multi-intent queries.

### Embedding Fine-Tuning

Two strategies for adapting embedding models:

- **Masked Language Modeling (MLM)**: Domain-adapted pre-training. Updates model knowledge without requiring labeled pairs. Use when you have domain corpus but limited labeled retrieval pairs.
- **Contrastive losses** (InfoNCE / Multiple Negatives Ranking Loss, Triplet, Cosine Embedding): Directly optimizes the retrieval objective. Use when you have labeled (query, positive doc, negative doc) triplets or click/purchase data.

## Hybrid Search: Combining Lexical and Semantic

Neither lexical nor semantic retrieval alone is sufficient. Semantic search fails on exact match requirements (names, acronyms, IDs). Lexical search fails on synonyms and semantic intent. The production answer is **hybrid search**.

### Reciprocal Rank Fusion (RRF)

The simplest fusion strategy. For each document d, combine ranks from each retrieval system:

```
RRF_score(d) = Σ 1 / (k + rank_i(d))
```

where k is a smoothing constant (typically 60). RRF is robust, requires no score normalization, and outperforms simple score-based fusion in most settings.

### Hybrid Architecture

1. **Lexical retrieval** (BM25 via Elasticsearch/OpenSearch): Handles exact keyword matches, entity names, product codes.
2. **Dense retrieval** (bi-encoder + ANN via FAISS/HNSW): Handles semantic intent, synonyms, related concepts.
3. **Graph expansion** (optional): Ontology-based query expansion for structured domains.
4. **Fusion**: RRF or learned fusion merges ranked lists.
5. **Re-ranking**: Cross-encoder or LLM-based reranker for the top-N candidates.

Eugene Yan's experience with hybrid RAG retrieval: combining BM25 (OpenSearch) with semantic search (e5-small-v2) consistently outperformed either alone. BM25 handles person names, acronyms ("RAG", "RLHF"), and exact IDs. Semantic handles paraphrases and domain concepts.

## Multimodal Search (Video/Image)

YouTube-style video search combines two parallel retrieval paths:

- **Text search**: Inverted index over video titles, descriptions, and tags. Elasticsearch/Lucene handles this out of the box.
- **Visual search**: Two-tower model with a video encoder (CNN or frame-level transformers for visual content) and a text encoder. Similarity by dot product of embeddings. ANN index over all video embeddings.
- **Fusion layer**: Combine ranked lists from text and visual paths.
- **Re-ranking**: Personalization signals, engagement signals (watch time, CTR, completion rate).

Text normalization pipeline for search: raw text → normalize (lowercase, remove accents, expand contractions) → tokenize → token IDs (via lookup table or hashing for OOV tokens).

## Key Evaluation Metrics

| Metric | What It Measures | When to Use |
|--------|-----------------|-------------|
| **Precision@k** | Fraction of top-k results that are relevant | When all top results matter |
| **Recall@k** | Fraction of relevant docs in top-k | Candidate generation quality |
| **MRR** | Mean reciprocal rank of first relevant result | Single-answer search |
| **MAP** | Mean Average Precision across queries | Ranked list quality |
| **NDCG** | Graded relevance with position discount | When relevance is graded |
| **CTR / Watch Time** | Downstream engagement | Online A/B test |

For most candidate generation systems, **Recall@k** is the primary offline metric — the retrieval stage's job is to not miss relevant items; the ranking stage handles precision.

## Architecture Principle: Start Lexical, Add Semantic

Eugene Yan's heuristic: "If you're building a search system from scratch, start with lexical (Elasticsearch/Lucene). They work out of the box. When you hit diminishing returns — especially on long-tail queries — augment with self-supervised query embeddings." Graph-based expansion is highest effort and most appropriate for structured product/food domains where the ontology is well-defined.

The practical progression: BM25 baseline → add embedding retrieval → add hybrid fusion → fine-tune embedding model on domain-specific click/purchase data.

## Sources

- Aman.ai: [Recommendation Systems — Search](https://aman.ai/recsys/search/)
- Eugene Yan: [Search: Query Matching via Lexical, Graph, and Embedding Methods](https://eugeneyan.com/writing/search-query-matching/)
- Aman.ai: [Chapter 2 — YouTube Video Search](https://aman.ai/h/des/youtube-video-search/)
