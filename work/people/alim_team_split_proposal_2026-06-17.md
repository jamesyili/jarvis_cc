# Proposal: Two-Track Team Setup — Alim Onboarding

**Date:** 2026-06-17
**Status:** Draft proposal — near-term setup, designed to survive into the eventual reorg.
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

| Person | Role | Workstream |
|---|---|---|
| Yuke | TL | Retentive Recs / Anticipation |
| Chuxi | IC | Retentive Recs / Anticipation |
| Yidi | IC | Retentive Recs + Content Exploration |
| Bella | TL | RecGPT |
| Hanlin | IC | RecGPT |
| Zihao | IC | Content Exploration / MDD (+ fractional UPP tie) |
| Ryan | IC | UPP infra / CLR support (matrixed — see below) |
| Charlie backfill | open req | Anticipation or RecGPT (Alim's call) |

**Track A: 7 named + 1 req (8 heads).** Anticipation growth reqs (already business-justified, +0.6–0.8% SSv2) land here as they fill.

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

1. **Zili stays with James to manage out.** A formal manage-out belongs with the manager who holds the documented pattern, not a brand-new EM in week one. James completes it; the head then frees up.

2. **Ryan reports to Alim, works in James's workstreams (matrixed).** Ryan → UPP infra / CLR support under James's TLs for now; Alim owns the person. Re-point Ryan's work toward Track A's pillar over time. *(Confirm: matrix vs. move the work.)*

3. **UPP succession hedge.** Zihao keeps a fractional UPP / Piyush pairing so moving him to Track A doesn't reset the retrieval-architecture knowledge transfer. Ryan deliberately pushed into UPP infra to thicken the hedge.

4. **Substrate seam stays with James.** UIC / pUIC (Track A) feeds CLR / UPP (Track B); Chuxi → Devin's retentive-signal bridge is now cross-EM. James arbitrates that interface explicitly, not delegated during Alim's ramp.

5. **Chuxi full on Retentive Recs.** Her Reflex allocation moves to Alok / JJ so she isn't split across two EMs during her promo run.

---

## Open before rollout

- **Yuke transition timing** — read the situation on return, set direction, *then* hand to Alim. Don't transfer an unresolved situation cold. A change of EM may itself be good for Yuke; it's also a test of how Alim handles a real management situation.
- **Ryan: matrix vs. move** — confirm whether his UPP/CLR work stays in Track B (matrixed) or follows him into Track A.
- **Comms order** — what Alim is told he's inheriting; sequencing of the announcement to the team.

---

## Headcount summary

| | Named | Reqs | Total |
|---|---|---|---|
| Track A (Alim) | 7 | 1 (Charlie backfill) + Anticipation growth | 8+ |
| Track B (James) | 9 | — | 9 (→8 post-Zili) |

~16 named, the same lean org that drove **+2.1% SSv2 / +0.33% WAU (~1.1M) / ~$3M savings** in 2025 — now structured for two EMs and two clear missions.
