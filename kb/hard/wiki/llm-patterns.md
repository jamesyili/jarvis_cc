---
concept: LLM Patterns for Products
tags: [llm-patterns, guardrails, caching, defensive-ux, feedback-collection]
sources:
  - kb/hard/raw/eugene-yan/patterns-for-building-llm-based-systems-products.md
last_compiled: 2026-04-05
related: [genai-platform, llm-evaluation, retrieval-augmented-generation]
understanding: 2  # basic understanding (assumed where James's background applies)
relevance: 2  # somewhat / potentially relevant
knowledge_updated: 2026-09-07
---

# LLM Patterns for Products

Building an LLM demo is easy. Building an LLM _product_ is hard. The gap between the two is the same gap Karpathy identified with self-driving: "It's easy to demo a car driving around a block, but making it a product takes a decade." Seven patterns bridge that gap — organized along two axes: closer to the data vs. closer to the user, and improving performance vs. reducing cost/risk.

## The Seven Patterns

| Pattern | Purpose | Axis |
|---------|---------|------|
| **Evals** | Measure performance | Data-side, offensive |
| **RAG** | Add fresh/external knowledge | Data-side, offensive |
| **Fine-tuning** | Task-specific capability | Data-side, offensive |
| **Caching** | Reduce latency & cost | Data-side, defensive |
| **Guardrails** | Ensure output quality | User-side, defensive |
| **Defensive UX** | Anticipate & handle errors | User-side, defensive |
| **Collect user feedback** | Build the data flywheel | User-side, both |

---

## 1. Evals: Build These First

> "How important evals are to the team is a major differentiator between folks rushing out hot garbage and those seriously building products in the space." — HackerNews

Evals are the foundation. Without them, every model or prompt change is a guess. Think of it as **Eval Driven Development (EDD)**: collect task-specific examples (prompt, context, expected output), run them on every change, measure improvements and regressions.

### The Metrics Problem

Classic NLP metrics — BLEU, ROUGE — have known limitations. They're reference-based (require gold outputs), don't account for paraphrasing, and correlate poorly with human judgment on open-ended tasks. BLEU has even shown _negative_ correlation with human fluency ratings.

Practical metric selection:

- **Classification/extraction tasks**: Standard precision, recall, F1, AUC. These work.
- **Tasks with reference outputs** (translation, extractive summarization): BLEU, ROUGE, or BERTScore (uses cosine similarity between contextual embeddings — handles synonyms).
- **Open-ended generation** (summarization, dialogue, Q&A): LLM-as-judge.

### LLM-as-Judge

**G-Eval**: Provide a strong LLM (GPT-4) with evaluation criteria, let it chain-of-thought through evaluation steps, then score. GPT-4 as evaluator achieves Spearman 0.514 correlation with human judgments — outperforming all prior automated metrics.

Known biases to mitigate:
- **Position bias**: LLMs favor the first option. Swap order, run twice; count only consistent wins.
- **Verbosity bias**: LLMs prefer longer responses. Normalize length.
- **Self-enhancement bias**: Don't use the same LLM to judge its own outputs. GPT-4 self-favors at +10%, Claude at +25%.

When in doubt: **vibe check wins**. Having a set of 10-20 representative prompts that you manually scan during training is often more valuable than any automated metric. Real prompt: "suggest games for a 3-year-old and a 7-year-old to play" — watching how the answer changes as the model trains tells you more than MMLU.

---

## 2. RAG: To Add Knowledge

RAG (Retrieval-Augmented Generation) fetches relevant external context and injects it into the LLM's input. Key benefits:
- Reduces hallucination by grounding generation on retrieved facts.
- Cheaper to update a retrieval index than to retrain/fine-tune an LLM.
- Easier to delete/correct data (update the index) than to unlearn weights.

Hybrid retrieval outperforms pure embedding search:
- **BM25** handles exact tokens: names, acronyms, IDs ("RAG", "gpt-3.5-turbo", "Kaptir 2.0").
- **Semantic search** (bi-encoder + ANN) handles paraphrases and conceptual matches.
- Combine via RRF or learned reranker.

On embedding models: FastText for quick POCs; sentence-transformers (BERT/RoBERTa-based) for solid baselines; E5 or GTE family for top retrieval performance. The `query:` / `passage:` prefix convention for asymmetric retrieval tasks helps instruction-tuned models. See [[hard/wiki/approximate-nearest-neighbor|ANN Search]] for indexing strategies.

---

## 3. Fine-Tuning: To Get Better at Specific Tasks

Fine-tuning is warranted when:
- Off-the-shelf models underperform on your specific task.
- You need consistent format/tone that prompt engineering alone can't guarantee.
- You want to reduce latency/cost by distilling a large model into a smaller specialized one.
- You have proprietary data that shouldn't leave your environment.

Fine-tuning flavors:
- **Continued pre-training**: Domain-specific MLM or next-token prediction on unlabeled domain corpus.
- **Instruction fine-tuning**: Supervised on (instruction, output) pairs — teaches the model to follow instructions.
- **Single-task fine-tuning**: Narrow specialization (toxicity detection, classification, extraction).
- **RLHF**: Preference learning via reward model + PPO — aligns generation with human preferences.

Efficient fine-tuning: **LoRA** and **QLoRA** are the practical defaults. LoRA trains low-rank adapter matrices (0.1% of parameters) — achieves near-full-fine-tuning performance with much lower memory. QLoRA extends this with 4-bit quantization: fine-tune a 65B model in 48GB GPU RAM vs. >780GB.

Alignment tax: fine-tuning on one task can reduce performance on others. Modular smaller specialized models often beat one large all-in-one model.

---

## 4. Caching: To Reduce Latency and Cost

Cache LLM responses keyed on the _embedding_ of the input request. Future semantically similar requests are served from cache.

Practical implementation (GPTCache pattern):
1. Embed incoming request.
2. Check similarity against cached request embeddings (FAISS, Hnswlib).
3. If similarity exceeds threshold: serve cached response.
4. If not: call LLM, cache response and embedding.

**When caching works**: Power-law request distributions where a small number of popular queries drive most traffic (search queries, product summaries, FAQ answers). Cache hit rate is the key metric.

**When to be careful**: Semantic caching on free-form NL input can serve wrong responses. "Mission Impossible 2" and "Mission Impossible 3" might be semantically similar enough to cross the threshold, but serve the wrong answer. Better caching strategies:
- **Item ID-based**: Pre-compute summaries per product/entity and serve by ID.
- **Pair-based**: Comparison tables between two known items.
- **Constrained input**: Structured options (dropdowns, filters) with pre-computed responses.

Pre-computing offline (batch mode) shifts generation cost to asynchronous and reduces real-time API calls — best of both worlds for high-traffic use cases.

---

## 5. Guardrails: To Ensure Output Quality

Guardrails validate LLM output before serving it. Categories:

**Structural guidance**: Use constrained generation (Microsoft Guidance, Outlines, SGLang) to enforce output schema directly — inject structural tokens rather than hoping the LLM gets JSON right.

**Syntactic guardrails**: Categorical output within valid choices; numeric output within expected ranges; SQL/Python syntax validation; URL reachability checks.

**Semantic/factuality guardrails**: Verify the output is grounded in retrieved context. Use cosine similarity or fuzzy matching between output and source documents, or use an LLM to verify factual consistency (SelfCheckGPT: if multiple independent completions disagree, the original is likely hallucination).

**Content safety guardrails**: Check for inappropriate/harmful content. Simple: blocklist matching. Complex: dedicated moderation classifier or LLM evaluator (NeMo-Guardrails approach).

**Input guardrails**: Reject or sanitize adversarial or out-of-scope inputs before they reach the primary model. Midjourney's NSFW blocking is an example.

Implementation order: Start with syntactic (deterministic, cheap). Add semantic when factuality matters. Add content safety when user-generated input or harmful output is a risk.

---

## 6. Defensive UX: To Anticipate Errors Gracefully

LLMs produce variable, sometimes wrong output. Defensive UX accepts this as a constraint and designs around it.

**Set right expectations**: Add disclaimers. Google Bard, ChatGPT's landing page — both make limitations visible upfront. Short-term trust reduction, long-term trust building.

**Efficient dismissal**: Let users easily ignore AI output (GitHub Copilot: just keep typing). An AI feature that can't be dismissed becomes a nuisance.

**Attribution**: Cite sources (BingChat style). Allows users to verify, calibrate trust, and understand provenance. Apple's "Because you've read non-fiction" — shows why, not just what.

**Anchor on familiarity**: Don't introduce exotic UX alongside AI. Users should focus on the task, not on learning a new interface. Chat is not always the right UX — it demands high user effort and raises expectations proportionally. Prefer constrained, familiar UI patterns.

**On chat UX**: Chat offers flexibility but requires more user effort, lacks signifiers for how to adjust outputs, and has no consistent "shape." Most users prefer clicking > typing. Chat should be a secondary option, not the primary interaction pattern, unless the task genuinely requires free-form dialogue.

---

## 7. Collect User Feedback: Build the Data Flywheel

Data — specifically human preference data — is one of the few durable moats in LLM products. Collecting it deliberately drives compounding improvement.

**Explicit feedback**:
- Thumbs up/down (ChatGPT): Direct preference signal for RLHF.
- Regenerate response: Strong negative signal.
- Midjourney's U/V buttons: Upscale (strong positive), Variation (positive), New set (negative) — rich comparison data.

**Implicit feedback**:
- Accept code suggestion in full (Copilot) = strong positive.
- Accept and edit = positive.
- Ignore or delete = negative.
- Modifying the prompt that generated code = negative signal on the generation.

Feedback signals feed directly into: eval datasets, fine-tuning datasets, reward model training, and guardrail development. The longer you delay building this pipeline, the longer your competitor's flywheel spins without you.

---

## Pattern Selection Guide

| Problem | Primary Pattern |
|---------|----------------|
| Don't know if system is improving | **Evals** first |
| Hallucination / outdated knowledge | **RAG** |
| Model doesn't behave as required | **Fine-tuning** or prompt engineering first |
| Latency or API cost too high | **Caching** |
| Malformed, harmful, or wrong outputs | **Guardrails** |
| Users confused or losing trust | **Defensive UX** |
| Improving over time | **User feedback collection** |

These patterns are complementary, not exclusive. Production LLM systems typically implement all seven — the question is sequencing. Start with evals (you can't improve what you can't measure), add RAG early if freshness or factuality matters, build guardrails before public launch, and design the feedback collection loop into the UX from day one.

## Sources

- Eugene Yan: [Patterns for Building LLM-based Systems & Products](https://eugeneyan.com/writing/llm-patterns/)
