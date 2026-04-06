# Primers • DeepSeek V3

**Source:** https://aman.ai/primers/ai/deepseekV3/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

# DeepSeek-V3 Technical Primer

## Overview

**DeepSeek-V3** is a powerful Mixture-of-Experts (MoE) language model. It is characterized by its scale, efficiency, and strong performance, competing with leading closed-source models such as GPT-4o and Claude-3.5-Sonnet.

* **Scale and Sparsity:** The model comprises **671B total parameters**. Only **37B parameters are activated for each token** during inference, balancing capacity with computational tractability.
* **Cost Efficiency:** DeepSeek-V3 required only **2.788M H800 GPU hours for its full training** (Pre-Training, Context Extension, and Post-Training). The pre-training stage alone consumed 2.664M H800 GPU hours over 14.8T tokens, corresponding to a total cost of approximately $5.576 million USD.
* **Stability:** The training process demonstrated remarkable stability over 14.8T tokens, with **no irrecoverable loss spikes or rollbacks** reported.

## Architecture

DeepSeek-V3 adheres to the Transformer framework, integrating two major architectural innovations validated in DeepSeek-V2: **Multi-head Latent Attention (MLA)** for efficient inference and **DeepSeekMoE** for economical training. The model architecture includes **61 Transformer layers** with a hidden dimension of 7168. All FFNs, except for the first three layers, are replaced by MoE layers.

### Attention Mechanism: Multi-head Latent Attention (MLA)

MLA is the self-attention mechanism, primarily designed to significantly reduce the Key-Value (KV) cache size during inference via **low-rank joint compression**.

* **KV Compression:** The compressed latent vector for keys and values, $c\_{KV\_t} \in \mathbb{R}^{d\_c}$, and the decoupled key, $k^R\_t$, are the only vectors that need to be cached during generation. The KV compression dimension ($d\_c$) is set to 512.
* **Query Compression:** Attention queries are also compressed into a latent vector $c\_{Q\_t} \in \mathbb{R}^{d’\_c}$ to reduce activation memory during training. The query compression dimension ($d’\_c$) is set to 1536.
* **Dimensionality:** The model uses $n\_h=128$ attention heads, a dimension per head $d\_h=128$, and a per-head dimension for the decoupled RoPE-carrying key/query $d^R\_h=64$.

### MoE Configuration and Load Balancing

DeepSeek-V3 utilizes the DeepSeekMoE architecture.

* **Expert Structure:** Each MoE layer consists of **1 shared expert and 256 routed experts**. The intermediate hidden dimension of each expert is 2048.
* **Activation:** **8 routed experts** ($K\_r=8$) are activated for each token.
* **Auxiliary-Loss-Free Load Balancing:** DeepSeek-V3 pioneers an **auxiliary-loss-free strategy** for load balancing to mitigate the performance degradation associated with conventional auxiliary losses. This is achieved by introducing a **dynamic bias term ($b\_i$)** for each expert, which is only used for determining the top-$K\_r$ routing, not for the final gating value calculation. Ablation studies show this strategy leads to **greater expert specialization patterns** compared to auxiliary-loss-based models. The bias update speed ($\gamma$) was $0.001$ for most of the training.
* **Complementary Sequence-Wise Loss:** A complementary sequence-wise balance loss ($\mathcal{L}\_{\text{Bal}}$) is retained with an **extremely small weighting factor ($\alpha = 0.0001$)**, solely to prevent extreme imbalance within any single sequence.
* **Routing Constraint:** A restricted routing mechanism limits communication costs by ensuring each token is sent to at most **$M=4$ nodes**.
* **No Token Dropping:** Due to the effective load balancing strategy, **DeepSeek-V3 does not drop any tokens** during training or inference.

### Training Objective: Multi-Token Prediction (MTP)

DeepSeek-V3 employs a **Multi-Token Prediction (MTP) objective**, which densifies training signals and enhances model performance.

* **Prediction Depth:** The model predicts **one additional token** ($D=1$) besides the next token.
* **Implementation:** The MTP module uses shared embedding layers and output heads with the main model to maintain memory efficiency. The MTP loss weight ($\lambda$) was set to $0.3$ for the first 10T tokens and $0.1$ for the remaining 4.8T tokens.
* **Inference Acceleration:** MTP can be repurposed for speculative decoding. The acceptance rate of the second token prediction ranges from **85% to 90%**, enabling a significantly improved decoding speed of **1.8 times Tokens Per Second (TPS)**.

## Training Infrastructure and Optimization

The model was trained on a cluster of **2048 NVIDIA H800 GPUs**. The training utilized a meticulous combination of parallelism strategies: **16-way Pipeline Parallelism (PP)**, **64-way Expert Parallelism (EP)** spanning 8 nodes, and **ZeRO-1 Data Parallelism (DP)**. Tensor Parallelism (TP) was avoided to reduce complexity and memory overhead.

### FP8 Mixed Precision Training

DeepSeek-V3 validated an **FP8 mixed precision training framework** for the first time on an extremely large-scale model, reducing memory usage and accelerating training.

* **Data Format:** The **E4M3 format** (4-bit exponent, 3-bit mantissa) is adopted for all FP8 tensors, prioritizing mantissa over exponent bits for higher precision.
* **Fine-Grained Quantization:** To mitigate quantization errors from outliers, a fine-grained strategy is used:
  + **Activations:** Quantized on a **tile-wise 1x128** basis.
  + **Weights:** Quantized on a **block-wise 128x128** basis.
* **Increased Accumulation Precision:** To ensure numerical stability, intermediate results in FP8 GEMM operations are promoted to **FP32 registers on CUDA Cores** at specific intervals ($N\_C=128$ elements) for high-precision accumulation. This addresses the limitation of standard Tensor Core accumulation precision.
* **Stability:** The relative loss error of the FP8-trained model remained consistently **below 0.25%** compared to the BF16 baseline.

### DualPipe Parallelism

The custom **DualPipe** algorithm was designed for efficient pipeline parallelism, reducing pipeline bubbles compared to existing methods (Table 2 in source).

* **Computation-Communication Overlap:** DualPipe overlaps the computation and communication within forward and backward chunks, ensuring that both **all-to-all and PP communication can be fully hidden** during execution. This co-design results in a **near-zero all-to-all communication overhead**.
* **Communication Kernels:** Customized cross-node all-to-all communication kernels were developed to utilize InfiniBand (IB) and NVLink bandwidths efficiently. Only **20 SMs** are needed to fully utilize the bandwidths for communication.

## Pre-Training Strategy

DeepSeek-V3 was pre-trained on **14.8T high-quality and diverse tokens**.

* **Data Composition:** The corpus optimizes the ratio of **mathematical and programming samples** and expands multilingual coverage beyond English and Chinese.
* **Fill-in-Middle (FIM):** The **Prefix-Suffix-Middle (PSM) FIM strategy** was incorporated at a rate of **0.1** during pre-training to enhance the ability to predict middle text.
* **Long Context Extension:** Context length was progressively extended from 4K to 32K and then to **128K** using the YaRN method over two phases.

## Post-Training Enhancements

Post-training involved SFT and RL to align the base model with human preferences and enhance its capabilities.

* **Reasoning Distillation from DeepSeek-R1:** Advanced reasoning capabilities were distilled from the specialized **DeepSeek-R1 series** of models. The SFT training used samples generated with **system prompts designed to guide the model toward reflection and verification patterns** (distilled from R1). This significantly improved math and coding performance.
* **Self-Rewarding (Constitutional AI):** For general, hard-to-verify scenarios, the model employs the **constitutional AI approach** using the **voting evaluation results of DeepSeek-V3 itself as a feedback source** (“Self-Rewarding”) to enhance alignment.
* **RL Optimization:** Reinforcement Learning uses **Group Relative Policy Optimization (GRPO)**, which estimates the baseline from group scores instead of requiring a separate critic model.

## Evaluation and Performance Metrics (Chat Model)

DeepSeek-V3 is the **strongest open-source model currently available** and is competitive with closed-source frontier models.

| Benchmark (Metric) | DeepSeek-V3 Score | Comparative Detail | Source |
| --- | --- | --- | --- |
| **MMLU (EM)** | **88.5%** | Competitive with GPT-4o and Claude-Sonnet 3.5. |  |
| **MMLU-Redux (EM)** | **89.1%** | Surpasses its peers on this refined MMLU version. |  |
| **GPQA-Diamond (Pass@1)** | **59.1%** | Ranks just behind Claude-Sonnet 3.5 on this PhD-level testbed. |  |
| **MATH-500 (EM)** | **90.2%** | State-of-the-art for non-long-CoT models, outperforming the next best model by $\sim$10%. |  |
| **Codeforces (Percentile)** | **51.6%** | Top-performing model for coding competition benchmarks. |  |
| **SWE Verified (Resolved)** | **42.0%** | Trails Claude-Sonnet-3.5 but significantly outperforms other open-source models in engineering tasks. |  |
| **DROP (3-shot F1)** | **91.6%** | Outperforms all other models in this long-context understanding benchmark. |  |
| **C-SimpleQA (Correct)** | **64.8%** | Surpasses GPT-4o and Claude-Sonnet-3.5, highlighting strength in Chinese factual knowledge. |  |
| **IF-Eval (Prompt Strict)** | **86.1%** | Significantly outperforms predecessors in instruction-following ability. |  |

DeepSeek-V3 also achieved a **groundbreaking milestone** on the open-ended **Arena-Hard** benchmark with a win rate of **85.5%** against the GPT-4-0314 baseline, performing on par with Claude-Sonnet-3.5-1022.
