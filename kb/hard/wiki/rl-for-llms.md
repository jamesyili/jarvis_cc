---
concept: Reinforcement Learning for LLMs
tags: [rlhf, ppo, grpo, reinforce, reasoning, deepseek-r1]
sources:
  - kb/hard/raw/cameron-wolfe/ppo-for-llms-a-guide-for-normal-people.md
  - kb/hard/raw/cameron-wolfe/reinforce-easy-online-rl-for-llms.md
  - kb/hard/raw/cameron-wolfe/grpo-tricks-for-making-rl-actually-work.md
  - kb/hard/raw/cameron-wolfe/group-relative-policy-optimization-grpo.md
  - kb/hard/raw/cameron-wolfe/demystifying-reasoning-models.md
  - kb/hard/raw/sebastian-raschka/the-state-of-reinforcement-learning-for-llm-reasoning.md
  - kb/hard/raw/aman-ai/primers-rft.md
last_compiled: 2026-04-05
related: [reinforcement-learning, large-language-models, llm-evaluation]
---

# Reinforcement Learning for LLMs

## The Core Idea

Reinforcement learning (RL) treats an LLM as a **policy**: given a prompt (state), it generates a response (action), receives a reward, and updates its weights to maximize future rewards. Unlike supervised finetuning where the training signal is a labeled answer, RL lets a model explore its own completions and learn from outcome feedback.

RL has played two distinct roles in LLM history:
1. **Alignment** — training models to produce human-preferred outputs (RLHF)
2. **Reasoning** — training models to solve verifiable problems via long chain-of-thought (RLVR)

The algorithms, reward sources, and practical complexity differ significantly between these two regimes.

---

## The RLHF Pipeline

The canonical alignment procedure, popularized by InstructGPT (2022), has three stages:

**Stage 1 — Supervised Finetuning (SFT).** Finetune the pretrained base model on human-written demonstrations of desired behavior. This is not RL yet — it provides a well-behaved starting point for the RL phases.

**Stage 2 — Reward Model Training.** Collect a preference dataset: for each prompt, generate several responses and have annotators rank them. Train a reward model (RM) — typically a copy of the SFT model with a regression head instead of a language head — to predict a scalar preference score. The RM is trained with a ranking loss derived from the Bradley-Terry model, pushing it to assign higher scores to preferred completions.

**Stage 3 — PPO Finetuning.** Use the frozen RM as the reward signal and train the SFT model further with PPO. The RL objective is to maximize expected RM score while keeping the new policy close to the SFT reference via a KL penalty.

This three-step recipe was the dominant LLM post-training approach from 2022–2024. Its main liability: the reward model introduces a proxy that can be hacked, and collecting preference data is expensive.

---

## Proximal Policy Optimization (PPO)

PPO was the default RL optimizer for LLMs for years. It is complex and compute-heavy, but it works reliably.

### RL Formulation for LLMs

| RL Concept | LLM Mapping |
|---|---|
| Policy | The LLM itself |
| State | Prompt + tokens generated so far |
| Action | Next token predicted |
| Trajectory | Full completion |
| Reward | RM score (or verifiable signal) |

PPO uses the **MDP formulation** — each token is its own action with its own advantage estimate.

### The Surrogate Objective

PPO builds on the **policy ratio** `r_t(θ) = π_θ(a_t|s_t) / π_old(a_t|s_t)`, which measures how much more (or less) likely a token is under the current policy vs. the "old" policy (the policy at the start of the current update batch).

The PPO loss takes the minimum of a clipped and unclipped objective:

```
L_PPO = min(r_t(θ) · A_t,  clip(r_t(θ), 1-ε, 1+ε) · A_t)
```

This clipping mechanism enforces a **trust region**: if the advantage is positive and the policy ratio would grow too large, the gradient is zeroed. The model can't greedily over-update on any single action. A typical clipping range is `ε = 0.2`.

### KL Divergence Penalty

In addition to clipping, PPO for LLMs subtracts a KL divergence penalty from the reward to keep the policy close to the SFT reference model:

```
reward = RM_score - β · KL(policy || reference)
```

This prevents reward hacking and maintains language coherence. The KL is approximated per token as the difference in log probabilities between policy and reference.

### The Critic and Advantage Estimation

PPO uses a learned **value model (critic)** to estimate the advantage function `A(s, a) = Q(s, a) - V(s)`. The critic — another copy of the LLM with a regression head — predicts expected cumulative reward from any partial completion. It is updated alongside the policy via an MSE loss between predicted and actual rewards.

**Generalized Advantage Estimation (GAE)** is the standard approach: it blends 1-step TD residuals (low variance, high bias) with Monte Carlo estimates (low bias, high variance) via a mixing parameter λ. In practice, LLMs use outcome supervision (reward only at EOS), so most TD residuals reduce to differences in value function estimates between consecutive tokens.

### PPO's Memory Footprint

PPO requires four copies of the LLM in memory simultaneously:
1. The policy (actively trained)
2. The reference policy (frozen SFT model, for KL)
3. The critic (trained alongside policy)
4. The reward model (frozen)

This is the main reason simpler algorithms have displaced PPO for reasoning tasks.

---

## REINFORCE — Simpler Online RL

REINFORCE eliminates the critic entirely. It estimates the value function baseline by averaging rewards across the batch (or as a moving average over training), rather than using a learned model.

The policy gradient in REINFORCE is:
```
∇ = (reward - baseline) × Σ log π(token_t | context)
```

Where the baseline is just the mean reward in the current batch. No value model, no actor-critic complexity. The full completion is treated as a single action (bandit formulation), and the loss is computed over the entire sequence.

**REINFORCE Leave-One-Out (RLOO)** improves on vanilla REINFORCE by sampling K completions per prompt. The baseline for completion i is the average reward of the other K-1 completions to that same prompt. This prompt-specific baseline lowers variance substantially compared to a global average. RLOO reduces memory by ~50% vs. PPO and runs 2-3× faster, while matching PPO in quality.

Key insight: the high variance of REINFORCE relative to PPO turns out not to matter much for finetuning pretrained LLMs. The model already has a strong prior from pretraining. PPO's complexity was designed for training from scratch, which is a harder RL problem.

---

## GRPO — Group Relative Policy Optimization

GRPO is the algorithm behind DeepSeek-R1 and most modern open reasoning models. It preserves PPO's clipped surrogate loss but replaces the critic with a group-based advantage estimate.

### Advantage Without a Critic

For each prompt, GRPO samples a **group** of G completions. The advantage for completion i is:

```
A_i = (r_i - mean(r_1,...,r_G)) / std(r_1,...,r_G)
```

This normalized, group-relative advantage replaces GAE entirely. No separate value model is needed. Every token in completion i gets the same advantage score, and the PPO clipping mechanism handles per-token weighting via the policy ratio.

### Differences from PPO

| Feature | PPO | GRPO |
|---|---|---|
| Critic / value model | Yes (4 LLMs in memory) | No (2-3 LLMs in memory) |
| Advantage estimation | GAE with learned critic | Group-relative normalization |
| KL divergence | Subtracted from reward | Added as penalty to loss (often omitted for reasoning) |
| Completions per prompt | 1 | G (typically 8–16) |
| Primary use | RLHF alignment | RLVR reasoning |

GRPO frequently omits KL divergence entirely for reasoning tasks. The model's behavior is expected to diverge significantly from the SFT reference as it learns long chain-of-thought reasoning — imposing a KL constraint would hamper that evolution.

### RLVR: Verifiable Rewards Replace the Reward Model

Reinforcement Learning with Verifiable Rewards (RLVR) pairs GRPO with rule-based verification instead of a neural reward model. For math, string-match the boxed answer. For code, run tests in a sandbox. This eliminates reward hacking and the expense of training and serving a separate RM.

The reward function in DeepSeek-R1-Zero has just two components:
- **Accuracy reward**: binary correct/incorrect
- **Format reward**: `<think>...</think>` structure enforced

From these simple rewards alone, the model learns sophisticated reasoning behavior through exploration.

---

## Reasoning Models: The DeepSeek-R1 Pipeline

DeepSeek-R1 demonstrated that you can build a frontier reasoning model via a carefully staged combination of SFT and RL. The pipeline has four stages:

**Stage 1 — Cold Start (Reasoning-Oriented SFT).** Finetune DeepSeek-v3-Base on "thousands" of long chain-of-thought examples. These examples teach the model what a reasoning trace looks like — format, self-reflection style, summarization of the thought process. This provides a stable initialization for RL rather than starting from a raw base model.

**Stage 2 — Reasoning-Oriented RL (GRPO + RLVR).** Run large-scale GRPO on verifiable math/code problems. The model self-evolves: it learns to generate longer, more structured reasoning traces, naturally develops self-reflection and backtracking behaviors, and steadily improves on hard benchmarks (AIME 2024 accuracy grows from ~15% to ~70%+).

**Stage 3 — Rejection Sampling + General SFT.** Use the Stage 2 model to generate 600K reasoning trajectories + 200K general-purpose examples (writing, translation, etc.). Filter for correctness and quality. Finetune on this 800K-example dataset to broaden the model's capabilities beyond pure math/code.

**Stage 4 — General-Purpose RLHF.** Final RL round with mixed rewards: verifiable rewards for reasoning tasks, neural reward models for general helpfulness and harmlessness. Aligns the model for production use.

**DeepSeek-R1-Zero** is the ablation: pure RL from the base model, no SFT. It still develops impressive reasoning capabilities, but suffers from language mixing and poor readability. The cold start data in R1 primarily fixes these quality-of-life issues.

**Distilled variants** are trained by taking Qwen-2.5 or LLaMA-3 base models and running SFT on the 800K examples from Stage 3. No RL involved. Smaller distilled models outperform GPT-4o on reasoning benchmarks and match o1-mini despite being 7B–32B parameters.

---

## Practical Tricks for GRPO

Vanilla GRPO has known failure modes at scale. Research (particularly DAPO, Dr. GRPO) identified and fixed them:

**1. Entropy collapse.** The standard PPO clip range `[1-ε, 1+ε]` suppresses low-probability (exploration) tokens. Fix: decouple upper and lower clip bounds. Use `[1-ε_low, 1+ε_high]` with `ε_high > ε_low` (e.g., 0.28 vs. 0.2). This prevents the token distribution from collapsing to near-deterministic outputs and preserves exploration.

**2. Zero-gradient from all-correct groups.** As training progresses, more groups have all-correct completions → zero advantage for every token → zero gradient → smaller effective batch → noisier updates. Fix: dynamic sampling — over-sample prompts and filter out all-correct groups until a full, useful batch is assembled.

**3. Token-level vs. sample-level loss aggregation.** Standard GRPO averages loss within each completion first, then averages across completions. This underweights individual tokens in longer responses. Fix: aggregate directly across all tokens with equal weight. This also reduces the length bias that causes incorrect responses to grow unnecessarily long.

**4. Overlong sample handling.** Don't negatively reward truncated completions with a hard −1. If the reasoning process was valid but just too long, a hard penalty confuses the model. Fix: mask truncated samples from the gradient entirely, or use a soft length-based penalty that scales the negative reward linearly within a "punishment interval."

**5. Data quality and batch size.** GRPO needs large batches and diverse difficulty distribution. Filter out trivially easy prompts (zero gradient) and trivially hard ones (never correct, never a learning signal). Multiple-choice formats are also dangerous — easy to guess correctly at random, which corrupts the reward signal.

**Monitoring health.** Track: (1) average response length (should increase steadily); (2) training reward (should increase stably); (3) entropy of the token distribution (should stay in a reasonable range, not collapse); (4) held-out validation accuracy (guards against reward hacking).

---

## Reward Modeling

Reward models are LLMs with a regression head that predict a scalar preference score. They are trained with a ranking loss:

```
L_RM = -log σ(r_chosen - r_rejected)
```

This pushes the model to assign higher scores to preferred completions. The RM is trained once on preference data and then frozen during PPO training.

**Key distinction from the critic:** The RM scores complete responses and stays frozen. The critic scores partial completions and is actively updated alongside the policy.

**Reward hacking** is the main risk: with enough RL training, the policy learns to exploit weaknesses in the RM rather than genuinely improving. Symptoms include responses that score well on the RM but are obviously bad to humans. RLVR with verifiable rewards largely sidesteps this problem.

---

## Algorithm Comparison

| | PPO | REINFORCE/RLOO | GRPO |
|---|---|---|---|
| Memory (# LLMs) | 4 | 3 | 2–3 |
| Advantage estimate | GAE (learned critic) | Mean reward baseline | Group normalization |
| Completions/prompt | 1 | 1 (REINFORCE), K (RLOO) | G (8–16) |
| Complexity | High | Low | Medium |
| Primary domain | RLHF alignment | RLHF alignment | RLVR reasoning |
| KL handling | Subtract from reward | Subtract from reward | Add to loss (often omitted) |

---

## Cross-References

- [[hard/wiki/transformer-architecture|Transformer Architecture]] — the underlying model architecture being trained
- [[hard/wiki/llm-evaluation|LLM Evaluation]] — metrics and benchmarks used to measure RL training progress
- [[hard/wiki/retrieval-augmented-generation|RAG]] — often combined with reasoning models for knowledge-grounded tasks
