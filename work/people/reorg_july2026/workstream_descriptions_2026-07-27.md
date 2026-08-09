# Workstream Descriptions — per-project reference (2026-07-27)

> **⚠️ READ FIRST — 2026-08-02 corrections. This is a dated 7/27 record; the body below is preserved as written, but four things in it are now wrong. Do not propagate them (this doc feeds the EM primer).**
> 1. **RecGPT / GenRet is a gains engine, not a time-boxed incubation.** The "explicit graduation/sunset criteria" and "graduates to Anticipation Modeling at settle" framing is **RETIRED** (James, 8/2: *"GenRet is gains producing and we just need to increase its impressions and make it more gains producing"*). No criteria artifact is owed. **Bella moves with the charter.**
> 2. **Team names changed hands.** "Anticipation Modeling" is not a live team name — Alim's team is **Retrieval Modeling**; Daniel's is **Curation ML**. Any "→ Anticipation Modeling at settle" reads as the T2 open question, not a decision.
> 3. **Intelligent Boards is a funded strategic bet**, not boards ballast — funded under Andrew Yaroshevsky's anticipation vision, with Balaji sprinting the prototype. IB is the **mid-funnel adoption step** after the pin-level exploration module (top of funnel).
> 4. **Recommended Boards is deliberately slow-played** — starved of funding rather than divested, pending product direction (James, 8/2).
>
> Current T2 design record: `p13n_retrieval_split.md`.

> **2026-08-08 layer — T1 Workstreams & Leads locked in James's accountability doc (system of record now: `p13n_retrieval_em_primer.md` §4).** Ten areas, one TL + one EM each: 1 UPP Retrieval (Piyush/James) · 2 CLR (Devin/James) · 3 Lightweight Scoring (Yali/James) · 4 Responsiveness + L1 Utility (JJ/James) · 5 Retentive Recs (UIC, pUIC) — three-legged: Retrieval Chuxi/Alim · Blending Andreanne/Rahul · UU Simin/Yingjian · 6 Unified Explore Backend (Roderick/Daniel) · 7 LLM for Recommendations (Balaji/Daniel) · 8 Collection Personalization (Yongwoo/Daniel) · 9 Reflex (Dafang/James) · 10 RecGPT / Generative Retrieval (Bella/James). Prioritized cross-org initiatives: Content Exploration (Bella/James — **NEW**), Content Quality (JJ/James), See More/See Less (Yali/James), NLFU Growth (ISR JJ · Modeling Devin / James). Note LWS and L1 Utility are now **separate areas** (modeling engine vs. business-control layer) — the matrix below predates the split.
>
> **ME DEFUNDED (James confirmed 8/8 — first explicit record anywhere in the repo):** Multi-Embedding gets no further investment; paradigm consolidation with RecGPT (two next-gen retrieval paradigms competing for one candidate budget — RecGPT won on ceiling, #1 CG on HF by Apr 2026; 150 sizers transferred ME→RecGPT in H1 2026; ME to maintenance). Full record: primer §3 "Multi-Embedding — built, published, sunset."

**Purpose:** deliverable 1 of the 7/27 session — one entry per workstream. Each entry has a **doc-ready description** (exec-safe, pasteable into the org GDoc's Workstreams & Leads / Mission cells), **current state** (internal, as of 7/27 — do NOT paste), and **ownership**. Sources: `org_design_doc_2026-07-24_exec_voice.md`, `org_design_proposal_2026-07_v2.md`, project files (`upp_retrieval_em.md` 7/25, `retentive_recs.md` 7/25, `reflex_program_state_2026-07.md`, `l1_utility.md`, `nlfu_support_2026.md`, `cost_investigation_2026.md`), `daniel_liu_team_2026-07.md`.

**Team names (LOCKED 7/24):** Retrieval Foundations (James) · Retrieval Modeling (Daniel) · Anticipation Modeling (Alim). **Org name (LOCKED 7/25): "Personalization Retrieval and Anticipation."**

---

## Dimensions matrix (annotation layer, added 7/27)

Legend: **●** delivering now · **◐** candidate / in-flight · **○** not currently. Role = James's portfolio frame (substrate / engine / bet / ballast / accelerator). XFN = cross-org heat (exposure + coordination load).

| # | Workstream | Team | SSv2 | WAU/Ret | Cost | 0-to-1 | Role | Pager | XFN |
|---|---|---|---|---|---|---|---|---|---|
| 1 | UPP | James | ◐ | ○ | ○ | No — standing framework (V1/FM = frontier layer) | Substrate | ○ | **High** |
| 2 | CLR + GULP | James → Alim @settle | ● | ○ | ◐ | No | Engine | ● | Low |
| 3 | LWS | Daniel | ● | ○ | ◐ | No | Engine | ● | Med |
| 4 | Retentive Recs + UEB | Alim | ○ | ◐ | ○ | **Yes** — LLM-pUIC incubation | Bet-heavy | ◐ | High |
| 5 | Reflex | James | ○ | ○ | ◐ | **Yes** — settle review | Accelerator (bet) | ○ | High |
| 6 | RecGPT / GenRet | James → Alim @settle | ○ | ◐ | ○ | **Yes** — time-boxed, sunset criteria | Bet → engine | ○ | Med |
| 7 | Intelligent Boards | Daniel (gated ~60d) | ○ | ◐ | ○ | **Yes** — gains-origin gate | Bet | ● | Med |
| 8 | Recommended Boards | Daniel | ○ | ○ | ○ | No | Ballast | ● | Low |
| 9 | Foundations & Efficiency | James | ◐ | ○ | **●** | No | Engine (cost) | ● | Med |
| 10 | NLFU (cross-org) | James front door | ○ | ● (0.5% NLFU WAU goal) | ○ | — | Funded deliverables | — | High |
| 11 | SM/SL (cross-org) | Daniel (LWS lane) | ◐ | ○ | ○ | — | Closed as design item | — | High |
| 12 | Content Quality (cross-org) | ⟨unknown⟩ | — | — | — | — | — | — | — |
| 13 | Cost investigation | James (for Dylan) | ○ | ○ | **●** | — | Org-internal | — | Med |

**What the matrix shows (portfolio-balance readout):**
- **Daniel:** LWS engine ● + IB bet + RecBoards ballast → **balanced** per the 7/24 gate (every team pairs engine + bet).
- **Alim day 1: no delivering engine.** Both pUIC tracks are bets; his engines (GenRet, CLR) arrive only at settle. Day-1 topline carry = model-pUIC as candidate. This is the design *reason* GenRet graduates in — worth saying out loud in the doc rather than leaving as an inference.
- **James:** UPP substrate ◐ + F&E cost engine ● + Reflex bet → balanced; gains-legibility hinges on UPP launches converting ◐→● (this week's push).
- **The 4.5% SSv2 carry today concentrates in LWS + CLR** (F&E responsiveness supporting); UPP is the swing factor. If Dylan/Jeff probe "where does 4.5% come from," that's the honest decomposition.

---

## 1. UPP — Unified Personalization Platform

**Leg:** Retrieval Foundations (James) · **TL:** Piyush (anchor; Zihao = cross-surface training lead + succession hedge)
**Dimensions:** SSv2 ◐ (P2P candidate strong, no top-line yet) · Cost ○ · 0-to-1: standing framework, V1/FM = frontier layer · Role: **substrate** · Pager: none (surfaces serve) · XFN: **high** (SSJ/Search/Ads politics, CTO attention)

**Doc-ready:** The shared retrieval framework and personalization backbone the organization builds on. UPP owns the cross-surface user-representation and retrieval substrate that CLR and LWS both consume, so the substrate is built once and owned centrally rather than maintained as variants that drift apart. Measured on cross-surface adoption and the engagement gains its models deliver on partner surfaces.

**Current state (internal):** V0 (non-scaled, no FM component) + V1 (with foundation-model component) both feeding at least the P2P baseline. V0 online results strong but no top-line SSv2 yet — P2P keeps raising the baseline. V1 needs more time before going online. HF + Notif progress slow. **James + Piyush aligned: launch push across surfaces starts this week (~7/27).** P2P launch candidate doubles as the exec ads-collaboration proof point (Dylan blessed 7/22). Politics: SSJ "partial-UPP" scheme escalated to Jeff; Kurchi wrestling for ownership; intent-modeling-inside-UPP now CTO-voiced (Madrigal, ELT 7/13) — co-option play live. Search resourcing hesitant.

## 2. CLR + GULP

**Leg:** Retrieval Foundations day 1 → **Anticipation Modeling at settle** · **TL:** Devin (Yichi, Ryan in pod; Kim Toy = potential coverage post-loan)
**Dimensions:** SSv2 ● (production CG stack) · Cost ◐ (GPU serving efficiency) · 0-to-1: no · Role: **engine** · Pager: ● CG serving · XFN: low

**Doc-ready:** Frontier retrieval modeling on the org's main candidate-generation stack, including GPU-served retrieval already in production (the capability Madrigal flagged as "bread and butter for Meta"). GULP rides with CLR. Deliberately excluded from Daniel's day-one load (onboarding digestion); stays with James transitionally and targets Anticipation Modeling at the settle point, where the CLR↔Retentive Recs synergy is strongest.

**Current state (internal):** stable under Devin. Builds on UPP as framework. Settle-gate: both EMs landed. Kim's loan wind-down (Dylan ask #2) affects future coverage.

## 3. LWS — Lightweight Preranking

**Leg:** Retrieval Modeling (Daniel), inherited day 1 · **TL:** Yali (de facto owner; Hedi; Zili on the workstream)
**Dimensions:** SSv2 ● (the reliable gains engine) · Cost ◐ (GPU scale-up) · 0-to-1: no · Role: **engine** · Pager: ● (moves with charter day 1) · XFN: med (SM/SL → Bill Ready visibility)

**Doc-ready:** Lightweight **preranking** modeling (not scoring — corrected descriptor) — the reliable gains engine of the Retrieval Modeling charter. Oncall moves with the charter to Daniel on day one. Near-term LLM seed: LWS distillation. Also the SM/SL strategic home (modeling > heuristics).

**Current state (internal):** SM/SL retrieval side staffed with Yali (+ Raymond Hsu on Lily's side) — announced 7/25, leadership "loved it." GPU scale-up unblocked (see L1/F&E). Zili is on LWS but James retains his PIP — perf case does not move with the charter.

## 4. Retentive Recs (+ Unified Explore Backend)

**Leg:** Anticipation Modeling (Alim) · **TLs:** Chuxi (ramping, runs both pUIC syncs) · Roderick (UEB, currently Daniel's report)
**Dimensions:** SSv2 ○ (launch lull) · WAU/Ret ◐ (pUIC bets aim here) · 0-to-1: **yes** — LLM-pUIC incubation w/ named owner · Role: **bet-heavy** (engine arrives at settle via GenRet/CLR) · Pager: ◐ new pUIC serving surface (ramping) · XFN: high (ATG/UU sync structure, Growth/NLFU)

**Doc-ready:** Retention-optimized recommendations: predict the interests that bring a Pinner back and have the content ready when they arrive. Two predictive-UIC tracks (model-based + LLM-based) plus the feedback loop; UEB consolidates the explore surfaces into the anticipation leg. Both pUIC experiments land within Alim's first month. Measured on retention and fresh-content discovery.

**Current state (internal):** deliberate launch lull — all effort in the two pUIC tracks. Model-based ahead but serving path troubled (legacy of Yuke's TL period); LLM-based not performant right now and slowed further as Chuxi leans into model track. FBL launch landed during OOO (Olafur/Andreanne/Armando); FBL-in-L1/Retrieval in flight. Q3 cadence set: Chuxi runs both pUIC syncs, James backup-only. Staffing: **zero net-new heads** (7/25 decision); Lionel = light RR-serving starter; Zelun Wang (ATG) = leverage candidate via Zhenyu. James's August exit ramp: walking tours w/ Alim+Chuxi weeks 1–2 → ledger + escalations → few hrs/wk by Sept. James's single biggest time-sink since China return.

## 5. Reflex

**Leg:** Retrieval Foundations (James — primary personal time) · **Leads:** Dafang (overall TL) · JJ (Build, ~half) · Tim (PM) · Rui + Dormer committed
**Dimensions:** SSv2 ○ · Cost ◐ (velocity → cost, indirect) · 0-to-1: **yes** — settle-point review · Role: **accelerator** (the org-wide bet) · Pager: none · XFN: high (Andrew's org, Ads funding, cross-org adoption)

**Doc-ready:** The AI-enabled dev-velocity accelerator: productizes AI-leveraged engineering practice (Pinvestigator, Pinkerton) as internal platform that every workstream adopts. Deliberately a small, nimble vTeam. Measured on adoption across workstreams and measurable dev-velocity gains.

**Current state (internal):** Dylan named James/Dafang/Tim the three POCs. Tim 1:1 (7/25): Dafang slower than anticipated; James-role ambiguity → Dylan gets the role-sentence ask. James's named lane = **evals/quality (Detect stage w/ Chao + Gideon)**; contribute into Chao's docs, never parallel versions; 2-session ramp before the Chao working session. Weekly Tim/Dafang/James sync pulled to early Aug. Funding: Dinesh (Ads) funding Reflex; considering UPP funding Q4. Bella Simulate = V0 by mid-Aug (dated deliverable). Inbound interest: "Brian (?)" from Ads (identity soft), Sen's tooling offer.

## 6. RecGPT / Generative Retrieval

**Leg:** Retrieval Foundations (James, incubation) → **graduates to Anticipation Modeling at settle** · **TL:** Bella (Staff) · Hanlin (delivery pair) · Yuke (single stream)
**Dimensions:** SSv2 ○ (pre-gains) · WAU/Ret ◐ (the intended engine-at-graduation) · 0-to-1: **yes** — time-boxed, explicit sunset criteria · Role: **bet → engine** · Pager: none · XFN: med (ATG; shared LLM-serving investment)

**Doc-ready:** Time-boxed incubation of generative retrieval, with explicit graduation/sunset criteria and a settle-point review. Graduates to Anticipation Modeling once incubation criteria are met — the proven-gains engine that balances that team's frontier-heavy portfolio. Shares the consolidated LLM-serving investment with LLM-pUIC and board recs.

**Current state (internal):** QC mechanism installed 7/25 — weekly experiment-ledger template ("model trained" is not a state) + pinned priority list in the Yuke/Bella/James channel. Bella: H1 doc with dated deliverables (Simulate V0 mid-Aug), ER pre-review. Yuke: dated decision rule — end-Sept checkpoint, PIP starts Oct if dated deliverables missed. ATG read (via Tim): RecGPT-as-backbone "more of a P2" — if descoped mid-process, pre-decide Yuke's fallback stream. **Graduation destination note: Bella does not want to move under Alim — resolve at settle.**

## 7. Intelligent Boards

**Leg:** Retrieval Modeling (Daniel) initially — **placement gated (~60d)** · **TL:** Balaji (Staff; placement itself a Dylan decision-ask)
**Dimensions:** SSv2 ○ (~6 mo flat) · WAU/Ret ◐ (notif pairing "wow") · 0-to-1: **yes** — gains-origin gate decides home · Role: **bet** · Pager: ● boards (Daniel) · XFN: med (notifications, Explore)

**Doc-ready:** The frontier 0-to-1 bet of the boards portfolio. Hasn't driven top-line metrics in ~6 months, but the recent notification collaboration produced step-change ("wow") improvements — latent upside unlocked by surface pairings. Settle signal: gains originating in modeling improvements → stays in Retrieval Modeling; gains from surface pairings (notifications, Explore) → moves to Anticipation Modeling at settle.

**Current state (internal):** James publicly folded IB into the anticipation space (7/20, quiet scope claim). Dhruvil told 7/24 the anticipation team "likely" gets it — genuinely open. Dylan shared the notif launch review — James's graded homework: get into the nitty-gritty. Ling straddles RR + IB.

## 8. Recommended Boards

**Leg:** Retrieval Modeling (Daniel) · **TL:** boards TL TBD (fill after first real Daniel conversation)
**Dimensions:** SSv2 ○ · WAU/Ret ○ · 0-to-1: no · Role: **ballast** (live traffic, KTLO + optionality) · Pager: ● boards · XFN: low

**Doc-ready:** Mature live surface — board recommendations serving production traffic on Related Pins and Search, with several small models keeping those alive. The portfolio ballast next to LWS (engine) and IB (bet). Boards modeling and LWS preranking are adjacent disciplines; co-locating them lets techniques and infrastructure transfer directly.

**Current state (internal):** no metric movement ~6 months; keep-the-lights-on plus frontier optionality. Unity Board (backend mirror of Unity HF) essentially finalized per Roderick.

## 9. Foundations & Efficiency (Responsiveness, L1 Utility, Cost)

**Leg:** Retrieval Foundations (James) · **Owners:** JJ (~half his scope) · Rui (L1/Real-Time ops owner)
**Dimensions:** SSv2 ◐ (responsiveness support) · Cost **●** (carries the $2M line) · 0-to-1: no · Role: **engine (cost)** · Pager: ● L1/Real-Time (Rui) · XFN: med (Growth/NLFU, Faisal-GenAI thread)

**Doc-ready:** The efficiency and responsiveness substrate: in-session responsiveness, the L1 Utility platform (mid-funnel utility selection — shopping/freshness/safety knobs, SID + UIC diversity controls, streaming constrained selection), and cost savings. Kept as consolidated scope per Dylan's guidance against divesting small things. L1/Real-Time oncall sits here (Rui) with continuous pager coverage through the transition.

**Current state (internal):** JJ mid-return (back mid-Aug; plate ranking due before return); L1 Utility opportunities: remaining CGs into LWS+L1, GPU LWS scale-up (unblocked), business knobs as first-class controls. Faisal/GenAI thread lands on James's system — engage as L1-platform owner; JJ writes the placement doctrine post-return. Cost: feeds the $2M savings top-line + the cost investigation (below).

## 10. Cross-org: NLFU support (H2)

**Front door:** James (+ Dhruvil) · **Status:** live, Dylan looped James in ~7/24

**Doc-ready:** P13N support for New Low Frequency User growth (Growth-led, Brian Lee carrying; ~0.5% NLFU WAU goal). Our posture: fund via named deliverables on existing engines, never ringfenced bodies (Dylan-aligned). Committed items: NLFU × Responsiveness follow-ups (JJ), RR offsite-signal NLFU experiment iterations, NLFU-targeted RR experiments, LLM-pUIC × PinnerSpark as the sparse-user interest engine.

**Current state (internal):** Monday message posted 7/27 AM — timely, Dylan covering NLFU at her staff. Pocketed: LFU eval suite/debiasing (#4), NLFU Dynamic Triggering (Alok, #6). Sen (§49) = help-first sequence; inventory of existing NLFU-serving work = due item.

## 11. Cross-org: SM/SL

**Status:** staffed + announced 7/25 — **CLOSED as an org-design item.** Yali drives retrieval side alongside Raymond Hsu; LWS lane = strategic home. Jeff priority #1 (Bill Ready focus). Keep as a New Initiatives row, not an open question.

## 12. Cross-org: Content Quality

**Status:** appears in the GDoc Cross Org list — **no repo intel on scope/POC yet.** Capture owner + ask at the first mention in a live channel (likely candidates: ties to safety/quality filtering in L1 Utility's negative-head stack). Flagged so the GDoc row doesn't ship empty by accident.

## 13. Org-internal: Cost / Budget Investigation

**Owner:** James, driving for Dylan (Jeff priority #3) · Core ~$5M/yr over; **>$1.8M under Dylan** — James's own dig. Going well; Monday 7/27 staff update delivered. Next: Dhruvil's person confirmed, prioritized trim list, feed Jeff's EM discussion. Q3 Tier 2 (handled). Feeds the **$2M Cost Savings** top-line metric in the GDoc.
