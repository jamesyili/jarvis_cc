---
concept: Large Language Models
tags: [llm, gpt, language-models, scaling, reasoning, context-length]
sources:
  - kb/hard/raw/aman-ai/natural-language-processing-language-models.md
  - kb/hard/raw/aman-ai/nlp-llm-context-length-extension.md
  - kb/hard/raw/aman-ai/primers-overview-of-large-language-models.md
  - kb/hard/raw/aman-ai/models-meena.md
  - kb/hard/raw/aman-ai/models-generative-pre-trained-transformer-4-gpt-4.md
  - kb/hard/raw/aman-ai/models-llama.md
  - kb/hard/raw/sebastian-raschka/understanding-and-implementing-qwen3-from-scratch.md
  - kb/hard/raw/sebastian-raschka/understanding-reasoning-llms.md
  - kb/hard/raw/sebastian-raschka/the-state-of-llms-2025-progress-problems-and-predictions.md
  - kb/hard/raw/sebastian-raschka/the-big-llm-architecture-comparison.md
  - kb/hard/raw/nathan-lambert/opus-46-codex-53-and-the-post-benchmark-era.md
  - kb/hard/raw/nathan-lambert/claude-code-hits-different.md
last_compiled: 2026-04-05
related:
  - hard/wiki/transformer-architecture
  - hard/wiki/retrieval-augmented-generation
  - hard/wiki/llm-evaluation
  - hard/wiki/rl-for-llms
  - hard/wiki/ai-agents-and-agentic-systems
---

# Large Language Models

## Foundations: From N-grams to Neural Language Models

A language model assigns probabilities to sequences of text — formally, it models P(word_t | context). Early n-gram models made a Markov assumption that only the last n−1 words matter. This produced a sparsity problem: unseen sequences get zero probability, and 3–4-word windows lack coherent long-range context.

Neural language models broke the Markov constraint. Window-based feed-forward networks were first, followed by RNNs with recurrent state, then the key architectural shift: contextual embeddings. ELMo (2018) demonstrated that a word's representation should depend on its full sentence context — "bank" means something different in "river bank" vs. "investment bank." ELMo produced this via bidirectional LSTM trained on a task corpus.

The modern LLM era begins with the GPT line: autoregressive transformers trained to predict the next token. Autoregressive (causal, left-to-right) models like GPT assign P(token_t | token_1..t-1) and generate by sampling token by token. Contrast with masked models (BERT), which predict randomly masked tokens given full bidirectional context — suited for classification and embedding tasks but not open-ended generation. Today's frontier LLMs are predominantly autoregressive.

**Perplexity** — the exponentiated cross-entropy — remains the standard intrinsic metric for language modeling quality. Meena (2019), Google's 2.6B-parameter conversational model, introduced SSA (Sensibleness and Specificity Average) as a human-eval complement to perplexity, anticipating the later shift toward human-preference evaluation. GPT-3's landmark contribution was demonstrating that a large enough model could perform *in-context learning* — adapting to entirely new tasks from a few examples in the prompt, without weight updates.

## Scaling Laws and the Chinchilla Correction

The Kaplan et al. (2020) scaling laws established that LLM loss decreases predictably as a power law of model size, data, and compute. This drove labs to train ever-larger models — GPT-3 at 175B, PaLM at 540B — often on relatively modest data.

The Chinchilla paper (Hoffmann et al., 2022) revised this: given a fixed compute budget, the optimal strategy is to scale data and model size roughly equally — approximately **20 tokens per parameter**. GPT-3's 175B parameters were optimal for ~3.5 trillion tokens, far more than the 300B it was actually trained on. Chinchilla at 70B, trained on 1.4T tokens, outperformed Gopher at 280B. The practical consequence: labs shifted toward smaller, data-denser models. LLaMA-1 (Meta, 2023) applied this insight to produce open-weight models at 7B–65B that outperformed their nominal size suggests, by training longer on public web data. LLaMA-2 and subsequent releases pushed this further.

DeepSeek V3's 2024 training cost report (~$5M for a 671B MoE run) suggested another correction: compute-efficient architectures like Mixture-of-Experts can dramatically reduce the effective cost of frontier-scale training.

## Major Model Families

**GPT line (OpenAI):** GPT-3 established in-context learning at scale. GPT-4 added multimodality and RLHF alignment, passing bar exams in the top 10% and substantially improving reasoning over GPT-3.5. The Codex/GPT-5 line has pivoted toward coding agents.

**Claude (Anthropic):** Characterized by strong instruction-following, long-context reliability, and a product-first approach. Claude 4 (May 2025) bet on coding agents before benchmarks justified it. Opus 4.5 and 4.6 drove the Claude Code step-change — a qualitative shift in agentic software creation where the interface itself became a differentiator, not just the model weights.

**Gemini (Google DeepMind):** Led benchmark cycles in 2024–2025 with multimodal capability and long context, but lost ground in the agentic coding era by 2026.

**LLaMA / open-weight ecosystem (Meta):** LLaMA-2's use of RoPE (Rotary Position Embeddings) and open-source release made it the foundation for the open-weight explosion. LLaMA-3 and LLaMA-4 continued pushing this lineage.

**DeepSeek (DeepSeek AI):** V3 (671B MoE, Dec 2024) and R1 (Jan 2025) are landmark open-weight models. V3 introduced Multi-Head Latent Attention (MLA) — which compresses KV tensors into a lower-dimensional space before caching, outperforming both MHA and GQA at equivalent cost — alongside a fine-grained MoE architecture. R1 showed that reasoning behavior emerges from pure RL, rivaling o1 at a fraction of the inference cost.

**Qwen (Alibaba):** Released under Apache 2.0 with no commercial restrictions. Qwen3 (2025) offers sizes from 0.6B dense to 480B MoE, with the 235B-Instruct variant ranked top-10 on LMArena as of this writing. A 1T-parameter "max" variant was released September 2025. Qwen3 uses RoPE with grouped-query attention and SwiGLU activations — architecturally conservative, quality-optimized.

## Context Length Extension

The original transformer encodes position via fixed positional encodings, limiting context to the training window. Extending this matters because long-context LLMs can process entire codebases, legal documents, or session histories without RAG.

**RoPE (Rotary Position Embeddings)**, used in LLaMA and its descendants, encodes position via rotations applied to query/key vectors, making attention scores depend on *relative* distance rather than absolute position. This makes RoPE amenable to interpolation.

**Position Interpolation (PI):** Rather than extrapolating positions beyond the training window (which produces out-of-distribution, unstable attention scores), PI *downscales* position indices to fit within the trained range. LLaMA-7B extended to 32K tokens with only 1,000 fine-tuning steps. The theoretical upper bound of interpolation error is at least 600x smaller than extrapolation.

**NTK-aware and Dynamic NTK:** NTK-aware scaled RoPE extends to 8K context with no fine-tuning by preserving high-frequency components during scaling. Dynamic NTK adjusts the scaling factor as a function of current sequence length — longer sequences get more aggressive scaling — which outperforms static interpolation.

**YaRN:** Combines dynamic NTK with a temperature parameter that modulates attention across extended windows. Extended LLaMA-2 to 128K with 0.1% of the original pretraining corpus.

**LongLoRA:** Sparse local attention (Shift Short Attention) during fine-tuning approximates full attention while cutting compute 16x. At inference, the model reverts to standard full attention. Extended LLaMA-2 7B to 100K tokens on a single 8×A100 node.

**MemGPT:** Instead of extending the context window, treats the LLM as an OS. Main context (RAM) holds the active window; external storage (disk) holds past sessions and documents. The LLM manages its own memory via function calls — enabling effectively unbounded context at the cost of retrieval latency.

The practical framing: a longer context window is analogous to more RAM. It enables in-context learning over private, task-specific data without fine-tuning, which is often the highest-leverage configuration for enterprise LLM applications.

## Reasoning Models

The standard LLM pipeline — pretraining → SFT → RLHF — produces capable but non-deliberative models. Reasoning models add a structured thinking phase: multi-step intermediate generation before the final answer.

OpenAI's o1 (Sep 2024) was the first widely-deployed reasoning model: it runs multiple internal reasoning iterations before returning a response, at higher cost-per-query than GPT-4o. The exact mechanism is undisclosed, but likely combines SFT on chain-of-thought data with RL and heavy inference-time scaling.

DeepSeek R1 (Jan 2025) provided the first public blueprint:

1. **R1-Zero:** Pure RL from the DeepSeek-V3 base, no SFT. Rewards are verifiable — a compiler for code, a deterministic checker for math, an LLM judge for format. Reasoning emerged spontaneously: the model developed `<think>` traces without being explicitly trained to do so. This confirmed reasoning as an *emergent* RL behavior, not just an SFT artifact.

2. **R1:** Added cold-start SFT data (from R1-Zero), followed by further RL with added consistency rewards, then another round of SFT (600K CoT + 200K knowledge examples), then final RL with human preference labels. This is standard RLHF + verifiable rewards, but with CoT-heavy SFT data throughout.

3. **R1-Distill:** Smaller Qwen and LLaMA models fine-tuned on R1's SFT data. Demonstrates that SFT alone on high-quality CoT data transfers strong reasoning to sub-10B models — but distillation can't drive frontier progress on its own.

The four approaches to building reasoning models:
- **Inference-time scaling:** Chain-of-thought prompting, majority voting, beam search, process reward models — no training change, higher compute at inference.
- **Pure RL (RLVR):** Verifiable rewards on math/code; reasoning emerges, no SFT needed. GRPO (from DeepSeek R1) became the dominant algorithm variant in 2025.
- **SFT + RL:** The reliable production blueprint. Strong base → CoT SFT → RL with verifiable + preference rewards.
- **Distillation:** SFT from a stronger model's outputs. Efficient and accessible but dependent on the teacher.

The tradeoffs are real: reasoning models are verbose, expensive, and prone to "overthinking" on simple tasks. The correct pattern is to route complex multi-step problems (math proofs, hard code debugging) to reasoning models and simple factual queries to standard LLMs.

## The Post-Benchmark Era

From 2023–2025, benchmark improvements mapped reliably to felt capability gains — more reliable tool use, broader task coverage, stronger reasoning. That era is ending.

By early 2026, Opus 4.6 vs. Codex 5.3 represents the new regime: benchmark deltas are minor and poorly predictive of agentic task performance. Gemini 3 Pro topped benchmarks in November 2025, was declared the new leader, and within two months had no meaningful presence in the agentic coding space. Anthropic's approach — deprioritizing benchmark optics in favor of agentic usability — proved prescient.

Assessment is shifting toward: how well does the model handle unsupervised, multi-step, real-world tasks? Can it manage context, recover from errors, operate across tools, maintain coherent long-horizon behavior? These are harder to measure and benchmark less directly. The product layer — the harness, the CLI, the agent scaffolding — now matters as much as the base model.

The implication: model selection increasingly requires extended use-based testing, not benchmark comparison tables. Consistent, domain-specific personal testing is replacing release-day benchmark scorecards as the signal source.

## Architectural Convergence and Open Questions

Seven years from GPT-2, frontier LLMs share a recognizable core: [[hard/wiki/transformer-architecture|transformer]] backbone, RoPE positional embeddings, SwiGLU activations, grouped-query (or latent) attention, and MoE feedforward layers at scale. The variation is in training recipe, data mix, and post-training pipeline.

Key open problems:
- **Continual learning:** LLMs forget old knowledge when trained on new data (catastrophic forgetting). No scalable solution yet; expected to be a 2027 focus.
- **RLVR generalization:** Currently limited to math and code where rewards are verifiable. Extending to open-domain reasoning via process reward models or LLM-judge-scored explanations is the next frontier.
- **Reliability in long-horizon agentic tasks:** Current models fail at complex multi-step work requiring sustained context and self-correction. This is where the next generation of capabilities will be felt before benchmarks can measure it.

See also: [[hard/wiki/rl-for-llms|RL for LLMs]], [[hard/wiki/llm-evaluation|LLM Evaluation]], [[hard/wiki/retrieval-augmented-generation|RAG]], [[hard/wiki/ai-agents-and-agentic-systems|AI Agents]].
