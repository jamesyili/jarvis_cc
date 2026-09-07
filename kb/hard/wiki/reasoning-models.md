---
concept: Reasoning Models & Inference-Time Scaling
tags: [reasoning, o1, deepseek-r1, inference-scaling, chain-of-thought]
sources:
  - kb/hard/raw/sebastian-raschka/understanding-reasoning-llms.md
  - kb/hard/raw/sebastian-raschka/categories-of-inference-time-scaling-for-improved-llm-reasoning.md
  - kb/hard/raw/cameron-wolfe/demystifying-reasoning-models.md
last_compiled: 2026-04-05
related: [rl-for-llms, large-language-models, prompt-engineering]
understanding: 1  # very little exposure / unknown (default)
relevance: 2  # somewhat / potentially relevant
knowledge_updated: 2026-09-07
---

# Reasoning Models & Inference-Time Scaling

Reasoning models represent a qualitative shift from standard LLMs: rather than generating a direct answer, they spend variable compute "thinking" through a problem via an extended internal chain of thought before producing a final response. This gives rise to a new scaling axis — inference-time compute — that operates independently of model size or training duration.

## What Makes a Reasoning Model

A reasoning model is an LLM specialized to excel at multi-step tasks: math competition problems, complex coding challenges, scientific reasoning, logical puzzles. The defining behavioral property is a **long chain of thought (long CoT)** — a several-thousand-token internal reasoning trace in which the model:

- Decomposes problems into sub-problems
- Works through each part step by step
- Detects and corrects errors in its own reasoning
- Explores alternative solution paths
- Self-verifies before committing to an answer

This long CoT differs from standard CoT prompting (see [[hard/wiki/prompt-engineering|Prompt Engineering]]) in length (thousands vs. dozens of tokens), purpose (internal computation vs. human-readable explanation), and source (trained via RL rather than prompted at inference time).

OpenAI's o1 hides the raw CoT from users; DeepSeek-R1 exposes it in `<think>` tags. Either way, the reasoning trace is the mechanism, not the product.

## Training Approaches

Four approaches exist for building reasoning models, ranging from purely inference-time to purely training-time:

### 1. Inference-Time Scaling (No Training Required)

The simplest approach: spend more compute at inference time on a standard LLM. Techniques:
- **CoT prompting**: "Think step by step" elicits reasoning without training changes. Effective for moderately complex tasks on large models.
- **Best-of-N / rejection sampling**: sample multiple responses, pick the best one (via a reward model, majority vote, or highest sequence probability). Performance improves with N, up to a point.
- **Self-consistency**: sample K diverse reasoning paths, take the majority answer.
- **Search (beam, MCTS)**: explore multiple solution branches, guided by a process reward model.

These methods are training-free but expensive — generating 400 candidates costs 400× the compute of one generation.

### 2. Pure Reinforcement Learning (RLVR)

DeepSeek-R1-Zero demonstrated that reasoning can *emerge* from pure RL applied directly to a pretrained base model — no SFT required ("cold start"). The RL setup uses **verifiable rewards**:
- **Accuracy reward**: deterministic rule-based check against ground truth (e.g., exact string match for math answers, test case execution for code).
- **Format reward**: LLM judge verifies structural constraints (e.g., reasoning appears inside `<think>` tags).

No neural reward model is used — RLVR with rule-based rewards avoids reward hacking and allows much longer training runs than RLHF. The optimizer is GRPO, which eliminates the critic/value model by normalizing rewards within a group of sampled responses.

The "Aha!" moment: during pure RL training, the model spontaneously begins generating internal reasoning traces without being explicitly trained to do so. This demonstrates that extended thinking is a learnable behavior that RL can elicit from a sufficiently capable base model.

### 3. SFT + RL (Full Pipeline)

The highest-performing approach, used for DeepSeek-R1 (the flagship model) and likely OpenAI's o1:

1. **Cold-start SFT**: use R1-Zero to generate CoT training data; fine-tune the base model on this data.
2. **RL round 1**: apply GRPO with accuracy + format + consistency rewards. Consistency reward penalizes language mixing (switching languages mid-response).
3. **Second SFT data collection**: sample 600K CoT examples from the RL checkpoint + 200K knowledge examples.
4. **RL round 2**: final RL stage with both verifiable rewards (math/code) and human preference labels (general questions).

This pipeline yields substantial gains over pure RL: DeepSeek-R1 dramatically outperforms R1-Zero on all benchmarks. The SFT stages provide structured initialization that makes RL more stable and effective.

### 4. Distillation (SFT-Only, Smaller Models)

For building cost-effective smaller reasoning models: fine-tune a smaller model (e.g., Llama 8B, Qwen 7B) on the 800K SFT dataset generated from DeepSeek-R1. No RL is applied. These "distilled" models achieve surprisingly strong reasoning performance relative to their size — DeepSeek-R1-Distill-Llama-70B competes with o1-mini.

Key limitation: distillation always depends on an existing stronger model for data generation. It cannot drive further capability frontiers.

**Distillation vs. pure RL for small models**: For models under ~30B parameters, distillation (pure SFT on strong CoT data) substantially outperforms applying pure RL from scratch. Pure RL appears to require scale to produce strong emergent reasoning. Above ~70B, both approaches become more viable.

## Benchmarks for Reasoning Models

Standard LLM benchmarks (GSM8K, MMLU) are saturated by reasoning models — reasoning models need harder evals:

- **AIME**: US Math Olympiad qualifying exam. GPT-4o: 12%; o1: 74–93%; o3: ~97%.
- **GPQA Diamond**: PhD-level multiple-choice science. Experts score ~65%; GPT-4o: ~50%; o1: ~77%.
- **ARC-AGI**: Grid-based pattern recognition puzzles; described as "North Star toward AGI." GPT-4o: 5%; o3 high-compute: 87.5% — first model to exceed human-level performance of 85%.
- **Codeforces**: Competitive programming. o3: Elo 2727, top-200 among competitive programmers.

## Inference-Time Compute: Taxonomy

Test-time scaling methods break into two dimensions:

**Generate more tokens (sequential compute):**
- Long CoT: model internally generates thousands of reasoning tokens before answering.
- Self-refinement: model generates a draft, then critiques and revises iteratively.

**Generate multiple outputs (parallel compute):**
- Best-of-N: sample N responses, select by reward model or majority vote.
- Self-consistency: majority vote over K diverse reasoning paths.
- MCTS / beam search: explicit tree search guided by a process reward model.

Mixing both (long CoT + best-of-N) yields the best results. OpenAI's o3 is believed to use both training-time RL and aggressive inference-time scaling, which contributes to its higher per-token cost vs. DeepSeek-R1.

## When to Use Reasoning Models

Reasoning models are the right tool for:
- Complex math, competitive programming, and logic puzzles
- Scientific reasoning requiring multi-step deduction
- Tasks where verifiability enables RL training or answer checking

They are overkill (expensive and sometimes worse due to "overthinking") for:
- Simple factual questions
- Summarization and translation
- Tasks requiring broad world knowledge rather than step-by-step inference

## Practical Considerations

**Cost**: Reasoning models generate far more tokens per query. DeepSeek-R1 is cheaper at inference than o1 partly because it invests more in training-time reasoning rather than test-time search.

**Budget models**: Sky-T1 (32B, trained for $450 on 17K SFT samples) and TinyZero (3B, pure RL for <$30) show that modest reasoning capabilities are achievable at low cost.

**Overhead on non-reasoning tasks**: Forcing reasoning on simple tasks can degrade performance — the model "overthinks" and introduces errors. Use routing to direct queries to reasoning models only when needed.

## Sources

- Sebastian Raschka, "Understanding Reasoning LLMs" — `kb/hard/raw/sebastian-raschka/understanding-reasoning-llms.md`
- Sebastian Raschka, "Categories of Inference-Time Scaling for Improved LLM Reasoning" — `kb/hard/raw/sebastian-raschka/categories-of-inference-time-scaling-for-improved-llm-reasoning.md`
- Cameron Wolfe, "Demystifying Reasoning Models" — `kb/hard/raw/cameron-wolfe/demystifying-reasoning-models.md`
