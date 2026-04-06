---
concept: Mixture of Experts (MoE)
tags: [moe, sparse-models, expert-routing, deepseek, scaling]
sources:
  - kb/hard/raw/aman-ai/primers-mixture-of-experts.md
  - kb/hard/raw/cameron-wolfe/mixture-of-experts-moe-llms.md
  - kb/hard/raw/aman-ai/primers-deepseek-v3.md
last_compiled: 2026-04-05
related: [transformer-architecture, distributed-training, large-language-models]
---

# Mixture of Experts (MoE)

Mixture of Experts is the dominant architectural pattern for scaling large language models beyond what is computationally tractable with dense transformers. The core insight: replace each feed-forward layer with a set of parallel "expert" networks and route each token to only a small subset of them. Total parameter count grows, but per-token compute stays roughly constant.

## The Scaling Problem MoE Solves

Dense transformers activate all parameters for every input token. As model size grows, training and inference FLOPs scale linearly with parameter count — creating an increasingly unaffordable compute bill at trillion-parameter scale. MoE decouples *model capacity* from *per-token compute* by conditionally activating only a fraction of parameters. A model can have 671B total parameters (DeepSeek-V3) while only computing with 37B of them per token.

## Core Architecture

### Experts

In a standard transformer, each block contains a multi-head attention sublayer followed by a feed-forward network (FFN). MoE replaces the FFN with a collection of `N` independent FFNs, each with its own weights, called **experts**. Every `P`-th layer is converted to an MoE layer; other layers remain dense. Common strides: P=2 (every other layer), P=4 (every fourth layer).

The output of an MoE layer for a single token is the weighted sum of the outputs from the selected experts:

```
y(x) = sum_{i in Top-k(g(x))} g_i(x) * E_i(x)
```

Where `g(x)` is the routing probability vector, `Top-k(g(x))` selects the top-k experts, and `E_i(x)` is the i-th expert's output.

### Router

The routing mechanism maps each token to experts. In its simplest form:
1. Apply a linear projection to the token vector to produce a logit vector of size N.
2. Apply softmax to get a probability distribution over experts.
3. Select the top-k experts (k=1 in Switch Transformer; k=2 in Mixtral, Llama).

The weighted combination of the top-k expert outputs becomes the layer's output for that token. All components — attention, experts, and router — are trained jointly.

### Shared vs. Routed Experts

A refinement introduced in DeepSeek architectures: designate a small number of **shared experts** that *every* token passes through, plus a larger pool of **routed experts** that tokens are selectively sent to. Shared experts capture common knowledge that would otherwise be redundantly stored across routed experts, improving parameter efficiency and reducing redundancy.

## Load Balancing

The naive router converges to a "collapse" regime: a small number of popular experts receive most tokens, while others are ignored. This is self-reinforcing — favored experts train more and thus get selected more. Two auxiliary losses prevent this:

**Importance loss** (Shazeer et al. 2017): penalizes high variance in expert importance scores (summed routing probabilities across a batch).

**Load balancing loss** (Switch Transformer / ST-MoE): directly penalizes uneven token assignment by taking the dot product of (fraction of router probability per expert) and (fraction of tokens dispatched per expert). Minimized when both are uniform.

**Router z-loss** (ST-MoE): additionally penalizes large logit values before softmax to prevent numerical instability from exploding exponentials at scale.

**Auxiliary-loss-free balancing** (DeepSeek-V3): introduces a dynamic per-expert bias term used only during routing decisions. This avoids degrading task performance from auxiliary loss gradients while still achieving load balance. DeepSeek-V3 reports greater expert specialization with this approach.

## Expert Capacity

Static batch computation on hardware requires fixed buffer sizes. **Expert capacity** defines the maximum number of tokens that can be routed to any single expert per batch:

```
expert_capacity = (tokens_per_batch / num_experts) * capacity_factor
```

A capacity factor of 1.0 assumes perfectly balanced routing. Setting it above 1.0 (e.g., 1.25–2.0) provides slack for imbalanced distributions. Tokens that overflow capacity are **dropped** — they bypass the expert and propagate through the residual connection unchanged. Excessive token dropping degrades quality; it should be monitored and kept low. DeepSeek-V3 eliminates token dropping entirely through its effective load balancing.

## Historical Evolution

| Model | Year | Key Contribution |
|-------|------|-----------------|
| Sparsely-Gated MoE (Shazeer et al.) | 2017 | First large-scale sparse MoE with top-k routing and importance loss |
| GShard | 2020 | Distributed MoE training across thousands of TPUs |
| Switch Transformer | 2021 | Simplified to top-1 routing; 7× pretraining speedup over dense baseline |
| ST-MoE | 2022 | Router z-loss; stable training at scale |
| Mixtral 8×7B | 2024 | Open-source MoE: 47B total / 13B active params, top-2 routing per layer |
| DeepSeek-V2/V3 | 2024/2025 | 671B total / 37B active; auxiliary-loss-free balancing, shared experts, MLA attention |

## Active vs. Total Parameters Trade-off

The central MoE trade-off: more total parameters → better model quality; fixed active parameters → constant inference compute. Mixtral 8×7B has 47B total parameters but only 13B are active per token, making it comparable in inference cost to a ~13B dense model while performing closer to a 47B model. DeepSeek-V3 pushes this further: 671B total, 37B active.

**Inference advantages:** At low batch sizes, inference is faster because fewer FLOPs per token. At high batch sizes, throughput scales because experts can be parallelized across devices.

**Inference disadvantages:** All parameters must reside in memory even though most are inactive per token. A 671B MoE needs enough GPU memory to hold 671B parameters — this is the primary hardware constraint.

## Expert Parallelism

For distributed training and inference, experts are sharded across devices. Tokens are dispatched via all-to-all communication, processed by the assigned expert (possibly on a different device), and the results are gathered back. This creates a compute-communication trade-off: more experts = better model quality = more all-to-all communication overhead. DeepSeek-V3 uses 64-way expert parallelism across 8 nodes with custom RDMA/InfiniBand kernels that achieve near-zero all-to-all overhead through compute-communication overlap.

## Expert Specialization

Do experts learn distinct skills? Empirically: not cleanly by topic domain. Analysis of Mixtral 8×7B shows that routing does not cluster by subject matter (e.g., science vs. sports). However, structured behavior exists: tokens with similar syntactic roles or positions (e.g., code indentation tokens, Python `self` keyword) tend to be routed to the same expert. Experts appear to specialize in syntactic/structural patterns rather than semantic topics.

## Limitations

- **Memory-intensive inference**: All parameters must be loaded even when inactive.
- **Training instability**: More sensitive to hyperparameter choices and initialization than dense models.
- **Hard to fine-tune**: Higher risk of overfitting on small datasets; requires careful regularization.
- **Latency variability**: Routing decisions vary per token, creating less predictable latency.
- **Low/mixed precision sensitivity**: Routing operations are numerically sensitive; full float32 often required for the router.

## Sources

- Aman.ai, "Primers: Mixture of Experts" — `kb/hard/raw/aman-ai/primers-mixture-of-experts.md`
- Cameron Wolfe, "Mixture-of-Experts (MoE) LLMs" — `kb/hard/raw/cameron-wolfe/mixture-of-experts-moe-llms.md`
- Aman.ai, "Primers: DeepSeek V3" — `kb/hard/raw/aman-ai/primers-deepseek-v3.md`
