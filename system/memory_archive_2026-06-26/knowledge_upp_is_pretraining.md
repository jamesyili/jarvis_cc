---
name: UPP is foundation pretraining for user representations
description: UPP at Pinterest is foundation-model pretraining for user representations — not a downstream feature-consumer or user embedding layer. Matt Chun PM, Hongtao/Piyush/Rui working group.
type: reference
originSessionId: 12c21b47-b0e7-4d9e-b017-f2e477d37178
---
**UPP** at Pinterest is foundation-pretraining for user representations — Pinterest's version of the pretrain-finetune paradigm applied to user embeddings (like Meta's HSTU or generative user foundation models). It is **not** a downstream feature consumer, not a retrieval-layer-with-feature-inputs, and not a generic user-embedding API.

**Key facts:**
- **PM:** Matt Chun (canonical ID `matt_chun` in Reflex experts registry)
- **Working group:** Hongtao Lin, Rui Liu, Piyush Maheshwari, Zihao Chen, Jaewon Yang, Dimitra, Matt Chun
- **James's blog post #1 framing:** *"Survey the pretrain+finetune paradigm in recsys. Cover CLR architecture, what's pretrained vs fine-tuned, why this paradigm, UPP angle, predictions."* — UPP is one example of the paradigm, not the paradigm itself
- **Cross-org operational model exists** at `work+self/projects/upp/cross_org_operational_model/draft_v3_synthesized.md`
- **Cannot mention UPP by name in public blog posts** — internal work-in-progress
- **Faisal partnership track** is around UPP (UU work for Retentive Recs)

**Implications for technical reasoning:**
- Visual user signature as a *downstream feature* does NOT plug into UPP's training task — different layer entirely
- "Training UPP models" means training the pretrained backbone, not adding feature inputs to a retrieval model
- UPP-Retrieval is downstream of UPP (uses UPP-trained representations for retrieval) — that's distinct from UPP itself

**Why this memory exists:** 2026-05-11 session — Leo mapped UPP as a downstream retrieval-layer-with-feature-inputs in a technical brainstorm. James corrected: *"UPP is not surfacing here. I'm not seeing how training UPP models is going to help here. You might be mistaken about what UPP is."* Verify before propagating UPP framing in technical design conversations.
