# System Design Prep — Question Index

*Source: `interview_prep/system_design_prep.pdf` (93 pages, extracted 2026-05-22).*

One markdown per design question, plus framework + reference material.

## Framework (read first)
- **[00_FRAMEWORK.md](00_FRAMEWORK.md)** — Interview framework, ML system design template, AI system design template. Read first to anchor approach across all questions.

## Trust & Safety / Integrity classifiers (5 variants of the same problem)
- **[01_harmful_content_detection.md](01_harmful_content_detection.md)** — Initial framing of harmful content detection.
- **[02_multi_layered_harmful_content.md](02_multi_layered_harmful_content.md)** — Multi-layered detection architecture.
- **[03_ml_safety_classifier.md](03_ml_safety_classifier.md)** — Broader ML Safety Classifier framing.
- **[04_defense_in_depth_brief.md](04_defense_in_depth_brief.md)** — Brief defense-in-depth design.
- **[05_defense_in_depth_full.md](05_defense_in_depth_full.md)** — **Most comprehensive variant.** Full blueprint with safety KPIs, multi-layer architecture, constitutional classifiers, adversarial robustness. This is the version to lead with for OpenAI Integrity.

## Generative + multimodal designs
- **[06_gmail_smart_compose.md](06_gmail_smart_compose.md)** — Smart Reply / Smart Compose (seq2seq + prompt engineering).
- **[07_rag_system.md](07_rag_system.md)** — RAG system design (chunking, embeddings, retrieval, generation, eval).
- **[08_image_captioning.md](08_image_captioning.md)** — Image captioning (encoder-decoder, CLIP/ViT, BPE tokenization).
- **[09_text_to_image.md](09_text_to_image.md)** — Text-to-image generation (latent diffusion).
- **[10_text_to_video.md](10_text_to_video.md)** — Text-to-video (5s 720p @ 24fps from text prompt).

## Retrieval + recommendation designs
- **[11_youtube_search.md](11_youtube_search.md)** — Text-to-video search (representation learning, two-tower, ANN).
- **[12_video_newsfeed_rec.md](12_video_newsfeed_rec.md)** — Video / Newsfeed recommendation (hybrid filtering, candidate generation + ranking, two-tower).
- **[13_visual_search.md](13_visual_search.md)** — Similar content / visual search (image embeddings, contrastive learning).

## Classical systems design
- **[14_chat_system.md](14_chat_system.md)** — Chat system with online indicators, push notifications, group limits.

## Reference material
- **[99_REFERENCE.md](99_REFERENCE.md)** — Transformers (attention, multi-head, encoder/decoder), RLHF / RLAIF / DPO, AI Safety primer, Scaling techniques (horizontal/vertical, caching, TTL/eviction, latency numbers).

---

## Highest-leverage files for May 27 OpenAI Integrity prep

If time is short, the integrity-relevant material is:

1. **[05_defense_in_depth_full.md](05_defense_in_depth_full.md)** — The blueprint to internalize. Constitutional classifiers, multi-layer architecture, FP rate targets, jailbreak prevention KPIs.
2. **[00_FRAMEWORK.md](00_FRAMEWORK.md)** — Internalize the 5-10/10-15/15-25/5 minute structure. Reid Gustin's loop (if you get there) will run on this clock.
3. **[02_multi_layered_harmful_content.md](02_multi_layered_harmful_content.md)** — Multimodal classifier patterns, fusion methods, fairness considerations.
4. **[99_REFERENCE.md](99_REFERENCE.md)** — Skim the RLHF and AI Safety sections; expect adjacent questions.

## What this prep doesn't yet have

- Explicit FP/FN trade-off framing as a first-class lens (the user-experience reframe James added 2026-05-22). Worth weaving into how you talk about Safety KPIs (target FP <1%) from `05_defense_in_depth_full.md`.
- Cipher / jailbreak attack walkthroughs that show how the layered defense responds adaptively. The previous Anthropic loop (`failed_anthropic_system_design.pdf`) cut off at the cipher example without resolving it — that's the gap to close before the next technical loop.
- Recent (2025–2026) constitutional AI + RLAIF advances. Reference material in `99_REFERENCE.md` is solid foundationally but doesn't reflect post-2024 advances.
