---
concept: LLM Evaluation
tags: [evals, llm-as-judge, benchmarks, evaluation, perplexity, human-eval, statistical-rigor]
sources:
  - kb/hard/raw/eugene-yan/evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge.md
  - kb/hard/raw/eugene-yan/task-specific-llm-evals-that-do-dont-work.md
  - kb/hard/raw/cameron-wolfe/the-anatomy-of-an-llm-benchmark.md
  - kb/hard/raw/sebastian-raschka/understanding-the-4-main-approaches-to-llm-evaluation-from-scratch.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/ai-agents-and-agentic-systems|AI Agents & Agentic Systems]]"
  - "[[hard/wiki/large-language-models|Large Language Models]]"
---

# LLM Evaluation

Evaluating LLMs is harder than it looks. Models can perform well on benchmarks while failing at real tasks; LLM-as-judge correlates imperfectly with human judgment; benchmarks saturate within months of publication; and human evaluation doesn't scale. Building a reliable eval stack requires understanding the tradeoffs across four distinct approaches: benchmark-based evaluation, verifier-based evaluation, LLM-as-judge, and human evaluation.

## Four Approaches to LLM Evaluation

Sebastian Raschka's taxonomy provides a clean mental model:

**1. Multiple-choice / benchmark accuracy**: Evaluate on fixed datasets with known answers. MMLU, GPQA, BIG-Bench, ARC. Automated, cheap, reproducible. Best for knowledge breadth and capability thresholds. Limitations: saturates quickly, doesn't capture open-ended quality, susceptible to contamination.

**2. Verifier-based evals**: Evaluate against a programmatic correctness check — test suite pass rates for code, exact answer matching for math. Used in RLVR training and for coding benchmarks like HumanEval, SWE-Bench. Objective and scalable when the domain is verifiable. Limitation: restricted to domains with deterministic correctness.

**3. LLM-as-judge**: Use a frontier LLM to score or compare outputs. Direct scoring (rate 1–5), pairwise comparison (which response is better), or reference-based (does this match a gold response). Scales arbitrarily and handles open-ended tasks. Limitation: introduces model-specific biases that must be calibrated.

**4. Human evaluation**: Gold standard for subjective quality, alignment, and edge cases. Expensive, slow, and hard to reproduce at scale. Essential for final validation before deployment; impractical as a daily development signal.

In practice, a mature eval stack combines all four: benchmarks for development velocity, verifiers for objective tasks, LLM judges for open-ended quality, and targeted human evaluation to calibrate the automated evals.

## Benchmark Anatomy and Saturation

Good benchmarks share several properties:
- **Data quality**: Expert-curated questions, validated answers, clear error taxonomy
- **Difficulty ceiling**: Questions hard enough that current models don't saturate
- **Diversity**: Broad coverage across domains and difficulty levels
- **Contamination controls**: Tests not present in common pretraining corpora

**MMLU** (Hendrycks et al. 2020): 16K multiple-choice questions across 57 subjects from elementary to professional level. Simple format, broad coverage. Became the standard general-knowledge benchmark. Problem: ~6.5% of questions have errors (MMLU-Redux audit); easy questions inflated scores. **MMLU-Pro** removed easy questions, expanded choices from 4 to 10, and added harder reasoning questions — harder to saturate and more discriminative.

**GPQA** (Graduate-level Google-Proof Q&A): 198–596 expert-written questions in biology, chemistry, and physics. PhD experts achieve 65–74%; non-experts with internet access achieve only 34%. Designed to be unsolvable by Googling. Much harder to saturate than MMLU; still being solved by frontier reasoning models at 87%+.

**BIG-Bench / BIG-Bench Hard / BBEH**: Community-sourced, 204 diverse tasks. BIG-Bench Hard (23 tasks where models lagged humans at release) saturated by early 2025. BIG-Bench Extra Hard replaced each task with a harder version — requires many-hop reasoning, long-context retrieval, error detection in reasoning traces.

**Benchmark saturation cycle**: MMLU → MMLU-Pro → GPQA → GPQA hard variants → new frontiers. The field invents harder benchmarks as models solve easier ones. Benchmarks for coding (SWE-Bench Verified, LiveCodeBench) and math (AIME, FrontierMath) are now the primary discriminators at the frontier.

**Evaluation format matters**: Multiple-choice with 4 choices vs. 10 choices; zero-shot vs. few-shot (5-shot MMLU); chain-of-thought vs. direct answer. Performance can swing 5–15% based on format alone. Models should be evaluated consistently.

## LLM-as-Judge: Calibration and Biases

LLM-as-judge (also called LLM evaluator) uses a strong LLM to evaluate another model's output. Three approaches:

**Direct scoring**: Rate a single response on a scale (1–5) across dimensions like factual consistency, relevance, helpfulness. More flexible; better for objective dimensions. Use one dimension per prompt — multi-dimension prompts yield noisier scores.

**Pairwise comparison**: Given two responses, which is better? More reliable for subjective quality; naturally handles ties. The standard method in Chatbot Arena (LMSYS). Limitation: position bias — responses in position A are sometimes preferred regardless of quality.

**Reference-based**: Compare generated output to a gold reference. Works for summarization (does this capture the key facts?) and translation. Requires having ground-truth references.

**Key biases to calibrate**:
- **Verbosity bias**: Longer responses are often rated higher even when they're not actually better
- **Self-enhancement bias**: Models prefer their own style of output
- **Position bias**: In pairwise comparison, the first or second option may be systematically preferred
- **Sycophancy**: Judges may prefer responses that match their priors rather than being genuinely better

**Chain-of-thought helps**: Asking the judge to explain its reasoning before scoring improves consistency. Large judges (52B+) competitive with finetuned preference models; smaller judges less reliable.

**Correlating with humans**: Target LLM-human correlation ≥ human-human inter-annotator agreement. Human-human correlation on a task is the ceiling for automated evals. Cohen's κ (categorical agreement, chance-adjusted), Spearman's ρ, and Kendall's τ are the standard metrics. Prefer classification framing (binary good/bad) over 5-point scales where possible — binary outputs have better-defined precision and recall.

**Finetuned evaluators**: For specific tasks (toxicity detection, factual inconsistency, NLI), a small finetuned classifier often outperforms a large general-purpose judge at orders-of-magnitude lower cost and latency. Finetuning on ~1000 task-specific labeled examples can lift ROC-AUC from 0.56 (essentially random) to 0.85 for factual consistency detection.

## Task-Specific Eval Patterns That Work

**Classification and extraction**: Use recall, precision, ROC-AUC, PR-AUC. Accuracy is too coarse — break it into class-level precision and recall across thresholds. Plot the distribution of predicted probabilities to assess separation quality; poor separation means no clean threshold for production.

**Summarization (factual consistency)**: NLI-based evaluation — treat the source document as premise, the generated summary as hypothesis, and measure whether the summary is entailed by the source. Fine-tune an NLI model on factual inconsistency data; this outperforms ROUGE, BERTScore, and LLM-based evals in discriminativeness. Standard n-gram metrics (ROUGE) have poor separation between good and bad summaries — their distributions overlap too much to cut a reliable threshold.

**Summarization (relevance)**: Train a reward model on human preference data or fine-tune an NLI model on relevance judgments. BARTScore and QA-based evals also work for aspect-level relevance in opinion summarization.

**Translation**: Use learned metrics (BLEURT, COMET) rather than BLEU. For production quality monitoring, reference-free COMETKiwi enables quality estimation without human-written references.

**Length adherence**: Trivial to compute but often overlooked. Directly count words/characters; essential for push notifications, UI summaries, and constrained generation contexts.

## Eval-Driven Development

Building evals is not just measurement — it's specification. A good eval suite forces clarity about what "good output" actually means. Key practices:

- **Build evals before fine-tuning**: Don't discover failure modes after deployment
- **Log and analyze failures**: Evals that only report aggregate accuracy miss systematic failure patterns
- **Calibrate against human judgment early**: Run a human audit of your automated evals on a sample. If automated evals disagree with humans at a high rate, the eval is the problem.
- **Include adversarial / edge-case tests**: The marginal failing case is usually more important than the average-case pass rate

## Statistical Rigor

Small eval datasets produce noisy rankings. The standard error of a proportion p over n samples is sqrt(p(1-p)/n). With n=100 and p=0.7, the 95% CI is ±9 percentage points — enough to make two models with 5-point differences indistinguishable. Most benchmark comparisons reported in papers have insufficient sample sizes to reliably rank models that are close. Use the full benchmark test set, not subsamples, and report confidence intervals alongside point estimates.

For pairwise comparisons in arena-style settings, Elo ratings accumulate enough games to stabilize but require accounting for time decay as models improve.

## The Post-Benchmark Era Signal

By 2025-2026, leaderboard-driven evaluation has lost most of its discriminating power at the frontier. The gap between Opus 4.6 and Codex 5.3 is barely visible in benchmarks but is clearly felt in sustained agentic use across multi-day coding projects. This signals that the relevant evaluation unit has shifted from individual responses to multi-step task completion in realistic environments. The right eval for an agentic coding assistant is not MMLU — it's "does it complete a real GitHub issue correctly?" SWE-Bench Verified, SWE-Lancer, and similar agentic evals are the emerging standard for reasoning + coding agents.

## Sources

- Eugene Yan: Evaluating LLM Evaluators — key considerations, biases, prompting techniques, finetuning evaluators
- Eugene Yan: Task-Specific LLM Evals — classification metrics, summarization NLI approach, translation metrics
- Cameron Wolfe: The Anatomy of an LLM Benchmark — MMLU, MMLU-Pro, GPQA, BIG-Bench family deep dives
- Sebastian Raschka: Understanding the 4 Main Approaches to LLM Evaluation — multiple-choice, verifiers, leaderboards, LLM judges with code
