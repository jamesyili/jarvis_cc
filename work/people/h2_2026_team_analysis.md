# H2 2026 Deep Examination — Scope, Progress, Risks, Opportunities + 2025-YE Comparison

*Prepared 2026-08-01 (Saturday, pre-announcement) from a four-agent sweep: current roster/scope, project progress, risk inputs, and a 2025 year-end reconstruction. Private analysis — contains perf-case material; strip before any sharing. Sources cited inline; data-quality notes in the appendix.*

---

## TL;DR

The org enters H2 roughly **30% bigger than December 2025** (~20 → 26+2 reqs), with an EM layer that doubled (1 first-time EM → 2 experienced M16s), and a charter that widened from "HF Candidate Generation" to the full **retrieval + curation + anticipation stack**. The 2025 team delivered +2.1% SSv2 / +0.33% WAU / ~$3M savings with one fragile EM; the 2026 team carries a **4.5% SSv2 + $2M cost + retention** target across three legs — **two of which are unproven** (Alim's leg has no delivering engine day 1; Daniel's leg is inherited and half-unknown).

**The defining H2 risk is concentration:** the weeks of 8/3–8/17 stack the announcement, three perf deliveries, the Zili gate, the RR handoff, and the EM-sync kickoff — all bottlenecked on James. **The defining H2 opportunity is cashing the UPP win** — V0 beat OneTrans head-to-head (James, 8/1: SSv2 wins US + Canada, strong engagement wins globally) — into a launch, a narrative, and a settled seam; plus converting the real-but-partial span shed (RR now, CLR at Oct — NOT GenRet, which stays into ~2027) into Director-altitude hours.

---

## 1. Current scope snapshot (as of 8/1)

**Structure:** P13N Retrieval (announce 8/5) = Retrieval Foundations (James) · **Curation ML** (Daniel Liu, 7 ICs, intact) · **Retrieval Modeling** (Alim, pod of 4). *(T1 names per the 8/1 Work-Leo delta — Daniel's team was styled "Retrieval Modeling" and Alim's "Anticipation Modeling" in July docs and in this analysis's older phrasing; the delta also re-cut workstreams 10→9 and corrected staffing — see `reorg_july2026/work_leo_delta_2026-08-01.md`.)* 24 ICs + 2 EMs + intern + 2 open reqs (L15, L13, unallocated by design). End-state decisions ~early Oct at the three-EM sync (CLR, GenRet graduation, IB gate, UEB, Balaji, reqs, remaining lines).

**Topline carry:** SSv2 4.5% → Daniel 2.0 / James 1.5 / Alim 1.0 · Cost $2M → James 1.2 / Daniel 0.6 / Alim 0.2 · WAU/retention = Alim's primary. ⚠️ Leo-proposed split, not yet sanity-checked against H1 actuals, not yet to Dylan. Honest decomposition: today's SSv2 concentrates in **LWS + CLR**; **UPP is the swing factor**.

**Workstream state, one line each:** UPP — V0 online strong, no top-line SSv2 yet, launch push started 7/27, V1 not online, SSJ wrestle escalated to Jeff · CLR+GULP — stable engine (Devin) · LWS — reliable engine, oncall → Daniel day 1 · RR — deliberate launch lull; model-pUIC serving debt, LLM-pUIC underperforming; both experiments land in Alim's month one, zero net-new heads · Reflex — POCs named (James/Dafang/Tim), Dafang slower than hoped, James's role-sentence ask open with Dylan; Shifu integration lane opened · RecGPT/GenRet — time-boxed incubation, Simulate V0 mid-Aug (Bella), ATG reads it "P2," graduation criteria unwritten (owed before 8/17) · IB — flat ~6 months, notif-pairing upside, gains-origin gate ~60d · F&E — carries the $2M line (JJ back mid-Aug + Rui) · Cost investigation — >$1.8M/yr found under Dylan, staff update delivered 7/27 · NLFU — 0.5% WAU sprint, SSv2 trade-off authorized only through end-Sept · SM/SL — staffed (Yali + Raymond Hsu), success criteria with Dylan still owed · Content Quality — **owner unknown, no repo intel**.

---

## 2. Top H2 risks (ranked)

### R1 — The August compression (near-certain; cascading)
Weeks 8/3–8/17 stack: announcement + two team meetings · three perf deliveries week of 8/10 (Bella before her demo, Yuke separate day, Daniel's own H1 pending Yan input) · Zili gate ~8/13 hard against her 8/18–9/3 PTO · RR pen-transfer 8/10 · EM-sync kickoff 8/17 · JJ returns mid-Aug into three queued deliverables. Single bottleneck: James. One slip cascades — ER bundle late → delivery week slides into the PTO boundary → gate mis-sequenced.
**In motion:** ER bundle Monday 8/3; timeline doc; delivery-week sequencing locked.
**Gap:** no slack. Anything unplanned (a Yan exit, an announcement flare-up) has nowhere to land. Pre-decide what drops first (candidates: Cupcake lookback, skip-level starts, NLFU inventory).

### R2 — The three-case perf cluster (high likelihood of at least one hard turn)
Yuke: formal path, adversarial, counter-documenting, I-485 constraint, his 2025 **Exceeds** is the record's obstacle — Aug–Sept peer validation is load-bearing. Bella: fortified-not-adversarial, rating-and-doc path, top-lab flight trigger, rating-handoff hold (James delivers 2026). Zili: pre-PIP, gate ~8/13, possible PTO resignation. All three held by James through the reorg optics window; ER pre-review already overdue. Plus the known record defect: **Bella/Yuke oncall-goal collision must be differentiated before ER sees both docs**.
**In motion:** the whole delivery-week machine; case records built; tripwires filed.
**Gap:** emotional/calendar drain is unbudgeted — the 7/31 containerization decision (one weekly perf block after docs land) needs to actually happen or H2 strategy time evaporates.

### R3 — Anticipation-leg cold start (the reorg's structural bet)
Alim's leg has **no delivering engine day 1** (by design), no L15+, a two-level-gap ramping TL (Chuxi) who also carries the backchannel prior, a triple-fragility new hire (Lionel), and a month-one deliverable dependent on **Ling Lan — who reports to Daniel** (the named souring scenario). Both pUIC tracks are troubled (serving debt; LLM track underperforming). Overlay: the promise ledger (pod-of-4 vs. the closing promises) and the Tier-1 ramp watch (ER-consult decision pending; ~60-day settle read late Sept; day-90 recompute ~late Oct). If month one lands 0-for-2 on the only metric the leg owns, the reorg narrative and Alim's retention wobble together.
**In motion:** RR/UEB lean-in ask + PM-interface handoff (8/5–8/10); scope-coupling frame; Ling Lan lock = James→Daniel; walking tours; instrument panel.
**Gap:** the Ling Lan availability lock is still not confirmed done — it predates Alim's start as a named action. Close it in the Daniel 1:1.

### R4 — UPP: converting the win before the seam gets drawn elsewhere (materially reduced 8/1)
**UPDATE (James, 8/1): V0 beat OneTrans head-to-head — SSv2 wins in US + Canada, strong engagement wins globally — with known semantic-relevance regressions; Dylan + Matt Chun pushing the launch as the exemplar of the new decision process they're escalating for** ⟨experiment/surface details to file in the UPP record⟩. The evidence risk is gone; what remains is **conversion + exemplar risk**: shipping the trade-off with the acceptance documented at the deciding altitude and the regression disclosed first (see O1), while the Kurchi/SSJ wrestle (escalated to Jeff, "Intentful UPP" doc + committee proposal) tries to redraw ownership above James — during the exact weeks he's consumed by R1/R2. V1 still not online; HF/Notif adoption slow; Piyush still the SPOF with a not-there-yet hedge.
**In motion:** launch push live; Dylan-blessed P2P ads-collab proof point; Matt Chun pushing Core-VPs-decide.
**Gap:** the Dylan seam pre-frame (queued since 7/17) — now **armed with results** — should land this month; a shipped, attributed win is the strongest anti-committee move available.

### R5 — Daniel-side unknowns + the Yan context window
The biggest single SSv2 slice (2.0) rides on a team James has never operated: Yang Liu on parental leave (return/ramp open), Yongwoo + Felix workstreams unknown, Kim Toy loaned to Dhruvil (wind-down owed to Dylan), Balaji placement open, IB flat ~6 months with an Andrew cut-paperwork history. Daniel's own H1 depends on Yan, who may exit — that context evaporates on his last day. Develop-or-document runs concurrently and quietly.
**In motion:** Wed Yan 1:1 asks (review mechanics, inherited commitments, asks-with-dates); Daniel 1:1 questions; skip-levels from 8/10.
**Gap:** a simple workstream map for Yongwoo/Felix/Yang is the cheapest unknown-killer — ask Daniel for it Tuesday.

### R6 — Exec clocks: cost, GenAI, and the JJ dependency
The $2M savings line ($1.2M on James's own leg) + the ~$5M/$1.8M investigation + the 12-week Bill/Anoop GenAI perception sprint + NLFU's SSv2-trade-off authorization **expiring end-Sept** all run on exec time, not team time. Three of these route through **JJ, who returns mid-Aug** to: GenAI placement doctrine, L1 hosting surface, NLFU responsiveness — while his IC16 case sits at Jeff's round with Kurchi's calibration sniping on record. A promo miss in this AI market converts the cost-line owner into a flight risk.
**In motion:** investigation "going well," staff update delivered; doctrine assigned to JJ with James editing; SM/SL air cover pre-blessed.
**Gap:** JJ's first week back needs sequencing (doctrine vs. L1 vs. NLFU) before he's triple-booked by default; promo-decision contingency (retention gesture) worth pre-thinking.

### R7 — Attrition tail cluster (low individual probability, high compound cost)
Bella (top-lab trigger, 3-month notice promised) · JJ (promo-miss × market) · Devin (watch; CLR SPOF with cover) · Zili (PTO resignation possibility) · Yuke (stuck, but AC21 could self-resolve) · Yan (context, not headcount). Any two landing Sept–Oct hits capacity and the settle-point narrative simultaneously.
**Gap:** no single move — but the settle design (criteria-gated, evidence-based) is the shock absorber; keep it.

### R8 — Dormant commitments quietly aging (low, but cheap to fix; trimmed 8/1)
Cupcake lookback stalled before Tim/Yan commitments locked (and Yan may leave) · preranking paper's RecSys deadline unconfirmed · SM/SL success criteria never converted from air cover into agreed criteria. *(Removed 8/1: Pinkerton — stall is now a deliberate fold-into-Reflex; PINvestigator — in regular use, only the file is stale.)*

---

## 3. Top H2 opportunities (ranked)

### O1 — Ship the UPP trade-off safely (re-scoped 8/1: win is real, launch is an exemplar, regression is known)
**V0 beat OneTrans head-to-head: SSv2 wins in US + Canada, strong engagement wins globally — but NOT a slam dunk: semantic-relevance regressions exist.** Dylan + Matt ⟨= Matt Chun, confirm⟩ want to push the launch anyway **as the exemplar of the new decision-making process they're escalating for.** That's sponsorship + speed + showcase status for UPP — with exemplar coupling risk: if the regression sours publicly, the launch failure and the process failure amplify each other, and "UPP degrades relevance" is exactly the SSJ stick. The play: (1) trade-off acceptance written at the deciding altitude with monitoring + rollback criteria; (2) remediation trajectory attached to the launch (characterize → bound → announce the V1/fix path); (3) **disclose the regression first** — narrative = "beat OneTrans on SSv2 + engagement with a measured relevance trade-off we're managing"; (4) done right, exemplar coupling is risk-transfer in James's favor — the call belongs to the process, the clean execution belongs to his org. Seam pre-frame to Dylan goes out armed with the honest version. Full posture: UPP record 8/1 addendum.

### O2 — Convert the real-but-partial span shed into Director-altitude hours (honest version, corrected 8/1)
The clean "shed at settle" story oversold it — **GenRet is not going anywhere soon** (James, 8/1): graduation criteria ≈ Bella's H2 deliverables, which land post-rating → James carries RecGPT + both attached cases into ~Q1 2027, and the Oct settle item is really *criteria + destination*, not a move. The honest shed inventory: **RR now** (this week — PM interface via the 4-way handoff), **day-1 oncall/ops** (LWS + boards → Daniel), **CLR at Oct** (with Devin). That's still real weekly time — but the H2 attention win comes equally from the two management-cost reducers on what *can't* shed: the perf work containerized to one weekly block, and the RecGPT experiment ledger keeping the incubation inspectable without constant presence. **The discipline: refuse to backfill reclaimed RR/CLR hours with inherited operational work.** First move: write the GenRet graduation criteria before 8/17 anyway — they gate the *destination* decision and self-synchronize with the case timeline.

### O3 — Own the GenAI placement doctrine while the exec window is open
James created #genai-feed-wg, holds the platform-owner posture, and the 12-week Bill-sprint clock guarantees exec attention through October. The 1–2 page doctrine (JJ writes mid-Aug, James edits) is cheap and positions P13N Retrieval as *where GenAI signals get placed correctly* — with L1 Utility as the hosting surface. Prior results (flat v3, negative user-tower) mean a doctrine that says *no* correctly is genuinely valuable.

### O4 — Cash the cost investigation as exec currency
The >$1.8M find is already delivered at staff; the remaining artifact — a prioritized trim list feeding Jeff's EM discussion — is Jeff priority #3, Director-shaped work, and armor for the org in a cost year. Pairs with the $2M savings top-line the org already carries. Cheap to finish; high visibility per hour.

### O5 — The Reflex × Shifu × Simulate triangle (strengthened 8/1: Pinkerton folds in, PINvestigator proves the lane)
"Search is asking Shifu to integrate itself within Reflex" + Dinesh's Ads funding + UPP-funding consideration for Q4 + Bella's Simulate V0 demo (mid-Aug, Andrew-requested) + JJ's return to Build. Two 8/1 upgrades: **Pinkerton's stall becomes deliberate consolidation — fold it into Reflex** (one narrative, one funding story; its DSAT substance becomes Detect/Prove content instead of a separate thing to defend), and **PINvestigator is now in regular investigative use** — live proof for James's named Detect/evals lane ("already in weekly use" beats any roadmap slide). If the role-sentence from Dylan lands, H2 converts Reflex from James's discretionary bet into the org's platform story. Watch: don't amplify who-integrates-into-whom (Kurchi sensitivity).

### O6 — First scoreboard win for the Anticipation leg
Either pUIC track landing in August gives Alim's leg its first evidence, Chuxi's TL ramp its first proof, and the retention narrative its fuel — and it feeds directly into the Oct settle as the evidence the gates run on. Adjacent: the **NLFU sparse-user window (LLM-pUIC × PinnerSpark) expires end-Sept** — a visible cross-org contribution at near-zero marginal cost if the LLM track recovers.

**Quick hits:** KDD next cycle (draft done — pick the window and calendar it) · preranking paper to RecSys (confirm deadline) · Daniel LLM-backbone requirement inventory with Anna (retention + platform play in one artifact) · shape the two reqs at settle against demonstrated load · Chuxi TL formalization once RR evidence lands.

---

## 4. New team vs. 2025 year-end

| Dimension | Dec 2025 | Aug 2026 | Read |
|---|---|---|---|
| **Size** | ~20 (~17 ICs, 1 EM, intern) | 26 + 2 open reqs (24 ICs, 2 EMs, intern) | +~30%, and +50% vs. start of 2025 |
| **EM layer** | Bowen (M16, first-time, flight undisclosed) | Alim (M16, hired via 10-candidate loop) + Daniel (M16, inherited with team) | From one fragile EM to two experienced ones — but both are *new to James* (one ramping, one inherited) |
| **Charter** | HF Candidate Generation: retrieval core (CLR/LWS/L1/RT/RR-early/GenRet-early) | P13N Retrieval: + curation ML, + boards (IB/RecBoards), + UEB, + anticipation as a named leg | Charter roughly doubled in surface; boards/curation are net-new competencies |
| **Metric carry** | Delivered +2.1% SSv2, +0.33% WAU, ~$3M savings | Target 4.5% SSv2 + $2M cost + retention primary | Target ~2× the delivered 2025 SSv2, on +30% headcount — but split across two unproven legs |
| **Bets vs. engines** | Engines: LWS/CLR. Bets: RR (vision→plan), UPP (direction, one experiment) | Engines: LWS/CLR (+GenRet maturing). Bets: UPP-at-scale, pUIC×2, GenRet, Reflex, IB revival | Bet portfolio ~3× larger; UPP went from direction → CEO/CTO-visible substrate |
| **External brand** | KDD 2025 paper | Eng blog (program lead, Jeff amplifying), KDD 2026 draft, RecSys preranking, "persona-based recs" narrative | Publication track became a charter feature (and a Daniel-retention tool) |
| **Fragility profile** | Hidden: Bowen's flight, no succession, TL bench of "3 IC16s" thin under the hood | Explicit: 3 active perf cases, named SPOFs with hedges, promise ledger, gates and tripwires | 2026 carries **more** risk but **managed** risk — the apparatus (gates, criteria, case records) didn't exist in 2025 |
| **Churn absorbed** | 2025: +6 hires, clean growth | Since Jan: −Bowen, −Sophia, −David, −Charlie (managed out); +Ryan, +Rui, +Lionel, +Alim, +Daniel's 7 | The org grew *through* its heaviest churn period — the 2025 team never absorbed a shock like this |
| **James's altitude** | EM with one sub-EM; hands-on across everything; Exceeds + $1.2M refresh | Sr EM over a 3-team org; one of the two ML Sr EMs (with Dhruvil); Director substrate (M18 target mid–EOY 2027) | The role changed more than the org did: from running a team to designing an org — H2 is the first test of operating at that altitude |

**The honest one-paragraph version:** the 2025 year-end team was smaller, simpler, and quietly fragile — one first-time EM already interviewing, no succession plan, and its excellent results concentrated in engines James personally supervised. The 2026 team is bigger, structurally sounder on paper (two real EMs, explicit gates, portfolio law), and carries visibly more risk — three perf cases, a cold-start leg, a contested swing-factor project, and a target that doubles the delivered 2025 number. The difference that matters most isn't headcount: **2025's org couldn't have survived losing James's personal attention on any engine; the 2026 design is explicitly built so it can — but that design is unproven until the Oct settle holds.**

---

## Appendix — Data-quality notes

- **KDD:** the RR file's last entry (May) predates the decision — submission was **deliberately deferred to the next cycle** (James, 7/27); the 7/31 deadline was retired, not missed.
- 2025 numbers disagree between files: Notifications ML "5 launches / ~1.5M WAU" (self-review) vs. "6–7 MAU-improving launches" (canonical bullets). Unreconciled.
- No contemporaneous Dec-2025 record exists (repo history starts 2026-03-27); the comparison roster is back-inferred, medium confidence on IC names, high on structure/size.
- The 2.0/1.5/1.0 SSv2 and cost splits are **Leo-proposed and unratified** — sanity-check vs. H1 actuals before they reach Dylan.
- Stale project files: preranking paper (~Apr/May), learned dynamic triggering (3/31). **Corrected 8/1 (James):** Pinkerton (file 5/14) — stalled by choice, folding into Reflex; PINvestigator (file 4/11) — project is ACTIVE and in regular investigative use, only the file is stale. UPP file (7/27) predates the OneTrans head-to-head result — 8/1 entry appended.
- Content Quality workstream: no owner and no intel anywhere in the repo — flagged as a GDoc-row-at-risk.
