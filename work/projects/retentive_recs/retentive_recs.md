# System Context: Retentive Recommendations & The Prediction Engine
**Current Status: August 2026 — RR now Alim's (confirmed 8/21), Chuxi ws-TL visibly running the program; model-pUIC broke its lull with first LFU-cohort gains (unstable — reversion/restart plan in motion); novelty-definition redesign (Yidi) + CLR-relevance design (Zelun) + Chuxi's unify-into-RecGPT-structure 1-pager all landed the same week; weekly reading group launched**

> Technical reference content below remains accurate as of January/March 2026. August + July + May + April 2026 program status sections capture current results, narrative artifacts, and co-author roster. Read the August status section first; the technical content for architecture deep dives.

---

## Program Status — August 2026 Update (2026-08-22, from #puic-collab screenshots + Yidi's design doc)

### Model-pUIC: first real gains signal, and a disciplined validate-bigger plan

- **Chuxi + Devin Kreuzer (8/19): promising LFU-cohort results** for certain time ranges — **session gains + topline SSv2 proxy gains**. Caveats stated plainly: gains unstable (flip on/off when switching end days) and a **pre-AA on key metrics (MAU)**; LFU ≈ 53% of users, so her read is: run longer with more traffic for a stable reading. No traffic left at CG top level, so the plan is:
  1. `hf_model_pred_uic_cg` — **revert** (20 days in), keep **one enabled group (sizer=100, mv12) at 4%/group** — goal: validate a true LFU gain launchable for the LFU workstream.
  2. `hf_model_pred_uic_cg_v2` — **revert + restart with anchor/ratio-based subsequence sampling** (the new sampling strategy from the pUIC meeting) once Yidi's PR deploys. Yidi asked to run the reversions.
- **Yan Chen funnel analysis (8/21, via Armando's funnel-debugger tool,** variant `score_sort_enable_mv_12_size_100`**):** even at CG, model-pUIC isn't much more explorative than frontier sampling — the difference is in the funnel **survival curve: model-pUIC takes its deep drop at L1 Presort**, frontier sampling drops at Ranking. **Chuxi's mechanism: UIC CG overfetch ≈1x vs PS pUIC 5x** → the L1 Presort drop is expected (~5:1). *Concrete tuning lever identified: overfetch ratio.*
- **Yan Chen (8/21): both experiments loaded into the app.** Post-bug-fix: fewer impressed novel domains but **better adoption rate** (`hf_model_pred_uic_cg` v4); adding user-sequence sampling buys slight novel-domain gains **at the cost of adoption** (v2/v3). Added a new novel-content definition (14-day lookback of engagement by pincept domain, consistent with Helium's use-case adoption metric) — but flags it's weak for LFU (inactive 14 days → every CG looks explorative) → **UIC-based novelty definition is more informative**, especially once the long-UIC signal lands.

### Novelty-definition redesign (Yidi, design doc 8/22)

- **Diagnosis: the current mean-history similarity dilutes minority interests.** Worked example: a future nail-art pin against 3 nail-art + 7 food history pins scores novelty **0.704 by mean** but **0.13 by top-3** — the mean asks "close to the user's average?" when the right question is "close to *any* existing interest?"
- **Proposals, in order:** (1) **Top-K history similarity** (first experiment: mean vs K=1/3/5); (2) **cluster-aware max-centroid similarity** (cluster history, novelty = 1 − max centroid similarity — matches intended semantics directly); (3) later: discrete **SID-prefix / P2I-level** novelty labels (hierarchy joins; label-only at first, never a model input).
- **Eval discipline:** keep the legacy mean-based bucketized recall for run-to-run continuity, **add a strategy-aligned bucketized metric that shares the exact score implementation with training** (else train/eval silently disagree); overall retrieval recall stays the guardrail; make the action label configurable (currently hardcoded to repin) before multi-action labels land.

### The consolidation thread — RecGPT structure spreading into RR (strategic)

- **Zelun Wang (8/20): "Improving Condition Relevance in Homefeed CLR" — full design received 8/22.** **Problem:** HF CLR is trained primarily for engagement → underweights the request condition, over-relies on historical user preference — **a named blocker for pUIC**. Last year's attempt (relevance loss directly on the existing b head) reduced engagement; this design keeps engagement heads intact and adds a **dedicated relevance output** (b head serves engagement use cases; relevance output serves condition-focused ones like new-interest exploration). **Relevance teacher** (semantic condition↔candidate similarity, à la notif CLR): interest text = SearchSage 25c text emb vs OmniSage v1 pin emb · board = OmniSage board vs pin · pin = OmniSage source-pin vs pin. **Design A — user-aware relevance head:** parallel head on the existing CLR viewer tower, sees the same user+condition representation as the engagement heads but trains against the semantic teacher; init from pretrained CLR, joint training (freeze-then-unfreeze = optional later experiment). Pros: small change, preserves personalization, reuses pretrained b head + pin index, objectives co-adapt. Risk: user features still present → head can relearn historical-user bias instead of respecting the condition. **Design B — condition-only relevance head:** maps the condition embedding directly into the existing CLR pin-embedding space, bypassing user/engagement features. Pros: strongest condition-adherence guarantee, clean engagement/relevance separation, reuses pin tower + ANN index. Risk: user-agnostic → loses within-topic personalization. **Shared infra both ways:** teacher construction, pin tower + retrieval index, per-condition train/eval metrics, eval HTML (interest text / source-pin image), b-head engagement-regression monitoring. **Loss comparison:** pointwise MSE (preserves absolute teacher score) vs listwise KL (transfers relative ranking over a shared candidate set); unchanged pretrained HF CLR = no-distillation baseline. **Sequence:** shared infra → Design A → **stop-and-review gate** (relevance, engagement, qualitative, runtime) → Design B only if A still overweights user history. Alim engaged same-day ("this is awesome! I will take a look").
- **Chuxi: "2-in-1 pUIC prediction & retrieval via RecGPT structure" — full design received 8/22** (announced as 1-pager 8/21; credits Zelun's novelty training/eval implementation + PinnerFormer v2). **Problem:** current pUIC is 2-step — PinnerSage-style user tower emits a novelty embedding in raw-OSv1 pin space → passed into CLR as a "Pin" condition (serving: HFR L500 UFR → Scorpion `puic_user_tower` → `ps_puic_user` position-0 slice → CLR condition tower → prod pin index). First online ABs surfaced two gaps: (1) **novelty-embedding ↔ retrieved-pins mismatch** (CLR not trained with relevance loss — the exact gap Zelun's design attacks); (2) **not enough novelty jump** (novelty supply, mean-centroid over clustered history, heavyweight repin label). **Proposal:** collapse prediction + retrieval into RecGPT by adding a **novelty prompt `p_novel` (256-D, init from `p_repin`)** beside the five action prompts — a **side readout**: `q_novel = L2Norm(D_shared(concat(h₀, p_novel, step0_context)))`, never selected by the action-label extractor, trained with pUIC's novelty rank-weighted softmax (+ triplet ablation, softmax first). Benefits claimed: novelty and retrieval learned in one space (relevance gap closes by construction) + RecGPT's longer, feature-enriched sequence (SID available for coarse history compression) with no extra infra. **Training arms:** `P-novel` (freeze everything, train only the prompt row — clean capacity probe, reuses prod index) · `P-all` (prompts only) · `F-full` (full finetune from checkpoint — new index + strict standard-relevance guardrails) · `S-joint` (from scratch — max capacity, highest task-conflict risk). **Eval:** `enable_novelty_eval` tag; fixed global pos_seq_sim decile buckets applied to *every* prompt; headline = ΔHR@K(q_novel vs matched action prompt); HTML visualization with sanity checks (does q_novel retrieve lower-history-sim pins; **does it collapse to q_repin**; survival through dedupe/ranking). **Serving:** same model both roles — standard 6-iteration × 5-action autoregressive rollout unchanged; one extra q_novel decode from saved prefill h₀; q_novel isolated from `_produce_next_batch_inputs`/action sampling/standard compression; **append slot 30** (masked at fraction 0, versioned semantic offset); fixed-total budget 90% standard / **10% novel** (mirrors the PS-pUIC×CLR experiment budget for attribution).
- **Leo integration flags (8/22, for James to route or sit on):** (1) **The novelty definition inside Chuxi's design is the one Yidi's doc just falsified** — `w_novel`, triplet selection, and the eval buckets all score novelty against `mean(history)`, the exact mean-dilution flaw (nail-art example). Same-week docs, same channel: these two need to converge — Yidi's top-K/cluster-aware score should define both the training weight and the buckets, or the 2-in-1 trains toward and is graded by a miscalibrated label. (2) **Collapse risk:** init-from-p_repin + shared frozen decoder means the only pressure away from repin is the novelty weighting — the collapse check should be quantitative (q_novel↔q_repin similarity tracked per run), not just HTML eyeballing. (3) **Query-side fix, funnel-side gap:** a better novelty query still dies at Yan's L1 Presort drop if the overfetch ratio isn't fixed — the 2-in-1 addresses gap #1 and half of gap #2; the funnel plumbing is a separate, cheaper lever. (4) **Sequencing:** run P-novel first (256 trainable params, prod index, near-zero risk), escalate to P-all → F-full only on evidence — the doc lists the arms but doesn't commit the cheap-first order. (5) **Zelun-overlap roadmap question:** if 2-in-1 lands, pUIC no longer needs CLR relevance — but Zelun's design still matters for board/interest/pin conditions generally; someone should say which use cases each serves so they're complementary, not racing.
- **Leo strategic read:** the as-few-models-as-possible consolidation direction is now arriving bottom-up, with **RecGPT as the unifying architecture absorbing PS pUIC + the CLR handoff** — bridges the RR↔RecGPT workstreams, strengthens the "gains engine to scale" narrative for the November GenRet fork (RecGPT structure becoming load-bearing infra for RR raises the cost of parking it), and is independent corroboration the strategy is legible to the team — the same week Bella was asked for her strategy one-pager.

### Program health / org read

- **Weekly Retentive Recs Reading Group launched** in #puic-collab (join = read the paper beforehand + take a rotation slot).
- All of the above is landing in **Alim's month one with Chuxi as ws-TL visibly running the program** — reversion plans, funnel forensics, design docs, a reading group, cross-pod engagement (Yan, Yidi, Zelun/ATG, Devin K). **The RR handoff is producing, not stalling. James's role from here: amplify and observe; resist re-inserting as driver** (he remains the context-richest person in the space — that's exactly the temptation to manage).

---

## Program Status — July 2026 Update (2026-07-25)

### State: lull on launches, all-in on pUIC

- **No launch candidate in a while — a deliberate lull:** the team has been "pouring heart and soul" into the **two predictive-UIC tracks**. **LLM-based pUIC: not very performant right now. Model-based pUIC: better — but the serving path has been riddled with issues**, which James attributes to **Yuke's TL oversight** (see team_members_scope.md Yuke 6/23–7/25 arc).
- **Chuxi stepping deeper into model pUIC** (as the new TL) → things are improving and **Yidi is happier**. Trade-off accepted: **LLM pUIC slows down further.**
- **FBL win during James's China OOO:** **Olafur, Andreanne, and Armando landed a launch using FBL** (feedback loop). Still in the midst of **landing the FBL application in L1 / Retrieval.**
- **Cross-org cadence aligned** with **Yingjian (UU)** and **Zhenyu Tan (Sr. EM, ATG — confirmed 7/25; earlier Notif-side note superseded)** on project meeting cadence + who drives. **Chuxi and Anna supportive.** Q3 meeting structure (screenshot filed 7/25):
  - **[Weekly] Tuesday UIC Sync, 1pm PST** — Long/Dynamic/Hybrid UIC, cluster persistence, Feedback Loop, UEB + Explore surfaces. Runner: **Simin Li (UU)**; backups: Andreanne Lemay, James. Attendees — UU: Simin Li, Raymond Dinh, Sufyan Suliman, Bonds Gao; P13N: Andreanne Lemay, Chuxi, Alok, Armando, Yan Chen, Roderick Gao; Activation: Sepehr Valipour, Omar Nada, ZJ Jiang.
  - **[Bi-weekly] Wednesday LLM pUIC Sync, 1pm PST** — Runner: **Chuxi** (backup **Zelun Wang**). P13N: Ling Lan, Chuxi, Yan Chen, Armando; ATG: Zelun Wang, Logan Jeon, Xiangyi Chen; UU: Ruchen Zhen.
  - **[Weekly] Wednesday Model-Based pUIC Sync, time TBD** — Runner: **Chuxi** (backup Zelun Wang). P13N: Chuxi, Yidi, Ling Lan; ATG: Zelun Wang.
  - Read: **Chuxi runs both pUIC syncs; James is backup-only on UIC** — the delegation structure is already in place on paper.
- **Zelun Wang (ATG engineer in this space):** per his manager, may want to spend more time on both pUIC efforts — a leverage candidate.

### James's position (7/25)

- **This is James's single biggest time-sink since returning from China** — and the project where he holds the most context and understanding.
- **Staffing decision OPEN:** should RR get more engineers (more people running experiments)? Current inputs: **Alok** helping (came in this weekend) but high-maintenance; **Lionel** planned here (starts 7/27); possible **Zelun** leverage; question is whether even more firepower is warranted.

### Amplification: Jeff highlighting the blog post in #core-eng (2026-07-29)

- **Jeff's EA pinged James 7/29:** Jeff's weekly message to **#core-eng** will highlight the *Pinner Progression* Engineering Blog post; EA offered James edit rights on the blurb. Extends the amplification chain (blog 4/17 → CTO conference mentions → **Jeff org-wide highlight, week of 7/29**), days before the Aug 5 reorg announcement.
- Leo blurb rewrite (delivered in-session; James to send): centers **"persona-based recommendations"** powered by UIC, keeps the UCAN rule ("largest market"), adds the "WAU is historically very hard to move through recommendations alone" kicker, softens the clicks/saves knock. Verify before send: mirror the post's actual team credits; use the public WAU number if the post cites one.

---

## Program Status — May 2026 Update (2026-05-23)

### Headline shifts since April

1. **Three-word feedback loop launched on partial CG funnel — core RR hypothesis empirically validated.** The bandit / feedback-loop mechanism (Section 6 below) was the keystone bet — that explicit feedback over geometric regions increases retrieval efficiency. This is now empirically tested in production on part of the CG funnel with gains. **Next move: broader CG funnel rollout — expected to compound the gains.** For Director-narrative purposes: this is no longer "we believe feedback loops matter" — it's "we shipped and validated the bet."

2. **pUIC is now a dual-track program with two sequenced online proofs sequenced around James's OOO.**
   - **Model-based pUIC** — 2 engineers, recall metrics improving significantly offline, **online experiments end of May (before OOO)**. This is the cleaner-architecture, lower-risk track. Validates the "predict UIC at the model level" thesis with a real production lift signal.
   - **LLM-based pUIC** — large cross-team effort (Daniel Liu's team + James's team) on plumbing, pipeline, model. Initial results not great but **Dylan has provided feedback** on the predicted-UIC terms (LLM output quality is the load-bearing variable). James's VLM (visual user signature) work is feeding this track — interpretable user-state generation as input to the LLM prediction step. **Online experiments end of June (after return from OOO).** Risky-but-promising; the "this is where the field is going" track.

3. **KDD 2026 paper: full draft DONE.** James's three sole-author sections (Prior Work, Architecture, Future Work) plus the co-authored sections all closed. Paper deadline July 31, 2026 still holds; notification November 2026. The "Feedback Loop needs experiment results" dependency that was the open risk in April is also closed — see #1 above.

4. **Engineering Blog post shipped 4/17.** James publicly named program lead on Pinterest Engineering Blog. Externally legible Retentive Recs identity now established. Matt Madrigal (CTO) amplification chain confirmed at 5/4 EPD demo.

### Implications for Director narrative

The RR "Engine" story (per the Engine/Accelerator frame from 5/16) is now built on three load-bearing proof points: (a) UCAN WAU holdout-validated, (b) feedback loop hypothesis empirically validated on partial CG funnel, (c) two sequenced pUIC online proofs landing May/June. For the Dylan team-design conversation, this is exactly the "what's working under my current scope, here's what compounds when expanded" evidence base.

### Updated workstream status (week of 2026-05-23)

| Workstream | Status | Notes |
|---|---|---|
| **Program-level holdout** | ✅ UCAN WAU stable (carried) | Global still maturing; lead with UCAN externally. |
| **Three-word feedback loop / Geometric Bandit** | ✅ **LAUNCHED on partial CG funnel with gains** | Empirical validation of core RR hypothesis. Broader CG funnel rollout = next move with expected additional gains. |
| **Model-based pUIC** | Offline recall metrics improving significantly | **Online experiments end of May (before James OOO).** 2 engineers driving. |
| **LLM-based pUIC** | Plumbing + pipeline + model active; initial quality not great; Dylan-feedback informing | **Online experiments end of June (after return).** Cross-team with Daniel Liu's team. VLM signature work (James) feeding interpretable user-state generation. |
| **Heuristic pUIC** | Live, mostly neutral; positive for LFU (carried from April) | Forms the empirical anchor. |
| **Front-end experiment integration** | Landed (carried) | — |
| **KDD 2026 paper full draft** | ✅ **DONE** | Deadline July 31. Notification November. |
| **Pinterest Engineering Blog** | ✅ **SHIPPED 4/17** | James publicly named program lead. CTO-amplification chain confirmed at 5/4 EPD demo. |

### Open: VLM-as-pUIC-input architectural decision

James's VLM (Pinkerton visual user signature, V0 done 5/29 target) feeds the LLM-based pUIC track. The architectural question — *how the interpretable visual signature passes into the LLM prediction step* — is the load-bearing interface decision for whether the VLM work compounds the LLM-pUIC track or runs parallel to it. Pattern A (Pinkerton as data-API via MCP, reasoning lives in consumer) is the locked architectural decision per 5/16. Operational hookup TBD.

---

## Program Status — April 2026

### Headline result

**UCAN (US/CANADA) WAU gains are stable** in the program-level holdout. Global WAU gains across all regions are showing but **not yet stable** — do not broadcast globally yet, let the holdout mature.

**This is the holy-grail signal for the program.** A program-level holdout showing topline lift in the largest market is what proves the entire Retentive Recs bet — not a feature, not a sub-population win, but the validation that the architecture moves the needle at scale. WAU gains via ranking/CG experiments are historically rare in industry; achieving this in UCAN justifies every architectural decision in the technical sections below.

**Narrative implication for all artifacts:** Lead every external-facing narrative (KDD paper abstract, Pinterest Engineering Blog, blog posts, interview answers) with the **UCAN-specific framing** — "holdout-validated WAU gain in our largest market." Specific, defensible, won't get retracted if global wobbles.

### Status by workstream (week of 2026-04-07)

| Workstream | Status | Notes |
|---|---|---|
| **Program-level holdout** | ✅ UCAN WAU stable; global WAU not yet stable | Don't broadcast global gain prematurely. UCAN is the citable result. |
| **Heuristic pUIC** | Live, mostly neutral overall | **Positive for LFU (Low Frequency Users)** — retention gains may emerge over time. LFU is where the prediction thesis earns its keep (you can't anticipate the next interest of a high-frequency user). |
| **Model-based serendipity prediction** | Strong offline results | Online AB ~1 month out. Strongest forward signal for the prediction story. |
| **LLM-based pUIC** | Good qualitative prediction evaluations | No quantitative production data yet. Methodological frontier. |
| **Front-end experiment integration** | Landing | Going well. |
| **RL Feedback Loop / Geometric Bandit** | **Nearing completion — about to start AB (new 2026-04-11)** | Offline eval design done earlier; now implementation is wrapping and the team is preparing to launch the first online experiment. **This materially de-risks the KDD paper timeline** — the "feedback loop needs experiment results" dependency that Armando flagged is no longer an open-ended risk. If AB launches within the next 1-2 weeks, there is realistic runway to have real experiment data by the July 31 paper deadline. PinnerSage offline results remain the insurance if AB results run long. |

### The three prediction tracks (the live story for Anna's "claim 2")

The "predict next steps" novelty claim — Anna's biggest open question — is no longer aspirational. Three complementary tracks are running in parallel, each at a different evidence state:

1. **Heuristics** — fast-to-deploy, live in production, modest LFU gains. The empirical anchor.
2. **Model-based serendipity prediction** — strong offline results, online AB ~1 month out. The "this will work at scale" claim.
3. **LLM-based prediction** — good qualitative evaluations, no quantitative data yet. The "this is where the field is going" claim.

**Narrative frame:** "We attacked the prediction problem through three complementary approaches — fast-to-deploy heuristics, model-based serendipity scoring, and LLM-based qualitative prediction. Here's what each is telling us." This is more credible than overclaiming a single approach, and gives Anna's claim 2 immediate substance for the paper, the blog post, and any interview answer.

---

## Anticipation Vision — Authorship + CTO Amplification (April 2026)

Retentive Recommendations is the **named technical key** under Pinterest's company-wide Anticipation Vision (the vision for ALL of 2026 personalization). The vision authors **explicitly recognize Retentive Recs as the architecture that makes Anticipation possible.**

**Authors of the Anticipation Vision:**
- **Andrew Yaroshevsky** (Sr Director, Product — Anna's manager)
- **Dylan Wang** (Sr Director, Engineering — James's manager)
- **Mira** (Senior Director, Design)

**One-sentence frame:** "Pinterest should not just show you things you want, but anticipate what you might want next and show that to you instead."

**CTO surface area:** Andrew has pitched the Anticipation Vision to **Matt Madrigal (CTO of Pinterest)**. Matt has subsequently talked about it **openly at a conference**, naming it as one of the things he is most excited about for Pinterest personalization and ML/AI. The endorsement chain: Mira + Dylan + Andrew authored the vision → Andrew pitched to Matt → Matt amplified externally on the public record.

**Why this matters for Retentive Recs:** The vision the CTO is amplifying at conferences is built on James + Anna's architecture. This converts internal architectural recognition into external CTO-level visibility — but only if the team produces narrative artifacts (Engineering Blog, KDD paper) that name James in the loop. See artifact plans below.

---

## KDD 2026 Paper Plan

**Target:** KDD 2026 Applied Data Science track, July cycle.

**Page limit:** 9 pages with figures (8 with appendix).

**Authorship:** Multi-author. **James position: "I'll take any authorship" — explicitly not fighting for first author.** Three sole-author sections (Prior Work, Architecture, Future Work). Armando + Anna are load-bearing co-authors and are the operational engine of the paper.

### Section ownership

| Section | Author(s) |
|---|---|
| Abstract | (TBD) |
| Background | Anna Kiyantseva |
| Prior Work | **James Li** (sole) |
| Architecture | **James Li** (sole, with subsections below) |
| → Representation | Armando Ordorica, Jiacong He (departing — see below) |
| → → [Live Technical Doc] Improving Exploration/Exploitation Strategies at Pinterest | (linked) |
| → → Persistence → SID vs. other eval'd | (covered in subsection) |
| → Prediction | Armando Ordorica, Yuke Yan |
| → → Reference to how this connects w/ downstream reward | (in subsection) |
| → Federation | Armando Ordorica, Olafur Gudmundsson |
| Evaluation | Armando Ordorica |
| → Holdout | (covered) |
| Experiment Results | (TBD — depends on experiment landing) |
| Future Work | **James Li** (sole) — "Using cluster-level features as a sequence?" |

**Yuke delegation note:** Yuke is busy landing impact, but James will delegate Architecture/Prediction subsections to him to support Yuke's career and keep him invested. (See `stakeholders.md` §8 — Yuke is a flight risk; KDD paper is a career-aligned investment.)

### Anna's three novelty claims (the spine of the paper)

1. **Current representation is inadequate for broad longitudinal movements** → Board_create supervision of the sequence
2. **No ability to predict next steps** → THE BIGGEST OPEN QUESTION — but no longer aspirational; see Three Prediction Tracks above
3. **Ability to evaluate not just point-wise change but a categorical change of activity**

All three move topline / WAU. Claim 2 is where Retentive Recs intersects directly with the Anticipation Vision and Andrew's Reflex work.

### Armando's framing notes

- **Piggyback on OmniSage** (different inputs; MDD paper referenced methodology). Novel construction in a new domain. The way the components are pieced together is novel.
- **Double down on predicting NOT at the point-wise change.**
- **Feedback Loop + Explore/Exploit** now using composite rewards + applied at the user level (typically used for content exploration) + SID at the global level.
- **Need offline analysis to avoid "throwing shit at the wall" framing.**
- **Feedback Loop has good offline eval design — needs experiment results.**
- **PinnerSage predictions offline results look really good.** Insurance: provides defensible story even if live experiments don't fully bake by July 31.

### James's defense-prep gap (architecture section)

**OmniSage piggyback is fragile under reviewer scrutiny.** James needs a one-paragraph "what's reused, what's novel, why the new construction is non-trivial" defense ready before draft v1. Don't let Armando be the only one who can answer "what's actually novel here." This is the Architecture author's job.

### Timeline + risks

| Date | Milestone |
|---|---|
| End of April 2026 | Soft draft + thoughts |
| Beginning of May 2026 | Next sync (full team) |
| End of April + 1-2 weeks | Bring in additional contributors |
| **July 24, 2026** | Abstract deadline (KDD ADS July cycle) |
| **July 31, 2026** | Paper deadline |
| October 4-18, 2026 | Author rebuttal period |
| November 23, 2026 | Notification |

> Note: James's notes had 2025 dates from a copy-paste error; KDD 2026 ADS July cycle dates corrected above.

**Key risk:** If the Feedback Loop / Geometric Bandit experiment results don't land in time for July 31, paper slips → KDD slot lost → fall back to next cycle. PinnerSage offline results are the insurance.

**Update 2026-04-11:** Feedback Loop work is **nearing completion and about to start AB**. This materially de-risks the paper timeline — the "needs experiment results" dependency is closer to resolving. Watch for AB launch timing in the next 1-2 weeks; if it lands cleanly, real experiment data by July 31 is realistic.

**Setup:** Armando to set up new repo + Cursor setup for the team.

---

## Pinterest Engineering Blog Plan

**James is the named program lead in this artifact.** This is the externally-visible Pinterest Engineering Blog post that publicly identifies James as leading Retentive Recommendations.

### Status (2026-04-11)

- **Draft exists.** Jiacong He wrote a draft.
- **Jiacong is leaving the company.** He is on the **blending team** — minimal impact on James's team retention. But his departure means the editor role is open.
- **James is taking the editor role.** Committed 2026-04-11. Rationale: being named as program lead requires *being* the lead on the publication itself. Punting the editing means losing the recognition by default.
- **Anna was hesitant** when James subtly floated her taking the editor role. Acceptable — Anna + Armando are load-bearing for the KDD paper, which is its own multi-week effort. Engineering Blog editing should not pull her off KDD.

### James's editor scope

1. **Inherit Jiacong's draft.** Get the file before Jiacong is offboarded; verify completeness.
2. **Corral cross-team engineers for final edits.** This is the hard part — multiple teams contributed; final edits need each team's sign-off. James as program lead is the one with the authority to drive this.
3. **Insert the UCAN WAU headline.** Lead with the validated result.
4. **Coordinate with Pinterest Engineering Blog editorial process.** Likely a content / marketing review step.
5. **Land the post.** Target date TBD — aim for end of April / early May to align with KDD paper draft cadence and to capitalize on Matt Madrigal's continued external amplification.

### Why this is the highest-leverage 5-10 hours of work for the Director conversation

- **Effort:** Editing existing draft + corralling cross-team engineers ~ 5-10 hours over 1-2 weeks. Lower than writing from scratch.
- **Leverage:** Pinterest Engineering Blog post naming James Li as program lead on a project that just shipped UCAN-stable WAU gains, in a vision the CTO is amplifying at conferences. **This is the externally-visible artifact closest to the Anticipation Vision narrative.**
- **Counterfactual:** If James doesn't take this, the framing drifts. Punting is structurally damaging for the Director case.

---

## Co-Author Roster (April 2026)

| Person | Role | Notes |
|---|---|---|
| **James Li** | Program lead (Engineering Blog) + KDD paper author for Prior Work, Architecture, Future Work | Named lead on Pinterest Engineering Blog publicly. Editor role taken from Jiacong 2026-04-11. |
| **Anna Kiyantseva** | PM partner / Background author / political amplifier | Inner Circle ally. Reports to Andrew. Hesitant about editor role — keep her on KDD paper Background. |
| **Armando Ordorica** | KDD paper operational engine — Representation, Prediction, Federation, Evaluation | Load-bearing. Setting up new repo + Cursor for the team. NEW stakeholder — needs entry in stakeholders.md. |
| **Yuke Yan** | KDD paper Prediction co-author | IC15, Retentive Recs TL. Flight risk per stakeholders.md §8. James will delegate sections to support his career. |
| **Olafur Gudmundsson** | KDD paper Federation co-author | NEW stakeholder — needs entry in stakeholders.md. |
| **Jiacong He** | Original Engineering Blog draft author + KDD Representation co-author | **Leaving the company.** On blending team. Minimal team retention impact. James inheriting his Engineering Blog editor role 2026-04-11. KDD Representation likely absorbs into Armando. |
| **Chuxi Wang** | Primary IC for Retentive Recs (per stakeholders.md §8) | Promo vehicle is p(UIC). Now also 20% Pinkerton commit going forward. |

---

## 1. Core Objective: Solving the "Serendipity" Problem
**Transitioning from Reactive Exploitation to Proactive Prediction.**

Historically, the industry has struggled with the "Explore / Exploit" dilemma. "Exploit" algorithms are efficient but lead to boredom and decay, while "Explore" algorithms often fail because they rely on random "undirected leaps" or generic popularity, which users perceive as irrelevant noise. The "Holy Grail" is **Serendipity**: showing the user something they didn't know they wanted, but which feels immediately relevant.

The **Retentive Recommendations** program solves this by operationalizing **User Interest Clusters (UIC)**. By moving from simple pattern matching to **Geometric Prediction** and **LLM-Based Reasoning**, we engineer serendipity—delivering exploration that is "sensible," personalized, and structurally aligned with the user's real life.

### **January 2026 Status Update: Validation**
As of January 2026, we have successfully validated the core thesis. By leveraging UICs as a superior form of user representation in our ranking stack, **we have achieved statistically significant lifts in both engagement and retention metrics.**

Moving retention via ranking experiments is historically rare and difficult, as retention is typically a lagging indicator driven by product market fit rather than algorithm tuning. Achieving this lift confirms that **UIC is the correct atomic unit for long-term pinner value**, validating our move to the next phase: **Prediction**.

---

## 2. The Data Foundation: User Interest Clusters (UIC)
The atomic unit of this system is the **User Interest Cluster (UIC)**. It replaces rigid taxonomy with dynamic "Use Case Clouds" located in a universal embedding space.

### 2.1. The OmniSage Representation
The power of the UIC is derived from its underlying embedding space, **OmniSage**, which uniquely fuses three distinct signal layers:
1.  **Visual & Semantic (CLIP):** Encodes the raw "meaning" of content (e.g., a hiking boot looks like a shoe).
2.  **Interaction Graph (Engagement):** Encodes user preference by clustering items that are co-engaged by the same user.
3.  **Social Graph (Pin-Board Topology):** Encodes "utility" by clustering items that are curated together on the same boards by the community.

**Result:** In OmniSage, "closeness" represents **functional utility**, not just visual similarity. A *hiking boot* and a *granola bar* are neighbors because the Graph connects them via "Hiking Trip" boards. This allows us to represent nuanced, unlabeled behaviors (e.g., "Minimalist Apartment Gardening") without needing explicit taxonomy labels.

### 2.2. UIC Signal Composition
A UIC is an **externalized feature** stored in the GSS Feature Store, enabling low-latency access across the stack.
* **Centroid/Medioid:** The coordinate center of the cluster in OmniSage space.
* **Action Counts:** Aggregated interactions (Repins, Closeups, Clicks, Search) associated with the cluster.
* **Cluster Variance:** Statistical measures (Min, Max, P50, Std Dev) of cosine similarity within the cluster, indicating "tightness" or "focus".
* **Temporal Distribution:** Time buckets to track interaction velocity (e.g., is this cluster accelerating or decaying?).

### 2.3. Stateful Lifecycle Management
Unlike static profiles, UICs carry state metadata that dictates system behavior:
* **Enticement:** High exploration, low efficiency threshold. Focus on gauging receptivity.
* **Activation:** Refinement of scope. Success metric = Board Creation ("Sealing the deal").
* **Stabilization:** Exploitative reinforcement. Success metric = Efficiency/Repins.
* **Re-evaluation:** Managed decline. Success metric = Proactive pivoting to new use cases via extinction or re-introduction.

---

## 3. Geometric Prediction Strategies
Leveraging the continuous nature of the OmniSage embedding space, we employ **Geometric Prediction** to navigate users to their next interest.

### Strategy A: Vector Transport (Trajectory Prediction)
We treat user evolution as a physics problem involving drift through the embedding space.
* **Concept:** Users do not jump randomly; they flow through adjacent concepts (e.g., *Apartment* $\rightarrow$ *Balcony* $\rightarrow$ *Gardening*).
* **Mechanism:** By analyzing the historical paths of the "Golden Cohort" (retained users), we calculate **velocity vectors** for any given coordinate.
* **Application:** If a user is at Coordinate $A$, we apply the population-level velocity vector $\vec{v}$ to predict their arrival at Coordinate $B$, seeding content from $B$ before they explicitly search for it.

### Strategy B: Graph Completeness (Topological Prediction)
We leverage the "Pin-Board Graph" structure to identify missing functional components of a Use Case.
* **Concept:** A complete Use Case (e.g., "Camping") has a specific graph topology connecting *Gear*, *Locations*, and *Food*.
* **Mechanism:** The system scans the user's current UIC. If the user has dense nodes for *Gear* and *Locations* but a "structural void" where *Food* normally exists in the OmniSage graph, the system predicts *Food* as the next high-utility node.
* **Application:** Recommending items that "complete the set" based on graph topology rather than generic popularity.

### Strategy C: Sensible Sourcing (Cluster Collision)
We solve the "Cold Start" and "Undirected Leap" exploration problems by calculating the geometric intersection of existing clusters.
* **Concept:** "Serendipity" is finding the logical bridge between known interests.
* **Mechanism:** If User has $UIC_1$ (Vegan Cooking) and $UIC_2$ (Budget Travel), we query the embedding space for the **Centroid** between $UIC_1$ and $UIC_2$.
* **Application:** The system recommends "Vegan Camping Food"—a niche located mathematically between the two existing clusters, ensuring exploration feels personalized and safe.

### Strategy D: Synthetic Profiling
* **Concept:** Low-signal users are volatile due to sparse data.
* **Mechanism:** We match a low-signal user's fragment (e.g., 2 clicks) to a mature "Synthetic Cluster" aggregated from thousands of similar users.
* **Application:** We "spoof" a robust profile to immediately provide depth and diversity, bypassing the "training wheels" phase.

---

## 4. The Reasoning Engine (LLM/VLM Integration)
The UIC acts as the bridge between raw behavioral data and high-level reasoning capabilities.

* **The Problem:** Traditional recommenders match patterns ("bought hammer" $\rightarrow$ "buy nails"). They do not understand *intent*.
* **The Solution:** We treat the UIC as a **Dynamic Prompt** for LLMs and VLMs.
* **Workflow:**
    1.  **Input:** The VLM ingests the visual/semantic tokens of the pins within a UIC (e.g., images of wood, blueprints, saws).
    2.  **Reasoning:** The Model deduces the real-world objective: *"The user is building a deck."*
    3.  **Generation:** The Model generates a "Next Best Action" plan: *"After building, they will need staining and furniture."*
    4.  **Output:** The system queries OmniSage for "Wood Staining" and "Outdoor Furniture" clusters, effectively recommending a **future timeline** rather than just a similar product.

---

## 5. Operational Architecture
The UIC signal is integrated into the entire Homefeed stack via the **User Feature Representation (UFR) Node**.

### 5.1. Candidate Generation (CG)
* **Conditioning:** UICs serve as the "condition" input for Conditional Learned Retrieval models.
* **Retrieval:** We fetch candidates that are chemically close to the UIC medioid, or "predicted" coordinates based on Geometric Strategy.

### 5.2. Utility & Ranking (L1/L2)
* **Weight Tuning:** We create specific utility weights based on the UIC's lifecycle state.
    * *Enticement State:* Higher weight on **Closeups/Clicks** (signaling curiosity).
    * *Stabilization State:* Higher weight on **Repins/Saves** (signaling utility).
    * *Re-evaluation State:* Down-weighting of engagement signals to allow for decay and replacement.

### 5.3. Diversity (SSD)
* **Logic:** We enforce diversity *between* UICs (broadening) and *within* UICs (deepening).
* **Mechanism:** The diversity scorer ensures the feed isn't dominated by a single "Stabilized" cluster, explicitly reserving slots for "Enticement" clusters derived from Geometric Prediction.

---

## 6. Strategic Imperatives
This architecture serves as the "Operating System" for Pinterest’s key strategic bets:

1.  **Retention (MAU $\rightarrow$ WAU):** By predicting UIC decay and proactively seeding the next use case, we create a continuous chain of value, preventing the "empty feed" experience that leads to churn.
2.  **AI Forward (Agents):** AI Agents require context to be useful. The UIC provides a portable, pre-computed "Theory of Mind" for the user, allowing agents to understand *who* they are helping instantly (e.g., "I know you are a vegan budget traveler").
3.  **Explore (Use Case Expansion):** Moving Explore from "Random Popularity" to "Sensible Sourcing" allows us to safely expand users into new verticals, driving the multi-use-case depth that correlates with long-term retention.

---

## 7. Strategic Alignment: Powering the "Anticipation" Vision
Retentive Recommendations is not a siloed ranking project; it is the **technical engine** that makes the company-wide **"Anticipation"** vision  possible.

### 7.1 The "Brain" of Anticipation
The "Anticipation" strategy centers on moving users from *reactive matching* to *predictive journeys*.
* **The "What":** The company vision calls for "Journey Jumps" (predicting the s'mores bar after the firepit).
* **The "How":** Retentive Recommendations provides the **Geometric Prediction** capabilities (Vector Transport, Graph Completeness) required to execute these jumps reliably. Without the UIC's ability to model trajectory in embedding space, "Anticipation" remains an abstract concept without a delivery mechanism.

### 7.2 Enabling "Downstream Rewards"
A key pillar of Anticipation is shifting incentives from short-term clicks to long-term value.
* **The Mechanism:** Our work on **UIC Lifecycle Management** (detecting decay in "Stabilized" clusters and injecting "Enticement" clusters) is the operational implementation of Downstream Rewards. We are building the system that explicitly trades short-term efficiency for long-term retention health.

### 7.3 The Portable Signal for "Cross-Surface Action"
Anticipation requires a coherent experience across Homefeed, Search, and Notifications.
* **The Enabler:** The UIC is designed as an externalized feature in the GSS Feature Store, making it a portable "User State" that can be accessed by the **Unified P13N Platform (UPP)**.
* **The Impact:** When Homefeed predicts a "Camping" journey via UIC, that same signal is instantly available to Notifications (for "Camping Gear" alerts) and Search (for personalized query suggestions), ensuring the "Anticipation" effect is felt ubiquitously.

# Technical Specification: Retentive Recommendations & The Prediction Engine
**Version:** 2.0 (January 2026)
**Domain:** Homefeed Discovery / Personalization
**Status:** Validated / Scaling Phase

---

## 1. Executive Summary: The Engineering of Serendipity
Traditional recommendation systems face the **"Explore/Exploit" dilemma**: "Exploit" algorithms drive short-term efficiency but cause long-term churn through boredom; "Explore" algorithms often fail due to relevance noise. 

**Retentive Recommendations** solves this by shifting the paradigm from **Reactive Matching** (logging history → finding lookalikes) to **Geometric Prediction** (mapping trajectory → anticipating future state).

The core thesis—now validated by statistically significant retention lifts—is that **User Interest Clusters (UIC)** represent the correct atomic unit for modeling long-term user value. By leveraging UICs within an **OmniSage** embedding space, we can engineer "serendipity": exploration that is mathematically adjacent to confirmed utility rather than randomly sourced.

---

## 2. Core Abstraction: User Interest Clusters (UIC)
The UIC replaces rigid taxonomy with dynamic "Use Case Clouds" rooted in a high-dimensional vector space.

### 2.1 The OmniSage Embedding Space
UICs do not exist in isolation; they are coordinates within **OmniSage**, a fused latent space that encodes three distinct signal layers[cite: 1644, 2266]:
1.  **Visual/Semantic Layer (CLIP):** Encodes raw pixel/text meaning (e.g., *Hiking Boot* $\approx$ *Running Shoe*).
2.  **Interaction Graph:** Encodes user preference via co-engagement (e.g., Users who click *Hiking Boot* also click *Granola Bar*).
3.  **Topology Graph (Pin-Board):** Encodes functional utility via curation (e.g., *Hiking Boot* and *Tent* coexist on "Camping" boards).

**Technical Definition:** A UIC is a tuple defined as $C_i = \{ \vec{\mu}_i, \Sigma_i, T_i, A_i \}$, where:
* $\vec{\mu}_i$: The **Medioid vector** representing the cluster center in OmniSage space.
* $\Sigma_i$: **Cluster Variance** (Min, Max, P50, Std Dev of internal cosine similarity), representing "focus."
* $T_i$: **Temporal Distribution**, modeling the velocity/decay of the interest.
* $A_i$: **Action Vectors**, aggregated interaction counts (Repins, Closeups, Clicks, Search)[cite: 1645].

### 2.2 Signal Construction (L500 Sequence)
The UIC signal is constructed in real-time from the user's **L500 sequence** (last 500 actions).
* **Clustering Algorithm:** Complete-link hierarchical clustering is performed on the sequence.
* **Merge Criteria:** Events merge only if similarity exceeds a threshold $\theta$ relative to *all* events in the target cluster, ensuring high coherence[cite: 2583].
* **Externalization:** Computed UICs are stored in the **GSS Feature Store**, enabling low-latency access across CG, Ranking, and Diversity stages without re-computation[cite: 2938].

#### Clustering Parameters (v2)
The clustering logic is governed by the following configuration. The *underlined* parameters are primary candidates for experimentation.

```json
clusterParamString = {
    "viewName": "ssuliman_testing",
    "version": "CLUSTERED_OMNISAGE_V1_EMBEDDING",
    "eventCountThreshold": 1000,
    "clusterLimit": 25,                 // Max clusters per user
    "dimension": 32,                    // Embedding dimension
    "similarityThreshold": 0.5,         // Threshold for merging events into cluster
    "maxLandmarks": 30,                 // Max landmark images per cluster
    "actionTypesForClustering": ["PIN_REPIN", "PIN_CLOSEUP"],
    "customizedActionWeights": {
        "PIN_REPIN": 2.0,               // Repins weighted 2x vs Closeups
        "PIN_CLOSEUP": 1.0
    },
    "sampleMethod": "NONE",
    "queryRewardFunc": "REPIN_CLICK",
    "actionTypesForBackfilling": [],
    "useMedoidAggregator": True,
    "actionTypeCount": Map<ActionType, Integer>,
    "skipLshTermGeneration": True,
    "appendStats": True,
    "computeClusterWeight": True
}
---

## 3. The Prediction Engine: Geometric Strategy
*Status: Heuristic MVP Phase*

We reject generic "diversity" heuristics (e.g., random noise). True prediction requires modeling **Momentum** and **Composition**. We employ two deterministic geometric strategies to generate "Predicted UICs" that serve as seed queries for the Candidate Generator (CLR).

### 3.1 Strategy A: Time-Vector Extrapolation (Momentum)
We treat user interest not as a static point, but as a vector with velocity. We assume the user's interest is drifting *away* from the center of the cluster towards their most recent interactions.

* **Logic:** $Trajectory = \text{Recent} - \text{History}$
* **Calculation:**
    1.  Identify the **Cluster Medoid** ($\vec{\mu}_{UIC}$): The geometric center of the cluster (The "Average").
    2.  Identify the **Temporal Edge** ($\vec{p}_{latest}$): The embedding of the most recent interaction *assigned* to this cluster.
    3.  Compute the **Drift Vector**: $\vec{v} = \vec{p}_{latest} - \vec{\mu}_{UIC}$.
    4.  **Prediction:** $\vec{target} = \vec{p}_{latest} + \lambda \vec{v}$ (where $\lambda$ is a scalar, typ. 0.5 - 1.0).
* **Outcome:** If a user moves from *Basic Baking* $\rightarrow$ *Sourdough*, the vector points toward *Fermentation*. We retrieve from *Fermentation* before the user searches for it.

### 3.2 Strategy B: Geometric Mixups (Sensible Sourcing)
We solve the "Cold Start" exploration problem by calculating the geometric intersection of existing clusters. This mimics "compositional reasoning" in the embedding space.

* **Logic:** Serendipity is often the bridge between two known interests.
* **Calculation:**
    1.  Select Top 2 strongest UICs: $UIC_A$ and $UIC_B$.
    2.  **Topology Check:** Verify $UIC_A$ and $UIC_B$ have non-zero co-occurrence in the global Pin-Board graph (prevents "Frankenstein" merges like *Motorcycles* + *Cupcakes*).
    3.  **Prediction:** $\vec{target} = \text{Slerp}(\vec{\mu}_A, \vec{\mu}_B, 0.5)$.
* **Outcome:** User has `Mid-Century Modern` and `Cats`. The midpoint vector retrieves `Mid-Century Cat Furniture`.

### 3.3 Strategy C: Graph Completeness (Topological Prediction)
We leverage the "Pin-Board Graph" to identify **structural voids** in a use case.
* **Mechanism:** A complete use case (e.g., "Camping") has a known topological structure connecting nodes like *Gear*, *Location*, and *Food*.
* **Execution:** The system scans the user’s UIC. If nodes for *Gear* and *Location* are dense but *Food* is sparse/absent, the system identifies the "missing centroid" required to complete the graph topology and boosts those candidates.

### 3.4 Strategy D: Cluster Collision (Sensible Sourcing)
We solve the "Cold Start" exploration problem by calculating geometric intersections.
* **Mechanism:** If User has $UIC_A$ (Vegan Cooking) and $UIC_B$ (Budget Travel), we query OmniSage for the **Geometric Median** between $\vec{\mu}_A$ and $\vec{\mu}_B$.
* **Execution:** The system retrieves "Vegan Camping Food"—a niche located mathematically between existing clusters, ensuring exploration is "safe" and personalized.

### 3.5 Strategy E: Synthetic Profiling
We mitigate volatility in low-signal users (LSU) via "Synthetic Clusters."
* **Mechanism:** LSUs lack sufficient data for stable clustering. We match LSU fragments (e.g., 2 clicks) to mature "Synthetic Clusters" aggregated from thousands of high-signal users with similar initial trajectories.
* **Execution:** We "spoof" a robust profile for the LSU, immediately enabling depth and diversity recommendations.

---

## 4. The Reasoning Layer: LLM Integration
We treat the UIC as a **Dynamic Prompt** for Large Language/Vision Models.
* **Input:** VLM ingests visual tokens from pins within a UIC (e.g., *wood, blueprints, saw*).
* **Inference:** The model deduces intent ("Building a deck") and generates a "Next Best Action" plan ("Needs staining").
* **Output:** The system queries OmniSage for the "Wood Staining" cluster, essentially recommending a **future timeline**.

---

## 5. Operational Architecture
The architecture is federated across the entire Homefeed stack via the **User Feature Representation (UFR) Node**.

### 5.1 Candidate Generation (CG)
* **Conditional Learned Retrieval (CLR):** We deprecate the "Followed Interests" logic. Instead, the CLR two-tower model accepts the **UIC Medioid** $\vec{\mu}_i$ directly as a "condition" input.
* **Efficiency:** This reduces "overfetch" ratios (fetching candidates irrelevant to the current user state), generating significant infra cost savings (approx. 322k/year projected).

### 5.2 Ranking (Pinnability) & Utility
* **Composite Labeling:** Instead of adding new heads (which increases latency), we use **Curriculum Learning** via composite labels.
    * *Standard Label:* `repin`
    * *Composite Label:* `repin` + `new_use_case` (where `new_use_case` is defined by distance > threshold $\delta$ from existing UICs).
    * **Weighting:** Composite positives are weighted $2\alpha$ vs standard $\alpha$, forcing the model to learn "exploration" as a high-value trait.
* **State-Dependent Utility:**
    * *Enticement Phase:* Utility function boosts **Closeups/Clicks** (curiosity signals).
    * *Stabilization Phase:* Utility function boosts **Repins/Saves** (commitment signals).

### 5.3 Diversity & Blending
* **Inter-Cluster vs. Intra-Cluster:** The diversity scorer explicitly allocates slots to distinct UICs to prevent feed collapse.
* **Mechanism:** We reserve slots specifically for "Enticement" clusters (derived from Prediction Strategies) to ensure the feed is never 100% "Stabilization" content.

---

## 6. Feedback & Reinforcement: The Geometric Bandit (New)
*Status: Design Phase*

To prevent "Zombie Clusters" (interests that persist despite disengagement) and "Infinite Exploration" (randomly showing new topics forever), we implement a **Thompson Sampling Bandit**.

**CRITICAL ARCHITECTURE DECISION:** We explicitly **DEPRECATE Semantic IDs (SIDs)** for reward tracking. SIDs cause "Signal Bleed" (aliasing distinct user interests into generic categories). We instead use **Geometric Hashing**.

### 6.1 The Geometric Key (LSH)
We track rewards based on the specific region of the embedding space the user is interacting with.

* **Key Generation:** `LSH_Key = SimHash(UIC.medioid, bits=16)`
    * *SimHash* preserves cosine similarity. Similar vectors hash to the same key; dissimilar vectors hash differently.
* **Storage:** `Map<User_ID + LSH_Key, Beta_Distribution_Params>`
* **Advantage:** "Glamping" and "Survivalist Camping" are geometrically distant. They generate different LSH keys, ensuring the user's dislike of one does not penalize the other.

### 6.2 The Reward Function: Log-Lift
We optimize for **Momentum**, not absolute Click-Through Rate (CTR). High-volume, stale interests should not crowd out low-volume, growing interests.

* **Formula:** $R_t = \log(\frac{CTR_{current} + \epsilon}{CTR_{baseline} + \epsilon})$
    * $CTR_{current}$: Engagement in the current session/window.
    * $CTR_{baseline}$: The user's historical average for this LSH key (or global average if new).
* **Negative Feedback:** "Fast Scroll" or "Hide" actions are treated as explicit penalties (reducing the $\alpha$ parameter in the Beta distribution), forcing the confidence interval to collapse immediately.

### 6.3 Sampling Logic (Thompson)
At serving time, we do not rank clusters by their raw score. We sample from their Beta distributions.
* **Stabilized Clusters:** Have narrow distributions (High confidence).
* **Predicted/New Clusters:** Have wide distributions (Low confidence).
* **Result:** The bandit naturally "explores" the wide distributions occasionally. If the user engages (Log-Lift), the mean shifts right. If they ignore, the mean shifts left and variance decreases (stopping exploration).

---

## 7. Strategic Alignment: "Anticipation"
This architecture is the technical engine for the company-wide **Anticipation** vision.

* **Journey Jumps:** By implementing **Vector Transport**, we move from "reactive matching" to "predictive jumps" (e.g., Firepit $\rightarrow$ S'mores).
* **Downstream Rewards:** By managing **Lifecycle States**, we explicitly trade short-term CTR for long-term retention (WAU), optimizing for the "Golden Cohort" trajectory rather than the "Clickbait" trajectory.
* **Cross-Surface Portability:** Because UICs are externalized in GSS, the "Predicted Next Interest" is available instantly to **Search** (query suggestions) and **Notifications** (alerting), creating a unified "Theory of Mind" for the user across the platform.

---

## 8. James's Framing: The Three Key Innovations (March 2026)

This section captures how James frames the core innovations of Retentive Recommendations — useful for interview prep, stakeholder comms, and learning agenda alignment.

### Innovation 1: Personalized Interest Representation
We moved beyond a global interest definition into a personalized one. We don't cluster over all possible pins, but rather cluster over only the pins the user has engaged with. This makes a much easier problem and a much more accurate representation. Improvements:
- Longer history (L500 sequence instead of shorter windows)
- Dynamic cluster count (not fixed categories — users with diverse interests have more clusters)
- Complete-link hierarchical clustering ensures high coherence within each UIC

### Innovation 2: Embedding-Space Prediction at the Interest Level
We are predicting a point in space in the embedding space where the user is likely to engage, using what they have historically already engaged with. This is fundamentally different from pin-level prediction. This is "use case" or "interest level" prediction personalized to the user. The Geometric Prediction strategies (Vector Transport, Sensible Sourcing, Graph Completeness) all operate at this level — predicting where in the embedding space the user is heading, not which specific pin they'll click.

### Innovation 3: The RL Feedback Loop
How we build an actual feedback loop to do reinforcement learning for explore-exploit, to make sure we thoroughly and effectively explore the different regions of the embedding space for each user. The Geometric Bandit (Thompson Sampling over LSH keys with Log-Lift reward) is the mechanism. This is novel because:
- Exploration is systematic and trackable (per-region Beta distributions)
- Reward measures momentum (Log-Lift) not absolute engagement
- Negative feedback collapses exploration immediately (no zombie clusters)
- The bandit handles the explore/exploit tradeoff automatically through posterior width