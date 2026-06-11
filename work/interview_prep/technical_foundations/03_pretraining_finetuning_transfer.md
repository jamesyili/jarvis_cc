# 03 — Pretraining, Fine-tuning & Transfer

> **Bridge:** This is your blog topic *and* your org's whole thesis. UPP's three-tier hierarchy — Foundation Model → base CLR/CFM → surface fine-tunes — is the foundation-model paradigm applied to users. You can speak the pretrain→finetune story from production, including its *failure mode* (cross-surface transfer that doesn't generalize — the P2P stall), which is a more credible answer than the textbook version.
> **Book:** Ch 13–14 (scaling laws), Ch 20–22 (data), Ch 26 (SFT), Ch 30 (pretraining run).

---

## 1. The core idea

Pretraining and fine-tuning is a **factoring of the learning problem**: learn a *general-purpose representation once* on cheap, abundant, self-supervised data; then *adapt it cheaply* to many specific tasks with small labeled datasets. You amortize the expensive part (representation) across every downstream consumer.

Why this dominates: labels are scarce and expensive; raw sequences (text, user actions) are abundant and self-labeling (the next token *is* the label). So you spend your compute budget learning structure from the abundant signal, and spend your scarce labels only on the last-mile adaptation. **The org-design consequence is the part you live:** *whoever owns the foundation model owns the leverage, and surfaces specialize on top.* That is the UPP platform thesis and the frontier-lab business model in one sentence.

---

## 2. The stack (every stage, in order)

| Stage | Data | Objective | Teaches |
|---|---|---|---|
| **Pretraining** | huge, raw, self-supervised | next-token / masked / contrastive | general representation, world structure |
| **Mid-training** | curated domain + long-context | continued next-token | domain skew, longer context |
| **SFT** | small, curated (prompt, ideal-response) | imitation | format, task-following, refusals |
| **Preference alignment** | comparisons | RLHF / DPO (guide 05) | which good answer is wanted |

### Self-supervised objectives (the engine of stage 1)
- **Autoregressive / next-token** (GPT, UPP FM) — predict the next element. The dominant objective; directly gives a generative model.
- **Masked** (BERT) — predict held-out elements from both sides; good for bidirectional *embeddings*, not generation.
- **Contrastive** (CLIP, SimCLR; OmniSage) — pull augmented/positive pairs together (guide 01).

### Scaling laws (interview vocab, not arithmetic)
- **Performance is a smooth power law** in model size, data, and compute — you can *predict* a big run's loss from small runs. This is why frontier labs derisk billion-dollar runs.
- **Chinchilla / compute-optimal:** for a fixed compute budget, scale params and tokens *together* — the rule of thumb is **~20 training tokens per parameter**. Earlier models (GPT-3) were oversized and under-trained.
- **Inference-aware:** if you'll serve a model a lot, *over*-train a smaller one past compute-optimal (Llama-style) — cheaper to serve. Know that the optimum shifts when you price in serving. (Connects to guide 07.)
- EM-altitude takeaway: *"scaling laws turn 'how big a model / how much data' from a guess into a budgeted decision."* Don't re-derive FLOP counts; the book itself says interviewers want judgment, not arithmetic.

### Fine-tuning / transfer mechanics
- **Full fine-tune** — update all weights; best quality, expensive, risks **catastrophic forgetting** (overwriting pretrained knowledge). Mitigate with low LR, mixing in pretraining data, or freezing lower layers.
- **PEFT / LoRA** — train small low-rank adapters, freeze the base. Cheap, many task-specific adapters over one base. Know it exists and why (cost, multi-tenant).
- **Transfer is not free.** A representation pretrained on distribution A may not help task B if the gap is too large — *negative transfer*. This is exactly your P2P story (below): cross-surface pretraining was *at least not hurting*, but proving it *helps* is a separate, harder question.

---

## 3. Your anchor: UPP three-tier + cross-surface transfer

### The hierarchy is the paradigm
```
[Foundation Model]  user-level next-token pretraining (one, shared)
        │ fine-tune
   ┌────┴────┐
[Base Ranking]   [Base Retrieval]      ← CFM (ranking), CLR dual-tower (retrieval)
   │ fine-tune        │ fine-tune
[Surface rankers] [Surface retrievers]  ← HF, Notif, Search, P2P
```
*"Pretrain a general user representation once; base models specialize by task (rank vs retrieve); surface models specialize by surface."* — this is BERT→task-heads, said in recsys.

### Cross-surface transfer — the live, honest version
- **The win:** the "shared base + surface-specific fine-tune" thesis is *empirically fed* on Notif — three sequenced launches, the latest **+200k WAU**, compounding. Pretrained HF base → Notif fine-tune → DHEN scaling shipped real lift.
- **The hard part (and the credible interview beat):** P2P cross-surface pretraining is "**at least not hurting**" but the narrative needs "**improving**." Two debates you can articulate cleanly: (1) is the *eval methodology* even measuring transfer correctly — if so, more engineers won't help (guide 06); (2) even with correct eval, does the bet *generalize* to P2P, or is this a case where transfer doesn't hold? **Being able to say "transfer is an empirical question per target, and here's how I'd tell a measurement problem from a generalization problem" is a senior answer most candidates can't give** — because they've only ever seen transfer work in a paper.

### Double-duty: this is your blog post
Blog post #1 is pretrain-finetune in recsys. UPP is that paradigm *shipping in production with CTO-visible momentum.* You can't name UPP, but the authorial confidence comes from watching it work at scale — and writing it sharpens the exact muscle an interviewer probes.

---

## 4. The frontier-lab connection

- The entire modern LLM is this stack: pretrain (guide 02 architecture) → mid-train → SFT → align (guide 05). You now hold the whole pipeline.
- **Build vs buy vs fine-tune vs prompt** is the EM judgment call this guide arms: prompt/RAG when the base already knows it; fine-tune when you need a behavior/format reliably; pretrain/continue-pretrain only when the domain distribution is genuinely off (the bar your org cleared for *users*, which generic text models don't represent).
- **Data is the real differentiator** (Hoang Part VIII): filtering, dedup, contamination. The model architecture is commoditized; the data pipeline is the moat. Tie to guide 06 (contamination = eval validity).

---

## 5. Interview-portable (90 seconds)

> *"Pretrain-finetune is a factoring: learn a general representation once on cheap self-supervised data, then adapt cheaply with scarce labels — so you amortize the expensive part across every consumer. My org runs this for users: a foundation model pretrained with user-level next-token prediction, base retrieval and ranking models fine-tuned from it, and surface models fine-tuned per surface. The win is real — we've shipped compounding cross-surface transfer onto Notifications. The part I'd stress in an interview is the failure mode: transfer is an empirical question per target. On one surface our cross-surface pretraining is 'not hurting' but we can't yet prove it 'helps,' and the first thing I do there is separate a measurement problem — is the eval even capturing transfer — from a generalization problem, because they have completely different fixes. On scaling, I treat the laws as a budgeting tool — compute-optimal is roughly twenty tokens per parameter, and the optimum shifts smaller if you're going to serve it a lot."*

**Likely probes:**
- "When pretrain vs fine-tune vs prompt?" → distribution gap + reliability need + label budget; prompt/RAG cheapest, pretrain only when the domain is genuinely off-distribution.
- "Catastrophic forgetting?" → low LR, replay pretraining data, freeze lower layers, or LoRA.
- "How big a model / how much data?" → scaling laws, compute-optimal ~20:1, adjust for serving cost.
- "How do you know transfer helped?" → held-out eval *on the target*, ablate the pretrained init, watch for negative transfer (your P2P discipline).

---

## 6. Self-test (out loud, from memory)

1. Why does pretrain-finetune beat training task-specific models from scratch? What exactly are you amortizing?
2. Name the self-supervised objectives and which model family each suits (generation vs embedding).
3. State the Chinchilla rule and why the optimum shifts when serving cost matters.
4. What is catastrophic forgetting and three ways to mitigate it?
5. Map the UPP three-tier hierarchy onto pretrain → base → surface. What's the self-supervised objective at the top?
6. Cross-surface transfer "isn't hurting but isn't helping." How do you tell a measurement problem from a generalization problem?

*Shaky on 1–3? Hoang Ch 13–14 (skim) + Ch 26. 5–6 are your UPP docs.*
