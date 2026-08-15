# Integrating Quality/Safety Objectives into the Recommendation System — Design Options

> **Source of record.** Pasted verbatim by James 2026-08-14. **This is the CQ-team doc (Qinglong Zeng, Sr EM Content Quality → reports to Faisal Farooq).** James's framing: *"their preferred tactics essentially."*
> **The load-bearing sentence: "CQ's preference is L2, for both the utility change and the ranking-loss change."** L1 Utility is James's team's system (JJ/Rui owners); CFM/UPP pretrain backbone is also James's. Read the recommendation section with that in mind.

## Motivation

Hard filtering is necessary for clearly unsafe content but insufficient as the primary quality lever:
- It creates **step-function engagement tradeoffs** (e.g., the **racy filter cost ~4–5% male impressions**).
- **Filtered slots backfill with other borderline content.**
- **Score-based soft enforcement achieves a better quality↔engagement Pareto** across Notif/HF/Search.
- Most importantly: **an engagement-only ranker is structurally biased** — negative feedback (hides/reports/short clicks) is sparse, and low-quality "slop" can still drive long clicks, so the model learns to amplify it. **Simply adding quality features has not been enough.**

→ Make quality a **first-class objective** in the ranking stack.

Two option families, each with two orthogonal design axes:
- **Utility change** (serving-time score combination) — *where* (L1 vs L2 utility) and *how* (quality head in ranker vs separate quality model).
- **Loss-function modification** (training-time label/example reweighting) — *where* (L1 vs L2 model) and *when* (fine-tune vs pretrain/CFM-UPP vs both).

"The two families are complementary, not mutually exclusive: utility changes adjust **what is shown now** (and can address clustering via spacing); loss modification changes **what the ranker learns** and debiases the objective at the root."

---

## Option Family 1: Utility Change

`utility = f(engagement_utility) − λ · g(quality_score)`

A graded, serving-time re-ranking penalty — not a binary filter; `g(·)`/λ shaped and tuned per surface/audience.

### Axis 1A — Where: L1 utility vs L2 utility

**Option 1A-i: L1 utility**

*Pros*
- **Upstream quality control.** Caps the flow of borderline candidates before the full ranker, reducing over-recommendation at the source.
- **Decoupled from the contested L2 blender.** Avoids touching the heavily-tuned blender utility that surface teams (e.g. P2P) are protective of — **a lower-friction path to ship**.
- **Cheap and lightweight.** Good fit for early learning experiments (**aligns with HF's ask**) and teen-safety image-side work (e.g. drug/alcohol).
- Content-side scores can be precomputed/cached, O(1) lookup — matched to L1's tight per-candidate budget.

*Cons*
- **Image-level only today.** L1 utility cannot consume domain/landing-page-level signals (GenAI-domain, DQv4) → not a drop-in for P2P/Search domain-demotion use cases.
- **Coarse / low context.** Little personalization or full-candidate context at L1; less precise tradeoffs.
- **Permanent candidate loss risk.** Penalizing too hard upstream removes candidates the full ranker could have handled with more nuance.
- **The engagement-only full ranker downstream can partially undo it.** *"This is the subtle one."* L1 controls which candidates flow and their initial utility, but **L2 still has the final say on ordering** — if L2 isn't quality-aware it re-ranks purely on engagement, so a borderline-but-engaging pin L1 demoted **can float right back up at L2**. "Our L1 effect gets diluted/washed out downstream. We are relying on 'reduce how many borderline candidates even reach L2' rather than 'guarantee they rank low in the final feed.'"

**Option 1A-ii: L2 utility (full-ranker / blender)**

*Pros*
- Most precise place to trade off quality vs engagement per final slot; richest features and full candidate context.
- **Proven.** P2P (LQS Rate V2 **−0.87%**, UCAN shopping gains, neutral topline) and Search (UCAN LQS **~−10%**, US repins **+1.13%**) demotion experiments ran here successfully.
- Supports domain/landing-page signals; fine-grained impression-based calibration + per-content-type tuning (e.g. milder demotion for shopping).

*Cons*
- **Highest friction / ownership sensitivity.** The blender is heavily tuned and surface-owned; teams wary of consuming external CQ signals directly (the HF/P2P concern).
- **Still a serving-time patch** — doesn't fix what the model learned.

### Axis 1B — How: quality head in the ranking model vs a separate quality model

**Option 1B-i: Quality head inside the ranking model (multi-task)**

*Pros* — Context-aware (quality conditioned on user × context × content), co-calibrated with engagement heads → cleaner combination in utility. Near-zero marginal serving cost, same forward pass; **"fits the CFM/UPP head-adapter design (similar to the existing hide/report head)."** Representation sharing.

*Cons* — **Label bottleneck**: needs quality/safety labels on the surface's own training traffic at scale (certified LLM prompts + labeling budget) — **the known gating dependency**. Coupled iteration (quality changes require retraining). Multi-task tuning risk (gradient conflict, loss weighting, negative transfer). Less reuse — quality definition baked per-model.

**Option 1B-ii: Separate quality model (external score → utility)**

*Pros* — Decoupled + reusable; one shared score feeds L1, L2, Notif, Search → the "unified quality utility" vision; CQ and ranking teams iterate independently. Precomputable/cacheable as a content attribute → ideal for L1. Rich dedicated supervision (LLM-labeled data, not limited by ranker label sparsity). **Auditable + controllable** — explicit λ, transparent for policy/teen-safety, easy to dial per surface.

*Cons* — Static / not personalized (ignores user/context tolerance). **Calibration mismatch** — combining a separately-trained score with engagement preds needs care; λ tuning manual and brittle. Extra system to maintain. **Post-hoc** — doesn't debias engagement predictions; "the engagement head still *wants* to promote engaging slop."

---

## Option Family 2 — Loss-Function Modification (label / example reweighting)

Change what the ranker learns: down-weight (or drop) positive-engagement training examples when the item is flagged low quality. "The **engagement purification / degaming** direction — directly attacks the structural bias."

`loss = Σ_i w_i · BCE(pred_i, label_i)`, where `w_i ↓` if `item_i` is flagged low quality and engagement is positive.

### Axis 2A — Where: L1 model vs L2 model

**2A-i: L1 (light ranker) loss modification** — *Pros:* debiases early-funnel scoring at the learned level, not just a penalty; cheaper to retrain/iterate. *Cons:* limited signal + capacity (compact/image-level feature set); **bounded impact** — final ordering dominated by L2.

**2A-ii: L2 (full ranker) loss modification** — *Pros:* biggest effect on final ordering; rich features. *Cons:* expensive + sensitive; surface teams protective; slower iteration.

### Axis 2B — When: fine-tune vs pretrain (CFM/UPP) vs both

**2B-i: Pretrain stage (CFM/UPP backbone)** — *Pros:* **maximum leverage** — a debiased backbone is inherited by every surface that fine-tunes on it → consistency + amortized one-time cost; best data (largest cross-surface volume, hard negatives from well-ranked impressions). *Cons:* **pretrain/fine-tune objective mismatch** — pretraining with a quality objective then fine-tuning with an engagement objective might wash out or override it.

**2B-ii: Fine-tune stage** — *Pros:* surface-specific + flexible; matches **UPP's label-weight / head-adapter design** (label weights often computed in the dataloader at fine-tune); faster iteration, smaller blast radius, easy per-surface A/B. *Cons:* sparser data (rare quality events per surface); duplicated effort per surface.

**2B-iii: Both** — *Pros:* most thorough; strongest long-term posture. *Cons:* most coordination, cost, complexity; hardest to attribute; needs mature labels everywhere.

---

## Recommendation / suggested sequencing

**(1) Utility change and loss modification — do both.** Near-term the utility change gives shippable low-risk wins with existing proof points (Notif, Search), and lets us stand up the shared/unified quality score + monitoring everything else reuses. In parallel, invest in loss-function modification as the durable fix, since utility penalties are post-hoc and leave the engagement objective itself biased.

**(2) L1 vs L2 — CQ's preference is L2**, for both the utility change and the ranking-loss change. Rationale:
- **Signal coverage.** The majority of quality signals are **domain/landing-page-level** (GenAI-domain, DQv4, link quality), which L1 cannot consume today (image-level only). L2 supports the full signal set.
- **L1 gets washed out.** If enforcement is only upstream, the engagement-only full ranker downstream can re-promote borderline-but-engaging content L1 demoted. **"L2 is where final ordering is decided, so quality enforcement there actually sticks."**
- **Precision + proof.** L2 has the richest features/context for per-slot tradeoffs and impression-based calibration; both P2P and Search demotion launches already validated at L2.
- Concession: *"We recognize surface teams feel 'more upstream = less friction,' so **L1 can serve as an optional complementary density lever** (reduce how many low-quality candidates even reach the full ranker, per the 'quality in both L1 and L2' idea), but **the primary enforcement point should be L2**."*

**(3) Fine-tune vs pretrain (CFM/UPP) vs both — CQ believes quality should be integrated across both**, rolled out in phases:
- **Phase 1 — Prove it at fine-tune on a few pilot surfaces (notif/search).** Quality-aware loss reweighting (and/or a quality head) at fine-tune on a small set of receptive surfaces; demonstrate quality wins with neutral/positive engagement; establish the label pipeline and eval.
- **Phase 2 — Push into the shared pretrain backbone (CFM/UPP).** Once wins are demonstrated, integrate the quality objective into cross-surface pretraining so the backbone learns debiased representations every surface inherits — maximum leverage and consistency.
- **Phase 3 — Reinforce at fine-tune across all surfaces.** Keeping it at both stages is deliberate: prevents the pretrain quality signal from being washed out by an engagement-only fine-tune, and lets each surface apply its own quality definition/weights on top of the shared backbone.

## Open questions (theirs)

1. We have both image-level and non-image-level quality signals; if we go with L1, what do we do with non-image-level quality problems?
2. The majority of our quality signals are **non-personalized**. Precomputed signals might be a better option than adding a quality head in ranking models?
3. For loss reweighting: **down-weight vs fully drop** positive examples? What weight schedule, and how do we guardrail against over-suppressing legitimately engaging content?
4. Do we want to start with quality reweighting for the **pretrain** stage, or **fine-tuning** stage?
