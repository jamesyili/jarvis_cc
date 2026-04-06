---
concept: Large Language Models
tags: [llm, gpt, language-models, scaling, context-length, decoder-only, chinchilla]
sources:
  - kb/hard/raw/aman-ai/primers-overview-of-large-language-models.md
  - kb/hard/raw/sebastian-raschka/the-big-llm-architecture-comparison.md
  - kb/hard/raw/sebastian-raschka/from-gpt-2-to-gpt-oss-analyzing-the-architectural-advances.md
  - kb/hard/raw/nathan-lambert/opus-46-codex-53-and-the-post-benchmark-era.md
  - kb/hard/raw/aman-ai/nlp-llm-context-length-extension.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/transformer-architecture|Transformer Architecture]]"
  - "[[hard/wiki/llm-post-training|LLM Post-Training]]"
  - "[[hard/wiki/rl-for-llms|RL for LLMs]]"
  - "[[hard/wiki/llm-evaluation|LLM Evaluation]]"
---

# Large Language Models

Large language models (LLMs) are autoregressive transformer-based models trained to predict the next token over massive text corpora. They represent the dominant paradigm in NLP and have become general-purpose reasoning engines with emergent capabilities not explicitly trained for. Seven years on from GPT-2, the fundamental architecture has changed remarkably little — what has changed are the scale, training recipes, and the post-training alignment pipelines that shape behavior.

## Foundations: Language Modeling and Pretraining

The core task is **next-token prediction**: given a sequence of tokens, predict the probability distribution over the vocabulary for the next token. Training on internet-scale data (trillions of tokens) via this self-supervised objective produces models that compress vast world knowledge into billions of parameters.

GPT-3 (2020) demonstrated that language models trained purely on next-token prediction, at sufficient scale, could perform few-shot in-context learning — solving tasks from examples in the prompt without any weight updates. This was a paradigm shift: a single pretrained model could serve many tasks via prompting.

The pretraining process is expensive and done once. GPT-3 training required ~355 GPU-years. Modern frontier models cost hundreds of millions of dollars to pretrain. This creates strong incentives to maximize data quality and efficiency.

## Scaling Laws and Chinchilla

Kaplan et al. (2020) showed that model loss follows predictable power laws with respect to parameters and compute. Larger models, more data, and more compute all improve performance predictably. This justified the race to build ever-larger models.

The **Chinchilla scaling law** (Hoffmann et al. 2022) revealed that earlier models like GPT-3 were substantially undertrained — too many parameters for too little data. The optimal compute-efficient allocation roughly equals 20 training tokens per parameter. A 70B-parameter model trained optimally needs ~1.4 trillion tokens; a 7B model needs ~140B tokens. After Chinchilla, the field shifted toward training smaller models longer rather than maximizing parameters.

## Architectural Signature: The Modern Decoder

From GPT-2 to gpt-oss-120B, the decoder-only transformer has evolved incrementally but consistently:

- **LayerNorm → RMSNorm**: Simpler, computationally cheaper. Standard since Llama (2023).
- **Absolute positional embeddings → RoPE**: Encodes relative position via rotation; enables context extension. Universal since Llama. See [[hard/wiki/transformer-architecture|Transformer Architecture]].
- **GELU activation → SwiGLU**: Gated linear unit variant with slightly better expressivity at equivalent parameter count. Standard in most frontier models.
- **Multi-head attention → Grouped-query attention (GQA)**: Reduces KV cache at inference with negligible quality loss. Standard in Llama 3, Qwen3, Gemma 3.
- **Dropout removed**: Modern large-scale models rarely overfit during single-epoch pretraining; dropout measurably hurts performance.
- **Dense FFN → Mixture-of-Experts (MoE)**: Replaces single FFN with routing over multiple expert FFNs. Dramatically increases parameter capacity with proportionally less inference compute per token.

The 2025 consensus architecture: decoder-only, RoPE, RMSNorm, SwiGLU, GQA or MLA. MoE for the largest models.

## Major Model Families

**GPT (OpenAI)**: GPT-1 through GPT-4 pioneered the decoder-only scaling approach. GPT-3 (175B, 2020) demonstrated few-shot learning. GPT-4 (2023) added multimodality and RLHF-based alignment. OpenAI's first open-weight models since GPT-2 are gpt-oss-20b and gpt-oss-120b (2025), both MoE architectures with GQA and alternating sliding window attention (128-token window every other layer).

**LLaMA / Llama (Meta)**: LLaMA 1 (2023) established the open-source decoder benchmark and catalyzed a wave of fine-tuned derivatives. Llama 2 introduced RLHF alignment. Llama 3 (2024) scaled to 405B with GQA and RoPE at 8K→128K context. Llama 4 (2025) moves to a MoE architecture.

**Claude (Anthropic)**: Constitutional AI training + RLHF emphasis on safety and helpfulness. Claude 3 series (Haiku/Sonnet/Opus) defined tiered deployments. Claude 4 (2025) doubled down on agentic coding capabilities; Claude Code with Opus 4.5/4.6 caused a step-change in agentic software engineering performance.

**Gemini (Google DeepMind)**: Natively multimodal from the start. Gemini 2.5 Pro pushed long-context capabilities (1M tokens). Gemma 3 (27B) is Google's open-weight release featuring sliding window attention in a 5:1 local-to-global ratio with a 1024-token window, markedly reducing KV cache memory at minimal perplexity cost.

**DeepSeek**: The most architecturally innovative recent entrant from a Chinese lab. DeepSeek-V3 (671B total, 37B active per token) uses Multi-Head Latent Attention (MLA) for KV compression and fine-grained MoE (256 experts, 9 active per token). DeepSeek-R1 combined RLVR with long-chain-of-thought reasoning and established that open models can match frontier closed models on reasoning benchmarks. Released at a fraction of US frontier lab costs, prompting broad industry reassessment of both economics and methodology.

**Qwen (Alibaba)**: Among the strongest open-weight models as of 2025. Dense models (0.6B–32B) and MoE variants (30B–235B). Qwen3-Next and Qwen3.5 introduced hybrid attention (3:1 Gated DeltaNet to Gated Attention blocks), signaling that linear attention hybrids have entered the main model line, not just efficiency variants.

**Phi (Microsoft)**: Small Language Models optimized for on-device and low-resource deployment. Phi-4 (14B) achieves strong performance through data quality emphasis rather than scale.

## Context Length Extension

Standard pretrained models degrade when given inputs longer than their training context window. Several techniques extend context:

**Positional Interpolation (PI)**: Downscales position indices to fit within the original context range before computing RoPE encodings. Meta extended Llama 2 from 4K to 32K tokens in ~1000 fine-tuning steps. Stable because interpolation stays in-distribution rather than extrapolating.

**YaRN**: Combines NTK-aware scaling with dynamic interpolation. Extends Llama models to 128K tokens using ~0.1% of the original pretraining corpus. Dynamic NTK adapts attention scaling based on actual sequence length, avoiding the fixed tradeoff of static linear scaling.

**LongLoRA**: Efficient fine-tuning via Shift Short Attention (S²-Attn) during training. Splits sequences into groups, shifts context across groups in half the attention heads, and approximates full attention cheaply. Extended Llama 2 70B to 32K on a single 8×A100 machine. Compatible with FlashAttention-2.

**Sliding Window Attention**: Restrict most layers to a local window; intersperse full-attention layers for long-range retrieval. Gemma 3 uses a 1024-token window at a 5:1 ratio; ablation studies show minimal perplexity impact. gpt-oss uses a 128-token window alternating with full attention.

The practical challenge of long context in 2025 is less "can the model handle it" and more "does the model actually use it well." The "lost in the middle" phenomenon shows models often underweight information from the center of very long contexts, motivating retrieval-augmented approaches even when raw context length supports naively stuffing the full document.

## Capabilities and Known Limitations

After instruction tuning and RLHF, LLMs can follow complex multi-turn instructions, reason through problems with chain-of-thought prompting, write and edit code and text, translate and summarize, and use tools via structured interfaces.

Known failure modes:

- **Hallucination**: Confident generation of factually incorrect information, with no reliable self-knowledge of what the model knows vs. doesn't.
- **Reversal curse**: "A is B" does not reliably generalize to "B is A" — knowledge is directional in the training distribution.
- **Context underutilization**: Information in the middle of long prompts is often underweighted relative to the beginning and end.
- **Calibration**: Models express similar confidence across statements of very different factual reliability.
- **Reasoning limits**: Strong on familiar reasoning patterns; weaker on novel multi-step problems requiring genuine backtracking and state tracking.

## The Post-Benchmark Era

As of 2025-2026, standard benchmarks (MMLU, GSM8K, HumanEval) have largely saturated. The highest-scoring models on these metrics no longer reliably correspond to the most useful models in deployment. Gaps between models are felt primarily in agentic settings — multi-step coding, tool use, long-horizon tasks — where academic benchmarks fail to discriminate.

Model releases from Anthropic (Claude 4 series) explicitly deprioritized benchmark gains in favor of demonstrated agentic performance improvements. This signals a structural shift: the field is transitioning from benchmark-driven development toward evaluation through real-world task completion in agent harnesses. Useful discriminating signals now come from sustained use at scale (Claude Code adoption, comparative coding agent evaluations) rather than eval leaderboards. See [[hard/wiki/llm-evaluation|LLM Evaluation]] for the full evaluation methodology landscape.

## Sources

- Aman.ai Primers: Overview of LLMs — embeddings, context length, RAG, model catalog
- Sebastian Raschka: The Big LLM Architecture Comparison — DeepSeek V3, OLMo 2, Gemma 3, Llama 4 architecture breakdown
- Sebastian Raschka: From GPT-2 to gpt-oss — incremental architectural evolution analysis
- Nathan Lambert: Opus 4.6, Codex 5.3, and the Post-Benchmark Era — agentic evaluation shift signal
- Aman.ai: NLP LLM Context Length Extension — PI, YaRN, LongLoRA, MemGPT technical details
