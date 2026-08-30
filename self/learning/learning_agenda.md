# Learning Agenda — LLM×RecSys + Reflex (14-Week Program)

Created: 2026-08-30 (replaces the Q2 2026 five-track agenda → `archive/learning_agenda_2026Q2.md`)
Owner: James
Status: live · **Weeks dated Mon 8/31 → Sun 12/6, 2026** · review at week 7 and week 14

**Why this program exists.** The 8/15 ruling: *I choose the LLM×recsys frontier, because it's where my time disappears — and I don't need anyone's building to pursue it.* This is that choice made executable. Goal is **judging depth**, not implementation mastery: interrogate a RecGPT-class proposal at parity, review the team's fine-tuning like an expert, reason about serving cost without borrowing opinions, and design Reflex's feedback loops from first principles.

**The learning law (8/15, binding):** learning-for-use flows; learning-for-the-badge grinds. Every week below names the live decision it feeds. If a week ever stops connecting to a real decision, flag it in session — don't push through.

**Time budget:** ~3 hrs/week dedicated + ambient on-the-job. Substrates: Colab/toy repos (primary hands-on) · work-leo exercises (prompts written here, run at work) · Leo-as-lab (judge/eval exercises on Leo's own logs).

**Deliberately excluded:** pretraining at depth and interview drilling — that's lab-bar prep, gated on the calm-week test (~mid-Sept). If the bar activates, it gets added *as* bar prep, honestly labeled. Old non-technical tracks (Claude Code mastery, eng leadership, ML system design) continue ambiently, not as curriculum.

**Companion system (carried over):** concept notes as individual `.md` files in this folder (what I understand / nuances / still working through / how it shows up in my work); learning events logged in session logs. Weekly checkbox = crossable, scoreboard-style.

**Source verification note:** all URLs verified via live search Aug 2026 by four research agents; a few domains couldn't be fetched directly from the research sandbox (kipp.ly, bbycroft.net, eugeneyan.com, netflixtechblog, yuan-meng.com) — confirmed via multiple independent citations. If a URL 404s, title-search it.

---

## The five areas and their live decisions

| Area | Weeks | Live decision it feeds |
|---|---|---|
| 1 · Generative retrieval / semantic IDs | 1, 4-5, 8-10 | **GenRet/RecGPT owner decision (November)** · LWS×UPP integration fork · holding parity with ATG and Karthik (DE) |
| 2 · Post-training practice | 6-7 | **HF fine-tuning iterations (live now, Piyush/Zihao)** · distillation-to-serving path |
| 3 · Transformer internals | 2-3 | Foundation for areas 1-2; capability claims judgment |
| 4 · Inference economics | 11-12 | **GPU-serving productionization push** · the cost line |
| 5 · RL for agents + evals | 13-14 (+stretch) | **Curator/Skeptic improvement plan** (eval_09 six-idea menu) · any "RL-train our agent" proposal |

---

## Week-by-week

### ☐ W1 · Aug 31 – Sep 6 — The generative-recommendation map
- Lesson: `lessons/w01_generative_rec_map.html` (interactive — the three-meanings map, RQ-VAE walked with real numbers, the terminology glossary, production-evidence ledger)
- Watch: Eugene Yan, AI Engineer 2025 keynote — https://www.youtube.com/watch?v=YxpwskHTtkc (35 min, warm-up)
- Read: Yuan Meng, "Is Generative Recommendation the ChatGPT Moment of RecSys?" — https://www.yuan-meng.com/posts/generative_recommendation/ (~2 hrs; the single best on-ramp — TIGER → HSTU → OneRec with skepticism intact)
- **Output:** one page naming the three things people mean by "generative recommender" — (a) semantic-ID generative retrieval (TIGER), (b) sequential transduction at scale (HSTU), (c) end-to-end cascade replacement (OneRec) — and which one RecGPT actually is. *(work-leo: file it where the November decision prep lives.)*

### ☐ W2 · Sep 7 – 13 — Training dynamics: what actually changes the weights
*(Re-aimed 8/30 against LR-0001: the forward pass is known cold — attention math, multi-head, RoPE, SASRec/BERT4Rec, TransAct/CFM/CLR mappings. The genuine gap is training mechanics. Do NOT re-watch attention explainers.)*
- Lesson: `lessons/w02_training_dynamics.html` (interactive — optimization, loss-curve diagnosis, recsys training specifics: sampled softmax, in-batch negatives, LogQ)
- Build: Karpathy, "Let's build GPT" — https://www.youtube.com/watch?v=kCc8FmEb1nY — **watch for the training loop, not the attention block**: loss → backward → step, then train the Shakespeare model and read its loss curve (~2 hrs; Colab)
- **Exit test:** given a loss curve + config, diagnose stalled vs diverging vs overfitting, and explain what warmup and clipping each protect against.

### ☐ W3 · Sep 14 – 20 — Generation mechanics: decoding, beam search, KV cache
- Lesson: `lessons/w03_generation_mechanics.html` (interactive — sampling/temperature, beam search + constrained decoding over a valid-ID trie, KV-cache arithmetic; the direct bridge to TIGER in W4 and serving econ in W11)
- Explore: bbycroft.net 3D LLM visualization — https://bbycroft.net/llm (~45 min; locate K and V, note their shapes and why the cache is per-token)
- **Exit test:** given (layers, heads, d_model), write the parameter count; given a beam width and SID vocabulary, sketch how constrained decoding keeps generation valid.

### ☐ W4 · Sep 21 – 27 — Generative retrieval: the founding papers
- Read: TIGER, "Recommender Systems with Generative Retrieval" — https://arxiv.org/abs/2305.05065 (~2 hrs; internalize content embedding → RQ-VAE codes → seq2seq, and what Amazon-Beauty benchmarks do NOT prove)
- Read: "Better Generalization with Semantic IDs" (YouTube ranking, RecSys 2024) — https://arxiv.org/abs/2306.08121 (~1 hr; the cheapest useful SID adoption — SIDs as features in the existing ranker — the baseline a full generative rewrite must beat)
- **Output:** concept note on RQ-VAE / semantic IDs — including the cold-start honesty question.

### ☐ W5 · Sep 28 – Oct 4 — Hands-on: build the toy generative retriever
- Run: EdoardoBotta/RQ-VAE-Recommender — https://github.com/EdoardoBotta/RQ-VAE-Recommender — on MovieLens 1M, end-to-end (~3 hrs over two sittings; Colab/laptop)
- Inspect **by hand**: codebook utilization, collision rates, what happens to an item's SID when the RQ-VAE retrains. The failure modes (dead codes, collisions, unstable IDs) become tangible — more judging depth per hour than any paper.
- **Output:** three observed failure modes, written down; they become review questions verbatim.

### ☐ W6 · Oct 5 – 11 — Post-training I: the pipeline at manager altitude
- Watch: Karpathy, "Deep Dive into LLMs" — https://www.youtube.com/watch?v=7xTGNNLPyMI — SFT section onward at 1.5x (~75 min; his "SFT = imitation, RL = practice" framing is the vocabulary)
- Read: Nathan Lambert, The RLHF Book — https://rlhfbook.com/ — intro + SFT + preference-data chapters (~1 hr; navigate from TOC, chapter numbering shifts)
- Skim: Raschka, "New LLM Pre-training and Post-training Paradigms" — https://magazine.sebastianraschka.com/p/new-llm-pre-training-and-post-training (~30 min)
- **Exit test:** whiteboard pretraining → SFT → RM/preference → RL and say what each stage's data looks like. **Use immediately:** the reviewer's checklist (Appendix B) at the next HF fine-tuning review with Piyush/Zihao.

### ☐ W7 · Oct 12 – 18 — Post-training II: run a LoRA fine-tune yourself
- Read: Raschka, "Practical Tips for Finetuning LLMs Using LoRA" — https://magazine.sebastianraschka.com/p/practical-tips-for-finetuning-llms (~40 min; extract the r/alpha/target-modules rules of thumb first so nothing is cargo-culted)
- Run: Unsloth SFT notebook (Qwen3-4B or Llama-3.1-8B), free Colab — https://github.com/unslothai/notebooks + guide https://unsloth.ai/docs/get-started/fine-tuning-llms-guide — stock first, then swap in a custom dataset (300–1,000 examples shaped like the team's task; e.g., query+item → relevance judgment) and retrain (~2 hrs attention)
- **Output:** a model you personally fine-tuned + visceral sense of what r/alpha/LR/epochs feel like. *(Leo-as-lab option: fine-tune on Leo session-log style transfer instead.)*
- **Mid-program review:** is the 3 hrs/week holding? Is each week feeding a real decision? Adjust here, not silently.

### ☐ W8 · Oct 19 – 25 — Generative recommendation at scale (the HSTU pole)
- Read: HSTU, "Actions Speak Louder than Words" — https://arxiv.org/abs/2402.17152 — §1-3 + scaling/deployment + M-FALCON serving sections (~2 hrs; skim kernels); slides: https://icml.cc/media/icml-2024/Slides/32684.pdf
- Read: Shaped.ai HSTU explainer — https://www.shaped.ai/blog/is-this-the-chatgpt-moment-for-recommendation-systems (~45 min; author-reviewed)
- Skim: Wukong scaling law — https://arxiv.org/abs/2403.02545 (~30 min: intro, curves, conclusion)
- Optional background: kick off meta-recsys/generative-recommenders ml-1m quickstart — https://github.com/meta-recsys/generative-recommenders — and compare HSTU vs SASRec HR@10 yourself
- **Exit test:** a crisp answer to "do recsys models scale like LLMs?" (power laws exist but are architecture-contingent; sequence models scale, DLRMs need surgery; exponents shallower than language).

### ☐ W9 · Oct 26 – Nov 1 — Production evidence and the honest tradeoffs
- Read: OneRec V1 — https://arxiv.org/abs/2506.13695 (full) + V2 architecture/deployment — https://arxiv.org/pdf/2508.20900 (~2 hrs; note how modest the online wins are vs. the infra spend)
- Read: LIGER, generative-vs-dense head-to-head — https://arxiv.org/abs/2411.18814 (~1 hr; **the bridge paper for a two-tower veteran** — dense still out-ranks pure generative; the hybrid mitigates cold-start)
- Skim: MTGR (Meituan) cross-feature ablation — https://arxiv.org/abs/2505.18654 (~30 min; the strongest documented counterargument to "throw away the feature stack")
- **Output:** two-column ledger — reported online wins vs infra cost/complexity, cited by paper.

### ☐ W10 · Nov 2 – 8 — The prosecutor's file (GenRet decision-ready)
- Read: PinRec — https://arxiv.org/abs/2504.10507 (~1 hr; generative retrieval on the surfaces you built — benchmark every claim against memory); teardown companion: https://www.shaped.ai/blog/pinrec-teardown-inside-pinterests-production-ready-generative-retrieval-model
- Read: GRID practitioner's handbook (Snap) ablations — https://arxiv.org/abs/2507.22224 (~1 hr; many "critical" SID components matter less than claimed)
- Skim: cold-start reproducibility study — https://arxiv.org/abs/2603.29845 · synerise HSTU critique (baseline hygiene) — https://sair.synerise.com/basemodel-vs-meta-ais-hstu-for-sequential-recommendations/ · Netflix foundation-model pair — https://netflixtechblog.com/foundation-model-for-personalized-recommendation-1a0bd8e02d39 + https://netflixtechblog.medium.com/integrating-netflixs-foundation-model-into-personalization-applications-cf176b5860eb · Eugene Yan's written survey as consolidation — https://eugeneyan.com/writing/recsys-llm/
- **Output (the point of the whole area):** your personal judging checklist, tuned to RecGPT — seed from Appendix A. *(work-leo: this walks into the November decision and any ATG review.)*

### ☐ W11 · Nov 9 – 15 — Inference economics I: the arithmetic
- Work by hand: kipp.ly, "Transformer Inference Arithmetic" — https://kipp.ly/transformer-inference-arithmetic/ (~1.5 hrs; do every calculation for one model you own numbers for)
- Read: Baseten ops:byte guide — https://www.baseten.co/blog/llm-transformer-inference-guide/ (~40 min; redo its math for your fleet's GPUs)
- Read: Anyscale continuous batching — https://www.anyscale.com/blog/continuous-batching-llm-inference (~40 min; be able to redraw the two diagrams)
- **Exit test:** calculations 1–4 of Appendix C from memory.

### ☐ W12 · Nov 16 – 22 — Inference economics II + capability judgment
- Read: JAX ML Scaling Book, "All About Transformer Inference" — https://jax-ml.github.io/scaling-book/inference/ (~1.25 hrs, do the quizzes)
- Read: Grootendorst, "A Visual Guide to Quantization" — https://www.maartengrootendorst.com/blog/quantization/ (~45 min; keep the comparison table)
- Read: Character.AI serving cost posts — https://blog.character.ai/optimizing-ai-inference-at-character-ai-2/ + part deux (~30 min; for each technique, one line on whether it applies to an LLM-in-recsys path)
- Read: "chinchilla's wild implications" — https://www.lesswrong.com/posts/6Fpvch8RR29qLEWNH/chinchilla-s-wild-implications (~45 min; then answer why Llama-3 trained past Chinchilla-optimal)
- **Exit test:** calculations 5–8, especially #8 — the LLM-in-the-ranking-path feasibility math. *(work-leo: bring to the GPU-serving push.)*

### ☐ W13 · Nov 23 – 29 — **Thanksgiving week (PTO stick honored): light + flex**
- Catch-up buffer for anything slipped, plus light reading only:
- Read: Jay Alammar, "The Illustrated DeepSeek-R1" — https://newsletter.languagemodels.co/p/the-illustrated-deepseek-r1 (~30 min; the map for W14)
- Read: Shunyu Yao, "The Second Half" — https://ysymyth.github.io/The-Second-Half/ (~20 min; evaluation now dominates algorithms — the frame for Reflex)
- Nothing else. The org works through your PTO; so does the curriculum.

### ☐ W14 · Nov 30 – Dec 6 — RL for agents: rewards, hacking, and evals
- Read: RLHF Book — Reward Models + Policy Gradients chapters (~90 min; work the GRPO advantage equation by hand for a group of 4 — why no value network, and what that costs)
- Read: Raschka, "The State of RL for LLM Reasoning" — via https://sebastianraschka.com/blog/ (~45 min, intro half)
- Read: Lilian Weng, "Reward Hacking in RL" — https://lilianweng.github.io/posts/2024-11-28-reward-hacking/ (~40 min, RLHF sections) + METR, "Recent Frontier Models Are Reward Hacking" — https://metr.org/blog/2025-06-05-recent-reward-hacking/ (~30 min; for each transcript, name the harness flaw that allowed it)
- **Output:** half-page memo — *"how would Reflex's verdict pipeline get Goodharted?"* — this is direct input to the Curator/Skeptic plan. **Exit test:** explain GRPO in 5 minutes without notes.

### Stretch (December, unscheduled — pick by pull, not obligation)
- **The judge-calibration exercise (highest value, Leo-as-lab or work-leo):** take 30 traces from Reflex's `verdict_log.jsonl` (or Leo's logs), hand-label pass/fail, write a judge prompt, measure judge–human agreement with Cohen's kappa per Eugene Yan's recipe — https://eugeneyan.com/writing/llm-evaluators/
- Anthropic, "Demystifying Evals for AI Agents" — https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents (~45 min; audit one Reflex harness against its component checklist) + Hamel Husain's evals FAQ as standing reference — https://hamel.dev/blog/posts/evals-faq/
- Unsloth GRPO notebook — https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide — run it, then **deliberately weaken the format reward and watch the model exploit it**: reward hacking reproduced on your own GPU
- Agentic RL survey — https://arxiv.org/abs/2509.02547 (intro + MDP formalization + self-improvement/memory sections) · credit-assignment survey — https://arxiv.org/pdf/2604.09459 (problem setup; why "just run GRPO on our agent" usually fails) · Meta "Early Experience" — https://arxiv.org/pdf/2510.08558 (the bridge from the memory literature you already know to RL)
- Thinking Machines, "On-Policy Distillation" — https://thinkingmachines.ai/blog/on-policy-distillation + Pinterest search-relevance distillation — https://medium.com/pinterest-engineering/improving-pinterest-search-relevance-using-large-language-models-4cd938d4e892 (the reference architecture for the team's teacher→student path) + "Let's Verify Step by Step" — https://arxiv.org/abs/2305.20050 and the Qwen PRM lessons corrective — https://arxiv.org/pdf/2501.07301

---

## Appendix A — Judging questions for a generative-recommendation proposal

**Semantic IDs / RQ-VAE:** (1) ID stability under catalog churn — retrain cadence, migration path, what fraction of items change SIDs? (2) Codebook health at 10⁸–10⁹ items — utilization, collision rate, disambiguation? (3) Cold-start honesty — measured lift on cold slices vs the cheap alternative of SIDs-as-features in the existing ranker? (4) Where does collaborative signal enter a content-derived ID space?

**Generative vs two-tower:** (1) Show the generative-vs-tuned-two-tower head-to-head on our data, same candidate budget, first. (2) p99 latency and cost per 1k requests for beam search vs one ANN lookup at our QPS — does constrained decoding fit? (3) Beam search concentrates mass — what's the diversity/dedup mechanism, and how are policy/contractual items guaranteed retrievable? (4) What serves the request when the model emits an invalid SID?

**HSTU-style "delete the feature stack":** (1) Which cross features does this discard, and the ablated cost of each (MTGR: scaling doesn't recover them)? (2) Baseline hygiene — production ranker with full features and tuning, or an academic SASRec? Who tuned the baseline? (3) Show the compute-vs-quality curve on *our* data — what exponent, and where does it cross the current model? (4) Streaming/incremental training — a batch-retrained generative model can be *worse* at freshness than the online-learned stack.

**Cascade replacement (OneRec-style):** (1) Kuaishou's headline is ~0.5% stay time after enormous spend — what lift on what metric justifies this here, at what MFU/cost? (2) Where do the cascade's between-stage knobs (policy, ads load, integrity) live in a single model, and what's the reward model's failure mode? (3) Can it launch behind the existing ranker (retrieval-only, PinRec-style) or is it all-or-nothing?

**LLM-as-ranker/feature-factory:** (1) Tuned or frozen, and is a conventional model still in the serving path? Production evidence favors LLMs offline (features, labels, distillation) over online. (2) Did you compare against distilling the LLM's signal into the existing model — the pattern that actually ships?

## Appendix B — Reviewer's checklist for fine-tuning work

**Data:** (1) Where did every example come from, who/what labeled it, what's the label error rate — did anyone hand-read a random 100? (2) Contamination checked against every eval, including the online holdout (temporal leakage counts)? (3) What's the mix, and what did removing each slice do? No mixture ablations = folklore.

**Method:** (4) Was more/better SFT data tried before preference methods? DPO earns its keep on "fluent but wrong preference," not "can't do the task." (5) Where do preference pairs come from and how on-policy are they? KTO if you only have thumbs, not pairs. (6) Why LoRA vs full FT — r, alpha, target modules, measured (not assumed) quality gap?

**Eval:** (7) What's the held-out suite nobody model-selected against? (8) LLM judge validated against human ratings, different model family than the generator, length-bias checked? (9) Overfit/degradation signals — response-length drift, diversity collapse, regression on untargeted capabilities? (10) What would reward-hacked look like here, concretely? If nobody can tell the story, nobody looked.

**Serving:** (11) Path from checkpoint to latency budget — distill to what student, on-policy or off, quantized how, measured quality drop per step (Pinterest writeup = reference shape)? (12) Online A/B tied to the offline eval, drift monitoring, versioned data+configs, rollback?

## Appendix C — The 8 back-of-envelope calculations (from memory by W12)

1. **KV cache/token** = 2 × layers × kv_heads × head_dim × bytes. (Llama-3-70B FP16 ≈ 320 KB/token → 8K context ≈ 2.6 GB *per concurrent sequence* — why MQA gave Character.AI ~8x, and why batch×context, not weights, caps concurrency.)
2. **Model memory** = params × bytes (70B FP16 = 140 GB — doesn't fit one H100; INT4 = 35 GB — does).
3. **Batch-1 decode ceiling** ≈ memory bandwidth / bytes-per-token (70B FP16 on H100 ≈ 24 tok/s; FP8 ≈ 48) — decode is memory-bound; quantization ≈ linear decode speedup.
4. **Memory- vs compute-bound crossover:** GPU ops:byte (H100 ≈ ~300) vs workload arithmetic intensity — the one number explaining why prefill is cheap/token, decode expensive, and batching is the whole game.
5. **Cost per M tokens** = $/hr ÷ (tokens/sec × 3600) × 10⁶ — utilization, not list price, is the lever.
6. **Training FLOPs** ≈ 6 × params × tokens; inference ≈ 2 × params/token; Chinchilla ≈ 20 tok/param — and at high inference volume you over-train a smaller model instead.
7. **When quantization pays:** weight-only when decode is weight-bandwidth-bound (small batch); KV-cache quantization when batch×context rivals weights (long histories, high concurrency — i.e., recsys).
8. **LLM-in-ranking-path feasibility:** prefill ≈ 2 × params × prompt_tokens FLOPs. 1B over 2K-token history ≈ ~8 ms on H100 @50% MFU — fits 100 ms; 70B ≈ ~560 ms — doesn't. Recsys twist: no cross-request KV reuse on per-user histories, but scoring N candidates against one cached history amortizes (M-FALCON).

## Appendix D — The 10 design questions for any self-improvement loop

(1) Where does reward come from — verified or learned? A learned judge is a proxy that WILL be optimized against. (2) Outcome, process, or both — and who checks the checker? PRM-as-reranker ≫ safer than PRM-as-training-signal. (3) What gets credit over a 40-turn trajectory with one terminal reward? (4) How would it get hacked — can the agent see/modify/route around the grader; can it flatter the judge? (5) Are weight updates needed at all, or does memory/context suffice? (Memory improvement is reversible, auditable, cheap — weight updates need recurring cross-context failures + thousands of graded trajectories.) (6) Is the environment stationary and resettable — same task twice, fair trial? (7) Signal per dollar — enough within-group reward spread for GRPO to learn at all? (8) Judge calibration — kappa (not raw %) against how many human labels, re-checked as criteria drift? (9) What degrades off the metric, and what holdout tripwires catch it? (10) The null hypothesis — would better prompts/tools/base model beat the loop at 10% of the cost?

---

**Provenance:** built 2026-08-30 from four deep-research passes (generative retrieval · post-training · transformers+serving · RL-for-agents), each briefed on the profile (20-yr recsys, judging-depth goal, 3 hrs/wk, learn-by-doing) with URL verification. Sequencing owned by Leo: GR before the November gate, PT while HF fine-tuning is live, serving before year-end GPU decisions, RL/evals feeding the Curator/Skeptic plan.
