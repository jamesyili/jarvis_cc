# Viral Remix Pipeline — High-Level Plan

**Status:** Pre-PRD. Convert this into a formal PRD before starting build.
**Owners:** Daniel, James
**Repo:** Separate repo, TBD (not `rekko.ai`)
**Date:** 2026-04-17

---

## 1. Vision

A faceless short-form video channel in the **celebrity + news + entertainment** niche, where finished videos are produced by:

1. Retrieving short clips (3–5s each) from a VLM-annotated database of viral content (TikTok + YouTube) scraped over a rolling window
2. Generating an editorial TTS script with original commentary on top of the clips
3. Stitching clips + TTS + captions + recurring intro/outro brand elements into a 30–60s vertical video

James and Daniel are the only operators. The pipeline is not productized for external creators. It is a content-operating business + infra craft project.

## 2. What This Is Not (Non-Goals)

- **Not a SaaS or API** for external creators. No multi-tenant, no auth, no billing.
- **Not tied to the @rekko.ai brand.** New sister channel. Rekko's prediction-market identity stays intact. Can tie back later if synergy emerges.
- **Not a pure generative-video play.** Real clips remixed + editorial commentary is the bet. Generative video (Veo, Runway, Sora) stays out of MVP; can be added later for B-roll fill-ins only.
- **Not a 10-year crawl.** Start with 6–12 months of rolling viral content. 10 years is a scope-creep fantasy.

## 3. Users + Success Metrics

**Users:** James + Daniel (operators). Indirect: the channel's audience.

**Primary bet framing (James + Leo, 2026-04-17):** This is **(i) a craft/portfolio bet** + **(ii) a distribution-learning bet**. It is **not** a revenue bet. Revenue is a lag signal, not a target.

**6–9 month success criteria:**
- **(i) Craft:** Working end-to-end pipeline + 20 quality videos produced + 1 blog post synthesizing the build (generative-video infra portfolio artifact).
- **(ii) Distribution:** Posting cadence sustained ≥3 months; 3-month channel retention curve captured; reverse-engineered playbook documented.
- **(iii) Revenue (lag signal, not goal):** If channel succeeds, expect $150–500/mo in platform revenue by month 9. Track, don't optimize for.

**Explicit anti-goal:** Over-build infra for a revenue target that is too small to justify the build. If money becomes the point, rescope.

## 4. Platform Strategy

**Source platforms (where we crawl):**
- TikTok — highest signal for viral celebrity/news content, most trend-responsive
- YouTube (Shorts + long-form entertainment clips) — larger catalog, easier scrape
- Reuse `rekko.ai/src/rekko_server/scrapers/viral_discovery.py` and `viral_broll*.py` as starting infrastructure

**Target platform (where we post):**
- **Phase 1: YouTube Shorts first.** Reasons: Content ID is predictable (can dispute systematically), monetization programs more favorable to new channels, longer discoverability window, fair-use framing holds up better under YouTube's DMCA process
- **Phase 2: Expand to TikTok.** Trend-response upside higher but takedown/shadowban risk higher
- **Phase 3: Instagram Reels.** Lowest priority — monetization weak for new channels

**Decision deferred:** posting cadence (target 1/day minimum, 3/day ideal) and review gate (human-in-loop per video vs. sampled QC).

## 5. System Architecture (High-Level)

```
[Source Scrapers]          [Clip Extraction]          [Annotation Layer]
 TikTok discovery   ──►    Shot boundary detect  ──►   VLM: scene desc
 YouTube discovery  ──►    Clip segmentation     ──►   Celebrity recognition
                                                       Emotion + context tags
                                                       ▼
                                                 [Clip Database]
                                                 (vector + metadata)
                                                       ▼
[Topic Input] ──► [Topic Expansion] ──► [Retrieval] ──► [Ranking]
 Trending news        Topic → search             Semantic + keyword
 Manual brief         queries for DB             + recency + engagement
                                                       ▼
                                                 [Script Generation]
                                                 TTS commentary
                                                 Editorial POV
                                                 Hook + payoff
                                                       ▼
                                                 [Clip-Script Alignment]
                                                 Which clip plays when
                                                       ▼
                                                 [Stitch + Render]
                                                 Intro + clips + captions
                                                 + outro + watermark
                                                       ▼
                                                 [QC Gate]
                                                 Human review (MVP)
                                                       ▼
                                                 [Post + Track]
```

### 5.1 Stage Details

| Stage | MVP (weeks 1–6) | Phase 2 (month 2–3) | Phase 3 (month 4+) |
|-------|-----------------|---------------------|---------------------|
| Scrapers | Reuse Rekko's `viral_discovery` + `viral_broll`. One source first (YouTube Shorts). | Add TikTok. Rolling 6-month window. | Trend-responsive crawl (pull on breaking news). |
| Clip extraction | Fixed 3–5s segments via shot boundary (PySceneDetect or similar). | Action segmentation; find the "moment." | Multi-shot narrative extraction. |
| Annotation | Gemini Flash or GPT-4o-mini on keyframes. Celebrity ID, scene, emotion, context tags. | Add speaker diarization, quote extraction. | Full VLM on video tokens (when cost drops). |
| Clip DB | Postgres + pgvector. Start with <10K clips. | Scale to 100K–1M clips. | Consider specialized vector DB. |
| Retrieval | Text → embedding → top-k. | Hybrid (BM25 + semantic + recency + engagement). | Personalized to channel's performance history. |
| Script gen | Claude or Gemini, editorial POV prompt, ~70:30 commentary-to-clip ratio. | Voice-cloned consistent narrator persona. | Self-iterating on performance data. |
| Stitch + render | Rekko's Remotion or FFmpeg pipeline reused. Fixed intro/outro. Burned-in captions. | Per-niche templates. Dynamic transitions. | Adaptive pacing based on retention curves. |
| QC | Human review every video. | Sample 1/3. | Fully autonomous + weekly audit. |

### 5.2 Key Design Decisions to Resolve in PRD

1. **VLM choice for annotation.** Gemini Flash cheapest, GPT-4o-mini balanced, Claude Haiku for context. Cost per clip at scale matters — do a spike.
2. **Embedding model** for clip retrieval. OpenAI `text-embedding-3-small` default; consider multimodal embeddings (CLIP, VideoCLIP).
3. **TTS engine.** ElevenLabs (realism, ~$5/mo Starter) vs. Kokoro (local, free). Rekko already uses Kokoro — can reuse, but ElevenLabs produces higher-retention audio.
4. **Voice/persona identity.** Single cloned voice = channel brand anchor. Clone whose voice? Daniel? Synthetic character?
5. **Stitch engine.** Reuse Rekko's Remotion renderer vs. build custom.
6. **Clip database scale.** Cap initial catalog at 10K–50K clips. 10-year fantasy → explicit descope.

## 6. Legal + Compliance

**Working legal template:** Commentary-heavy faceless editorial (the TMZ / PopCrave / Hollywood Unlocked / Commentiquette pattern). This is a working model. It is **not** a greenfield legal question.

**Non-negotiable guardrails (bake into pipeline from day 1):**

- **Commentary-to-footage ratio ≥2:1** speaking time over silent clip time. Enforce in pipeline — reject videos that fail this ratio.
- **Clip spans 3–5 seconds each.** No full-scene reproductions.
- **Real editorial POV** — the TTS script must add meaning, critique, context, or report. Not just narrate what's on screen.
- **Source attribution** in video captions/description when possible.
- **No defamation.** LLM editorial output needs a factual guardrail pass — don't let the AI make claims about real people without grounding.

**Risks that commentary does NOT solve:**

- **Content ID (YouTube) + TikTok fingerprint match** will flag uploads automatically regardless of fair-use posture. **Expect 20–40% takedown/demonetization rate.** Operations plan needs a dispute queue + counter-notification workflow. Daniel carries the ongoing dispute-queue load.
- **Right of publicity (CA §3344, NY, TX, VA)** is orthogonal to copyright. Celebrity likeness used commercially = separate cause of action. News/commentary framing mitigates but doesn't eliminate. Avoid deepfakes and misleading framing completely.
- **AI-generated commentary is legally untested.** Courts have not definitively ruled on whether AI editorial qualifies as transformative under §107 factor 1. Carrying novel risk the incumbents (TMZ et al.) are not.

**Pre-build spend:** $500–1K for a 1-hour IP attorney consult to stress-test the specific operating model before Daniel commits weeks of engineering. **Non-optional in my view.** This is the single cheapest risk-retire move.

## 7. Operating Model (Gap to Close)

**This is the biggest gap in the current plan.** Build ≠ operate. Successful celebrity/news content farms post 3–10 videos/day, respond to breaking news within hours, and maintain editorial consistency. Current plan covers build; does not cover operate.

**Week 1 deliverable (Daniel):** Reverse-engineer 10 successful celebrity/news/entertainment channels on TikTok + YouTube Shorts. Output: a spreadsheet with:

- Channel name + platform + subscriber count
- Posts per day, posts per week
- Avg video length
- Hook format (first 2 seconds)
- Commentary-to-clip ratio estimate
- Editorial POV (what's the take? what's the voice?)
- Recurring video formats (list, reaction, retrospective, breaking news)
- Intro/outro pattern
- Caption style
- How they respond to breaking celebrity news — lag time from event to post

This work comes **before** significant code is written. It sizes the operating muscle needed and saves months of wrong-direction building.

**Open operating questions for the PRD:**

- Posting cadence target (min viable / stretch)
- Who operates the posting (Daniel full? Shared? Automated with manual approval?)
- Review gate (per-video human review vs. sampled vs. fully autonomous)
- Trend-response workflow (breaking-news alert → content turnaround time)
- Channel naming + brand identity
- Intro/outro assets (who designs)
- Editorial voice/persona definition

## 8. MVP Scope (First 4–6 Weeks)

**In scope:**
- Repo bootstrap (separate from `rekko.ai`)
- Port `viral_discovery` + `viral_broll` scrapers
- YouTube Shorts scraper first (not TikTok)
- Basic clip segmentation (PySceneDetect)
- Basic VLM annotation (Gemini Flash on 3 keyframes per clip)
- Clip DB (Postgres + pgvector, <10K clips)
- Simple retrieval UI (text → ranked clips)
- Manual stitch workflow: CLI or minimal web UI where Daniel picks clips, writes/edits TTS script, previews stitch
- First 3–5 videos produced end-to-end using the pipeline (manual), posted
- Channel set up, intro/outro assets designed

**Explicitly out of MVP:**
- Auto-ranking / auto-stitch
- TikTok source
- Fully autonomous pipeline
- Trend-ingestion / auto-topic-generation
- Generative-video fill-ins (Veo, Runway, etc.)
- Analytics dashboard
- Cross-posting automation
- 10-year crawl

## 9. Phase 2 (Months 2–3)

- Auto-stitch given a script (align clips to script beats)
- Auto-rank retrieval (engagement-weighted)
- Add TikTok source
- Sustained posting cadence (1/day minimum)
- Operations playbook locked in (cadence, review gate, trend-response)
- First channel retention data captured

## 10. Phase 3 (Month 4+)

- Trend-responsive content ingestion (breaking-news triggers)
- Multi-clip narrative intelligence
- Voice-cloned consistent narrator
- Quality-and-retention feedback loop

## 11. Open Questions for the PRD (for James + Daniel)

1. **Channel name + identity.** What's the brand? What's the editorial voice?
2. **Specific sub-niche focus.** "Celebrity/news/entertainment" is broad. Pick 2–3 sub-formats for MVP (e.g., "celebrity relationship drama breaking news," "retrospective deep dives," "reaction-style commentary").
3. **Voice/persona.** Cloned voice of whom? Off-the-shelf ElevenLabs?
4. **Posting cadence target + operating ownership.** Daniel posts daily? Weekends too?
5. **Review gate.** Per-video human review in MVP. How does that scale at Phase 2?
6. **IP attorney consult** — before or after build begins? (Strong recommendation: before.)
7. **Exit criteria for this bet.** If at month 6 the channel has <5K followers + no retention signal, do you stop or pivot? Define the pre-mortem.

## 12. Proposed First Actions (Next 2 Weeks)

**Week 1:**
1. Daniel: reverse-engineer 10 successful channels, produce the spreadsheet above
2. James: book IP attorney consult ($500–1K)
3. Both: decide channel name + identity + specific sub-niche focus
4. James: set up new repo scaffold, port Rekko's scraper modules as starting infra

**Week 2:**
1. Daniel: write first draft of the PRD using this plan as input
2. James: spike on Gemini Flash annotation cost at 1K clips — produce $/clip number
3. Both: agree on MVP scope after PRD and attorney feedback

**Gate to proceed past Week 2:** attorney consult done + PRD in draft + cost spike complete. If any of these surfaces a kill-condition, rescope or abandon before more time goes in.

---

## Appendix: Decisions Made During Grill (2026-04-17)

| Decision | Value |
|----------|-------|
| User | Internal only — James + Daniel. Not productized. |
| Path | Path A (faceless content generator), with Path C (storyboard/retrieval) as an internal phase of the pipeline. |
| Niche | Celebrity + news + entertainment. |
| Editorial overlay | TTS with commentary + original scripting on top of remixed clips. |
| Unique channel identity | Consistent intro/outro + distinctive voice. |
| Brand tie-in | Separate sister channel, not @rekko.ai. Can tie back later. |
| Primary KPI | (i) Craft/portfolio bet + (ii) Distribution-learning bet. NOT revenue. |
| Repo | Separate from `rekko.ai`. |
| Platform-first | YouTube Shorts (MVP), then TikTok (Phase 2). |

## Appendix: Adversarial Risks Explicitly Accepted

| Risk | Accepted because |
|------|------------------|
| Legal exposure on celebrity content | Commentary-heavy framing matches TMZ / PopCrave pattern that survives. Lawyer consult pre-build is the mitigation. |
| Content ID takedowns at 20–40% rate | Operational cost absorbed by Daniel's dispute-queue handling. |
| Distribution skill gap | Reverse-engineering playbook (week 1) is the learning wedge. |
| Small revenue ceiling for the scope of build | Explicitly reframed as craft + distribution-learning bet, not revenue bet. Revenue is lag indicator only. |
| 10-year crawl fantasy | Descoped to 6–12 month rolling window. |
| Full-generative video replaces this approach | Bet is that VLM-annotated real-clip remix beats pure gen on authenticity signal for viral celebrity/news content. Unproven; accepting. |
