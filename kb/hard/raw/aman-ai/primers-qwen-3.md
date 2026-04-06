# Primers • Qwen 3

**Source:** https://aman.ai/primers/ai/qwen3/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

# Qwen3 Technical Primer (Maximum Density)

## Overview and Motivation

**Qwen3** is the latest series of open-weight large language models (LLMs) from the Qwen family, representing a decisive step toward Artificial General Intelligence (AGI). Qwen3 introduces a unified framework designed to balance **frontier performance across STEM, reasoning, and language tasks** with practical efficiency. All Qwen3 models are publicly accessible under the **Apache 2.0 license**.

* **Scale and Sparsity:** The model family includes dense models and **Mixture-of-Experts (MoE)** architectures scaling up to **1.8 trillion parameters** (with 64B active per token). The flagship model, **Qwen3-235B-A22B**, features **235B total parameters** with **22B activated parameters per token**.
* **Training Scale:** Pre-training covered **36 trillion tokens** across **119 languages and dialects**, significantly expanding coverage from the 29 languages supported by Qwen2.5.
* **Core Innovation:** Qwen3 integrates **thinking mode** (for complex, multi-step reasoning) and **non-thinking mode** (for rapid, context-driven responses) into a single model. This eliminates the need for switching between dedicated models (e.g., between chat-optimized and reasoning models).

## Architectural Advances

The Qwen3 series includes 6 dense models (0.6B to 32B) and 2 MoE models (Qwen3-30B-A3B and Qwen3-235B-A22B).

### MoE Configuration

* **Expert Count:** Qwen3 MoE models have **128 total experts** with **8 activated experts per token**.
* **Architecture:** The MoE design specifically **excludes shared experts**, unlike some other MoE architectures.
* **Load Balancing:** The model adopts the **global-batch load balancing loss** to encourage expert specialization.
* **Flagship Specs:** The Qwen3-235B-A22B model has **94 layers** and utilizes 64 Query heads and 4 Key/Value heads (64 / 4).

### Attention and Context Scaling

* **Attention Stabilization (QK-Norm):** Qwen3 introduces **QK-Norm** to normalize queries and keys independently before the dot-product attention. This addresses instability at long sequence lengths, reducing perplexity growth by **20–30%** relative to baseline configurations during **128K context extrapolation**.
* **Efficiency:** **Grouped Query Attention (GQA)** is implemented, sharing Key-Value pairs across query heads to yield **linear scaling with a reduced memory footprint**.
* **Positional Embedding:** **Rotary Position Embeddings (RoPE)** are enhanced with **Adaptive Basis Function (ABF)**. The base frequency of RoPE is increased from $10,000$ to $1,000,000$ using ABF to maximize effective sequence utilization during context extension.
* **Long-Sequence Inference:** **Dual Chunked Attention (DCA)** is introduced to optimize long-sequence inference by chunking sequences into overlapping windows, achieving a throughput improvement of **1.6$\times$ at 128K tokens** without accuracy loss. Context length is extended to **128K** using the **YaRN** method.
* **Tokenizer:** Qwen’s tokenizer is utilized, implementing byte-level byte-pair encoding (BBPE) with a vocabulary size of **151,669**.

## Pre-Training Innovations

Qwen3 models are trained through a proprietary **three-stage curriculum** on **36 trillion tokens**.

### Corpus and Data Synthesis

* **Data Sources:** The dataset covers **119 languages** and includes high-quality content in coding, STEM, reasoning tasks, and synthesized data.
* **Synthesis Methods:** Synthetic data (trillions of tokens) is generated using specialized models: **Qwen2.5-VL** (for PDF text recognition), **Qwen2.5-Math** (for mathematical content), and **Qwen2.5-Coder** (for code snippets). Code datasets are automatically validated against execution environments.
* **Instance-Level Optimization:** Unlike previous studies, Qwen3 optimizes the data mixture at the **instance-level** using fine-grained data labels and ablation experiments on small proxy models.

### Three-Stage Pre-Training Process

1. **General Stage (S1):** Training on **over 30 trillion tokens** at a sequence length of 4,096 tokens to build a strong foundation of general knowledge.
2. **Reasoning Stage (S2):** Training on **about 5T higher-quality tokens** with an increased proportion of STEM, coding, and reasoning data.
3. **Long Context Stage (S3):** Training on **hundreds of billions of tokens** at a sequence length of **32,768 tokens** using YaRN and DCA. The corpus for this stage includes **75% of text between 16,384 and 32,768 tokens** in length.

## Post-Training and Thinking Control

The post-training pipeline is designed with **Thinking Control** and **Strong-to-Weak Distillation** as dual core objectives.

### Four-Stage Post-Training Pipeline (Flagship Models)

1. **Long-CoT Cold Start (S1):** Supervised fine-tuning (SFT) is performed on curated Chain-of-Thought (CoT) examples that **require deeper reasoning**, excluding queries solvable without CoT.
2. **Reasoning RL (S2):** Reinforcement learning is applied using **GRPO** (Group Relative Policy Optimization) on **3,995 challenging query-verifier pairs** not used in the cold-start phase. This stage resulted in the AIME’24 score increasing from **70.1 to 85.1** over 170 RL training steps for Qwen3-235B-A22B.
3. **Thinking Mode Fusion (S3):** Continual SFT integrates **“thinking” and “non-thinking” modes** using a specific chat template.
   * **Explicit Control:** The flags `/think` and `/no think` are introduced in the user query or system message. The non-thinking mode response retains an **empty thinking block** (`<think></think>`) to ensure internal format consistency.
   * **Dynamic Budget:** The model naturally develops the ability to handle **intermediate cases** where reasoning is halted at a user-defined threshold (**thinking budget**), inserting a stop instruction. Performance scales **smoothly and consistently** with the allocated thinking budget.
4. **General RL (S4):** Aims for broad capability enhancement across **over 20 distinct tasks**.
   * **Reward System:** Utilizes three distinct reward types: **Rule-based Reward** (for format adherence), **Model-based Reward with Reference Answer** (using Qwen2.5-72B-Instruct to score output), and **Model-based Reward without Reference Answer** (trained on human preference data).
   * **Agent Ability:** The model is trained to correctly invoke tools via designated interfaces, performing **complete multi-turn interaction cycles with real environment execution feedback**.

### Strong-to-Weak Distillation

This method is used for lightweight models (0.6B to 30B-A3B) to enhance performance and impart mode-switching capabilities with high efficiency.

* **Efficiency:** Distillation achieves significantly better performance than direct RL while requiring approximately **1/10 of the GPU hours**.
* **Process:** Includes two phases: **Off-policy Distillation** (using combined /think and /no think teacher outputs) and **On-policy Distillation** (where the student generates sequences and is fine-tuned by aligning its logits with the teacher model to minimize KL divergence).

## Evaluation and Performance Metrics

Qwen3-235B-A22B demonstrates **state-of-the-art overall performance among open-source models** in both thinking and non-thinking modes.

### Competitive Benchmarking (Qwen3-235B-A22B-Base)

The base model version outperforms key open-source rivals despite being significantly smaller.

| Baseline Comparison | Qwen3-235B-A22B-Base (235B/22B) | DeepSeek-V3 Base (671B/37B) | Rationale |
| --- | --- | --- | --- |
| **Total Params Ratio** | 1.0 | $\sim 3.0\times$ Larger | Qwen3 outperforms DeepSeek-V3 on **14 out of 15 benchmarks**. |
| **Activated Params Ratio** | 1.0 | $\sim 1.7\times$ Larger | Qwen3 uses $\sim 2/3$ activated parameters. |
| **MMLU-Redux** | **87.40** | 86.14 | Highest score among competitors. |
| **MATH** | **71.84** | 62.62 | Significant performance lead. |
| **EvalPlus (Coding)** | **77.60** | 63.75 | Strong coding superiority. |

### Flagship Performance (Qwen3-235B-A22B, Post-Trained)

| Benchmark | Thinking Mode Score | Non-Thinking Mode Score | Comparative Detail |
| --- | --- | --- | --- |
| **MMLU-Redux** | **92.7** | 89.2 | Thinking mode is competitive with GPT-4o, Gemini 2.5 Pro. |
| **GPQA-Diamond** | 71.1 | 62.9 | Lower than Gemini 2.5 Pro (84.0) but strong for open source. |
| **AIME’25** (Math) | **81.5** | 24.7 | Demonstrates effectiveness of “Thinking Mode” for complex math. |
| **LiveCodeBench v5** | 70.7 | 35.3 | High performance in the agent/coding domain. |
| **CodeForces (Rating)** | **2056 / 98.2%** | 1387 / 75.7% | SOTA CodeForces rating among reasoning models, surpassing DeepSeek-R1 and Gemini 2.5 Pro. |
| **Arena-Hard** (Alignment) | **95.6** | **96.1** | Highest score among models listed, surpassing GPT-4o (85.3). |

### Multilingual Expertise

* Qwen3 achieves competitive performance across all evaluated benchmarks covering **119 languages**.
* Multilingual evaluations (Multi-IF, MT-AIME2024, PolyMath) show Qwen3 consistently outperforms DeepSeek-V3 and Gemini Flash in non-English STEM and reasoning tasks (e.g., MT-AIME2024: Qwen3-235B-A22B Thinking **80.8** vs. Gemini 2.5 Pro **76.9**).

## Comparison of Thinking Modes: Qwen3 vs. Claude 4

Qwen3 and Claude 4 models treat internal reasoning differently in terms of user control:

* **Qwen3 (Explicit Control):** Integrates thinking and non-thinking modes via **chat templates** and **explicit user flags** (`/think` and `/no think`). Users can dynamically allocate computational resources via the **thinking budget mechanism**.
* **Claude 4 (Internal/Gated):** The Extended Thinking Mode is triggered internally, and the model’s lengthy thought processes are typically **summarized by a smaller model** [Claude 4 Sources]. Full unsummarized thought processes are often restricted to a “Developer Mode” or specialized deployments [Claude 4 Sources].
