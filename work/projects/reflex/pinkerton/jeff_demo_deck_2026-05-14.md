# Pinkerton — Jeff demo deck (5–8 min)

**Presenters:** Dimitra Tsiaousi (Notifs) + Chuxi (HF) — co-led with James Li (HF)
**James's role:** Opening only (Slide 1). Hands off to Dimitra; takes Q&A if directed.
**Audience:** Jeff (VP)
**Format:** 7 slides, ~6 min talk + 2 min Q&A
**Ask:** 1 FTE to operationalize Pinkerton as a shared org tool
**Status:** v0 draft 2026-05-14

---

## Design notes (read first)

- **Altitude.** Jeff sees all surfaces; EMs see one. Lead with the *cross-surface fragmentation* problem — that's his altitude, not ours.
- **James opens, then hands off — by design.** Director-altitude move: convene, frame, let the team show up. Chuxi gets VP-altitude exposure on the HF demo; Dimitra carries the joint partnership frame. James is *visibly the convener*, not the presenter.
- **Beat 3 (Prove).** Both surfaces have already used Pinkerton on real DSAT cases (#notifications-feedback + Dylan's HF Irrelevant Pins). Lean on the evidence — this is not a pitch for something hypothetical.
- **Agentic framing earned, not asserted.** Show the deep-dive trace first; "agentic AI" is the natural shape, not a buzzword grab.
- **One ask, late.** 1 FTE goes on the last slide. Don't soften it; don't bury it; don't trade altitude for asking small.
- **Anticipation lineage subtle.** This is a *DSAT diagnostic*, not a Reflex pre-announce. The deeper vision shows up only if Jeff pulls.

---

## Slide 1 — Title (James opens)

**Pinkerton**
*Cross-surface DSAT diagnostic.*

Presented by **Dimitra Tsiaousi** (Notifications) and **Chuxi** (Homefeed).
Co-led with James Li.

> Speaker note (James, ~45 sec):
>
> "Dimitra and I have been hitting the same problem on opposite surfaces — when users tell us something's broken, we can't actually see what they saw, and we can't get to the engineering root cause without days of manual work. We built compatible v0s on Notifs and HF independently, joined them, and we're calling it Pinkerton. Dimitra is going to walk you through what it does on Notifs; Chuxi will show you the HF side on Dylan's irrelevant-pin case. We have one ask at the end."
>
> *Hand off to Dimitra. Do not narrate Slide 2.*

---

## Slide 2 — Motivation (Dimitra)

**Today, when a user is dissatisfied, we can't see why.**

- DSAT signals land in Slack, surveys, leadership escalations — but we have **no way to walk the experience** the way the user lived it.
- Fragmented across surfaces — Notifs, HF, Search, Board More Ideas — and the products don't talk to each other.
- Engineering deep-dive into *why* a bad experience happened (CG? ranking? copy? content?) requires bespoke pulls from each team. Days of work per case.
- The result: we react to DSAT, we don't diagnose it.

> Speaker note (Dimitra): open with a concrete notif-side DSAT case that took days to debug. One sentence on the HF parallel (Dylan's irrelevant pins) — Chuxi will show that one live. Frame the *cross-surface* angle: "this isn't a Notifs problem or an HF problem, it's a Pinterest problem."

---

## Slide 3 — Goal (Dimitra)

**Pinkerton: an agentic diagnostic that meets DSAT where it lives — across surfaces, end-to-end.**

What Pinkerton does:
1. **Walks the user experience** across surfaces (Notifs → HF → Search → BMI) as one trace, not four.
2. **Quantifies** personalization, content quality, relevance — and **copy**, not just content.
3. **Diagnoses down to engineering components** — funnel stage, candidate generator, ranking head, model version.
4. **Proactive, not reactive** — stratified sampling across user segments (resurrected, new, power) to find DSAT *before* it escalates.

Why agentic: each diagnosis is a multi-step investigation. Pinkerton generates hypotheses, pulls signals, validates, and reports — without a human writing the SQL.

> Speaker note (Dimitra): Don't dwell on "agentic" — the next two slides earn it. If Jeff asks "why agents?", the answer is *because the investigation is multi-step and each step's tools depend on the previous step's findings.* Then hand to your own demo.

---

## Slide 4 — Demo 1: Notifications (Dimitra)

**Live case: #notifications-feedback debug**

- Trigger: real DSAT report from #notifications-feedback channel.
- Pinkerton ingests the user + notification, walks the send-decision path.
- Output: ranked hypotheses for why the user disliked it — copy, timing, content, targeting.
- Already running. Already used by the Notifs team.

*(Dimitra drives the screen for ~90 seconds, then hands to Chuxi.)*

> Speaker note (Dimitra): Your surface is the *proof Pinkerton isn't just an HF play*. The cross-surface generality is what makes this Jeff-altitude. Close by handing the screen to Chuxi: "Same shape on Homefeed — Chuxi will show the HF case."

---

## Slide 5 — Demo 2: Homefeed (Chuxi)

**Live case: Dylan's HF Irrelevant Pins**

- Trigger: Dylan's escalated case of irrelevant pins for a real user.
- Pinkerton fetches the full HF request, walks all 14 funnel stages.
- Output: stage-by-stage diagnosis — where the irrelevant candidate entered, where it should have been filtered, which model assigned the high score.
- Sponsor traction: Rajat (VP) and Dylan already pulling on it for live debugging.

*(Chuxi drives the screen for ~90 seconds.)*

> Speaker note (Chuxi): Land "Rajat + Dylan are already using this" once, factually, then move on. Don't over-claim — Jeff knows what real usage looks like. Speak to the *14-stage funnel trace* as the technical depth signal — that's the part no dashboard does. Hand back to Dimitra for Slide 6.

---

## Slide 6 — Where this goes (Dimitra)

**From reactive debug → proactive cross-surface quality engine.**

A simple diagram (build before demo):

```
DSAT signal ──┐
              ├──► Pinkerton walks experience ──► Diagnose ──► Action
Stratified ───┤         (cross-surface)         (eng layer)    (PR / model / copy)
sampling ─────┘
```

What Pinkerton unlocks:
- **Quantify** quality per segment per surface — finally comparable across the org.
- **Target** specific audiences (resurrected, low-DAU, new users) for proactive quality work.
- **Close the loop** — from diagnosis to PR / model / copy change.

> Speaker note (Dimitra): Name the vision without over-selling. Jeff already moved on the AI direction on 5/7; don't re-pitch it. Pinkerton is the *operating system* of the AI direction, not the pitch for one.

---

## Slide 7 — Ask (Dimitra)

**One ask: 1 full-time engineer to operationalize Pinkerton.**

What that FTE unlocks:
- Cross-surface infra (shared trace schema, shared agent backbone)
- Stratified-sampling layer for proactive runs
- Action loop (PR proposals, model registry hooks, copy A/B)

Today Pinkerton exists because James, Dimitra, and Chuxi are running it on 20%-time on top of full jobs. To make it a real org tool, it needs an owner.

> Speaker note (Dimitra): Don't soften. State it, then stop talking. If Jeff asks "from where" — defer: "happy to work that with you, Dylan, and [Dimitra's manager]." James can field this Q from his seat if directed.

---

## Q&A prep

| Likely Q | Short answer |
|---|---|
| "Why agentic vs. a dashboard?" | Each DSAT case is a multi-step investigation — the next tool to pull depends on what the previous step found. Dashboards can't branch. |
| "How does this relate to Reflex / Andrew's work?" | Reflex generates hypotheses from aggregate signals; this tool diagnoses individual DSAT cases. Complementary — Andrew and I are aligned. |
| "How does this relate to Roberto's search tool?" | Roberto's tool is single-surface request debug. Ours is cross-surface DSAT diagnostic with proactive sampling. Different scope. |
| "Why you two?" | We hit the pain on opposite surfaces independently and built compatible v0s. Joining is cheaper than either team building it standalone. |
| "Who would the FTE report to?" | (Open — pre-align with Dylan / Dimitra's manager before demo.) |
| "Cost at scale?" | LLM cost is the constraint for proactive sampling. Stratified sampling is the lever — we run on representative slices, not full traffic. |

---

## Open before the demo

- **Diagram on Slide 6.** Build a clean version (current draft is ASCII).
- **Pre-align ask routing.** Dylan + Dimitra's manager should know the 1-FTE ask is coming before Jeff hears it.
- **Demo failure backup.** Pre-recorded screen capture of each surface in case live demo flakes.
- **Dry run.** End-to-end with Dimitra + Chuxi once; trim if over 6 min. James times the opening to ≤45 sec.
- **Q&A coverage plan.** Dimitra fields cross-surface / ask / partnership questions. Chuxi fields HF technical depth. James fields routing / sponsor / Reflex-relation questions only if directed.
