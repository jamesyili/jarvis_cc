# Proposal: Two-Track Team Setup — Alim Onboarding

**Date:** 2026-06-17
**Last updated:** 2026-06-24
**Status:** Updated — material changes since 6/17. Yuke off Track A, Bella departing, Chuxi as incoming TL, LWS decision deferred. Dylan review required before finalizing.
**Author:** James (with Leo)

---

## Context

Alim joins as EM under James, supporting ~8 people to start. This setup is near-term (independent of reorg timing) and is designed so it does not have to be undone when the broader reorg lands. It splits the current org into two coherent tracks, each with its own identity and mission.

**Principle:** Map people to coherent scope. Alim takes the model-development cluster (anticipation, generative, exploration); James holds the retrieval platform, real-time serving, and the AI-leveraged engineering bet.

---

## Track A — Alim's team

### Identity: **Anticipation & Generative Recs**

### Mission
Anticipate what a Pinner wants next, and generate it. We build the user-state substrate (UIC / pUIC) and the generative and exploratory retrieval on top of it, turning early intent into the right candidate before the user has to ask. Measured on retention (WAU / MAU) and fresh-content discovery.

**We own:**
- Retentive Recs / Anticipation — UIC, pUIC
- RecGPT / PinRec — generative retrieval
- Content Exploration / MDD

### Roster

| Person | Role | Workstream | Status |
|---|---|---|---|
| Chuxi | **Incoming TL** | Retentive Recs / Anticipation / pUIC | Stepping up from IC — TL conversation pending Yuke's Monday 6/29 decision |
| Yidi | IC | Retentive Recs + Content Exploration | Active, carrying most of model-based pUIC implementation |
| Hanlin | IC | RecGPT | Active |
| Zihao | IC | Content Exploration / MDD (+ fractional UPP tie) | Active |
| Ryan | IC | UPP infra / CLR support (matrixed — see below) | Active |
| Bella | ~~TL~~ | RecGPT | **DEPARTING** — Meta offer in hand, ER process initiated to protect backfill req |
| Charlie backfill | open req | Anticipation or RecGPT (Alim's call) | Actively hiring; arriving shortly after Alim. ⚠️ Rajat has changed this req to Toronto — Dylan conversation needed |
| Bella backfill | open req | RecGPT | Protected via ER process; lands on Bella's resignation |

**Track A: 5 active + 2 incoming reqs = 7 working.** Alim was told 8-9 to start with 1 Staff (Bella) and 2 seniors (Ryan + Yuke). Both anchors are now off the roster. LWS scope (Yali + Hedi, both senior) is a possible addition — see decision below.

> **Note on Yuke:** Yuke was originally on Track A as TL. As of 6/24 he has admitted to actively interviewing, been told he's not doing IC15 work, and is presenting his own proposal at Monday's 6/29 1:1. He will almost certainly step to IC and remain on **James's side (Track B)** — not handed to Alim. This was the right call: Alim should not inherit a disengaged, actively-interviewing IC as his first management challenge.

---

## Track B — James's team

### Identity: **Retrieval Platform & AI-Leveraged Engineering**

### Mission
Be the retrieval backbone the whole Homefeed runs on, and the engineering force-multiplier the org runs on. We own the unified retrieval platform (UPP), learned retrieval (CLR), lightweight scoring, and real-time serving, plus the AI-leveraged tooling (Reflex / Pinkerton) that speeds every team's iteration. Measured on SSv2 and cost / latency efficiency.

**We own:**
- UPP Retrieval (cross-surface platform)
- HF CLR (learned retrieval backbone)
- LWS (lightweight scoring / fast shaping)
- Real-Time / L1 Utility / Responsiveness
- Dynamic Triggering
- Reflex / Pinkerton / Pinvestigator (AI-leveraged engineering)

### Roster

| Person | Role | Workstream |
|---|---|---|
| Piyush | TL | UPP Retrieval |
| Devin | TL | HF CLR |
| Yichi | IC | HF CLR |
| JJ | TL | Real-Time / L1 Utility / Responsiveness |
| Ray | IC | L1 Utility |
| Alok | IC | Dynamic Triggering + Reflex |
| Yali | IC | LWS |
| Hedi | IC | LWS |
| Zili | IC | LWS |

**Track B: 9 named** (→ 8 after Zili's exit).

---

## Key design decisions

1. **Yuke stays on James's side (Track B) as IC.** Not transferred to Alim. James handles the performance + transition situation directly. Green card dependency means no abrupt departure; James manages through the transition.

2. **Chuxi steps up to TL on Track A.** Already carrying the pUIC work in practice. TL conversation happens after Yuke's 6/29 1:1 formalizes his path. Chuxi doesn't know yet. Clean growth story and promo vehicle (IC17 path).

3. **LWS (Yali + Hedi) stays on Track B for now — with an option.** Alim came for Retentive Recs, not LWS. Starting him focused on what he's excited about is cleaner than hitting a headcount number with scope he didn't sign up for. However, offering LWS as a genuine choice to Alim in week one is the plan — if Dylan is okay with it. Both Yali and Hedi are senior, so LWS would close the seniority gap (Ryan + Yali + Hedi = 3 seniors vs. the 2 promised). The offer must be framed as a real choice, not a nudge.

4. **Bella backfill goes to Alim.** Her headcount req is protected via ER process (Dylan-directed). When she resigns, that head routes to Track A.

5. **Charlie backfill goes to Alim — but Toronto flag needs Dylan.** Rajat has changed this req to Toronto. James needs to address this with Dylan in first week back. If the Toronto constraint holds, it changes the hiring pool and possibly the timeline for Alim's team getting to 7+.

6. **Zili stays with James.** Performance documentation + relationship sit with James. Standard handoff — Alim inherits what the team has — but James keeps the formal management of this case. Zili may also be LWS if LWS transfers to Alim later.

7. **Ryan reports to Alim, works in James's workstreams (matrixed).** Ryan → UPP infra / CLR support under James's TLs for now; Alim owns the person. Re-point Ryan's work toward Track A's pillar over time.

8. **UPP succession hedge.** Zihao keeps a fractional UPP / Piyush pairing so moving him to Track A doesn't reset the retrieval-architecture knowledge transfer. Ryan deliberately pushed into UPP infra to thicken the hedge.

9. **Substrate seam stays with James.** UIC / pUIC (Track A) feeds CLR / UPP (Track B); Chuxi → Devin's retentive-signal bridge is now cross-EM. James arbitrates that interface explicitly, not delegated during Alim's ramp.

10. **Pre-start call with Alim: light touch.** No heavy briefing required. Walk him through the real team composition ("things have moved since we talked") and the backfill trajectory. He accepted the role for the work and for James — the conversation resets expectations without becoming damage control.

---

## Open before rollout

- **Monday 6/29 Yuke 1:1** — formalize IC decision. Then Chuxi TL conversation can happen. Do both before Alim starts.
- **Dylan conversation (week of 7/6)** — run full org structure by Dylan before finalizing. Key items: Yuke managed, Bella ER + backfill, Alim structure, LWS choice offer, Charlie backfill Toronto issue, JJ promo. James is asking Dylan for more time in her first week back.
- **Chuxi TL conversation** — happens after Yuke is settled, before Alim arrives mid-July. She needs to be in TL mode from Alim's day one.
- **Charlie backfill Toronto flag** — Rajat changed this req to Toronto. Needs resolution with Dylan. Affects Alim's team trajectory.
- **LWS decision** — pending Dylan approval. If yes, offer as genuine choice to Alim in week one.
- **Ryan: matrix vs. move** — confirm whether his UPP/CLR work stays in Track B (matrixed) or follows him into Track A.
- **Comms order** — sequencing of announcement to the team once Yuke path and Chuxi TL are settled.

---

## Headcount summary (as of 2026-06-24)

| | Active | Incoming reqs | Total at steady-state |
|---|---|---|---|
| Track A (Alim) | 5 (Chuxi, Yidi, Hanlin, Zihao, Ryan) | Charlie backfill ⚠️Toronto + Bella backfill | 7 (+ LWS option: +2 = 9) |
| Track B (James) | 9 (Piyush, Devin, Yichi, JJ, Ray, Alok, Yali, Hedi, Zili + Yuke as IC) | — | 9–10 |

**What Alim was told:** 8-9 people, 1 Staff (Bella), 2 seniors (Ryan + Yuke). **Reality:** 5 active, 2 seniors (Ryan only confirmed; Yali + Hedi available if LWS transfers). Gap is manageable via backfills + LWS choice, and Alim's primary excitement is the Retentive Recs work, not the headcount.

~16 named across both tracks — same lean org that drove **+2.1% SSv2 / +0.33% WAU (~1.1M) / ~$3M savings** in 2025 — now structured for two EMs and two clear missions.
