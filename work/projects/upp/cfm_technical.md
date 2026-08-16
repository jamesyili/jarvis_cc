# CFM — Conditional Foundation Model (Ranking) — Technical Reference

**Created 2026-06-07** from authoritative internal material James surfaced (CFM design doc + architecture diagram + CFM model-scaling doc). Complements the retrieval-side refs (`ubr_design.md`, `clr_technical.md`) — those cover the **retriever**; this covers the **ranking** CFM and the scaling research.

> Companion artifact: `system/artifacts/transformers-for-recsys.html` (Part 6) renders this with the embedded architecture diagram and connections back to transformer fundamentals / TransAct.

---

## 1. What CFM is

CFM is a **single unified ranking model** that predicts engagement for a pin in **any context** — trained on and serving **Homefeed, Related Pins (P2P), Board-More-Ideas (BMI), Notifications, Search**. Cornerstone of UPP: a strong unified ranker surface teams fine-tune.

Compositionally: **CFM = FM backbone + TransAct v2 (16k long-seq) sequence module + feature cross + ranking heads**, trained with **future-action loss (FM component, ℒ_ntl) + BCE ranking loss + pairwise loss (ℒ_pwl + ℒ_ce)**. "Based on Foundation Model, but also uses TransAct v2 and other core-ranking innovations."

**Three-tier UPP hierarchy:** Foundation Model → Base Models (the CFMs: ranking CFM + retrieval CFM/UBR) → Surface-specific models.

---

## 2. Architecture (from the diagram)

- **FM backbone** runs over the *Recent n user sequence* via the *ID Embedding Table*; trained with next-token loss **ℒ_ntl** (recurrent arrows). Per-position outputs + a *dummy token* + *candidate-conditional* tokens feed the ranking model.
- **Ranking model** (feature process + crossing) consumes those tokens + *Additional Pin, Request, Context info* → **ℒ_pwl + ℒ_ce**.
- **Per-surface "surface-specific embedding generation"** (one per surface j):
  - **TransAct v2** over *16k-NN sequence* + *Recent-m sequence* + *Surface sequence*
  - **Surface Feature Cross** over *surface-specific request/context info*
  - → emits the red **"conditional on candidate pin"** surface tokens that feed the ranking model.
- Legend: cream = request-level tokens, purple = dummy token, red = conditional-on-candidate-pin; circles = ID / Action-FV-type / pre-embedded features.

### High-level design specifics
- Ranking model with **conditionally-triggered, per-surface context encoders** (FM and feature cross may each need their own per-surface encoder). Built on the **Foundation Ranker** backbone.
- Sequence + interaction modeling: Foundation Ranking transformer + ID embeddings, plus 16k (compressed when available) + real-time omnisage transformer (= TransAct v2).
- Feature cross over sage embeddings, transformer outputs, optional context embeddings.
- **Per-surface context encoders DON'T share params** (P2P encoder only gets gradient from P2P rows).
- **Per-surface context features:** Search = search sage emb · P2P = query-pin os + pinclip + id embedding · BMI = board os emb · HF = learned emb (no features).
- **Single-epoch training** (to start) so the embedding table can update during PT & FT.
- ⚠ Xue Xia flag: sequence formats differ across surfaces → may cause issues.
- ⚠ Open naming: "Foundation Ranker" may be distinct from pure "FM"; depth/width unspecified.

---

## 3. The Pinnability-Light (Pinnability Sequential) insight

Per-feature ROI test: (1) cost to store/train/serve the feature + its internal repr; (2) metric win from **dropping** it and reinvesting the saved cost in better training (more architecture, longer training, higher serving). Result: **many features have strongly negative ROI — primarily sparse vector annotation features.**

**Worth keeping:** key metadata (request time, pin creation time, pin neardup id) · key sage features (omnisage, pinclip) · key user-sequence features · PinPerf/UserPerf scalar features.

**The unlock:** the trimmed set is **natively present across all core-surface datasets** (these features matter for every surface), so it (a) doesn't hurt Pinnability-alone performance and (b) **avoids the feature-set coordination problem** that normally makes cross-surface backbones hard to ship. → Central proposal: trimmed-feature cross-surface ranking model as the backbone for core rankers.

Prior art cited: Closeup Level Engagement Model; Jinfeng Rao's Cross-Surface Pretraining; productionized GULP Ranker v0 (fine-tuned Pinnability).

---

## 4. FM vs CFM vs Surface model

| | FM | CFM | Surface model |
|---|---|---|---|
| Data | source-of-truth; **no impressions** (no hard negatives) | tabularml: impressions + actions | tabularml: impressions + actions |
| Features | long-seq only: os, neardup, action type, timestamp, fv type | + real-time seq, 16k seq, 256d os, 256d pinclip, cand pin-age | full surface feature set |
| Loss | future-action (next-token) only | future-action + BCE ranking + pairwise | BCE primary + future-action (FM comp) + pairwise |

Takeaways: **FM ≠ ranker** (no impressions/candidate info → can't train pointwise; "learned this the hard way"). **CFM ≈ Surface model** ("aren't that different") — CFM is essentially the surface model's shape, pretrained cross-surface.

---

## 5. Deploying CFM into a surface

- **Minimal:** keep only surface-specific embedding generation + FM components, discard the rest → CFM as an embedding module into feature cross (exactly how FM is used today).
- **Maximal:** keep the full CFM; override the last layer for custom heads + engagement loss; surfaces add features via CFM feature cross and/or surface embedding generation.

**Must hold identical across CFM PT ↔ surface FT** (consolidation targets, priority order):
- **P0** FM model + architecture (core reason to pretrain)
- **P1** TransAct architecture (major quality lever; benefits from cross-surface data)
- **P2** Feature cross
- **P3** Which features are used
- **P4** Label weights/heads/task — change as little as possible from prod per surface, to isolate consolidation effects.

Dataset distribution held fixed PT/FT for maintenance simplicity.

**Why it works:** compute efficiency (pretrain once, amortize) · more data without quality loss (cross-surface hard negatives from impressions) · training→serving compute migration (more headroom in serving than training; SOTA-hardware gap larger in serving; fp8/fp4 easier in inference; many rankers score more candidates than typical → room for more compute/candidate).

---

## 6. CFM Model Scaling (in-flight research)

**Authors:** Matthew Lawhon, Matthew Poska, Kousik Rajesh, Kelly He, Jaewon Yang. Related docs: "Conditional FM"; "[One-Pager][ATG] Next-Gen Teacher Foundation Model"; "Future of RecSys Models in 2026."

**Bet.** Conventional **FM** pretraining scale often fails to transfer to FT metrics unless FT compute also increases. Hypothesis: **CFM** pretraining transfers better to ranking under a **fixed FT compute budget**. **Early signal: CFM pretraining → ~1% repin wins on both HF and BMI FT jobs, no architecture scale-up, similar FT compute.**

**Central question (FT compute fixed):** scaling behavior of FM vs CFM, and does CFM-pretraining scale beat FM at the same fixed FT budget? **Success criterion:** statistically significant FT-metric + online wins from scaling CFM pretraining vs equivalently-scaled FM.

**Constraints:** FT compute fixed (training); serving clusters have underutilized GPUs (host-CPU-bottlenecked, low SM activity → inference headroom). **Distillation:** targets larger non-serveable architectures (don't leverage request-level compute); complementary to student scaling (teacher can be arbitrarily better since it needn't be serveable).

**Hypotheses:** (1) under fixed FT compute, CFM-pretraining scale > FM-pretraining scale on transfer; (2) for larger backbones, partial/frozen FT (LoRA + frozen components) closes the gap to full FT within budget; (3) teacher–student or longer-context pretraining further improves CFM transfer at constant FT compute.

**FT methods ablated** (each on both FM- and CFM-pretrained backbones, per scale point; optimizer/epochs/BS tuned only within the same FT budget): frozen+quantized embedding table (+ ablate dense/all-loss + scale-up BS) · multi-epoch w/ smaller dataset (may need multi pretrain snapshots) · LoRA on selected blocks (LoRA + DoRA; SVD/PiSSA vs standard init) · full FT under budget + emb-table updates (<1 epoch) · LoRA + emb-table updates · frozen emb-table + partial FT (top-k blocks) · frozen emb-table + frozen FM (head-only) · mixed (low-rank adapters + selective LayerNorm/bias) · LoRA on emb-table.

**Results so far:**
- **LoRA on modules (emb+dense, ±DCN; DoRA; PiSSA init) → ~−2% repin** (underperformed; PEFT not winning yet). Variants: bd_lora_det_r32/bd_lora_r32, dcn_lora_r32_v3 (freeze emb+dense, LoRA on DCN), dora_backbone_r32, lora_backbone_pissa_r32, lora_backbone_std_r32.
- **Freeze + quantize embedding table + projection layer → ~+0.3% repin** (modest). Variants: emb_adapter, freeze_emb, freeze_quant_emb, freeze_quant_emb_lora, quant_emb_adapter.
- All variants had **lower throughput** than baseline. Batch sizes: master control 4400; baseline_v3 4000 (80M embedding table); other groups 2200 (tunable). All runs **without semi-sync**.
- ⚠ Snapshot, not verdict: the ~1% headline came from *pretraining*, not these FT tricks; open question is whether scaled CFM pretraining + a budget-friendly FT strategy compounds. Treat deltas as provisional.

---

## 7. New names surfaced (CFM/scaling)

| Name | Note |
|---|---|
| Matthew Lawhon | CFM scaling co-author; also Reflex Modeling lead (per `reflex/archive/tim_friday_5-29_debrief.md`). Earlier in UPP alignment thread ("one base model per category" view). |
| Matthew Poska | CFM scaling co-author (he/him). New name. |
| Kousik Rajesh | CFM scaling co-author. New name. |
| Kelly He | CFM scaling co-author. New name. |
| Jaewon Yang | CFM scaling co-author; recurring in UPP (CFM transformer-output-vs-FM-output point). |
