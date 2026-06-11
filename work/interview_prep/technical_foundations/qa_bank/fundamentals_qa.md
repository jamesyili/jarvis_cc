# Fundamentals Q&A — depth probes with model answers

**How to use:** answer cold (out loud), *then* check the key. If your answer missed the **bold** load-bearing phrase, re-read that guide section. Comprehensive coverage, module by module (01–08). Current as of 2025-era methods (GRPO, MLA, ultra-sparse MoE, agentic RL). Anchors to your work are noted so you can bridge to a built system.

> Format per item: **Q** → model answer. Pair with the 90-second spoken versions in each guide's §5/§7.

---

## 01 — Representation Learning & Embeddings

**Q1. What is an embedding, and why is learning the space the hard part?**
A learned map from a raw object (token, pin, user) to a dense vector where **geometry encodes meaning**. Once you have a good space, retrieval = nearest-neighbor, ranking = dot product, clustering = k-means — all cheap. **Most of the value and cost is in the representation; downstream heads are cheap.** That's the foundation-model thesis and your UPP three-tier thesis in one line.

**Q2. Write the InfoNCE/contrastive loss and explain each term.**
$\mathcal{L} = -\log \frac{e^{q\cdot k^+/\tau}}{e^{q\cdot k^+/\tau} + \sum_{k^-} e^{q\cdot k^-/\tau}}$. It's **softmax cross-entropy where the "classes" are items**: pull the anchor $q$ toward its positive $k^+$, push from negatives $k^-$. Temperature $\tau$ controls how hard the separation is (low $\tau$ = sharper).

**Q3. Why are in-batch negatives biased, and what's the fix?**
In-batch negatives sample items proportional to their frequency, so **popular items appear as negatives too often** → the model under-ranks them at serving. Fix = **logQ / sampled-softmax correction**: subtract $\log(\text{sampling prob})$ from the logit (Yi et al. 2019, "sampling-bias-corrected"). Naming this signals you've actually trained retrieval.

**Q4. In-batch vs hard negatives — what does each teach?**
Random/in-batch negatives teach **coarse** structure (cheap, batch-size-bound). **Hard negatives** (plausible-but-wrong) teach **fine** discrimination — they're where most retrieval quality comes from. Mining them well is the core craft.

**Q5. Why two towers for retrieval instead of one cross-encoder?**
Because the item tower is **precomputed and ANN-indexed**; at serving you run only the query tower, then approximate-NN. A cross-encoder is more accurate but must score every item per request — infeasible at retrieval scale. **Cross-encoders return at the ranking stage**, where the candidate set is small.

**Q6. How do you know an embedding is "good"?**
**Recall@K / MRR** against held-out positives; **alignment & uniformity** (positives close AND space used evenly — collapse = everything maps to a few points = useless); **linear-probe** a frozen embedding for a labeled factor; then **online A/B**. (See guide 06.)

**Q7. What makes OmniSage special as a representation?**
It **fuses three signals** — CLIP visual + co-engagement graph + pin-board topology — so **closeness = functional utility, not visual similarity**. A hiking boot and a granola bar are neighbors via "camping" boards. The geometry does the work a taxonomy used to.

**Q8. How would you handle cold-start in an embedding-based system?**
**Synthetic profiling** (your RR Strategy D): match a low-signal user's fragment to a mature synthetic cluster aggregated from similar users; plus lean on **content features in the item tower** (so new items embed without interaction history) and reserve **exploration slots**.

**Q9. Map "user-level next-token prediction" (UPP FM) to the LLM recipe.**
Sequence = the user's action history (L500); tokens = actions/items; objective = causal next-action prediction; the learned per-position vector = the **user representation** base models consume. Same self-supervised recipe as GPT, applied to behavior.

**Q10. Isn't this all just word2vec?**
Same family (co-occurrence → geometry). The modern moves are the **fusion of heterogeneous signals** (OmniSage), the **self-supervised sequence objective** (next-token), and **scale** (billion-item contrastive with hard negatives + popularity correction).

---

## 02 — Transformers & Attention

**Q1. Write scaled dot-product attention and explain it in one breath.**
$\text{softmax}(QK^\top/\sqrt{d_k})V$. Each position emits a **query**, scores it against every position's **key** (similarity / soft nearest-neighbor), softmaxes into weights, and reads out a blend of **values**. **Attention is differentiable retrieval over the sequence.**

**Q2. Why the $\sqrt{d_k}$ scaling?**
Without it, dot products grow with dimension and **saturate the softmax** toward one-hot, killing gradients. Scaling keeps the distribution soft and trainable.

**Q3. Why multi-head?**
One head can express only one weighting. **Parallel heads on subspaces** learn different relations (syntax, coreference, position). Concatenate and project.

**Q4. What does the causal mask do, and why is it required?**
Zeros attention to future positions so token $t$ sees only $\le t$. This makes **next-token prediction well-posed** (no peeking) — it's exactly the UPP FM setup over user actions.

**Q5. Why do transformers need position encodings? What does RoPE buy?**
Attention is **permutation-invariant**, so order must be injected. **RoPE (rotary)** rotates Q/K by position so *relative* distance lives in the dot product — generalizes to longer contexts better than learned absolute embeddings.

**Q6. State attention's complexity and two consequences.**
$O(n^2 d)$ in sequence length — **quadratic**. Consequences: long context is expensive, and it drives the whole KV-cache / attention-variant toolbox.

**Q7. "Attention is quadratic" — what's wrong with that as a 2025 claim?**
It's the **2017 picture**. Frontier models are sub-quadratic: KV-cache compression along **MHA → MQA → GQA → MLA** (GQA = Llama/Mistral/Gemma default; MLA = DeepSeek low-rank KV), plus sliding-window/linear attention. **FlashAttention is separate — it doesn't lower $O(n^2)$, it makes it IO-efficient on-GPU.** Don't conflate them.

**Q8. Walk MHA → MQA → GQA → MLA — what does each step buy?**
MHA caches one K/V *per head* (expensive). **MQA** shares one K/V across *all* heads (cheap, slight quality hit). **GQA** shares K/V within $G$ groups (the sweet spot, open-weights default). **MLA** low-rank-compresses the KV into a small latent (DeepSeek). Each shrinks the KV cache for cheaper long-context decode.

**Q9. Encoder-only vs decoder-only — when each?**
Encoder-only (BERT) = bidirectional, for **embeddings/classification**. Decoder-only (GPT/Claude/Llama) = causal, for **generation** — the dominant LLM architecture.

**Q10. Why is generation slow?**
Quadratic attention + **memory-bound autoregressive decoding** (each token streams weights + growing KV from memory). The KV cache amortizes recompute; batching amortizes the weight load. (Guide 07.)

---

## 03 — Pretraining, Fine-tuning & Transfer

**Q1. Why does pretrain-finetune beat training task-specific models from scratch? What are you amortizing?**
You **learn a general representation once** on cheap, abundant, self-supervised data, then adapt cheaply with scarce labels — **amortizing the expensive representation across every downstream consumer**. Labels are scarce; raw sequences are abundant and self-labeling.

**Q2. Name the self-supervised objectives and which model family each suits.**
**Next-token/autoregressive** (GPT, UPP FM) → generation. **Masked** (BERT) → bidirectional embeddings. **Contrastive** (CLIP, OmniSage) → similarity/retrieval spaces.

**Q3. State the Chinchilla rule and when the optimum shifts.**
For a fixed compute budget, scale params and tokens together — **~20 tokens per parameter** (compute-optimal). If you'll **serve** the model heavily, over-train a *smaller* model past compute-optimal (cheaper inference) — the optimum shifts smaller.

**Q4. What is catastrophic forgetting, and three mitigations?**
Fine-tuning **overwrites pretrained knowledge**. Mitigate with low learning rate, **replaying pretraining data**, freezing lower layers, or **LoRA/PEFT** (train small adapters, freeze the base).

**Q5. When pretrain vs fine-tune vs prompt/RAG?**
Prompt/RAG when the base **already knows it** (cheapest). Fine-tune when you need a **behavior/format reliably**. Pretrain/continue-pretrain only when the **domain distribution is genuinely off** — the bar your org cleared for *users* (generic text models don't represent user behavior).

**Q6. Map the UPP three-tier hierarchy onto pretrain → base → surface.**
**Foundation Model** (user-level next-token pretraining, shared) → **base retrieval/ranking** (CLR / CFM, fine-tuned by task) → **surface models** (fine-tuned per surface: HF, Notif, Search, P2P). BERT→task-heads, in recsys.

**Q7. Cross-surface transfer "isn't hurting but isn't helping." How do you diagnose?**
Separate **a measurement problem from a generalization problem**: (1) is the offline eval even *measuring* transfer? If so, more engineers won't help. (2) If the eval is right and it still doesn't transfer, it's **negative/weak transfer to that target** — accept and reframe. Different fixes; diagnose before staffing. (Your live P2P call.)

**Q8. What do scaling laws actually buy a decision-maker?**
They turn "how big a model / how much data" from a guess into a **budgeted, predictable decision** — you forecast a big run's loss from small runs, which is how labs derisk billion-dollar training. EM altitude: judgment, not FLOP arithmetic.

**Q9. SFT vs RLHF — what can each teach?**
SFT (imitation on demonstrations) teaches **format, task-following, refusals** — but can't rank among many acceptable answers. RLHF (preference) teaches **which** good answer is wanted. (Guide 05.)

**Q10. Why is "data the real differentiator"?**
Architecture is largely commoditized; the **data pipeline** (filtering, dedup, mid/post-training curation, contamination control) is the moat and the largest lever on quality. Ties to eval validity (guide 06).

---

## 04 — Retrieval, Ranking & Two-Tower

**Q1. Why is recommendation a cascade? Draw it.**
You can't score billions with your best model under a latency budget, so you **progressively filter**: retrieval (L0, ANN, →thousands) → preranking (L1/LWS, cheap, →hundreds) → main ranking (L2, expensive multi-task, →tens) → post-ranking (blending/diversity). Cheaper-coarser upstream, expensive-precise downstream.

**Q2. State the preranking alignment/accuracy decomposition (your paper).**
The preranking objective decomposes into exactly two components (**exclusivity**): **alignment** = overlap with the main ranker's selections, **accuracy** = conditional engagement above a shared ranker threshold. They **combine linearly** (linearity result), calibrated by regressing online lift on the two.

**Q3. Why measure alignment on the *unimpressed* pool, not impressed traffic?**
Impressed data is **biased toward what already survived to exposure**, so it can't recover the true alignment term — it reweights toward seen positions and mixes in exposure effects. Switching to unimpressed moved offline winner-prediction **70%→80%** in your experiments.

**Q4. What is Sample Selection Bias (SSB) in preranking, and three fixes?**
L1 is **trained on impressed items but serves on the much larger post-CG pool** — "an exam beyond the syllabus" (train/serve distribution shift). Fixes: include **unimpressed items as negatives**, **p-select labels** (was it in L2 output?), **KD from the L2 teacher**.

**Q5. Why ANN not exact NN at L0? Why two-tower not cross-encoder at L0?**
Exact NN over 10⁹ vectors per request is infeasible — **ANN** (HNSW/FAISS) trades a little recall for huge speed. Two-tower lets you **precompute+index** the item side; a cross-encoder can't be precomputed, so it only survives on the small post-retrieval set.

**Q6. What is calibration, how do you measure it, and why does multi-objective ranking break without it?**
A predicted p(action)=0.1 must mean 10% empirically. Measure with **O/E ratio** (decile reliability tables) and **ECE**. Multi-objective ranking combines heads via a **utility = Σ wᵢ·p(actionᵢ)**; if heads are miscalibrated the weighted sum is meaningless (your Reflex ranker_calibration_audit does per-segment O/E across 8 heads).

**Q7. How do you combine multiple objectives at the ranking stage?**
Predict **multiple heads** (repin, closeup, click, hide…) — often a shared bottom with task towers (MMoE-style gating) — then a **utility function** combines calibrated head predictions into one score; the weights encode product strategy (your blender_utility work).

**Q8. How does CLR use a UIC vector?**
CLR is a **conditional** two-tower retriever: the UIC medioid (or a predicted coordinate) is a **conditioning input** that steers retrieval toward the interest cluster you're serving. It's the bridge from Anticipation's geometric prediction to retrieval, and cutting overfetch via UIC-conditioning saved ~$322k/yr.

**Q9. Map a RAG pipeline onto the cascade.**
**Embed → ANN retrieve (L0) → optional rerank (a small L2 cross-encoder) → stuff context → LLM generate.** Same recall/precision trade your paper formalizes; failure modes (recall miss, stale index, retriever/reranker disagreement) = your alignment problem.

**Q10. Offline metric improved but online didn't — what's happening?**
Offline↔online correlation failure. Likely **alignment measured on the biased impressed set**, or an accuracy metric (PR-AUC) that doesn't track lift — in your Table 1, PR-AUC predicted the winner **backwards**. Fix: choose theory-justified metrics and **calibrate them against online lift**. (Guide 06.)

**Q11. Post-ranking — what does diversity/blending do?**
Merges multiple candidate sources (presort → diversity → SSD → final chunk) and optimizes the feed as a **set** — inter/intra-cluster diversity + reserved exploration slots — not just top-N by score.

---

## 05 — RLHF, Preference Optimization & Reward Modeling

**Q1. Why is alignment a reward-design problem, not a labeling problem?**
You can't write down "the answer you want" as labels — the target is a **subjective preference**, often only expressible as "A > B." So you **learn a reward from comparisons, then optimize against it** — and the central risk is the gap between the learned proxy and true preference (Goodhart with a gradient).

**Q2. Draw the three-stage RLHF pipeline.**
**SFT** (imitate demonstrations) → **reward model** (Bradley-Terry on pairwise comparisons) → **RL** (PPO maximizes reward **minus a KL penalty to the SFT reference**). The SFT model is also the reference policy.

**Q3. Write the Bradley-Terry RM loss. What is the RM architecturally?**
$\mathcal{L} = -\log\sigma(r(x,y_w) - r(x,y_l))$ — maximize the probability the preferred response scores higher. The RM is usually **the LM with the token-head swapped for a scalar head**.

**Q4. Why the KL penalty in PPO? Two concrete reward-hacking behaviors without it.**
KL keeps the policy near the **trusted reference** so it can't drift into adversarial high-RM-but-garbage outputs. Without it: **verbosity, sycophancy, keyword-stuffing** — high RM score, low true value.

**Q5. DPO vs classic RLHF — what does DPO remove, and what do you give up?**
DPO **folds the RM and RL loop into a closed-form policy loss** on preference pairs (the policy is its own implicit reward model). Simpler, more stable, no RM serving. You give up a **reusable, inspectable RM** and can over-fit the preference set.

**Q6. When is KTO the right call?**
When you only have **unpaired binary feedback** (thumbs-up/down), not ranked pairs. KTO uses a prospect-theory utility loss and **obliterates the paired-comparison requirement** — far cheaper labeling, directly relevant to integrity data collection.

**Q7. RLVR — what makes a reward "verifiable," and why does it kill RM-hacking?**
The reward is a **ground-truth check** (tests pass? math correct?) rather than a learned proxy — so there's no imperfect RM to hack. Powers reasoning models (o-series, DeepSeek-R1). The reward-design problem mostly disappears *where you can verify*.

**Q8. PPO vs GRPO — what does GRPO remove, and how does it estimate the advantage?**
GRPO **drops the value/critic network**. It samples a **group of G outputs** per prompt and computes the advantage as **(reward − group mean)/group std** — group-relative scoring instead of a learned baseline. Cheaper, less memory, more stable at reasoning scale; the DeepSeek-R1 default. Successors (DAPO/GSPO/CISPO) fix long-CoT instability.

**Q9. What's RLAIF / Constitutional AI?**
Replace/augment human feedback with **AI feedback** — a model critiques/ranks against a written **constitution** of principles. Scales preference collection past human throughput; Anthropic's public reference and the substrate of constitutional classifiers.

**Q10. Explain Thompson sampling with your Geometric Bandit. Why log-lift not raw CTR?**
Maintain a **Beta posterior per (user, embedding-region)**; at serving **sample** from each and act on the sample, so uncertain regions get explored without a hand-tuned epsilon. Reward = **log-lift** (momentum vs the user's baseline) so a high-volume stale interest can't crowd out a low-volume growing one — a deliberate reward-design choice against degeneration.

**Q11. The field is moving along two axes — name them.**
**Reward axis**: learned-proxy → verifiable (where checkable) → AI-feedback (where not). **Optimizer axis**: PPO → critic-free (GRPO and successors). Either way the reward-design problem moves, it doesn't vanish.

---

## 06 — Evaluation, Simulation & Validity

**Q1. Eval has three jobs in increasing difficulty — name them.**
**Measure** (compute a number — easy), **correlate** (make it predict the online outcome — hard), **validate** (keep it predictive under distribution shift and optimization pressure — hardest; contamination/Goodhart live here).

**Q2. ROC-AUC vs PR-AUC — when does each lie, which for harm detection?**
ROC-AUC is **optimistic under heavy class imbalance**; for **rare positives (harm, fraud) use PR-AUC**. Saying this unprompted signals shipped imbalanced classifiers.

**Q3. Offline metric improved, online didn't — give three causes and how to distinguish.**
(1) **Offline↔online correlation failure** — the metric doesn't track lift (calibrate against online lift); (2) **distribution mismatch** — measured on biased (impressed) data (re-measure on the serving distribution); (3) **novelty effect** — temporary spike (run the A/B longer). Distinguish by checking the metric-vs-lift regression and the data distribution.

**Q4. What is eval *validity* vs *measurement*? Use the UPP P2P case.**
Measurement = the number is computed correctly. Validity = the number **measures the thing you care about**. P2P transfer looked flat — the first question was validity: *is the offline eval even capturing cross-surface transfer?* If it's a measurement-design problem, **more engineers won't fix it.**

**Q5. What is contamination, three controls, and how does a forward-test-set help?**
Benchmark data leaking into pretraining makes the score fiction. Controls: **dedup, canary strings, temporal holdouts**. A **forward-in-time test set** (train Jul–Dec, test Mar–Apr — your preranking paper) guards against both contamination and distribution shift.

**Q6. Why hold guardrail metrics neutral, and which ones?**
A win you ship **must not move a harm/health guardrail** — recsys: WAU, hide rate, report rate (your preranking A/B held all neutral); safety system: over-blocking rate, appeal rate, fairness gaps. You don't trade an engagement win for a harm regression.

**Q7. What makes a *safety* eval different from a capability eval?**
It must be **adversarial and distribution-shifted** — it passes right up until someone attacks the system. Capability evals measure typical-case skill; safety evals must measure worst-case behavior under an adversary and drift.

**Q8. LLM eval methods and their failure modes.**
**Perplexity** (intrinsic, weak), **benchmarks** (MMLU/GSM8K/HumanEval/safety — contamination-prone), **LLM-as-judge** (scalable but **position/verbosity/self-preference bias**), **human** (gold, slow/expensive). Triangulate; don't trust one.

**Q9. What is offline policy evaluation / replay, and its limit?**
Estimate a new policy's value from **logged data** without shipping (counterfactual/off-policy). Limit: logs only cover actions the **old policy took** — coverage bounds validity. Reflex's Simulate stage + BuildValidator-vs-real-PRs is replay-against-ground-truth.

**Q10. How does the Reflex Skeptic stay calibrated?**
It reads its own **verdict_log** to track precision (human-agreed rate) and adjusts confidence — an evaluator **monitoring its own validity against fresh human labels**. Good answer to "how do you keep an automated evaluator honest."

---

## 07 — Inference & Serving Economics

**Q1. Prefill vs decode — which is compute-bound, which memory-bound, and the metric each sets?**
**Prefill** processes the whole prompt at once — **compute-bound**, sets **TTFT**. **Decode** generates one token at a time — **memory-bandwidth-bound** (streams weights + growing KV per token), sets **throughput**.

**Q2. What is the KV cache, why does it exist, what does it constrain, one way to shrink it?**
Stores past keys/values so each new token is $O(n)$ not $O(n^2)$. It **grows with batch × sequence length** and often becomes the binding constraint on concurrency. Shrink via **GQA/MQA** (share K/V across heads) or **MLA** (low-rank compression).

**Q3. List the cost levers and what each trades. First move?**
**Quantization** (precision→memory/speed — usually the first move), **distillation** (big teacher→small student), **pruning** (sparsity→speed), **MoE** (params↑, active-FLOPs flat), **batching** (latency↔throughput), **caching** (recompute→memory), **speculative decoding** (draft+verify).

**Q4. Why is a retrieval model two-tower — as an inference-economics decision?**
To **precompute and index the static item side** so you only compute the query side live (then ANN). It's the recsys analogue of caching K/V — don't recompute the static part per request.

**Q5. What is MoE, and why are frontier models adopting it?**
Replace the dense FFN with $N$ expert FFNs + a router sending each token to top-$k$ — **per-token compute scales with active experts, capacity with total experts** (sparsity = total/active). Buys more parameters without more per-token FLOPs. DeepSeek-V3 (671B/37B), Kimi K2 (1.04T/32B), Mixtral (8×top-2) are all MoE.

**Q6. What's the hard part of MoE?**
**Load balancing** — without it, "rich-get-richer" expert collapse. Classic fix = auxiliary load-balancing loss (Switch); modern = **auxiliary-loss-free balancing via dynamic per-expert biases** (DeepSeek-V3), which avoids competing with the LM objective. Plus all-to-all communication overhead in expert-parallel training.

**Q7. "Make this cheap to serve" — your playbook.**
**Distill a smaller student → quantize → batch (continuous batching) → cache (prefix/semantic) → put it first in a cascade** so the expensive model only sees what survives. (= your LWS/funnel logic; = a fast distilled safety classifier in front of an expensive one.)

**Q8. What's online/offline feature skew and why does it bite?**
Features computed differently in **training (offline) vs serving (online)** → you train on a distribution you can't serve. Fix: compute the same features both paths (or a unified feature store like GSS). Classic production failure.

**Q9. What does MLA do specifically?**
DeepSeek's **Multi-head Latent Attention** down-projects K/V into a small **latent vector** that's cached (with a RoPE component kept separate), then up-projects — drastically shrinking the KV cache while preserving quality. The current frontier of KV compression.

---

## 08 — Agents, Tool Use & Multi-Agent

**Q1. What turns a chat model into an agent? Name the three additions.**
A **loop + tools + state**: the model **acts (tool calls), observes results, and decides the next step** until a goal is met — with memory persisting across steps. Autonomy traded for reliability.

**Q2. Workflows vs agents (Anthropic's distinction)?**
**Workflows** orchestrate LLMs + tools through **predefined code paths**; **agents** let the LLM **dynamically direct its own process**. Most reliable production "agents" are actually workflows — predefined paths are auditable and bounded. Reflex is workflow-end on purpose.

**Q3. Name the four canonical agentic design patterns and map Reflex to them.**
**Reflection** (Skeptic — self-critique/refute), **Tool Use** (playbooks/MCP), **Planning** (PM decomposes), **Multi-agent Collaboration** (PM/DS/Skeptic/Curator roster).

**Q4. Why is adversarial verification the highest-leverage reliability pattern?**
Errors **compound**: a 90%-reliable step run 10× is ~35% end-to-end. An **independent critic that tries to refute** the proposer catches plausible-but-wrong outputs a single agent rubber-stamps — Reflex's Skeptic.

**Q5. Why is agent evaluation different from model evaluation?**
You must grade the **trajectory, not just the output** — did it use the right tool, stay in budget, avoid the destructive action. The **dangerous failures are in the path**, and output-only eval misses them. Agent eval is still largely unsolved.

**Q6. How do you let an agent modify production safely?**
**Bound the blast radius**: allowlist of writable paths + **magnitude caps** (diff caps, rate limits) + **human gate** on risky actions — Reflex's BuildValidator (allowlist + 150-line diff cap, signed off).

**Q7. MCP vs A2A?**
**MCP (Model Context Protocol)** standardizes agent↔tools/data; **A2A (Agent-to-Agent)** standardizes agent↔agent. Reflex reaches Presto/Slack/Asana over MCP; Pinkerton is an A2A-style callable agent.

**Q8. Why do long agent runs fail, and how do you mitigate?**
**Compounding error** + **reward hacking over the horizon** (more steps = more room to satisfy the metric while missing intent). Mitigate with **short loops, decomposition, and verification** at each step.

**Q9. How do you ground an agent?**
Feed it **real structured state** (your UIC-as-dynamic-prompt → "next best action") and **tools that return ground truth**, not the model's guesses. Grounding is exactly where free-running agents struggle.

**Q10. What's the training frontier for agents?**
**Agentic RL / tool-integrated reasoning**: agents are increasingly *trained* — RL over multi-step tool-use trajectories with **verifiable rewards** (RLVR/GRPO applied to agents) — not just prompted. Most candidates miss that the frontier is *RL on agents*.

---

## Cross-cutting integrative questions (the senior signal)

**Q1. In one sentence, how are a recsys, a foundation model, an LLM, and an agent the same machine?**
All four are **Represent → Retrieve/Rank → Generate/Decide → Learn-from-feedback** — and **attention is the differentiable, in-sequence version of the retrieval primitive** you build at billion-item scale.

**Q2. Where does "the value and the cost" sit in any of these systems, and what follows?**
In the **representation** — downstream heads are cheap. So the architecture question is always *what's the shared representation, who owns it, and how do consumers specialize on top* — the foundation-model and UPP-platform thesis.

**Q3. Name three "the naive metric lies" traps across the stack.**
**Popularity bias** in in-batch negatives (retrieval), **alignment-on-impressed** (preranking), **contamination / ROC-AUC under imbalance** (eval). In each, the convenient metric mis-ranks; you fix it by choosing the theory-justified measurement.

**Q4. Where does RLHF show up outside chat models?**
Recsys **feedback loops** (your Geometric Bandit = contextual-bandit RL), Reflex's **human-correction loop** (preference signal → policy update with auditable state), and **agentic RL**. Reward design is the common hard part.
