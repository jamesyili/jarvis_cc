# Pre-June Readiness Plan

> James OOO all of June. Dylan OOO 6/1 → ~7/6. Rajat: TBC.
> **Hard sign-off cutoff: Fri 2026-05-30** (Dylan's last day).
> **Re-entry gap:** 7/1 → 7/6 — James back, Dylan still out, no sponsor buffer.
> Last updated: 2026-04-19.

---

## The forcing function

Karen's question landed: *"If you came back 2026-07-01 and exactly one thing had gone sideways, which would you most regret?"* → **EM hire not signed, team left afloat.** That anchors the plan. Everything else orbits it.

With both sponsor and EM out in June, the three load-bearing moves are:
1. **Sign the EM before 5/15 tripwire** so onboarding overlaps James's last two weeks.
2. **Stand up pod leads as the delegation spine** — survives EM uncertainty AND becomes the structure the new EM inherits.
3. **Lock everything requiring Dylan's stamp by 5/30** — no verbal agreements left dangling.

---

## Burn-down: Ship-by-5/30

| # | Item | Owner | Due | Status | Notes |
|---|------|-------|-----|--------|-------|
| 1 | EM backfill — signed offer | James + recruiter | 5/15 tripwire | Pipeline empty after 4/16 Weak Lean No | **#1 priority.** Push recruiter weekly. If no offer by 5/15, pod model IS the plan, not fallback. |
| 2 | JJ IC16 packet — submitted | JJ writes, James coaches | ~5/25 | Started 4/17 | **Coach, don't do.** 1:1 next week — tell JJ to own the writing. Dylan endorsement before 5/30. |
| 3 | Charlie CPP — launched, outcome complete, Charlie departs before 6/1 | James + ER POC | Start 4/30, resolve by ~5/28 | ER POC Thursday 4/23 | No HRBP coverage needed during James's OOO — Charlie is out before James leaves. Don't split W4+ across June. |
| 4 | KDD paper — 3 sole-author sections soft draft | James | 4/30 | In progress | 10 working days. Can't write in June. |
| 5 | Pretrain-finetune blog #1 draft | James | Target TBD (May) | Status unconfirmed since 4/17 | Status check this week. Pick a real date. |
| 6 | Pod lead memo + escalation path | James | Dylan sign-off 5/30 | Not started | See strawman below. Merges with "deputy memo" — one doc. |
| 7 | CG ↔ Dhruvil ↔ Yan ownership 1-pager | James | Dylan sign-off 5/30 | Position articulated in `dylan_1on1_log.md` | Turn into signed artifact. No verbal agreements. |
| 8 | H2 pre-seed memo to Dylan | James | Share by 5/20 | Not started | Frontier/Production split vision. Dylan carries narrative in James's absence. |
| 9 | Q2 self-review draft | James | Leave with Dylan by 5/30 | Not started | Dylan writes Q2 review while James is OOO — give her the source material. |

## Narrative-lock (must happen pre-June)

| # | Item | Owner | Due | Status | Notes |
|---|------|-------|-----|--------|-------|
| 10 | Rajat OH — PinSight + UPP + **mention June coverage** | James | 5/8 | Booked | Weave one line at end: "Dylan and I both out all of June — here's my coverage plan." Plants seed early. |
| 11 | Jeff OH — PINvestigator demo | James | Ask Dylan in next 1:1; target mid-May | Awaiting Dylan OK | Protocol: don't self-book. |
| 12 | Andrew 1:1 — operational month-out conversation | James | May window | Not scheduled | Natural repair channel for 4/16 frame-capture residue. Frame as coverage, not repair. |
| 13 | Team communication — June scope + PTO framing | James | ~5/25 | Not drafted | See "team framing" section below. |

## Hand-off (written briefs + warm intros)

| # | Item | Owner | Due | Status | Notes |
|---|------|-------|-----|--------|-------|
| 14 | Pinsight M1 — Chuxi driving during June | James | 5/30 | Active | Brief in pod memo. |
| 15 | Reflex co-dev continuity — Anna + Matt briefed | James + Andrew | 5/30 | Feedback Curator PR shipping 4/19 | Tell Andrew directly in 1:1 (item #12). |
| 16 | RLHF coalition continuity — Dhruvil + Rahul carry | James | 5/30 | 7-person team forming | Tell them explicitly pre-June so no vacuum. |
| 17 | **JJ calibration timing — confirm date this week** | James | This week | Not confirmed | If calibration falls in June, James + Dylan both out = no advocate. Rajat pre-brief in 5/8 OH becomes critical. Dylan written endorsement before 5/30 = packet must speak without live advocacy. |

## Deferred to July (explicitly parked)

- Viral remix Steps 6-11 — Daniel primary, James zero-pilot during June
- graphify Phase 2-4 — tool-builder trap; not load-bearing
- Blog posts: generative recsys, EM growth, self-improvement
- Recommendation system from scratch
- Retentive-recs / predicted serendipity blog (P0 deferred to post-re-entry)
- Better context structure audit

---

## Pod structure (comprehensive — all 17 reports mapped)

### Pod 1: UPP Retrieval — **Lead: Piyush** (3)

| Member | Role |
|--------|------|
| **Piyush** (IC16) | Pod lead / UPP Retrieval TL |
| Zihao | IC (UPP + Content Exploration ~50%) |
| Sophia | IC (UPP Search CLR) |

**Scope:** UPP Base Retrieval architecture, surface expansion (Search/P2P), cross-surface pretraining.
**June posture:** Piyush runs proof point on cadence; new surface scoping parks.
**Notes:** Piyush-as-pod-lead = TL→EM growth signal. De facto already holds the role.

### Pod 2: CLR — **Lead: Devin** (2)

| Member | Role |
|--------|------|
| **Devin** | Pod lead / CLR TL |
| Ryan | IC (onboarding from April) |

**Scope:** Conditional Learned Retrieval backbone (UPP's retrieval core).
**June posture:** Continue CLR improvements feeding UPP; no new architecture decisions.
**Notes:** CLR is the backbone of UPP — tight coordination with Pod 1 but distinct ownership. Ryan onboarding accelerates during May.

### Pod 3: Retentive Recs — **Lead: Yuke** (3)

| Member | Role |
|--------|------|
| **Yuke** | Pod lead / Retentive Recs TL |
| Chuxi | IC (80% Pinsight M1 / 20% Retentive Recs) |
| Yidi | IC (Retentive Recs + Content Exploration fractional) |

**Scope:** p(UIC) integration into anticipation flow, retention signal work, Andrew's CTO demo, Pinsight M1 via Chuxi.
**June posture:** Chuxi keeps Pinsight M1 stable; Yuke drives p(UIC) on cadence.
**Notes:** Separate from RecGPT by design — retention = production integration; generative = frontier bet.

### Pod 4: RecGPT — **Lead: Bella** (2)

| Member | Role |
|--------|------|
| **Bella** | Pod lead / RecGPT TL |
| Hanlin | IC (improving — stays on RecGPT) |

**Scope:** Generative retrieval, ATG alliance, one production-quality result.
**June posture:** Maintenance; no new ATG scoping until James + Dylan return.
**Notes:** Small by design but stable. Escalation during June: Bella → peer-EM coverage partner.

### Pod 5: LWS — **Lead: Yali** (3)

| Member | Role |
|--------|------|
| **Yali** | Pod lead / LWS owner |
| Hedi | IC (LWS) |
| Zili | IC (LWS — monitor, no active perf action) |

**Scope:** Lightweight Scoring, GPU serving continuity, steady gains.
**June posture:** Keep-the-lights-on; no new model scaling initiatives.
**Notes:** **Yali-as-pod-lead IS the recognition move** ("Yali feels recognized" goal from Q2 roadmap). Formalizing her TL role removes the "de facto owner" ambiguity.

### Pod 6: Funnel Efficiency / Real-Time — **Lead: JJ** (2 during June; 3 in May)

| Member | Role |
|--------|------|
| **JJ** | Pod lead / Funnel Efficiency + Real-Time TL (**IC16 promo cycle**) |
| Alok | IC (PhP / Dynamic Triggering ~50%, Pinsight adjunct) |
| ~~Charlie~~ | **Departing before 6/1 via CPP outcome** |

**Scope:** L1 Utility, Real-Time, PhP/DT, funnel efficiency, PINvestigator maintenance.
**June posture:** JJ keeps PINvestigator stable; Alok on PhP cruise. Pod at 2 heads during James's OOO.
**Notes:** Pod-lead role IS the IC16 promo case — broader project ownership evidence. Not an overload risk at this level; full-EM would be. Charlie's CPP completes pre-June under James's review; no HRBP coverage gap during James's OOO.

### Cross-cutting initiatives (not a pod — project allocation)

| Initiative | Driver | Pod home |
|-----------|--------|----------|
| Pinsight M1 | Chuxi (lead), Alok (adjunct) | Pod 3 (Chuxi) / Pod 6 (Alok) |
| PINvestigator | JJ | Pod 6 |
| Reflex co-dev | James primary → **Anna K + Matt C carry during June** | External |
| RLHF coalition | Dylan-side: Dhruvil + Rahul carry during June | External |

### Departing

- **David** — April 2026

**Roster during June:** 3 + 2 + 3 + 2 + 3 + 2 = 15 (David departed April, Charlie departs pre-June)
**Roster at pod announcement (5/1):** 16 including Charlie winding down

---

## Escalation path during June

```
Pod lead → designated peer EM → Rajat
```

**Peer EM coverage partner options** (secure by 5/30, reciprocal coverage):

| Option | Rationale | Risk |
|--------|-----------|------|
| **Francisco** | Peer under Dylan, good relationship, Mexico team = less direct overlap | Stretched on horizontal platform work |
| **Tim Leung** | Peer under Dylan, James mentors him | Frontend focus ≠ ML escalation |
| **Olafur** | IC Sr. Staff under Dylan | Not an EM, no people-manager authority |
| **Darren** | Cross-org, politically aligned, "good pals" | Cross-org chain adds friction |

**Recommendation:** Francisco primary (same reporting line as James, Dylan knows him as coverage), Darren secondary for cross-org adjacencies. **Not Yan** — active territorial friction on CG ownership = conflict of interest.

### Timing

| Milestone | Date |
|-----------|------|
| Pods announced internally | 5/1 |
| Run with James steering | 5/1 → 5/30 |
| Dylan sign-off on pod memo + escalation path | 5/30 |
| June coverage active | 6/1 → ~7/1 |
| James returns, re-entry with pod leads | week of 7/1 |
| Dylan returns | ~7/6 |
| New EM inherits pod structure (evolves in July+) | when signed |

---

## Team framing (what to say, concretely)

**NOT** *"Take it easier in June."* That creates drift and loses ground vs. Dhruvil's team.

**Say:**
1. *"Here are the 3 things that ship in June — [UPP proof point, M1 stability, oncall + Charlie PIP on backstop]. Named owner per each."*
2. *"No new scoping, no new pitches, no stakeholder-facing net-new work. Committed deliverables + keep-the-lights-on only."*
3. *"If you've been holding PTO, use this window. I'm out, Dylan's out, Rajat knows."*
4. *"[Deputy pod leads] have final say on scope during June. Escalate to [peer EM] → Rajat if blocked."*

Mirrors Dylan's pacing DM culture. Pace, not lower the bar.

---

## James's personal June protocol (Goal 0)

Negative goals, per Karen:
- **No Slack.** Full disconnect.
- **No Pinterest email.**
- **No viral-remix commits.** Daniel-primary → zero-pilot for the month (write into `viral_remix_plan.md`).
- **One phone-friendly reading track, singular:** Yegge "thin harness, fat skills" + chrysb LLM memory. Nothing else.
- **No blog drafting, no mock interviews, no "just one thing."**

**Re-entry protocol (week of 7/1):**
- Day 1: briefing with pod leads (90 min)
- Day 2-3: catch up async, no meetings
- No Dylan 1:1 until she's back ~7/6
- No new commitments first week back

---

## Q2 goals mapping (original March 2026 roadmap vs pre-June plan)

From `goals.md` Q2 Roadmap. Frame: *"The Q2 story is about what was built, not who left."*

| Q2 Goal | Current state | Risk | Key pre-June move |
|---------|---------------|------|-------------------|
| **UPP** — one surface beyond HF with measurable results | Piyush pod lead; proof point running; must-win landed 3/30 ✓ | 🟡 Watch | May 8 Rajat OH locks UPP framing before OOO |
| **RecGPT** — prod-quality result + ATG invest signal | Bella pod + Hanlin improving | 🔴 Risk — June maintenance pauses ATG touchpoints | Confirm current ATG signal; may trigger Q2 roadmap drop condition |
| **Retentive Recs / p(UIC)** — integrated into anticipation flow | Yuke pod lead; heuristic pUIC live, neutral overall, positive LFU | 🔴 Risk — James is Andrew's expert-in-loop | Close "pUIC + CG quota tuning clarity push" (P0 backlog) pre-June |
| **CLR** — contributes to UPP cross-surface | Devin pod formalized; Ryan onboarding | 🟢 Track | Accelerate Ryan ramp in May |
| **LWS** — steady gains + Yali feels recognized | Yali pod lead (recognition formalized) | 🟢 Track ✓ | Done on recognition |
| **JJ promoted to IC16 by end-June** | Pod lead + packet coaching | 🔴 Risk — **calibration may fall in June; both James AND Dylan out** | See burn-down #17 — confirm calibration date this week |
| **PINvestigator demoed to Jeff** | 5/5 next steps done ✓; Jeff OH pending Dylan OK | 🟡 Watch | Ask Dylan in next 1:1 |
| **Pinsight M1 shipped + M2 prototype** | M1 in prod ✓; M2 status ❓ | ❓ Confirm | M2 status check |
| **Darren eval DS contributing** | Status ❓ | ❓ Confirm | Status check |

### Monthly tripwires against today (2026-04-19)

- **April 1 (passed):** Presentation landed ✓, Piyush absorbed UPP ✓, Ryan started ✓, burnout watch ongoing.
- **May 1 (12 days):** EM offer signed = **AT RISK** (pipeline empty post-4/16); pod memo drafted; JJ packet drafted by JJ.
- **June 1:** UPP framing locked with Rajat ✓ (via 5/8); JJ packet submitted; Retentive Recs impact; **H2 design started** → pre-seed Dylan.

### Dylan asks status

| Ask | Status |
|-----|--------|
| EM backfill timeline + ownership | Pipeline empty — push recruiter hard |
| GULP protection | ❓ Confirm in next 1:1 |
| Air cover for performance decisions | Charlie CPP: ER POC Thursday 4/23 ✓ |
| VP sponsorship | Rajat OH 5/8 ✓; Jeff OH pending Dylan OK |

### Two-Track Org end state

- **EM hire is the gating move.** Pods bridge until EM lands.
- If no signed EM offer by 5/15, pods ARE the plan through James's OOO and into July handoff.
- When EM does land, they inherit 6 working pods — not a mandate to reshape immediately.

---

## Open inputs

- [ ] Exact dates for James's OOO (assumed 6/1 → 6/30)
- [ ] Rajat June availability — need to confirm in 5/8 OH
- [ ] ER POC Thursday 4/23 — coverage conversation outcome
- [ ] **JJ promo calibration cycle date — critical; if in June, both advocates are out**
- [ ] Pinsight M2 prototype status
- [ ] Darren eval DS contribution status
- [ ] RecGPT ATG investment signal (may trigger maintenance-mode drop)
- [ ] GULP protection status — ask Dylan
- [ ] Peer EM coverage partner selected (Francisco primary, Darren secondary recommendation)

---

## Maintenance

Update this file weekly. Move items from "Burn-down" → "Done" or slip dates explicitly. If anything slips past 5/30, re-label as "July" or "Dropped" — no dangling items.
