---
concept: LLM Hallucination
tags: [hallucination, factuality, grounding, faithfulness]
sources:
  - kb/hard/raw/lilian-weng/extrinsic-hallucinations-in-llms.md
  - kb/hard/raw/eugene-yan/evaluation-hallucination-detection-for-abstractive-summaries.md
  - kb/hard/raw/aman-ai/primers-factuality-in-llms.md
last_compiled: 2026-04-05
related: [llm-evaluation, retrieval-augmented-generation]
---

# LLM Hallucination

Hallucination — generating content that is fabricated, inconsistent with source material, or ungrounded in fact — is one of the primary reliability failures of language models. Understanding it requires a precise taxonomy: not all errors are the same kind, and different mitigation strategies apply depending on the failure mode.

## Taxonomy

### Intrinsic vs. Extrinsic Hallucination

The most fundamental distinction:

**Intrinsic (in-context) hallucination**: The model's output contradicts information explicitly provided in the context. For example, a summary that changes a number, swaps subject and object, or introduces a negation not present in the source document. The ground truth for evaluation is the provided context itself.

**Extrinsic (out-of-context) hallucination**: The model generates content not grounded in either the provided context *or* world knowledge — it fabricates facts, invents citations, invents entities, or states confident falsehoods about the world. Evaluating this requires external knowledge verification, not just context comparison.

### Factuality Taxonomy (More Granular)

**Short-form factuality**: Correctness of atomic, single-fact responses (e.g., "What year was X born?"). Evaluable by exact match against an authoritative source. Benchmarks: TruthfulQA, SimpleQA, HaluEval.

**Truthfulness / intrinsic factuality**: Whether the model's internal knowledge (captured during pretraining) is accurate. A model may be internally consistent but still wrong if its training data contained errors or if facts have changed post-cutoff.

**Faithfulness / extrinsic factuality**: Whether the output is consistent with provided evidence (source documents, retrieved passages). A faithful output neither contradicts nor introduces information beyond what the evidence supports. Faithfulness does *not* require the evidence itself to be accurate — only that the output aligns with it.

**Groundedness**: A stricter version of faithfulness for RAG systems. Groundedness requires both (1) the output is entailed by the evidence and (2) the evidence itself is relevant and sufficient to support the claims. An output can be faithful to a retrieved passage yet ungrounded if the retrieval was incomplete.

**Long-form factuality**: Factual accuracy across multi-sentence outputs. Compounds errors because each additional sentence introduces new factual claims, magnifying error probability.

## Causes

**Knowledge cutoff and outdated facts**: Models encode knowledge from training data, which has a temporal cutoff. Facts that change over time (political offices, record holders, current events) become incorrect without retrieval.

**Plausibility bias**: Training on internet text teaches models that plausible-sounding text is rewarded. A model may generate a credible-sounding but fabricated citation because that pattern was common in training data.

**Attention failure on long contexts**: In long inputs, models may fail to attend adequately to relevant source information, generating from prior rather than the context — producing technically extrinsic hallucinations even when the answer was available.

**Sycophancy**: Models trained with RLHF can learn to generate confident, authoritative-sounding responses because humans rate confident outputs more positively, even when the model's actual confidence is low.

**Compounding in generation**: Early hallucinations condition subsequent generation. A fabricated claim in sentence 2 can cause sentence 3 to build on that false premise, creating cascading errors.

## Measurement Approaches

### Reference-Based Metrics

Compare generated output to a gold reference: ROUGE (n-gram overlap), BERTScore (contextual embedding similarity), MoverScore (soft token alignment). Fast and scalable but limited: reference quality matters, and modern LLMs often produce outputs that surpass human-written references — making reference-based metrics unreliable as absolute quality measures.

### NLI-Based (Entailment) Metrics

Use a Natural Language Inference model to determine whether each claim in the output is entailed by (supported by), contradicted by, or neutral with respect to the source.

**SummaC**: Applies NLI at sentence level rather than document level. For each sentence in the output, compute NLI against every sentence in the source; retain the maximum entailment score per output sentence; aggregate by mean. More reliable than document-level NLI because NLI models were trained on sentence pairs.

Key finding from SummaC: up to 30–43% of summaries on CNN/DailyMail contain faithfulness errors; XSum had ~92% faithfulness error rate. Abstractive hallucination is pervasive.

### QA-Based Metrics

Generate questions from the output, answer them using the source document, and measure answer overlap. Intuition: if the output says X, we can ask "is X true in the source?" and verify via a QA model.

**QAGS** (Wang et al. 2020): Generate questions from the output summary, answer them against both the summary and the source, compare answers.

**QuestEval**: Combines both directions — generate questions from source (recall-oriented) and from output (precision-oriented), combine via harmonic mean.

**QAFactEval**: Systematic comparison of QA and NLI approaches; finds QAFactEval slightly outperforms QuestEval, but simple MNLI/ANLI classifiers remain strong baselines.

### LLM-as-Judge

Use a capable LLM (GPT-4, Claude) as an evaluator. **G-Eval** (Liu et al. 2023): provide the LLM with the task description, evaluation criteria, a CoT evaluation rubric, and the text to evaluate; have it score 1–5. GPT-4 as judge achieves Spearman correlation of 0.514 with human judgments — outperforming all automated metrics. But: GPT-4 has a known bias toward AI-generated text (rates it higher than human-written summaries even when humans prefer the latter).

### SelfCheckGPT

Sampling-based hallucination detection without a reference. Core assumption: *if a model knows a fact, its stochastically sampled responses will be consistent with each other*. If it's hallucinating, different samples will diverge and contradict.

Procedure: sample multiple responses at temperature > 0; measure pairwise consistency (via NLI or n-gram overlap); high divergence signals likely hallucination. Useful for detecting factual uncertainty without external knowledge sources.

### Search-Augmented Evaluation

**SAFE** (Wei et al. 2024): decompose the output into atomic factual claims; for each claim, retrieve supporting evidence via search; verify claim against evidence. More reliable than RM-based methods for long-form outputs. Part of LongFact benchmark.

**FActScore** (Min et al. 2023): same decompose-retrieve-verify pattern; uses Wikipedia as the knowledge source.

## Mitigation Strategies

### Retrieval-Augmented Generation (RAG)

Augment generation with retrieved evidence relevant to the query at inference time. The model is constrained to ground its output in the retrieved passages. Effective at reducing knowledge-cutoff hallucinations and improving groundedness. Does not fully solve the problem — models can still ignore retrieved context or hallucinate details not in retrieved documents. See [[hard/wiki/retrieval-augmented-generation|Retrieval-Augmented Generation]].

### Self-Consistency and Voting

Sample K outputs; take the majority answer. Inconsistent hallucinations are suppressed because fabricated details rarely agree across samples. Most effective for questions with verifiable single answers (math, factoid QA). Less effective for open-ended generation where there is no single correct output.

### NLI-Based Post-Hoc Filtering

Run a trained NLI model over each sentence of the output against the source document. Flag sentences with entailment score below a threshold. Either filter them out or prompt the model to regenerate those sentences. Scalable, no LLM calls required.

### Citation and Grounding Constraints

Require the model to cite specific evidence for each claim. Evaluate whether the cited evidence actually entails the claim. Forces grounding at generation time. Implemented via prompting ("cite your sources") or fine-tuning.

### DOLA (Decoding by Contrasting Layers)

At inference time, contrast the probabilities predicted by earlier and later transformer layers. Later layers encode more task-specific knowledge; earlier layers encode more surface/statistical patterns. By amplifying the later-layer signal, factual accuracy improves without fine-tuning or retrieval.

### Training-Time Interventions

- **RLHF with factuality rewards**: train reward models that penalize unsupported claims. Effective but requires careful construction of factuality-sensitive preference data.
- **Knowledge-augmented fine-tuning**: fine-tune on high-quality, fact-verified data.
- **Self-critique loops**: train models to identify and correct their own hallucinations via iterative self-evaluation.

## Practical Calibration

Models often hallucinate confidently. Calibration — aligning confidence to accuracy — is a prerequisite for reliable deployment. Well-calibrated models should say "I don't know" when they don't know. Strategies for improving calibration: temperature scaling on the output, sampling entropy as a confidence signal, prompting models to express uncertainty ("I'm not sure, but...").

A key finding: models sometimes internally represent truthfulness correctly even when generating false outputs (Orgad et al. 2025). Internal probing of activations can detect likely hallucinations before they are decoded — an emerging technique for selective regeneration.

## Summary of Evaluation Tools

| Method | Requires Reference? | Granularity | Best For |
|--------|--------------------|----|---------|
| ROUGE/BERTScore | Yes | Document | Fast automated eval |
| SummaC (NLI) | No (uses source) | Sentence | Faithfulness to source |
| QAGS/QuestEval | No (uses source) | Claim | Consistency checking |
| SelfCheckGPT | No | Sentence | Uncertainty detection |
| G-Eval (LLM judge) | No | Document | High-quality holistic eval |
| SAFE / FActScore | No (uses search) | Atomic claim | Long-form factuality |

## Sources

- Lilian Weng, "Extrinsic Hallucinations in LLMs" — `kb/hard/raw/lilian-weng/extrinsic-hallucinations-in-llms.md`
- Eugene Yan, "Evaluation & Hallucination Detection for Abstractive Summaries" — `kb/hard/raw/eugene-yan/evaluation-hallucination-detection-for-abstractive-summaries.md`
- Aman.ai, "Primers: Factuality in LLMs" — `kb/hard/raw/aman-ai/primers-factuality-in-llms.md`
