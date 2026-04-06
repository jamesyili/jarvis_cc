# Primers • LLM-as-a-Judge / Autoraters

**Source:** https://aman.ai/primers/ai/LLM-as-a-judge/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** llms, ml-fundamentals

---

* [Overview](#overview)
* [Motivation: Why LLM-as-a-Judge Is Needed Beyond Traditional Metrics](#motivation-why-llm-as-a-judge-is-needed-beyond-traditional-metrics)
  + [Limitations of Traditional Evaluation Metrics](#limitations-of-traditional-evaluation-metrics)
  + [The Rise of Human Evaluation—and Its Costs](#the-rise-of-human-evaluationand-its-costs)
  + [LLM-as-a-Judge as a Scalable Approximation to Human Judgment](#llm-as-a-judge-as-a-scalable-approximation-to-human-judgment)
  + [Why This Matters for Modern LLM Tasks](#why-this-matters-for-modern-llm-tasks)
  + [From Evaluation to Ranking and Learning](#from-evaluation-to-ranking-and-learning)
* [Background: Learning-to-Rank (LTR) Paradigms](#background-learning-to-rank-ltr-paradigms)
  + [Pointwise Ranking](#pointwise-ranking)
  + [Pairwise Ranking](#pairwise-ranking)
  + [Listwise Ranking](#listwise-ranking)
* [Pointwise LLM-as-a-Judge in Practice](#pointwise-llm-as-a-judge-in-practice)
  + [How LLM-as-a-Judge Fits into LTR](#how-llm-as-a-judge-fits-into-ltr)
  + [Pointwise LTR Framing for LLM-as-a-Judge](#pointwise-ltr-framing-for-llm-as-a-judge)
  + [Design Principles for Reliable Judge Prompts](#design-principles-for-reliable-judge-prompts)
  + [Example Pointwise LLM-as-a-Judge Prompt](#example-pointwise-llm-as-a-judge-prompt)
    - [Why This Is Pointwise LTR](#why-this-is-pointwise-ltr)
* [Fine-Tuning Encoder, Encoder–Decoder, and Decoder-Only Models for LTR](#fine-tuning-encoder-encoderdecoder-and-decoder-only-models-for-ltr)
  + [Why Fine-Tune Models for LTR?](#why-fine-tune-models-for-ltr)
    - [Scalability and Latency Constraints](#scalability-and-latency-constraints)
    - [Direct Optimization of Ranking Metrics](#direct-optimization-of-ranking-metrics)
    - [Stability, Calibration, and Reproducibility](#stability-calibration-and-reproducibility)
    - [Integration into Retrieval and RAG Pipelines](#integration-into-retrieval-and-rag-pipelines)
  + [How LTR Fine-Tuning Works: A Unified View](#how-ltr-fine-tuning-works-a-unified-view)
  + [Architectural Choices](#architectural-choices)
    - [Encoder-Only Models](#encoder-only-models)
    - [Encoder–Decoder Models](#encoderdecoder-models)
    - [Decoder-Only Models](#decoder-only-models)
  + [The Role of LLM-as-a-Judge in LTR Fine-Tuning](#the-role-of-llm-as-a-judge-in-ltr-fine-tuning)
  + [Encoder-Only Models for LTR](#encoder-only-models-for-ltr)
    - [Pointwise Encoder-Only Ranking](#pointwise-encoder-only-ranking)
      * [Architecture](#architecture)
      * [Example: monoBERT](#example-monobert)
      * [Loss Function](#loss-function)
      * [Input–Output Example](#inputoutput-example)
    - [Pairwise Encoder-Only Ranking](#pairwise-encoder-only-ranking)
      * [Architecture](#architecture-1)
      * [Example: duoBERT](#example-duobert)
      * [Loss Function](#loss-function-1)
      * [Input–Output Example](#inputoutput-example-1)
    - [Listwise Encoder-Only Ranking](#listwise-encoder-only-ranking)
      * [Architecture](#architecture-2)
      * [Example: ListBERT](#example-listbert)
    - [Direct and Approximate Optimization of NDCG](#direct-and-approximate-optimization-of-ndcg)
      * [NDCG Definition](#ndcg-definition)
      * [Common Listwise Losses](#common-listwise-losses)
    - [Relationship to LLM-as-a-Judge Supervision](#relationship-to-llm-as-a-judge-supervision)
    - [Takeaways](#takeaways)
  + [Encoder–Decoder Models for Learning-to-Rank (LTR): Listwise Reasoning at Decode Time](#encoderdecoder-models-for-learning-to-rank-ltr-listwise-reasoning-at-decode-time)
    - [Why Encoder–Decoder for Ranking?](#why-encoderdecoder-for-ranking)
    - [Fusion-in-Decoder (FiD): The Core Pattern](#fusion-in-decoder-fid-the-core-pattern)
      * [Architecture](#architecture-3)
    - [ListT5: Encoder–Decoder Listwise Re-Ranking](#listt5-encoderdecoder-listwise-re-ranking)
      * [Architecture](#architecture-4)
      * [Output Representation](#output-representation)
    - [Training Objectives for Encoder–Decoder Ranking](#training-objectives-for-encoderdecoder-ranking)
      * [Sequence Cross-Entropy Loss](#sequence-cross-entropy-loss)
      * [Connection to NDCG Optimization](#connection-to-ndcg-optimization)
    - [Advantages Over Encoder-Only Listwise Models](#advantages-over-encoder-only-listwise-models)
    - [Using LLM-as-a-Judge for Encoder–Decoder Supervision](#using-llm-as-a-judge-for-encoderdecoder-supervision)
    - [When to Use Encoder–Decoder Rankers](#when-to-use-encoderdecoder-rankers)
    - [Takeaways](#takeaways-1)
  + [Decoder-Based LLM-as-a-Judge for LTR](#decoder-based-llm-as-a-judge-for-ltr)
    - [Pointwise Prompt-Based LLM-as-a-Judge](#pointwise-prompt-based-llm-as-a-judge)
      * [Prompt Pattern](#prompt-pattern)
      * [Interpretation as Pointwise LTR](#interpretation-as-pointwise-ltr)
      * [Loss Function](#loss-function-2)
    - [Pairwise Prompt-Based LLM-as-a-Judge](#pairwise-prompt-based-llm-as-a-judge)
      * [Prompt Pattern](#prompt-pattern-1)
      * [Pairwise LTR Interpretation](#pairwise-ltr-interpretation)
      * [Associated Loss (When Used for Training)](#associated-loss-when-used-for-training)
    - [Listwise Prompt-Based LLM-as-a-Judge](#listwise-prompt-based-llm-as-a-judge)
      * [Prompt Patterns](#prompt-patterns)
      * [Listwise LTR Interpretation](#listwise-ltr-interpretation)
    - [Listwise Loss Functions and NDCG Optimization](#listwise-loss-functions-and-ndcg-optimization)
      * [Normalized Discounted Cumulative Gain (NDCG)](#normalized-discounted-cumulative-gain-ndcg)
      * [Optimizing NDCG](#optimizing-ndcg)
        + [Listwise Surrogate Losses](#listwise-surrogate-losses)
        + [Gradient-Based Approximations to NDCG](#gradient-based-approximations-to-ndcg)
        + [Using LLM Judges to Approximate NDCG](#using-llm-judges-to-approximate-ndcg)
      * [Can Categorical Cross-Entropy Be Used for Listwise Ranking?](#can-categorical-cross-entropy-be-used-for-listwise-ranking)
        + [When Categorical Cross-Entropy Applies](#when-categorical-cross-entropy-applies)
        + [Limitations of Categorical Cross-Entropy for Ranking](#limitations-of-categorical-cross-entropy-for-ranking)
        + [Relationship to NDCG](#relationship-to-ndcg)
      * [Input–Output Example (Listwise)](#inputoutput-example-listwise)
    - [Takeaways](#takeaways-2)
* [Automatic Prompt Optimization (APO) for LLM-as-a-Judge](#automatic-prompt-optimization-apo-for-llm-as-a-judge)
  + [Why Prompt Optimization Is Critical for LLM-as-a-Judge](#why-prompt-optimization-is-critical-for-llm-as-a-judge)
  + [ProTeGi: Prompt Optimization with Textual Gradients](#protegi-prompt-optimization-with-textual-gradients)
  + [Formal Objective](#formal-objective)
  + [Textual Gradients as Loss Signals](#textual-gradients-as-loss-signals)
  + [Prompt Updates via Semantic Gradient Descent](#prompt-updates-via-semantic-gradient-descent)
  + [Beam Search over the Prompt Space](#beam-search-over-the-prompt-space)
    - [Expansion Step: Generating Successor Prompts](#expansion-step-generating-successor-prompts)
    - [Selection Step: Updating the Beam](#selection-step-updating-the-beam)
    - [Exploitation–Exploration Trade-off](#exploitationexploration-trade-off)
  + [Selection as Best-Arm Identification](#selection-as-best-arm-identification)
    - [Mapping Prompt Selection to Bandits](#mapping-prompt-selection-to-bandits)
    - [Upper Confidence Bound (UCB) and UCB-E](#upper-confidence-bound-ucb-and-ucb-e)
    - [Successive Rejects: A Natural Fit](#successive-rejects-a-natural-fit)
    - [Successive Halving](#successive-halving)
    - [Example from the Paper](#example-from-the-paper)
  + [Implications for LLM-as-a-Judge Systems](#implications-for-llm-as-a-judge-systems)
  + [Key Takeaways](#key-takeaways)
* [Putting It All Together: LLM-as-a-Judge in Modern Evaluation Pipelines](#putting-it-all-together-llm-as-a-judge-in-modern-evaluation-pipelines)
  + [End-to-End Evaluation Pipelines with LLM-as-a-Judge](#end-to-end-evaluation-pipelines-with-llm-as-a-judge)
  + [Combining Prompted Judges with Trained Rankers](#combining-prompted-judges-with-trained-rankers)
  + [Failure Modes and Limitations of LLM-as-a-Judge](#failure-modes-and-limitations-of-llm-as-a-judge)
    - [Bias and Positional Effects](#bias-and-positional-effects)
    - [Prompt Sensitivity and Variance](#prompt-sensitivity-and-variance)
    - [Over-Optimization and Reward Hacking](#over-optimization-and-reward-hacking)
  + [Best Practices for Production Use](#best-practices-for-production-use)
  + [Summary and Outlook](#summary-and-outlook)
* [Panel / Jury of LLMs-as-Judges](#panel--jury-of-llms-as-judges)
  + [Motivation: Why a Single Judge Is Not Enough](#motivation-why-a-single-judge-is-not-enough)
  + [Panel of LLM Evaluators (PoLL): Core Concept](#panel-of-llm-evaluators-poll-core-concept)
  + [Judge Diversity and Panel Composition](#judge-diversity-and-panel-composition)
  + [Aggregation and Voting Strategies](#aggregation-and-voting-strategies)
    - [Binary Judgments (e.g., QA correctness)](#binary-judgments-eg-qa-correctness)
    - [Ordinal or Likert-Type Scores (e.g., 1–5 ratings)](#ordinal-or-likert-type-scores-eg-15-ratings)
    - [Pairwise Preference Judgments](#pairwise-preference-judgments)
  + [Empirical Results and Human Correlation](#empirical-results-and-human-correlation)
  + [Cost and Latency Advantages](#cost-and-latency-advantages)
  + [Relationship to LLM-as-a-Judge and LTR Paradigms](#relationship-to-llm-as-a-judge-and-ltr-paradigms)
  + [Practical Guidance: When to Use a Panel of Judges](#practical-guidance-when-to-use-a-panel-of-judges)
  + [Takeaways](#takeaways-3)
* [Multimodal LLMs-as-Judges (LMM / VLM-as-a-Judge)](#multimodal-llms-as-judges-lmm--vlm-as-a-judge)
  + [Why Multimodal Judges Are Necessary](#why-multimodal-judges-are-necessary)
  + [Paradigm: VLM / LMM-as-a-Judge](#paradigm-vlm--lmm-as-a-judge)
  + [LLaVA-Critic: Generalist Multimodal Judge](#llava-critic-generalist-multimodal-judge)
    - [Overview](#overview-1)
    - [Key Contributions](#key-contributions)
    - [Training Data and Setup](#training-data-and-setup)
    - [Architecture](#architecture-5)
    - [Evaluation Scenarios](#evaluation-scenarios)
  + [Prometheus-Vision: Fine-Grained Multimodal Evaluation](#prometheus-vision-fine-grained-multimodal-evaluation)
    - [Overview](#overview-2)
    - [Core Idea](#core-idea)
    - [Architecture and Training](#architecture-and-training)
    - [Dataset: Perception Collection](#dataset-perception-collection)
    - [Empirical Results](#empirical-results)
  + [Multimodal Judges in Preference Learning](#multimodal-judges-in-preference-learning)
  + [When to Use Multimodal Judges](#when-to-use-multimodal-judges)
* [Reinforcement Learning for LLMs-as-Judges](#reinforcement-learning-for-llms-as-judges)
  + [Motivation: Why RL for Judges?](#motivation-why-rl-for-judges)
  + [Core Idea: Thinking-LLM-as-a-Judge via RL](#core-idea-thinking-llm-as-a-judge-via-rl)
  + [Unified Verifiable Training via Synthetic Data](#unified-verifiable-training-via-synthetic-data)
  + [Reward Design: Optimizing Judgment Quality](#reward-design-optimizing-judgment-quality)
    - [Verdict Correctness Reward](#verdict-correctness-reward)
    - [Consistency Reward (Mitigating Positional Bias)](#consistency-reward-mitigating-positional-bias)
    - [Extended Reward Components](#extended-reward-components)
    - [Putting It Together: Joint Optimization](#putting-it-together-joint-optimization)
  + [Reasoning-Optimized Training via Reinforcement Learning](#reasoning-optimized-training-via-reinforcement-learning)
    - [Group Relative Policy Optimization (GRPO)-based Optimization](#group-relative-policy-optimization-grpo-based-optimization)
    - [Why GRPO Is Well-Matched to J1](#why-grpo-is-well-matched-to-j1)
    - [Seed Prompts and Thought Structure](#seed-prompts-and-thought-structure)
    - [Empirical Effect on Reasoning Quality](#empirical-effect-on-reasoning-quality)
  + [J1 Formulations: Pairwise, Pointwise, and Multitask Judges](#j1-formulations-pairwise-pointwise-and-multitask-judges)
    - [Pairwise J1 with Verdict (PaV)](#pairwise-j1-with-verdict-pav)
    - [Pairwise J1 with Scores (PaS)](#pairwise-j1-with-scores-pas)
    - [Pairwise J1 with Scores and Verdict (PaVS)](#pairwise-j1-with-scores-and-verdict-pavs)
    - [Pointwise J1 with Scores (PoS)](#pointwise-j1-with-scores-pos)
    - [Multitask Pairwise & Pointwise J1 (MT)](#multitask-pairwise--pointwise-j1-mt)
      * [Multitask Objective and Full Loss Function](#multitask-objective-and-full-loss-function)
      * [Full Multitask Loss](#full-multitask-loss)
      * [Why Multitask Training Is Effective](#why-multitask-training-is-effective)
  + [Synthetic Data Generation for Verifiable Judging](#synthetic-data-generation-for-verifiable-judging)
    - [Dataset Composition](#dataset-composition)
    - [Synthetic Preference Generation for Verifiable Tasks (MATH)](#synthetic-preference-generation-for-verifiable-tasks-math)
    - [Synthetic Preference Generation for Non-Verifiable Tasks (WildChat)](#synthetic-preference-generation-for-non-verifiable-tasks-wildchat)
    - [Position-Agnostic Pair Construction](#position-agnostic-pair-construction)
    - [Why Synthetic Data Works for J1](#why-synthetic-data-works-for-j1)
  + [Learned Reasoning Behaviors](#learned-reasoning-behaviors)
  + [Empirical Performance](#empirical-performance)
    - [PPE (Preference Proxy Evaluations)](#ppe-preference-proxy-evaluations)
    - [RewardBench](#rewardbench)
    - [JudgeBench](#judgebench)
    - [RM-Bench](#rm-bench)
    - [FollowBenchEval](#followbencheval)
    - [RewardBench v2](#rewardbench-v2)
      * [Key Differences Between RewardBench v1 and RewardBench v2](#key-differences-between-rewardbench-v1-and-rewardbench-v2)
  + [Implications for LLM-as-a-Judge Systems](#implications-for-llm-as-a-judge-systems-1)
  + [Relationship to Panels and Multimodal Judges](#relationship-to-panels-and-multimodal-judges)
  + [Key Takeaways](#key-takeaways-1)
  + [From J1 to JudgeLRM](#from-j1-to-judgelrm)
* [Biases and Mitigation Strategies](#biases-and-mitigation-strategies)
  + [Length and Verbosity Bias](#length-and-verbosity-bias)
    - [Description](#description)
    - [Why It Happens](#why-it-happens)
    - [Mitigation Strategies](#mitigation-strategies)
  + [Positional and Ordering Bias](#positional-and-ordering-bias)
    - [Description](#description-1)
    - [Why It Happens](#why-it-happens-1)
    - [Mitigation Strategies](#mitigation-strategies-1)
  + [Self-Preference and Model Identity Bias](#self-preference-and-model-identity-bias)
    - [Description](#description-2)
    - [Why It Happens](#why-it-happens-2)
    - [Mitigation Strategies](#mitigation-strategies-2)
  + [Over-Confidence and Hallucination Blindness](#over-confidence-and-hallucination-blindness)
    - [Description](#description-3)
    - [Why It Happens](#why-it-happens-3)
    - [Mitigation Strategies](#mitigation-strategies-3)
  + [Prompt Sensitivity](#prompt-sensitivity)
    - [Description](#description-4)
    - [Why It Happens](#why-it-happens-4)
    - [Mitigation Strategies](#mitigation-strategies-4)
  + [Reward Hacking](#reward-hacking)
    - [Description](#description-5)
    - [Why It Happens](#why-it-happens-5)
    - [Mitigation Strategies](#mitigation-strategies-5)
  + [Takeaways](#takeaways-4)
* [Causal Judge Evaluation (CJE): Calibrated Surrogate Metrics for LLM-as-a-Judge](#causal-judge-evaluation-cje-calibrated-surrogate-metrics-for-llm-as-a-judge)
  + [Motivation: Why Calibration Is Necessary for LLM-as-a-Judge](#motivation-why-calibration-is-necessary-for-llm-as-a-judge)
  + [Problem Setup and Notation](#problem-setup-and-notation)
  + [Core Contribution: The Causal Judge Evaluation (CJE) Framework](#core-contribution-the-causal-judge-evaluation-cje-framework)
    - [AutoCal-R: Mean-Preserving Reward Calibration](#autocal-r-mean-preserving-reward-calibration)
    - [SIMCal-W: Stabilizing Importance Weights](#simcal-w-stabilizing-importance-weights)
    - [OUA Inference: Valid Uncertainty Quantification](#oua-inference-valid-uncertainty-quantification)
  + [Implications for LLM-as-a-Judge Systems](#implications-for-llm-as-a-judge-systems-2)
* [When to Use Which Paradigm: A Practical Decision Guide](#when-to-use-which-paradigm-a-practical-decision-guide)
  + [Pointwise Evaluation: When Absolute Scoring Is Enough](#pointwise-evaluation-when-absolute-scoring-is-enough)
    - [When to Use Pointwise](#when-to-use-pointwise)
    - [Why Pointwise Works Well](#why-pointwise-works-well)
    - [Extensions: Panels and Multimodal Judges in Pointwise Settings](#extensions-panels-and-multimodal-judges-in-pointwise-settings)
    - [When Pointwise Breaks Down](#when-pointwise-breaks-down)
  + [Pairwise Evaluation: When Relative Preference Matters](#pairwise-evaluation-when-relative-preference-matters)
    - [When to Use Pairwise](#when-to-use-pairwise)
    - [Why Pairwise Often Improves Reliability](#why-pairwise-often-improves-reliability)
    - [Panels and Multimodal Pairwise Evaluation](#panels-and-multimodal-pairwise-evaluation)
    - [Trade-offs](#trade-offs)
  + [Listwise Evaluation: When Global Ranking Quality Matters](#listwise-evaluation-when-global-ranking-quality-matters)
    - [When to Use Listwise](#when-to-use-listwise)
    - [Why Listwise Is Powerful](#why-listwise-is-powerful)
    - [Panels and Multimodal Listwise Evaluation](#panels-and-multimodal-listwise-evaluation)
    - [Trade-offs](#trade-offs-1)
  + [A Simple Escalation Strategy (Including Judges and Modalities)](#a-simple-escalation-strategy-including-judges-and-modalities)
  + [Comparative Analysis Across Evaluation Dimensions](#comparative-analysis-across-evaluation-dimensions)
  + [Practical Tips](#practical-tips)
    - [Use pointwise evaluation by default](#use-pointwise-evaluation-by-default)
    - [Add judge panels before changing paradigms](#add-judge-panels-before-changing-paradigms)
    - [Use pairwise evaluation when relative preference matters](#use-pairwise-evaluation-when-relative-preference-matters)
    - [Introduce multimodal judges only when grounding is required](#introduce-multimodal-judges-only-when-grounding-is-required)
    - [Use listwise evaluation sparingly, when ranking quality outweighs cost](#use-listwise-evaluation-sparingly-when-ranking-quality-outweighs-cost)
    - [The Core Principle](#the-core-principle)
* [References](#references)
  + [LLM-as-a-Judge Foundations and Bias Analysis](#llm-as-a-judge-foundations-and-bias-analysis)
  + [Panels / Juries of LLMs-as-Judges](#panels--juries-of-llms-as-judges)
  + [Multimodal LLMs-as-Judges](#multimodal-llms-as-judges)
  + [Learning-to-Rank (LTR) and Neural Re-ranking](#learning-to-rank-ltr-and-neural-re-ranking)
  + [Reinforcement Learning for LLMs-as-Judges and Reward Modeling](#reinforcement-learning-for-llms-as-judges-and-reward-modeling)
  + [Reward Model and Judge Benchmarks](#reward-model-and-judge-benchmarks)
* [Citation](#citation)

## Overview

* LLM-as-a-Judge (also known as an “autorater”) refers to the use of Large Language Models (LLMs) as automated evaluators of model-generated outputs. Instead of relying on static, rule-based, or purely statistical evaluation metrics, an LLM is prompted to assess the quality of an output with respect to a task definition, evaluation criteria, and scoring rubric. The judge model produces structured judgments such as scores (i.e., ratings), rankings, and rationales (i.e, explanations behind choice of rating/ranking).
* At a high level, an LLM-as-a-Judge system consists of:

  + A task specification describing what the evaluated model was asked to do
  + A rubric defining evaluation criteria and scoring scales
  + One or more candidate outputs to be evaluated
  + A judge model that applies the rubric to produce scores or rankings
* This paradigm has gained traction because modern LLMs possess strong capabilities in instruction following, semantic understanding, and comparative reasoning, allowing them to approximate human evaluators across a wide range of tasks.
* Early large-scale validation of this idea was presented in [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685) by Zheng et al. (2023), which demonstrated that GPT-4-based judges show high agreement with human preferences across conversational tasks. Subsequent work has extended this approach to reasoning, summarization, code generation, safety evaluation, and Retrieval-Augmented Generation (RAG).
* LLM-as-a-Judge evaluations are now widely used in:

  + Model development and ablation studies
  + Offline evaluation of generative systems
  + Reinforcement learning from AI feedback (RLAIF)
  + Ranking and reranking pipelines
  + Continuous evaluation in production systems
* Prominent industry adoption includes OpenAI’s evaluation framework ([Introducing OpenAI Evals](https://openai.com/blog/evals)), Anthropic’s use of AI feedback for alignment ([Constitutional AI](https://www.anthropic.com/news/constitutional-ai)), and Google’s large-scale preference modeling pipelines.
* Conceptually, LLM-as-a-Judge reframes evaluation as a learned inference problem rather than a handcrafted metric. Instead of computing overlap statistics or heuristic scores, the judge model directly reasons about whether an output satisfies task-specific criteria.
* The following figure ([source](https://arxiv.org/abs/2306.05685)) shows an example of an LLM-based evaluation loop, where multi-turn dialogues between a user and two AI assistants—LLaMA-13B (Assistant A) and Vicuna-13B (Assistant B)—initiated by a question from the MMLU benchmark and a follow-up instruction. GPT-4 is then presented with the context to determine which assistant answers better.

* In practice, LLM-as-a-Judge setups vary along several dimensions:

  + [Pointwise vs. pairwise vs. listwise evaluation](#background-learning-to-rank-ltr-paradigms)
  + [Discrete vs. continuous scoring](#design-principles-for-reliable-judge-prompts)
  + [Free-form vs. schema-constrained outputs](#design-principles-for-reliable-judge-prompts)
  + [Zero-shot vs. fine-tuned judge models](#fine-tuning-encoder-encoderdecoder-and-decoder-only-models-for-ltr)
* Despite these variations, most systems share a common principle: the judge model is treated as an approximate oracle for human judgment, with explicit instructions and structure used to reduce variance and bias.
* In the next section, we will examine **why LLM-as-a-Judge is needed**, and why traditional automatic metrics (e.g., BLEU, ROUGE, exact match) are insufficient for modern generative tasks.

## Motivation: Why LLM-as-a-Judge Is Needed Beyond Traditional Metrics

### Limitations of Traditional Evaluation Metrics

* Traditional evaluation metrics were designed for narrow, well-defined tasks with deterministic or near-deterministic outputs. Examples include BLEU for machine translation, ROUGE for summarization, Exact Match (EM) for question answering, and accuracy or F1 for classification. While these metrics are easy to compute, fast, and reproducible, they fail to capture many properties that matter for modern LLM outputs.
* Key limitations include:

  + **Surface-form dependence**: Metrics like BLEU and ROUGE rely on n-gram overlap, penalizing valid paraphrases and rewarding shallow lexical similarity. This was extensively analyzed in [On the Limitations of Automatic Metrics for Evaluating Natural Language Generation](https://aclanthology.org/W17-2602/) by Novikova et al. (2017).
  + **Inability to measure reasoning quality**: Exact match and token overlap metrics cannot distinguish between correct reasoning and lucky guessing, or between flawed reasoning and correct final answers.
  + **Poor alignment with human judgment**: Numerous studies show weak correlation between traditional metrics and human preferences for tasks like summarization and dialogue, e.g., [Re-evaluating Automatic Metrics for Natural Language Generation](https://aclanthology.org/D19-1389/) by Reiter (2019).
  + **Single-reference bias**: Many benchmarks rely on one or a few reference outputs, even though generative tasks are inherently one-to-many.
  + **Task brittleness**: Metrics must be redesigned for each task, making them difficult to generalize across domains such as reasoning, safety, instruction following, or creativity.
* As LLMs began to outperform reference-based baselines while producing diverse and high-quality outputs, these weaknesses became critical bottlenecks to progress.

### The Rise of Human Evaluation—and Its Costs

* To address these shortcomings, the community increasingly relied on human evaluation. Human judges can assess:

  + Semantic correctness
  + Factuality
  + Coherence and clarity
  + Helpfulness and safety
  + Preference between multiple outputs
* However, human evaluation introduces its own challenges:

  + **Cost and latency**: Large-scale human evaluation is expensive and slow.
  + **Inconsistency**: Inter-annotator agreement can be low, especially for subjective criteria.
  + **Limited scalability**: Continuous evaluation during training or deployment is impractical.
  + **Reproducibility issues**: Results depend heavily on annotator pools and instructions.
* These issues are discussed in detail in [How to Evaluate Language Models: A Survey](https://arxiv.org/abs/2307.03109) by Chang et al. (2023).

### LLM-as-a-Judge as a Scalable Approximation to Human Judgment

* LLM-as-a-Judge emerged as a pragmatic compromise between brittle automatic metrics and expensive human evaluation. The core insight is that strong LLMs already encode many of the same linguistic and semantic priors that humans use when judging outputs.
* Empirical evidence supporting this idea includes:

  + High agreement between GPT-4 judges and human annotators on dialogue quality and reasoning tasks, shown in [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685) by Zheng et al. (2023).
  + Strong correlation between AI preference models and human feedback in Reinforcement Learning (RL) pipelines, as demonstrated in [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) by Ouyang et al. (2022).
  + Effective use of AI-generated feedback in place of human annotations in [Constitutional AI](https://www.anthropic.com/news/constitutional-ai).
* LLM-as-a-Judge offers several advantages:

  + **Semantic sensitivity**: Judges reason about meaning, not surface form.
  + **Task flexibility**: New tasks can be evaluated by changing prompts rather than metrics.
  + **Low marginal cost**: Once deployed, evaluations scale cheaply.
  + **Structured output**: Judges can emit scores, rankings, and rationales.
  + **Fast iteration**: Enables rapid offline evaluation during model development.

### Why This Matters for Modern LLM Tasks

* Modern LLM applications—reasoning, tool use, code generation, RAG, safety alignment—often lack clear ground truth. Evaluation becomes inherently subjective or context-dependent.
* Examples where traditional metrics fail but LLM-as-a-Judge succeeds include:

  + **Chain-of-thought reasoning**: Evaluating whether reasoning is valid, not just whether the final answer matches.
  + **Summarization faithfulness**: Detecting subtle hallucinations that ROUGE cannot capture, as shown in [Evaluating the Factual Consistency of Summaries](https://arxiv.org/abs/2008.01415) by Kryściński et al. (2020).
  + **Instruction following**: Determining whether constraints were followed, even when outputs differ lexically.
  + **Safety and policy compliance**: Judging nuanced violations where keyword matching fails.
* As a result, LLM-as-a-Judge has become a foundational component of modern evaluation pipelines.

### From Evaluation to Ranking and Learning

* Crucially, LLM-as-a-Judge is not limited to scalar scoring. It naturally connects to **Learning-to-Rank (LTR)** formulations:

  + Scoring an output independently (pointwise)
  + Comparing two outputs relatively (pairwise)
  + Ranking lists of outputs holistically (listwise)
* [Background: Learning-to-Rank (LTR) Paradigms](#background-learning-to-rank-ltr-paradigms) offers a detailed discourse on this topic, covering each paradigm in detail.
* This connection enables downstream use cases such as:

  + Model selection and benchmarking
  + Dataset filtering and curriculum construction
  + Reward modeling for RL
  + Reranking in retrieval and generation pipelines
* In the next section, we will formally introduce **Learning-to-Rank paradigms (pointwise, pairwise, listwise)** and explain how LLM-as-a-Judge fits naturally into these frameworks.

## Background: Learning-to-Rank (LTR) Paradigms

* LTR provides the formal framework that underlies many modern evaluation, ranking, and reranking systems. While LTR originated in information retrieval and search, its abstractions map cleanly onto LLM-as-a-Judge setups, where the “query” is a task specification and the “documents” are candidate model outputs.
* At a high level, LTR methods differ in **how relevance or quality is modeled and optimized**. The three dominant paradigms are pointwise, pairwise, and listwise ranking.

### Pointwise Ranking

* In pointwise LTR, each candidate is scored independently (i.e., in an absolute manner) with respect to the query. The model learns a function:

  \[f(q, x\_i) \rightarrow s\_i\]
  + where \(q\) is the query (or task), \(x\_i\) is a candidate output, and \(s\_i\) is an absolute relevance or quality score.
* Classic examples include regression or classification approaches, where the model predicts relevance labels or probabilities. Early neural formulations include [RankNet](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/MSR-TR-2010-82.pdf) by Burges et al. (2010) and later transformer-based rankers such as [monoBERT](https://arxiv.org/abs/1910.14424) by Nogueira et al. (2019).
* In the context of LLM-as-a-Judge:

  + The judge scores each output independently
  + Scores may be binary, ordinal, or continuous
  + No explicit comparison between outputs is required
* This is the **most common formulation** used in practice, because it is simple, parallelizable, and easy to operationalize.

### Pairwise Ranking

* Pairwise LTR models learn relative preferences between two candidates at a time. Instead of predicting absolute scores, the model predicts which of two candidates is better:

\[f(q, x\_i, x\_j) \rightarrow P(x\_i \succ x\_j)\]

* Training data consists of ordered pairs \((x\_i, x\_j)\) labeled according to preference. Optimization typically minimizes a pairwise loss such as logistic loss:

  \[\mathcal{L}\_{\text{pairwise}} = - \log \sigma(s\_i - s\_j)\]
  + where \(\sigma\) is the sigmoid function.
* Examples include [RankNet](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/MSR-TR-2010-82.pdf) by Burges et al. (2010) and pairwise extensions of transformer models such as [duoBERT](https://arxiv.org/abs/1910.14424) by Nogueira et al. (2019).
* In LLM-as-a-Judge systems, pairwise evaluation appears when:

  + The judge is asked “Which output is better?”
  + Human-like preference judgments are required
  + Absolute scoring is difficult or ill-defined
* Pairwise judgments often exhibit **higher inter-annotator agreement** than absolute ratings, a phenomenon discussed in [A Large-Scale Analysis of Evaluation Biases in LLMs](https://arxiv.org/abs/2305.17926) by Wang et al. (2023).

### Listwise Ranking

* Listwise LTR methods consider the entire candidate set jointly and optimize a loss defined over permutations or ranked lists:

  \[f(q, {x\_1, \dots, x\_n}) \rightarrow \pi\]
  + where \(\pi\) is an ordering of the candidates.
* Listwise approaches directly optimize ranking metrics such as NDCG or MAP using differentiable approximations. Well-known listwise losses include ListMLE proposed in [Listwise Approach to Learning to Rank - Theory and Algorithm](https://icml.cc/Conferences/2008/papers/167.pdf) by Xia et al. (2008) and softmax cross-entropy over permutations, introduced in [Listwise Approach to Learning to Rank](https://dl.acm.org/doi/10.1145/1277741.1277800) by Cao et al. (2007).
* More recent transformer-based listwise models include:

  + [ListBERT](https://arxiv.org/abs/2206.15198) by Kumar et al. (2022)
  + [ListT5](https://arxiv.org/abs/2402.15838) by Yoon et al. (2024)
  + Agentic rerankers such as [REARANK](https://arxiv.org/abs/2505.20046) by Zhang et al. (2025)
* In LLM-as-a-Judge settings, listwise evaluation arises when:

  + The judge must rank multiple outputs at once
  + Relative ordering matters more than absolute scores
  + Global consistency across outputs is important

## Pointwise LLM-as-a-Judge in Practice

* This section explains how pointwise LTR is realized in practice using LLM-as-a-Judge, and introduces a concrete, production-ready judge prompt.

### How LLM-as-a-Judge Fits into LTR

* LLM-as-a-Judge can be viewed as an **instantiation of LTR**, where the judge model implicitly implements an LTR paradigm (pointwise, pairwise, and listwise) via prompting or fine-tuning.
* Crucially:

> LLM-as-a-judge models most commonly perform **pointwise** evaluation (scoring each output independently against a rubric), though pairwise or listwise ranking is also used in some settings.

* This design choice reflects practical trade-offs:

  + Pointwise judging is simpler and cheaper
  + Pairwise judging reduces calibration issues
  + Listwise judging captures global consistency but is more expensive
* In the next section, we will how an LLM-as-a-Judge operationalizes **pointwise LTR**, introduce the judge prompt, and discuss design principles for reliable judge prompts before moving on to fine-tuning encoder and decoder models for LTR.

### Pointwise LTR Framing for LLM-as-a-Judge

* Under a pointwise formulation, the judge estimates an absolute quality score for each candidate output \(x\_i\), conditioned on the task \(q\):

  \[s\_i = f\_\theta(q, x\_i)\]
  + where:

    - \(q\) encodes the task description and evaluation criteria
    - \(x\_i\) is a single model-generated output
    - \(s\_i\) may be binary, ordinal, or scalar
    - \(f\_\theta\) is implemented via an LLM prompted as a judge
* Unlike traditional neural rankers, the scoring function is not hard-coded or trained from scratch; instead, it is **induced via natural language instructions**. This makes prompt design the critical interface between evaluation intent and model behavior.
* Pointwise LLM-as-a-Judge is especially well-suited for:

  + Offline evaluation of generated outputs
  + Reward modeling bootstrapping (in RL-based policy/preference optimization pipelines)
  + Dataset filtering and quality control
  + Continuous evaluation in CI pipelines
* Empirically, pointwise judging has been shown to correlate strongly with human ratings when prompts are carefully structured, as demonstrated in [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685) by Zheng et al. (2023).

### Design Principles for Reliable Judge Prompts

* Several best practices have emerged for robust pointwise judge prompts:

  1. **Explicit role definition**: The judge should be instructed to behave as an impartial evaluator, not a helper or teacher.
  2. **Clear separation of task and evaluation**: The prompt must distinguish between what the model was asked to do and how it should be judged.
  3. **Structured criteria with explicit scales**: Binary, ternary, ordinal, and Likert-type scales should be clearly labeled to reduce ambiguity.
  4. **Anchored examples**: Providing example inputs for each score level stabilizes calibration and reduces variance, similar to rater training in human evaluation.
  5. **Schema-constrained outputs**: Enforcing JSON or schema-based outputs reduces parsing errors and improves reproducibility.
  6. **Omission of improvement suggestions**: Judges should evaluate, not coach, unless explicitly instructed.
* These principles are echoed in industry evaluation frameworks such as [OpenAI Evals](https://openai.com/blog/evals) and preference modeling pipelines described in [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) by Ouyang et al. (2022).

### Example Pointwise LLM-as-a-Judge Prompt

* Below is an **example pointwise LLM-as-a-Judge prompt** for evaluating a summarization task, implementing the principles above. This prompt instantiates a mixed-scale, rubric-driven evaluator and corresponds directly to a pointwise LTR model that scores each output independently.
* Importantly, the prompt includes **anchored example inputs for each evaluation criterion and each rubric level**, which serve as calibration references for the judge. Multiple such examples can be provided per rubric level, enabling **few-shot learning** that improves scale consistency, reduces ambiguity between adjacent scores, and stabilizes judgments across different criteria.
* Example prompt for an LLM-as-Judge for evaluating a summarization task (mixed scales, JSON output):

```
# Role Definition

You are an impartial, highly rigorous evaluator acting as a judge for assessing model-generated summaries of technical articles. 
Your role is to assess whether a given model-generated summary successfully fulfills the task of producing a concise, accurate synthesis of a technical article, capturing its main claims, key supporting points, and overall conclusion while remaining faithful to the original content. 
All evaluations must be conducted strictly according to the specified evaluation criteria and scoring rubrics, with the expectation that the target summary length is 120–150 words.

# Evaluation Criteria and Scales

* Accuracy (binary yes/no)
* Coverage (ordinal scale: 0–3)
* Faithfulness (ternary ordinal scale: 0–2)
* Clarity (Likert-type ordinal scale: 1–5)
* Conciseness (ternary ordinal scale: 0–2)

# Scoring Rubrics with Anchored Example Inputs

## Accuracy (yes/no)

Whether the summary contains any factual errors relative to the source.

* yes: No factual errors are present.  
  Example input that should be rated yes:  
  “The paper evaluates a transformer-based model on three benchmarks and reports consistent performance improvements across all of them,” when the source article states exactly this.

* no: One or more factual errors are present.  
  Example input that should be rated no:  
  “The authors conducted a large-scale human trial to validate the approach,” when the source explicitly states that no human experiments were performed.

## Coverage (0–3)

The extent to which major points of the source are included.

* 3: All major points are included.  
  Example input that should be rated 3:  
  A summary that describes the problem motivation, the proposed method, the experimental setup, the main results, and the stated limitations.

* 2: Most major points are included with one minor omission.  
  Example input that should be rated 2:  
  A summary that explains the method and results but omits a short discussion of future work mentioned at the end of the article.

* 1: Some major points are missing.  
  Example input that should be rated 1:  
  A summary that reports numerical results but does not explain what method or model produced them.

* 0: The summary is largely incomplete.  
  Example input that should be rated 0:  
  A summary that only provides background context and never mentions the method, results, or conclusions.

## Faithfulness (0–2)

Whether the summary introduces unsupported information or interpretations.

* 2: All statements are directly supported by the source.  
  Example input that should be rated 2:  
  A summary that paraphrases the article’s claims without adding interpretations or conclusions beyond what is stated.

* 1: The summary contains a minor unsubstantiated inference.  
  Example input that should be rated 1:  
  A summary that claims the method is “likely to generalize to all domains,” when the paper only reports results in a limited setting.

* 0: The summary is unfaithful.  
  Example input that should be rated 0:  
  A summary that introduces a recommendation, application, or claim that does not appear anywhere in the source article.

## Clarity (Likert-type ordinal scale: 1–5)

The organization, readability, and coherence of the summary.

* 5: Exceptionally clear and well-structured.  
  Example input that should be rated 5:  
  A summary with a clear logical flow from motivation to method to results, written in precise and unambiguous language.

* 4: Mostly clear with minor issues.  
  Example input that should be rated 4:  
  A summary that is easy to understand overall but contains one awkward transition or slightly unclear sentence.

* 3: Adequately clear but uneven.  
  Example input that should be rated 3:  
  A summary that is generally understandable but includes several vague phrases or mildly confusing sentences.

* 2: Hard to follow.  
  Example input that should be rated 2:  
  A summary that jumps between ideas without clear transitions, making the structure difficult to follow.

* 1: Unclear or incoherent.  
  Example input that should be rated 1:  
  A summary with disorganized sentences, unclear references, and no apparent structure.

## Conciseness (0–2)

Adherence to the target length and avoidance of unnecessary detail.

* 2: Fully concise.  
  Example input that should be rated 2:  
  A summary within 120–150 words that avoids repetition and includes only essential information.

* 1: Minor conciseness issues.  
  Example input that should be rated 1:  
  A summary that slightly exceeds the word limit or repeats one idea unnecessarily.

* 0: Not concise.  
  Example input that should be rated 0:  
  A summary that is substantially longer than the target length or includes extensive irrelevant detail.

# Model Outputs to Evaluate

You will be given a single model-generated summary of a source article. Evaluate this summary according to the evaluation criteria.

# Evaluation Instructions

1. Read the role definition, evaluation criteria, and scoring rubrics carefully.  
2. For the given model-generated summary, assign a score for each criterion using the defined scales.  
3. For each assigned score, provide a clear, evidence-based rationale explaining why the summary merits that score according to the rubric.  
4. Judge only what is present in the summary.  
5. Base decisions strictly on the rubric descriptions, using the example inputs only as anchors.  
6. Apply scales consistently across all evaluated summaries.

# Required Output Format (Strict JSON)

For each model-generated summary, output a single JSON object with the following structure and keys exactly as specified:

{
  "accuracy": {
    "score": "yes | no",
    "justification": "<string>"
  },
  "coverage": {
    "score": <integer 0–3>,
    "justification": "<string>"
  },
  "faithfulness": {
    "score": <integer 0–2>,
    "justification": "<string>"
  },
  "clarity": {
    "score": <integer 1–5>,
    "justification": "<string>"
  },
  "conciseness": {
    "score": <integer 0–2>,
    "justification": "<string>"
  },

  // OPTIONAL BLOCK: include only if critical errors or violations are present
  "errors_or_violations": [
    "<string>",
    "<string>"
  ]
}

# Additional Requirements

* If no errors or violations are identified, omit the errors_or_violations field entirely.
* If included, errors_or_violations must be a non-empty array of concise, concrete descriptions.
* Each justification should be concise and evidence-based, typically 1–2 sentences.
* Do not include placeholder text.
* Do not include any keys not explicitly specified above.
* Do not include any text outside the JSON object.

# Tone and Constraints

* Maintain a neutral, professional, and analytical tone.
* Do not suggest improvements.
* Do not include any content outside the required JSON structure.
```

#### Why This Is Pointwise LTR

* This prompt implements pointwise ranking because:

  + Each output is scored independently
  + No cross-output comparisons are required
  + Scores can be aggregated or thresholded downstream
  + The judge function approximates \(f(q, x\_i)\) directly
* This formulation enables simple extensions such as:

  + Ranking outputs by weighted sums of criteria
  + Filtering low-quality outputs
  + Training reward models via supervised regression
* In the next section, we move beyond prompting and examine **fine-tuning encoder-only and encoder–decoder models for LTR**, covering pointwise, pairwise, and listwise objectives with architectures, loss functions, and concrete input–output examples.

## Fine-Tuning Encoder, Encoder–Decoder, and Decoder-Only Models for LTR

* Modern ranking systems sit at the intersection of **information retrieval**, **generation**, and **evaluation**. While prompt-based LLM-as-a-Judge systems provide flexibility and fast iteration, many real-world applications require **fine-tuned ranking models** that are efficient, stable, and explicitly optimized for ranking objectives.
* This section provides an overarching view of **why** encoder-only, encoder–decoder, and decoder-only models are fine-tuned for LTR, and **how** each architecture supports pointwise, pairwise, and listwise ranking paradigms.

### Why Fine-Tune Models for LTR?

* Fine-tuning ranking models is motivated by fundamental limitations of purely prompt-based or heuristic evaluation approaches.

#### Scalability and Latency Constraints

* Prompt-based LLM judges are expensive at inference time and do not scale well to scenarios involving:

  + Millions of query–candidate comparisons
  + Low-latency retrieval and reranking pipelines
  + Online serving with strict SLA requirements
* In contrast, fine-tuned rankers—especially encoder-only models—can score thousands of candidates per second on commodity hardware. This trade-off is extensively discussed in [Neural Information Retrieval: A Literature Review](https://arxiv.org/abs/1707.08690) by Mitra et al. (2018).

#### Direct Optimization of Ranking Metrics

* Traditional prompt-based evaluation yields **scores or preferences**, but does not directly optimize ranking metrics such as NDCG, MAP, or MRR.
* Fine-tuned LTR models enable:

  + Approximate or direct optimization of ranking metrics
  + Use of differentiable surrogate losses
  + Consistent behavior across training and inference
* The importance of metric-aware optimization was established in early LTR work such as [Learning to Rank Using Gradient Descent](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/MSR-TR-2005-82.pdf) by Burges et al. (2005).

#### Stability, Calibration, and Reproducibility

* Prompt-based LLM judges can exhibit:

  + Sensitivity to prompt wording
  + Drift across model versions
  + Stochastic variance in outputs
* Fine-tuned ranking models provide:

  + Fixed decision boundaries
  + Calibrated score distributions
  + Reproducible evaluation results
* This is critical for production evaluation pipelines and benchmarking, as noted in [How to Evaluate Language Models: A Survey](https://arxiv.org/abs/2307.03109) by Chang et al. (2023).

#### Integration into Retrieval and RAG Pipelines

* Ranking models are core components of:

  + Multi-stage retrieval pipelines
  + Reranking for dense and hybrid search
  + Retrieval-augmented generation (RAG)
* Fine-tuned rankers can be tightly integrated into these systems, unlike prompt-based judges that operate externally. Practical examples are detailed in [Dense Passage Retrieval for Open-Domain Question Answering](https://arxiv.org/abs/2004.04906) by Karpukhin et al. (2020) and [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) by Lewis et al. (2020).

### How LTR Fine-Tuning Works: A Unified View

* Across architectures, LTR fine-tuning follows a common conceptual pattern:

  1. **Define a query**: The query may be a user query, a task description, or an evaluation prompt.
  2. **Define candidates**: Candidates may be documents, passages, model-generated outputs, or tool responses.
  3. **Define a relevance signal**: Relevance may come from:

     + Human annotations
     + LLM-as-a-Judge outputs
     + Implicit feedback (clicks, dwell time)
  4. **Optimize a ranking objective**: Using pointwise, pairwise, or listwise loss functions.
* This abstraction allows LTR techniques to generalize across search, evaluation, and generation tasks.

### Architectural Choices

* Different transformer architectures support LTR in different ways.

#### Encoder-Only Models

* Encoder-only models (e.g., BERT-style transformers) map inputs to contextual embeddings and produce scalar scores.

  + Best suited for **pointwise and pairwise ranking**
  + High precision due to joint encoding
  + Computationally expensive for large candidate sets
* These models dominate **late-stage reranking**, as exemplified by monoBERT and duoBERT ([Multi-Stage Document Ranking with BERT](https://arxiv.org/abs/1910.14424) by Nogueira et al. (2019)).

#### Encoder–Decoder Models

* Encoder–decoder models enable **list-level reasoning** by separating representation and aggregation.

  + Encoder processes each candidate independently
  + Decoder jointly attends over all candidates
  + Supports listwise objectives naturally
* This design underpins architectures such as FiD ([Fusion-in-Decoder for Open-Domain Question Answering](https://arxiv.org/abs/2007.01282) by Izacard et al. (2021)) and ListT5 ([ListT5: Listwise Re-ranking with Fusion-in-Decoder Improves Zero-shot Retrieval](https://arxiv.org/abs/2402.15838) by Yoon et al. (2024)).

#### Decoder-Only Models

* Decoder-only models perform ranking via **generation or classification over text**.

  + Can be prompted for pointwise, pairwise, or listwise judgments
  + Support reasoning-intensive ranking
  + Often used without fine-tuning, but can also be trained
* Prompt-based ranking with decoder-only models is explored in [RankGPT: A Prompt-Based Pairwise Ranking Framework for LLMs](https://arxiv.org/abs/2304.09542) by Sun et al. (2023) and large-scale evaluation studies such as [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685) by Zheng et al. (2023).

### The Role of LLM-as-a-Judge in LTR Fine-Tuning

* LLM-as-a-Judge acts as a **scalable supervision source** across architectures:

  + Pointwise scores \(\rightarrow\) regression targets
  + Pairwise preferences \(\rightarrow\) ranking constraints
  + Listwise rankings \(\rightarrow\) permutation supervision
* This enables **weakly supervised LTR**, reducing reliance on expensive human labels, as demonstrated in [Training Language Models from AI Feedback](https://arxiv.org/abs/2302.08582) by Bai et al. (2023).

### Encoder-Only Models for LTR

* Encoder-only transformer models form the backbone of most **high-precision neural ranking systems** used today. These models take structured inputs (queries, documents, or generated outputs) and map them to contextual representations that are then converted into relevance scores. Their strength lies in **token-level interaction modeling**, which makes them especially effective for reranking small candidate sets.
* Canonical encoder-only architectures are based on transformers such as [BERT](https://arxiv.org/abs/1810.04805) by Devlin et al. (2018), [RoBERTa](https://arxiv.org/abs/1907.11692) by Liu et al. (2019), and [ELECTRA](https://arxiv.org/abs/2003.10555) by Clark et al. (2020).
* Encoder-only rankers are most commonly implemented as **cross-encoders**, where the query and candidate are jointly encoded, enabling full self-attention across tokens.

#### Pointwise Encoder-Only Ranking

##### Architecture

* In pointwise ranking, the model independently scores each query–candidate pair.
* **Architecture:** **Cross-encoder**
* **Input format:**

  \[\texttt{[CLS] q [SEP] d\_i [SEP]}\]
* **Output:** scalar relevance score derived from the final `[CLS]` embedding
* This joint encoding allows the model to capture fine-grained semantic interactions such as negation, entity alignment, and discourse structure, which are inaccessible to bi-encoders.

##### Example: monoBERT

* [Multi-Stage Document Ranking with BERT](https://arxiv.org/abs/1910.14424) by Nogueira et al. (2019)
* monoBERT estimates an absolute relevance probability:

\[s\_i = P(\text{relevant} \mid q, d\_i)\]

* Although originally designed for document retrieval, monoBERT-style models are now widely used to rank **generated outputs**, including summaries, answers, and tool responses.

##### Loss Function

* Pointwise models are typically trained using **binary cross-entropy** or regression losses:

  \[\mathcal{L}\_{\text{pointwise}} =
  -\left[y\_i \log s\_i + (1 - y\_i)\log(1 - s\_i)\right]\]
  + where \(y\_i \in {0,1}\) is a relevance label.
* When supervision comes from LLM-as-a-Judge, labels may be:

  + Binary (acceptable / unacceptable)
  + Ordinal (Likert-style scores)
  + Continuous (normalized quality scores)

##### Input–Output Example

* **Input:**
  + **Query:** “Summarize the paper”
  + **Candidate:** model-generated summary
* **Output:** \(s\_i = 0.91\)
* This setup directly mirrors a **pointwise LLM-as-a-Judge**, where each output is scored independently.

#### Pairwise Encoder-Only Ranking

* Pairwise ranking reframes relevance as a **relative preference** between two candidates under the same query.

##### Architecture

* Cross-encoder
* Input format:

  \[\texttt{[CLS] q [SEP] d\_i [SEP] d\_j [SEP]}\]
* The model processes both candidates jointly and produces a score indicating which is preferred.

##### Example: duoBERT

* Proposed in [Multi-Stage Document Ranking with BERT](https://arxiv.org/abs/1910.14424) by Nogueira et al. (2019), duoBERT estimates:

\[p\_{i,j} = P(d\_i \succ d\_j \mid q)\]

* Unlike pointwise models, pairwise models are invariant to absolute score calibration, which often leads to more stable training.

##### Loss Function

* A common choice is **pairwise logistic loss** (introduced in [RankNet](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/MSR-TR-2010-82.pdf) by Burges et al. (2010)):

\[\mathcal{L}\_{\text{pairwise}} = -\log \sigma(s\_i - s\_j)\]

* This loss encourages the score of the preferred candidate to exceed that of the non-preferred one.

##### Input–Output Example

* **Input:** Query + Summary A + Summary B
* **Output:** \(P(A \succ B) = 0.78\)
* Pairwise supervision aligns closely with **pairwise LLM-as-a-Judge prompts** (“Which output is better?”), which have been shown to yield higher agreement than absolute ratings, as discussed in [A Large-Scale Analysis of Evaluation Biases in LLMs](https://arxiv.org/abs/2305.17926) by Wang et al. (2023).
* The following figure ([source](https://arxiv.org/abs/1910.14424)) shows an illustration of a multi-stage ranking architecture involving BM25 as the first stage, monoBERT as the second stage, and duoBERT as the third stage. In the first stage \(H\_0\), given a query \(q\), the top-\(k\_0\) (\(k\_0 = 5\) in the figure) candidate documents \(R\_0\) are retrieved using BM25. In the second stage \(H\_1\), monoBERT produces a relevance score \(s\_i\) for each pair of query \(q\) and candidate \(d\_i \in R\_0\). The top-\(k\_1\) (\(k\_1 = 3\) in the figure) candidates with respect to these relevance scores are passed to the last stage \(H\_2\), in which duoBERT computes a relevance score \(p\_{i,j}\) for each triple \((q, d\_i, d\_j)\). The final list of candidates \(R\_2\) is formed by re-ranking the candidates according to these scores (see Section 3.3 for a description of how these pairwise scores are aggregated).

#### Listwise Encoder-Only Ranking

* Listwise ranking considers an entire candidate set jointly and optimizes ranking quality at the list level.

##### Architecture

* Extended cross-encoder
* Input includes multiple candidates (often truncated for efficiency)
* Output is a list of scores or a permutation distribution
* Listwise methods aim to optimize ranking metrics directly rather than approximating them via pairwise comparisons.

##### Example: ListBERT

* [ListBERT: Learning to Rank E-commerce Products with Listwise BERT](https://arxiv.org/abs/2206.15198) by Kumar et al. (2022)
* The following figure ([source](https://arxiv.org/abs/2206.15198)) shows the ListBERT architecture.

#### Direct and Approximate Optimization of NDCG

* A central motivation for listwise ranking is **directly optimizing ranking metrics** such as Normalized Discounted Cumulative Gain (NDCG).

##### NDCG Definition

* Given a ranked list, DCG is defined as:

\[\text{DCG} = \sum\_{i=1}^{n} \frac{2^{rel\_i} - 1}{\log\_2(i + 1)}\]

* … and NDCG is:

  \[\text{NDCG} = \frac{\text{DCG}}{\text{IDCG}}\]
  + where IDCG is the DCG of the ideal ranking.
* Because NDCG is non-differentiable, encoder-only models rely on **surrogate losses**.

##### Common Listwise Losses

* **ListMLE** ([Listwise Approach to Learning to Rank](https://dl.acm.org/doi/10.1145/1277741.1277800) by Cao et al. (2007)):

\[\mathcal{L}\_{\text{ListMLE}} = -\log P(\pi^\* \mid {d\_1,\dots,d\_n})\]

* **Softmax Cross-Entropy over relevance labels**
* **LambdaRank / LambdaLoss**, which approximate gradients of NDCG ([Learning to Rank Using Gradient Descent](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/MSR-TR-2005-82.pdf) by Burges et al. (2005))
* These methods weight gradient updates by estimated changes in NDCG, allowing encoder-only models to optimize ranking quality more directly.

#### Relationship to LLM-as-a-Judge Supervision

* Encoder-only rankers are often trained using supervision derived from LLM-as-a-Judge:

  + Pointwise judge scores \(\rightarrow\) regression or classification labels
  + Pairwise judge preferences \(\rightarrow\) ordered pairs
  + Aggregated judge rankings \(\rightarrow\) listwise permutations
* This weak supervision strategy is increasingly common in large-scale systems where human labels are scarce, and is conceptually aligned with RLAIF pipelines such as [Training Language Models from AI Feedback](https://arxiv.org/abs/2302.08582) by Bai et al. (2023).

#### Takeaways

* **Cross-encoder architectures enable high-precision ranking** by jointly encoding the query and candidate output, allowing full token-level interaction and capturing fine-grained relevance signals that simpler models miss.
* **All major LTR paradigms are supported**—pointwise (absolute scoring), pairwise (relative preferences), and listwise (global ordering)—with different trade-offs in supervision complexity, stability, and alignment with ranking objectives.
* **Listwise training methods enable approximate or direct optimization of NDCG**, using surrogate losses such as ListMLE or gradient-based approaches like LambdaRank to overcome the non-differentiability of ranking metrics.
* **LLM-as-a-Judge provides scalable, high-quality supervision signals** that can replace or augment human annotations, enabling efficient fine-tuning of encoder-based LTR models across pointwise, pairwise, and listwise settings.

### Encoder–Decoder Models for Learning-to-Rank (LTR): Listwise Reasoning at Decode Time

* Encoder–decoder architectures extend encoder-only rankers by enabling **list-level reasoning during decoding**, rather than relying solely on encoder-side interactions. This shift is especially powerful for **listwise ranking**, where the objective depends on the *entire ordering* of candidates (e.g., NDCG), and where global trade-offs across candidates matter.
* Foundational encoder–decoder models include [T5](https://arxiv.org/abs/1910.10683) by Raffel et al. (2019) and [BART](https://arxiv.org/abs/1910.13461) by Lewis et al. (2019). In ranking settings, these models are adapted to ingest multiple candidates and produce **ranking-aware outputs**—scores, permutations, or ordered tokens—via the decoder.

#### Why Encoder–Decoder for Ranking?

* Encoder-only listwise rankers face two core limitations:

  1. **Quadratic encoder cost** when jointly encoding many candidates.
  2. **Weak global reasoning**, since most listwise losses still rely on per-item scores.
* Encoder–decoder models address both by:

  + Encoding each candidate independently (linear in list size).
  + Performing **global interaction in the decoder**, which attends over *all* candidate encodings.
* This design enables richer list-level dependencies while keeping computation tractable.

#### Fusion-in-Decoder (FiD): The Core Pattern

* The canonical architecture for encoder–decoder ranking is **Fusion-in-Decoder (FiD)**, introduced in
  [Fusion-in-Decoder for Open-Domain Question Answering](https://arxiv.org/abs/2007.01282) by Izacard et al. (2021).

##### Architecture

* **Encoder**: independently encodes each (query, candidate) pair
* **Decoder**: attends jointly over all encoded representations
* **Output**: sequence conditioned on the *entire candidate set*
* The following figure ([source](https://arxiv.org/abs/2007.01282)) shows the architecture of the FiD architecture, where multiple embedded documents are fused at decoding time.

* Formally, each candidate \(d\_i\) is encoded as:

\[h\_i = \text{Enc}(q, d\_i)\]

* The decoder then conditions on the set \({h\_1, \dots, h\_n}\) to produce outputs.

#### ListT5: Encoder–Decoder Listwise Re-Ranking

* A representative ranking system built on FiD is **ListT5**.
* [ListT5: Listwise Re-ranking with Fusion-in-Decoder Improves Zero-shot Retrieval](https://arxiv.org/abs/2402.15838) by Yoon et al. (2024)

##### Architecture

* **Backbone:** T5-style encoder–decoder
* **Encoder input:** multiple (query, document) pairs
* **Decoder output:** **ranking tokens** representing an ordering
* Unlike encoder-only models that emit scalar scores, ListT5 generates a **sequence that encodes the ranking itself**.

##### Output Representation

* For a list of \(k\) candidates, the decoder emits a sequence such as:

  ```
    3 > 7 > 1 > 5 > ...
  ```
* This sequence represents a permutation \(\pi\) over candidates.

#### Training Objectives for Encoder–Decoder Ranking

* Encoder–decoder rankers are naturally trained with **sequence-level objectives**, which align well with listwise metrics.

##### Sequence Cross-Entropy Loss

* Given a target permutation \(\pi^\*\), training minimizes:

\[\mathcal{L}\_{\text{listwise}} =
-\sum\_{t=1}^{k} \log P(\pi^\*\_t \mid q, {d\_i}, \pi^\*\_{<t})\]

* This loss encourages the model to generate the correct ranking order token by token.

##### Connection to NDCG Optimization

* While NDCG is non-differentiable, encoder–decoder models approximate it by:

  + Training on permutations sorted by relevance labels
  + Emphasizing early positions in the sequence (higher DCG weight)
  + Using curriculum strategies that prioritize top-ranked correctness
* Some systems additionally **reweight token-level losses** by DCG discounts:

\[w\_t = \frac{1}{\log\_2(t + 1)}\]

* so that early ranking errors incur larger penalties, approximating NDCG optimization.

#### Advantages Over Encoder-Only Listwise Models

* Encoder–decoder rankers offer several advantages:

  + **True listwise reasoning** at decode time
  + **No need for score calibration**
  + **Direct permutation generation**
  + **Better alignment with ranking metrics**
* Empirically, ListT5 shows strong performance in **zero-shot and low-supervision** settings, outperforming encoder-only baselines on retrieval benchmarks, as reported in [ListT5: Listwise Reranking with Fusion-in-Decoder Improves Zero-shot Retrieval](https://arxiv.org/abs/2402.15838) Yoon et al. (2024).

#### Using LLM-as-a-Judge for Encoder–Decoder Supervision

* Encoder–decoder rankers are particularly well-suited to supervision from LLM-as-a-Judge:

  + **Pointwise judges** \(\rightarrow\) relevance labels used to construct permutations
  + **Pairwise judges** \(\rightarrow\) partial order constraints
  + **Listwise judges** \(\rightarrow\) direct target sequences
* This pipeline mirrors weak-supervision strategies used in [Training Language Models from AI Feedback](https://arxiv.org/abs/2302.08582) by Bai et al. (2023), where AI-generated preferences replace or augment human labels.

#### When to Use Encoder–Decoder Rankers

* Encoder–decoder ranking is most appropriate when:

  + Ranking quality matters more than latency
  + Candidate sets are moderate in size (e.g., 10–100)
  + List-level consistency is critical
  + Outputs must be globally coherent
* These models are increasingly used in **RAG pipelines**, **evaluation benchmarks**, and **zero-shot reranking** scenarios.

#### Takeaways

* **Encoder–decoder architectures enable listwise reasoning during decoding**, allowing global comparison across all candidates rather than independent scoring.
* **Fusion-in-Decoder (FiD) is the dominant architectural pattern for listwise LTR**, as it encodes each query–document pair independently and fuses all representations in the decoder. This avoids quadratic encoder costs while preserving the ability to compare and weigh all candidates jointly during ranking.
* **ListT5 demonstrates strong listwise ranking performance in low- and zero-shot settings** by adapting the T5 encoder–decoder architecture with FiD-style decoding and listwise objectives. Its results show that encoder–decoder rankers can generalize effectively even with limited supervised ranking data.
* **Sequence-level losses act as practical surrogates for direct NDCG optimization** because they encourage correct global orderings over candidate lists. Although NDCG itself is non-differentiable, sequence cross-entropy and permutation-based losses approximate its behavior by penalizing incorrect relative positions throughout the ranked list.
* **LLM-as-a-Judge enables scalable supervision**, supplying listwise training signals without extensive human annotation.

### Decoder-Based LLM-as-a-Judge for LTR

* Decoder-only LLMs, such as GPT-style architectures, can act directly as ranking judges through prompting, without explicit parameter fine-tuning. In these setups, ranking behavior is induced at inference time via natural language instructions rather than learned scoring heads. Prompt-based LLM-as-a-Judge systems naturally support pointwise, pairwise, and listwise LTR formulations.
* This section describes how each paradigm is realized with decoder-only judges and explains, in depth, how listwise losses and NDCG-based objectives arise when listwise judgments are used for optimization or supervision.
* Recent work demonstrates that decoder-based judges can be specialized into evaluator LLMs that closely match human and proprietary-LLM judgments under both pointwise and pairwise formulations. Notably, Prometheus-style evaluators formalize LLM-as-a-Judge as rubric-conditioned scoring within a decoder-only architecture ([Prometheus: Inducing Fine-grained Evaluation Capability in Language Models](https://arxiv.org/abs/2310.08491) by Kim et al. (2023); [Prometheus 2: An Open Source Language Model Specialized in Evaluating Other Language Models](https://arxiv.org/abs/2405.01535) by Kim et al. (2024)).
* These systems treat evaluation as a conditional generation problem over instructions, candidate outputs, optional reference answers, and explicit evaluation criteria, grounding ranking behavior in structured supervision rather than implicit prompting alone.

#### Pointwise Prompt-Based LLM-as-a-Judge

* In pointwise evaluation, each candidate output is judged independently against a rubric.

##### Prompt Pattern

* A typical pointwise judge prompt instructs the LLM to:

  + Read the task and evaluation criteria
  + Evaluate a single candidate output
  + Return a discrete label or numeric score
* Example:

  ```
    You are a judge. Based on the rubric below, assign a score from 1–5.
    Task: <task description>
    Output: <candidate>
    Rubric: <criteria>
    Score:
  ```

##### Interpretation as Pointwise LTR

* This corresponds to estimating an absolute relevance or quality score:

  \[s\_i = f(q, x\_i)\]
  + where \(q\) is the task specification and \(x\_i\) is a single output.
* This formulation underlies many practical LLM-as-a-Judge systems, including MT-Bench-style evaluations described in [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685) by Zheng et al. (2023).
* Beyond pure prompting, pointwise judging has been explicitly modeled via supervised evaluator LLMs trained to emit both natural-language rationales and scalar scores conditioned on user-defined rubrics and reference answers, as demonstrated in [Prometheus: Inducing Fine-grained Evaluation Capability in Language Models](https://arxiv.org/abs/2310.08491) by Kim et al. (2023).
* In this formulation, the scoring function is extended to include reference material and evaluation criteria:

  \[f\_{\text{direct}} : (q, x\_i, a, e) \rightarrow (r\_i, s\_i)\]
  + where \(a\) denotes a reference answer, \(e\) a structured score rubric, \(r\_i\) a verbal justification, and \(s\_i \in {1,2,3,4,5}\) the pointwise relevance score, enabling fine-grained, rubric-aligned supervision (cf. [Prometheus](https://arxiv.org/abs/2310.08491) by Kim et al. (2023)).
* Empirically, [Prometheus: Inducing Fine-grained Evaluation Capability in Language Models](https://arxiv.org/abs/2310.08491) by Kim et al. (2023) shows that rubric-conditioned pointwise judgments substantially improve correlation with human evaluators, achieving Pearson correlations comparable to GPT-4 on MT-Bench and Vicuna Bench.
* The following figure ([source](https://arxiv.org/abs/2310.08491)) shows that compared to conventional, coarse-grained LLM evaluation, a fine-grained approach that takes user-defined score rubrics as input.

##### Loss Function

* While prompt-based judging does not itself involve optimization, pointwise judge outputs are commonly reused as supervision signals when training downstream evaluators or reward models.
* In practice, scalar scores produced by judges are treated as regression targets and optimized using mean squared error:

\[\mathcal{L}\_{\text{MSE}} = (s\_i - \hat{s}\_i)^2\]

* When scores are discretized into ordinal buckets (e.g., 1–5), cross-entropy over score classes is also sometimes used, though regression losses are more common in evaluator training.
* Evaluator LLMs such as Prometheus are trained directly on rubric-conditioned pointwise supervision by minimizing the expected squared error between predicted and reference scores:

\[\mathcal{L}\_{\text{direct}} = \mathbb{E}\_{(q,x,a,e)} \left[(s\_i - \hat{s}\_i)^2\right]\]

* Importantly, Prometheus jointly models rationale generation and score prediction in a single autoregressive decoding pass, coupling interpretability with scalar accuracy rather than treating explanation and scoring as separate objectives ([Prometheus](https://arxiv.org/abs/2310.08491) by Kim et al. (2023)).

#### Pairwise Prompt-Based LLM-as-a-Judge

* In pairwise evaluation, the judge compares two candidates and expresses a preference.

##### Prompt Pattern

```
You are a judge. Which output is better for the task?
Task: <task>
Output A: <candidate A>
Output B: <candidate B>
Answer (A or B):
```

* This formulation mirrors pairwise preference modeling used in RLHF and ranking systems.

##### Pairwise LTR Interpretation

* The judge estimates:

\[P(x\_i \succ x\_j \mid q)\]

* This aligns with pairwise ranking frameworks such as RankNet and duoBERT, and is directly studied in [RankGPT: A Prompt-Based Pairwise Ranking Framework for LLMs](https://arxiv.org/abs/2304.09542) by Sun et al. (2023).
* Pairwise prompting has been extended to supervised evaluator LLMs capable of ranking outputs under explicit, user-defined criteria. [Prometheus 2: An Open Source Language Model Specialized in Evaluating Other Language Models](https://arxiv.org/abs/2405.01535) by Kim et al. (2024) introduces a unified formulation conditioning on the task, two candidates, optional reference answers, and an evaluation criterion:

  \[f\_{\text{pair}} : (q, x\_i, x\_j, a, e) \rightarrow (r\_{ij}, y\_{ij})\]
  + where \(y\_{ij} \in {i,j}\) denotes the preferred candidate and \(r\_{ij}\) is a comparative rationale highlighting criterion-specific differences.
* The following figure shows a comparison of direct assessment and pairwise ranking. Both responses could be considered decent under the umbrella of ‘helpfulness’. However, the scoring decision might change based on a specific evaluation criterion.

* [Prometheus 2: An Open Source Language Model Specialized in Evaluating Other Language Models](https://arxiv.org/abs/2405.01535) by Kim et al. (2024) demonstrates that pointwise and pairwise judges can be unified within a single decoder-only evaluator via weight merging, enabling strong performance across both LTR paradigms.

##### Associated Loss (When Used for Training)

* Pairwise judgments are commonly converted into a logistic loss:

\[\mathcal{L}\_{\text{pairwise}} = -\log \sigma(s\_i - s\_j)\]

* Pairwise prompting is known to reduce calibration variance relative to absolute scoring, a phenomenon also discussed in
  [Training Language Models to Follow Instructions with Human Feedback](https://arxiv.org/abs/2203.02155) by Ouyang et al. (2022).
* Prometheus 2 further shows that training separate pointwise and pairwise evaluators and merging their parameters yields higher agreement with human rankings than joint multi-task training, providing empirical justification for treating LLM-as-a-Judge systems as flexible LTR models whose optimization objective can shift between pointwise, pairwise, and listwise regimes ([Prometheus 2](https://arxiv.org/abs/2405.01535) by Kim et al. (2024)).

#### Listwise Prompt-Based LLM-as-a-Judge

* Listwise evaluation asks the LLM to reason jointly over an entire set of candidates and produce a ranked ordering or structured list-level judgment.

##### Prompt Patterns

* A common listwise prompt is:

  ```
    Rank the following outputs from best to worst according to the rubric:
    1. <candidate 1>
    2. <candidate 2>
    3. <candidate 3>
    Return the ranked order:
  ```
* Alternatively, the judge may be asked to assign scores jointly and produce a sorted list.

##### Listwise LTR Interpretation

* Listwise ranking models a permutation over candidates:

\[\pi = f(q, {x\_1, \dots, x\_n})\]

* Unlike pointwise or pairwise methods, listwise approaches optimize ranking quality **at the list level**, capturing interactions between candidates.
* Prompt-based listwise judging has been explored in recent work such as [Rank-K: Test-Time Reasoning for Listwise Reranking](https://arxiv.org/abs/2505.14432) by Yang et al. (2025), where decoder models explicitly reason about entire candidate sets.

#### Listwise Loss Functions and NDCG Optimization

* When listwise judgments from an LLM-as-a-Judge are used to train or evaluate ranking models, they are typically connected to **listwise loss functions**. These losses aim to optimize ranking quality **at the list level**, rather than independent scores, and are designed to align with ranking metrics such as NDCG.

##### Normalized Discounted Cumulative Gain (NDCG)

* One of the most widely used listwise ranking metrics is **NDCG**, introduced in [Cumulated Gain-based Evaluation of IR Techniques](https://dl.acm.org/doi/10.1145/582415.582418) by Järvelin and Kekäläinen (2002).
* For a ranked list of length \(k\), Discounted Cumulative Gain (DCG) is defined as:

\[\text{DCG}@k = \sum\_{i=1}^{k} \frac{2^{rel\_i} - 1}{\log\_2(i + 1)}\]

* where:

  + \(rel\_i\) is the relevance grade of the item at rank position \(i\)
* NDCG normalizes DCG by the ideal ranking:

\[\text{NDCG}@k = \frac{\text{DCG}@k}{\text{IDCG}@k}\]

* This normalization allows ranking quality to be compared across queries with different relevance distributions.

##### Optimizing NDCG

* NDCG is **non-differentiable** because it depends on discrete rank positions. As a result, it cannot be optimized directly with gradient descent. Instead, several surrogate strategies are used.

###### Listwise Surrogate Losses

* A common approach is to optimize a surrogate likelihood over permutations.
* **ListMLE**, introduced in [Listwise Approach to Learning to Rank](https://dl.acm.org/doi/10.1145/1277741.1277800) by Cao et al. (2007), models the probability of the ground-truth permutation (\pi^\*):

  \[\mathcal{L}\_{\text{ListMLE}} = -\log P(\pi^\* \mid s\_1, \dots, s\_n)\]
  + where \(s\_i\) are model scores. This loss encourages the model to assign higher scores to items appearing earlier in the target ranking.

###### Gradient-Based Approximations to NDCG

* Another family of methods directly approximates the **gradient of NDCG**.
* **LambdaRank** and **LambdaMART**, described in [Learning to Rank using Gradient Descent](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/MSR-TR-2010-82.pdf) by Burges et al. (2010), compute pairwise gradients weighted by the change in NDCG caused by swapping two items:

\[\lambda\_{i,j} \propto |\Delta \text{NDCG}\_{i,j}|\]

* This approach preserves the pairwise structure of optimization while explicitly targeting listwise ranking quality.

###### Using LLM Judges to Approximate NDCG

* In LLM-as-a-Judge pipelines:

  + The judge produces relevance grades or ranked lists
  + These induce a pseudo ground-truth permutation (\pi^\*)
  + NDCG can be computed directly on judge-derived rankings
  + Or used indirectly to supervise ranking models via listwise losses
* This allows **metric-aligned optimization without human annotations**, which is especially valuable in large-scale or continuously evolving systems.

##### Can Categorical Cross-Entropy Be Used for Listwise Ranking?

* **Categorical Cross-Entropy (CCE) can be used for listwise ranking**, but only under **specific formulations**, and it is important to understand its limitations.

###### When Categorical Cross-Entropy Applies

* Categorical cross-entropy can be used when **listwise ranking is reformulated as a classification problem**, typically in one of the following ways:

1. **Top-1 (or Top-k) Prediction**:
   * The model predicts which item should appear at rank 1 (or within the top \(k\)).
   * If a probability distribution over candidates is produced:\[P(i \mid q, {x\_1,\dots,x\_n})\]
   * … then categorical cross-entropy applies:

     \[\mathcal{L}\_{\text{CCE}} = -\sum\_{i=1}^{n} y\_i \log P(i)\]
     + where (y\_i) is a one-hot indicator of the correct top-ranked item.
2. **Position-Wise Classification**:
   * Some models decompose ranking into multiple classification steps, predicting which item belongs at each rank position. Each step uses categorical cross-entropy over remaining candidates.
3. **Softmax-Based Listwise Losses**:
   * Certain listwise objectives (including simplified versions of ListNet) can be interpreted as categorical cross-entropy between:

     + A target distribution derived from relevance labels
     + A predicted softmax distribution over scores
   * This perspective is discussed in [Learning to Rank: From Pairwise Approach to Listwise Approach](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/MSR-TR-2007-40.pdf) by Cao et al. (2007).

###### Limitations of Categorical Cross-Entropy for Ranking

* While usable, categorical cross-entropy has important limitations in ranking contexts:

  + It does **not directly model permutations**, only class probabilities
  + It does **not encode rank position sensitivity** (e.g., top-heavy emphasis)
  + It does **not naturally align with NDCG**, which discounts lower ranks
  + It assumes a single correct label or distribution, which may not reflect graded relevance
* As a result, categorical cross-entropy is generally **inferior to NDCG-aware losses** (e.g., ListMLE, LambdaRank) when the goal is high-quality ranking across the entire list.

###### Relationship to NDCG

* Categorical cross-entropy is **not an NDCG-consistent loss**. Optimizing CCE does not guarantee improvements in NDCG, except in restricted cases (e.g., when only top-1 accuracy matters).
* Therefore, in practice:

  + **CCE is acceptable for coarse listwise supervision**
  + **NDCG-driven or permutation-based losses are preferred for ranking quality**
  + **LLM-as-a-Judge outputs are often better consumed via NDCG-aligned objectives**

##### Input–Output Example (Listwise)

* **Input**: Task + 5 candidate summaries
* **LLM Judge Output**: `3 > 1 > 5 > 2 > 4`
* **Derived Supervision**:

  + Permutation \(\pi^\*\)
  + Optional relevance grades inferred from positions
  + NDCG computed against downstream model outputs

#### Takeaways

* **Pointwise judging** estimates absolute quality scores for individual outputs
* **Pairwise judging** models relative preferences between two outputs
* **Listwise judging** produces global rankings over entire candidate sets
* **NDCG** is the dominant evaluation metric for listwise ranking quality
* **NDCG is non-differentiable** and therefore requires surrogate optimization methods
* **Listwise losses such as ListMLE and LambdaRank** effectively approximate NDCG during training
* **Categorical cross-entropy (CCE)** can be used in constrained listwise setups (e.g., top-1 or position-wise classification)
* **CCE is generally weaker than NDCG-aware losses** for full-list ranking optimization
* **LLM-as-a-Judge** enables scalable, metric-aligned supervision and generation of listwise training signals

## Automatic Prompt Optimization (APO) for LLM-as-a-Judge

* This section explores integrating Automatic Prompt Optimization (APO) directly into the LLM-as-a-Judge narrative. The core idea is that judge reliability is dominated not only by the underlying model, but by the quality of the evaluation prompt itself. APO methods turn judge prompt design into a data-driven learning problem rather than a manual craft.

### Why Prompt Optimization Is Critical for LLM-as-a-Judge

* LLM-as-a-Judge systems depend on prompts that specify evaluator roles, rubrics, scales, and constraints. As established throughout the primer, even small prompt variations can significantly affect scores, rankings, and bias characteristics. This sensitivity introduces a new failure mode: evaluation instability driven by prompt mis-specification rather than model capability.
* APO addresses this by treating the judge prompt as an optimizable object. Instead of freezing the prompt and evaluating models, we iteratively improve the prompt itself using feedback derived from data. This reframing aligns naturally with LTR, reinforcement-style feedback loops, and weak supervision pipelines used throughout modern LLM evaluation.
* A canonical method in this space is ProTeGi, introduced in [Automatic Prompt Optimization with “Gradient Descent” and Beam Search](https://arxiv.org/abs/2305.03495) by Pryzant et al. (2023).

### ProTeGi: Prompt Optimization with Textual Gradients

* ProTeGi is a non-parametric algorithm that optimizes prompts using only black-box access to an LLM API. This makes it particularly relevant for LLM-as-a-Judge systems, which often rely on proprietary models where gradients and internal states are inaccessible.
* At a high level, ProTeGi mimics gradient descent in natural language space. Instead of computing numerical gradients with respect to parameters, it computes textual gradients: natural-language descriptions of how and why the current prompt fails.
* The following figure shows an overview of Prompt Optimization with Textual Gradients (ProTeGi), illustrating how a prompt is evaluated on data, critiqued via textual gradients, and iteratively refined through editing and search.

### Formal Objective

* Let:

  + \(p \in \mathcal{L}\) denote a prompt written in natural language,
  + \(\mathcal{D}\_{\mathrm{tr}} = {(x\_i, y\_i)}\_{i=1}^n\) be training data,
  + \(\mathrm{LLM}\_p(x)\) be the output of the LLM when prompted with \(p\) and input \(x\),
  + \(m(p, \mathcal{D})\) be an evaluation metric (e.g., accuracy, F1, or agreement with human judges).
* The optimization goal is:

  \[p^\* = \arg\max\_{p \in \mathcal{L}} m(p, \mathcal{D}\_{\mathrm{te}})\]
  + where \(\mathcal{D}\_{\mathrm{te}}\) is a held-out validation or test set.
* This objective mirrors how LLM-as-a-Judge prompts are evaluated in practice: by measuring how well judge outputs align with desired evaluation behavior.

### Textual Gradients as Loss Signals

* ProTeGi replaces numerical loss gradients with natural-language critiques. Given a prompt \(p\), the algorithm evaluates it on a minibatch \(\mathcal{D}\_{\mathrm{mini}} \subset \mathcal{D}\_{\mathrm{tr}}\) and collects errors:

\[e = {(x\_i, y\_i) \in \mathcal{D}\_{\mathrm{mini}} \mid \mathrm{LLM}\_p(x\_i) \neq y\_i}\]

* A fixed feedback prompt \(\nabla\) then instructs the LLM to analyze these errors and produce a textual gradient:

\[g = \mathrm{LLM}\_{\nabla}(p, e)\]

* The gradient \(g\) is a semantic error signal describing flaws in the prompt, such as vague instructions, missing constraints, or ambiguous rubric definitions. Conceptually, \(g\) plays the same role as a loss gradient in parameter space, but operates over meaning rather than numbers.

### Prompt Updates via Semantic Gradient Descent

* Given a textual gradient \(g\), a second fixed editing prompt \(\delta\) asks the LLM to revise the original prompt in the opposite semantic direction, meaning that the edit explicitly counteracts the failure modes identified in \(g\) by adding missing constraints, clarifying ambiguous instructions, strengthening underspecified criteria, or removing misleading or overly permissive language that contributed to the observed errors:

\[p' = \mathrm{LLM}\_{\delta}(p, g)\]

* Rather than producing a single update, ProTeGi generates multiple candidate prompts at each step, reflecting uncertainty in how best to fix the identified issues. This mirrors stochastic or multi-directional updates in optimization.
* The following figure shows the dialogue tree used to mimic gradient descent, where feedback prompts generate textual gradients and editing prompts apply them to produce improved prompts across iterations.

### Beam Search over the Prompt Space

* Because the space of coherent natural-language prompts is discrete, high-dimensional, and highly non-convex, ProTeGi cannot rely on a single sequence of prompt edits. Instead, it embeds textual gradient updates inside a beam search procedure that explicitly maintains multiple competing hypotheses about what a “better” prompt might look like. This design choice is central to the algorithm’s robustness and efficiency.
* At iteration \(t\), ProTeGi maintains a beam:

  \[B\_t = {p\_t^{(1)}, p\_t^{(2)}, \dots, p\_t^{(b)}}\]
  + where \(b\) is the beam width. Each prompt in the beam represents a distinct semantic hypothesis about how the task should be specified.

#### Expansion Step: Generating Successor Prompts

* For each prompt \(p \in B\_t\), ProTeGi applies an expansion operator \(\mathrm{Expand}(p)\), which generates a diverse set of successor prompts using three mechanisms described explicitly in the [paper](https://arxiv.org/abs/2305.03495):

  1. **Minibatch-driven error analysis**: The prompt \(p\) is evaluated on a randomly sampled minibatch \(\mathcal{D}\_{\mathrm{mini}} \subset \mathcal{D}\_{\mathrm{tr}}\), and incorrect predictions are collected:

     \[e = {(x\_i, y\_i) \mid \mathrm{LLM}\_p(x\_i) \neq y\_i}\]
  2. **Textual gradient generation**: A fixed feedback prompt \(\nabla\) instructs the LLM to analyze these errors and describe systematic flaws in \(p\). For example, in the jailbreak detection task, a typical gradient might state that the prompt “fails to account for indirect or hypothetical attempts to bypass safety rules,” directly identifying a semantic blind spot in the original instructions.
  3. **Prompt editing and paraphrasing**: Each textual gradient \(g\) is applied to \(p\) using an editing prompt \(\delta\), producing multiple revised prompts that attempt to fix the identified issues. These revised prompts are then further paraphrased using a separate LLM call to explore nearby regions of the semantic space while preserving meaning.
* As a result, \(\mathrm{Expand}(p)\) returns a heterogeneous set of candidates:

\[\mathrm{Expand}(p) = {p'\_1, \dots, p'\_k} \cup {p''\_{11}, \dots, p''\_{km}}\]

* where the \(p'\) prompts reflect directed improvements guided by textual gradients, and the \(p''\) prompts represent local Monte Carlo exploration through paraphrasing.

#### Selection Step: Updating the Beam

* After expansion, the candidate set can grow rapidly, often to dozens or hundreds of prompts per iteration. ProTeGi therefore applies a selection operator \(\mathrm{Select}\_b(\cdot)\) to retain only the top \(b\) candidates:

\[B\_{t+1} = \mathrm{Select}\_b \left( \bigcup\_{p \in B\_t} \mathrm{Expand}(p) \right)\]

* Importantly, selection is not done by exhaustively evaluating every candidate on the full training set. Instead, ProTeGi uses approximate performance estimates obtained from limited data, which are refined adaptively across iterations.

#### Exploitation–Exploration Trade-off

* This beam search structure enables a principled balance between exploitation and exploration:

  + **Exploitation**: High-performing prompts remain in the beam across iterations and are repeatedly refined using new textual gradients. In the paper’s experiments, this leads to prompts that progressively rewrite vague task descriptions into precise, annotation-style instructions.
  + **Exploration**: Maintaining multiple prompts in the beam prevents premature convergence. Even if an early gradient is misleading or overly specific, alternative prompts can survive and later outperform the initial leader. Paraphrasing further diversifies the search by exploring semantically equivalent but syntactically distinct formulations.
* The authors show empirically that this balance is critical: greedy prompt editing underperforms beam-based optimization, while beam search enables ProTeGi to achieve up to 31% relative improvement over the initial prompt across tasks such as hate speech detection, fake news classification, and jailbreak detection.

### Selection as Best-Arm Identification

* After beam expansion, ProTeGi must choose which prompt candidates are worth keeping. A naïve approach—evaluating every candidate prompt on the full training set—would be prohibitively expensive, since each evaluation requires multiple LLM API calls. ProTeGi addresses this by reframing prompt selection as a best-arm identification problem from bandit optimization.

#### Mapping Prompt Selection to Bandits

* In this formulation:

  + Each prompt candidate \(p\_i\) is treated as an arm.
  + Let \(\mathcal{D}\_{\mathrm{tr}}\) denote the full training dataset, and let \(m(\cdot, \cdot)\) be the task-specific evaluation metric (for example, accuracy). The true (unknown) reward of an arm is defined as its performance on the full dataset:

    \[\mu(p\_i) = m(p\_i, \mathcal{D}\_{\mathrm{tr}})\]
  + Let \(\mathcal{D}\*{\mathrm{sample}} \subset \mathcal{D}\*{\mathrm{tr}}\) denote a randomly sampled minibatch from the training data. Pulling an arm corresponds to evaluating the prompt on this minibatch, producing a noisy reward observation at time step \(t\):

    \[r\_{i,t} = m(p\_i, \mathcal{D}\_{\mathrm{sample}})\]
* The objective is not regret minimization (as in classic online bandits), but identification of the top \(b\) arms with the highest expected rewards using as few total evaluations as possible. This distinction is critical and motivates the specific algorithms explored in the [paper](https://arxiv.org/abs/2305.03495).

#### Upper Confidence Bound (UCB) and UCB-E

* ProTeGi first considers UCB-style algorithms, which balance exploration and exploitation by augmenting empirical performance estimates with uncertainty terms.

  + For each prompt \(p\_i\), the UCB score at time \(t\) is:\[\mathrm{UCB}\_t(p\_i) = Q\_t(p\_i) + c \sqrt{\frac{\log t}{N\_t(p\_i)}}\]
  + where:

    - \(Q\_t(p\_i)\) is the empirical mean performance,
    - \(N\_t(p\_i)\) is the number of samples evaluated so far,
    - \(c\) controls the exploration–exploitation trade-off.
* UCB-E is a more exploration-heavy variant designed specifically for best-arm identification, offering better theoretical guarantees in this setting. In practice, however, the authors observe that both UCB and UCB-E introduce additional hyperparameters (e.g., the exploration coefficient \(c\), which must be carefully tuned to avoid under- or over-exploration, and the total sampling budget \(T\), which determines how many minibatch evaluations are allocated across arms) that can be brittle across tasks.

#### Successive Rejects: A Natural Fit

* To avoid tuning-sensitive hyperparameters, ProTeGi emphasizes Successive Rejects, a provably optimal algorithm for best-arm identification.
* The algorithm operates in \(n - 1\) phases for \(n\) candidate prompts:

  1. Initialize the surviving set:
     \(S\_0 = {p\_1, \dots, p\_n}\)
  2. At phase \(k\), evaluate each \(p \in S\_{k-1}\) on \(n\_k\) data points and compute empirical scores.
  3. Eliminate the lowest-performing prompt to obtain \(S\_k\).
* The evaluation budget per phase is allocated according to:

  \[n\_k =
  \left\lfloor
  \frac{1}{0.5 + \sum\_{i=2}^{n} \frac{1}{i}}
  \cdot
  \frac{B - n}{n + 1 - k}
  \right\rfloor\]
  + where \(B\) is the total query budget. This schedule gradually increases evaluation fidelity as the candidate set shrinks, ensuring efficient use of LLM calls.

#### Successive Halving

* ProTeGi also evaluates Successive Halving, a more aggressive variant in which roughly half of the candidates are discarded at each phase:

\[n\_k = \frac{B}{|S\_{k-1}| \log\_2 |S\_{k-1}|}\]

* While this can reduce computation further, it risks prematurely discarding promising prompts when performance estimates are still noisy. The [paper](https://arxiv.org/abs/2305.03495) reports that Successive Rejects offers a better robustness–efficiency trade-off across tasks.

#### Example from the Paper

* In the jailbreak detection experiments, beam expansion generates many prompt variants that differ subtly in how they define “intent,” “policy circumvention,” or “hypothetical scenarios.” Early minibatch evaluations are noisy, but Successive Rejects quickly eliminates prompts that rely on superficial keyword matching. Prompts that explicitly instruct the judge to reason about intent and indirect strategies consistently survive later phases, eventually dominating the beam.
* Crucially, these high-quality prompts are identified without ever evaluating all candidates on the full dataset, reducing LLM API usage while still achieving up to 31% relative improvement over the initial prompt.

### Implications for LLM-as-a-Judge Systems

* ProTeGi is particularly well-suited to LLM-as-a-Judge settings, where prompt evaluation is expensive, performance differences are subtle and noisy, and overfitting to small validation sets is a real risk.
* ProTeGi integrates naturally with LLM-as-a-Judge in several ways:

  1. **Judge prompt calibration**: Evaluation prompts defining roles, rubrics, and scoring scales can be optimized to better match human judgments, improving agreement and reducing variance.
  2. **Bias mitigation**: Textual gradients explicitly surface systematic judge failure modes (e.g., verbosity bias, keyword over-reliance, underspecified criteria), enabling targeted and interpretable prompt corrections.
  3. **Metric alignment**: By defining a metric \(m(\cdot)\) as agreement with human evaluators, pairwise preferences, or downstream ranking quality, prompt optimization directly aligns judge behavior with evaluation objectives.
  4. **Weak supervision pipelines**: Higher-quality judge prompts yield cleaner and more stable supervision signals for LTR models and RLAIF pipelines, compounding downstream performance gains.
* By framing prompt selection as best-arm identification, ProTeGi allocates evaluation budget efficiently, avoiding exhaustive validation while remaining statistically grounded, and making large-scale, automatic optimization of LLM-as-a-Judge prompts feasible in practice.

### Key Takeaways

* APO elevates LLM-as-a-Judge from a static evaluation heuristic to a learnable, improvable component. ProTeGi demonstrates that judge prompts can be optimized using principled, interpretable, and data-driven methods that closely parallel classical optimization, but operate in semantic space.
* ProTeGi closes an important loop in modern evaluation pipelines: not only are models evaluated by LLMs, but the evaluators themselves can be systematically improved.

## Putting It All Together: LLM-as-a-Judge in Modern Evaluation Pipelines

* This section synthesizes the ideas from earlier sections and shows how **LLM-as-a-Judge**, **LTR**, and **neural ranking models** are combined in practice. We focus on end-to-end system design, typical pipelines, and known failure modes.

### End-to-End Evaluation Pipelines with LLM-as-a-Judge

* A canonical modern evaluation pipeline looks like:

  1. **Generation stage**: A base model (or multiple candidate models) produces outputs for a task.
  2. **Judging stage (LLM-as-a-Judge)**: A judge model evaluates each output using a structured prompt (often pointwise).
  3. **Aggregation / ranking stage**: Scores are aggregated, thresholded, or ranked to:

     + Select the best output
     + Filter low-quality data
     + Produce training signals
  4. **Optional learning stage**: Judge outputs are used to fine-tune ranking or reward models.
* This pattern appears in many systems, including OpenAI’s internal evaluation tooling ([Introducing OpenAI Evals](https://openai.com/blog/evals)) and Anthropic’s RLAIF pipelines ([Training Language Models from AI Feedback](https://arxiv.org/abs/2302.08582) by Bai et al. (2023)).

### Combining Prompted Judges with Trained Rankers

* In practice, systems often use a **hybrid approach**:

  + **LLM-as-a-Judge** for:

    - Bootstrapping labels
    - Evaluating new tasks
    - Handling subjective criteria
  + - **Trained encoder LTR models** for:
    - Low-latency inference
    - Large-scale ranking
    - Stable, repeatable behavior
* A common pattern:

  1. Use an LLM judge to score or rank outputs offline
  2. Train a pointwise, pairwise, or listwise ranker on these signals
  3. Deploy the ranker in production
  4. Periodically refresh supervision with the judge
* This mirrors the teacher–student paradigm described in [Distilling Step-by-Step](https://arxiv.org/abs/2303.17071) by Magister et al. (2023).

### Failure Modes and Limitations of LLM-as-a-Judge

* Despite its power, LLM-as-a-Judge has known weaknesses.

#### Bias and Positional Effects

* LLM judges may exhibit:

  + Preference for longer or more verbose outputs
  + Positional bias in pairwise or listwise setups
  + Over-rewarding fluent but incorrect responses
* These effects are analyzed in [Large Language Models Are Not Fair Evaluators](https://arxiv.org/abs/2305.17926) by Wang et al. (2023).
* A detailed discourse on biases in LLM-as-a-Judge systems is available in the [Biases and Mitigation Strategies](#biases-and-mitigation-strategies) section.

#### Prompt Sensitivity and Variance

* Judge outputs can vary with:

  + Prompt phrasing
  + Ordering of criteria
  + Presence or absence of examples
* Mitigations include:

  + Anchored examples (as in your prompt)
  + Schema-constrained outputs
  + Majority voting or self-consistency
* See [Self-Consistency Improves Chain of Thought Reasoning](https://arxiv.org/abs/2203.11171) by Wang et al. (2022).

#### Over-Optimization and Reward Hacking

* When models are trained directly against a fixed judge:

  + They may exploit blind spots in the rubric
  + Scores may increase without true quality gains
* This is analogous to reward hacking in RL, discussed in [Specification Gaming](https://arxiv.org/abs/1903.03400) by Krakovna et al. (2020).

### Best Practices for Production Use

* Empirically grounded best practices include:

  + Use **pointwise judging** by default; escalate to pairwise/listwise only when needed
  + Keep rubrics simple and interpretable
  + Separate hard constraints (binary) from subjective criteria (Likert-type)
  + Periodically revalidate judge alignment with humans
  + Avoid training directly against a single static judge
* These principles align with guidance from [How to Evaluate Language Models: A Survey](https://arxiv.org/abs/2307.03109) by Chang et al. (2023).

### Summary and Outlook

* LLM-as-a-Judge represents a shift from brittle, task-specific metrics toward **learned, semantic evaluation**. When combined with Learning-to-Rank methods and neural ranking models:

  + It enables scalable, flexible evaluation
  + It provides supervision for ranking and reward models
  + It integrates naturally into RAG and alignment pipelines
* Future directions include:

  + Multi-judge ensembles
  + Calibrated uncertainty estimation
  + Hybrid human–AI evaluation loops
  + Formal guarantees on judge consistency

## Panel / Jury of LLMs-as-Judges

* Before discussing bias modes and mitigation strategies for individual LLM judges, it is important to introduce a complementary and increasingly influential idea: **using a panel (or jury) of LLMs-as-Judges instead of a single judge model**. Panels of LLMs-as-Judges represent a principled extension of LLM-as-a-Judge in which **multiple evaluator models jointly assess outputs**, and their judgments are aggregated.
* This approach is motivated by bias reduction, robustness, and cost–performance trade-offs, and is formalized and empirically validated in [Replacing Judges with Juries: Evaluating LLM Generations with a Panel of Diverse Models](https://arxiv.org/abs/2404.18796) by Verga et al. (2024).
* Panels provide a **systematic improvement over single-judge evaluation** by:

  + Reducing intra-model bias
  + Increasing agreement with human judgments
  + Improving robustness to prompt perturbations
  + Lowering cost and latency relative to a single large judge
* They represent a natural evolution of LLM-as-a-Judge toward **jury-style evaluation**, aligning automated evaluation with best practices from human annotation, information retrieval, and statistical reliability theory.

### Motivation: Why a Single Judge Is Not Enough

* Most LLM-as-a-Judge systems rely on a **single strong evaluator**, often a frontier proprietary model such as GPT-4. While convenient, this design has several fundamental limitations:

  1. **Intra-model bias**: Judge models tend to recognize and favor outputs that are stylistically, semantically, or distributionally similar to their own generations. This self-preference effect is empirically documented in [LLM Evaluators Recognize and Favor Their Own Generations](https://arxiv.org/abs/2401.01917) by Panickssery et al. (2024).
  2. **High variance and prompt sensitivity**: Small changes in prompt wording or formatting can produce large swings in evaluation outcomes, particularly for large models that over-reason or inject external knowledge. This instability is demonstrated in [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685) by Zheng et al. (2023).
  3. **Cost and latency at scale**: Using a single frontier model as a judge is expensive and slow, limiting scalability, accessibility, and continuous evaluation.
* [Replacing Judges with Juries: Evaluating LLM Generations with a Panel of Diverse Models](https://arxiv.org/abs/2404.18796) by Verga et al. (2024) empirically show that even very strong models such as GPT-4 can be **surprisingly weak or unstable judges** in certain settings, motivating a shift away from single-oracle evaluation.
* The core insight is that **evaluation suffers from the same variance and subjectivity problems as human annotation**, and therefore benefits from aggregation rather than reliance on a single rater—an idea long established in IR evaluation practice.

### Panel of LLM Evaluators (PoLL): Core Concept

* A **Panel of LLM Evaluators (PoLL)** replaces a single judge \(J\) with a set of heterogeneous judges:

\[{J\_1, J\_2, \dots, J\_k}\]

* Ideally, these judges are drawn from **different model families**.
* Instead of computing an evaluation score as:

\[\text{score}(a) = J(a)\]

* PoLL computes:

  \[\text{score}(a) = f\bigl(J\_1(a), J\_2(a), \dots, J\_k(a)\bigr)\]
  + where:

    - \(a\) is the model-generated output being evaluated
    - \(J\_i(a)\) is the judgment from the \(i\)-th evaluator
    - \(f\) is an aggregation (pooling or voting) function
* This formulation mirrors classical techniques for reducing annotator variance in information retrieval and QA evaluation, as discussed in [Variations in Relevance Judgments and the Measurement of Retrieval Effectiveness](https://dl.acm.org/doi/10.1145/290941.291017) by Voorhees (1998).

### Judge Diversity and Panel Composition

* A key design principle of PoLL is **heterogeneity**. The PoLL study constructs panels using evaluators from disjoint model families, including:

  + GPT-3.5 (OpenAI)
  + Claude 3 Haiku (Anthropic)
  + Command R (Cohere)
* The motivation is to reduce **correlated errors and self-preference effects**, which arise when judges share training data, architectural biases, or generation styles.
* Crucially, Verga et al. (2024) find that:

> **A panel of smaller, cheaper, heterogeneous models consistently outperforms a single large model as a judge**, when measured against human judgments.

* This supports broader findings that evaluator quality is **task- and bias-dependent**, rather than monotonically increasing with model size, as also observed in [An Empirical Study of LLM-as-a-Judge for LLM Evaluation](https://arxiv.org/abs/2403.02839) by Huang et al. (2024).

### Aggregation and Voting Strategies

* Different evaluation scales require different aggregation functions.

#### Binary Judgments (e.g., QA correctness)

* Max pooling is effective:

\[f\_{\max}(a) = \max\_j J\_j(a)\]

* This favors recall and avoids false negatives when at least one judge correctly identifies validity.

#### Ordinal or Likert-Type Scores (e.g., 1–5 ratings)

* Mean (average) pooling is preferred:

\[f\_{\text{avg}}(a) = \frac{1}{k}\sum\_{j=1}^k J\_j(a)\]

* Averaging produces smoother, more stable scores than majority voting for ordinal scales.

#### Pairwise Preference Judgments

* Each judge produces a preference \(a \succ b\), and aggregation is typically performed via **majority voting** or averaged logits.
* The choice of aggregation function directly affects bias, variance, and sensitivity, and should be aligned with the underlying rubric scale.

### Empirical Results and Human Correlation

* PoLL is evaluated across the following data across six datasets, including KILT-NQ, TriviaQA, HotpotQA, Bamboogle, and Arena-Hard:

  + Single-hop QA
  + Multi-hop QA
  + Pairwise chatbot evaluation (Chatbot Arena / Arena-Hard)
* The following figure shows (top) rankings of model performance change drastically depending on which LLM is used as the judge on KILT-NQ; (bottom) panel of LLM evaluators (PoLL) has the highest Cohen’s \(\kappa\) correlation with human judgements.\*\*

* Key empirical findings from Verga et al. (2024):

  + Higher Cohen’s \(\kappa\) agreement with humans on QA tasks
  + Higher Kendall–\(\tau\) and Pearson correlation with human rankings
  + Lower variance across prompts and evaluator choices
  + Dramatically reduced intra-model bias (models no longer rank themselves highest)
* These results directly reinforce concerns raised in [Large Language Models Are Not Fair Evaluators](https://arxiv.org/abs/2305.17926) by Wang et al. (2023).

### Cost and Latency Advantages

* A counterintuitive but important result is that PoLL is **significantly cheaper and often faster** than using a single large judge:

  + A three-model PoLL is reported to be **7–8× cheaper** than GPT-4 Turbo
  + Parallel execution of smaller models reduces wall-clock latency
* This undermines the assumption that the best judge must always be the largest or most capable model.

### Relationship to LLM-as-a-Judge and LTR Paradigms

* Panels of judges can be applied across **all evaluation and ranking paradigms**:
* **Pointwise**: each judge scores outputs independently; scores are pooled
* **Pairwise**: each judge compares outputs; preferences are aggregated
* **Listwise**: each judge ranks a list; rankings are combined (e.g., Borda count)
* In practice:

> Panels are most commonly used in **pointwise and pairwise LLM-as-a-Judge setups**, where they deliver the largest robustness gains per unit cost.

* This complements listwise ranking approaches such as
  [ListBERT](https://arxiv.org/abs/2206.15198) by Kumar et al. (2022) and
  [ListT5](https://arxiv.org/abs/2402.15838) by Yoon et al. (2024), where diversity is typically introduced at the data or decoding level rather than the evaluator level.

### Practical Guidance: When to Use a Panel of Judges

* Use a **panel of LLM judges** when:

  + Evaluation bias has high downstream cost
  + Human agreement is critical
  + You are benchmarking, publishing, or reporting results
  + Single-judge variance is unacceptable
  + Cost constraints rule out a single large judge
* Panels are less necessary when:

  + Tasks are trivial or highly objective
  + Absolute correctness can be verified symbolically
  + Latency budgets are extremely tight
  + Trained rankers already handle evaluation in production

### Takeaways

* Panels of LLMs-as-Judges transform evaluation from a single-oracle decision into a **statistical estimation problem**. By leveraging diversity, aggregation, and redundancy, PoLL delivers:

  + Higher human alignment
  + Reduced bias
  + Lower variance
  + Better cost–performance trade-offs
* As such, jury-style evaluation forms a natural foundation for robust LLM-as-a-Judge systems and directly motivates the subsequent discussion of **biases in LLM-as-a-Judge and mitigation strategies**.

## Multimodal LLMs-as-Judges (LMM / VLM-as-a-Judge)

* This section introduces **multimodal LLMs-as-Judges**, where the evaluator model directly consumes and reasons over **non-textual inputs** (images, and in some cases video) in addition to text. This paradigm extends LLM-as-a-Judge beyond purely linguistic tasks and is essential for evaluating modern **vision-language models (VLMs)** and **large multimodal models (LMMs)**.
* Multimodal LLMs-as-Judges extend the LLM-as-a-Judge paradigm to perception-heavy tasks, enabling **grounded, scalable, and interpretable evaluation** of vision-language systems. Together with panel-based judging and bias-aware mitigation strategies, they form a critical foundation for evaluating and aligning next-generation multimodal models.
* We focus on two representative and influential lines of work:

  + **LLaVA-Critic**: a generalist multimodal judge trained for broad evaluation and preference learning
  + **Prometheus-Vision**: a fine-grained rubric-driven VLM evaluator

### Why Multimodal Judges Are Necessary

* Text-only LLM judges are fundamentally limited when evaluating multimodal tasks:

  + They cannot directly perceive visual content
  + They rely on intermediate captions or OCR pipelines
  + Errors propagate from perception to judgment
  + Multiple inference stages increase cost and latency
* These limitations are explicitly discussed in [Prometheus-Vision: Vision-Language Model as a Judge for Fine-Grained Evaluation](https://arxiv.org/abs/2401.06591) by Lee et al. (2024). The following figure ([source](https://arxiv.org/abs/2401.06591)) illustrates the fact that conventional metrics measure the similarity between the response and ground-truth answer, which is not expressive enough. Moreover, it could not pinpoint what is missing within the response with respect to the evaluation criteria. In contrast, the VLM-as-a-Judge pipeline provides not only the flexibility to adhere to arbitrary evaluation criteria but also provides detailed language feedback that specifically pinpoints the deficiencies.

* As a result, **VLM-as-a-Judge** (or LMM-as-a-Judge) has emerged, where the judge model directly processes the same multimodal inputs as the model being evaluated.

### Paradigm: VLM / LMM-as-a-Judge

* Formally, a multimodal judge estimates:

\[s\_i = f\_\theta(x^{\text{image}}, x^{\text{text}}, y\_i)\]

* where:

  + \(x^{\text{image}}\) is the visual input
  + \(x^{\text{text}}\) is the instruction or question
  + \(y\_i\) is the candidate response
  + \(s\_i\) is a score, label, or preference
* This mirrors pointwise and pairwise LTR, but with **joint multimodal grounding**.
* Multimodal judges are now used for:

  + Visual instruction following
  + Image and video captioning evaluation
  + Visual QA and reasoning
  + Hallucination detection
  + Preference learning and reward modeling

### LLaVA-Critic: Generalist Multimodal Judge

#### Overview

* **LLaVA-Critic** is the first open-source **generalist multimodal evaluator**, explicitly trained to act as a judge across a wide range of vision–language tasks.
* Paper: [LLaVA-Critic: Learning to Evaluate Multimodal Models](https://arxiv.org/abs/2410.02712) by Xiong et al. (2024)
* Project page: [LLaVA-Critic blog](https://llava-vl.github.io/blog/llava-critic)

#### Key Contributions

* Introduces **critic instruction-following data** for multimodal evaluation
* Supports both **pointwise scoring** and **pairwise ranking**
* Produces **scores + natural language justifications**
* Matches or exceeds GPT-4V / GPT-4o alignment on multiple benchmarks
* Enables **preference learning** for LMM alignment

#### Training Data and Setup

* Each training instance follows:

\[(\text{Image}, \text{Question}, \text{Response}, \text{Criteria}, \text{Score}, \text{Reason})\]

* … or, in pairwise mode:

\[(\text{Image}, \text{Question}, \text{Response}\_1, \text{Response}\_2, \text{Criteria}, \text{Preference}, \text{Reason})\]

* The model is fine-tuned using **standard autoregressive cross-entropy loss** over both the judgment and justification tokens.

#### Architecture

* **Backbone:** LLaVA-OneVision (7B / 72B)
* Multimodal encoder + language decoder
* Evaluation treated as instruction-following generation
* The following figure ([source](https://arxiv.org/abs/2410.02712)) shows an example of LLaVA-Critic training data. The top block shows pointwise scoring, where LLaVA-Critic predicts a score to evaluate a single response’s quality; the bottom block illustrates pairwise ranking, where it rank response pairs. In both settings, LLaVA-Critic learns to provide reasons for its judgments.

#### Evaluation Scenarios

* LLaVA-Critic is evaluated on:

  + Visual chat benchmarks (LLaVA-in-the-Wild, LLaVA-Wilder)
  + Integrated capability benchmarks (MMVet)
  + Hallucination detection (MMHal-Bench)
  + Preference benchmarks (WildVision Arena)
* It shows strong **Pearson correlation** and **Kendall’s \(\tau\)** with GPT-4o and human judgments, even at 7B scale.

### Prometheus-Vision: Fine-Grained Multimodal Evaluation

#### Overview

* **Prometheus-Vision** focuses on **fine-grained, rubric-conditioned evaluation**, emphasizing transparency and interpretability.
* Paper: [Prometheus-Vision: Vision-Language Model as a Judge for Fine-Grained Evaluation](https://arxiv.org/abs/2401.06591) by Lee et al. (2024)
* Code and models: [Prometheus-Vision GitHub](https://github.com/kaistAI/prometheus-vision)

#### Core Idea

* Instead of coarse criteria (helpfulness, relevance), Prometheus-Vision evaluates responses using **custom, instance-specific rubrics**, each with explicit score descriptions.
* Each instance includes:

  + Image
  + Instruction
  + Response to evaluate
  + Customized score rubric
  + Reference answer
  + Output: feedback + score
* This enables **rubric-conditioned judgment**, analogous to trained human graders.
* The following figure ([source](https://arxiv.org/abs/2401.06591)) illustrates the fact that previous automatic metrics could not capture whether a VLM’s response is aware of aesthetic harmony. With Prometheus-Vision, users could define customized score rubrics that they care about instead of assessing based on coarse-grained criteria such as helpfulness, relevance, accuracy, and comprehensiveness. Each component within the Perception Collection consists of 5 input components: an instruction, a real-world image, a response to evaluate, a customized score rubric, and a reference answer. Based on this, Prometheus-Vision is trained to generate a language feedback and a score decision.

#### Architecture and Training

* Backbone: LLaVA-1.5 (7B / 13B)
* Training objective: sequential generation of

  1. Language feedback (rationale)
  2. Scalar score
* Loss function (autoregressive cross-entropy):

\[\mathcal{L} = - \sum\_{t} \log P(y\_t \mid x)\]

* A fixed delimiter phrase (“So the overall score is”) is used to stabilize decoding.

#### Dataset: Perception Collection

* 15K fine-grained score rubrics
* 5K real-world images
* 150K evaluated responses
* Balanced score distribution (1–5)

#### Empirical Results

* Prometheus-Vision achieves:

  + Pearson correlation up to **0.786** with human evaluators
  + Competitive or superior alignment to GPT-4V on multiple benchmarks
  + High-quality natural language feedback preferred by humans

### Multimodal Judges in Preference Learning

* Both [LLaVA-Critic](https://arxiv.org/abs/2410.02712) and [Prometheus-Vision](https://arxiv.org/abs/2401.06591) are used to generate **reward signals** for multimodal preference learning.
* For example, LLaVA-Critic is used to generate pairwise preferences for **Direct Preference Optimization (DPO)**:

\[\mathcal{L}\_{\text{DPO}} = - \mathbb{E} \left[ \log \sigma\left(\beta (r(y^+) - r(y^-))\right) \right]\]

* This enables **RLAIF-style alignment** for multimodal models, reducing reliance on costly human annotations.

### When to Use Multimodal Judges

* Multimodal LLMs-as-Judges are essential when:

  + Evaluation depends on visual grounding
  + Hallucinations must be detected against images
  + Fine-grained visual attributes matter
  + Preference learning is multimodal
  + End-to-end vision–language behavior is evaluated
* They are less necessary when:

  + Tasks are purely textual
  + Visual inputs can be deterministically verified
  + Latency budgets are extremely tight

## Reinforcement Learning for LLMs-as-Judges

* A recent and important evolution of LLM-as-a-Judge systems is the use of **RL to explicitly train judge models to reason before making evaluation decisions**. Prior generations of judges relied primarily on prompting or offline optimization to elicit reasoning, but **the reasoning process itself was never a first-class optimization target**. In contrast, J1 treats reasoning as a *policy* that can be directly improved through interaction with a reward signal, as formalized in [J1: Incentivizing Thinking in LLM-as-a-Judge via Reinforcement Learning](https://arxiv.org/abs/2505.10320) by Whitehouse et al. (2025).
* Rather than relying solely on prompting, Supervised Fine-Tuning (SFT), or preference optimization methods such as DPO, **RL-based judge training directly optimizes the quality of judgment reasoning itself**. Concretely, J1 optimizes not only whether a judge selects the correct response, but also whether it learns to **systematically analyze, verify, and compare responses through explicit chain-of-thought reasoning**. This is evidenced by qualitative traces in the paper, where the judge learns to generate reference answers, identify errors, and revise its own intermediate conclusions.
* RL therefore represents a **foundational shift** in how LLM-as-a-Judge systems are built. Instead of static evaluators whose reasoning behavior is frozen after training, RL produces **trained reasoning agents** whose evaluation strategies improve over time through interaction with verifiable feedback. In J1, this shift enables judges to internalize robust evaluation behaviors such as **dynamic criteria generation, self-correction, and error localization**, even though no human-written reasoning traces are ever provided.
* This section focuses on **J1**, which represents the **most comprehensive and rigorous RL framework for training thinking LLM judges to date**. J1 unifies synthetic data generation, verifiable reward design, and online RL (via GRPO) into a single framework capable of training **generalist judges** across reasoning, writing, instruction following, and safety domains.

### Motivation: Why RL for Judges?

* Earlier LLM-as-a-Judge systems relied primarily on:

  + Zero-shot or few-shot prompting (e.g., MT-Bench-style judges)
  + SFT on judgment examples or critiques
  + Preference-based optimization such as DPO on judgment pairs
* While effective to some extent, these approaches suffer from two core limitations that J1 explicitly targets:

  1. **Reasoning is implicit and uncontrolled**
     Judges may generate chain-of-thought reasoning when prompted, but this reasoning is **not directly optimized for correctness, robustness, or consistency**. As a result, prior judges often exhibit brittle behaviors, such as confidently justifying incorrect verdicts or relying on superficial cues. The J1 paper shows that prompting alone cannot reliably induce behaviors like reference-answer generation or iterative self-correction, whereas RL can.
  2. **Non-verifiable evaluation tasks dominate real-world judging**
     Many critical judgment tasks—such as helpfulness, writing quality, and instruction adherence—**lack ground-truth labels**, making supervised learning ill-posed. This limitation forces prior work to rely on noisy human labels or heuristic reward models, which are expensive and difficult to scale.

> The key insight behind J1 is that **judgment quality can be optimized if evaluation tasks are reformulated to produce verifiable reward signals**, even when the original task is subjective. By converting both verifiable (e.g., math correctness) and non-verifiable (e.g., WildChat writing quality) judgments into **synthetic preference prediction problems**, J1 enables the use of RL with **deterministic, rule-based rewards**. This reformulation is what makes online RL feasible and stable for judge training.

* The following figure ([source](https://arxiv.org/abs/2505.10320)) illustrates the thinking patterns of pairwise and pointwise J1 models during RL training. J1 learns to outline evaluation criteria, generate reference answers, re-evaluate correctness, and compare between responses. Pairwise setup outputs a final verdict indicating the better response, pointwise generates a real-valued score, with a higher score for the better response.

### Core Idea: Thinking-LLM-as-a-Judge via RL

* J1 reframes LLM-as-a-Judge as a **reasoning-first policy optimization problem**, where the judge is explicitly trained to *think before judging*. Rather than treating reasoning as an auxiliary artifact, J1 makes it a **central component of the learned policy**.
* Instead of directly predicting a score or preference, the judge is trained to:

  1. **Generate explicit chain-of-thought reasoning**, including evaluation criteria and intermediate checks
  2. **Arrive at a final verdict or score** based on this reasoning
  3. **Receive a reward based on judgment correctness and consistency**, which backpropagates through the entire reasoning trajectory
* Formally, the judge samples an output from a policy \(\pi\_\theta\):

  \[(t, y) \sim \pi\_\theta(\cdot \mid x, a)\]

  where:

  + \(x\) is the evaluation prompt or instruction
  + \(a\) is one or more candidate responses (e.g., a single response for pointwise judging or a pair \((a,b)\) for pairwise judging)
  + \(t\) is the generated **reasoning trace** (thought tokens)
  + \(y\) is the final **score or judgment/verdict** (e.g., preferred response or scalar score)
* RL is used to optimize \(\pi\_\theta\) such that **both the reasoning process \(t\) and the final judgment \(y\) improve over time**. Crucially, the reward is computed **only from verifiable signals**—such as whether the correct response was chosen under both orderings—yet the optimization pressure shapes the *entire reasoning trajectory*. This explains why J1 learns behaviors like reference-answer generation and iterative self-correction without ever being explicitly instructed to do so.

### Unified Verifiable Training via Synthetic Data

* A central challenge in training and evaluating judges for large language models (LLMs) is that many real-world evaluation tasks are **non-verifiable** — meaning there is no canonical ground-truth label against which to measure correctness. For example, asking whether an assistant’s creative essay is “good enough” or whether a conversational reply is “polite and helpful” does not admit a single correct answer. Traditional evaluation strategies either require expensive human annotations or rely on heuristic scoring, both of which struggle to scale across tasks with subjective components.
* **J1 addresses this by converting *both verifiable and non-verifiable evaluation tasks into a unified, verifiable format*** that can be directly optimized. The key idea is to reframe evaluation as a **preference judgment** over pairs of responses where one response is designated as better than the other. This turns every judgment into a **verifiable binary decision problem**, allowing RL and other optimization techniques to be applied uniformly.
* This transformation is achieved through **synthetic preference pair generation**, building on prior work such as [Self-Taught Evaluators](https://arxiv.org/abs/2408.02666) by Wang et al. (2024), and [Learning to Plan & Reason for Evaluation with Thinking-LLM-as-a-Judge](https://arxiv.org/abs/2501.18099) by Saha et al. (2025).
* In the J1 framework, training examples consist of triplets \((x, a, b)\) where:

  + \(x\) is an instruction or task prompt,
  + \(a\) and \(b\) are candidate responses produced either by the model being evaluated or by auxiliary generation processes,
  + and a **synthetic preference label** indicates which of the two should be considered better.
* **Verifiable tasks (e.g., math and reasoning)** can be converted by defining the preferred response in terms of objective correctness. For instance, on mathematical reasoning subsets like **MATH**, the model designates the output that **arrives at the correct numeric answer** as preferred, and any output with an arithmetic or logical error as inferior. If an instruction is *“Compute the sum of all two-element subsets of \(\{1,2,3,4,5,6\}\),”* the correct response computes 105 by enumerating pairs and summing them; the less preferred response might mistakenly omit one element category, leading to an incorrect sum. This synthetic comparison renders the preference verifiable even though the underlying task originally lacked an explicit “better” metric.
* **Non-verifiable tasks (e.g., open-ended dialogue)** are converted by *controlled perturbations* of a high-quality response to produce a degraded alternative. For example, taking an original high-quality assistant reply from the **WildChat** dataset of real ChatGPT interactions (primarily English conversational data), one can introduce noise into the instruction (e.g., adding conflicting constraints, irrelevant or malformed instructions, or stylistic distortions, etc.) and then generate a corresponding response. The original reply is labeled as preferred, and the noisy reply as inferior, yielding a **synthetic but atomically verifiable preference** because one response is systematically worse by construction.
* After this transformation, *both* task types share the same training objective:

  + Preference pairs \((a,b)\) are generated synthetically,
  + **Exactly one response is designated as preferred**, and
  + The judge’s task becomes **predicting the better response**, a **fully verifiable objective**.
* With this reformulation, J1 eliminates the need for multiple domain-specific scoring methods. Instead of defining bespoke measures of quality for writing, safety, reasoning, and instruction following, everything is reduced to **binary verifiable judgments**, ultimately rendering a **single generalist judge model** trained across diverse tasks. This approach enables RL to be applied **uniformly and scalably** across domains that span QA, reasoning, open-end writing, safety classification, and fine-grained instruction adherence, all with **verifiable supervision signals** systematically derived from synthetic data.
* The following figure ([source](https://arxiv.org/abs/2505.10320)) illustrates the reinforcement learning recipes for training J1 models. We generate synthetic preference pairs for both verifiable and non-verifiable tasks to create position-agnostic training batches. Rewards based on [verdict correctness](#verdict-correctness-reward), [consistency](#consistency-reward-mitigating-positional-bias), and score alignment jointly optimize evaluation thoughts and verdicts using online GRPO. Pointwise-J1 is trained only via distant supervision from pairwise labels. MultiTask-J1 combines pairwise and pointwise formulation.

### Reward Design: Optimizing Judgment Quality

* In J1’s RL framework, **reward design is central** to teaching the judge model to produce accurate and consistent verdicts on synthetic preference pairs. Rather than training a separate, learned reward model (as in classic RL from human feedback), J1 uses **rule-based, verifiable reward signals** that depend only on whether the judge correctly identifies the preferred response. This makes the supervision signal **explicit, stable, and cheaply computable** across all synthetic data.

#### Verdict Correctness Reward

* The **primary reward component** in J1 is the *verdict correctness* reward, which checks whether the model’s final verdict aligns with the known preferred response in a synthetic pair. For a given preference pair \((x,a,b)\), suppose the model produces verdict \(\hat{y}\) indicating whether \(a\) or \(b\) is better. The verdict correctness reward is defined as

  \[r\_{\text{correct}}(\hat{y}, y^\*) =
  \begin{cases}
  1 & \text{if }\hat{y}=y^\*,\\
  0 & \text{otherwise}
  \end{cases}\]
  + where \(y^\*\) is the ground-truth synthetic preference label that designates which response is superior. This simple **binary reward encourages the judge to match the constructed preference** and is directly verifiable from the synthetic construction.
* For example, if \((x,a,b)\) comes from the **MATH** subset of synthetic data where \(a\) correctly solves a math problem and \(b\) fails, the \(r\_{\text{correct}}\) reward is 1 only if the judge correctly picks \(a\) as preferred. Similarly for **WildChat** pairs, choosing the non-noisy (higher quality) response over the noisy one yields the correctness reward.

#### Consistency Reward (Mitigating Positional Bias)

* A major challenge in pairwise judging is **positional bias**: LLM judges often prefer whichever response appears in a certain position, regardless of content. This phenomenon was identified by Peiyi Wang et al. in the paper [Large Language Models are not Fair Evaluators](https://aclanthology.org/2024.acl-long.511/) by Wang et al. (2024), which shows that simply swapping the order of candidate responses significantly alters evaluation outcomes.
* To combat this, J1 introduces a **consistency reward** that *explicitly rewards the judge for making the same correct decision regardless of candidate order*. For each preference pair, the training batch includes **both orderings** of the same pair — \((x,a,b)\) and \((x,b,a)\) — making the judge process them jointly. The consistency reward is then:

  \[r\_{\text{consistency}} =
  \begin{cases}
  1 & \text{if }\hat{y}\_{a\succ b}=y^\* \text{ and }\hat{y}\_{b\succ a}=y^\*,\\
  0 & \text{otherwise}
  \end{cases}\]
  + where \(\hat{y}\_{a\succ b}\) and \(\hat{y}\_{b\succ a}\) denote the judge’s predicted verdicts when the response order is \((a,b)\) and \((b,a)\), respectively. Only when the judge is correct in both positions does it receive the consistency reward, explicitly **penalizing positional bias** which would otherwise exploit order cues.
* In practice, this reward encourages the model to treat semantic content — not order positions — as the basis for judgment. For example, if a judge picks \(a\) over \(b\) when presented as \((a,b)\) but erroneously picks \(b\) over \(a\) when presented as \((b,a)\), then \(r\_{\text{consistency}}\) is 0, notwithstanding the correctness of one ordering. This forces consistent evaluation behavior across placements.

#### Extended Reward Components

* In the J1 training experiments, extensions to the core reward design were explored to further refine the judgment process. For example, **format-based rewards** were tested to enforce structural conventions such as explicit thinking tags (e.g., requiring the judge to use a “” section), but these were found to have \*minimal impact\* on judgment quality compared to the fundamental correctness and consistency rewards.
* Additionally, some variants of J1 adopt a **score-based formulation**, where the judge generates real-valued scores \(s\_a\) and \(s\_b\) for responses \(a\) and \(b\), respectively, and the verdict is derived by comparing them:

\[\hat{y}=\begin{cases}
a & \text{if } s\_a > s\_b,\\
b & \text{otherwise}
\end{cases}\]

* In these cases, the same correctness and consistency criteria are adapted to check whether the score ordering aligns with the synthetic preference label.

#### Putting It Together: Joint Optimization

* With these reward components, the judge’s **policy** \(\pi\_\theta\) (parameterized by model parameters \(\theta\)) is optimized via RL to maximize expected reward over synthetic pairs:

\[\max\_\theta \mathbb{E}\_{(x,a,b)\sim \mathcal{D}}\bigl[r\_{\text{correct}}+r\_{\text{consistency}}\bigr]\]

* where \(\mathcal{D}\) is the distribution of synthetic preference pairs. This joint objective encourages the model not only to pick the correct preferred response, but to do so *consistently across varying input orderings*, thus directly addressing fundamental deficiencies documented in prior work.

### Reasoning-Optimized Training via Reinforcement Learning

* Beyond converting evaluation into a verifiable prediction problem and defining robust rewards, **J1 explicitly optimizes the *reasoning process* of the judge**. The core hypothesis is that high-quality judgments require not only correct final decisions but also **structured, deliberate chain-of-thought reasoning**. This design choice aligns with recent findings that reasoning quality can be substantially improved when RL directly targets intermediate thought processes rather than only final outputs.
* To achieve this, J1 adopts **Group Relative Policy Optimization (GRPO)** as its RL algorithm, following the approach introduced in [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://arxiv.org/abs/2402.03300) by Zhihong Shao et al. (2024), and later popularized in large-scale reasoning models such as [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948) by Daya Guo et al. (2025).
* A detailed discourse on GRPO is available in our [Policy Optimization](../preference-optimization/#group-relative-policy-optimization-grpo-1) primer.

#### Group Relative Policy Optimization (GRPO)-based Optimization

* In J1, the judge model defines a policy \(\pi\_\theta\) that generates a sequence of **thought tokens** \(t\) followed by a **final judgment** \(y\), conditioned on an input \((x,a,b)\) and a reasoning-eliciting seed prompt. The full output is thus:

\[(t, y) \sim \pi\_\theta(\cdot \mid x, a, b)\]

* GRPO optimizes this policy by comparing multiple sampled trajectories for the same input and computing **relative advantages** using **group normalization within the batch of sampled rollouts**. Concretely, for a batch of \(K\) sampled outputs \({(t\_k, y\_k)}\_{k=1}^K\) generated for the same input, each trajectory receives a reward \(r\_k\) (e.g., from verdict correctness and consistency). The **group-relative advantage** is computed by normalizing rewards **within the rollout group**:

  \[\mu = \frac{1}{K}\sum\_{j=1}^{K} r\_j,
  \qquad
  \sigma = \sqrt{\frac{1}{K}\sum\_{j=1}^{K}(r\_j - \mu)^2 + \epsilon}\]
  \[A\_k = \frac{r\_k - \mu}{\sigma}\]
  + where, \(\mu\) and \(\sigma\) denote the **group mean and standard deviation of rewards computed over the batch of sampled rollouts**, and \(\epsilon\) is a small constant added for numerical stability. This **group normalization step** ensures that policy updates depend on **relative performance among rollouts for the same input**, rather than absolute reward scale, reducing gradient variance and stabilizing training across tasks with heterogeneous reward distributions.
* By operating on **mean–variance–normalized intra-group advantages**, GRPO encourages the judge to prefer **reasoning trajectories that outperform their peers within the same rollout group**, aligning naturally with the comparative structure of judgment tasks and enabling robust RL without a learned value model.
* The GRPO loss used to update the judge policy is then:

\[\mathcal{L}\_{\text{GRPO}}(\theta)
= -\mathbb{E}\_{k}\bigl[ A\_k \log \pi\_\theta(t\_k, y\_k \mid x,a,b) \bigr]\]

* This formulation encourages the model to **increase the probability of reasoning trajectories that outperform their peers**, while suppressing weaker or inconsistent reasoning paths. Importantly, this does not require a learned critic or value function, making GRPO **stable and well-suited to synthetic supervision**.

#### Why GRPO Is Well-Matched to J1

* J1’s training setup naturally produces **multiple reasoning trajectories per prompt**, since the same preference pair can be evaluated under different response orderings and with multiple stochastic generations. GRPO exploits this structure by:

  + emphasizing **relative quality of reasoning**, not absolute reward magnitude,
  + reducing variance compared to vanilla policy-gradient methods, and
  + directly aligning optimization with the *ranking nature* of preference judgments.
* This design mirrors the reasoning-first philosophy adopted in DeepSeek-R1, where RL is used to incentivize models to “think longer” and self-correct. However, J1 differs in a crucial way: instead of optimizing task-level correctness (e.g., solving math problems), it optimizes **evaluation correctness**, teaching the model *how to judge* rather than *how to solve*.

#### Seed Prompts and Thought Structure

* To ensure that GRPO optimizes meaningful reasoning rather than degenerate shortcuts, J1 conditions the judge on a **seed thinking prompt** that explicitly instructs the model to:

  + outline evaluation criteria,
  + optionally generate a reference answer,
  + compare candidate responses step-by-step,
  + and only then emit a final verdict.
* This approach is inspired by structured evaluation prompts introduced in [Learning to Plan & Reason for Evaluation with Thinking-LLM-as-a-Judge](https://openreview.net/forum?id=PNRznmmWP7) by Saha et al. (2025), but J1 extends it by **reinforcement-learning the reasoning itself**, rather than merely prompting it.

#### Empirical Effect on Reasoning Quality

* Qualitative analyses in the J1 paper show that, under GRPO training, judges learn to adopt **systematic evaluation strategies**, including:

  + self-generation of reference solutions for verifiable tasks,
  + explicit error localization in incorrect responses,
  + dynamic criteria generation for non-verifiable writing prompts, and
  + iterative self-correction when initial assessments conflict with evidence.
* These behaviors emerge *without any human-written reasoning supervision*, relying entirely on synthetic preference pairs and verifiable reward signals, demonstrating that **reasoning-optimized RL can be successfully applied to evaluation models**, not just task-solving models.

### J1 Formulations: Pairwise, Pointwise, and Multitask Judges

* Building on unified verifiable training and reasoning-optimized RL, **J1 introduces multiple judge formulations** that differ in how inputs are structured, what outputs are produced, and how rewards are computed. These formulations are designed to explore trade-offs between **comparative context**, **positional bias**, and **training efficiency**, while remaining within the same verifiable RL framework.

#### Pairwise J1 with Verdict (PaV)

* The **pairwise verdict formulation** is the most direct instantiation of LLM-as-a-Judge. Given an instruction \(x\) and two candidate responses \(a\) and \(b\), the judge produces a chain-of-thought \(t\) followed by a **binary verdict** \(y \in {a,b}\):

\[(t, y) \sim \pi\_\theta(\cdot \mid x, a, b)\]

* This formulation closely mirrors classical preference learning setups and is aligned with earlier LLM-judge approaches such as [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685) by Zheng et al. (2023). However, unlike prompting-based judges, PaV is **trained with RL** and explicit verifiable rewards.
* The reward for PaV combines verdict correctness and consistency:

\[r\_{\text{PaV}} = r\_{\text{correct}} + r\_{\text{consistency}}\]

* Empirically, PaV benefits from **direct comparative context**, enabling the judge to reason about relative strengths and weaknesses between responses. However, without additional mechanisms, pairwise judgments are susceptible to **positional bias**, motivating further extensions.

#### Pairwise J1 with Scores (PaS)

* To expose richer evaluation signals, J1 introduces a **score-based pairwise formulation**, where the judge outputs **real-valued scores** \(s\_a\) and \(s\_b\) instead of an explicit verdict:

\[(t, s\_a, s\_b) \sim \pi\_\theta(\cdot \mid x, a, b)\]

* The final verdict is derived deterministically:

\[\hat{y} =
\begin{cases}
a & \text{if } s\_a > s\_b, \\
b & \text{otherwise}
\end{cases}\]

* The reward checks whether the **score ordering matches the synthetic preference label**:

  \[r\_{\text{PaS}} =
  \mathbb{1}[ (s\_a - s\_b)(y^\*\_a - y^\*\_b) > 0 ]\]
  + where:
    - \(y\) is the **model-predicted verdict** induced by the score difference \(s\_a - s\_b\)
    - \(y^\*\) encodes the **ground-truth synthetic preference direction** as a signed pair
    - \(y^\*\_a = 1, y^\*\_b = -1\) if \(a \succ b\),
    - \(y^\*\_a = -1, y^\*\_b = 1\) otherwise.
* This formulation is inspired by generative reward modeling approaches such as [Generative Reward Models](https://arxiv.org/abs/2410.12832) by Mahan et al. (2024), but differs in that **scores are generated by the language model head itself**, allowing reasoning and scoring to be jointly optimized.
* Note that a **consistency reward is not explicitly added to \(r\_{\text{PaS}}\)**, but PaS **implicitly supports consistency** when trained with swapped-order rollouts, since order invariance is encouraged implicitly through the continuous score difference \(s\_a - s\_b\).

#### Pairwise J1 with Scores and Verdict (PaVS)

* J1 further introduces a **hybrid formulation** that outputs both intermediate scores and a final verdict:

\[(t, s\_a, s\_b, y) \sim \pi\_\theta(\cdot \mid x, a, b)\]

* In this setup, the **verdict alone determines the reward**, while scores act as **latent reasoning aids** rather than supervised targets:

\[r\_{\text{PaVS}} = r\_{\text{correct}} + r\_{\text{consistency}}\]

* This design allows the model to internally reason with graded assessments while remaining grounded in a verifiable binary objective, bridging the gap between discrete judgments and continuous evaluations.

#### Pointwise J1 with Scores (PoS)

* To directly address positional bias, J1 introduces a **pointwise judge formulation**, where the model evaluates a **single response in isolation**:

  \[(t, s) \sim \pi\_\theta(\cdot \mid x, a)\]
  + … with \(s \in [0,10]\) representing the quality of response \(a\).
* Pointwise judges are **inherently position-consistent**, since each response is scored independently. However, they lack explicit comparative context. J1 overcomes this limitation by training PoS models via **distant supervision from pairwise data**. Given a preference pair \((a,b)\) with \(a \succ b\), the reward is:

\[r\_{\text{PoS}} = \mathbb{1}[ s\_a > s\_b ]\]

* This approach is novel in that it trains a pointwise judge **without any human-annotated absolute scores**, relying solely on synthetic pairwise preferences, extending ideas from [Self-Rationalization Improves LLM as a Fine-grained Judge](https://arxiv.org/abs/2410.05495) by Trivedi et al. (2024) and [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) by Ouyang et al. (2022).

#### Multitask Pairwise & Pointwise J1 (MT)

* Finally, J1 unifies pairwise and pointwise paradigms into a **single multitask judge**, trained jointly on two complementary types of supervision derived from the **same synthetic preference pairs**:

  + **pairwise score-based or verdict-based samples**, where the judge compares two responses \((a,b)\) to the same instruction \(x\), and
  + **pointwise scoring samples**, where each response is evaluated independently but supervised indirectly via the pairwise preference signal.
* In contrast to prior work that trains separate judges or requires human-labeled absolute scores, J1 trains both paradigms **within a single policy** \(\pi\_\theta\), sharing parameters, reasoning prompts, and RL dynamics. This enables **transfer of evaluation strategies** between comparative and absolute judgment modes.

##### Multitask Objective and Full Loss Function

* Let \(\mathcal{D}\_{\text{pair}}\) denote the distribution of pairwise judgment episodes and \(\mathcal{D}\_{\text{point}}\) the induced pointwise episodes constructed from the same preference pairs. For both cases, J1 applies **Group Relative Policy Optimization (GRPO)**, sampling \(K\) reasoning trajectories per input.
* For a **pairwise episode**, the model generates thought tokens \(t\) and a verdict (or scores), receiving rewards based on **verdict correctness and positional consistency**. The **mean–variance normalized group-relative advantage** is computed as:

  \[A\_k^{\text{pair}}
  =\frac{
  r\_k^{\text{pair}}
  -\mu^{\text{pair}}
  }{
  \sigma^{\text{pair}} + \epsilon
  },
  \quad
  \mu^{\text{pair}} = \frac{1}{K}\sum\_{j=1}^{K} r\_j^{\text{pair}},
  \quad
  \sigma^{\text{pair}} = \sqrt{\frac{1}{K}\sum\_{j=1}^{K}(r\_j^{\text{pair}}-\mu^{\text{pair}})^2}\]
  + The corresponding GRPO pairwise loss is:\[\mathcal{L}\_{\text{pairwise}}
  =-\mathbb{E}\_{(x,a,b)\sim\mathcal{D}\_{\text{pair}}}
  \mathbb{E}\_{k}
  \bigl[
  A\_k^{\text{pair}}
  \log
  \pi\_\theta(t\_k, y\_k \mid x,a,b)
  \bigr]\]
* For a **pointwise episode**, each response \(a\) is scored independently, but rewards are computed **jointly across the original preference pair**. Given a synthetic preference \(a \succ b\), the reward is:

  \[r^{\text{point}} = \mathbb{1}[ s\_a > s\_b ].\]
  + Using the **same mean–variance normalized GRPO advantage formulation defined earlier**, the pointwise loss is:\[\mathcal{L}\_{\text{pointwise}}
  =
  -\mathbb{E}\_{(x,a)\sim\mathcal{D}\_{\text{point}}}
  \mathbb{E}\_{k}
  \bigl[
  A\_k^{\text{point}}
  \log
  \pi\_\theta(t\_k, s\_k \mid x,a)
  \bigr]\]

##### Full Multitask Loss

* The **full multitask objective** used in J1 is the sum of the two GRPO losses:

\[\boxed{
\mathcal{L}\_{\text{MT}}
=\mathcal{L}\_{\text{pairwise}}
+\mathcal{L}\_{\text{pointwise}}
}\]

* As in the original J1 formulation, **no explicit weighting parameter \(\lambda\) is introduced**. Instead, pairwise and pointwise updates are interleaved during training, with **shared normalization ensuring comparable gradient scales across tasks**.

##### Why Multitask Training Is Effective

* Empirically, the multitask judge achieves **higher position-consistent accuracy** and **lower verdict-flip or tie rates** than either pairwise-only or pointwise-only formulations.
* This reflects a complementary synergy:

  + **pairwise training offers comparative grounding**, while
  + **pointwise training enforces positional robustness**, and
  + **shared normalized advantages prevent either objective from dominating optimization**.
* By optimizing \(\mathcal{L}\_{\text{MT}}\), J1 directly addresses long-standing evaluation failure modes identified in
  [Large Language Models Are Not Fair Evaluators](https://aclanthology.org/2024.acl-long.511/) by Wang et al. (2024), showing that **comparative reasoning and positional consistency can be jointly achieved within a single judge**.

### Synthetic Data Generation for Verifiable Judging

* The effectiveness of J1 critically depends on its ability to generate **high-quality synthetic preference pairs** that transform diverse evaluation tasks into **verifiable supervision signals**. Rather than relying on costly human annotations, J1 constructs a unified synthetic dataset that supports RL across both objective and subjective domains.
* J1’s synthetic data pipeline builds directly on the strategy introduced in [Self-Taught Evaluators](https://arxiv.org/abs/2408.02666) by Wang et al. (2024), and reused in [Learning to Plan & Reason for Evaluation with Thinking-LLM-as-a-Judge](https://openreview.net/forum?id=PNRznmmWP7) by Saha et al. (2025), enabling **controlled comparisons** between offline preference optimization and online RL on the *same data distribution*.

#### Dataset Composition

* The final J1 training dataset consists of approximately **22K synthetic preference pairs**, drawn from two complementary sources:

  + **WildChat prompts** (≈17K samples), derived from [WildChat: 1M ChatGPT Interaction Logs in the Wild](https://openreview.net/forum?id=Bl8u7ZRlbM) by Zhao et al. (2024), representing *non-verifiable*, open-ended user interactions such as dialogue, writing, and instruction following.
  + **MATH prompts** (≈5K samples), taken from [Measuring Mathematical Problem Solving With the MATH Dataset](https://openreview.net/forum?id=7Bywt2mQsCe) by Hendrycks et al. (2021), representing *verifiable* reasoning tasks with exact ground-truth answers.
* Each data point ultimately yields a **preference-labeled tuple**:

  \[(x, a, b, y^\*)\]
  + where \(y^\* \in \{a \succ b, b \succ a\}\) is known by construction.

#### Synthetic Preference Generation for Verifiable Tasks (MATH)

* For **verifiable reasoning tasks**, synthetic preferences are generated by exploiting objective correctness. Given a prompt \(x\) from the MATH dataset, an LLM generates multiple candidate solutions. A reference answer \(z^\*\) is either known (from the dataset) or independently verified.
* A response \(a\) is labeled preferred over \(b\) if:

\[\mathbb{1}[a \text{ reaches } z^\*] = 1
\quad\text{and}\quad
\mathbb{1}[b \text{ reaches } z^\*] = 0\]

* For example, if \(x\) asks for the sum of all two-element subsets of \({1,2,3,4,5,6}\), then a response that correctly derives:

  \[\binom{6}{2} = 15,\quad \text{sum} = 5 \times (1+2+3+4+5+6) = 105\]
  + … is labeled preferred, while a response that makes an arithmetic aggregation error is labeled rejected. This yields a **clean, verifiable preference pair** without human intervention.

#### Synthetic Preference Generation for Non-Verifiable Tasks (WildChat)

* For **non-verifiable prompts**, where no canonical answer exists, J1 employs **controlled instruction degradation** to construct preferences. Starting from an original prompt \(x\) and a high-quality response \(a\), a *noisy variant* of the instruction \(\tilde{x}\) is generated by introducing perturbations such as:

  + conflicting constraints,
  + irrelevant or malformed instructions,
  + or stylistic distortions.
* An LLM then produces a response \(b\) to \(\tilde{x}\). The preference label is assigned as:

  \[a \succ b\]
  + … since \(b\) is systematically degraded by construction. This method ensures that **preference correctness is guaranteed**, even though the task itself lacks an objective ground truth.
* This approach follows the same philosophy as prior synthetic evaluation pipelines, but J1 uses it explicitly to enable **verifiable RL**, rather than only offline preference optimization.

#### Position-Agnostic Pair Construction

* To support bias-aware training, every preference pair is **duplicated with reversed orderings**:

\[(x, a, b, y^\*) \quad \text{and} \quad (x, b, a, y^\*)\]

* These paired samples are placed in the **same training batch**, enabling the computation of consistency rewards during RL. This batching strategy is essential for addressing positional bias, as documented in [Large Language Models are not Fair Evaluators](https://aclanthology.org/2024.acl-long.511/) by Wang et al. (2024).

#### Why Synthetic Data Works for J1

* Although synthetic, this dataset has several crucial properties:

  + **Verifiability**: every preference label is correct by construction.
  + **Diversity**: WildChat and MATH jointly cover reasoning, dialogue, writing, safety, and instruction following.
  + **Scalability**: data generation is cheap and extensible to new domains.
  + **Compatibility with RL**: rewards can be computed deterministically without learned reward models.
* As demonstrated empirically in the J1 paper, training on only **22K synthetic pairs** is sufficient to outperform judges trained on **hundreds of thousands or millions of human-labeled samples**, validating the effectiveness of **synthetic-first evaluation learning**.

### Learned Reasoning Behaviors

* A central empirical finding of **J1** is that **RL with verifiable rewards induces rich, systematic reasoning behaviors in LLM judges**, even though **no human-written rationales or chain-of-thought annotations are provided at any stage**. All reasoning emerges purely from RL optimization over synthetic preference pairs.
* Qualitative analysis of thinking traces from [J1: Incentivizing Thinking in LLM-as-a-Judge via Reinforcement Learning](https://arxiv.org/abs/2505.10320) by Whitehouse et al. (2025) reveals that RL-trained judges consistently adopt **structured evaluation strategies**, including:

  + **Dynamic generation of evaluation criteria**:

    - Judges infer task-specific criteria directly from the instruction \(x\), such as correctness, faithfulness, adherence to constraints, output format, clarity, or safety. These criteria are **generated on the fly** rather than hard-coded, reflecting flexible evaluation behavior also emphasized in [Learning to Plan & Reason for Evaluation with Thinking-LLM-as-a-Judge](https://openreview.net/forum?id=PNRznmmWP7) by Saha et al. (2025).
  + **Self-generated reference answers**:

    - For verifiable tasks, J1 judges frequently compute an internal reference solution \(z^\*\) before evaluating candidate responses. For example, when judging a combinatorics problem, the model derives:\[\binom{6}{2} = 15,\quad \text{total sum} = 5 \times \sum\_{i=1}^6 i = 105\]
    - … and then compares each assistant’s reasoning against this reference, as illustrated in the math traces.
  + **Iterative self-correction**:

    - Judges often revise initial assessments after deeper inspection. A response that appears plausible at first may be downgraded after detecting a subtle logical or arithmetic inconsistency. This mirrors behaviors observed in reasoning-optimized models such as [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948) by Guo et al. (2025), but here applied specifically to *evaluation* rather than *problem solving*.
  + **Explicit error localization and feedback**:

    - When rejecting a response, J1 frequently pinpoints the precise failure mode (e.g., an incorrect simplification step or a violated instruction constraint) and explains why it leads to an inferior outcome. This behavior is visible in both verifiable math examples and non-verifiable writing evaluations.
* Crucially, these reasoning patterns emerge **without human-written thinking traces**. The only supervision comes from **verifiable rewards on the final judgment**, demonstrating that **optimizing evaluation correctness via RL implicitly induces high-quality reasoning processes**.

### Empirical Performance

* J1 achieves **state-of-the-art results across major judge and reward-model benchmarks**, spanning both verifiable and non-verifiable evaluation tasks. These benchmarks collectively assess preference accuracy, positional robustness, and alignment with human judgments.

#### PPE (Preference Proxy Evaluations)

* **PPE** was proposed in [PPE: Preference Proxy Evaluations](https://github.com/lmarena/PPE) by Chiang et al. (2024).
* PPE is a large-scale benchmark for evaluating reward models and LLM judges using **proxy preference signals** that correlate strongly with human judgments and downstream RLHF performance. It is widely used to assess **preference modeling quality and judge reliability at scale**.
* On **PPE Correctness**, J1 shows substantial improvements over both baseline LLM judges and specialized reward models. In particular:

  + **J1-Qwen-32B-MultiTask** achieves an overall accuracy of **76.8**, outperforming models trained on far larger datasets.
  + Gains are consistent across sub-benchmarks such as **MMLU-Pro**, **MATH**, **GPQA**, **MBPP-Plus**, and **IFEval**.

#### RewardBench

* **RewardBench** was introduced in [RewardBench: Evaluating Reward Models for Language Modeling](https://arxiv.org/abs/2403.08555) by Lambert et al. (2024).
* It is a comprehensive benchmark designed to evaluate reward models and LLM-as-a-Judge systems across a wide range of tasks, including **instruction following, safety, reasoning, and preference alignment**, measuring how well reward signals reflect human preferences.
* J1 establishes a new state of the art on RewardBench:

  + **J1-Qwen-32B-MultiTask** achieves an overall score of **93.6**, outperforming prior generative reward models such as EvalPlanner and DeepSeek-GRM, despite being trained on far less data.

#### JudgeBench

* **JudgeBench** was proposed in [JudgeBench: A Benchmark for Evaluating LLM-based Judges](https://arxiv.org/abs/2410.12784) by Tan et al. (2025).
* JudgeBench is specifically designed to evaluate **LLM-based judges** on difficult pairwise and pointwise judgment scenarios where traditional automatic metrics fail. It includes tasks across **reasoning, knowledge, math, and coding**.
* On JudgeBench, J1 demonstrates:

  + **Higher position-consistent accuracy**, meaning correct verdicts under both \((a,b)\) and \((b,a)\) orderings.
  + Substantially fewer verdict flips than standard pairwise judges, validating the effectiveness of J1’s consistency-aware rewards.

#### RM-Bench

* **RM-Bench** was proposed in [RM-Bench: Benchmarking Reward Models of Language Models with Subtlety and Style](https://arxiv.org/abs/2410.16184) by Wang et al. (2024).
* RM-Bench is a reward-model benchmarking suite used to evaluate **scalar reward models, generative reward models, and LLM judges** across preference learning and correctness-based evaluation tasks. It is commonly reported alongside PPE and RewardBench.
* J1 outperforms both scalar reward models trained with Bradley–Terry objectives and generative reward models trained on much larger datasets, demonstrating superior robustness to subtle stylistic and semantic variations.

#### FollowBenchEval

* **FollowBenchEval** was proposed in [FollowBench: A Multi-level Fine-grained Constraints Following Benchmark for Large Language Models](https://arxiv.org/abs/2310.20410) by Jiang et al. (2024).
* This evaluation suite measures how well reward models and LLM judges assess **instruction-following quality**, including consistency, preference accuracy, and positional robustness in pairwise comparisons.
* J1 achieves the strongest reported performance on FollowBenchEval, particularly excelling at identifying subtle instruction violations that simpler reward models often miss.

#### RewardBench v2

* While **J1** reports strong performance across PPE, RewardBench v1, JudgeBench, RM-Bench, and FollowBenchEval, it **does not evaluate on RewardBench v2**, which represents a substantial evolution in reward model and LLM-judge evaluation methodology.
* **RewardBench v2** was proposed in [RewardBench 2: Advancing Reward Model Evaluation](https://arxiv.org/abs/2506.01937) by Malik et al. (2025).

##### Key Differences Between RewardBench v1 and RewardBench v2

* **Unseen human prompts**:

  + Unlike RewardBench v1, which reused prompts from downstream evaluations, RewardBench v2 is built primarily on **new, previously unseen human prompts**, largely sourced from WildChat.
  + This design significantly reduces contamination and benchmark leakage, making correlations with downstream performance more meaningful.
* **Best-of-N (\(N > 2\)) evaluation format**:

  + RewardBench v2 moves from a binary chosen–rejected setup to a **1-chosen vs. 3-rejected** format.
  + This lowers the random baseline from 50% to 25%, increasing headroom and making strong reward models easier to distinguish.
* **Expanded multi-skill coverage**:

  + RewardBench v2 evaluates six domains:

    - Factuality
    - Precise instruction following
    - Math
    - Safety
    - Focus (on-topic quality)
    - Ties (new domain testing calibration among multiple equally correct answers)
  + The **Ties** domain is entirely new and explicitly tests whether reward models avoid arbitrary over-preference among equally valid answers.
* **Accuracy-based evaluation with downstream grounding**:

  + Unlike preference-only benchmarks, RewardBench v2 emphasizes **accuracy-based scoring**, while still demonstrating strong correlation with:

    - Best-of-N inference-time scaling
    - PPO-based RLHF training
  + Models score on average **20+ points lower** than on RewardBench v1, indicating substantially increased difficulty.
* **Stronger empirical linkage to downstream performance**:

  + RewardBench v2 shows:

    - Pearson correlation ≈ 0.87 with Best-of-N downstream task performance
    - Meaningful but saturating correlation with PPO-based RLHF, highlighting that benchmark accuracy is necessary but not sufficient for RL success
  + Crucially, the benchmark reveals **lineage mismatch effects**, where high-scoring reward models can still perform poorly in RLHF if misaligned with the policy model’s base distribution.
* The following figure ([source](https://arxiv.org/abs/2506.01937)) shows RewardBench v2’s benchmark construction and evaluation setup, highlighting its unseen human prompts, best-of-4 format, expanded domains (including Ties), and improved correlation with downstream RL fine-tuning and best-of-N sampling performance.

### Implications for LLM-as-a-Judge Systems

* Although J1’s absence from RewardBench v2 does not invalidate its reported strengths, RewardBench v2 introduces **failure modes and calibration challenges** not covered by earlier benchmarks.
* In particular:

  + The **Ties** domain stresses judge calibration rather than raw preference discrimination.
  + The Best-of-4 setup penalizes overly confident or brittle reward signals.
* As RewardBench v2 gains adoption, it is likely to become a **standard reference benchmark** for next-generation LLM judges and reward models, complementing (and in some cases superseding) RewardBench v1.
* Practically, future evaluations of J1-like systems would benefit from reporting RewardBench v2 results to demonstrate robustness under **harder, more realistic, and less-contaminated evaluation conditions**.

### Relationship to Panels and Multimodal Judges

* RL is complementary to other robustness strategies:

  + **Panels of LLMs-as-Judges**: RL improves each judge’s internal reasoning; panels reduce variance across judges
  + **Pointwise vs. pairwise paradigms**: J1 unifies both within a single multitask model
  + **Test-time scaling**: RL-trained judges benefit strongly from majority voting and averaging
* In practice, the strongest systems combine **RL-trained thinking judges + panel aggregation**.

### Key Takeaways

* **RL enables direct optimization of judgment reasoning**, not just final outputs. By applying RL to the judge’s chain-of-thought, J1 learns *how* to evaluate—developing structured criteria, reference answers, and self-correction behaviors—rather than merely matching preference labels.
* **Synthetic preference data makes RL feasible even for subjective evaluation tasks**. By converting both verifiable and non-verifiable prompts into preference-labeled pairs, J1 extends verifiable training signals to domains such as writing, dialogue, and instruction following.
* **Consistency-based rewards effectively mitigate positional bias**, a long-standing failure mode of LLM judges. Training on both response orderings and rewarding order-invariant correctness leads to more reliable and robust judgments.
* As a result of these design choices, **RL-trained judges substantially outperform both prompted judges and traditional reward models**.
* Concretely, **J1-Qwen-32B outperforms much larger models such as DeepSeek-R1-671B**, despite having fewer parameters and being trained solely on synthetic data.
* J1 also surpasses **both scalar reward models and generative reward models** that are trained on far more data, demonstrating that *how* a judge is trained can matter more than dataset scale alone.
* **Test-time scaling further improves accuracy**, either through self-consistency over multiple verdicts or by averaging score-based judgments:
  \(\hat{y} = \arg\max\_{y} \sum\_{i=1}^{N} \mathbb{1}[y\_i = y].\)
* Collectively, these findings demonstrate that **online RL is a powerful and general mechanism for training high-quality, generalist LLM judges**, enabling robust evaluation across domains that were previously considered incompatible with verifiable supervision.

### From J1 to JudgeLRM

* In addition to J1, **concurrent work has independently arrived at the conclusion that RL is essential for training high-quality LLM judges**, particularly for reasoning-intensive evaluation tasks. A notable example is [JudgeLRM: Large Reasoning Models as a Judge](https://arxiv.org/abs/2504.00050) by Chen et al. (2025), which similarly applies **RL with outcome-driven rewards** to explicitly activate and improve evaluative reasoning in judge models.
* JudgeLRM provides complementary empirical evidence that **SFT alone fails as evaluation tasks become more reasoning-heavy**. The paper demonstrates a **negative correlation between SFT performance gains and the proportion of reasoning-required judgment samples**, showing that static training paradigms struggle precisely where judgment is most cognitively demanding. By contrast, RL-trained JudgeLRM models learn **verification, subgoal decomposition, double-checking, and decision justification behaviors**, closely paralleling the emergent reasoning patterns observed in J1.
* Together, **J1 and JudgeLRM establish a converging research direction**: treating LLM-as-a-Judge not as a passive scorer, but as a **reasoning agent trained via RL**. While J1 emphasizes **synthetic preference construction and consistency-based rewards** for generalist judging across subjective and objective tasks, JudgeLRM adopts a **structural/format reward** and **a multi-component content reward** (with a relation reward, absolute reward, and confidence reward) for pairwise scoring. Despite these design differences, both works arrive at the same core conclusion—**judgment is inherently a reasoning-intensive task, and RL is the correct mechanism for training robust, reliable LLM judges**.

## Biases and Mitigation Strategies

* While LLM-as-a-Judge offers strong alignment with human judgment at scale, it is not neutral or error-free. Judge models inherit biases from pretraining data, instruction tuning, and prompt design. This section catalogs the **most common bias modes observed in LLM-as-a-Judge**, explains why they arise, and summarizes **practical mitigation strategies** grounded in the literature and deployed systems.

### Length and Verbosity Bias

#### Description

* LLM judges tend to prefer **longer, more verbose outputs**, even when verbosity does not correlate with correctness or usefulness. Longer answers often appear more fluent, detailed, and confident, which can mislead judges into assigning higher scores.
* This bias is empirically documented in [Large Language Models Are Not Fair Evaluators](https://arxiv.org/abs/2305.17926) by Wang et al. (2023).

#### Why It Happens

* Pretraining data rewards explanatory, verbose text
* Instruction tuning often emphasizes “helpfulness”
* Fluency is conflated with quality in latent representations

#### Mitigation Strategies

* **Explicit conciseness criteria**: Add a dedicated conciseness dimension (as in your rubric) to counterbalance verbosity.
* **Length normalization**: Penalize or bucket scores by length bands.
* **Hard constraints**: Explicitly instruct judges to ignore verbosity unless required by the task.
* **Pairwise comparison with swapped lengths**: Use pairwise prompts where one answer is shorter but correct.
* Supported by practices in [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685) by Zheng et al. (2023).

### Positional and Ordering Bias

#### Description

* In pairwise or listwise evaluation, LLM judges may favor:

  + The first item presented
  + The last item presented
  + Items appearing earlier in a list
* This positional bias affects both absolute judgments and relative rankings.

#### Why It Happens

* Transformer attention asymmetries
* Instruction-following heuristics (“evaluate the first answer”)
* Exposure bias from conversational data
* Documented in [A Large-Scale Analysis of Evaluation Biases in LLMs](https://arxiv.org/abs/2305.17926) by Wang et al. (2023).

#### Mitigation Strategies

* **Randomized ordering**: Shuffle candidate order across evaluations.
* **Bidirectional evaluation**: Evaluate (A, B) and (B, A) and average results.
* **Explicit neutrality instructions**: Instruct the judge to ignore position and treat all candidates symmetrically.
* **Pointwise fallback**: Use pointwise scoring when ordering effects dominate.

### Self-Preference and Model Identity Bias

#### Description

* LLMs often prefer outputs that resemble their own style, reasoning patterns, or phrasing. When the judge model is similar to the generator, this can lead to **self-reinforcement bias**.
* Observed in both evaluation and reward modeling contexts, including [On the Dangers of Stochastic Parrots](https://dl.acm.org/doi/10.1145/3442188.3445922) by Bender et al. (2021) (indirectly) and later preference modeling work.

#### Why It Happens

* Shared pretraining distributions
* Latent style matching
* Instruction-following alignment effects

#### Mitigation Strategies

* **Judge–generator separation**: Use a different model family or version for judging.
* **Ensemble judges**: Average scores across heterogeneous judge models.
* **Style-agnostic rubrics**: Focus criteria on factuality and constraints, not phrasing.
* **Human calibration checks**: Periodically validate judge preferences against human annotations.
* Used in practice in RLAIF systems such as [Training Language Models from AI Feedback](https://arxiv.org/abs/2302.08582) by Bai et al. (2023).

### Over-Confidence and Hallucination Blindness

#### Description

* LLM judges may fail to penalize **confident but incorrect** outputs, especially when errors are subtle, technical, or require external knowledge.
* This issue is closely related to hallucination detection challenges discussed in [Evaluating the Factual Consistency of Summaries](https://arxiv.org/abs/2008.01415) by Kryściński et al. (2020).

#### Why It Happens

* Judges rely on internal world knowledge, which may be incomplete
* Fluent text triggers higher perceived plausibility
* Lack of grounding signals

#### Mitigation Strategies

* **Faithfulness criteria**: Explicitly separate factual correctness from fluency.
* **Context-aware judging**: Provide the source document or evidence to the judge.
* **Binary constraint checks**: Use yes/no checks for factual violations before subjective scoring.
* **Hybrid pipelines**: Combine LLM judges with symbolic or retrieval-based validators.
* Common in RAG evaluation pipelines such as those described in [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) by Lewis et al. (2020).

### Prompt Sensitivity

#### Description

* LLM-as-a-Judge outputs can vary significantly with small prompt changes, leading to instability across runs or versions.
* Analyzed in [How to Evaluate Language Models: A Survey](https://arxiv.org/abs/2307.03109) by Chang et al. (2023).

#### Why It Happens

* Implicit instruction weighting
* Order effects in criteria presentation
* Ambiguous scale definitions

#### Mitigation Strategies

* **Anchored examples**: Provide example inputs for each score level (as in your prompt).
* **Schema-constrained outputs**: Enforce JSON or schema-based responses.
* **Prompt freezing**: Version and lock judge prompts.
* **Self-consistency**: Sample multiple judge outputs and aggregate, as in [Self-Consistency Improves Chain of Thought Reasoning](https://arxiv.org/abs/2203.11171) by Wang et al. (2022).

### Reward Hacking

#### Description

* When models are trained directly against a fixed judge, they may learn to exploit weaknesses in the rubric rather than improve true quality.
* This phenomenon mirrors classical reward hacking, discussed in [Specification Gaming](https://arxiv.org/abs/1903.03400) by Krakovna et al. (2020).

#### Why It Happens

* Static evaluation criteria
* Predictable judge behavior
* Optimization pressure without diversity

#### Mitigation Strategies

* **Judge rotation**: Periodically update or ensemble judges.
* **Mixed supervision**: Combine human and AI judgments.
* **Adversarial testing**: Probe judge failure modes explicitly.
* **Holdout evaluators**: Maintain unseen evaluation criteria.

### Takeaways

* LLM-as-a-Judge is powerful but **not objective by default**. Robust systems:

  + Anticipate common bias modes
  + Encode counterbalances directly into rubrics
  + Use escalation strategies (pointwise \(\rightarrow\) pairwise \(\rightarrow\) listwise)
  + Periodically validate against human judgment
* With these safeguards in place, LLM-as-a-Judge becomes a reliable, scalable component of modern evaluation and ranking pipelines.

## Causal Judge Evaluation (CJE): Calibrated Surrogate Metrics for LLM-as-a-Judge

### Motivation: Why Calibration Is Necessary for LLM-as-a-Judge

* [Causal Judge Evaluation: Calibrated Surrogate Metrics for LLM Systems](https://arxiv.org/abs/2512.11150) by Landesberg et al. (2025) identify three fundamental statistical failures in standard LLM-as-a-Judge practice when judge scores are treated as direct proxies for oracle outcomes such as human preferences or downstream KPIs.

  1. **Preference inversion:** uncalibrated judge scores \(S\) may be positively correlated with oracle labels \(Y\) overall, yet induce incorrect rankings where higher \(S\) implies lower \(Y\).
  2. **Invalid uncertainty estimates:** naive confidence intervals constructed on uncalibrated judge scores exhibit near-zero coverage, even when nominally set to 95%.
  3. **Off-policy evaluation (OPE) collapse under limited overlap:** importance-weighted estimators such as IPS and SNIPS fail even when effective sample size (ESS) appears high, due to insufficient coverage of target-policy-typical regions.
* These failures directly challenge the assumption—implicit in much prior LLM-as-a-Judge work—that correlation between judge scores and human labels is sufficient for reliable evaluation.

### Problem Setup and Notation

* The paper formalizes LLM evaluation as a calibrated surrogate estimation problem. Logged data are tuples \((X\_i, A\_i, S\_i)\) collected under a logging policy \(\pi\_0\), where \(S\_i = s(X\_i, A\_i)\) is a scalar judge score available for all samples, and a small oracle slice additionally provides labels \(Y\_i\).
* For a target policy \(\pi'\), the estimand is the counterfactual value:

\[V(\pi') = \mathbb{E}[Y(\pi')]\]

* Sequence-level importance weights are computed via teacher forcing:

\[W\_{\pi', i} = \frac{\pi'(A\_i \mid X\_i)}{\pi\_0(A\_i \mid X\_i)} = \exp\big(\log p\_{\pi'}(A\_i \mid X\_i) - \log p\_{\pi\_0}(A\_i \mid X\_i)\big)\]

### Core Contribution: The Causal Judge Evaluation (CJE) Framework

* CJE introduces a unified framework that corrects all three failure modes through three tightly coupled components:

  1. **AutoCal-R:** reward calibration via mean-preserving isotonic regression from judge score \(S\) to oracle outcome \(Y\).
  2. **SIMCal-W:** importance-weight calibration using stacked, \(S\)-monotone, unit-mean projections to stabilize variance.
  3. **Oracle-Uncertainty-Aware (OUA) inference:** confidence intervals that explicitly propagate calibration uncertainty.
* Together, these components instantiate what the authors call Design-by-Projection, where justified structural assumptions (monotonicity, mean constraints, orthogonality) are encoded as projections onto restricted statistical models with provably lower variance.

#### AutoCal-R: Mean-Preserving Reward Calibration

* The first step in CJE is to learn a calibrated reward \(R = f(S)\) using a small oracle-labeled slice. In its default mode, AutoCal-R fits an isotonic regression:

  \[\hat f \in \arg\min\_{f \in \mathcal{M}\_\uparrow} \sum\_{i \in \mathcal{O}} (Y\_i - f(S\_i))^2\]
  + where \(\mathcal{M}\_\uparrow\) is the set of monotone non-decreasing functions.
* This projection preserves the mean of \(Y\) exactly and prevents preference inversion by construction. When monotonicity in \(S\) is insufficient—e.g., due to length bias—the method automatically falls back to a two-stage calibration, first learning a flexible index \(Z = g(S, X)\) and then applying isotonic regression on its empirical CDF.
* The following figure shows the CJE pipeline overview: a small oracle slice provides labels to train a calibration model \(S \rightarrow Y\), which is then applied to large-scale surrogate-only evaluation where oracle labels are unavailable, enabling policy evaluation at a fraction of the cost.

#### SIMCal-W: Stabilizing Importance Weights

* CJE shows that high ESS does not guarantee reliable OPE when the logging policy rarely visits regions typical of the target policy. This phenomenon is formalized via the Coverage-Limited Efficiency (CLE) lower bound:

  \[\mathrm{SE}(\hat V\_{\mathrm{IPS}}) \ge \frac{\sigma\_T \alpha}{\sqrt{\beta n}} \sqrt{1 + \chi^2(\pi'\_T \mid\mid \pi\_{0,T})}\]
  + where \(\alpha\) is target mass in the target-typical region \(T\) and \(\beta\) is logger mass in that region.
* SIMCal-W addresses variance—but not coverage—by projecting raw importance weights onto the space of unit-mean, $S$-monotone functions and stacking increasing, decreasing, and baseline candidates to minimize influence-function variance. This ensures:

\[\mathbb{E}\_{\pi\_0}[W\_{\pi'}] = 1 \quad \text{and} \quad \mathrm{Var}(W\_{\pi'}) \text{is controlled}\]

#### OUA Inference: Valid Uncertainty Quantification

* A key insight of the paper is that treating the learned calibration function \(\hat f\) as fixed leads to dramatic underestimation of uncertainty. CJE decomposes total variance as:

  \[\mathrm{Var}\_{\text{total}}(\hat V) = \mathrm{Var}\_{\text{eval}}(\hat V \mid \hat f) + \mathrm{Var}\_{\text{cal}}(\hat f)\]
  + … and estimates \(\mathrm{Var}\_{\text{cal}}\) via a delete-one-oracle-fold jackknife over the calibration step.
* Empirically, this increases coverage from near 0% (naive CIs) to 85–96% across estimators on the Chatbot Arena benchmark.

### Implications for LLM-as-a-Judge Systems

* CJE reframes LLM-as-a-Judge from a heuristic proxy into a statistically principled surrogate modeling problem. Its results imply that:

  + Correlation between judge scores and human labels is insufficient without calibration.
  + Pairwise or listwise rankings derived from uncalibrated judges can be systematically wrong.
  + Reliable uncertainty estimates require accounting for calibration uncertainty, especially when oracle labels are scarce.
* CJE provides a formal foundation for many previously discussed failure modes—preference inversion, overconfidence, and reward hacking—and offers concrete, theoretically grounded mitigation strategies.

## When to Use Which Paradigm: A Practical Decision Guide

* This section provides a concrete, system-level decision guide for choosing between **pointwise**, **pairwise**, and **listwise** paradigms when using LLM-as-a-Judge and LTR. It additionally clarifies **when to introduce multimodal judges** and **when to replace a single judge with a panel of judges**.
* The goal is to help you select the *simplest paradigm that reliably solves the problem*, escalating only when necessary along three orthogonal axes:

  1. **Evaluation granularity** (pointwise \(\rightarrow\) pairwise \(\rightarrow\) listwise)
  2. **Judge capacity** (single judge \(\rightarrow\) panel of judges)
  3. **Input modality** (text-only \(\rightarrow\) multimodal)

### Pointwise Evaluation: When Absolute Scoring Is Enough

#### When to Use Pointwise

* Use **pointwise evaluation** when:

  + You need to score each output independently
  + Outputs will be filtered, thresholded, or aggregated later
  + The task has reasonably well-defined criteria
  + You want maximal scalability and parallelism
  + Latency and cost are important constraints
  + You are bootstrapping supervision data
  + Global ordering between outputs is not required
* Typical use cases:

  + Offline model evaluation
  + Dataset filtering and quality control
  + Reward modeling targets
  + CI-style regression testing
  + RAG document scoring
  + Safety or policy compliance checks
  + Hallucination detection with binary or ternary criteria
* This is the **default choice** in most production systems.

#### Why Pointwise Works Well

* Simple mental model: “Is this output good?”
* Easy to operationalize with structured rubrics
* Works naturally with mixed-scale criteria (binary, ternary, Likert-type)
* Judge calls are embarrassingly parallel
* Maps directly to pointwise LTR models (e.g., monoBERT-style scoring)
* As noted earlier, **LLM-as-a-judge models most commonly perform pointwise evaluation (scoring each output independently)**, as documented in [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685) by Zheng et al. (2023).

#### Extensions: Panels and Multimodal Judges in Pointwise Settings

* Pointwise evaluation is also the **most common entry point** for both:
* **Panels of LLMs-as-Judges**, where multiple judges score each output independently and scores are aggregated (e.g., averaged or max-pooled), as shown in [Replacing Judges with Juries](https://arxiv.org/abs/2404.18796) by Verga et al. (2024).
* **Multimodal LLMs-as-Judges**, where the judge consumes images (or video) alongside text to score outputs for vision–language tasks, such as [LLaVA-Critic](https://arxiv.org/abs/2410.02712) by Xiong et al. (2024) and [Prometheus-Vision](https://arxiv.org/abs/2401.06591) by Lee et al. (2024).
* In practice, most multimodal judging today is **pointwise**, because it is simpler, cheaper, and easier to calibrate than multimodal pairwise or listwise evaluation.

#### When Pointwise Breaks Down

* Judges struggle to calibrate absolute scores
* Small differences between outputs matter
* Outputs are all “good enough,” but ordering matters
* Scale drift across batches becomes noticeable
* Single-judge bias or instability becomes apparent
* When these issues appear, **pairwise evaluation or judge panels** are often the next step.

### Pairwise Evaluation: When Relative Preference Matters

#### When to Use Pairwise

* Use **pairwise evaluation** when:

  + You care about *which output is better*, not how good it is
  + Outputs are close in quality
  + Absolute scores are noisy or poorly calibrated
  + Human-like preference judgments are desired
  + You are selecting between two or a small number of candidates
  + You want to reduce scale interpretation ambiguity
* Typical use cases:

  + A/B testing between models
  + Preference modeling and reward learning
  + Human-in-the-loop evaluation
  + Model selection
  + Tie-breaking among top candidates
  + Pairwise reward modeling for RLHF or RLAIF

#### Why Pairwise Often Improves Reliability

* Pairwise judgments reduce cognitive load for both humans and models:

  + Easier to answer “Which is better?” than “How good is this?”
  + Reduces ambiguity in ordinal or Likert-type scales
  + Higher inter-annotator and human–model agreement, as shown in [Large Language Models Are Not Fair Evaluators](https://arxiv.org/abs/2305.17926) by Wang et al. (2023)
* Pairwise evaluation aligns naturally with:

  + Pairwise LTR objectives (RankNet, duoBERT)
  + Preference datasets used in RLHF and RLAIF
  + Direct Preference Optimization (DPO)

#### Panels and Multimodal Pairwise Evaluation

* Pairwise evaluation is especially effective when combined with **panels of judges**:

  + Each judge independently decides which output is better
  + Preferences are aggregated via majority vote or averaged logits
  + Reduces positional bias and self-preference effects
* This strategy is empirically validated in [Replacing Judges with Juries](https://arxiv.org/abs/2404.18796) by Verga et al. (2024), which shows that small, diverse panels outperform single large judges in pairwise settings.
* Multimodal pairwise judging is used less frequently, but is critical when:

  + Visual grounding is required to decide preference
  + Two captions, answers, or explanations must be compared against an image
  + Reward signals are generated for multimodal preference learning
* LLaVA-Critic explicitly supports such pairwise multimodal judging.

#### Trade-offs

* Quadratic cost in number of candidates
* Harder to aggregate across many outputs
* Still local: no global consistency guarantees
* If you need *global ordering* across many outputs, listwise evaluation becomes appropriate.

### Listwise Evaluation: When Global Ranking Quality Matters

#### When to Use Listwise

* Use **listwise evaluation** when:

  + You must rank many outputs at once
  + Global consistency across outputs matters
  + You want to optimize ranking metrics directly
  + Interactions between outputs affect evaluation
  + You can afford higher compute and memory cost
* Typical use cases:

  + Final-stage reranking in RAG pipelines
  + Search result ordering
  + Leaderboard construction
  + Evaluation of multiple candidate generations
  + Research settings where ranking quality is paramount

#### Why Listwise Is Powerful

* Listwise methods:

  + Optimize ranking quality holistically
  + Capture inter-item dependencies
  + Avoid local inconsistencies (e.g., A > B, B > C, but C > A)
* Modern listwise systems include:

  + Encoder-only listwise rankers such as [ListBERT](https://arxiv.org/abs/2206.15198) by Kumar et al. (2022)
  + Encoder–decoder listwise rankers such as [ListT5](https://arxiv.org/abs/2402.15838) by Yoon et al. (2024)
  + Agentic and reasoning-based rerankers such as [REARANK](https://arxiv.org/abs/2505.20046) by Zhang et al. (2025)

#### Panels and Multimodal Listwise Evaluation

* Listwise evaluation can also be combined with:

  + **Panels of judges**, using rank aggregation methods (e.g., average rank, Borda count)
  + **Multimodal judges**, when ranking depends on visual evidence
* However, this combination is **computationally expensive** and is typically reserved for:

  + Small candidate sets
  + Offline evaluation
  + Research benchmarks

#### Trade-offs

* Highest computational cost
* More complex training and inference
* Harder to debug and calibrate
* Often unnecessary unless ranking quality is critical

### A Simple Escalation Strategy (Including Judges and Modalities)

* A practical escalation strategy used in real systems:

  1. Start with **pointwise LLM-as-a-Judge (single, text-only)**
  2. Add **a panel of judges** if:

     + Scores are unstable
     + Bias is suspected
  3. Move to **pairwise evaluation** if:

     + Differences are subtle
     + Calibration is unreliable
  4. Introduce **multimodal judges** if:

     + Evaluation depends on images or video
  5. Use **listwise evaluation** only when:

     + You must rank many candidates
     + Global ordering quality is essential
* This mirrors how humans evaluate: absolute judgments first, comparisons next, full rankings last—while consulting multiple evaluators when stakes are high.

### Comparative Analysis Across Evaluation Dimensions

| **Evaluation Dimension** | **Configuration** | **Typical Use Cases** |
| --- | --- | --- |
| Evaluation granularity | Pointwise | Independent scoring, filtering, CI evaluation, reward bootstrapping, default evaluation mode |
| Pairwise | A/B testing, preference learning, tie-breaking, calibration-sensitive evaluation |
| Listwise | Final-stage reranking, leaderboard construction, global ordering of many candidates |
| Judge capacity | Single judge | Low-cost evaluation, rapid iteration, prototyping, low-stakes tasks |
| Panel of judges | Bias reduction, robustness, human-aligned scoring, high-stakes evaluation |
| Input modality | Text-only | Language modeling, reasoning, summarization, code and policy evaluation |
| Multimodal | Vision–language tasks, captioning, VQA, multimodal preference learning |

### Practical Tips

#### Use pointwise evaluation by default

* Pointwise evaluation should be the starting point for almost all LLM-as-a-Judge systems because it imposes the fewest assumptions on the evaluation problem.
* In pointwise evaluation, each output is judged independently against a rubric. This matches how most quality criteria are defined in practice (correctness, safety, faithfulness, clarity) and maps cleanly to scalable infrastructure: evaluations are parallelizable, easy to cache, and easy to aggregate downstream.
* Pointwise judging also aligns naturally with how LLMs are instruction-tuned. Asking “Is this output acceptable under these criteria?” is a task modern LLMs handle reliably, especially when rubrics include anchored examples and constrained output schemas.
* Most importantly, pointwise evaluation gives you **useful signals early**. Even if scores are noisy, they are sufficient for filtering, regression testing, and bootstrapping supervision. In practice, many systems never need to move beyond pointwise judging.
* **Escalation trigger:** move on only if absolute scores become unstable, poorly calibrated, or insufficient to distinguish high-quality outputs.

#### Add judge panels before changing paradigms

* If pointwise evaluation starts to show variance, bias, or inconsistency, the first escalation should be **adding judges**, not changing the evaluation granularity.
* Panels of LLMs-as-Judges reduce error by aggregation rather than by making the task harder for a single judge. Empirically, averaging or pooling judgments from diverse models improves alignment with human evaluations more reliably than switching to pairwise or listwise judging with a single model.
* Judge panels specifically mitigate:

  + Self-preference bias (models favoring their own outputs)
  + Prompt sensitivity and formatting artifacts
  + Overconfidence in fluent but incorrect answers
* Operationally, panels are easy to introduce because they preserve the same prompt and evaluation interface. You simply replicate the judge call across models and aggregate results.
* **Escalation trigger:** move beyond panels only if **relative ordering** between outputs, rather than absolute quality, becomes the core requirement.

#### Use pairwise evaluation when relative preference matters

* Pairwise evaluation should be introduced when the question is no longer “Is this good?” but rather “Which of these is better?”
* This situation arises when:

  + Outputs are close in quality
  + Most candidates pass minimum quality thresholds
  + Absolute scores compress or saturate
  + Human decision-making would naturally be comparative
* Pairwise judging reduces calibration issues because it eliminates the need to interpret score scales. Both humans and LLMs are more reliable when making comparative judgments, especially under subtle trade-offs.
* In practice, pairwise evaluation is most effective when combined with judge panels. Each judge provides a preference, and aggregation yields a stable decision even if individual judgments disagree.
* **Escalation trigger:** move beyond pairwise only if you must rank **many outputs simultaneously** and require global consistency.

#### Introduce multimodal judges only when grounding is required

* Multimodal LLMs-as-Judges should be introduced only when the evaluation task depends on **non-textual evidence**.
* Examples include:

  + Visual question answering
  + Image-grounded explanation evaluation
  + Caption correctness and hallucination detection
  + Multimodal preference learning
* If the task can be reliably reduced to text (e.g., via deterministic preprocessing), text-only judges are usually cheaper, faster, and more stable.
* Multimodal judging increases system complexity: it requires multimodal inputs, heavier models, and careful prompt design to ensure grounding is actually used. As a result, multimodal judges should be treated as **specialized evaluators**, not defaults.
* **Escalation trigger:** introduce multimodal judges only when text-only judges fail due to missing perceptual information.

#### Use listwise evaluation sparingly, when ranking quality outweighs cost

* Listwise evaluation is the most expressive but also the most expensive paradigm. It should be reserved for cases where **global ranking quality is the primary objective**.
* This includes:

  + Final-stage reranking in retrieval or RAG pipelines
  + Benchmark leaderboard construction
  + Research settings where ranking metrics matter more than cost
* Listwise methods allow judges or models to reason over interactions among all candidates, avoiding local inconsistencies inherent in pointwise or pairwise decisions. However, they come with significant drawbacks: higher computational cost, reduced scalability, and increased difficulty in debugging failures.
* In production systems, listwise evaluation is often applied to **small candidate sets** or performed offline, with pointwise or pairwise methods handling the majority of evaluations.
* **Escalation trigger:** use listwise evaluation only when pairwise comparisons fail to produce a consistent or acceptable ordering.

#### The Core Principle

* Across all dimensions, the guiding principle is: **Increase robustness before increasing complexity.**
* Start simple, add redundancy (panels), then change the evaluation task (pairwise), and only then adopt the most expressive (and expensive) paradigms such as multimodal or listwise judging.

## References

### LLM-as-a-Judge Foundations and Bias Analysis

* [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685) by Zheng et al. (2023)
* [Large Language Models Are Not Fair Evaluators](https://arxiv.org/abs/2305.17926) by Wang et al. (2023)
* [LLM Evaluators Recognize and Favor Their Own Generations](https://arxiv.org/abs/2401.01917) by Panickssery et al. (2024)
* [An Empirical Study of LLM-as-a-Judge for LLM Evaluation](https://arxiv.org/abs/2403.02839) by Huang et al. (2024)

### Panels / Juries of LLMs-as-Judges

* [Replacing Judges with Juries: Evaluating LLM Generations with a Panel of Diverse Models](https://arxiv.org/abs/2404.18796) by Verga et al. (2024)
* [Variations in Relevance Judgments and the Measurement of Retrieval Effectiveness](https://dl.acm.org/doi/10.1145/290941.291017) by Voorhees (1998)

### Multimodal LLMs-as-Judges

* [Prometheus-Vision: Vision-Language Model as a Judge for Fine-Grained Evaluation](https://arxiv.org/abs/2401.06591) by Lee et al. (2024)
* [LLaVA-Critic: Learning to Evaluate Multimodal Models](https://arxiv.org/abs/2410.02712) by Xiong et al. (2024)
* [LLaVA: Large Language and Vision Assistant](https://arxiv.org/abs/2304.08485) by Li et al. (2023)

### Learning-to-Rank (LTR) and Neural Re-ranking

* [Multi-Stage Document Ranking with BERT](https://arxiv.org/abs/1910.14424) by Nogueira et al. (2019)
* [ListBERT: Learning to Rank E-commerce Products with Listwise BERT](https://arxiv.org/abs/2206.15198) by Kumar et al. (2022)
* [ListT5: Listwise Re-ranking with Fusion-in-Decoder Improves Zero-shot Retrieval](https://arxiv.org/abs/2402.15838) by Yoon et al. (2024)
* [REARANK: Reasoning Re-ranking Agent via Reinforcement Learning](https://arxiv.org/abs/2505.20046) by Zhang et al. (2025)
* [Rank-K: Test-Time Reasoning for Listwise Reranking](https://arxiv.org/abs/2505.14432) by Yang et al. (2025)

### Reinforcement Learning for LLMs-as-Judges and Reward Modeling

* [J1: Incentivizing Thinking in LLM-as-a-Judge via Reinforcement Learning](https://arxiv.org/abs/2505.10320) by Whitehouse et al. (2025)
* [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://arxiv.org/abs/2402.03300) by Shao et al. (2024)
* [DeepSeek-R1: Incentivizing Reasoning in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948) by Guo et al. (2025)
* [Self-Taught Evaluators](https://arxiv.org/abs/2408.02666) by Wang et al. (2024)
* [Learning to Plan and Reason for Evaluation with Thinking-LLM-as-a-Judge](https://openreview.net/forum?id=PNRznmmWP7) by Saha et al. (2025)

### Reward Model and Judge Benchmarks

* [PPE: Preference Proxy Evaluations](https://github.com/lmarena/PPE) by Chiang et al. (2024)
* [RewardBench: Evaluating Reward Models for Language Modeling](https://arxiv.org/abs/2403.13787) by Lambert et al. (2024)
* [RewardBench 2: Advancing Reward Model Evaluation](https://arxiv.org/abs/2506.01937) by Malik et al. (2025)
* [JudgeBench: A Benchmark for Evaluating LLM-based Judges](https://arxiv.org/abs/2410.12784) by Tan et al. (2024)
* [RM-Bench](https://arxiv.org/abs/2408.02666) by Wang et al. (2024)
* [FollowBenchEval](https://arxiv.org/abs/2505.10320) by Whitehouse et al. (2025)

## Citation

If you found our work useful, please cite it as:

```
@article{Chadha2020DistilledAutoraters,
  title   = {Autoraters / LLM as a Judge},
  author  = {Chadha, Aman},
  journal = {Distilled AI},
  year    = {2020},
  note    = {\url{https://aman.ai}}
}
```
