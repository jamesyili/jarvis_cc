# Team Members & Scope (P13N Retrieval — James's org)

> James's org, whole: the **people** (roster, per-person context, dynamics) and the **scope** (org shape, charters, workstreams, boundaries, canonical outcomes). Renamed from `team_members.md` 2026-08-01, absorbing the team/project/scope content from `organization.md` — that file now covers org structure + teams outside this org and points here.

Last updated: 2026-08-15 (**T2 scenario-boards session (phone)** — four numbered scenario boards built for the trio, §T2 scenario boards below + private artifact; **Nima hired into CLR** (was REQ-1); Bella = **Reflex 1° / RecGPT 2°, stays James-direct in every scenario**; **Rui rides with LWS**; **Esteban → UEB**; IB·LLM-pUIC staffing note (Balaji+Ling carry both, LLM×RecSys fold-back); name trims: "CLR + GULP" → CLR, "UEB & LLM-pUIC" → UEB.) Prior: 2026-08-02 (deep context pass — per-person H1 records folded in from James's own drafts: Yali/Hedi/Yidi/Hanlin enriched from near-empty stubs, Chuxi TL-in-writing, Zihao 7/15 'contested one' marked SUPERSEDED; GenRet = gains engine; IB vs RecBoards split. Prior: 2026-08-01 (rename + org-shape/scope sections built from `reorg_july2026/` full context: org = P13N Retrieval, three teams locked, announcement Wed 8/5. Prior: 2026-07-31 midyear-review sweep — all 13 H1 docs in `downward_reviews/h12026/`; Bella/Yuke/Zili/Alok 7/31 entries below.)

---

## Org shape (July 2026 reorg — announcement Wed 8/5)

> Full design record lives in `reorg_july2026/`: `org_design_proposal_2026-07_v2.md` (system of record) · `org_doc_fill_2026-07-27.md` (GDoc paste content) · `workstream_descriptions_2026-07-27.md` (per-workstream detail + dimensions matrix) · `announcement_week_timeline_2026-08.md` (week-of-8/3 plan + Phase 2 process).

- **Org name: P13N Retrieval** (Dylan re-decided 7/27 — "for now," her hedge against exec-priority churn; Dhruvil's org = **P13N Ranking**). Retires "HF CG." **Anticipation Foundations** remains the cross-org *program* name.
- **Scope sentence (v2):** the pre-ranking funnel end to end, from user signal to what the ranker sees, plus the anticipation modeling built on top of it (Retentive Recs, pUIC, boards/exploration ML). Ranking starts where we end; surfaces belong to P13N-Experiences.
- **Dylan's reorg (announces Wed 8/5):** Daniel Liu (M16) + his 7-person Curation ML team re-parent **laterally** from Yan to James (team intact under Daniel in the interim); Dhruvil gains the blending team (Rahul Goutam + ~5–6). Only Dhruvil + James took headcount this cycle.
- **Transition states (James, 8/1): T1 → T2, no T3.**
  - **T1 — starts the week of 8/3, immediately after the announcement:** **Alok, Chuxi, Lionel, Yidi report to Alim**, whose team is named **"Retrieval Modeling"** (re-decided from the July design's "Anticipation Modeling"). **Everyone else stays reporting to James; Daniel retains his team (Curation ML) intact.** No other changes at T1.
  - **T2 — ~Nov 2026 (moved from ~early Oct, James 8/3 — Yan's freeze-through-Q3 ask + Daniel team-fragility reads):** between T1 and T2, **James + Daniel + Alim figure out the right structure together** — the standing EM staff sync (kickoff ~week of 8/17; process, principles, and settled/open lists in `reorg_july2026/p13n_retrieval_split.md`). Open at T2: **the organizing axis** (`reorg_july2026/p13n_retrieval_split.md` — 3 open charters × 2 teams → 4 viable combinations) · CLR placement · **GenRet landing** (graduation framing retired 8/2; **Bella moves with it**) · IB gains-origin gate (~60d) · UEB consolidation · Balaji · the two open reqs · remaining James-direct lines. **Settled 8/2: James = UPP + Reflex only at T2.**

### The three-team charter design (July target — a T2 input, NOT the T1 state)

> The table below is the 7/24 design proposal, kept as the working charter map feeding the T2 process. **T1 reality differs:** Alim's team carries the name "Retrieval Modeling" (the July table assigned that name to Daniel's leg — superseded); Daniel's team stays **Curation ML** through T1; "Retrieval Foundations" remains design vocabulary, not an announced name. Team names and final ownership settle at T2.

| Team | EM | Mission | Ownership (initial → settle) |
|---|---|---|---|
| **Retrieval Foundations** | **James** | Own the substrate the org builds on: the shared UPP retrieval framework, AI-enabled dev velocity (Reflex), platform efficiency | UPP (Piyush anchor; Zihao cross-surface training + succession hedge) · Reflex (James's primary time; JJ Build ~half, Dafang overall TL, Tim PM) · Foundations & Efficiency (JJ ~half + Rui: responsiveness, L1 Utility, cost — carries the $2M line) · CLR + GULP transitional (Devin; → Alim's team at settle was the July lean; **open at T2**; Ryan + Rui = named SWE support starting H2, likely SGI first) · GenRet (Bella) — **a gains engine to scale, not an incubation (James, 8/2)** — **UPP confirmed James-direct at T2** (8/1 delta) |
| **Curation ML** *(T1 name — **naming saga 8/3:** James gave Daniel the call → Daniel picked "Personalization Product ML" → **Dylan HELD the rename same evening**: "let's hold on… the product ML team name for now. I have other considerations, naming can always be modified later" (Slack 6:50 PM) → Curation ML stands, no team name in the 8/5 email. ⚠️ "Retrieval Modeling" in July docs now means Alim's team; T2 TBD)* | **Daniel Liu** | Frontier ML modeling that drives metric gains across preranking + boards, and publishes (KDD, RecSys) | LWS preranking (inherited day 1, oncall moves with it; Yali de facto TL) = the reliable gains engine · Intelligent Boards (Balaji TL; frontier bet, placement gated on the gains-origin read ~60d) · Recommended Boards (ballast; live traffic on Related Pins/Search) |
| **Retrieval Modeling** *(T1 name per 8/1 delta — was styled "Anticipation Modeling" in July design docs; T2 TBD)* | **Alim Virani** (he/him) | Anticipate what a Pinner wants next: model the interests that bring a Pinner back and have content + serving path ready. Measured on retention + fresh-content discovery | **Day-1 pod = Chuxi / Yidi / Alok / Lionel** (told individually last week of July). Two workstreams (8/1 delta split): **Retentive Recs Retrieval** (Chuxi FT — ramping TL, runs both pUIC syncs as coordination; Yidi FT; Alok primary w/ Reflex secondary; model-pUIC + feedback loop) · **UEB & LLM pUIC** (Roderick FT + Lionel FT — Lionel ramps as Roderick's backend partner in T1; Ling secondary) · July lean was that it gains GenRet + CLR at settle — **both now open at T2, decided on the organizing axis** (`reorg_july2026/p13n_retrieval_split.md`) |

- **Portfolio law (7/24 gate):** every team pairs a reliable gains **engine** with real 0-to-1 **bets** — no all-risk team, no all-harvest team. Alim has no delivering engine day 1 (by design — GenRet/CLR arrive at settle); day-1 topline carry = model-pUIC as candidate.
- **Topline accountability (initial-state allocations, settle review):** SSv2 4.5% → Daniel 2.0 / James 1.5 / Alim 1.0. Cost $2M → James $1.2M / Daniel $0.6M / Alim $0.2M. WAU/retention = Alim's primary carry. ⟨Split is Leo-proposed from portfolio evidence — sanity-check vs. H1 actuals before it reaches Dylan.⟩
- **Oncall (no pager gap):** LWS oncall → Daniel day 1 · boards oncall stays with Daniel · L1/Real-Time → Rui (under F&E) · new pUIC serving surface staffs via deliberate SWE ramp (Lionel). **Zili's perf management stays with James** even as rotations move — no incoming EM inherits an open case.

### Workstreams & leads (current)

| Workstream | Team / front door | Technical lead | Evolution |
|---|---|---|---|
| UPP | James | Piyush | The framework supporting CLR + LWS; the org's unifying retrieval foundation |
| CLR *(8/15: "CLR + GULP" label retired — just CLR)* | James day 1 → Alim at settle *(scenario boards 8/15: → Alim in Sc 1/2/4, → Daniel in Sc 3)* | Devin | Frontier retrieval modeling; deliberately excluded from Daniel's day-one load. **Nima (L15, hired 8/15) lands here on joining** |
| LWS | Daniel | Yali | Lightweight preranking modeling; oncall moves with the charter day one; SM/SL strategic home. **8/15: Rui rides with LWS at T2 wherever it lands (never stays James-direct)** |
| L1 Utility / Real-Time | James | Rui (ops) · JJ | Consolidated within Foundations & Efficiency |
| Retentive Recs + Unified Explore Backend | Alim | Chuxi (ramping) · Roderick (UEB) | Both pUIC experiments land in month one; UEB consolidates into the anticipation leg. **8/15: UEB = Roderick + Lionel + Esteban (Esteban moves with it); the "UEB & LLM-pUIC" pairing retired — LLM-pUIC is carried by the IB crew (Balaji + Ling)** |
| Reflex | James | JJ (Build) · Dafang overall | Small vTeam, James's primary time; the accelerator every leg adopts |
| RecGPT / Generative Retrieval | James | Bella | **Gains engine (James, 8/2)** — the "time-boxed incubation / graduation-or-sunset" framing is RETIRED; the job is to raise its impression share and make it more gains-producing. T2 landing decided on the organizing axis like any other charter (July lean was Alim's team; open). **Watch: early exploration of RecGPT L0+L1 replacing the LWS/L1 model — makes LWS and GenRet a succession pair.** |
| Intelligent Boards | Daniel | Balaji | **Funded under Andrew Yaroshevsky's anticipation vision (James, 8/2) — a strategic bet, NOT boards ballast.** The funnel: **pin-level exploration module = top of funnel** (introduces new concepts) → **IB = mid-funnel** (converts introduction into serious adoption). The two flow into each other but need not be co-located. **Balaji is sprinting the initial IB prototype now.** Placement settles on the gains-origin read (~60 days). **8/3 (Yan 1:1):** the sprint = **10-wk dogfood sprint, ~wk 5** — LLM-based offline IB serving internal dogfood users (Andrew's ask); ~half the engineers across Yan's/Daniel's/Edward's teams; Daniel's folks own FM integration + e2e pipelines. **AMB = IB's previous iteration — never launched last year (the Daniel-team morale scar).** Deliberately conservative start; Q3–Q4 scale small by design *(per Yan, 1:1-only — don't cite onward)*. **8/5 (Yan 1:1):** post-10-wk sprint = **mostly dogfood, not A/B** — LLM serving constraints to solve, long iteration loop. James joining **Tue 30-min IB leads sync** + **weekly 30–45-min Andrew check-in** (Andrew = ultimate TL, hands-on "operation mode"; James asked Yan how to participate without undercutting his leadership) |
| Recommended Boards | Daniel | boards TL TBD | **Deliberately slow-played (James, 8/2): "we don't have to divest it explicitly… essentially starve it of funding, and eventually let's see what product direction takes us. There's very little top-down push."** Live surfaces (Related Pins, Search). ⚠️ Dylan 7/14: hasn't driven metrics in ~6 months, but a **notification collab produced "wow" improvements** and she asked James to get into the nitty-gritty — a graded test. Give her the gains-origin read as the answer |
| Foundations & Efficiency (Responsiveness, Cost) | James (JJ) | JJ · Rui | ~half of JJ's scope; kept per Dylan's guidance against divesting small things |

*8/15 additions to the table above:* RecGPT — **Bella = Reflex primary / RecGPT secondary; her line stays James-direct in every T2 scenario while the GenRet charter moves (→ Alim Sc 1, → Daniel Sc 2–4) — Daniel's Bella-stays carve offer made standing.* IB — **runs as "IB · LLM-pUIC": Balaji + Ling carry both; if the gate misses, the work folds into LLM×RecSys (the bet can't fully die).**

### T2 scenario boards (2026-08-15 — the deck for the trio)

Four member-level boards built 8/15 to float with Alim + Daniel — **numbered Scenario 1–4 by design, no team names (the EMs name their own teams later).** Spread so nothing reads pre-decided: each of GenRet, LWS, IB, and Kim's seat flips sides exactly once across the set — kills the "who gets RecGPT" single-trophy frame. **Interactive artifact (private, phone-friendly): https://claude.ai/code/artifact/4d644302-7e79-41c0-8b85-1a07d50ee37f** (also emailed 8/15). Full rosters + per-board flags: `reorg_july2026/t2_team_setup_scenarios_2026-08-11.md` §Update 8/15.

**Fixed on all four:** James = UPP (Piyush, Zihao) + Reflex/F&E (JJ) + Bella (line stays; charter moves without her) · GenRet charter leaves James · Rui rides with LWS · Chuxi = RR workstream TL · Kim leaves Daniel's line everywhere.

| # | Alim | Daniel | J/A/D | The flip it contributes |
|---|---|---|---|---|
| **Sc 1** *(was "By Stages")* | RR + UEB + CLR + GenRet at graduation | LWS + IB·LLM-pUIC + RB | 4/13/11 | GenRet → Alim |
| **Sc 2** *(was "Barbell")* | RR + UEB + CLR (ballast engine) | LWS + GenRet + IB·LLM-pUIC + RB | 4/11/13 | none — the spine board |
| **Sc 3** *(NEW 8/15 — James's board)* | LWS + RR + UEB | CLR + GenRet + IB·LLM-pUIC + RB | 4/11/13 | LWS ↔ CLR swap |
| **Sc 4** *(was "AnticipationCLR")* | RR + UEB + CLR + IB (Balaji Staff anchor) | LWS + GenRet + RB | 5/12/11 | IB → Alim · Kim stays James |

Kim on the boards: Sc 1–3 = Alim/RR (explorative-pUIC spine; her call — 3-way + Fri 8/21); Sc 4 = James/UPP-focused (⚠ conflicts her 8/11 not-100%-UPP line). Leo flags held privately: **Sc 3 reverses the T1 LWS grant** (Daniel's #1 keep — needs "nothing is decided, including what you already hold" said aloud) **and carries Nima to Daniel with CLR** (breaks the Alim senior-seat design); **Sc 4** has the worst Daniel carve optics (5 lines) + the weakest Kim seat; **Zili: PIP approved 8/15, launching soon** — her line stays James through the case; every board's LWS placement of her is post-resolution only.

Cross-org lanes: **NLFU** (James front door; named deliverables on existing engines) · **SM/SL** (Daniel's LWS lane; Yali + Raymond Hsu — closed as a design item) · **Content Quality** (owner unknown) · **Cost/budget investigation** (James, for Dylan; feeds the $2M line). Front-door routing table: `org_doc_fill_2026-07-27.md` §Proposal→Ownership.

---

## Roster (authoritative — James, 2026-07-15)

> Levels/families/projects confirmed by James. The per-person sections below carry the *narrative* context (perf cases, flight risk, growth); this table is the **source of truth for who exists and at what level.**
>
> **Naming correction (2026-07-15):** the engineer these notes called **"Ray"** is **Rui Wang** — a dictation/preferred-name artifact. One person, not two. Corrected throughout here and in `reorg_july2026/org_design_proposal_2026-07_v2.md`.

### Engineering Managers
| Name | Level (Family) | Role | Notes |
|---|---|---|---|
| **James Li** | **M17** MLE | EM lead for the organization | — |
| **Daniel Liu** | **M16** MLE | (current) EM on Curation ML | Supports 8 ICs (+Esteban, surfaced 8/3) + intern; comes to James via Dylan's reorg. **Naming saga 8/3: Daniel picked "Personalization Product ML" under the call James gave him → Dylan HELD it same evening ("other considerations; naming can always be modified later") → Curation ML stands; James owes Daniel the walk-back before Wed's email** |
| **Alim Virani** (he/him) | **M16** MLE | Retrieval Modeling (T1) | **Started 7/27/2026** — see Tier-1 entry |

### IC level distribution (27 incl. 2 open reqs — Esteban added 8/3)
| Level | Count | People |
|---|---|---|
| **L16** | 3 (11%) | Piyush, Bella, Balaji |
| **L15** | 12 (44%) | JJ, Zihao, Yali, Devin, Hedi, Yuke, Roderick, Yang, Kim, Yongwoo, Ryan, Nima (hired 8/15, starts 9/8) |
| **L14** | 8 (30%) | Chuxi, Ling, Hanlin, Rui, Felix, Alok, Lionel, Zili |
| **L13** | 4 (15%) | Yichi, Yidi, Esteban, Req-2 |

### Full IC roster
| Name | Level | Family | Current main projects | Reports to | Notes |
|---|---|---|---|---|---|
| Piyush Maheshwari | L16 | MLE | UPP · CLR (advisory) · LWS (advisory) | James | SPOF on UPP |
| Bella Huang | L16 | MLE | Reflex (1°) · RecGPT (2°) | James | Staying; top-lab leave-trigger. **8/15: marked Reflex primary / RecGPT secondary; stays James-direct in all four T2 scenario boards (rating-handoff hold; the GenRet charter moves without her — she matrixes in)** |
| Balaji Rengarajan (he/him) | L16 | MLE | Intelligent Boards | Daniel | Daniel 8/3: ~1 yr in, steady ramp; watch via seniority/level lens (top-level IC on his team); his ICs want scope/growth clarity. **Daniel 8/11: very solid backend + good ML expertise, very strong product sense, not that deep in modeling — "might be a good fit for Retentive Recs / pUIC / IB."** IB sprint = 100% his through conclusion. James 8/11: likely stays on Daniel's team → offer him things that travel with that team; Alim asked to chat with him (get-to-know register) |
| Devin Kreuzer | L15 | MLE | CLR · GULP | James | CLR lead |
| Ryan Kam | L15 | SWE | CLR · LWS (dev-velocity focused) | James | Joined ~May 2026 |
| J.J. Hu | L15 | MLE | Responsiveness · L1 · Reflex | James | **IC16 promo APPROVED (James, 8/4)** — effective date TBC; level tables updated when it lands |
| Yali Bian | L15 | MLE | LWS | James | De facto LWS owner. **OOO 8/31–9/18 (surfaced 8/16)** — breaks Daniel's coverage-map LWS-DRI line for 8/31–9/11 (backstop TBD by 8/21; Hedi natural). **8/16: Daniel drives the LWS×UPP onboarding rec (RecGPT path vs. L2) — her written inputs packet due before her OOO (≤8/29); James pre-frames the ByteDance credential early wk of 8/17** |
| Hedi Xia | L15 | MLE | LWS | James | **8/16: Daniel's first LWS contact on return (9/14 — Yali still out to 9/18); natural LWS coverage backstop for the 8/31–9/11 double-dark window; supporting role in the LWS×UPP rec (full lane: `daniel_liu_archive.md` §LWS·UPP)** |
| Yuke Yan | L15 | MLE | Retentive Recs · RecGPT | James | **Will move to RecGPT only**; PIP track |
| Zihao Chen | L15 | MLE | UPP · Content Exploration | James | UPP succession hedge |
| Roderick Gao | L15 | SWE | Unified Explore Backend | Daniel | **8/10 first skip-level (from the 8/7 queue) — strong, no concerns.** Learned of reorg from the email/Yan's message first ("a little bit of a surprise" — comms-sequencing datum, benign; already worked w/ James's team on RR so relaxed about the move). Amazon Ads recsys background, glad to shed ads terminology; happy to be at top-of-funnel. **Keep-doing feedback delivered:** ownership (chases things to the end) + obtaining/communicating clarity across many people = "foundation of a strong tech lead"; landed well, he wants to add product-why depth. **Self-identified leverage:** LRM [or LLM — dictation] online-serving enablement (real experiments, iterate on results, not just offline generation) · managing [prompt/model versions? — garbled] · serving latency. **Year-out ask:** whole-funnel domain expert + strong serving foundation for fast iteration; wants ATG (CG tech) + Ads connections. **Build vs lead: architecture/system altitude** — scale by coordinating (named Ling as platform-build partner), deliberately not owning all implementation. AI-fluent by disposition (uses AI to buy study time, scans what other companies try) — a rule-8 native. **James committed:** Q3 working model unchanged (Yan agreement, restated) · **"your deepest priority will always be UEB"** · support-only posture — "I will only put people in your effort, like Lionel," more on request. **He raised Unity Board ownership** (his side leverages it for UGC Board recs w/ own rec stack; the other team [Ads/ATG? — garbled] may lack the knowledge) → James pointed to **Bella's ownership investigation, promised a proposal "signed off across everyone"**; Roderick volunteered to think it through — **feed him to Bella as a named source.** |
| Yang Liu | L15 | MLE | **Parental leave** | Daniel | **Returning end of Nov 2026, gradual ramp (James, 8/10)** — counted out of H2 2026 planning; nothing lands during Daniel's 8/24–9/11 PTO; skip-level waits for her return |
| Kim Toy | L15 | MLE | UPP foundational (loaned to Dhruvil) · CLR | Daniel | Loan wind-down = Dylan ask. Yan 8/3: solo on UPP, wants her continuing (⚠️ cross-current w/ wind-down). Daniel 8/3: experienced, opinionated on new things; Daniel 8/5: "seems worried." **James 8/5: prior working relationship — she worked search-stage CLR with Devin and the team; no intro framing needed, check-in register is right.** **Dhruvil 8/5 (⚠️ 1:1-only, never cite — her mentor):** didn't like working w/ Yan; curation "too 0 or 1"; EM+PM leads left not-on-great-terms → change fatigue, career-planning anxiety; **preferred work likely NOT the curation stack** → reorg plausibly great for her. Her own preference = the missing input for the allocation call — get it at the skip-level BEFORE settling wind-down mechanics. **Dhruvil promised to release her from the loan if it helps her career (James 8/5)** — wind-down pre-agreed in principle, conditional on her benefit. James on record to Dhruvil: big plans / deep-IC or TL both viable. **8/6 team meeting: asked two good questions live (one on specifics; the other not retained) — James's read: satisfied by his answers.** Skip-level stays her-voice-first. **8/11 (Kim 1:1 #1, via James): does NOT want 100% UPP, does NOT want a 100% modeling job — energized by solving problems for users; full-stack background. ⚠️ Does not like Daniel as manager (James, 8/11) → any placement keeping her on Daniel's line is off the table regardless of work fit; viable homes = a user-facing surface under Alim (IB/UEB-shaped) or a James-direct hybrid (partial-UPP + user-facing), NOT 100% UPP. **8/11 Daniel 1:1:** his candid read — team switches, ML technical depth missing, missing impact; UPP challenges in his framing = infra blocks depth, lacking support/org structure, lacking recognition (LRs, SSv2). Strengths: organize/TL an effort, detail + holistic thinking, sound deliverables over volume; YE2025 Exceeds (rallying), YE2024 and prior Met; Dhruvil very happy with her. ⚠️ **Discrepancy, open question (James's, unresolved):** she tells Daniel she's happy with his support but questioned support in James's 1:1 — James wonders about baseline-emotions vs. audience-calibrated accounts (his word: whether she's working him for more support). Both readings live; the **3-way (James+Daniel+Kim) before both leave same day** is the instrument that collapses it. Placement state: James leaning **Retentive Recs** for her; Daniel's counter — **Balaji might be the better RR/pUIC/IB fit**; Kim's James-direct option still shapeless ("what is there to be done on my team" — open). Alim asked to chat with her (get-to-know register). **8/12 (James, via Daniel): she almost didn't get her LRs — sharpens the recognition thread; James's diagnosis (Leo-confirmed): setup failure, not performance — fragmentation kills her narrative, foundation work is calibration-invisible, no advocate in the room. Designed answer: exploration-surface TL seat under Alim (user-facing, not RR), James as explicit calibration sponsor, honest H2-2027 L16 timeline — full path + 3-way script in `reorg_july2026/t2_team_setup_scenarios_2026-08-11.md` §Kim. Seat is offered as her choice at the 3-way, decision Fri 8/21** **8/13 (1:1 #2): she self-selected into RR proper — loves it, wants it, wants to start; supersedes the UEB-not-RR seat design. Careful not to claim TL (Chuxi-aware, her own instinct); main concern = no very-senior in-space person to learn from (James offered Olafur Gudmundsson, IC17, Dylan-direct). Landing: bulk RR + CLR-relevance help, no UPP bridge mentioned. IC16 narrative synthesized from 4 yrs of reviews (gaps: topline linkage, model-depth, central-domain repeat, assertive visibility, developing owners). Next: James pre-briefs Alim before the Alim↔Kim chat. Full record + verbatim transcript: §Kim Toy — Archive below (merged 8/17; was standalone `kim_toy_archive.md`)** **8/15 (scenario boards): Sc 1–3 seat her Alim/RR (explorative-pUIC spine); Sc 4 = James/UPP-focused (⚠ conflicts her 8/11 not-100%-UPP line — weakest seat, kept for board symmetry). Still her call — 3-way + decision Fri 8/21. **8/15 late: sequence fully on the calendar — Alim pre-briefed (done), Alim↔Kim chat Mon 8/17**** |
| Yongwoo Noh | L15 | MLE | UGC Board Recs (w/ Felix) | Daniel | Filled 8/3 (Yan+Daniel 1:1s); recent UGC BR launch ~+300K WAU per Yan — unverified |
| **Nima** (was REQ-1) | L15 | MLE | CLR (on landing) | James | Granted ~7/11. **8/10: IC15 MLE role closed** — two finalists both won on James's team, James picked one. **8/15 (James): HIRED — Nima, starts Mon 9/8, will work out of CLR.** The "likely Nima seat" from the 8/11 boards confirmed; candidate for Alim's systems/pushback-TL senior seat if CLR lands on his leg at T2 |
| Rui Wang | L14 | SWE | Reflex · L1 | James | **= "Ray"** in prior notes. Joined ~late June 2026. **8/15: at T2 he rides with LWS wherever it lands (Daniel in Sc 1/2/4, Alim in Sc 3) — never stays James-direct** |
| Alok Malik | L14 | MLE | **Retentive Recs (primary)** · Reflex | **Alim (eff. w/o 8/3)** | RR is his own call; needed there as Yuke exits RR. **RESOLVED 7/31: goes to Alim with the announcement**; Reflex work matrixes back to James |
| Zili Li | L14 | MLE | LWS | James | **Pre-PIP: ER engaged 7/22, feedback delivered 7/30, PIP gate ~8/13** (PTO 8/18–9/3 → if fired, opens 9/8); James keeps it. **8/15 (James): PIP going ahead — approved ⟨dictated "DR approved"⟩, launches soon; James considers the outcome path clear. Her line stays James through the case (8/2 rule: no incoming EM inherits an open case) — the scenario boards' LWS placement is post-resolution only** |
| Hanlin Lu | L14 | MLE | RecGPT | James | — |
| Chuxi Wang | L14 | MLE | Retentive Recs | **Alim (T1, wk of 8/3)** | Supported, unannounced TL ramp |
| Lionel Bewa | L14 | SWE | — | **Alim (T1, wk of 8/3)** | **Joined 7/27**; Toronto; Charlie backfill |
| Ling Lan | L14 | MLE | Retentive Recs · Intelligent Boards | Daniel | Chuxi's daily delivery partner. Daniel 8/3: junior-lens worry = whether she keeps working w/ him post-reorg. **Daniel 8/11: "Ling is not really working on IB"** — the 50/50 IB split in his own 1:1-doc sketch overstates it; her load is effectively RR-side |
| Felix Yang | L14 | SWE | UGC Board Recs (w/ Yongwoo) | Daniel | Filled 8/3. Worry = continuity w/ Daniel post-reorg. **SENSITIVE — do not circulate (Daniel 8/3, shared for management support only): job-security anxiety, raised layoffs repeatedly; ex-Meta, green-card/PERM stability was a key reason for joining.** Very motivated; stability matters most |
| Yichi Wang | L13 | MLE | CLR | James | — |
| Yidi Wang | L13 | MLE | Retentive Recs | **Alim (T1, wk of 8/3)** | Carrying most of model-based pUIC |
| Esteban Zavala | L13 | SWE | UEB (w/ Roderick + Lionel) | Daniel | **Joined ~wk of 7/27**; remote — Texas. Surfaced by James 8/3 (not in prior roster). **8/15: assigned to the UEB workstream — moves with UEB to Alim on all four scenario boards (another line leaving Daniel; fold into the "UEB consolidates with its people" framing)** |
| **REQ-2 (open)** | L13 | MLE | — | James | Granted ~7/11; unallocated |

*Not in the 27: Rita Lyu (intern, Daniel's team, ~2 months left). Departed/exiting: Sophia, David, Charlie.*

**Alok — RESOLVED 2026-07-15.** Alok **decided to primarily be on Retentive Recs**, and James wants him there **because Yuke is leaving RR** (Yuke → RecGPT only). This **supersedes** the prior `reorg_july2026/org_design_proposal_2026-07_v2.md` §Calls #3 framing — *"Alok → Reflex 50% + UPP 50%. RR is staffed without him"* — which was wrong on both counts: he's not on UPP, and RR is **not** staffed without him. v2 corrected the same day.
> **Knock-on RESOLVED 2026-07-31 (James):** **Alok → Alim starting announcement week** (RR primary, matrixed into Reflex). Alim's day-1 pod is now Chuxi / Yidi / Alok / Lionel — no unresolved lines.

---

## Tier 1 — Weekly 1:1s

### Alim Virani (M16, ML Engineering Manager II — Retrieval Modeling, T1) — STARTED 7/27/2026

- **Role:** EM for **Retrieval Modeling** (T1 name per the 8/1 Work-Leo delta — supersedes the 7/24 "Anticipation Modeling" lock; T2 name TBD at the ~Nov design point, moved 8/3). Day-1 pod: Chuxi (L14) / Yidi (L13) / Alok (L14, **line CLOSED — under Alim**, 8/1 delta) / Lionel (L14, also started 7/27). No Staff/L15 in pod day-1 (Zihao = UPP full-time, never on RR — corrected 8/02).
- **Onboarding:** welcome sent 7/27; settled until first 1:1 later this week (agenda: `reorg_july2026/alim_1on1_agenda_2026-07-14.md` — core-fixed/edges-open frame). Leader-onboarding design per Q3 plan (weekly three-EM staff, IC-taught deep-dives). Scope held at settle gates: GenRet→Alim at settle; IB gains-origin read (~60d); CLR not promised.
- **2026-07-25/26 — BACKCHANNEL FLAG (SENSITIVE — uncorroborated; do-not-propagate discipline):** Chuxi, checking new folks' LinkedIn, found her **former Google manager is a 1st-degree connection to Alim** and asked him for a read. His reply (WeChat screenshots with James): "one of the worst people I've worked with" → escalated to "in a holistic view, he is actually the worst person I have worked with"; "so dumb, arrogant, and sleazy"; **"sexually harassed some of my former coworkers"**; **"he actually got on a PIP at the time at Google."** Source self-caveated: "he could have improved or fixed himself over the years, but you asked for my prior on him." **Provenance:** character + PIP claims = secondhand, one ex-colleague, years-dated; the **harassment claim is at least third-hand** (ex-manager relaying what former coworkers told him) — no names, no incident specifics, no Pinterest nexus. Note: the source knows Alim now manages Chuxi ("Chuxi is in trouble…") — this rumor lives in ex-Google networks **outside James's control** and could reach Pinterest by other routes.
- **James's handling (Sat 7/25 call + Mon 7/27 1:1, both w/ Chuxi):** calmed her — prior-workplace claims can be misleading/damaging; observe + monitor over time, corroborate from multiple sources, don't jump to conclusions; framed as a judgment-building rep for her. Monday: reaffirmed skip-level sponsorship, staying very close, will keep an eye on Alim through ramp. Chuxi "seems fine at this point."
- **Leo read (7/27, unratified):** unbundle the claims — character/competence = normal observe-and-monitor via existing ramp structures (RR walking tours w/ Alim+Chuxi wks 1–2 of Aug, weekly three-EM staff, skip check-ins); the **harassment claim is a different class** — observe-and-monitor is not a mitigation strategy for it, and the knowledge-holder is in his pod. Rec: **quiet ER confidential consult** ("received secondhand, no Pinterest concern, want guidance on my obligations" — a consult, not a report against Alim) → dated record + professional guidance + resolves whether/how to loop Dylan. Don't unwind or pre-judge the hire (`peer-flags-are-not-vetoes`); don't backchannel further (each hop propagates); **don't accelerate settle-gate scope transfers ahead of the ~60-day read** — the phased design is now also the hedge.
- **2026-07-28 — Roberto Konow positive reference (counter-evidence to the backchannel):** replying ~2 months late to James's 5/18 anonymous-reference ask, Roberto — Alim's direct former manager ("the very first EM I managed, when I was a Manager II") — wrote "I heard and see that Alim is now with us 🙂 I am really happy!" Unsolicited warmth from a direct former manager; thin on specifics, but directionally opposite the ex-Google-manager read. Hold both alongside each other; keep the observe-and-monitor posture unchanged.
- **2026-07-27 PM — Dylan looped (CONFIRMED; 1:1 agenda item "How to deal with Rumours"):** James raised the Alim backchannel with Dylan same-day. Her guidance (James: "good feedback"): **"Whether or not this is true is irrelevant. Move forward and give everyone a fair chance. Keep our head on about what is true and what is not."** Posture = fair-chance integration + epistemic discipline, no investigation appetite. The single-point-of-knowledge exposure is now shared upward the day it arrived. ⟨Scope of detail shared (harassment claim specifically vs. "rumors" generally) not specified — the ER-consult question technically remains James's open call for that claim-class, but urgency is much lower with Dylan on record.⟩

### Piyush Maheshwari (TL, UPP Retrieval)
- **Role:** Technical anchor for retrieval architecture. Primary IC on UPP.
- **Workstream:** UPP (top priority)
- **1:1:** Tue 3:00pm
- **Context:** Just came back from OOO. Already engaging on UPP. First 1:1 with James is Monday. Holds full retrieval architecture context post-Bowen.
- **Growth:** Building toward senior TL scope. UPP cross-surface expansion is his proving ground.

### Bella Huang (TL, RecGPT)
- **Role:** Tech lead for RecGPT / generative retrieval with ATG
- **Workstream:** RecGPT
- **1:1:** Mon 10:30am
- **Context:** OOO 3 weeks starting April 6. Flight risk — told James directly she's thinking about leaving this year (7 years at Pinterest). Thinks Meta/Coupang interviews easy to get. Would like pay bump. Will give 3 months notice.
- **James's honest assessment:** Never really connected. Doesn't create ideas — needs James to architect, then resists. Lacks decisiveness, conviction, communication skills. Dylan has lost trust over Group MP situation.
- **Position:** Not retaining, not managing out. Extract value while here. Don't invest retention capital. Build direct YiPing working relationship that doesn't depend on Bella.
- **2026-06-06 update (source-protected — keep between Leo + James):** Heard via a Meta-friend backchannel that Bella has a **Meta IC6 offer and is at team-matching** (late stage). Secondhand, pre-disclosure — Bella has *not* told James about the offer, doesn't know he knows. Advances the already-documented flight risk (she'd named Meta + 3-month-notice intent back in April). James's call: **not fighting for her** (consistent with standing position) — the goal is the **headcount/req**, which is live because of freeze risk + **1 head already lost to attrition (Sophia)** — that precedent is exactly why Bella's backfill can't be allowed to slip.
  - **Plan of record:** (1) Do NOT flag Dylan pre-resignation — no decision is attached yet, so it's only anxiety transfer into her OOO; discovery risk of waiting ≈ 0. (2) Quietly pre-stage the backfill now (where the req goes, RecGPT reshuffle, Reflex Simulate coverage). (3) The trigger is her **resignation** — then flag Dylan *and* claim the req in one move (confirmed + her disclosure + real decision = clean). (4) Offboard graciously regardless (protects the "good to work for" rep). RecGPT continuity partly hedged via the YiPing pairing.
- **2026-06-14 update — offer in hand + ER ticket filed.** Bella's external offer is now **confirmed/in hand** (past team-matching). James filed an **ER (Employee Relations) ticket** documenting the performance decline (email cites "noticeable decline over the past two months vs. her level — IC16 MLE — feedback given, no improvement"). **ER-ticket tactic — NOT Dylan-directed for Bella (corrected 2026-06-30):** the notion that an ER ticket makes an exit count as **managing out a low performer** (vs. regretted attrition), protecting the backfill req, was a **general tactic Dylan mentioned to James previously** — Dylan does **not** know about Bella's specific situation and did not direct this. (Earlier notes miscoded this as Dylan-directed for Bella; she has no knowledge of the case.) **Integrity check (James's honest read):** "a mix of the two" — there's a genuine headcount motive AND she **hasn't really performed well even from the beginning**, so the low-performer characterization has a real basis. Clean enough *because the substance is true*. Open: confirm with HR that the documentation actually secures the req (the perf-track and backfill-track are different mechanics).
  - **2026-06-30 update — Bella is STAYING (major reversal).** Bella told James directly she is **not leaving**, despite recsys offers in hand (incl. Meta). Reasoning: the offers are all lateral recsys with ~2x hours; Pinterest is the better *holding pattern* — a lower-workload job that leaves her 20–30% time to reskill into AI (taking Stanford CS337). **Named leave-trigger: an interview/offer from a top-tier AI lab (OpenAI/Anthropic specifically)** — committed to telling James if it comes. Explicitly said the current stack "cannot satisfy what I'm seeking." Her asks for staying: **promotion** + freedom to work on **agentic systems + generative retrieval**. **James's stance (unchanged):** not ready for promo, but she's doing good work / still valuable / directs + executes when asked → **keep her, don't manage out, don't promote near-term.** She **declined to TL Retentive Recs** when asked directly (confirms Chuxi as Retentive Recs TL; confirms Bella as capped *directed contributor*, not independent leader). ER thread should close as resolved/retaining. Backfill req predicated on her exit is moot. Full team-split roster reconciliation still pending (she was rostered DEPARTING on Alim's Track A).
  - **2026-07-25 update — ER case closing/paused; stance shifting back toward managing out (DECISION OPEN).** (1) **ER case on Bella is being closed — or at least paused** — James's call: "trending in the right direction," not the right time to PIP. ER pushed back gently ("are you sure about closing?"); after the conversation James is having **second thoughts**. (2) **Written feedback is now on record:** James sent Bella a **Slack message stating her RecGPT impact is not meeting expectations** — she isn't personally moving the needle on modeling scope; not enough metric improvement. (3) **ER's guidance:** make it formal in the **H2 performance conversation** — exactly where she's not meeting expectations, exactly what she must deliver. The **midyear review doc will be shared with both ER and Bella; ER wants to pre-review the draft.** James plans to hammer the lack-of-impact points + make IC16-TL expectations crystal clear (she can't skip effective tech-leading; communication skills underdeveloped with no improvement over years; the bar rises further for her IC17 aspiration). (4) **David (coach) convo:** David cut through with one question — "do you want her on the team?" James answered **immediately: no.** Two years, no leverage found; he thinks she knows it. David: there's a **kindness in being direct with her**; James agrees — wants to be clear. (5) **Current behavior read (James, 7/25):** not engaged in team activities, stopped contributing, delivers only when pushed / job-on-the-line, **actively interviewing or prepping for OpenAI/Anthropic** (her named leave-trigger targets). James: "I'm tired of doing that for both her and Yuke" — and it's not the example he wants leads setting for the new org (Alim/Daniel watching). (6) **Net: the 6/30 "keep her" stance is no longer live.** Open decision (this session's analysis queue): reopen/keep ER active vs. close + formalize via H2 doc; what "managing out vs. holding the bar" looks like given she may self-select out to a top lab. (7) **Confirmed reconciliation of the two reads (James, 7/25):** both true at different bars — she complies when pushed (registered as "improvement" against the June ER-case low) but ownership/discretionary effort/impact fail the IC16-TL bar; "trending in the right direction" was graded on a curve. James: technically OK today, grappling with the longer-term implications of letting that equilibrium remain. (8) **Third-party corroboration — Tim (Reflex PM), 1:1 notes 7/25:** Bella's Simulate work "**so far is not concrete enough**"; agreed timeline = **V0 with something to show by mid-August**; a presentation meeting (requested by Andrew, sharing Chi's simulation work) is on the calendar. Independent non-James datapoint for the H2 impact case — and a dated deliverable ER can anchor to. (9) **Dylan's posture (per James, 7/25): "keep an eye out and keep watching — no formal PIP."** Any formal PIP on Bella requires **explicit Dylan sign-off** James doesn't currently have. (10) **Leo rec (7/25, unratified): no formal PIP — run the rating-and-doc path.** H1 feedback doc (ER pre-reviewed) with plain impact/TL-bar language + dated deliverables (Simulate V0 mid-Aug; RecGPT metric goal TBD) + promo-ambiguity killed; year-end lands where the evidence lands (James's frame: "Meets Most" tier); PIP stays pre-armed with defined triggers (missed dated deliverables + stays + example-setting damage), taken to Dylan for sign-off only if triggers fire in Q4. Rationale: Dylan's posture makes PIP a fight she's advised against; Bella has a real exit vector (top-lab prep) so the bar + her optionality resolve it; and James already has Zili on a live PIP + Yuke pending — a third simultaneous formal process is heavy ER load and bad org signal right as Alim/Daniel land. Draft doc: `work/people/bella_huang_h1_2026_review_draft.md`.
  - **2026-07-27 1:1 (debriefed 7/30) — the H2 expectations conversation DELIVERED.** ~60 min (scheduled 30), heated at times, ended amicable. She arrived with a giant in-flight-experiments list — she'd felt the probing coming (named James's third-degree questioning in an ATG RecGPT sync as an earlier instance). (1) **James delivered verbally:** H1 impact below par for IC16 — too few launches / too little realized RecGPT impact; CG-impressions expansion moved only after his push; forward plan unclear. Behavioral: GPU-allocation handling = critique-only ("this doesn't work," what she won't take on) with no constructive team-level alternative → named as core IC16 expectation. This is the ER-advised formal H2 conversation, done, pre-announcement. (2) **Her feedback to James:** "too insecure about RecGPT" — his probing style scares team members. James accepted + operationalized (pre-labeling intent; she confirmed that helps). **Leo read:** accept the datapoint (tone/probing — Jiajing calibration check planned), not the causal frame — it converts "your impact is below bar" into mutual growth areas, and "James is insecure about RecGPT" may circulate as a narrative among the team/ATG partners. (3) **Draft H2 criteria co-written in the shared doc ("(TBD) Rough"):** RecGPT+Unimpressed+Teacher Distillation **+0.4% SSv2** (her hedge — "0→1, huge uncertainty" — recorded inline next to the number); Content Exploration initial launch + enablement (Content Success/P2P/Search); Reflex 0→1 + **user-bot-simulation pintool demo mid-Aug** (doc shareout before; integrate Chi's pintool work, migrate to Reflex repo later — matches Tim's V0 checkpoint); Team Leadership (proactive alignment-driving, capacity-audit-type contributions); Communication (proactive written coordination; her line: "RecGPT needs more management bandwidth"). **Support asks:** agent access (Teletraan/Unity teams), expectation checks w/ Dafang + Mehdi Ben Ayed, concrete leadership definition (**"prefer oncall" — Leo flag: that grades the IC16 leadership bar down to logistics; James's answer should be a real alignment-driving item, not oncall**), James involvement on sizer changes. Support items are future defense exhibits — close fast + date-stamp each. (4) **Leo blind-spot read (7/30, accepted by James):** the below-bar message existed only verbally — the shared doc is forward-looking, hedged, and *leads with* "Feedback for James" → the written H1 review is now more load-bearing, not less. Fix: paste a "Feedback for Bella (delivered)" section into the shared doc **with a Slack heads-up, not silently** (paste-ready text delivered in-session 7/30). (5) **Timeline locked 7/30:** this week = paste section + H1 edit pass → **ER pre-review by ~8/1** + kick off support asks (date-stamped); announcement week (8/3) = light touch, but calendar the shareout+demo as named dates, deliver the leadership definition, Jiajing calibration chat; **week of 8/10 = deliver H1 written review EARLY WEEK, BEFORE the Simulate demo** (review is about H1; demo is H2 evidence — sequence prevents renegotiation), demo mid-week, then ratify H2 doc with owner/metric/date on every line (SSv2 uncertainty as risk-management language, not co-equal caveat); Sept = 30-day check + running support log; PIP only if the pre-armed triggers fire, via Dylan sign-off.
  - **2026-07-31 — written H1 review FINAL + posture read + org decision.** (1) **James wrote the final H1 review** → `downward_reviews/h12026/bella_h1_2026_feedback_final.md` (pre-ER fix list in its header: Jaewon spelling, oncall-goal collision with Yuke's doc, grammar, promo-paragraph in-doc-vs-verbal). Case record + full H2 strategy → `downward_reviews/h12026/bella_huang_h1_2026_review_draft.md` Appendices A–B (strip-before-ER). (2) **Leo posture read (no objection): record-aware / defensively fortified, NOT adversarial** — she's contesting the outcome, not James; tripwires that flip the read: Jiajing confirms the "insecure" narrative circulating / she contests the pasted section or written review / support-ask weaponization / documentation-collection signals. Two-register posture: warm in person, armored+fast on paper; retaliation-optics counter = ER-advised provenance predates her 7/27 feedback. (3) **Org decision (James): she stays on RecGPT + Content Exploration and moves WITH the RecGPT unit at graduation** to its eventual new manager; hold at handoff = James delivers the 2026 rating, new manager starts 2027 goals. GenRet graduation stays criteria-gated (her H2 deliverables ≈ the graduation evidence → lands ~post-rating).

### Devin (TL, CLR)
- **Role:** CLR model expert, UPP backbone
- **Workstream:** CLR
- **1:1:** Tue 3:30pm
- **Context:** Sole deep CLR model expert currently. Ryan (April) provides coverage. Asked for strong collaborators. Watch for flight risk in 2-3 week gap before Ryan arrives.
- **Growth:** Leadership visibility. Q2 goal: Devin's leadership is visible in CLR improvements.

### JJ (TL, Real-Time + Pinvestigator)
- **Role:** Real-Time systems + L1 Utility (absorbing from David in April) + Pinvestigator collaboration
- **Workstream:** Real-Time, L1 Utility, Pinvestigator
- **1:1:** Tue 4:00pm
- **OUTCOME: PROMOTED to IC16** ✅ (James, confirmed on file 8/13 — he'd reported it earlier and it hadn't been filed; decision timing not recorded). The Kurchi-sniping/flight-risk thread is closed.
- **Context:** IC16 promo package **SUBMITTED in Workday 2026-07-10** — James's final edit preserved verbatim in `self/writing_style/example_promo_package.md` (Workday Q1/Q2/Q3). Q3 = decision ownership + communication to land decisions (per James: on Pinvestigator "I was making a lot of decisions for him"). Final version is quote-carried: full written assessments from Dafang, Nilesh Gohel, Olafur Gudmundsson, Vikram Deshpande woven in; ISR vision provenance corrected to Infra/PJ leads (JJ connected vision → practical application). Residual: ML Symposium year 2025 (Dafang quote) vs 2026 (James prose). Q1 = foundations/efficiency + AI tooling/ML-adjacent systems ("straddles ML systems and models"); Q2 = L1 Utility+efficiency / In-Session Responsiveness (PSv2 nod) / Pinvestigator+Reflex+mentorship; Q3 = tactical→strategic, strategic brevity. The old "ML depth gap" concern is answered in-package by reframing his depth as ML systems + agentic tooling. Open confirms before submit: savings total ($1.67M vs $1.8M), ML Symposium year (2025 vs 2026), Q1 ~10-engineer span, Heath/Olafur last names.
- **Cross-org buy-in intel (2026-07-09):** Content Success is investing in L1 Utility shopping controls — Heath (Senior EM) strong buy-in, Olafur (IC17 Senior Staff) can corroborate the story; the engineer driving the shopping control experiment is from Content Success. Leo rec: Olafur belongs on JJ's assessor list.
- **Risk:** ~~If promo doesn't land + Bowen departure + AI market = potent combination for JJ to look. Have contingency conversation ready.~~ **RESOLVED 8/4: IC16 promo officially approved** (effective date TBC). The retention scenario this guarded against didn't materialize; H1 feedback draft v2 (8/4) frames the promotion as the floor of the new bar.
- **Single point of failure:** Essentially solo on Real-Time. No coverage if he left.

### Yuke (TL → IC transition in progress)
- **Role:** Tech lead for Retentive Recs / p(UIC) — **TL role ending; stepping to IC**
- **Workstream:** Retentive Recs
- **1:1:** Thu 2:00pm
- **Context:** Flight risk. Been asking interview questions about market pay. Unhappy about promo deferral. Short tenure history.
- **Retention anchor:** EB1 green card sponsorship — James handling. Green card dependency means no abrupt departure.
- **Promo timeline:** Moot — stepping to IC.
- **Dynamic:** Doesn't get along with Devin. See Chuxi-Devin-Yuke dynamics in goals.md.
- **2026-06-14 update — OOO performance signal (decision-relevant for the TL call).** During James's OOO: **progress is slow, no proactive updates, and he's absent from the syncs** (not showing in meeting notes). Reinforces the already-documented flight risk (market-pay interview questions, promo-deferral unhappiness). James considered filing an ER ticket (worried he's interviewing) and **held off** — it's a yellow flag not a verdict (two weeks, read off meeting notes), no feedback has been given yet, and a flight-risk-driven ER record is improper/pretextual. **This is direct evidence for the goals.md "grow into the TL role, or reposition" call.** Investigate properly on return *before* concluding: did Yuke know he owned this / was expected to drive updates, or did ownership default to ambiguity when James left? Is he partly OOO himself? Did the sync structure change? Could be a character signal; could be a delegation gap that's partly James's. Hold loosely until back and clear-headed.
- **2026-06-23 update — delivery facts vs. fear-narrative (separated deliberately).** **Facts:** two workstreams Yuke owns as TL are stalled — (1) ME GPU serving still not delivered *even with Hanlin's help*, (2) model-based pUIC online serving not delivered, "setback after setback" despite TL role + two engineers. He is not training models that James can see, and isn't going deep on serving either. James is now weighing **replacing him on the critical workstream** (acknowledged as a likely push-out if he isn't already on the way out). **Fear-narrative (James's words, flagged as story not fact):** "certain he's interviewing for staff-level elsewhere and can't find it / or has found one and is waiting until I'm back to tell me." This is the engine writing — no evidence cited. **Corroborating context:** Yuke's Monday-off fever is real and part of a **team-wide sickness wave** (6/22–6/23: Zili off, JJ off, Hanlin OOO Wed 6/24, Yali off-but-on-call) — so the absence reads less like coasting than the heat first claimed. Carry the delivery question (real, cold, James's to own) into the return; leave the interviewing story parked until there's actual evidence.
- **2026-06-24 update — interviewing confirmed; TL transition initiated.** James had a direct conversation. **Key facts:** (1) Yuke confirmed he is actively interviewing. Reasons: doesn't believe in Pinterest long-term (Snap-repeat fear), wants backup plans, green card stability — NOT about James or the team. Also: devaluing traditional Staff ladder given industry trend of senior people leaving high titles for Anthropic/OpenAI technical staff roles. (2) Work accounting: ME GPU rollout — he's on Unity side, Hanlin on model deployment, claims progress. Model-based pUIC — deliberately deprioritized because not career-relevant; mostly unblocking Yidi and answering questions. LLM-based pUIC — reviewing Chuxi's code, working with her. (3) James delivered IC15 feedback directly: not making Staff, not doing IC15 job — below standard since roughly February. Yuke accepted with no pushback. (4) James gave two options: stay as TL of Retentive Recs, or step down to IC. Yuke committed to bringing his own proposal to **Monday 6/29 1:1**. (5) Yuke's constraint: doesn't want PIP threat; green card dependency keeps him from abrupt departure. **James's read:** Yuke is almost certainly choosing IC — he's already been behaving like one. Monday is the formalization.
- **2026-06-29 1:1 outcome (Yuke).** Yuke now **openly admits he's looking around** (hasn't found anything yet) and says he's **no longer sure he wants a lead role or the year-end promo.** James's read: clear — he's stepping off the ladder into a holding pattern. **Coaching landed:** after James's "okay to look, not okay to underperform while looking," Yuke has **stepped up — more proactive and visible, driving changes forward.** Two next-step options aligned: **Option A** — deep IC modeling work in one or two of **UPP / pUIC / Reflex**; **Option B** — continue as **TL of Retentive Recs.** **Design tension (Leo flag):** Option B collides with (a) the Chuxi-TL succession (Chuxi steps up *only if* Yuke steps down) and (b) the split (Retentive Recs is Alim's Track A; Yuke was to stay on James's Track B — can't TL a Track-A workstream from Track B). **Bella↔Yuke parallel:** both now in holding-pattern/looking mode; Bella (who talks with Yuke) thinks Yuke should try for promo while still here — a 2-person senior cluster to watch for contagion.
- **2026-07-06 DECISION — PIP track locked; A/B superseded.** James's read hardened: post-coaching "step up" is surface-level — Yuke is coasting at IC15, maximizing interview-prep time, and using the TL/coordinator label to pass the pod's work (largely Chuxi's) off as his own. Decision made — **when, not if, on the PIP.** The 6/29 A/B framing is dead: deep-IC modeling work is rejected as a landing spot on its own because it's an equally good hiding place ("trained a model" with no shippable deliverable). Locked plan: (1) **TL title stripped** — delivered as the already-aligned IC transition, kept clean of any PIP language, framed as role change under the reorg; (2) **Yuke stays under James, NOT Alim** — don't hand a brand-new EM a live perf case; James has the history and the process leverage; acknowledged cost: the perf-management burden stays on James; (3) **ER/HRBP confidential consult FIRST, before any formal word** — interviewing + ER-savvy + green-card-entangled is the exact pretextual-challenge profile; (4) **H1 below-expectations rating is the PIP on-ramp** (documented since Feb); (5) **formal PIP clock starts early August**, spaced from the TL strip and reorg announcement so each action stands alone (role change ≠ rating ≠ PIP — no reorg-retaliation reading); (6) **green card = time, not leverage**: EB1 recently filed; its value is that Yuke can't bolt, so the process can run clean and fully documented on James's clock. In conversation, use it only to *reassure* ("sponsorship continues") so fear doesn't crowd out the expectations message — never link GC to performance (coercion narrative + ER landmine). Expectations conversation = named, dated, measurable deliverables with quality bars; the PIP is what removes the hiding places.
- **2026-07-07 update — landing spot set (RecGPT), Dylan endorsed, Chuxi looped.** (1) **Dylan endorsed the TL→IC move** in the 7/7 re-entry 1:1; thanked James for transparency ("exactly the type of transparency she's looking for"); her follow-up question: **who TLs the space?** — James owes her a proposal. (2) **Landing spot: RecGPT/Generative Retrieval as IC — ONE workstream, not two.** James's call: an interviewing, distracted IC15 gets a single stream = single accountability, easier tracking, single TL. Yuke **asked for this space himself** — he owns wanting it, which strengthens the expectations conversation ("you asked for this; here's what delivering here looks like"). (3) **Bella aligned to keep an eye on his work** (also feeds her resource ask). Boundaries: Bella = technical TL-of-record ONLY — never part of the perf process, never PIP-aware; all deliverable definitions/tracking/documentation come from James (ER requirement anyway). Frame Yuke-capacity to Bella as *provisional*, not committed headcount. **Contagion watch:** Bella+Yuke are the documented 2-person looking cluster, now daily collaborators — when the process turns formal, the Bella-visible version must be indistinguishable from a normal role transition. (4) **OPEN — reporting line:** RecGPT is Track-A/Alim space. Leo rec: Yuke reports to James through the PIP window ("I'm holding the perf management so Alim can ramp"), transfers only after resolution. Not yet confirmed by James. (5) **Chuxi told transparently** (7/7); transition co-designed with her: Yuke out of pUIC → RecGPT IC; Chuxi leans into both pUIC tracks.
- **2026-07-22 update — full cut from Retentive Recs, co-decided with Chuxi (now TL).** With Chuxi ramping well as TL, she is **uncovering more issues that fell to the wayside during Yuke's earlier distraction** — corroborating the neglect from her vantage, not just James's. New concern named plainly: Yuke is **so good at managing up that James can't tell whether he's actually producing work.** So James + Chuxi **jointly decided to move Yuke fully off the Retentive Recs project so he can't hide behind it** (the pod's collective progress was the cover). Reinforces the single-stream RecGPT isolation logic (7/07 #2) with a second owner (Chuxi) now behind it, and adds fresh documented evidence for the PIP on-ramp.
- **2026-07-25 update — ER consult happened; David's "two months" frame; placement second thoughts (DECISION OPEN).** (1) **Dynamic (last ~2 weeks): heated, hot-cold.** James cordial + respecting Yuke's personal wishes, but it grates where work leverage is needed. Read: **doesn't care about the work, but is professional — does things when asked** (same compliance-without-ownership shape as Bella). (2) **Job-search read: failing.** Yuke can't find a desirable job; green card keeps him stuck; now trying to minimally meet expectations and not ruffle feathers. James: "he has overplayed his card." (3) **New incident — model-based pUIC:** another issue surfaced that Yuke **should have caught as TL** — legacy of the not-caring period. James gave heavy direct feedback (did not do a good job leading/ramping the space ⟨confirm which⟩); the space is super behind / very delayed. (4) **ER's two asks:** (a) make the **year-end/H2 feedback unambiguously "not doing well"** — tricky case because **Yuke got an Exceeds rating at end of 2025**, so an immediately-following low-performance claim is hard to prove; hence **ER wants validation via ad-hoc peer feedback**, not just James-vs-Yuke; (b) **keep clear documentation** — tricky precisely because Yuke does everything asked and is very responsive; documenting non-performance against a compliant subject is the hard part. James: "I really hate doing this — it brings me no joy." (5) **David (coach):** proposed a clear boundary conversation — "I'll give you two months, but after that I need to move on" — kindness with boundaries; this cannot go on forever. (6) **Placement second thoughts (OPEN):** RecGPT now = Bella + Yuke (+ Hanlin), i.e., the documented 2-person disengaged cluster co-located on one workstream. James wondering if he should instead park Yuke where he can crank out models (UPP-side ⟨confirm⟩) — but he **already committed the RecGPT placement in front of ATG**. Queued for this session's analysis. (7) **PIP timing = OPEN DECISION (7/25):** James going back and forth on whether to start the formal PIP (the 7/06 plan said clock starts early August). **ER has given clear instructions sufficient to start the process whenever James decides** — the blocker is James's decision, not process readiness. Queued for this session's analysis alongside placement. Reporting-line (James vs Alim) still unconfirmed. (8) **Leo rec (7/25, unratified) — dated decision rule instead of open-ended back-and-forth:** deliver a midyear expectations doc NOW (dated RecGPT deliverables + explicit consequence sentence, ER-reviewed); collect ER's ad-hoc peer validation during Aug–Sept (Chuxi/Yidi/Hanlin + ATG partner; Bella's input only as routine technical-TL observation, never PIP-framed); let the Aug 5 reorg announcement pass so actions stand alone; **end-of-September checkpoint = David's two-month boundary — deliverables met → he earns the seat; missed → formal PIP starts October** with a case immune to the Exceeds-2025 objection. Placement: **stays RecGPT** (ATG commitment, single-stream accountability he asked for, keeps the problem out of launch-critical UPP; "crank out models" = the exact hiding place the 7/06 plan rejected). Reporting: **stays James** through resolution. Watch-for: Tim's ATG notes rank RecGPT-as-backbone "more of a P2" — if RecGPT gets descoped mid-process, pre-decide the fallback stream rather than improvising mid-PIP.
- **2026-07-27 1:1 — first open fight-back; documentation clocked; visa holding-pattern self-declared.** James delivered the direct retrospective: Yuke **did not do a good job as TL on Retentive Recs**. **Yuke visibly fought back** — first open contest of the performance narrative (vs. the no-pushback 6/24 acceptance). Confirms ER's 7/25 warning that the "unambiguously not doing well" case will be contested → **the Aug–Sept ad-hoc peer validation is now load-bearing, not optional.** His three messages: (1) **"worried you are collecting documentation against me"** — he has clocked the process (ER-savvy profile per 7/06 plan). Posture: never deny; frame written expectations as clarity that protects both sides; **notify ER of this comment** — they'll want it on record and will coach the response. (Exact in-room wording not reconstructable per James — posture applies going forward.) (2) **Wants to do well in RecGPT, trying his best** — compliance-without-ownership shape, consistent. (3) **Unprompted: needs to finalize visa issues with Pinterest before "career next steps" — meanwhile wants to do a good job as IC.** = self-declared holding pattern until GC clears; independently confirms the 7/25 "job search failing, GC keeps him stuck" read and **validates the dated-decision rule** — he says he's staying and offering good-IC work, so convert the offer into commitment against the dated RecGPT deliverables. **Landmine unchanged (7/06): never link visa ↔ performance in either direction; sponsorship-continues reassurance only; no process-timing promises tied to visa resolution.**
- **2026-07-28 update — self-review captured; work-side gap facts locked; H1 doc now carries letter + Workday manager answers + context appendix.** Yuke's Workday self-review transcribed into the doc's appendix (claims: TL-drove-the-workstream, ME GPU rollout listed as an accomplishment, communication-framed learnings, H2 goals re-broadening into pUIC + whole HF stack). **James locked the work-side facts (7/28): one launch in all of H1 = frontier sampling**; both pUIC tracks missed H1 milestones; **model-pUIC ≥2 months behind via 3 separate design/leadership issues** — (a) serving track without the right user-sequence signal, untested (~1 mo delay); (b) modeling delegated to Zelun Wang (ATG) with little visibility, design discussion deferred to June → revealed only a subset of expected interactions in use; (c) embedding predictions unvetted (~1 wk) = **the July-surfaced issue** (found through the transition); **ME GPU passed launch review in 2025, slipped several months, unflagged until James's February ping** (likely the [February date] anchor — ⟨confirm earliest⟩); **very little own contribution** vs. Chuxi/Yidi/Zelun/Ling (names stay appendix/ER-side; letter unnamed). Workday Q1/Q2/Q3 manager blocks drafted — Q2 corrects his communication-only diagnosis (ownership of outcomes); Q3 supersedes his scope re-broadening (RecGPT single-stream only). Remaining before ER pre-review: artifact links, Feb-earliest confirm, RecGPT deliverables/dates.
- **2026-07-27 (later) — PLAN RATIFIED (James, with amendments):** (1) document material gaps, artifact-anchored, lawyer-readable; (2) peer corroboration of the Q1→Q2 reversal via ER, neutral prompts; (3) **comprehensive AND clear H1 downward feedback co-drafted with ER — this doc carries the forward guidance; NO separate expectations artifact** (supersedes that element of the 7/25 Leo rec); (4) regular ER check-ins (report the documentation comment verbatim + the visa mention factually); (5) **PIP consideration on James's clock post-reorg — the end-Sept checkpoint was NEVER ratified** (James 7/27: "2 month was never set in stone"; the 7/25 session-log "Decisions" line overstated it — corrected). **Second visa interpretation live:** he may hold an outside offer and need Pinterest's I-485 filing (→ AC21 portability) before moving — predicts compliance + maximum resistance to near-term employment threats + possible self-resolution; never enters any record or decision. Artifacts: `downward_reviews/h12026/yuke_h1_2026_review_draft.md` (v2, 7/27) + `yuke_h2_plan_2026-07-27.md` (deleted in the 8/1 cleanup — superseded by the mobility-clause design carried in the final H1 doc).
- **2026-07-31 — multi-sampling bug credit incident + final H1 doc + H2 flexibility design + cadence change.** (1) **Incident:** a bug in his pUIC multi-sampling PR was root-caused overnight by **Chuxi + Yidi** in their group DM (~9–11:30 PM 7/30: sampled path cut to 256 unpadded vs. the sms host's 500-length requirement, fails at legoconverter; fix = right-padding, designed by them). Next morning Yuke told James **in writing**: "I caught this bug within a few hours, already landed a fix… minor bug." James had already sent neutral forensic questions (who debugged/found it, what was the error, why not caught earlier) and Yuke committed to a **written summary** — he's on record before knowing what James knows. **Handling locked:** wait for the write-up, don't tip; verify with system artifacts (commit/PR timeline, same-bug check vs. the "unrelated error" in his notes) before treating as misrepresentation; **nothing shown to Yuke may be traceable to Chuxi's DMs** (screenshots stay ER-side; protect the source — she feeds the Aug–Sept peer validation); route via ER at the pre-review → likely a dated example under an "accurate representation of your own contribution" expectation or H2-ledger entry one. His 1:1 notes doc confirmed as careful defensive documentation (link-anchored, "[James]" attributions, "agree to disagree" logged; also claims "fully ramped up, consistent with previous estimate" about the experiment that was shut down with errors that same evening — self-recorded narrative-vs-dashboard gap). **Counter-discipline: James sends his own same-day written recap after every Yuke 1:1.** Alert-responsiveness ≠ improvement (the 6/29→7/06 step-up-then-surface pattern; the ledger decides). (2) **Final H1 doc:** James wrote it → `downward_reviews/h12026/yuke_h1_2026_feedback_final.md` (pre-ER fix list in header; assignment-independent goals + org-framed mobility clause = the 7/31 flexibility design). (3) **Fork held open (7/31):** at the ~Nov EM design point (T2 moved 8/3) either (a) goes with the RecGPT unit if the case is resolved, or (b) stays James-direct and reassigns to less-desirable-but-**measurable** work (guardrails: ride the org-design wave never a one-off, deprecations/cost-targets with dated endpoints not vague grind, **ER pre-clears the duties change with the I-485 flagged**). Reporting stays James through resolution — his counter-documentation makes transfer *worse* (fragments records, resets clocks, hands Alim a grenade, signals pressure works). (4) **Cadence (James, 7/30 Slack):** 1:1s → bi-weekly; weekly Monday posts in the Bella/James DM; bi-weekly summary in 1:1 notes.
### Alok Malik (L14, MLE)
> **Heading restored 2026-07-15** — this block had lost its `###` header and was rendering inside Yuke's section, silently attributing Alok's workstream + 1:1 to Yuke.

- **Workstream (current, 2026-07-15):** **Retentive Recs (primary) · Reflex.** Alok made the RR call himself, and James wants him there — **RR loses Yuke** (who goes to RecGPT only), so Alok is now load-bearing for that pod alongside Chuxi and Yidi.
- **Workstream (historical — SUPERSEDED):** Real-Time, PhP / Dynamic Triggering (~50% allocation, gate cleared March 30). Also supersedes v2 §Calls #3's "Reflex 50% + UPP 50%" — he is not on UPP.
- **Open — reporting line:** RR is Alim's charter but Reflex is James's. See the knock-on flagged in the roster section above.
- **1:1:** Thu 2:30pm
- **Context:** ELT presentation cleared funding gate. Alok moving to ~50% on Dynamic Triggering. Needs tight leash — give one scoped deliverable at a time. First task: scope Ads surface expansion with Mehdi (data, CG architecture, transfer analysis). Weekly review cadence on DT work.
- **2026-07-25 update — promo pressure vs. execution quality.** Alok is "being a pain as usual," high maintenance: **constantly asking about promotion** while **not being careful about his tasks and not going deep enough**. James actively working to get him back on point. Relevant to the Lionel ramp plan (Alok is the lean candidate to ramp Lionel — a coaching load on someone currently off-point) and to his RR load-bearing role in Alim's day-1 pod.
- **2026-07-31 — H1 review drafted + reporting resolved.** Review draft (developmental register — not a case; addresses the promo pressure head-on: the path is making the quality conversation disappear) → `downward_reviews/h12026/alok_h1_2026_feedback_draft.md`. Reporting: **→ Alim starting announcement week** (see roster). James delivers the H1 review as H1 manager; H2 tracking transitions to Alim.
- **2026-08-10 — unprompted 1:1 (James pulled him in) after Chuxi's ramp complaint; the relitigating pattern named.** *(James confirmed same session: the complainant is **Chuxi** — "Kurchi" was a dictation artifact.)* Her feedback, via the standing skip channel during their same-day 1:1: Alok isn't ramping into the RR/pUIC space; she doesn't want him on the project anymore; he's slowing her down more than anything. In the 1:1 Alok argued back and asked for more ramp time ("only been 20 days"); James left tired, feeling he's relitigating the same things; reads Alok as tired of it too. Converges with the 7/15 tight-leash and 7/25 promo-pressure/depth reads — a month-old pattern, not a ramp-speed artifact. **Open decision (with Alim, this week): re-scope, don't remove** — Alok stays RR (load-bearing as Yuke exits) but on separated, tightly scoped deliverables off Chuxi's critical path (the one-scoped-deliverable pattern that worked in spring; his Pinkerton secondary is a natural non-colliding lane). This is an intra-pod dynamic between two of Alim's reports — doubly Alim's to run. Handoff framing: attribute the flag as **TL staffing input** (depersonalizes it, builds Chuxi's TL legitimacy with Alim) — mindful she still carries the private Alim-backchannel prior, so calibrate attribution to what she'd be comfortable with; invite Alim's own read (his 8/5 take: "baggage with past, will warm up"). James stops direct alignment 1:1s; the drafted H1 review delivery is the one remaining James-owned conversation; future complaints route to Alim.
- **2026-08-17 — ESCALATED: the Alok↔Chuxi friction is now open conflict.** James: they're "not getting along… fighting" — the 8/10 one-directional complaint (Chuxi flagging Alok's ramp) has become a two-way fight. **James has a rough plan and intends to resolve it within ~2 weeks (by ~8/31)** — plan contents not yet filed ⟨capture when James shares⟩. Timing pressure: this is an intra-pod conflict inside Alim's day-1 pod during his ramp, RR is the load-bearing workstream, and **Kim is about to talk to Chuxi (~this week) as diligence on joining RR** — an open fight in the pod is exactly what could tip her toward the CLR fallback (her decision due 9/11; see §Kim Toy — Archive below). The 8/10 open decision (re-scope-don't-remove, routed to Alim) is now urgent, not pending.

### Chuxi Wang (L14, MLE — Retentive Recs, IC grow-in-place)
- **Role:** Primary IC on Retentive Recs / p(UIC). Promo vehicle. *(Prior "Incoming TL pending Yuke's IC transition" framing retracted 6/30 — see below.)*
- **Workstream:** Retentive Recs
- **1:1:** Wed 4:30pm
- **Context:** Bridge between Yuke (Retentive Recs) and Devin (CLR) on retentive signal integration. Make sure she's in architectural decision rooms, not just execution. Building independence as hedge against Yuke departure.
- **2026-06-24 update — TL succession.** James plans to give Chuxi most of Yuke's TL responsibilities once Yuke's path is formalized (Monday 6/29 1:1). Already has context on pUIC serving challenges; Yidi confirmed she's been involved in model-based pUIC. Model side easy pickup. Clean growth story. Chuxi does not yet know she's being considered — conversation pending Yuke decision.
- **2026-06-30 correction — Chuxi is NOT an imminent TL.** She's **IC14**; the Retentive Recs TL role is **IC16 minimum** (two-level gap). The 6/24 "give Chuxi most of Yuke's TL responsibilities" succession plan is **retracted** — she grows *in place* as an IC, gaining scope/visibility under Alim (his job as her manager), not by title. Yuke stays with Retentive Recs (A/B pending — see 6/29 entry). Ignore "incoming TL / IC17 path" framing.
- **2026-07-07 — sponsorship conversation (went about as well as possible); gradual TL ramp agreed.** James delivered "I'm your sponsor no matter what"; through the conversation **she accepted that skip-level sponsorship can serve her better than direct-manager sponsorship.** Her words: James is **one of the best managers she's ever worked with** — she didn't want it to change; James promised continued close work. **TL question asked directly** ("can you step into the TL role?"): her answer = yes-with-conditions — wants **a lot more support**, wants to **start slow / transition gradually**, **no drastic announcements**; wants real **decision-making over technical + longer-term calls** and to **help grow others**. *Reconciliation with the 6/30 IC14-vs-IC16 correction:* this is NOT a title announcement — it's a supported, unannounced ramp into technical leadership of pUIC (model-based + LLM-based) as Yuke exits the space; the formal TL answer to Dylan is still James's to propose. Also: given a choice of who to work with; **Ling Lan** (incoming with Daniel Liu's team; built the LLM-pUIC inferencing pipeline, already works with Chuxi daily) is the natural delivery partner.
- **2026-07-22 update — ramping well as TL; surfacing Yuke's neglect.** James's read: Chuxi is **doing a great job ramping into the TL role.** As she takes ownership she is **uncovering issues that fell to the wayside during Yuke's earlier distraction** — independent corroboration of the neglect. She and James **jointly decided to move Yuke fully off Retentive Recs** (see Yuke 2026-07-22). Strong ownership + judgment signal; the grow-in-place TL bet is paying off.
- **2026-08-02 — the TL role is now in writing.** Her H1 draft says *"as you step into a technical leadership role for Retentive Recommendations"* and names above-level signals plus "position you for impact beyond the IC14 bar." The repo has recorded this as a **supported, deliberately unannounced ramp** since 7/7 — written feedback is durable, so the role is now formalized *for her* whether or not the team is told. H1 impact: UIC signals in CLR (+0.11% SSv2 unique users, +0.17% DAU, +0.14% WAU) and the frontier-sampling iteration (+0.22% SSv2 proxy, +0.80% HF repins). Growth edge = **prioritization**: several 0-to-1 threads progressed without converting to launched impact, and peers flagged she gets "stretched too thin" by ad-hoc pulls.
- **2026-08-10 — 1:1 went well (TL ramp deepening) + first hard staffing flag via the skip channel.** James's read: she's gravitating toward the TL coaching. In the same 1:1 she flagged that **Alok isn't ramping into the RR/pUIC space and is slowing her down — she doesn't want him on the project** (filed in Alok's entry; dictation artifact "Kurchi" corrected same day). Read this as her **prioritization growth edge working** — her H1 flagged she gets stretched thin by drag on her critical path, and here she's naming the drag instead of absorbing it. Action routed to Alim (re-scope Alok off her critical path, not off RR); when attributing, use TL-staffing-input framing and stay mindful of her comfort level with Alim given the backchannel prior. Doing her own diligence on the new folks' LinkedIn, she found her ex-Google manager connected to Alim, got a troubling read back (details → Alim's Tier-1 entry; sensitive), and brought it **straight to James privately** rather than letting it travel — even offered to hold it ("not sure if you want to hear it now"). Was genuinely rattled ("really appreciate you offer chatting with me on weekends"); James took a Saturday call — calmed + reframed (observe/corroborate/don't-conclude; judgment-building opportunity). Mon 7/27 1:1: James reconfirmed skip-level sponsorship, staying very close, and watching Alim's ramp; she "seems fine at this point." **Watch:** she moves to reporting to Alim carrying this prior — her comfort/safety read during his ramp is a **first-class signal, not noise**; keep the standing private skip channel where she can flag anything early. **8/17: the Alok friction is now open two-way conflict** — details + James's 2-week resolution window in Alok's entry above; also note Kim will approach her (~this week) for RR diligence while this is live.

---

## Tier 2 — Biweekly 1:1s

### Zihao Chen (L15, MLE)
- **Workstream:** UPP (feature alignment, surface documentation), Content Exploration (~50%)
- **1:1:** Mon 3:30pm
- **Context:** Transitioning deeper into UPP architecture. Accelerate understanding by pairing with Piyush.
- **Growth:** Demonstrate basic project leadership on Content Exploration.
- ~~**2026-07-15 — the contested one.**~~ **SUPERSEDED 2026-08-01/02.** Zihao is **UPP full-time and was never on Retentive Recs** (work-leo delta correction); Alim's day-1 pod is Chuxi / Yidi / Alok / Lionel with **no L15 or above**. The move that this entry called unresolved never happened, so the UPP hedge stays intact under James. Kept for provenance: at **L15**, Zihao was at one point slated as the *only* senior IC in Alim's pod. He is also the **UPP succession hedge against Piyush** (see Single Points of Failure below). Moving him to Alim puts the UPP hedge inside another EM's pod, pointed at a charter (exploration) that pulls him away from UPP. Alim's first-sync agenda already carries the mitigation ("coordinate with Piyush before pulling him fully into exploration") — i.e. a hedge against a problem the move creates. **Unresolved.**

### Yali Bian (L15, MLE — LWS de facto owner / TL)
- **Workstream:** LWS + L1 Utility (de facto owner and TL) · **SM/SL retrieval-side co-owner**
- **1:1:** Thu 3:00pm (alternating with Hedi)
- **Context:** Give recognition. Consider one bounded project outside LWS to build range.
- **2026-08-02 — H1 record (from James's own v2 draft; the entry was 3 lines before this).** Verdict: **trending above IC15 MLE expectations — the strongest verdict in the H1 cycle.** Eight LRs delivering SSv2 +0.31 and SSv2-proxy +0.875; two foundational launches onboarding candidate generators to LWS (coverage toward ~80%, ~$67K cost savings); productionized LWS **GPU serving and migrated 100% of traffic**, resolving multiple SEVs — stable 3+ months with no GPU incident; **re-architected the LWS data/training pipelines, cutting training time from 40+ hours to ~7**. Peers: "strong ownership and independence," "clear communication and documentation."
- **2026-08-02 — SM/SL is the H2 test.** Named **retrieval-side co-owner with Raymond Hsu** (front end) — a true co-ownership seat, no primary/secondary — chosen by James with **strong endorsement from leadership across the org**. SM/SL is one of **Jeff's three stated priorities** ("for Bill Ready") and carries the highest visibility any IC on the team touches. ⚠️ **The success-criteria conversation with Dylan is still owed** (carried follow-up #7) — until it lands, accountability exists without an agreed definition of success.
- **Growth edge:** cross-org voice. Communicates well 1:1 and documents carefully — this is not a general communication weakness. The gap is **stating and holding a technical position in cross-org rooms before consensus exists**; in senior rooms, silence reads as agreement. Second edge: portfolio-level prioritization (roadmap time, breadth-vs-focus choices) rather than pure hands-on intensity.
- **⚠️ Pronoun ambiguity, unresolved:** this file uses she/her; a peer quote in the H1 v1 draft used "his," and James's v2 re-cut the quote so no pronoun appears. Confirm before anything is written where it matters.

### Hedi Xia (L15, MLE — LWS)
- **Workstream:** LWS preranking · unimpressed track · iterative diversity
- **1:1:** Thu 3:00pm (alternating with Yali)
- **2026-08-02 — first real record in this file.** Until now this entry was two lines: the thinnest of any tenured IC in the repo. Everything below comes from James's own H1 draft. **H1 2026 was Hedi's first review period at IC15.**
- **The headline: lead author of the RecSys preranking paper — ACCEPTED, with a 15-minute oral.** Fourteen pages, thirteen co-authors, carried from draft through submission. Establishes alignment and accuracy as the defining principles for the L1 layer. **This closes the stale backlog item that still read "confirm the RecSys 2026 deadline"** — the paper is in. Open: who presents, and whether the oral is worth staging as a team-visibility moment.
- **Technical contributions:** key contributor on the **unimpressed track** — designed model requirements, the pairwise distillation loss, and the blocking/optimization algorithms that made it computationally practical; supported launches across training-serving alignment, multi-embedding funnel efficiency, rank distillation, and early-funnel distribution. With Yidi, launched **LWS unified tower/transact (+0.10% total SSv2)**; ramped Yali on shopping CGS into L1 utility (+0.03% SSv2, +0.11% proxy). **Iterative diversity** — reframed diversity from a deterministic post-ranking layer into an optimization over L1 utility (+0.17% SSv2 proxy, +0.16% impression diversity).
- **How peers read them:** "strong technical depth with a quantitative lens," "careful, rigorous, and dependable," identifies risks early, "consistently turns discussions into deliverable outcomes." Distinctive strength = **first-principles reasoning**.
- **Growth edges:** (1) convert depth into a **more consistent cadence of shipped production gains** — one peer's framing was to "lean a bit more into an engineering mindset as distinct from a research one"; time-box exploration rather than resolving every uncertainty first. (2) **Broaden first-principles influence across the stack** — engage Dafang and the L3 diversity direction, carry ideas back into L1. (3) Give collaborators the *why*, not just implementation detail (the Zili handoff created avoidable confusion).
- ⚠️ **H1 doc has no explicit verdict sentence** — unusual for the cycle, and conspicuous in a first review period at a new level. Also: goal 1 asks Hedi to follow **Yali's** project leadership, and they are the same level.
- **Pronouns not stated anywhere in the record** — they/them used here by default.

### Yidi Wang (L13, MLE)
- **Workstream:** Retentive Recs (fractional), Content Exploration (fractional)
- **1:1:** Wed 4:00pm (alternating)
- **2026-08-02 — H1 record (from James's own draft).** Verdict: **solidly meeting IC13 expectations**, framed toward IC14. Largest contribution = implementing the **model-based pUIC serving path end to end** across model export, Scorpion GPU serving, and Unity retrieval: identified the SMS/RecGPT feature incompatibility and drove the **L500 migration**, rewrote model-export logic to produce deployable TorchScript, resolved int8/fp16 dequantization and Scorpion input-signature issues, and implemented the Unity serving graph — the production path the initial A/B is now running on. Also ran the heuristic pUIC outward-expansion experiment to a clean negative (useful: ruled the direction out). In **Content Exploration**, implemented most of the indexing-and-serving pipeline on the Manas Unified Embeddings Framework, without owning the end-to-end design. Peers: "ramped up quickly in a previously unfamiliar domain."
- **Scope-to-level note:** at **L13** she is carrying most of model-based pUIC — **the largest scope-to-level gap on the team**, and the strongest argument in her eventual IC14 case.
- **Growth edges:** (1) **proactive communication as a default** — the SMS/RecGPT constraint and the Scorpion blockers both surfaced later than they should have; this is a continuation of 2025 feedback, though peers explicitly recognize real improvement. (2) Move from strong executor to **self-directed ML owner** — she had a good idea (temporally ordered UICs) but raised it in a 1:1 rather than in a technical forum.
- **Reports to Alim from announcement week.**
- **2026-06-24 update.** Flagged to James (unprompted) that Yuke has been less engaged and she's been carrying most of the model-based pUIC implementation. Zelun (ATG) is the cross-team collaborator on this work. James asked her to add him to Slack threads with Yuke and Zelun — she agreed but wants their permission first. Strong signal of good judgment and communication; James gave her explicit positive feedback on communication dimension (significant improvement, lots of posting). Yidi also confirmed that Chuxi has been involved in pUIC and knows the serving challenges.

### David — DEPARTED
- **Status:** Gone (departed ~April–June 2026; negotiated a 2-month extension to his vesting cliff). Not on the 7/15 roster of 26. Cited alongside Sophia as churn context in the H1 self-review.
- **Former workstream:** L1 Utility — transferred to JJ, with Rui Wang now the operational owner underneath.

---

## Tier 3 — Monthly 1:1s

### Hanlin Lu (L14, MLE — RecGPT)
- **Workstream:** RecGPT / GenRet · Multi-Embedding
- **1:1:** Wed 4:00pm monthly
- **Performance:** ~~Hard mid-April checkpoint; if not shipping, moves to LWS.~~ **Resolved — H1 came in strong.**
- **2026-08-02 — H1 record (from James's own draft).** *"Congratulations on a strong first half… I'm happy with your performance."* Primary contributor to the **official HF-RecGPT CG launch**; led the diversity improvement via Gaussian noise; drove the **candidate-budget expansion transferring 150 sizers from Multi-Embedding to HF-RecGPT** (high ROI for a focused change); owned the **RecGPT ANN serving migration from Faiss to Manas (~$60K savings)**; collaborated on moving sequence serving onto UserEventsView. Led UOE and Decoupled Entity Representation on Multi-Embedding, and stepped up through the **HF Multi-Embedding GPU Serving rollout** to completion. Presented at **ML Symposium 2026** on productionizing generative retrieval.
- **The Manas migration is the growth story:** end-to-end ownership was the 2025 development area, and H1 showed clear improvement — worked through serving details, followed up proactively, documented, and carried it to conclusion. Peers: "takes the time to understand what is happening end-to-end rather than only looking at surface-level symptoms."
- **Growth edges:** turn technical activity into **named launches with topline SSv2 impact** (several H1 experiments — larger batch sizes, SID augmentation, GQA — produced offline gains that didn't translate online); develop **system-level judgment** to find more sizer-class opportunities; keep updates concise and decision-oriented. **"Exceeds at year-end" is named as reachable** — one of only two trajectory statements in the cycle.
- **H2:** co-mentors **Arowa** with Zihao. **Moves with the GenRet charter at T2** (James, 8/2).

### Sophia — DEPARTED
- **Status:** Left Pinterest (attrition, 2026). No longer on the team. Her loss is the "1 head already lost to attrition" precedent referenced in the Bella-backfill reasoning — the reason a slipped backfill can't be allowed.
- **Former workstream:** UPP

### Zili — pre-PIP sequence live (ER engaged 7/22 · feedback delivered 7/30 · PIP gate ~8/13)
- **Workstream:** LWS
- **1:1:** Tue 1:30pm monthly
- **2026-07-22 DECISION — move on the perf case:** James decided to act and **reached out to ER to start the process.** Ends the "manage rather than exit" holding pattern below. **Correction 7/30: "PIP initiated" overstated the state** — what started 7/22 was the ER engagement; ER's advice (Tue 7/28) is a pre-PIP sequence: (1) gather evidence/feedback from tech leads, (2) clear feedback in next 1:1, (3) **initiate PIP in 2 weeks if no improvement.**
- **2026-07-30 — step 2 DONE, feedback delivered in 1:1.** Three dimensions, sourced from TL feedback + James's observations: **Depth** (doesn't work blockers/nonsensical results herself before escalating), **Deliverables** (learnings/metric improvements/documentation below level bar), **Proactivity** (specifics TBD — bullet was empty in James's own notes; must be filled in the written recap). Severity named explicitly ("may have to move to more structured improvement plans") + support offered. **Her response: stoic** — "Ok," one question ("What are you expecting?" — answered with restated gaps, i.e., diagnoses not targets), "Nothing right now" to the support offer. Leo: don't over-read the flat affect (leaving / shut down / furious all consistent); her reply-or-silence to the written recap is the first real datapoint.
- **Sequencing vs. her PTO (8/18–9/3, approved, plans made):** the 2-week window **7/30 → ~Wed 8/13 fits entirely before PTO** — no pause needed. Progress review in the 1:1 week of 8/10; assessment on schedule ~8/13. **If it fires: do NOT initiate 8/14–8/17** (PIP-before-vacation = stew + adversarial return); prep paperwork with ER during her PTO, **open Tue 9/8** (9/4 = Friday before Labor Day, same problem). Get **ER sign-off on this sequencing this week**, not at the gate. Written same-day recap with concrete observable criteria per dimension = the artifact that makes the gate measurable (paste-ready draft delivered in-session 7/30; ER gets a copy).
- **Watch-fors:** live possibility she returns from PTO with a resignation (2.5-wk decide window right after a severity conversation) — process and record continue regardless; **keep the case with James through the reorg settle** — no reporting transfer mid-process.
- **2026-07-31 — written H1 review drafted** → `downward_reviews/h12026/zili_h1_2026_feedback_draft.md` (three dimensions mirror the 7/30 delivery; 4/06 FM-incident as the dated depth example). **Critical fill before ER: the Proactivity dimension still has no concrete examples** (empty in James's own 7/30 notes — weakest leg of the record). ER also owns: delivery timing vs. the ~8/13 gate + recap consistency, and whether the severity sentence goes in writing.
- **Performance:** Known underperformer. Not as urgent as Charlie — no backfill available, so manage rather than exit. Recurring pattern flagged by Bowen (previous manager) and multiple TLs: insufficient communication depth, doesn't show investigation work, escalates externally without demonstrating internal ownership.
- **2026-04-06 incident:** FM training job failed on CPU resources. After 3 hours of surface-level slack updates ("Yali suggested X, Piyush suggested Y, asking ray team"), James pushed for a debugging doc showing her own investigation. She declined, citing "the thread already contains all the info." Confirmed the pattern. James documented via slack (paper trail). She knows she's an underperformer.
- **Approach:** Backfill constraint means no active manage-out. Continue documenting pattern. Give clear, written expectations at next 1:1 (Tue 1:30pm). Don't invest disproportionate coaching capital — Charlie is the clearer case for action first.
- **Watch-for:** Whether Piyush also starts flagging. If so, the performance picture tightens and the backfill calculus may need to be revisited with Dylan.

### Charlie — EXITING (formal PIP/CPP)
- **Workstream:** AI projects (under James's direct TL supervision)
- **Status:** On formal PIP/CPP (decision 2026-04-07; CPP started 4/30). Exiting; James gets the headcount back. The backfill head is routed to **Alim's team** (Anticipation / RecGPT) per the 2026-06-17 team-split proposal.

---

## Kim Toy — Archive (merged 2026-08-17)

> Working archive for Kim Toy (L15 MLE, Curation ML; T2 placement in progress). Created 2026-08-13 as standalone `kim_toy_archive.md` when the volume outgrew the scope-table row; **merged into this file 2026-08-17 (James: no standalone doc)**. **Current-state row:** §Full IC roster above. **L16 seat design + 3-way script:** `reorg_july2026/t2_team_setup_scenarios_2026-08-11.md` §Kim. Dated entries newest-first; source material verbatim below each entry.
>
> ⚠️ Standing confidentiality: the not-Daniel datapoint (8/11) and all Dhruvil 1:1-only intel never leave James's head — not to Alim, not to the trio room, not to the 3-way.

---

### 2026-08-17 — The pause: she asks for time; decision by 9/11, CLR named as the alternative

**The surprise of the day (James's word).** After the 8/13 self-selection into RR, Kim **asked for more time to decide.** Same day, **Alim told James he really enjoys conversations with her and would love to have her as part of Retentive** — so the pull from the receiving team is now explicit and warm; the choice is genuinely hers.

**The settle, from a quick James↔Kim call:**
- **She decides by Thu 9/11** — basically one week after she's back from vacation ⟨implies she returns ~9/4; confirm dates⟩.
- **Her alternative, named: CLR** — "if it comes to that." So the decision space is RR-under-Alim vs. CLR, no third option on the table.
- **Next step, hers:** talk to **Chuxi** ⟨dictated "Chushi"⟩ first to understand the type of work involved, then go from there.

**Leo reads:**
- The hesitation is in-character, not a reversal — her own 8/13 transcript named it: *"what if I switch to a new area and it turns out things are not going well… we don't want to keep switching."* The 8/13 enthusiasm and the 8/17 pause are the same person: loves the work, fears the switch. Asking to talk to Chuxi first is her doing diligence exactly the way the change-fatigue read predicts.
- **The Chuxi conversation is doing double duty.** It informs Kim's choice *and* it's the first live contact of the pair the T2 doc flagged (senior addition to RR ⇒ explicit Chuxi role-design, due before 8/21). How that conversation lands — whether Chuxi reads Kim as reinforcement or encroachment — is a first-class signal for the role-design work, on top of Kim's own decision.
- **CLR-as-fallback couples her decision to the Alim/CLR machinery:** CLR ramps under Alim's leg (Nima/Devin/Kim-relevance bench per the Daniel action plan) — so *both* branches of her decision land in Alim's orbit one way or another. Also note 9/11 is the same date Daniel's dark window ends: the Kim settle will not close before Daniel departs 8/21, which changes the Tue 8/18 Daniel 1:1 "Kim proposal co-design" from closing a placement to designing around an open one.

---

### 2026-08-13 — 1:1 #2: Kim self-selects into Retentive Recs

**The landing (James's summary):** she really enjoys Retentive Recs; after James walked the project description she loved it more and wants to work on it. Framing agreed in the room — the two current challenges: (1) model-based pUIC, making it more explorative; (2) fetching relevant results given an explorative pUIC. She's already on #2 via search-stage CLR → lean into that, grow there, hoped path = modeling changes aimed at RR workstream goals. She is careful NOT to claim the TL role because of Chuxi ⟨dictated "Kurchi," resolved to Chuxi — RR's TL bet per the T2 doc; confirm⟩ but wants to lean in carefully. Excited; wants to talk to Alim and just get started. **Her main concern: no very-senior person in that space to work with and learn from.** James's answer in the room: **Olafur Gudmundsson** ⟨dictated "Oliver," resolved by James 8/13⟩ — Sr. Staff MLE (IC17), reports directly to Dylan, Content Exploration space, KDD-paper Federation co-author, active pUIC/UBR architecture reviewer, FBL launch with Andreanne/Armando — genuinely senior and genuinely in-space. End state per James: bulk of time in RR + helping CLR (relevance). **Next step: James 1:1s Alim BEFORE the Alim↔Kim chat (already scheduled to happen anyway) — gives him the context, asks him to decide whether he'd enjoy working with Kim.**

**Deltas vs. the 8/12 design** (T2 doc §Kim — logged there as Update 8/13):
- Designed seat was UEB-side exploration surface, **explicitly NOT RR** (Chuxi-runway protection). She self-selected into RR proper. The Chuxi role-design flag (T2 doc: "any senior addition to RR needs an explicit Chuxi role-design") is now **live and due before Fri 8/21**.
- No UPP bridge mentioned in the landing — the designed optional ~25% continuity looks dropped in practice; wind-down mechanics (Dhruvil pre-agreement, Aditya backlog handoff, Yan management) now need executing.
- The diagnosis conversation (setup-not-performance, calibration sponsorship, honest H2-2027 timeline) was NOT delivered in part 1 — still owed.

**Transcript themes (her voice):**
- **Context-switching is the top pain:** onboarding CLR + notifs stack + UPP simultaneously; "instead of trying to go deep… I'm just trying to get work done," never building understanding.
- **Switching hesitancy, named:** "what if I switch to a new area and it turns out things are not going well… we don't want to keep switching." (Reads as the change-fatigue/career-anxiety thread from the Dhruvil intel.)
- **Wants a dedicated, in-space senior TL** who holds her progress in mind — vs. context-switched advisors. Positive counterexample she volunteered: Piyush, Devin, Jaewon ⟨dictated "jaewong"⟩, Hongtao all proactively chip in and track what's going on.
- **The UPP support failure, precisely articulated:** Aditya (HF background, leads UPP infra, assigns her work) gives general suggestions without surface experience — doesn't know the metrics notifs cares about or the pipeline gotchas; the notifs team isn't looped into UPP infra meetings. Anya (PinRec TL, incidentally doing infra work) helps out of goodwill but has different motivations. Net: advisors without shared accountability — "it doesn't feel like I'm on the same team as you… there's not necessarily a motivation to really help and make sure my work goes through." She ends up scheduling sit-downs to force decisions and hates the overhead.
- **What brings her joy:** ramping a new area to feeling-like-an-expert; then explaining it, knowledge-sharing, documentation (latest model bundle, deploy processes). Worry attached: agentic flows make docs feel derivable-from-code; "we don't talk to each other enough and I'm falling into a trap like that"; general concern about how the future evolves (James: "we'll figure it out, things will stabilize").
- **Product-facing > pure modeling:** ranker side-by-sides at this level of optimization look indistinguishable to her ("both seem fine"); RR appeals because new content surfaces visibly — modules, features, impact you can see. "Happy to put product mindset into that." Enjoyed being part of a new thing spun up from scratch.

#### Verbatim — 1:1 part-1 transcript (dictated; names sic)

Kim: To digest but it's great to see how much work people are getting done. That's not the main point. The main point is really just making sure that you get a sense of the type of work. I added the LRS and launches because that's the work that is prioritized on those work streams. Hopefully you get a sense of what kind of work leads to launches on those work streams. Totally that makes sense.

I think I was gonna say I would love to get into more technical depth in these but I don't know what makes sense for us to spend our time on. If you have a way that you want to drive this discussion, I want you to be happy. Kim, that's my motivation. I believe that happy people do their best work and happiness is not like, "Oh man, I'm so joyful." It's more like, "Okay, it means different things to different people. For you in particular, I have a read. My initial read, I'm happy to share my read with you, but I also want us to iterate on that read, iterate on, and align on what makes sense as your path forward. I want us to be forward-looking and look to the vast arsenal of possibilities that exist and really pick something that delights you." That's really my goal.

That makes sense. I'm curious to hear your read but I guess I'll throw out some things that are top of mind for me in no particular order, just things I noticed about myself that maybe seem to work well or don't seem to work as well. I like about my current situation. I think one of the difficult parts is being pretty context-switched and trying to work in two very split areas, like trying to onboard onto CLR and the notice stack and UPP at the same time. I'm not sure that's the most amazing setup.

I find that instead of trying to go deep and better understand a system, I'm just trying to get work done and, by virtue of that, not spend as much time to understand because I'm just like, "Well then I'm never gonna get anything done." That's a little tricky versus getting a better understanding.

I'll admit I'm a little bit hesitant to switch at all just because I'm like, "Oh no what if I switch to a new area and it turns out things are not going well and then that would not be good. We don't want to keep switching. That's bad for everybody." A little hesitation there.

I think it would be nice to more closely work with people. I don't know if this is completely necessary but maybe having somebody who is a more dedicated TL to the space with some more expertise and being able to learn from them. The fact that they're probably focused on this particular area you're working in this area and that they'll have a reasonable sense of your progress, as opposed to, say, people not necessarily paying attention because they're also very context-switched and too busy to keep it in their mind.

I'll say even just appreciate, take piush and devin and jaewong and Hongtao, all chipping in. They all seem to have a reasonable sense of what's going on and are able to give advice so I appreciate everyone's proactivity. That's a counterexample. You've noticed, basically. Sorry was that a question? I'm just wondering because you want a stable TL who's focused on the problem, which is where I heard. The example you raise around puge and others, that's a counterexample, right? Okay, right.

Aditya is a HF engineer, but that is his experience from the work he did before. Yet the work I'm doing is mostly notifications. He's leading the UPP effort, like the infra effort, and is the one who has the general backlog in his mind and is trying to assign work and such.

It's not amazing because then if I come to him and kind of say, "I'm working through this. I am stuck here trying to work my way around," he might have general suggestions just from being knowledgeable but not from the basis of having experience with that surface, knowing what metrics they care about. Like some gotcha with the pipeline that someone on the team would have known. The notice team themselves is not necessarily all looped into UPP infra meetings and everything, right?

Just by virtue of the fact that Anya happens to be working on some infra stuff herself, it's like, thank goodness she's there. As the TL of PinRec as well she's also trying her best to give advice but I think she also has different motivations, right? Aditya cares more about the work he gives me, shipping idea, just cares from the stake of being a good person. It's more like both will try to give advice and we'll try to help debug but it doesn't feel like I'm not on the same team as you and we're not under the same manager. There's not necessarily a motivation to really help and make sure that my work goes through.

She'll try her best to answer but sometimes I feel a little stuck on how to move forward. The best I can do is schedule sessions with both of them and be like, "Hey, sit you guys both down. I heard this from you. I heard this from you. Let's make a decision how we're gonna move forward with these metrics. Okay what do we abandon the project?" Yeah this kind of thing. I don't enjoy the extra overhead.

James: What brings you joy?

Kim: and feeling comfortable around it, like being introduced to a new area, discovering the ins and outs, and basically feeling more like an expert. That's an exciting feeling. I like that, then being able to explain it to other people, being able to help other people understand, answer questions, and knowledge share. I like documenting stuff and making it easy for people to find how to do whatever it is, like what is the latest model bundle that you should use, what are the deploy processes, these kinds of things.

I like documentation. I wonder how much this does become outdated with the way that we should work nowadays with a lot of agentic flows. The kind of worry is that people are just like, "Well you can derive it from the code," which is true. "Okay ask the LLM to do some of this analysis for you." I just worry that we don't talk to each other enough and I'm definitely falling into a trap like that.

I don't know, concerns over the future. Don't know how things will evolve. Don't worry about that. We'll figure it out. Things will stabilize.

I think I do enjoy product-facing things a little more. I think pure modeling work is just like, you make improvements, you see numbers go up. That's great but it is more exciting to see things, I guess, appear as a product feature or to really visualize the impact. Sometimes we'll try this with modeling changes, like a ranker improvement. You try to run side by side and see if there's a difference. It is kind of difficult. It feels like just because at this point things are so optimized, I don't see a difference. Both seem fine to me.

I feel like that's why the retentive frex side does slightly appeal more because of the idea that somebody will see new content and that we can also make it appear not just as content in a feed but as modules explicitly. We can build new features around this and have it surface differently and become more obvious to users. I'm happy to put product mindset into that.

Enjoyed being part of a new thing and spinning it up from scratch.

#### Verbatim — James's landing summary (dictated; names sic)

Now finally: what she and I agreed on is that she really enjoys retentive recommendation and after I went through the project description she loved it even more and she really wants to work on it.

We also went over a framing of the current challenges:
1. Model-based P.U.I.C. and making that more explorative
2. Actually being able to fetch relevant results given an explorative P.U.I.C.

She's already working on the second one as part of search stage CLR so I'm saying let's lean into that and she can continue growing there. I'm hoping that she can make modeling changes but work towards this retentive recommendation sort of like work stream goals. She's also very careful. She's saying she doesn't want to claim to be the TL there because of Kurchi but she wants to be careful leaning in. She's excited and she wants to talk to a limb to figure things out and she wants to just get started.

Her main concern was not having someone very senior to work with and learn from in that space. I told her that Oliver actually is a great person she can work with in this space. That's sort of how we landed on things. I do think if this works out she can spend the bulk of her time in retentive while also helping with CLR, making it more relevant and things like that.

I will have a 1-on-1 with ALim before he meets her. He's already going to meet her anyway. I plan to kind of give him the context here and ask him to decide whether he would enjoy working with Kim.

---

### 2026-08-13 — IC16 performance narrative (4-year review synthesis)

Summary pasted by James this session; the full evidence-based report (chronological arc, rationale, project recommendations, nuances) lives as **`Kim_Toy_IC16_Performance_Narrative.md`** — generated outside this repo (not yet filed here). Source limitations noted in the report: 2020/2021 docs are ratings-only, no 2022 review supplied.

**Read-across to the RR landing (Leo):** the report's "best-fit next project" spec — high-reach relevance/ranking initiative, ambiguous scope, multiple partners, *direct model or ranking ownership*, reusable platform components, production experimentation, owned topline metric — is nearly a description of the RR seat, **provided her charter includes challenge #1 (model-based explorative pUIC), not just #2 (retrieval/fetch)**. Gap 2 (model-depth) is the one the seat could fail to close if she stays retrieval-only; gaps 4–5 (visible/assertive judgment, developing independent owners) are what the not-claiming-TL instinct would leave unexposed without explicit lane design.

#### Verbatim — narrative summary as pasted

##### Core narrative

> **Kim turns ambiguous, multi-team ML product efforts into scalable systems and coordinated execution. She creates technical clarity, builds reusable foundations, raises the engineering bar, and enables other engineers to deliver.**

Her progression is clear:

- **2023:** Strong technical execution expanded into project leadership and cross-team alignment.
- **2024:** Board Ranker established her as a foundational leader for the Curation ML team.
- **2025:** She operated at workstream scale—setting strategy and priorities for a 7+ engineer virtual team, driving execution, and improving organizational effectiveness.

##### Strongest attributes

1. **Creating direction from ambiguity** — She consistently identifies the real problem, clarifies tradeoffs, establishes a roadmap, and coordinates execution. TiDB, Board Ranker, and AutoCollage all demonstrate this pattern.
2. **Building reusable technical foundations** — Her work tends to outlast the immediate launch. Board Ranker created the team's first end-to-end modeling foundation and was subsequently reused. AutoCollage similarly produced reusable versioning, evaluation, monitoring, and generation infrastructure.
3. **Strong technical and operational judgment** — She recognizes unsustainable designs, hidden bottlenecks, operational risks, and wasted work. The most visible example was the **17× AutoCollage generation-speed improvement**, which unblocked the MVP.
4. **Multiplying the engineers around her** — Mentoring, onboarding, design reviews, documentation, and engineering standards recur throughout the reviews. By 2025, she was guiding a broader backend/ML group rather than only immediate project collaborators.
5. **Written clarity and engineering discipline** — Her design documents, roadmaps, launch materials, retrospectives, and decision tracking are a genuine mechanism for scaling her influence.

##### Consistent gaps relative to IC16

1. **Connect technical wins to topline outcomes** — Excellent technical metrics (17× speed, production scale, coverage, infra reuse) but recent feedback repeatedly asks for clearer linkage to engagement, retention, relevance, SSv2, or comparable company outcomes.
2. **Deepen model-focused ML ownership** — Board Ranker and LLM evaluation establish ML credibility, but her largest recent impact is weighted toward backend, platform, evaluation, and launch leadership. A stronger staff MLE case would include direct ownership of model or ranking innovation through production impact.
3. **Repeat the staff-scale pattern in a higher-reach domain** — AutoCollage is strong evidence of next-level scope, but it became a limited-reach and deprioritized area. Reproducing this leadership in a strategically central domain would make the case much more durable.
4. **Make her judgment more visible and assertive** — Communication quality is a strength. The gap is ensuring critical information and recommendations repeatedly reach all necessary leadership forums—and pushing more directly when risks or weak tradeoffs threaten the outcome.
5. **Develop independent technical owners** — Her mentorship is strong, but the next step is helping engineers formulate options and make decisions independently rather than relying on her for answers or detailed review.

##### Best-fit next projects

The strongest assignment would be a **high-reach relevance or ranking initiative** that combines: ambiguous product and technical scope; multiple engineering and cross-functional partners; direct model or ranking ownership; reusable platform components; production experimentation; and a clearly owned topline metric.

Other strong fits: an end-to-end **model-plus-platform** initiative; a multi-team ML program with substantial subprojects delegated to independent technical owners; a quality/evaluation flywheel connecting human or LLM evaluation directly to model iteration and online outcomes; a strategically important ML initiative that is blocked or off track, provided she owns it through the resulting product outcome—not merely the technical rescue.

##### IC16 assessment

Based on the supplied reviews, Kim has demonstrated that she **can operate at staff-shaped scope**. Her 2025 year-end manager feedback explicitly recognizes higher-level performance in technical strategy, roadmap shaping, and team-level execution.

The remaining question is less "Can she lead at that scale?" and more:

> **Can she reproduce that leadership in a strategically central ML domain, deepen model-level ownership, and deliver a clearly attributable business result?**

That would turn a strong emerging IC16 case into a durable one.

---

## Adjacent / Cross-Team (not direct reports)

### Edward Zhuang — partner EM (client side)
> Added 2026-08-11 from the Daniel 1:1; role resolved same day via the area-9/10 descriptions.
- **EM partner on Intelligent Boards** alongside Daniel (Daniel: reviewing executions, providing guidance, building with AI). His team owns **client implementations**: Josh + Tianhao (Collection P13N clients), Jiaqi + Yash (IB clients). Org/level still unstated — likely a P13N-Experiences/client org.

### David Yun ⟨org/role unresolved⟩
> Added 2026-08-11 from the Daniel 1:1 — new name, not previously in the repo.
- Counterpart for the **Feature Boards infra-cost sponsorship** question (~$50M/yr revenue surface, low engagement — "can we get infra cost sponsorship" discussion is with him). Likely infra-side; resolve.

### Olafur (TL, reports to Dylan)
- **Team:** Dylan's org (not James's direct team)
- **Role:** TL-level peer. Being looped in to review high-level architecture on model-based and LLM-based pUIC. Scope extension, not ownership transfer.
- **Added 2026-06-24.**

### Zelun (ATG team)
- **Team:** ATG (not James's direct team)
- **Role:** Cross-team collaborator on model-based pUIC with Yidi.
- **Added 2026-06-24.**

---

## Recently joined

### Ryan Kam (L15, SWE) — joined
- **Start date:** ~April–May 2026 (notes said April 6; James's 7/15 roster says "joined 2 months ago")
- **Workstream (current, per 7/15 roster):** **CLR · LWS (dev-velocity focused)** — supersedes the earlier "GULP/CLR with Devin, spare bandwidth to UPP infra" and the v1 table's "ML Infrastructure ⟨reconfirm⟩", which is now resolved.
- **Context:** Provides the CLR coverage hedge behind Devin.

### Rui Wang (L14, SWE) — joined ~late June 2026
- **Workstream:** Reflex · L1
- **Context:** **This is the person prior notes called "Ray"** (dictation/preferred-name artifact, corrected 2026-07-15). One of the two engineers James hired this half ("Ryan and Rui" — the H1 self-review says "Ryan and Ray").
- **Role in the org design:** **L1 / Real-Time operational owner** under the Foundations & Efficiency charter JJ co-owns (v2 §Calls #4, fork F6 resolved). He is the **day-1 oncall owner for L1/Real-Time** in the no-pager-gap table — the load-bearing reason this name has to be right in the Dylan-facing doc.

---

## Incoming

### Daniel Dormer (Contractor)
> Added 2026-07-25. **Not to be confused with Daniel Liu** (incoming EM).
- **Role:** Contractor on James's team, ~1 year working with James. Strong.
- **Workstream:** Reflex · Pinvestigator · migration tasks the team doesn't want to do.
- **Note:** Candidate technical guide for Lionel's possible oncall-alert-AI-cleanup ramp project (see Lionel 7/25).

### Yiping Wang (IC13, MLE)
> Added 2026-08-11, from the Daniel 1:1 — headcount not previously accounted for anywhere in the repo.
- **Start date:** **Mon 8/24/2026** — **Daniel's first day OOO** (out 8/21–9/11)
- **Location:** Toronto (third new Toronto arrival in 6 weeks: Lionel 7/27 → Yiping 8/24 → Nima S. 9/7)
- **Team / workstream:** Daniel's team — **Recommended Boards (Collection P13N)**
- **⚠️ Onboarding collides with the PTO window:** her manager is dark for her entire first three weeks. Week-1–3 design must be closed by 8/20 and named in Daniel's coverage map: day-1 owner (Yongwoo is the Collection P13N coverage DRI — confirm he's also her onboarding owner), buddy, starter task, and whether James runs Lionel-style 30/60/90 skip check-ins. Her arrival belongs in Daniel's 8/19–20 team-meeting cascade alongside the coverage announcement.
- **Note:** Daniel's 8/11 1:1-doc sketch had "+1 (new hire)" penciled under Collection P13N — James read that as Esteban (IC13-3); an incoming Collection P13N new hire makes Yiping the other plausible referent. Not relitigated, just flagged.

### Lionel Bewa (L14, SWE)
- **Start date:** **7/27/2026** — the same day Alim starts
- **Location:** Toronto (remote from the pod)
- **Workstream:** RR pod plumbing / serving (Charlie backfill)
- **Context:** Goes to **Alim's day-1 pod**. Framed deliberately as a **founding member**, not the new guy on an old team. **Triple-fragility onboarding** (new hire + new manager + remote) → named buddy (Roderick, as the org settles), deliberate oncall ramp, James runs 30/60/90 skip check-ins. Note the buddy currently reports to **Daniel**, not Alim.
- **2026-07-25 — starting project DECIDED (start is 7/27):** **Light RR-serving starter task inside his own pod** — James asks **Chuxi on Monday** what to give him (and continues feeding scoped work to Alok). **Onboarding support = deliberately distributed across the pod (Yidi, Chuxi, Alok), not a single buddy** — whole-pod helping, to build bonds in the new pod. **Alim scopes what Lionel takes on in the space going forward** — the two of them ramp up together; hand Alim the prepared plan in the first sync, his to adjust. **Oncall-alert-AI cleanup with Daniel Dormer = locked as a later/second project** ("figure it out later, not a big deal"). No onboarding doc needed per James. (Supersedes the single-buddy-Roderick onboarding note above; the Roderick backend partnership post-reorg remains available as the space matures. An Andreanne option was raised and scratched same-session.) Complication for path 1: **Alok is high-maintenance right now** (see Alok 7/25 note) — James is "trying to keep it all together."

---

## Key Dynamics

### Chuxi-Devin-Yuke Triangle
- Project (retentive signal → CLR) stays anchored in Retentive Recs
- Chuxi is the bridge. Yuke and Devin don't need to collaborate directly
- Framing to Devin: This enhances CLR. Ryan and Yichi will work closely with him.
- Framing to Yuke: Extends his workstream's reach. Chuxi is still his IC. This is his win.

### Single Points of Failure
*(refreshed 2026-07-15 against the confirmed roster)*
- **Piyush on UPP** — Zihao (L15) is the hedge and is **not there yet**. ⚠️ The hedge is also Alim's only senior IC — see Zihao's entry.
- **Bella on RecGPT/ATG** — hedged through the YiPing pairing; Hanlin (L14) + Yuke (L15, PIP track) also in RecGPT.
- **Yuke on Retentive Recs** — largely resolved: Yuke moves to RecGPT only; Chuxi (L14) + Yidi (L13) carry pUIC, with Ling Lan (L14, **Daniel's report**) as the delivery partner.
- **Devin on CLR** — Ryan Kam (L15) + Yichi (L13) provide coverage.
- **JJ on Real-Time** — **no longer solo:** Rui Wang (L14, ex-"Ray") is the L1/Real-Time operational owner underneath him.

### Cross-Training Approach
Make every workstream have at least two people in every design discussion. Not as policy — as habit. Nobody feels threatened, nobody feels like a backup, distributed knowledge in six months.

---

# Scope & Canonical Record (absorbed from `organization.md`, 2026-08-01)

> Moved here in the 8/1 people-folder reorg; updated where the July reorg changed them. `organization.md` keeps the leadership chain + outside-team context and points here. The stale March-2026 flat "Team structure" snapshot (Bowen-departure era: 17 directs, Bella-TL-RecGPT, Yuke-TL-RR, Charlie/David) was superseded by the Roster + Org shape sections above — git history has it.

## Scope boundaries (updated 2026-08-01 for P13N Retrieval)

### In scope
- **Retrieval / Candidate Generation:** selecting candidate items given user/context and conditioning signals.
- **Personalization foundations in retrieval:** embeddings, feature retrieval, user interest signals, exploration/exploitation knobs (as they shape candidate sets).
- **Conditioning / query composition:** building candidate requests/constraints.
- **Preranking / fast shaping:** lightweight preranking (LWS), early controls, filtering, dedupe, diversification constraints.
- **Indexing + supply:** candidate coverage/diversity via indexing strategies and retrieval sources.
- **Serving efficiency:** latency, cost, caching, reliability improvements tied to retrieval/preranking (F&E charter: responsiveness, L1 Utility, cost).
- **NEW with the July reorg — anticipation modeling:** pUIC (model-based + LLM-based), Retentive Recs, and their serving path, end to end.
- **NEW — boards portfolio:** Intelligent Boards, Recommend-a-Board, Unity Board (inherited with Curation ML).
- **NEW — exploration:** Unified Explore Backend / Explore Page ML + plumbing.
- **AI-leveraged engineering:** Reflex vTeam + agentic dev-velocity systems (Pinvestigator, Pinkerton) as internal platform.
- **Generative retrieval:** RecGPT/GenRet — **a gains engine to scale (James, 8/2)**; the time-boxed-incubation framing is retired.

### Out of scope (but coordinate tightly)
- Final ranking model ownership and training pipelines — **P13N Ranking (Dhruvil)**, which also now owns **blending** (Rahul Goutam's team moved there in the same reorg).
- Surfaces / UX — **P13N-Experiences (Yan)**; Curation Revisitation stays in Yan's org.
- Core infra platform components without clear retrieval ownership (we influence; partner owns).
- Product UX decisions (we shape via constraints, proof plans, and measured outcomes).

### Shared-ownership zones (where confusion happens)
- **CG vs Ranking boundary:** we own *candidate recall/coverage + fast shaping*; Ranking owns *heavier scoring and ordering*.
- **UPP cross-surface seams:** SSJ/Search politics — Kurchi wrestling for ownership *under* UPP (co-option play live); seam-drawing playbook in `stakeholders.md` §6.
- **IB placement:** gains-origin gate (~60d) decides Daniel's team vs. Alim's team — deliberately unsettled until the read.
- **Cross-org seams with Tim's and Yan's orgs stay cross-org** — governed by explicit notice/notification norms (the Cupcake lesson), not dissolved by the merger.

## Canonical 2025 topline outcomes (numbers that should appear early)
Use these as canonical headline metrics (repeatable, exec-legible):

- **Product impact:** **+2.1% total SSv2**, **+0.33% WAU** (≈ **+1.1M WAU**)
- **Company impact:** **~$3M/year annual cost savings** in 2025
- **NUX / Growth:** critical unblock for NUX Revamp backend; achieved ambitious **1% NUX Growth** goal while enabling the experience
- **Notifications:** enabled/accelerated Notifications ML with **~6–7 MAU-improving launches** (via platformization + retrieval work)

## 2025 narrative arc (high-level story)
2025 was a **modernize → consolidate → scale** year:
- **Modernized** CG stack toward learned retrieval + unified components (CLR, multi-embedding, L1 utilities, GPU serving)
- **Consolidated** away legacy/heuristics with active deprecations (**topics**, **bestpins**, **pinacle2**)
- **Scaled** impact across Pinterest surfaces (Homefeed first; enabled Notifications and broader **Unified Personalization Platform (UPP)** direction)
- **Shifted** Retentive Recommendations from product vision → concrete signals + shipping roadmap

## 2025 highlights (canonical bullets to reuse)

### A) Team growth & org maturity
- **New hires + onboarding (2025):** Hanlin Lu, Zili Li, Chuxi Wang, Sophia Zhu, Yidi Wang, Charlie Tian (he/him), Yali Bian *(and other 2025 hires as applicable; keep list current)*
- **July reorg:** DRP + RCG structure established; Bowen stepped in as EM; TLs stepped up materially across design/execution/ownership

### B) Company contributions (impact summary)
- Delivered **+2.1% SSv2** and **+0.33% WAU (~+1.1M)** (topline result)
- Delivered **~$3M/year** annual cost savings (infra + serving + deprecations + migrations)
- Enabled Growth via **NUX Revamp backend**; hit **1% NUX Growth** goal while unblocking the experience
- Enabled Notifications ML velocity and MAU impact via platformization + retrieval experimentation (**6–7 launches**)

### C) Technological impact (2025 pillars)

#### Modernized CGs (Engagement / SSv2)
- **CLR (Conditional Learned Retrieval)** as backbone; upgraded legacy interest/board/pin CGs → better relevance, coverage, flexibility
- **Multi-Embedding Learned Retrieval (ME LR)** → richer user representation; better diverse/tail interests
- **Deprecation of legacy services:** **topics**, **bestpins**, **pinacle2** → reduces complexity and frees operational cycles

#### ML advancements (Engagement / Retention)
- **LLM-based interest generation (PinnerSpark)**
- **Retentive Recommendations:** grounded in measurable signals + launches; shifted from "vision" to "shipping plan"
- **Modeling upgrades:** larger ID embeddings; improved losses/activations; more advanced user sequence modeling

#### Funnel / infra efficiency
- **L1 utility layer** + funnel efficiency improvements (early controls, alignment with downstream ranking, cost/latency optimization)
- **PhP** and related funnel improvements (internal naming; keep consistent with internal context)
- **LWS GPU serving:** unblocked model scale with materially better cost/latency profile

#### Research + technical communication
- **Multi-Embedding KDD paper**
- Multiple blog posts
- ML Symposium + ML Day presentation(s) on LWS / CLR / PhP
- Improved clarity and trust in offline evaluation (faster + more reliable offline experiments)

#### Retentive Recs → concrete shipping plan (status)
- Took Retentive Recs from product vision → concrete signal + launches: **launched in ranking**, two additional launches in retrieval and blending
- Clear roadmap focused on driving retention (WAU/MAU)

#### Cross-surface experimentation
- Established and started **UPP Retrieval experiment on Notifications** (technical + company impact)

### D) Operational improvements (maturity & leverage)
- Deprecation program: topics / bestpins / pinacle2; plus active work on **ownership clarity** ("find the right owners for workflows")
- Process rigor and runbooks: HF oncall revamp; "Manas debugging runbooks" and structured debugging practice
- Wiki improvements: better documentation of funnel numbers + shared understanding of the stack

## Technical system overview (high-signal mental model)

### Candidate generation pipeline (conceptual)
1) **Candidate supply / sources** (multiple retrieval sources; learned + legacy until consolidated)
2) **Conditioning / query composition** (user state, intent, constraints)
3) **Retrieval / recall** (broad fetch under latency constraints)
4) **Fast shaping** (LWS / filtering / dedupe / early controls / diversification constraints)
5) **Contracts to downstream** (candidate set + features + provenance + constraints → Ranking / Blending)

### What we optimize (typical tradeoffs)
- Recall vs precision · Freshness vs relevance · Diversity/coverage vs short-term engagement · Latency/cost vs quality · Stability vs iteration speed (trust preservation)

## 2026 roadmap priorities (themes to preserve)
Keep the language close to original intent.

### Themes (core)
- **Further consolidate the stack** — Unified Personalization Platform direction; CLR to replace heuristic CGs
- **Achieve ambitious SSv2 goals** — Retrieval/LWS model scaling up; Generative Recommendations (**RecGPT / PinRec**)
- **Grow retention (WAU, MAU)** — Retentive Recommendations roadmap
- **Cost savings + user experience** — Business logics in L1 utilities; personalized budget tunings; responsiveness & feedback loops
- **Grow i18n ecosystems and content freshness** — merit-driven distribution; content exploration funnel

### Q2 2026 Focus *(dated March 2026 — kept for record; largely resolved: UPP P2P launch candidate live, JJ package submitted 7/10, Alim hired, Charlie exited, Zili pre-PIP)*
- **UPP cross-surface expansion:** at least one surface beyond Homefeed with working UPP integration and measurable results by end of June. Must-win presentation March 30.
- **Retentive Recs / p(UIC):** integrated into anticipation flow with measurable retention improvement. Andrew's CTO demo with real data.
- **RecGPT:** one production-quality generative retrieval result + ATG investment signal.
- **JJ promo to IC16** (target end of June) · **EM backfill** (experienced hire) · **Performance decisions:** Charlie, Hanlin, Sophia, Zili checkpoints mid-Q2.

### Start / Stop framing (2026)

#### Things to START
- **Reliability + debuggability as first-class investment** — agentic workflows for end-to-end tracing across the HF stack (faster root-cause, fewer regressions); reduce "whack-a-mole" debugging time
- **Explore Page** — dedicated Explore backend to reliably surface new ideas/use cases; drive more active days, WAU, retention
- **VLM & LLM integrations** — domain moving rapidly; invest to adopt advancements continuously

#### Things to STOP
- **Duplicative improvements across individual models** — consolidate user sequence modeling iterations
- **Heuristic-based CG iterations** — high maintenance / limited upside; prioritize scalable model-based approaches

## Year-in-Review writing reference (moved from organization.md)

### Unified document strategy (single doc serving 3 audiences)
- **Layer 1 — Exec skim summary** (top; ~1/3 page): +2.1% SSv2 · +0.33% WAU (~+1.1M) · ~$3M/yr savings · NUX unblock + 1% NUX Growth goal · Notifications 6–7 launches. Format: 3–5 bullets, crisp, no paragraphs.
- **Layer 2 — Peer/system-level narrative** (~1–1.5 pages): DRP vs RCG missions and ownership boundaries; platformization interfaces + where CG creates leverage for other teams; 2026 priorities and cross-org asks/enablement.
- **Layer 3 — Internal team narrative + details** (3–6 pages): people growth + reorg story; technical pillars + major launches + deprecations; operational maturation; 2026 vision and how engineers plug in.

### Voice / style requirements (for Year-in-Review outputs)
- Executive presence: crisp, direct, high-signal; minimal fluff. Prefer bullets and strong verbs; avoid generic praise. Concrete nouns: systems, launches, deprecations, savings, outcomes. If placeholders are needed, label them explicitly (topline 2025 metrics above are **not** placeholders).

### Known constraints & realities
- Tier1 must stay compact (Helix upload limits); keep raw detail outside Tier1 and link it.
- Leadership expectation: **accuracy and trust** in exec-facing responses are non-negotiable.
- Team maturity dictates bandwidth: independence → more outward/platform leverage; instability → more internal foundation work.

### Pointers to raw material (outside Tier1)
- **Pointer:** Unified "2025 Year in Review" doc (exec skim + deeper layers) — Pinterest Context/<outside Tier1 path> — canonical narrative + verified numbers + reusable bullets; extracted state encoded above.
- **Pointer:** 2026 planning slides / roadmap source deck — Pinterest Context/<outside Tier1 path> — preserves exact language of priorities + start/stop framing; extracted state encoded above.

## Open questions (2026-04 vintage, moved from organization.md — partly superseded)
- Where are the crispest ownership boundaries between CG / Ranking / Blending for upcoming launches (especially Retentive Recs + RecGPT)? *(partly answered by the reorg: blending → Dhruvil; front-door + notice norms installed)*
- What is the highest-leverage "agentic debugging/tracing" workflow to build first? *(now Reflex-charter territory — evals/quality lane)*
- Explore Page: single-threaded owner + success metrics? *(UEB consolidates under Alim at target; Roderick driving)*
- EM JD framing for Two-Track Org? *(superseded — Alim hired; three-team design replaced Two-Track)*
- How to sequence performance management for Charlie and Zili with Dylan's air cover? *(Charlie exited via CPP; Zili pre-PIP gate ~8/13)*
