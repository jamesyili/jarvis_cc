# Diagnostic quiz — calibrating the learner model (September 2026)

**Purpose.** Replace the seed values in `kb/.kb/knowledge_state.json` with demonstrated ones. The seed (2026-09-07) assumed understanding 2 wherever James's background applies and guessed 3–4 where his production record warrants it. This quiz is the evidence. It covers every relevance-3 concept and sweeps relevance-2; relevance-0 concepts (CNNs, GANs, object detection, privacy, classical ML) are not assessed unless James asks.

**How to take it.** Open it with Leo (Claude Code) or Codex in **practice mode** (`learn` skill). One question at a time, spoken or typed, 2–4 minutes each, open book is fine but say so (supported rehearsal ≠ independent demonstration). The evaluator grades against the rubric below, quotes the key phrase, and writes the result with `python3 scripts/kb_knowledge_state.py set <concept> --understanding N --kind practice --by codex|claude --note "DQ-<id>: <phrase> — <what it showed>"`. Three sittings of ~45 minutes; stop a sitting whenever the time is gone and resume at the next question id (record the cursor in `learning_progress.md`). Skip any question whose answer James has already demonstrated in a lesson since 9/7; the model, not the quiz, is the record.

**Adaptive rule.** Each question names a target level. Start each concept at its seeded level. A clean answer at the target moves to the next-higher probe in the same cluster if one exists; a miss at a level-2 probe on a concept seeded at 2 lowers it to 1 with the reason in the note. Nothing is graded on delivery; terminology matters only where the wrong word would mislead a listener (the learn skill's terminology practice).

## Rubric (applied per question)

| Level | What the answer shows |
|---|---|
| **2 basic** | Correct definitions; knows the components and what each is for; can follow the mechanism when walked through it; errors appear at mechanism detail or in trade-offs. |
| **3 proven depth** | Explains the mechanism unprompted; names the central trade-off and at least one concrete failure mode; connects it to a system he has run or a decision he has made; precise about inputs, outputs, and training targets. |
| **4 boundary pushing** | Identifies what is wrong or limited about current published practice and proposes a testable alternative, or has shipped/published beyond it and can say exactly where the frontier moved. |
| **↓ to 1** | Definitional error on a concept the seed assumed at 2, or cannot place the concept in a system at all. |

---

## Sitting 1 — strengths (calibrate 3 vs 4) and the top of the queue

### Cluster A — Retrieval core
*Concepts: `two-tower-retrieval` (seed 4), `approximate-nearest-neighbor` (3), `recsys-embeddings` (3), `loss-functions` (3), `self-supervised-contrastive` (2), `embeddings-and-representation-learning` (3)*

- **DQ-A1** (target 4 · `two-tower-retrieval`) — UBR shares one backbone across five surfaces with per-surface condition towers. Defend the claim that this is beyond current published practice. What would a reviewer say is already known (sampling-bias-corrected two-tower, multi-task towers, Netflix-style consolidation), what is new, and where does it break? Name the cross-surface negative-contamination problem in your own words and how you would measure it.
- **DQ-A2** (target 3 · `loss-functions`, `self-supervised-contrastive`) — In-batch negatives with logQ correction. Why do popular items get over-penalized without the correction, and what does the correction do to the gradient? When does mixed negative sampling beat it, and what does cross-batch negative sampling buy that a bigger batch does not?
- **DQ-A3** (target 3 · `approximate-nearest-neighbor`, `two-tower-retrieval`) — Viewer tower on GPU, pin tower on CPU. What is in the HNSW index and what is computed per request? What changes when you go to N conditions × M heads per user, and where is the latency cliff? Contrast HNSW with ScaNN's anisotropic quantization: what objective does ScaNN align to, and why does it matter for inner-product retrieval?
- **DQ-A4** (target 4 · `recsys-embeddings`) — Interest collapse in multi-interest models (argmax routing starves K−1 vectors) and embedding collapse in wide DLRMs (added width goes low-rank) are called one lesson in the 9/5 research synthesis. Do you agree? What coordination mechanism did the team's multi-embedding retrieval use, and what would you do differently now?

### Cluster B — Generative retrieval and semantic IDs
*Concepts: `generative-recommendation` (seed 2), `llm-recsys` (2), `semantic-id-tokenization` (2)*

- **DQ-B1** (target 3 · `generative-recommendation`) — The paused W01 prompt, verbatim: "We currently use a two-tower model and ANN retrieval. You're proposing a TIGER-style alternative. Walk me through the architecture, what each model learns and from which loss, and how a request becomes a set of recommended items. What would you need to demonstrate before choosing it over the existing system?"
- **DQ-B2** (target 3 · `semantic-id-tokenization`) — RQ-VAE codebooks. Why does residual quantization produce a hierarchy? Why do collisions rise as the corpus churns, and what does re-tokenization drift do to an already-trained generator? Give two mitigations and say which one the SID practitioner's handbook found unnecessary.
- **DQ-B3** (target 3 · `generative-recommendation`, `llm-recsys`) — PinRec is RecGPT: it generates a representation and retrieves through ANN. Argue for that hybrid over trie-constrained decoding using the hallucination-ceiling finding, then say what the hybrid gives up.
- **DQ-B4** (target 3 · `llm-recsys`) — Dylan's 8/24 question, redone with numbers. RecGPT as L1 at 10^5 QPS: write the cost-per-request formula (parameters × generated tokens × candidates ÷ MFU × quantization gain × micro-batching), fill in plausible values, and state under what MFU and precision it beats LWS on cost. Where does the argument depend on caching?

### Cluster E — Pre-ranking and evaluation
*Concepts: `pre-ranking-cross-stage-consistency` (seed 3), `learning-to-rank` (3), `reranking` (3), `recsys-evaluation` (3), `a-b-testing` (3), `counterfactual-evaluation` (2), `offline-online-calibration-and-candidate-logging` (2)*

- **DQ-E1** (target 4 · `pre-ranking-cross-stage-consistency`, `recsys-evaluation`) — State the RecSys 2026 "Alignment + Accuracy" framework in your own words. What is the regression-calibrated metric, and why does it predict online shifts when NDCG does not? What is the claim's weakest point?
- **DQ-E2** (target 3 · `pre-ranking-cross-stage-consistency`, `learning-to-rank`) — Sample-selection bias and ranking inconsistency as one disease with three cures: data-side (full-space sampling), model-side (ECM), supervision-side (distillation). Which does LWS use today and why? What logging would the other two need that you do not have?
- **DQ-E3** (target 3 · `pre-ranking-cross-stage-consistency`) — Write the L1 exit criterion as an inequality: the cost of enforcing L1↔L2 consistency versus the cost of collapsing the stage. Name every variable and where you would get each number at Pinterest. When would you revisit it?
- **DQ-E4** (target 3 · `offline-online-calibration-and-candidate-logging`, `recsys-evaluation`) — Why is recall@K a poor predictor of engagement lift for a retriever? Design the calibration experiment for UBR using the P2P and Notif launches you already have online results for. What is the unit of analysis, and what would make you distrust the fit?
- **DQ-E5** (target 3 · `counterfactual-evaluation`) — Evaluate a new nominator offline using impressions logged under the current one. What is the propensity, why does IPS variance explode at the tail, what does clipping do, and what bias does clipping reintroduce? When would you rather run the online test?
- **DQ-E6** (target 3 · `a-b-testing`, `reranking`) — A diversity control in L1 utility improves impression diversity and moves SSv2 by +0.05% with a wide interval. Walk through how you decide to ship: the metric hierarchy, novelty effects, interference between concurrent retrieval experiments, and what you would say to a PM who wants it now.

---

## Sitting 2 — the scaling and serving lanes

### Cluster C — Scaling
*Concepts: `recsys-scaling-laws` (seed 1), `large-language-models` (2), `mixture-of-experts` (1), `user-foundation-models-and-distillation` (2), `transfer-learning` (2), `transformer-architecture` (2), `sequence-models` (2)*

- **DQ-C1** (target 2 · `large-language-models`, `recsys-scaling-laws`) — Chinchilla in one paragraph, then deliberate overtraining and why labs do it. Then invert it: recsys is data-rich and compute-starved. What would "compute-optimal" mean for a user model trained on unbounded fresh interaction logs, and why is the embedding-versus-dense split a question LLM labs never face?
- **DQ-C2** (target 3 · `recsys-scaling-laws`) — Design the retrieval scaling study. Axes, the fixed fine-tune-compute constraint and why it is the right constraint, the y-axis, and the interpretation rule when the curve flattens (the Wukong lesson). How would you place embedding-table capacity versus dense capacity as an axis without confounding it with data?
- **DQ-C3** (target 2 · `mixture-of-experts`) — Fine-grained experts, shared experts, auxiliary-loss-free balancing: what problem does each solve? Why does MoE decouple quality from activated FLOPs, and what breaks at serving time with expert parallelism?
- **DQ-C4** (target 3 · `user-foundation-models-and-distillation`) — Scale the teacher, not the student. Why can a non-serveable teacher be arbitrarily large? What do you distill (logits, embeddings, rankings) and how does the choice change the student's loss? The CFM doc says FM pretraining fails to transfer unless fine-tune compute rises: what does that imply for a distilled retrieval student?
- **DQ-C5** (target 3 · `transfer-learning`) — UPP's fine-tuning ladder: none, into_ft_dhen, late_fusion, both, and the LoRA gap. Where does catastrophic forgetting of cross-surface knowledge show up, how would you detect it, and which rung protects against it at what cost?
- **DQ-C6** (target 3 · `transformer-architecture`) — MHA → GQA → MLA: what each saves and why MLA's low-rank KV compression keeps quality. What is FlashAttention's actual trick, and what does it change for a 16k-token user sequence in TransAct v2?
- **DQ-C7** (target 2 · `sequence-models`, `recsys-scaling-laws`) — HSTU: why pointwise aggregated attention instead of softmax for a non-stationary item vocabulary? What does M-FALCON amortize, and why does that matter more for ranking than retrieval?

### Cluster D — Serving efficiency
*Concepts: `serving-efficiency-and-user-state-caching` (seed 2), `llm-inference-serving` (2), `model-compression` (2)*

- **DQ-D1** (target 3 · `serving-efficiency-and-user-state-caching`) — User-state caching for LWS. What exactly is cached: the encoded history's KV state or a pooled vector? How is it invalidated when the user acts mid-session? What hit rate would you expect per session, and how is this different from ISR's cache-based candidate generation?
- **DQ-D2** (target 3 · `serving-efficiency-and-user-state-caching`, `llm-inference-serving`) — Prefill/decode disaggregation mapped onto viewer-tower-GPU / pin-tower-CPU. What is compute-bound and what is bandwidth-bound in your stack? Where does the host-CPU bottleneck the CFM doc describes actually sit, and what would you measure first?
- **DQ-D3** (target 3 · `model-compression`, `llm-inference-serving`) — The quantization ladder FP8 → INT8 → INT4 for embedding tables versus transducer layers: where does quality die first and why? What does dot-product-preserving KV quantization (TurboQuant's idea) change relative to MSE-faithful quantization?
- **DQ-D4** (target 2 · `serving-efficiency-and-user-state-caching`) — Define model FLOPs utilization. Estimate it for LWS serving today from numbers you know, state your assumptions, and say what reaching 25% would require.
- **DQ-D5** (target 3 · `llm-inference-serving`, `generative-recommendation`) — Speculative decoding or multi-token prediction for SID beam search: with beam width 32 and 4-token SIDs, does it help? Work it out, including where verification cost lands.

---

## Sitting 3 — sequences, exploration, agents, and the relevance-2 sweep

### Cluster F — Sequences, exploration, retention
*Concepts: `sequence-models` (seed 2), `personalization-patterns` (3), `recsys-beyond-accuracy` (3), `bandits-exploration-exploitation` (2), `data-flywheel` (3)*

- **DQ-F1** (target 3 · `sequence-models`) — Lifelong sequences: SIM's GSU/ESU, TWIN's consistency-preserved GSU, SDIM's hashing. Why was consistency the decisive factor, and what does "hash-collision probability approximates softmax attention weight" actually claim? Where does TransAct v2's 16k sequence sit in this lineage?
- **DQ-F2** (target 3 · `bandits-exploration-exploitation`, `recsys-beyond-accuracy`) — The exploratory module as a bandit. What is the arm, what is the reward, and why does Thompson sampling versus UCB matter under delayed feedback at Pinterest scale? What does interest collapse look like in production, and what did frontier sampling change?
- **DQ-F3** (target 4 · `recsys-beyond-accuracy`, `data-flywheel`) — Retentive recommendations. Define the retention objective you would optimize, explain why pUIC is a proxy for it, and describe the feedback-loop trap: what breaks when the model trains on exposures it chose? What is your team's answer, and what would a skeptic say is still unmeasured?
- **DQ-F4** (target 3 · `personalization-patterns`) — Cold and low-frequency users: where does the behavior model run out, what does a text LLM add offline (interest summaries, pseudo-labels), and why should it never sit in the request path? Tie it to the NLFU commitments.

### Cluster G — Agents and evaluation
*Concepts: `ai-agents-and-agentic-systems` (seed 3), `agent-harnesses-and-self-evolution` (2), `llm-evaluation` (3), `prompt-engineering` (2), `retrieval-augmented-generation` (2)*

- **DQ-G1** (target 3 · `llm-evaluation`) — Reflex's judge. What must an LLM-as-judge be calibrated against, how did you ground automated results in human evaluation, and which judge failure modes (position, verbosity, self-preference) have you actually seen? What does GEPA change about calibration?
- **DQ-G2** (target 3 · `agent-harnesses-and-self-evolution`) — The harness papers you collected: AutoHarness, EvoHarness, SkillOS, WikiSkill, context-as-environment. State the shared thesis in one sentence. Which single idea would you take into Reflex Evolve first, and what is its dated kill criterion?
- **DQ-G3** (target 4 · `ai-agents-and-agentic-systems`) — Describe Leo's instinct system as a memory architecture: what is stored, how confidence moves, what is deliberately not automated and why. What would an EvoRec-style self-evolving loop need before it could be trusted to edit that memory?
- **DQ-G4** (target 2 · `retrieval-augmented-generation`, `prompt-engineering`) — Leo's KB is TF-IDF over 2,400 documents with a frozen graph. Where does that fail you, what would embedding-based retrieval fix, and why did you defer it? What in your prompting practice would you now call a pattern rather than a habit?

### Cluster H — Relevance-2 sweep (one probe each, level-2 check)
- **DQ-H1** (`llm-post-training`, `rl-for-llms`) — DPO versus GRPO in one minute each. What is OneRec's iterative preference alignment, and why is its +1.6% watch time a ranking result rather than a retrieval one?
- **DQ-H2** (`data-quality`) — FineWeb-Edu's lesson applied to interaction logs: design the quality classifier and the fixed-compute ablation for one LWS training slice. What would count as a positive result, and how does it relate to the unimpressed dataset?
- **DQ-H3** (`search-systems`) — Hybrid lexical plus dense retrieval, and why relevance and engagement objectives conflict more in P2P and Search CLR than in Homefeed. How does UBR's second design principle answer Kurchi's concern?
- **DQ-H4** (`distributed-training`, `distributed-systems`) — What does FSDP shard, when do you need sequence or context parallelism, and what would a 1B-parameter teacher on your data actually require that the current trainer lacks?
- **DQ-H5** (`vision-language-models`) — PinClip and OmniSage as item content: what does CLIP-style contrastive training give you and what does it miss for recommendation? Where do LLM-generated captions help and where do they leak popularity bias?
- **DQ-H6** (`reasoning-models`, `llm-hallucination`) — Test-time compute and "thinking" recommenders: why is this outside a 10 ms retrieval budget, and what is the one place reasoning could still enter your stack offline?

---

## After each sitting

1. The evaluator writes every graded concept with `set ... --kind practice` and a note that quotes the phrase that earned or cost the level. Unanswered questions write nothing.
2. Run `python3 scripts/kb_knowledge_state.py queue` and compare with the seed queue of 18. The difference is what the quiz found.
3. Record the cursor (next question id) in `self/learning/learning_progress.md`; the `learn` skill resumes from there.
4. After sitting 3, note in the agenda whether the 14-week sequence still matches the queue, and adjust the sequence, not the model.
