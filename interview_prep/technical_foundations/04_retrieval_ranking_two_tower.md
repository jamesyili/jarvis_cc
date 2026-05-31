# 04 — Retrieval, Ranking & Two-Tower Systems

> **Bridge:** This is your strongest whiteboard, full stop. You ship billion-item retrieval (CLR), you co-authored a **first-principles preranking framework** (alignment + accuracy), and you have published retrieval/ranking papers (KDD'25 multi-embedding retrieval, WWW'26 cross-user ranking). When an interviewer says "design a recommendation / search / RAG-retrieval system," you are not reasoning from a blog post — you are reporting from production and from your own papers. **Lead here.**
> **Book:** recsys-native (the Hoang book under-serves this); pairs with Ch 29 (serving) and §1's "attention is retrieval."

---

## 1. The core idea: the cascade funnel

You cannot score every item with your best model — billions of candidates, a few-hundred-millisecond budget. So you build a **cascade**: each stage is cheaper-but-coarser upstream, more-expensive-but-precise downstream, and each stage's only job is to hand the next stage a good enough candidate set.

```
corpus (10^8–10^9)
   │  L0  RETRIEVAL        recall-oriented; ANN over embeddings; "don't lose the good ones"
   ▼      (→ ~thousands)
   │  L1  PRERANKING/LWS   cheap scorer; ALIGN with the ranker under tight latency
   ▼      (→ ~hundreds)
   │  L2  MAIN RANKING     expensive multi-task scorer + utility; the precision stage
   ▼      (→ ~tens)
   │  POST-RANKING         blending, diversity (SSD), business rules
   ▼      final feed (~tens)
```

The governing insight — **the one you can prove because you wrote the paper:** *each stage should optimize agreement with the stage below it, not raw accuracy in isolation.* A preranker that's "more accurate" on engagement labels but disagrees with the main ranker wastes the ranker's capacity. This reframes the whole problem from "make each model accurate" to "make the funnel coherent."

---

## 2. Stage by stage (the fundamentals, with your anchors)

### L0 — Retrieval (two-tower + ANN)
- **Two-tower** (guide 01): user/query tower + item tower, trained contrastively so engaged pairs score high; item vectors **precomputed and indexed**; serve = run the query tower live → **ANN** search (HNSW / FAISS / ScaNN) over the index.
- **Why ANN, not exact:** exact nearest-neighbor over 10⁹ vectors per request is infeasible; ANN trades a little recall for orders-of-magnitude speed. Know HNSW (graph-based) exists; don't derive it.
- **Negative sampling is the quality knob:** in-batch negatives (cheap, batch-size-bound), **hard negatives** (plausible-but-wrong, where fine discrimination is learned), and the **logQ / sampled-softmax correction** for in-batch popularity bias (your "Sampling-Bias-Corrected Neural Modeling" reference [22] is the canonical paper).
- **Your anchor — CLR (Conditional Learned Retrieval):** a two-tower retriever that takes the **UIC medioid as a *conditioning* input** — retrieval is steered by *which interest cluster / predicted coordinate* you're serving. This is the bridge from Anticipation (predict a point in embedding space) to retrieval (fetch around that point). **Overfetch** (fetching more than you'll use) is the cost knob; cutting it via UIC-conditioning saved ~$322k/yr — a concrete infra-efficiency story.

### L1 — Preranking / LWS (your paper)
This is where you have a *framework*, not just experience. The preranking objective decomposes into exactly two things (no third independent scalar is needed — the **exclusivity** result):
- **Alignment** = overlap with the main ranker's selections (does L1 keep what L2 would pick?). Measured as **overlap@K, computed on the *unimpressed* candidate pool** — not impressed traffic, because impressed data is biased toward what survived to exposure. *This distinction — measure alignment on unimpressed — is the paper's load-bearing, counterintuitive result, and it's exactly the kind of "I know why the naive metric lies" insight that lands in an interview.*
- **Accuracy** = conditional engagement above a shared ranker threshold (among items L2 would rank similarly, does L1 favor the ones users actually engage?).
- **Combine linearly** (the **linearity** result justifies the ubiquitous linear metric/loss combos), calibrated by regressing online lift on (M_align, M_acc).
- **Training:** keep the production accuracy branch unchanged; *add* an alignment branch — **KD (KL distillation from the L2 teacher) + a weighted pairwise loss** — on the unimpressed distribution. Result: +1.43% save vs accuracy-only; switching alignment data from impressed→unimpressed alone moved offline winner-prediction 70%→80%.
- **Sample Selection Bias (SSB) is the central villain:** L1 is *trained* on impressed items but *serves* on the post-CG pool — "an exam beyond the syllabus." Fixes: include unimpressed items as (hard/easy) negatives, p-select labels, KD from L2. Know this cold — it's the recsys analogue of *train/serve distribution shift*.

### L2 — Main ranking (multi-task + utility)
- **Multi-task / multi-objective:** predict many heads (repin, closeup, click, save, hide, long-click…), often a shared bottom with task towers (**MMoE**-style gating). One model, many engagement predictions.
- **Utility function:** combine head predictions into one score via a weighted **utility** — `utility = Σ wᵢ · p(actionᵢ)`. The weights encode product strategy (your Reflex **blender_utility** work tunes exactly these). This is how a recsys turns many probabilities into one ranking.
- **Calibration is non-negotiable:** a predicted p(repin)=0.1 must mean 10% empirically, or the utility sum is garbage. Measure with **O/E ratio** (observed/expected, decile-binned reliability tables) and **ECE**; your Reflex `ranker_calibration_audit` does per-segment O/E across **8 production ranker heads**. Miscalibration by segment is a top source of hidden quality bugs.

### Post-ranking — diversity & blending
- **Blending pipeline** (your Reflex blender_reference): presort → diversity → **SSD (sequential/stochastic diversity)** → final chunk. Multiple candidate sources get merged into one feed.
- **Diversity** = inter-cluster (don't show ten near-identical pins) and intra-cluster, plus reserved slots for exploration (your RR "enticement" clusters). The feed isn't just top-N by score; it's a *set* optimized for satisfaction + diversity + business rules.

---

## 3. The unifying picture (and the RAG bridge)

- **RAG is this funnel with two stages and an LLM stapled on the end:** embed → ANN retrieve → (optional rerank) → stuff context into the LLM. When a frontier-lab interviewer asks about RAG, you're describing L0 (+ a reranker = a small L2) that you've built at far larger scale. The failure modes they care about — recall misses, stale index, reranker/retriever disagreement — are *literally your alignment problem*.
- **Reranking = cross-encoder** (the accurate, can't-scale model) applied only to the small candidate set L0 returned. Two-tower for recall, cross-encoder for precision — the same precision/efficiency trade your paper formalizes.

---

## 4. Whiteboard discipline (repair the Anthropic loop here)

This is the guide where the system-design anti-patterns bite, so bake the fixes in:
1. **Clarify the objective + the funnel first.** "What are we optimizing — engagement, relevance, safety? What's the latency budget and candidate scale?" Then draw the cascade. (Framework: `system_design/00_FRAMEWORK.md`.)
2. **Depth-then-breadth.** Don't list all four stages shallowly. Pick the interesting one (usually L0 negative sampling or L1 alignment) and go three levels deep, *then* surface.
3. **Lead with the trade-off, not the metric.** "Here's the precision/recall and FP/FN trade-off at this stage and who pays" before "here's the AUC."
4. **Name the data-distribution traps unprompted** — SSB, popularity bias, offline/online gap. Naming them is the senior signal.
5. **Resolve the hard case end-to-end** (a cold-start user, an adversarial item, a calibration drift) — don't leave it dangling.

---

## 5. Interview-portable (90 seconds)

> *"At scale you can't score everything, so recommendation is a cascade: ANN retrieval recalls thousands, a lightweight preranker cuts to hundreds, a heavy multi-task ranker scores tens, then diversity and blending build the final set. The non-obvious part — and I co-authored a paper formalizing this — is that each stage shouldn't maximize its own accuracy; it should maximize *agreement with the stage below it*. We proved the preranking objective decomposes into exactly two things, alignment and accuracy, that they combine linearly, and — the counterintuitive bit — that alignment has to be measured on the *unimpressed* candidate pool, because impressed data is biased toward whatever already survived to exposure. The villain throughout is sample-selection bias: every stage trains on a distribution narrower than the one it serves on, which is the recsys version of train/serve shift. On the retrieval side specifically I work on a conditional two-tower model that takes a user-interest-cluster vector as a steering input, with hard-negative mining and popularity-corrected in-batch negatives — and RAG is just a two-stage version of this with an LLM on the end."*

**Likely probes:**
- "Why two-tower for retrieval but a heavy model for ranking?" → precompute+ANN at recall scale; cross-encoder precision only survives on the small set.
- "How do you sample negatives?" → in-batch + hard negatives + logQ correction; SSB → include unimpressed.
- "Your offline metric improved but online didn't — why?" → offline/online gap; alignment-on-impressed lies; calibrate offline metric against online lift (your paper's whole point).
- "Cold start?" → synthetic profiling (RR Strategy D); content features in the item tower; exploration slots.
- "How do you combine multiple objectives?" → multi-task heads → utility weights; calibration (O/E) so the weighted sum is meaningful.
- "Design RAG retrieval." → embed → ANN → rerank; recall vs precision; index freshness; retriever/reranker alignment.

---

## 6. Self-test (out loud, from memory)

1. Draw the four-stage cascade with candidate counts. What is each stage's *job* (not its model)?
2. State the alignment/accuracy decomposition. Why measure alignment on *unimpressed* traffic?
3. What is sample-selection bias in preranking, and three ways to fight it?
4. Why ANN not exact NN at L0? Why two-tower not cross-encoder at L0?
5. What is calibration, how do you measure it (O/E, ECE), and why does multi-objective ranking break without it?
6. Explain how CLR uses a UIC vector. How is that the bridge from Anticipation's geometric prediction to retrieval?
7. Map a RAG pipeline onto this funnel, stage by stage.

*This is your moat — you should be able to teach all seven without notes. If not, re-read your own `preranking_paper/paper_capture.md` and `retentive_recs.md` §5.*
