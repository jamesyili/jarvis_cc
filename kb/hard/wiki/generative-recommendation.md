---
concept: Generative Recommendation
tags: [generative-recsys, semantic-ids, hstu, rq-vae]
sources:
  - kb/hard/raw/louis-wang/generative-recommendation-in-production-hstu-onerec-and-what-every-major-platfor.md
  - kb/hard/raw/louis-wang/two-bets-on-generative-recommendation-semantic-ids-vs-fine-tuned-llms.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/recommendation-systems|Recommendation Systems]]"
  - "[[hard/wiki/llm-recsys|LLM for RecSys]]"
  - "[[hard/wiki/large-language-models|Large Language Models]]"
understanding: 2  # basic understanding (assumed where James's background applies)
relevance: 3  # very relevant
knowledge_updated: 2026-09-07
---

# Generative Recommendation

For two decades, industrial recommendation systems followed the same blueprint: a two-stage pipeline where a lightweight retrieval model narrows millions of candidates to hundreds, then a heavier ranking model scores them. Generative recommendation replaces this architecture by framing recommendation as sequence generation — given a user's context, a single model generates item identifiers token by token.

The field is now in production at Meta, Google, Kuaishou, Alibaba, ByteDance, and LinkedIn. The question is no longer whether to move toward generative architectures, but how fast.

## Why Two-Stage Pipelines Hit a Ceiling

The classic ANN retrieval → re-ranking funnel has three structural limitations:

**The retrieval bottleneck:** The retrieval model must be simple enough to run at massive scale — which severely limits its expressiveness. Long user interaction histories, nuanced context signals, and fine-grained item attributes are typically lost at this stage. If the right item isn't retrieved, the ranker can never surface it.

**Stage inconsistency:** Retrieval and ranking are trained with different objectives, on different feature sets, with no joint optimization signal. Retrieval optimizes for recall; ranking optimizes for precision. These goals can actively conflict, and no amount of independent tuning resolves the mismatch.

**Static representations:** Candidate items are indexed as fixed embeddings at index time. The model can't dynamically adapt to a user's evolving context during inference, and long-tail items with sparse interaction histories get weak embeddings.

Generative recommendation addresses all three by training a single model end-to-end — but this requires rethinking how items are represented.

## The Semantic ID Breakthrough

Items need to be representable as discrete tokens before a generative model can predict them. Arbitrary numeric item IDs don't work — they carry no semantic information. There's no way for a model to reason that item `#4,821,033` is related to item `#4,821,034`.

**RQ-VAE (Residual Quantized Variational AutoEncoder)** is the solution adopted by virtually every major system. The process:
1. Start with a continuous item embedding (from content, metadata, behavior)
2. Compare against a learned codebook of prototype vectors; the nearest prototype index becomes token C₁ (broad category)
3. Compute the residual (difference between embedding and C₁ prototype); quantize the residual to get C₂ (finer detail)
4. Repeat for 3–8 rounds

Result: a short token sequence `[C₁, C₂, C₃, ...]` where similar items share code prefixes. Two NBA highlight clips share C₁ (sports) and C₂ (basketball) but differ at C₃ (specific game). A model generating `[sports, basketball, ...]` can generalize to recommend similar videos it has never seen in training — the code structure encodes the similarity.

This hierarchy is the critical property that makes generative recommendation practical. Semantic IDs are now the shared foundation across TIGER (Alibaba), HSTU (Meta), PLUM (Google), and OneRec (Kuaishou).

LinkedIn identified a related encoding problem: LLMs don't inherently understand raw numerical magnitudes. Converting continuous engagement counts (raw numbers like "4,382 likes") into percentile buckets wrapped in special tokens produced a 30× increase in correlation between popularity features and item embeddings.

## Paradigm A: Semantic ID-Based Autoregressive Models

With items tokenized, recommendation becomes a standard sequence prediction problem. A transformer decoder receives the user's interaction history — each item as its `[C₁, C₂, C₃]` token sequence — and predicts the token sequence of the next item autoregressively.

Training objective: minimize cross-entropy over next-item tokens given user history. Structurally identical to language model training. At inference, a **prefix trie** constrains decoding to valid item code sequences — the model cannot generate codes for non-existent items.

### Meta HSTU (ICML 2024)
The most influential production deployment, powering Reels recommendation at billion-user scale. Three architectural innovations:
- **Hierarchical temporal encoding:** Interactions across time scales (last minute vs. last month) carry different signals; encoded separately to avoid conflation
- **Relative position biases:** Recommendation sequences have temporal and categorical structure that absolute positional encodings handle poorly; learned relative biases replace them
- **Linear-complexity attention:** User histories span thousands of interactions; quadratic attention is intractable at that length

### Alibaba TIGER (NeurIPS 2023)
Generative retrieval for e-commerce. TIGER's semantic ID codebook incorporates structured item attributes — category, price tier, brand, seller type — directly into the quantization objective. Products with similar attributes cluster in the same code region, enabling cross-sell and substitute recommendations for items the user has never encountered.

### Kuaishou OneRec (2025)
The most radical deployment: collapses the entire recommendation pipeline — retrieval and ranking — into a single autoregressive model. Generates an ordered recommendation list directly as a sequence of semantic ID tokens. Beam search over the prefix trie yields multiple candidate lists; the best is selected.

OneRec V2 added: two-stage codebook learning (content codes first, then behavioral fine-tuning), beam search decoding, and constrained decoding via prefix trie.

### OneRec Think
Adds explicit reasoning before recommendation — the model first generates a structured trace about the user's inferred interests, mood, and context, then generates recommendations conditioned on that trace. The recommendation equivalent of chain-of-thought prompting:

*"This user watches cooking content in the evenings but exercise content in the mornings — it's 7am."*
*"They've seen this creator's last 5 videos; novelty likely matters here."*

Particularly effective for users with complex or evolving interests where shallow models struggle.

## Paradigm B: Fine-Tuned LLMs for Recommendation

A pretrained LLM has read the internet. It already knows that "NBA highlights" and "basketball game recap" are related. The fine-tuned LLM paradigm bets that this world knowledge transfers to recommendation.

Items are represented in natural language — titles, descriptions, metadata — mapped directly to tokens the LLM already understands. Fine-tuning strategies:
- **Continued Pre-Training (CPT):** Train the LLM on sequences of user interactions formatted as text, teaching it the platform's behavioral patterns on top of its world knowledge
- **Instruction tuning:** Frame recommendation as a prompt-completion pair ("Given this watch history: [...], recommend: [target]")
- **Preference alignment:** RLHF-inspired training on (recommended, rejected) item pairs

### Google PLUM (2024)
Adapts Gemini for YouTube Shorts recommendation via CPT on watch sequences. Notable: PLUM represents items as RQ-VAE semantic codes, not text titles — capturing behavioral structure that titles don't. +4.96% CTR lift in A/B testing, with gains concentrated on cold-start scenarios. The production deployment pre-computes item representations offline, reducing serving cost by over 95%.

### Alibaba LUM — Large User Model (2026)
A 7B parameter LLM pre-trained on tokenized behavior sequences, queried via condition tokens representing task context (surface, device, time of day). Runs offline — cached outputs injected as features into Taobao's existing DLRM ranker. The LLM never runs at serving time. +2.9% CTR gain in live testing. Demonstrates power-law scaling improvements up to 7B parameters.

### P5 (EMNLP 2022)
The conceptual ancestor: unifies five recommendation tasks (rating prediction, sequential recommendation, explanation, review summarization, direct recommendation) as a single text-to-text problem using T5.

## Trade-off Profile

| Dimension | Semantic ID Models | Fine-Tuned LLMs |
|---|---|---|
| Cold-start | Weak — needs interaction data | Strong — world knowledge fills gap |
| Data efficiency | Needs large interaction logs | Leverages pretraining |
| Item churn | Brittle — codebook rebuild required | Robust — new items described in text |
| Personalization depth | Strong — end-to-end behavioral training | Depends on fine-tuning quality |
| Serving latency | Fast — small vocab, trie decoding | Slow — large model, long context |
| Serving cost | Lower | Higher — requires aggressive caching |

## Generative Ranking

Beyond retrieval, the ranking stage is also moving to large sequence models. LinkedIn's generative ranker is a GPT-style transformer processing 1,000+ historical user interactions as a unified chronological sequence, combined via late fusion with count and affinity features, feeding a Multi-gate MoE prediction head.

ByteDance HLLM uses a hierarchical approach: an Item LLM processes each item's text and emits a compact embedding via a special `[ITEM]` token; a User LLM then processes the sequence of item embeddings (not raw text). This compresses behavior sequences to 1/6–1/4 of text-token length, making large-model ranking tractable.

ByteDance RankMixer found that standard transformer attention achieves only ~4.5% GPU utilization for recommendation workloads due to memory-bandwidth constraints. Hardware-aware architecture (parameter-free token mixing + sparse MoE) pushed utilization to 45%, enabling a 70× parameter scale-up (16M → 1B) with no latency regression.

## Convergence

The two paradigms are borrowing from each other:

- **PLUM** (LLM backbone) adopts RQ-VAE semantic IDs — capturing behavioral structure while retaining world knowledge
- **LUM** (ID-based production stack) injects LLM representations as features — improving the existing pipeline without replacing it

Both now share the same basic architecture: a transformer decoder, trained autoregressively, on sequences of tokens derived from user interactions. The structural gap has narrowed to one design choice: what vocabulary to use. Learned discrete codes (semantic IDs) vs. natural language tokens. The answer increasingly appears to be "both, in different parts of the system."

## Production Challenges

**Inference latency:** Autoregressive generation is inherently sequential. Sub-100ms recommendation at YouTube or TikTok scale requires speculative decoding, model distillation, hardware-aware beam search, and careful batching. PagedAttention (vLLM) for KV cache management applies directly.

**Item churn:** New items require codebook updates and model reindexing. No clean solution exists — periodic reindexing pipelines with incremental fine-tuning are the current approach.

**Exploration vs. exploitation:** Generative models trained on historical engagement over-exploit popular items. Semantic code structure helps generalize to related long-tail items, but principled exploration (genuinely novel content) remains unsolved.

**Evaluation:** Standard metrics (NDCG, AUC, hit rate) measure next-item prediction accuracy, not recommendation quality. A generated list that is accurate but redundant, or accurate but reinforces echo-chamber dynamics, scores well offline but harms users long-term. New evaluation frameworks are needed.

## Sources

- Louis Wang. *Generative Recommendation in Production: HSTU, OneRec, and What Every Major Platform Is Building* — two-stage ceiling, semantic ID breakthrough, HSTU, PLUM, TIGER, OneRec, LONGER, LEMUR, OneRec Think, production challenges
- Louis Wang. *Two Bets on Generative Recommendation: Semantic IDs vs. Fine-Tuned LLMs* — RQ-VAE mechanics, paradigm A vs. B trade-off analysis, TIGER, HSTU, OneRec, PLUM, LUM, P5, convergence thesis
