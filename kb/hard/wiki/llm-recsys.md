---
concept: LLMs in Recommendation Systems
tags: [llm-recsys, semantic-ids, generative-recommendation, bert4rec, hstu]
sources:
  - kb/hard/raw/louis-wang/generative-recommendation-in-production-hstu-onerec-and-what-every-major-platfor.md
  - kb/hard/raw/louis-wang/two-bets-on-generative-recommendation-semantic-ids-vs-fine-tuned-llms.md
  - kb/hard/raw/aman-ai/recommendation-systems-llm.md
last_compiled: 2026-04-05
related: [recommendation-systems, large-language-models, two-tower-retrieval]
understanding: 2  # basic understanding (assumed where James's background applies)
relevance: 3  # very relevant
knowledge_updated: 2026-09-07
---

# LLMs in Recommendation Systems

For two decades, recommendation systems followed a two-stage blueprint: lightweight retrieval narrows millions of items to hundreds, then a heavy ranker scores them. LLMs are now breaking that blueprint — first by enhancing specific stages, then by replacing them, and most recently by collapsing the entire pipeline into a single generative model.

## Why the Two-Stage Pipeline Has Limits

The classic retrieve-then-rank funnel has structural constraints that LLMs address:

**The retrieval bottleneck**: retrieval models must be simple enough to run at massive scale. Long user histories, nuanced context, and fine-grained item features are typically dropped. If the right item isn't retrieved, the ranker can never surface it.

**Stage inconsistency**: retrieval optimizes for recall; ranking optimizes for precision. They're trained on different objectives with different feature sets and no joint signal.

**Static representations**: items are indexed as fixed embeddings computed offline. The model can't adapt to a user's evolving context at inference time, and long-tail items with sparse interaction histories get weak embeddings.

## The Semantic ID Breakthrough

Before LLM-based generation can work, items need to be representable as tokens that a generative model can predict. Numeric item IDs carry no semantic information — the model can't infer that item #4,821,033 is related to item #4,821,034.

**Semantic IDs** solve this with **RQ-VAE (Residual Quantized Variational AutoEncoder)**: an item's embedding is quantized through multiple rounds, each round encoding the residual from the previous. The result is a short sequence of tokens (typically 3–8) where the first token captures broad category, each subsequent token encodes finer detail.

```
Item embedding → VQ Round 1 → C₁ (sports)
                residual ε₁ → VQ Round 2 → C₂ (basketball)
                residual ε₂ → VQ Round 3 → C₃ (NBA highlights)
```

Semantically similar items share code prefixes. A model generating `[sports, basketball, ...]` can generalize to recommend related items it's never seen in training. This is the key property that makes generative retrieval tractable.

LinkedIn found a related insight on the feature encoding side: raw engagement counts like "4,382 likes" are largely meaningless to LLM encoders. Converting them to percentile buckets in special tokens produced a 30× increase in correlation between popularity features and item embeddings.

## Paradigm A: Semantic ID Autoregressive Models

The first paradigm trains an autoregressive transformer to predict the token sequence of the next item, given the user's interaction history. Recommendation becomes structurally identical to next-token prediction in language modeling.

**Meta HSTU** (Hierarchical Sequential Transduction Units, ICML 2024) powers Reels at billion-user scale. Three architectural choices make it work:

- **Hierarchical temporal encoding**: separates short-term signals (last minute) from long-term context (last month) without conflating them
- **Relative position biases**: learned biases replace absolute positional encodings to handle recommendation's temporal structure
- **Linear-complexity attention**: user histories span thousands of interactions; standard attention is O(n²); HSTU uses a linear approximation

**Kuaishou OneRec** (2025) takes this further, collapsing retrieval and ranking into a single autoregressive model that generates an ordered recommendation list directly. OneRec V2 added two-stage codebook learning (content codes first, then behavioral fine-tuning), beam search decoding over a prefix trie, and constrained decoding to prevent generating invalid item codes.

**Alibaba TIGER** (NeurIPS 2023) applied generative retrieval to e-commerce, incorporating structured item attributes (category, price tier, brand) directly into the RQ-VAE codebook objective. Products sharing category and price range cluster in the same code region, enabling cross-sell and substitute recommendations for unseen items.

**Trade-offs**: autoregressive decoding over a small vocabulary (256–4096 codes per codebook, 3–8 rounds) with a prefix trie is fast. HSTU and OneRec serve at millisecond latencies at billion-user scale. But a new item requires updating the codebook and re-indexing — brittle for platforms with continuous item churn.

## Paradigm B: Fine-Tuned LLMs for Recommendation

The second paradigm takes a pretrained LLM — already trained on vast text — and fine-tunes it on interaction data. The bet: world knowledge transfers to recommendation. A model that understands what "NBA highlights" and "basketball game recap" are can reason about item similarity without interaction data.

**Fine-tuning strategies:**

- **Continued Pre-Training (CPT)**: train the LLM on sequences of user interactions formatted as text, teaching it the platform's behavioral patterns on top of its world knowledge
- **Instruction tuning**: frame the recommendation as a prompt-completion pair: "Given this user's history: [titles], recommend: [target]"
- **Preference alignment**: extend with RLHF-style training on (recommended, rejected) item pairs

**Production systems:**

**Google PLUM** (2024) adapts Gemini for YouTube Shorts via CPT on watch sequences. Critically, PLUM represents items as RQ-VAE semantic codes rather than text titles — borrowing the first paradigm's vocabulary. In live A/B testing: +4.96% CTR, with gains concentrated on cold-start scenarios where collaborative filtering has no signal.

**Alibaba LUM** (Large User Model, 2026) takes the feature injection path. A 7B parameter LLM runs offline, pre-trained on tokenized behavior sequences. Its output representations are cached and injected as supplementary features into the existing DLRM ranker. The LLM never runs at serving time. Result: +2.9% CTR on Taobao, with power-law scaling improvements up to 7B parameters.

**P5** (EMNLP 2022) established the paradigm by unifying five recommendation tasks — rating prediction, sequential recommendation, explanation generation, review summarization, direct recommendation — as a single T5 text-to-text problem.

## BERT4Rec and SASRec

Before the generative wave, transformer-based sequential recommenders were already advancing the field:

**BERT4Rec**: adapts BERT's masked language modeling objective to recommendation. Items in a user's interaction sequence are randomly masked; the model is trained to predict them using bidirectional context. Captures both past and future interactions, unlike unidirectional RNN-based approaches.

**SASRec** (Self-Attentive Sequential Recommendation): a GPT-style unidirectional transformer over interaction sequences. Standard strong baseline for sequential recommendation benchmarks. In head-to-head comparisons, ByteDance's HLLM improved Recall@5 from 5.142 (SASRec) to 6.129.

**Transformers4Rec** (Meta): a library that bridges NLP transformer architectures (GPT-2, BERT, XLNet) to sequential recommendation. Empirically found XLNet with replacement token detection worked well across datasets. Supports side information (user context, item metadata) as additional input features.

## The Convergence

The two paradigms are converging because they share a common substrate: a transformer decoder trained autoregressively on sequences of tokens. The only structural question is what vocabulary you use.

PLUM (Google) uses a pretrained LLM backbone but represents items as RQ-VAE codes — borrowing behavioral precision from paradigm A while retaining world knowledge from B.

LUM (Alibaba) runs an LLM offline and injects its representations into an existing ID-based DLRM pipeline — borrowing semantic richness from B without replacing the existing production infrastructure.

The question has shifted from "which paradigm?" to "which vocabulary, at which layer, trained on which signal?"

## Reasoning-Enhanced Recommendation

The most recent frontier: chain-of-thought reasoning applied to recommendation. **OneRec Think** (Kuaishou, 2025) generates an explicit reasoning trace before generating recommendations:

> "This user watches cooking content in evenings but exercise in mornings — it's 7am. They've seen this creator's last 5 videos; novelty matters."

This is the recommendation equivalent of chain-of-thought prompting. The key insight transfers from language: complex multi-step reasoning becomes tractable when the model has room to generate intermediate steps. Gains were largest for users with complex or evolving interests.

## Deployment Challenges

**Inference latency**: autoregressive decoding is sequential. At YouTube/TikTok scale, sub-100ms recommendation requires speculative decoding, model distillation, hardware-aware beam search, and aggressive offline pre-computation. PLUM reduces serving cost by >95% through offline pre-computation.

**Item churn**: platforms add new items continuously. Semantic ID systems require codebook updates for new items. LLM-based systems handle new items described in natural language gracefully. No clean solution exists for the codebook update problem in production.

**Exploration vs exploitation**: generative models trained on historical engagement strongly exploit popular items. Semantic code structure helps generalize to related long-tail items, but principled exploration remains an active area.

**Evaluation gap**: standard offline metrics (NDCG, hit rate, AUC) measure next-item prediction accuracy. A generated list that's accurate but redundant, or accurate but promotes echo-chamber dynamics, scores well offline but harms users long-term.

## When to Use Which Approach

| Situation | Recommendation |
|-----------|----------------|
| Rich interaction logs, latency-critical, large catalog | Semantic ID models (HSTU/OneRec as reference) |
| Cold-start or thin data is the primary problem | Fine-tuned LLMs (PLUM/LUM-style feature injection) |
| Existing ranking stack, want to add LLM signal incrementally | LUM-style offline LLM features injected into DLRM |
| Frontier scale, willing to invest in both | Converged architecture (PLUM: LLM backbone + semantic ID vocabulary) |

## Sources

- Louis Wang — [Generative Recommendation in Production: HSTU, OneRec, and What Every Major Platform Is Building](https://louiswang524.github.io/blog/generative-retrieval/)
- Louis Wang — [Two Bets on Generative Recommendation: Semantic IDs vs. Fine-Tuned LLMs](https://louiswang524.github.io/blog/genrec-paradigm-comparison/)
- Aman.ai — [Recommendation Systems: LLM](https://aman.ai/recsys/LLM/)
