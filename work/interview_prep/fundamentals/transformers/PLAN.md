# Transformers — Two-Phase Learning Plan (OOO 2026-06-08 → ~06-23)

**Constraints:** Phase 1 = iPhone-only, **no laptop / no code execution**, ~45–60 min/day, **on-demand** (James pulls via remote control — no scheduled push). Reading via emailed MD; reflection written in iPhone Notes → pasted to chat for feedback. At computer ~June 23 → Phase 2 (hands-on).

**Structure:** three streams, done **sequentially and completely** — **Stream 1 fully, then Stream 2, then Stream 3.** (Not rotated.)

**Resource decisions:**
- **Raschka, _Build an LLM from Scratch_ → Phase 2 only** (it's the code spine; don't buy for the code-free phase).
- **RLHF book = Nathan Lambert, _The RLHF Book_ (rlhfbook.com), James has the PDF** → powers **Stream 3**; also feeds Reflex RL work.
- Phase 1 lessons are **self-contained MD** — no book dependency.

**Format per Phase-1 module:** ~15 min read (emailed MD) + ~30–40 min in-chat Socratic quiz + a Notes reflection → I log a learning-record and advance the ZPD.

---

## Phase 1 — Away (iPhone, code-free) · Knowledge + reasoning

### ▶ Stream 1 — Training theory (FIRST, do completely) — your `llm_fundamentals` roadmap
- **1.1** Positional encoding: sinusoidal → RoPE  · `lessons/0003`  ← **start here**
- **1.2** The training objective: cross-entropy, perplexity, teacher forcing, what pretraining optimizes
- **1.3** Optimization that converges: AdamW, warmup + cosine, weight decay, gradient clipping
- **1.4** Stability: residuals / pre-norm, initialization, what makes training blow up
- **1.5** Decoding & KV-cache: sampling, the cache, serving cost

### Stream 2 — Recsys applications (SECOND)
- **2.1** Next-token → next-item: the loss change & sampled softmax  · `lessons/0002` *(already delivered — do it when we reach Stream 2)*
- **2.2** SASRec vs BERT4Rec as *training* problems (causal vs cloze; negatives dominate architecture)
- **2.3** Training a ranking transformer: BCE + future-action loss (TransAct v2 / CFM)
- **2.4** Pretrain → finetune for recsys (UPP FM→CFM; the transfer spectrum; LoRA conceptually)
- **2.5** CFM scaling as a research question (fixed-FT-budget transfer; design + interview framing)

### Stream 3 — Post-training & RLHF (THIRD) — uses your RLHF PDF; feeds Reflex
- **3.1** The post-training landscape: pretrain → SFT → RLHF / preference optimization
- **3.2** Reward models & preference data (engagement = implicit preference signal)
- **3.3** PPO vs DPO, conceptually (→ Reflex RL path)
- **3.4** RLHF ↔ recsys: RL for ranking, reward shaping, the Reflex angle

**Sequence:** 1.1 · 1.2 · 1.3 · 1.4 · 1.5 · 2.1 · 2.2 · 2.3 · 2.4 · 2.5 · 3.1 · 3.2 · 3.3 · 3.4. (~14 modules ≈ the 2.5 weeks.)

---

## Phase 2 — At computer (~June 23+) · Hands-on
> Get Raschka here if you want the code spine. Pairs with `rasbt/LLMs-from-scratch` + nanoGPT.

- **P2-1** Run nanoGPT / Raschka Ch5 — train a tiny GPT; watch loss → `log V`
- **P2-2** Overfit one batch + the debugging recipe (Karpathy) — break & fix on purpose
- **P2-3** Reading loss curves — diverge / plateau / overfit; LR sweeps
- **P2-4** Implement next-item training (sampled softmax) — toy SASRec
- **P2-5** Add a ranking head + BCE + future-action loss — toy TransAct/CFM
- **P2-6** LoRA finetune — replicate the CFM-scaling ablation shape (LoRA vs freeze+quant)
- **P2-7** Capstone: an end-to-end train → finetune → eval you can narrate in an interview

---

## How to pull (Phase 1, on-demand)
Ping me with any of:
- **"next"** — advances the sequence above (now → 1.1, then 1.2, …)
- a specific code — **"1.3"**, **"2.2"**, etc.

I email the MD + we quiz in chat. Write reflections in Notes, paste them to me. I email an updated **backup bundle** whenever the workspace changes.
