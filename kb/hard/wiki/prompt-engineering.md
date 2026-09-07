---
concept: Prompt Engineering & In-Context Learning
tags: [prompting, few-shot, chain-of-thought, icl, temperature]
sources:
  - kb/hard/raw/aman-ai/primers-prompt-engineering.md
  - kb/hard/raw/lilian-weng/prompt-engineering.md
  - kb/hard/raw/chip-huyen/generation-configurations-temperature-top-k-top-p-and-test-time-compute.md
last_compiled: 2026-04-05
related: [large-language-models, retrieval-augmented-generation]
understanding: 2  # basic understanding (assumed where James's background applies)
relevance: 2  # somewhat / potentially relevant
knowledge_updated: 2026-09-07
---

# Prompt Engineering & In-Context Learning

Prompt engineering is the practice of designing inputs to a language model — without changing its weights — to steer its outputs toward desired results. It is applied across tasks ranging from classification and translation to complex multi-step reasoning. At its core, prompt engineering exploits **in-context learning (ICL)**: the ability of large models to adapt their behavior based on examples and instructions provided within the input context.

## Prompting Fundamentals

### Zero-Shot Prompting

Simply describe the task and let the model respond. No examples provided. Works best for well-understood tasks on capable models:

```
Classify the sentiment: "I loved the movie."
Sentiment:
```

Zero-shot performance scales dramatically with model size and instruction-tuning quality.

### Few-Shot Prompting

Provide 1–5 (input, output) demonstrations before the actual query. The model infers the pattern and applies it:

```
Text: "The food was excellent." → Sentiment: Positive
Text: "Terrible service." → Sentiment: Negative
Text: "It was okay." → Sentiment:
```

Few-shot consistently outperforms zero-shot on complex or format-specific tasks. Key sensitivities:
- **Example quality** dominates effect size — bad examples hurt more than no examples.
- **Label balance**: uneven label distribution in examples creates majority label bias.
- **Ordering**: the last example's label is often over-weighted (recency bias).
- **Example selection**: semantically similar examples (retrieved via kNN on embeddings) outperform random selection.

### Instruction Prompting

Rather than demonstrating via examples, describe the task requirement directly with specific, precise language:

```
Label the sentiment of the following movie review as "positive" or "negative".
Review: "I'll bet the video game is more fun than the film."
Label:
```

Instruction-tuned models (GPT-4, Claude, Llama) are optimized for this format. Avoid negative instructions ("don't do X") — specify desired behavior positively ("do Y instead").

## Chain-of-Thought (CoT) Prompting

CoT prompting elicits step-by-step reasoning before the final answer. Introduced by Wei et al. (2022). CoT substantially improves accuracy on multi-step math, logical reasoning, and multi-hop QA — but only for models above ~50–100B parameters and for tasks that are actually complex enough to benefit.

**Zero-shot CoT**: Append "Let's think step by step" to the query. The model generates its reasoning chain spontaneously. Introduced by Kojima et al. (2022):

```
Q: If I have 10 apples, give 2 away, buy 5 more, and eat 1, how many remain?
A: Let's think step by step.
```

**Few-shot CoT**: Provide demonstrations that include reasoning chains, not just final answers. More reliable than zero-shot CoT for hard tasks.

**Auto-CoT**: Automatically generate CoT demonstrations by (1) clustering questions by topic and (2) applying zero-shot CoT to representative examples from each cluster. Reduces the manual effort of writing demonstrations.

**Practical tips:**
- Complexity in the reasoning chain matters more than number of steps. Longer, more explicit chains improve performance on complex problems.
- Newlines between steps work better than numbered steps or semicolons.
- CoT can be counterproductive on simple tasks — it can introduce errors through "overthinking."

## Advanced CoT Variants

### Self-Consistency
Sample multiple (diverse) reasoning chains for the same query, then take a majority vote over the final answers. Substantially more reliable than greedy single-path CoT, especially on math and logic. The diversity of paths matters: use temperature > 0 during sampling (temperature = 0.7 is commonly recommended).

### Tree of Thoughts (ToT)
Decomposes a problem into multiple thought steps, generates multiple candidate thoughts at each step, and searches through the resulting tree using BFS or DFS. A classifier (prompted LLM) scores partial solutions. Effective for tasks requiring exploration and backtracking.

### ReAct (Reason + Act)
Interleaves reasoning steps with actions (tool calls, web searches). The model generates a Thought, then an Action, then observes the result and updates its reasoning. Enables grounded reasoning over external knowledge without fine-tuning.

### Least-to-Most Prompting
Decompose a complex problem into a sequence of simpler sub-problems, solve them in order, and use each solution as context for the next. Useful when problems have clear hierarchical structure.

## Generation Configuration Parameters

Understanding sampling parameters is critical to controlling model outputs:

### Temperature

Temperature `T` divides the logits before softmax:

```
P_i = exp(x_i / T) / sum_j(exp(x_j / T))
```

- `T < 1` (e.g., 0.2): sharpens distribution, model almost always picks the highest-probability token. More deterministic, consistent, sometimes repetitive.
- `T = 1`: standard softmax, unmodified distribution.
- `T > 1` (e.g., 1.5–2.0): flattens distribution, increases probability of rarer tokens. More creative and diverse, but higher risk of incoherence.
- `T = 0`: argmax (greedy decoding), fully deterministic.

Recommended values: 0.7 for creative tasks, 0–0.2 for factual/structured tasks.

### Top-k Sampling

Restricts the candidate pool to the top-k most likely tokens, then renormalizes and samples. Reduces computation by avoiding softmax over the full vocabulary. A smaller k makes output more predictable; larger k increases diversity. Common range: k = 50–500.

**Limitation**: fixed k doesn't adapt to context. If only 2 reasonable continuations exist (yes/no question), k=50 introduces noise. If 500 reasonable continuations exist, k=50 is too restrictive.

### Top-p (Nucleus Sampling)

Selects the minimum set of tokens whose cumulative probability exceeds p, then samples from that set:

```
Select tokens until cumulative P(token) ≥ p
```

- `p = 0.9`: select tokens covering 90% of the probability mass. Dynamic — considers 2 tokens for binary choices, hundreds for open-ended queries.
- Common range: 0.9–0.95.

Top-p adapts more gracefully than top-k across different contexts, which is why it has become the more widely used default.

### Temperature, top-k, and top-p are typically combined: temperature reshapes the distribution, then top-k/p restricts the sampling pool. The order matters: apply temperature first, then apply top-k or top-p to the reshaped distribution.

## Structured Outputs

For production use, prompts often need to produce parseable structured output (JSON, SQL, specific formats). Three approaches:

1. **Prompting**: instruct the model to output JSON. Simple but unreliable — no guarantee of validity.
2. **Constrained sampling**: at token generation time, filter the logit vector to keep only tokens consistent with the target grammar (e.g., JSON grammar). Tools like `guidance` and `outlines` implement this.
3. **Fine-tuning**: train the model on examples with the desired format. Most reliable for critical production use.

## Role Prompting and System Instructions

Defining a persona or role in the system prompt influences tone, format, and behavior:

```
You are an expert data scientist reviewing a statistical analysis.
Your feedback should be technical, specific, and constructive.
```

Role prompting is not magic — model capabilities don't expand — but it can shift output toward more appropriate registers and improve adherence to domain conventions.

## Test-Time Compute via Sampling

Generating multiple outputs and selecting the best is a form of inference-time scaling (see [[hard/wiki/reasoning-models|Reasoning Models]]). Selection strategies:
- **Highest average log-probability**: pick the output with the highest mean token log-prob (normalizing for length).
- **Reward model scoring**: pass candidates through a reward model, pick the highest-scored.
- **Majority vote**: for tasks with verifiable answers (math, classification), take the modal answer.

Performance improves with N, but diminishing returns set in (OpenAI observed saturation around N=400 for math verifiers). In production, N=3–5 is a practical sweet spot.

## Prompt Decomposition

For complex tasks, decompose into sub-prompts and chain them:
- **Skeleton of Thought**: first generate an outline, then fill in each point in parallel.
- **Recursive prompting**: iteratively refine or expand a draft through multiple LLM calls.
- **Chain-of-Note / Chain-of-Knowledge**: augment reasoning steps with retrieved evidence.

## Sources

- Aman.ai, "Primers: Prompt Engineering" — `kb/hard/raw/aman-ai/primers-prompt-engineering.md`
- Lilian Weng, "Prompt Engineering" — `kb/hard/raw/lilian-weng/prompt-engineering.md`
- Chip Huyen, "Generation Configurations: Temperature, Top-k, Top-p, and Test-Time Compute" — `kb/hard/raw/chip-huyen/generation-configurations-temperature-top-k-top-p-and-test-time-compute.md`
