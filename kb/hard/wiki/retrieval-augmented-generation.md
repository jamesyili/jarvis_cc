---
concept: Retrieval-Augmented Generation
tags: [rag, retrieval, generation, llm, chunking]
sources:
  - kb/hard/raw/aman-ai/chapter-6-retrieval-augmented-generation.md
  - kb/hard/raw/chip-huyen/building-a-generative-ai-platform.md
  - kb/hard/raw/lilian-weng/how-to-build-an-open-domain-question-answering-system.md
  - kb/hard/raw/jay-alammar/the-illustrated-retrieval-transformer.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/embeddings-and-representation-learning|Embeddings & Representation Learning]]"
  - "[[hard/wiki/large-language-models|Large Language Models]]"
  - "[[hard/wiki/ai-agents-and-agentic-systems|AI Agents & Agentic Systems]]"
understanding: 2  # basic understanding (assumed where James's background applies)
relevance: 2  # somewhat / potentially relevant
knowledge_updated: 2026-09-07
---

# Retrieval-Augmented Generation

Retrieval-Augmented Generation (RAG) combines a retrieval system with a generative language model, grounding responses in external documents rather than relying on parametric knowledge baked into model weights. The motivation is fundamental: LLMs have training cutoffs, encode world knowledge inefficiently in parameters, and hallucinate when queried about facts outside training data. RAG addresses all three by making knowledge retrieval a first-class component of inference.

DeepMind's RETRO transformer illustrated the core insight clearly — a 7.5B parameter model matching GPT-3 (175B) by retrieving from a 2-trillion-token database at generation time. Language structure lives efficiently in parameters; factual world knowledge is better stored externally and fetched on demand.

## The Core Pipeline

RAG has two phases — offline indexing and online inference.

**Offline indexing:** Documents are parsed (using rule-based or AI-based parsers for PDFs), chunked into manageable pieces, encoded into embedding vectors by a text encoder (BERT, sentence-transformers, or proprietary models), and stored in a vector database. For multimodal documents, image encoders (CLIP) produce embeddings in a shared text-image space.

**Online inference:** Given a user query, the system (1) encodes the query with the same encoder, (2) performs nearest-neighbor search against indexed vectors, (3) retrieves top-k chunks, (4) assembles a prompt combining query and retrieved context, and (5) generates a response via an LLM.

The retrieval component is the same backbone powering search engines and recommender systems — RAG borrows that machinery directly.

## Chunking Strategies

Chunking decisions have outsized impact on retrieval quality. Key options:

- **Length-based:** Fixed character or token windows with overlap. Simple but can split sentences mid-thought. LangChain's `RecursiveCharacterTextSplitter` handles this with adjustable chunk sizes and separators.
- **Semantic/structural:** Split on document structure — headers, paragraph breaks, code blocks. Preserves logical units. MarkdownHeaderTextSplitter, HTMLHeaderTextSplitter.
- **Sliding window:** Overlapping windows reduce boundary artifacts. Research shows 100-word passages with overlap outperform non-overlapping splits.

The right chunk size balances a tension: too large and the embedding loses specificity; too small and individual chunks lack sufficient context for generation. A common production heuristic: 500–1000 tokens per chunk, 10–20% overlap. At scale, a 5M-page corpus at 3 text chunks and 3 image chunks per page yields ~40M indexed chunks — a scale where ANN algorithms are essential.

## Retrieval Methods

### Sparse (Term-Based)
TF-IDF and BM25 are classical baselines — fast, no GPU required, strong out of the box for lexical matching. Elasticsearch implements BM25 at production scale. Key limitation: no semantic understanding. "Doctor" and "physician" are treated as unrelated terms.

### Dense (Embedding-Based)
Query and documents are encoded into shared vector spaces; similarity is measured by cosine or dot-product distance. Enables semantic retrieval — finding relevant chunks even when vocabulary doesn't overlap. Dense Passage Retrieval (DPR) pioneered this for open-domain QA, using BERT to encode questions and passages independently.

Approximate Nearest Neighbor (ANN) makes dense retrieval practical at scale. See [[hard/wiki/approximate-nearest-neighbor|Approximate Nearest Neighbor]] for algorithms. In brief:
- **LSH:** Hash similar vectors into the same bucket
- **Clustering-based (FAISS):** IVF — search only within nearest centroid's cluster
- **Graph-based (HNSW):** State-of-the-art recall/latency tradeoff

Time complexity drops from O(N×D) exact search to O(log N) for ANN. FAISS (Meta), ScaNN (Google), and Elasticsearch all provide production-grade ANN backends.

### Hybrid Search
Production systems combine sparse and dense. A common sequential pattern: BM25 retrieves a broad candidate set; vector search re-ranks for semantic relevance. Another pattern is ensemble — multiple retrievers score independently, then rankings are combined. Both preserve speed while improving recall on semantically complex queries.

## Reranking

Retrieved chunks are ordered by embedding similarity, not by quality of answer. A dedicated cross-encoder reranker — processing query and chunk jointly — significantly improves precision at the cost of additional latency. "Lost in the Middle" (Liu et al., 2023) research shows models attend better to content at the beginning and end of context, so ordering of retrieved chunks matters even after inclusion.

## Advanced RAG Techniques

**Query rewriting:** User queries are often ambiguous or context-dependent. A lightweight LLM call rewrites before retrieval — resolving coreference, decomposing compound questions, and adding context. Example: "How about Emily Doe?" → "When did Emily Doe last purchase from us?"

**HyDE (Hypothetical Document Embeddings):** Generate a hypothetical answer to the query, embed that answer, use it as the retrieval query. The hypothesis is often geometrically closer to target documents than the raw question embedding.

**Multi-hop retrieval:** For questions requiring synthesis across multiple documents, retrieve iteratively — first-pass results inform a refined query for a second pass.

**RAG with structured data (Text-to-SQL):** External data can be tabular. The LLM generates SQL from natural language, executes it, and uses results as context for generation.

**RAFT (Retrieval-Augmented Fine-Tuning):** Fine-tunes the LLM to prioritize golden retrieved documents while ignoring distractor chunks. Addresses noisy retrieval degrading generation — the model learns to distinguish relevant from irrelevant context.

## RAG vs. Fine-Tuning vs. Long Context

Three approaches address grounding LLM responses in domain knowledge:

| Approach | Pros | Cons |
|---|---|---|
| RAG | Dynamic, updatable, cites sources, scalable | Retrieval latency, chunking brittleness |
| Fine-tuning | Deep domain adaptation, no retrieval cost | Expensive to retrain, knowledge becomes stale, no citations |
| Long context | Simple architecture | Expensive per query, "lost in the middle" degradation, still needs document curation |

RAG is optimal when knowledge changes frequently, scale is large, and source citations matter. Fine-tuning adds value when the LLM generates poor responses even with good retrieval context. Long context windows complement RAG for short corpora or when retrieval latency is unacceptable. For most production enterprise use cases, RAG is the default starting point.

## Evaluation

RAG evaluation decomposes into a triad of axes:

- **Context relevance:** Did the retriever fetch the right chunks? Metrics: Hit rate, MRR, NDCG, Precision@k.
- **Faithfulness:** Does the generated response stay grounded in retrieved context, or does it hallucinate? Methods: automated fact-checkers (SelfCheckGPT, SAFE), consistency checks, human review.
- **Answer relevance/correctness:** Does the response answer the question? Does it match the reference? Metrics: BLEU, ROUGE, METEOR; increasingly LLM-as-judge for semantic quality.

A RAG system can fail at any stage. Poor chunking degrades retrieval; poor retrieval makes accurate generation impossible; good retrieval can still be ignored by a poorly prompted LLM.

## Agentic RAG

When retrieval becomes a conditional decision — not always triggered, invoked based on the query — RAG becomes agentic. The LLM decides whether to search the web, query a vector store, execute SQL, or generate directly. Each retrieval action is a tool call. This architecture powers systems like Perplexity.ai. The model treats information sources as its environment to perceive and act upon — connecting directly to [[hard/wiki/ai-agents-and-agentic-systems|AI Agents & Agentic Systems]].

## Sources

- Aman Chadha. *Chapter 6: Retrieval-Augmented Generation* — production ChatPDF design, chunking strategies, ANN categories, evaluation triad
- Chip Huyen. *Building a Generative AI Platform* — RAG as context construction, hybrid search, query rewriting, agentic RAG, semantic caching
- Lilian Weng. *How to Build an Open-Domain Question Answering System* — retriever-reader framework history, DPR, BM25, dense vs. sparse evolution, end-to-end joint training
- Jay Alammar. *The Illustrated Retrieval Transformer* — RETRO architecture, key-value retrieval database, chunked cross-attention, separating language from world knowledge
