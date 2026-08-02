# Work-Leo delta — 2026-08-01 (org-planner session; updated 8/02)

*Pasted by James 2026-08-01 (personal-Leo announcement-eve session). Decisions from the work-side org-planner that this repo didn't have. Source of truth: work-leo `tools/ORG_PLANNER.md` + `tools/org_planner.html`. Propagated into this repo same day: team names fixed in `team_members_scope.md`, `organization.md`, both EM archives, `p13n_retrieval_split.md`, `h2_2026_team_analysis.md`, `backlog.md`; UPP state appended to `upp/upp_retrieval_em.md`. Dated July reorg docs deliberately keep their original strings (point-in-time records).*

**The headline trap: "Retrieval Modeling" changed hands** — it meant Daniel's team pre-reorg, it now means ALIM's team. Any doc pairing it with Daniel is actively wrong, not stale.

---

## 1. Team names — T1 (announcement, Aug 2026)

| EM | Name | Was (July design) |
|---|---|---|
| James | Retrieval Foundations | unchanged |
| **Daniel Liu** | **Curation ML** | "Retrieval Modeling" |
| **Alim Virani** | **Retrieval Modeling** | "Anticipation Modeling" |

## 2. Two time points, tracked separately

T1 = August 2026 (post-reorg, names above). T2 = Oct 2026 (~2 months): **names/charters deliberately TBD** — don't invent them before the three-EM end-state design lands. Assignment can vary by era (Rui: Reflex-primary T1 → CLR+GULP-primary T2).

## 3. Org name

**P13N Retrieval** (Dylan 7/27) / Dhruvil = P13N Ranking. Retires "Personalization Retrieval" and "HF CG."

## 4. Workstreams: 10 → 9 (the only allowed values)

`UPP` · `CLR + GULP` · `LWS + L1 Utility` · `Retentive Recs Retrieval` · `Unified Explore Backend & LLM pUIC` · `Reflex` · `RecGPT` · `Intelligent Boards` · `Recommended Boards`

- **Retentive Recs split:** `Retentive Recs Retrieval` (retrieval + model-pUIC + feedback loop) vs. `Unified Explore Backend & LLM pUIC` (UEB explore surfaces + LLM-pUIC track).
- **Retired:** `Efficiency` (responsiveness + L1 fold into `LWS + L1 Utility`; cost line tracked outside workstreams) · `Retrieval Foundations` as a project (SMS/Manas — dissolved; collided with James's team name) · `Cost investigation` (removed as tracked effort).
- `LWS + L1 Utility` explicitly includes L1 Utility and in-session responsiveness. ~~"L1/Real-Time pager follows the charter to Daniel"~~ **EXCISED 8/1 by James: "AI garbage" — no such pager transfer exists.** The real oncall record stands unchanged: L1/Real-Time ops = Rui under F&E per the no-pager-gap design in `team_members_scope.md`.

## 5. Staffing (T1, corrected 8/02)

| Person | Now (T1) | T2 |
|---|---|---|
| Ryan Kam | **LWS + L1 Utility** primary · CLR + GULP secondary | — |
| Rui Wang | **Reflex** primary · LWS + L1 secondary | **→ CLR + GULP primary**, Reflex secondary |
| J.J. Hu | **Reflex** primary · LWS + L1 secondary | — |
| Piyush | **UPP full-time** (CLR/LWS "advisory" was a category error — they consume UPP as a framework; dependency ≠ allocation) | — |
| Roderick | **UEB & LLM pUIC** full-time | — |
| Lionel | **UEB & LLM pUIC** full-time | — |
| Ling Lan | **Intelligent Boards** primary · UEB & LLM pUIC secondary | — |
| Chuxi | **Retentive Recs Retrieval full-time** — runs both pUIC syncs as coordination, not staffing [corrected 8/02] | — |
| Yidi | **Retentive Recs Retrieval** full-time | — |
| Alok | **Retentive Recs Retrieval** primary · Reflex secondary | — |
| Zihao | **UPP full-time** — never on Retentive Recs [corrected 8/02] | — |
| Yuke | **RecGPT full-time** | — |

Confirmed 8/02: Ryan + Rui are the named SWE support for CLR/SGI starting H2.

## 6. Alok's reporting line — CLOSED (under Alim). Drop all "line unresolved" language.

## 7. Allocation labels replace percentages

**Full-time** (only workstream) · **Primary** (main, but split) · **Secondary**. Distribution: **17 full-time · 7 split · 2 open reqs**.

## 8. Allocation invariants (enforced)

1. One primary each · 2. ≤2 workstreams per person · 3. Full-time = no secondaries · 4. Primary can't also be secondary · 5. Everyone has a primary except the reqs · 6. Everyone is placed on a team · 7. **[8/02] Every SPOF hedge must be staffed on the workstream it hedges** — RR-Retrieval hedges = Yidi + Alok; UEB hedges = Lionel + Ling.
Cross-org asks are excluded — they ride on top (Devin, Yali: full-time + XFN ask = correct).

## 9. Cross-org asks: 4 → 3, all front-door James

NLFU (JJ responsiveness · Devin CLR modeling) · Content Quality (JJ) · SM/SL (Yali via LWS lane). Cost investigation removed. **Daniel Dormer (contractor) excluded from all rosters/counts.**

## 10. Content decisions (planner)

Perf + people-sensitive material is **absent** from the planner (not toggled — absent; a test enforces it). Settle/graduation language stripped from workstream copy. Boards descriptions blank, **pending Daniel**. Org politics retained (SSJ boundary, CTO intent attention, ATG "P2" read, IB gains-origin). Phrasing constraint: staffing facts entangled with perf facts get de-named ("lost a senior IC to another stream").

## 11. Workstream state (8/02, James's note batch)

- **UPP** — V0 **beating P2P production (OneTrans)** on engagement + SSv2 (UCAN), regressing some semantic relevance; pushing for launch. **Search is adopting V0** and flags **GPU serving may be hard to get** — delivery risk on another org's capacity. **Stays with James directly at T2** (heavy managing up/across, high risk, clear leadership ask).
- **CLR + GULP** — historically strong gains, **deliberately under-funded H1** (capacity → UPP + RR). Ryan + Rui in on SWE tasks **H2, likely starting SGI**.
- **LWS + L1 Utility** — on-return moves: Ryan pairs with Yali (infra) · JJ hands off L1 diversity improvements · Rui implements L1 work for the Content Quality ask. Active Content Success collaboration.
- **Retentive Recs Retrieval** — **James's largest time draw** after losing a senior IC to another stream.
- **UEB & LLM pUIC** — Lionel ramps in during T1 as Roderick's backend partner.
- **Reflex** — agent ownership: **JJ → Build · Bella → Simulate · Alok → Pinkerton** (AI DSAT diagnostics) · Rui starts when he's back **8/9** (vacation — James, 8/1).
- **RecGPT** — lots of open experiments = why the QC ledger exists.

## Still open (gaps, not decisions)

- **Cost line: resolved-in-part (James, 8/1)** — savings will likely come through the **SGI work with Ryan** (CLR+GULP lane, H2); **additional savings sources still to be found elsewhere**. No single-threaded cost-engineering owner, by design.
- LWS+L1 and CLR+GULP read as split projects day 1 (Ryan/Rui report James, charters sit with Daniel/Alim) — intentional, fires warnings.
- 2.0/1.5/1.0 SSv2 split still proposal-grade — sanity-check vs. H1 actuals before Dylan.
- Boards workstream map: Yongwoo/Felix/Yang placeholders pending first substantive Daniel conversation.
- **Balaji placement** + **Kim loan wind-down** = the two open Dylan asks.
- Content Quality scope thin beyond "JJ owns it" — no counterpart POC.
