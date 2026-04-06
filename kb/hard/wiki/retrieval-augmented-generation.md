---
concept: Retrieval-Augmented Generation (RAG)
tags: [rag, retrieval, generation, llm, knowledge-grounding, chunking, hybrid-search, agentic-rag]
sources:
  - kb/hard/raw/aman-ai/primers-retrieval-augmented-generation.md
  - kb/hard/raw/aman-ai/primers-personalizing-large-language-models.md
  - kb/hard/raw/aman-ai/deep-research.md
  - kb/hard/raw/chip-huyen/building-a-generative-ai-platform.md
  - kb/hard/raw/eugene-yan/obsidian-copilot-an-assistant-for-writing-reflecting.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/embeddings-and-representation-learning|Embeddings and Representation Learning]]"
  - "[[hard/wiki/two-tower-retrieval|Two-Tower Retrieval]]"
  - "[[hard/wiki/transformer-architecture|Transformer Architecture]]"
  - "[[hard/wiki/ai-agents-and-agentic-systems|AI Agents and Agentic Systems]]"
  - "[[hard/wiki/llm-evaluation|LLM Evaluation]]"
---

# Retrieval-Augmented Generation (RAG)

RAG, introduced by Lewis et al. (2020), enhances LLM outputs by conditioning generation on externally retrieved evidence rather than relying solely on parametric (weight-baked) knowledge. It directly addresses three failure modes: **knowledge cutoff** (static training data), **hallucination** (confident confabulation on unknown facts), and **domain specificity** (models not trained on proprietary corpora). RAG also supports dynamic corpora — new or updated documents are reflected immediately through the retriever, requiring no retraining.

---

## Core Architecture: Indexing → Retrieval → Generation

**Indexing (offline).** Source documents are loaded, split into chunks, and each chunk is encoded into an embedding vector stored in a vector index (or inverted index for BM25). The quality of this step sets the ceiling for everything downstream.

**Retrieval (online).** At inference time, the user query is embedded (or tokenized for sparse retrieval) and the index is searched for the top-k most relevant chunks. These chunks are then passed as context to the LLM.

**Generation.** The LLM receives `[retrieved context] + [user query]` as its prompt and generates a grounded response. Because the model is conditioned on retrieved evidence, it has less need to rely on its own (potentially stale or incorrect) parametric knowledge.

---

## Chunking Strategies

Chunk size controls the precision–context trade-off: smaller chunks retrieve more precisely but lose surrounding context; larger chunks preserve context but introduce noise.

| Strategy | How it works | Best for |
|---|---|---|
| **Fixed-size** | Split by token count, with optional overlap | Simple baseline, low cost |
| **Sentence splitting** | Split at sentence boundaries (NLTK, spaCy) | Sentence-level embedding models |
| **Recursive** | Hierarchically apply multiple separators (LangChain `RecursiveCharacterTextSplitter`) | General-purpose text |
| **Structure-aware** | Respect markdown/HTML/LaTeX structure | Formatted documents |
| **Semantic chunking** | Group sentences by cosine similarity — split when similarity drops | Topically coherent retrieval |
| **Late chunking** | Embed the full document first, then pool into chunks — preserves cross-chunk context | Long-context models (JinaAI) |
| **Auto-merging** | Hierarchical chunks: merge small chunks into parent if enough retrieve the same parent | Reducing fragmentation |

**Late chunking vs. naive:** Naive chunking loses inter-chunk context (e.g., "she" can't resolve back to "Alice" in a prior chunk). Late chunking delays the split until after full-document embedding, preserving contextual relationships with the same storage cost. Late interaction (ColBERT) goes further — token-level MaxSim scoring for highest precision, but at ~500x the storage cost of naive chunking.

---

## Retrieval Approaches

### Lexical (Sparse) Retrieval
BM25 is the industry default sparse retrieval function. It improves on TF-IDF by adding term saturation (diminishing returns for repeated terms) and document-length normalization. It is sub-millisecond, deterministic, and fully interpretable. It excels at exact matches — identifiers, SKUs, medical codes, proper nouns — but fails on synonym and paraphrase queries.

### Semantic (Dense) Retrieval
Queries and documents are encoded into dense vectors (typically via sentence transformers / bi-encoders). Retrieval becomes approximate nearest-neighbor (ANN) search using FAISS, HNSW, ScaNN, or ANNOY. Dense retrieval handles paraphrase, synonymy, and natural language questions well but has higher compute cost and degrades on rare or newly introduced terms. Document embeddings must be recomputed when the model is updated.

**Contextual retrieval (Anthropic).** Prepend a model-generated chunk summary ("This chunk is from Q3 earnings call discussing APAC revenue") to each chunk before embedding. Reduces failed retrievals by 49%; combined with reranking, by 67%.

### Hybrid Retrieval
The dominant production pattern: BM25 retrieves a high-recall candidate set (k ≈ 100–1000), then a semantic model reranks the candidates. This ensures exact facts are never missed (lexical anchor) while also capturing implied intent (semantic precision).

**Score fusion alternatives:**
- *Linear fusion:* `score = α·BM25 + (1-α)·semantic_sim` — requires score normalization and tuning α.
- *Reciprocal Rank Fusion (RRF):* `RRF(d) = Σ 1/(k + rank_i(d))` where k=60. Rank-based, calibration-free, robust — the most common production choice.

**Reranking.** Cross-encoders (e.g., MonoT5, MonoBERT) attend over the concatenated query+document and produce a high-precision relevance score. Used on the top-50 to top-200 candidates; too expensive for full-corpus scoring.

---

## Advanced RAG

**Query rewriting.** Conversational queries like "How about his wife?" are ambiguous. A small model rewrites the query to be self-contained before retrieval ("When did Emily Doe last purchase from us?"). Critical for multi-turn chatbots.

**HyDE (Hypothetical Document Embeddings).** Instead of embedding the query directly, prompt the LLM to generate a *hypothetical* answer document, embed that, and use it for retrieval. The synthetic document lives in the same embedding space as real documents, dramatically improving zero-shot dense retrieval performance. Risk: the hypothetical document can hallucinate, biasing retrieval.

**Multi-hop RAG.** Some questions require chaining retrievals — retrieve intermediate facts, use them to formulate subsequent queries, repeat. Standard single-shot RAG fails here because intermediate facts don't appear directly relevant to the original question. Multi-hop pipelines formalize retrieval as a planning problem: decompose into sub-queries Q₁→Q₂→…→Qₙ, where each Qᵢ depends on the answer to Qᵢ₋₁.

**Iterative / FLARE.** Re-query the knowledge base mid-generation whenever the model's token confidence drops below a threshold. Bridges the gap between upfront retrieval and the model's need for information it discovers it needs during generation.

**Metadata filtering.** Apply hard filters (access control, document type, recency) before retrieval. Not a scoring feature — a constraint. Prevents data leakage, compliance violations, and stale results surfacing before semantic retrieval runs.

---

## Evaluation

RAG evaluation has two layers: retrieval quality and generation quality.

**Retrieval metrics:**
- *Context precision* — are the retrieved chunks ranked by relevance? (relevant chunks surfaced early)
- *Context recall* — are all facts needed to answer the question present in the retrieved set?
- *Context relevance* — do retrieved chunks actually address the query?

**Generation metrics:**
- *Faithfulness / groundedness* — are all claims in the response inferable from the retrieved context? (measures hallucination)
- *Answer relevance* — does the response address the original question?
- *BLEU / ROUGE / exact match* — string-overlap metrics; useful for factoid Q&A, weak for open-ended generation.

**RAGAS** (automated evaluation library) operationalizes these without requiring labeled data — only a few questions (plus reference answers for recall). The harmonic mean of faithfulness, answer relevance, context precision, and context recall is the RAGAS score.

---

## Production Considerations

**Latency.** Hybrid retrieval latency is additive: `T_total = T_filter + T_lexical + T_semantic + T_rerank`. Common optimizations: cache frequent query embeddings; apply reranker only to top-50 (not top-500); use query classifiers to skip semantic stages for identifier-heavy queries.

**Index freshness.** With BM25, adding documents is cheap (update inverted index). With dense retrieval, document embeddings must be recomputed on corpus changes and when the embedding model is updated. This creates a versioning problem: embedding model and index must stay in sync.

**Choosing k.** k controls recall vs. downstream cost. Rule of thumb: if a document doesn't appear in the top-k lexical candidates, the semantic reranker cannot recover it. Default: k ∈ [200, 500] for general-purpose RAG.

**Long context vs. RAG.** A 10M-token context window for 100k-document corpora requires ~32 H100 GPUs and exceeds $100/hour in inference costs. The KV cache alone can exceed 1TB of VRAM. RAG remains the cost-efficient answer for large corpora. Additionally, LLMs exhibit the *lost-in-the-middle* effect — information buried in the center of a long context is less reliably attended to — making retrieval-first architectures more reliable even when long context is technically feasible.

---

## RAG vs. Fine-Tuning vs. Long Context

| Approach | What it changes | When to use |
|---|---|---|
| **Prompt engineering** | Nothing — static in-context examples | Rapid prototyping, grounding open-ended conversations |
| **RAG** | What information the model sees at inference time | Dynamic corpora, limited labeled data, need for traceability |
| **Fine-tuning / PEFT** | The model's weights | Style, tone, task-specific behavior; requires labeled data + compute |
| **Long context** | The model's attention window | Small-to-medium corpora, infrequent queries; high inference cost |

**Practical rule:** Start with RAG. Once the retrieval pipeline works, add fine-tuning to improve linguistic style and vocabulary. RAG cannot adapt a model's voice; fine-tuning cannot give it fresh external knowledge. They are complementary.

---

## Agentic RAG

In agentic RAG, retrieval becomes one tool among many that an LLM agent can invoke. The agent decides *whether* to retrieve, *which* source to query (vector DB, SQL, web search, API), and *how many times* to iterate.

**Single-agent (router).** A single agent acts as a router, selecting the best retrieval tool per query. Handles queries that span multiple data sources.

**Multi-agent.** A master orchestrator coordinates specialized sub-agents: internal DB agent, personal data agent, public web agent. Enables comprehensive responses across heterogeneous data channels.

**Capabilities beyond retrieval.** Agentic RAG systems can also: validate retrieved facts by cross-referencing sources, perform multi-step reasoning before generation, update memory with user preferences, and execute write actions (with appropriate guardrails).

**Deep Research pattern.** Production agentic research systems (e.g., Anthropic's deep research) decompose the user query with a planner/lead-researcher, spawn parallel sub-agents for different aspects, collect evidence with citations, and synthesize. The agent decides retrieval strategy dynamically, making iterative multi-hop retrieval tractable at scale. See [[hard/wiki/ai-agents-and-agentic-systems|AI Agents and Agentic Systems]] for orchestration patterns.

---

## Sources

- `kb/hard/raw/aman-ai/primers-retrieval-augmented-generation.md` — primary source; comprehensive coverage of chunking, retrieval, hybrid search, HyDE, multi-hop, agentic RAG, evaluation
- `kb/hard/raw/aman-ai/primers-personalizing-large-language-models.md` — RAG vs. fine-tuning vs. prompt engineering comparison
- `kb/hard/raw/aman-ai/deep-research.md` — agentic RAG in production (multi-agent deep research architecture)
- `kb/hard/raw/chip-huyen/building-a-generative-ai-platform.md` — platform framing; query rewriting, context construction, agentic RAG, production trade-offs
- `kb/hard/raw/eugene-yan/obsidian-copilot-an-assistant-for-writing-reflecting.md` — applied RAG for personal knowledge base writing (minimal RAG-specific content)
