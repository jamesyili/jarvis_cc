---
concept: LLM Evaluation
tags: [evals, llm-as-judge, benchmarks, evaluation, ai-quality]
sources:
  - kb/hard/raw/eugene-yan/product-evals-in-three-simple-steps.md
  - kb/hard/raw/eugene-yan/task-specific-llm-evals-that-do-dont-work.md
  - kb/hard/raw/eugene-yan/evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge.md
  - kb/hard/raw/aman-ai/primers-llm-as-a-judge-autoraters.md
  - kb/hard/raw/aman-ai/primers-llmvlm-benchmarks.md
  - kb/hard/raw/cameron-wolfe/applying-statistics-to-llm-evaluations.md
  - kb/hard/raw/cameron-wolfe/the-anatomy-of-an-llm-benchmark.md
  - kb/hard/raw/sebastian-raschka/understanding-the-4-main-approaches-to-llm-evaluation-from-scratch.md
  - kb/hard/raw/nathan-lambert/opus-46-codex-53-and-the-post-benchmark-era.md
last_compiled: 2026-04-05
related: [hard/wiki/learning-to-rank, hard/wiki/recommendation-systems, hard/wiki/large-language-models]
---

# LLM Evaluation

Evaluation is the primary feedback loop for LLM development. The thesis is simple: you cannot improve what you cannot measure, and the quality of your evals determines the quality of your iteration cycle. In production, evals are not a one-time audit — they are the development loop itself.

## Four Main Approaches

**1. Multiple-choice / automated metrics.** Present the model with structured questions (e.g., MMLU's 57-subject, 16K-question dataset) and check accuracy against a known answer key. Fast and deterministic. The limitation: only tests selection from predefined options. High MMLU scores don't guarantee real-world utility; low scores do signal knowledge gaps. Variants include log-probability scoring (measuring confidence on each option) rather than just letter generation.

**2. Verifier-based / answer extraction.** The model generates a free-form answer; a verifier (code interpreter, math checker) extracts and validates the final answer against a ground truth. Powers reasoning model evaluation (MATH, GSM8K, AIME). Enables unlimited programmatic problem generation. Constraint: only applies to verifiable domains — math, code, logic. Cannot measure style, tone, or helpfulness.

**3. LLM-as-judge.** An LLM evaluates another LLM's output using a structured scoring prompt. Scales human-like evaluation to arbitrary volumes at low cost. The dominant approach for open-ended generation tasks (summarization, dialogue, instruction following) where automated metrics fail. See section below for setup and failure modes.

**4. Human preference / leaderboards.** Users or trained annotators compare two model outputs and vote for the preferred one. Aggregated via Elo ratings into a ranked leaderboard (e.g., LM Arena). Most valid signal for real-world usability, but expensive, slow, and subject to population bias in who votes.

These divide into two meta-categories: **benchmark-based** (methods 1–2, produce accuracy scores) and **judgment-based** (methods 3–4, produce preference rankings).

## LLM-as-Judge: Setup and Calibration

The basic setup: provide the judge model with the input, the response, and a scoring rubric; ask it to return a score or binary verdict. Three scoring formats:

- **Pointwise**: score a single response on a scale (e.g., 1–5). Simpler, maps to LTR pointwise ranking.
- **Pairwise**: compare two responses and pick the better one. Higher agreement with human preferences, but combinatorially expensive across many outputs.
- **Listwise**: rank multiple responses simultaneously. Efficient but requires careful prompt design.

**Calibration against human raters** is the validation step that makes or breaks LLM judges. The goal is to measure how well judge scores correlate with human judgments on the same items. High-agreement configurations typically use stronger judge models (GPT-4 class), chain-of-thought critique before scoring, well-specified rubrics, and reference answers where available.

**Failure modes:**

- *Position bias*: judges prefer responses presented first (or last), regardless of quality. Mitigate by running both orders and averaging.
- *Verbosity bias*: judges reward longer responses even when quality is equivalent. Explicitly instruct against length preference.
- *Self-preference*: a judge model assigned GPT-4 favors GPT-4 outputs; Claude judges favor Claude outputs. Use different-family judge models or a panel.
- *Prompt sensitivity*: small wording changes in the scoring prompt cause large score swings. Use stable, battle-tested rubrics.
- *Reward hacking*: models fine-tuned to maximize judge scores learn surface features the judge rewards, not actual quality. Use held-out human evals for final validation.
- *Over-confidence / hallucination blindness*: judges may not catch subtle factual errors, especially in domains requiring expert knowledge.

**Panel of judges** (jury approach) addresses single-judge weaknesses by aggregating scores from multiple different models. Increases robustness at the cost of inference budget.

## Benchmark Anatomy and Failure Modes

A benchmark is a finite sample drawn from the super-population of all possible evaluation questions for a skill. Performance on the benchmark estimates performance on the underlying skill — not the benchmark itself. This framing is important: optimizing on the benchmark surface is not the same as improving the skill.

**Key design elements:** domain taxonomy (enables per-domain debugging), data sourcing strategy (expert-curated vs. web-scraped), question format (multiple choice vs. generative), difficulty calibration, and data quality verification.

**Saturation** happens when frontier models all cluster near ceiling performance, making the benchmark unable to discriminate between them. MMLU was effectively saturated by 2024; BIG-Bench Hard by early 2025. The response is iterative hardening: MMLU → MMLU-Pro (harder questions, 4 options → 10 options, difficulty filtering) → GPQA (expert-written, Google-proof, 65% expert / 34% non-expert accuracy). BIG-Bench Hard → BIG-Bench Extra Hard (same reasoning categories, dramatically harder tasks).

**Contamination** is benchmark data appearing in training sets, inflating scores. Mitigations: hold out test sets, generate questions programmatically after the training cutoff (MathArena evaluates on competition problems shortly after release), and use dynamic benchmarks that can add fresh problems continuously.

**Gaming / overfitting**: models can be selected during development specifically because they score well on popular benchmarks (IFEval being one documented example). The benchmark becomes part of the training signal. IFBench (58 constraints vs. IFEval's 25) revealed 10–15 point performance drops on held-out instruction formats, confirming IFEval overfitting.

**Quality audits matter**: MMLU-Redux's audit of 5,700 questions found ~6.5% errors; in some subjects (Virology), error rates hit 57%. Removing incorrect data shifted model rankings significantly — Llama-3.1-405B moved from 16th to 1st place in Virology. Benchmark scores are only as reliable as the ground truth.

## Statistical Rigor

Most eval results are reported naively — a single accuracy number with no uncertainty quantification. This leads to mistaking noise for progress. The principled approach:

**Standard error and confidence intervals.** Treat eval scores as samples from a super-population. Report `mean ± SE` alongside every eval result. For IID questions, SE = `s / sqrt(n)` where `s` is sample standard deviation. For Bernoulli scores, SE simplifies to `sqrt(μ(1-μ)/n)`. Derive 95% CI as `x̄ ± 1.96 × SE`.

**Clustered errors.** When questions are not independent (same document, same language variant, same topic cluster), the CLT SE formula underestimates uncertainty. Use clustered standard errors, which account for within-cluster correlations. Failing to do this can understate SE by 3× or more.

**Variance reduction.** Two strategies: (1) resample `K` outputs per question and average scores — reduces within-question variance by `1/K`; (2) use next-token log-probabilities instead of sampled outputs, which eliminates within-question variance entirely. Do not adjust sampling temperature for variance reduction — it changes the evaluation target.

**Model comparison.** Comparing separate confidence intervals is too conservative (non-overlapping ≠ significant, overlapping ≠ not significant). Instead: compute the paired difference `d_i = score_A_i - score_B_i` for each shared question, then compute SE of the mean difference. Since models tend to agree on question difficulty, paired differences reduce variance for free. Report: mean difference, SE, CI, and cross-model score correlation.

The practical mandate: report `n`, SE, and CI alongside every eval number. If questions are clustered, report cluster-adjusted SE and the number of clusters.

## Eval-Driven Development (Product Evals)

For production systems, the feedback loop is: label a small dataset → calibrate an LLM judge to match human labels → run automated eval harness on every change. This three-step loop — label, align, automate — is the core of eval-driven development.

Task-specific considerations by output type:

- **Classification**: accuracy, F1, confusion matrix. Deterministic and cheap.
- **Summarization**: factual consistency (does the summary contain only information from the source?) is harder than fluency. LLM judges outperform ROUGE/BLEU for quality assessment.
- **Translation**: BLEU is standard but misses semantic equivalence; LLM judges capture it better.
- **Toxicity / copyright regurgitation**: requires domain-specific rubrics and classifiers; general-purpose judges are unreliable here.
- **RAG / long-form QA**: evaluate retrieval precision/recall separately from generation quality.

For agentic systems, eval complexity increases sharply: actions have downstream state effects, trajectories matter not just final outputs, and partial credit scoring becomes essential.

## The Post-Benchmark Era

As of 2025–2026, benchmark scores have largely decoupled from user-perceived quality. The pattern: benchmark deltas are minor at each release, but real-world capability (especially for coding agents, long-horizon tasks) still improves meaningfully. The Gemini 3 Pro episode illustrates the failure mode: declared leaderboard winner, effectively zero impact at the frontier of coding agents two months later.

The shift is from static benchmark performance to continuous in-use evaluation: how does the model behave across a diverse range of real tasks, over time, as measured by actual usage outcomes? Industry is moving toward:
- Agentic benchmarks (SWE-bench, AgentBench) that measure multi-step task completion
- Human-in-the-loop evals tied to production deployment
- Longitudinal usage metrics as the primary signal

The implication for practitioners: run your own domain-specific evals rather than relying on published leaderboard numbers. A model's rank on MMLU-Pro tells you almost nothing about its rank on your task.

## Practical Eval Pipeline Design

For a production LLM product:

1. **Collect golden examples** — 50–200 human-labeled input/output pairs that represent the full distribution of real requests, including edge cases.
2. **Calibrate your judge** — run a small human study to confirm the LLM judge agrees with human raters at ≥80% rate on your task.
3. **Automate the harness** — run the judge on every model change (prompt update, fine-tune, new model version). Store scores with timestamps.
4. **Track significance, not just direction** — require the paired-difference CI to exclude zero before declaring an improvement.
5. **Monitor for drift** — real-world inputs evolve; re-run golden set audits when input distribution shifts.

## Sources

- `kb/hard/raw/eugene-yan/product-evals-in-three-simple-steps.md` — three-step production eval loop
- `kb/hard/raw/eugene-yan/task-specific-llm-evals-that-do-dont-work.md` — task-specific eval approaches
- `kb/hard/raw/eugene-yan/evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge.md` — LLM-as-judge effectiveness
- `kb/hard/raw/aman-ai/primers-llm-as-a-judge-autoraters.md` — deep treatment of judge biases, LTR integration, panel of judges
- `kb/hard/raw/aman-ai/primers-llmvlm-benchmarks.md` — comprehensive benchmark survey (MMLU, GPQA, BIG-Bench, math, RAG, agent benchmarks)
- `kb/hard/raw/cameron-wolfe/applying-statistics-to-llm-evaluations.md` — statistical framework: SE, CI, clustered errors, paired comparison
- `kb/hard/raw/cameron-wolfe/the-anatomy-of-an-llm-benchmark.md` — benchmark construction, saturation, contamination, discriminability
- `kb/hard/raw/sebastian-raschka/understanding-the-4-main-approaches-to-llm-evaluation-from-scratch.md` — four-method taxonomy with code
- `kb/hard/raw/nathan-lambert/opus-46-codex-53-and-the-post-benchmark-era.md` — post-benchmark era, agentic evaluation shift
