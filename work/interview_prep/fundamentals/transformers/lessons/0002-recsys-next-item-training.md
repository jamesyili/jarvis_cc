# Stream 2 · Module 2.1 — From next-token to next-item

*Transformers › Stream 2 (recsys) › ~45–60 min › read on phone, work in Notes + chat*
*(Delivered early — do this one when we reach Stream 2, after Stream 1 is complete.)*

> **Mission tie-in.** This is the single concept that turns "I understand LLM training" into "I can reason about how we train SASRec / the FM / CFM." It's also the most common ML-system-design question in your lane: *"How would you train a model to recommend from a billion-item catalog?"*

---

## The one idea

Training a sequential recommender is the **same four-step loop** you learned in Lesson 01 — forward → loss → backward → update. **Only sub-step 1 (the loss) changes.** But that one change is the whole game in recsys, because it's where the catalog's scale and the negative-sampling problem live.

If you remember nothing else: **everything hard about training a recommender lives in the loss term.** Forward, backward, and AdamW are identical to an LLM.

---

## Why the LLM loss doesn't transfer directly

In language, the loss is cross-entropy over the vocabulary:

`loss = −log softmax(logits)[correct token]`

The softmax denominator sums over the vocabulary `V` — for GPT-2, `V ≈ 50,257`. Cheap.

In recsys, the "vocabulary" is the **item catalog**: millions to billions, and it **changes every day**. Now the softmax denominator must sum over *every item in the catalog, every step*:

`p(item) = exp(score_item) / Σ_over_ALL_items exp(score)`

That denominator is **computationally impossible** per training step. This is the central departure — and notice *where* it lives: it's sub-step 1 of the loop, the `F.cross_entropy(...)` line. Nothing else about training changed.

---

## The fix: sampled softmax / negative sampling

You don't normalize over the whole catalog. You score the **true next item** (the positive) against a **small sampled set of negatives**, and treat it as a much smaller classification problem:

`loss ≈ −log[ exp(s⁺) / ( exp(s⁺) + Σ_sampled exp(s⁻) ) ]`

Two sources of negatives, used together:

- **In-batch negatives** — the positives of *other users in the same batch* serve as your negatives. Free (already in memory), and the trick behind two-tower retrieval training.
- **Sampled negatives** — drawn from the catalog, usually by popularity.

Because you sampled (rather than summed over everything), the scores are biased toward frequent items. You correct this with a **logQ correction** — subtract `log Q(item)` (the sampling probability) from each score, so popular items aren't unfairly penalized. (Yi et al. 2019, the sampling-bias-corrected two-tower paper.)

---

## The lesson that matters more than the math: negatives dominate

Here's the strategic point, and it's the one your own notes already make:

- The SASRec replication finding (in your `transformers-for-recsys.html`): SASRec trained with sampled softmax / proper negatives **matches or beats BERT4Rec** — i.e. *the loss and the negatives often matter more than the encoder architecture.*
- **Hard negatives beat random negatives.** The best hard negatives are **impressions** — items the user *saw in a well-ranked feed and chose not to engage*. Those teach the model fine distinctions; random negatives are too easy.

Now connect it straight to UPP, because this is exactly why your FM/CFM story is shaped the way it is:

- **FM pretraining has no impressions logged** → no hard negatives → it can only do a future-action (next-item-ish) loss, and "can't be trained well with pointwise ranking losses." That limitation you documented **is a negatives problem in sub-step 1.**
- **CFM / surface models train on tabularml with impressions** → they *have* hard negatives → they can add the **BCE ranking loss** on top. The difference between "FM" and "a ranker" is, fundamentally, *what's available in the loss term.*

That's the through-line: **FM vs CFM is a sub-step-1 (loss + negatives) distinction**, not a forward-architecture one.

---

## Interview frame (say it in this order)

> "Train a retrieval model over a billion-item catalog?" → **Two-tower** (user tower + item tower), score = dot product. Train with **in-batch negatives + popularity-sampled negatives**, **logQ correction** for sampling bias, and **hard negatives (impressions)** where available. Serve via **ANN/HNSW**. The transformer is the user tower; the loss is where all the design lives.

---

## Your work (the 45–60 min) — answer in Notes, paste the starred ones to me

1. Full softmax over the catalog is infeasible. State **the cost per step** and **which line of the training loop** it lives in. (One sentence each.)
2. **★** You're getting great offline recall but mediocre online ranking. Your negatives are all random in-batch. **What do you change, and why?**
3. **★** Map it to FM vs CFM: **why can FM only do a future-action loss and not a pointwise ranking (BCE) loss?** (Hint: it's not the architecture.)
4. **logQ correction** — in one sentence, what bias is it fixing?

**Reflection (write in Notes):** In exactly 3 sentences, "how training a recommender differs from training an LLM." Force yourself to say *only sub-step 1 changes, and here's how.*

**Reply to me with #2 and #3.** I'll push on your reasoning, then log a learning-record and advance to **2.2 — SASRec vs BERT4Rec as training problems**.

---

*Sources: SASRec (Kang & McAuley 2018); Yi et al. 2019 "Sampling-Bias-Corrected Neural Modeling for Large Corpus Item Recommendations" (in-batch negatives + logQ); your `artifacts/transformers-for-recsys.html` (Parts 2–3, 6) and `work/projects/upp/cfm_technical.md` (FM-vs-CFM loss/negatives).*
