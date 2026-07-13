# Org Design Proposal — James's Expanded Org (DRAFT v1, 2026-07-08)

**Status: WORKING DRAFT — iterating with Leo. Not yet for Dylan.**
Deliverable: structure proposal Dylan asked for (7/7 1:1), ahead of mid-July downward comms. Announcement locks **outer lines only** (Daniel+team+scope → James; Alim starts 7/27 with a named pod); internal structure stays provisional through a 30–60 day observe window.

---

## Org name — **P13N Retrieval** (decided with Leo 2026-07-13; goes in the announcement locks)

Replaces "HF CG" / "P13N CG." Dylan still says "the CG team" — a component-era label, two years stale on scope. The announcement is the moment her vocabulary updates: she says the new name downward, repeatedly, and retires the old one herself. One definition line in the doc draws the Dhruvil seam: **retrieval = the full pre-ranking funnel — substrate → candidate generation → lightweight scoring — everything that decides what the ranker sees.**

- **Pairs with P13N-Experiences** (Yan): substrate ↔ consumption — the April 3 consensus embedded in the org chart.
- **Coverage:** CG, UPP, CLR, GenRet literal; pUIC = retrieval substrate (Pred UIC CLR is a CG); exploration backend = retrieval for Explore; boards models = board retrieval; LWS via the definition line. Reflex is a program — no org name covers tooling.
- **Seams untouched:** ranking (Dhruvil), IB consumption / surfaces (Yan), platform-for-all-of-Core (Francisco), anticipation charter (Andrew — multi-team).
- **Future-proof:** the flagship bet (Generative Retrieval) carries the org's name; survives the R-a-B/Unity KTLO-vs-deprecation call either way.
- **Rejected:** Core / Foundations (vague layer-claim — pokes Dhruvil, Francisco); Anticipation alone (over-claims Andrew's multi-team charter); **Anticipation Foundations — kept as the cross-org PROGRAM name**, not the org name (programs travel through the Yan seam and into Andrew's charter; stronger Director story than a box on the chart); Scoring / Serving (generic — every team scores and serves; no unique referent); Boards / IB (live consumption seam with Yan per April 3; R-a-B/Unity deprecation call pending inside the observe window; fails Dylan's anticipation-value filter — boards visibility lands in the routing table + announcement sentence instead); User Modeling (collides with the User Understanding team under Bo).

## Dylan-facing doc — skeleton (aligned with James 2026-07-10)

Nine parts. Decision-first throughout (no option menus except §7). Cold-reader-safe: no PIP language (Yuke = "role change, James retains through transition"), no Bella leave-trigger/retention specifics, no "Anna's veto" (say profile fit), no "develop-or-document" on Daniel, no "tight-leash" on Alok — write every named person's line as if they'll read it.

1. **The shape in one view** — three legs, one line each: mission + roster + count. Ten-second read.
2. **What the announcement locks vs. what stays provisional** — outer lines lock mid-July; internal placements provisional through the 30–60 day observe window. Makes her downward comms safe.
3. **The three legs** — one block each: mission, measured-on, day-1 roster, one risk + mitigation (Alim: promise gap via pre-start call; Daniel: phased scope + AI-leveraged-engineering charter hook; James-direct: per-person justification table + time story, GenRet time-boxed with sunset criteria).
4. **Operational ownership (oncall / maintenance / KTLO)** — table: rotation → day-1 owner → settle-state owner. Headline: no pager gap at any point. Resolves: JJ-goes-Reflex-full orphaning L1/RT (Ray = candidate answer to F6); LWS oncall moves with the pod day 1 + one explicit Zili sentence (rotation under Daniel, perf with James); Daniel's charter gains the concrete hook — first AI-leveraged oncall (Pinvestigator triage as default first responder, measured on time-to-diagnosis); Lionel oncall ramp deliberate (new + remote); R-a-B/Unity Board = KTLO-vs-deprecation call.
5. **Routing — who is responsible for what** (James add, 7/10) — front-door table for Dylan, Andrew, and PMs. Doubles as the XFN fast-path framework (Andrew's 7/9 feedback, structural response). First cut (Leo, 7/10):

   | Domain | Front door (EM) | Technical owner | Routing notes |
   |---|---|---|---|
   | Anticipation / Retentive Recs (pUIC, feedback loop) | **Alim** | Chuxi (ramping) | Anna + anticipation PMs route product asks to Alim day 1; James = escalation path through Alim's first ~30 days |
   | Exploration surfaces (UEB, Content Exploration/MDD) | **Alim** | Roderick | — |
   | Generative Retrieval / RecGPT | **James** (incubation) | Bella | Time-boxed; moves when structure revisits |
   | Reflex / AI tooling (Build agents, Pinvestigator, Pinkerton) | **James** | JJ (Build) · Dafang (overall TL, Dylan's line) | Andrew + Tim (PM) route here — the "where James's time goes" story made visible |
   | UPP retrieval | **James** (transitional) | Piyush | F3 endgame; cross-org channels (Sai, Jaewon) unchanged |
   | Scoring/serving platform (LWS day 1; CLR at settle; R-a-B/Unity Board maintenance) | **Daniel** | Devin (CLR) · LWS TL TBD | Infra partners + platform asks; oncall per §4 |
   | L1/Real-Time maintenance | **James** via Ray → Daniel at settle | Ray | JJ consults, doesn't carry the pager |
   | **PM front door (newer / non-recsys PMs — Michael's org)** | per-domain EM above | — | Replaces ad-hoc pings to individual engineers; pairs with the self-serve tooling framework being scoped |

   Watch-fors on this section: (a) PM front-door row framed as **service** ("named owner, faster answers"), never boundary-enforcement — it's the structural answer to Andrew's feedback, landing the week Michael onboards; (b) **Anna hears the RR→Alim handoff from James directly before reading it anywhere**, same beat as the Chuxi story; (c) one explicit line noting Andrew's three channels (Reflex via James+Tim, ISR via JJ, feedback tooling via framework) so it reads designed, not fragmented.
6. **Calls I've made** — F1 LWS-first, Lionel→Alim, F4 Alok, F6 Ray — stated as decisions, one-line rationale each.
7. **Where I want your input** — two max: F2 Balaji (touches the Alim promise), Kim loan wind-down (needs her cover with Dhruvil).
8. **Sequencing after the announcement** — who hears what in which order (Daniel first from James, Bella continuity, Chuxi grow-in-place story, Yuke as already-aligned role change) + 30/60/90 observe checkpoints.
9. **Appendix** — Master IC table (reference, not body).

## Design principles (Dylan-derived + James-set)

1. **James carries few direct ICs, each with explicit justification** and a story for how James spends his time (Dylan's direct feedback, 7/7).
2. **James's time goes to Reflex** — Dylan aligned. The direct pod exists to serve that.
3. **Alim focused on Retentive/Anticipation** — gives James back time; delivers the ~1-month RR push (both pUIC experiments).
4. **Don't overload Daniel at the start** — he and his team are onboarding a new org; scope arrives in phases.
5. **Anna's veto:** Daniel doesn't own RR/product-instinct space. Scoring/serving/platform scope fits his profile (technical, straightforward, delivers).
6. **Bella doesn't move** (manager continuity; conditional stayer). **Yuke stays under James through the PIP window** (RecGPT work; Bella technical-TL-of-record only).
7. **Zili's perf management stays with James** even when LWS moves (carry-over decision, reaffirmed — no new EM starts with an inherited perf case).
8. **Fairness to Daniel:** moves framed as scope-following-people (Ling→pUIC, Roderick+UEB→exploration); Daniel hears the why from James first, right after Dylan's announcement.
9. **Devin stays CLR lead** (NOT a broader platform-TL role for now); his L16 path runs through CLR+UPP.

## Master IC table (every IC — level · job family · main project(s))

Levels marked **?** are inferred from title or unconfirmed — see Gaps register below. Some ICs carry two projects (listed both).

### James's current directs (17 incl. Lionel)
| IC | Level | Family | Main project(s) | Draft destination |
|---|---|---|---|---|
| Piyush | **L16** | MLE | UPP (pure) — but **uber-TL (TL of TLs) over CLR + LWS too** | James direct → endgame fork F3 (⚠️ his TL scope spans the F1 move) |
| Devin | **L15** | MLE | CLR (lead) · GULP | CLR pod → Daniel (fork F1) |
| Yichi | **L13** | MLE | CLR | with CLR pod |
| Ryan | **L15** | SWE | ML Infrastructure | placement ⟨reconfirm — not CLR-specific⟩ |
| JJ | **L15** (L16 case parked) | MLE | Real-Time/L1 · **Reflex (Build lead)** | James direct (Reflex) |
| Ray | **L14** | SWE | L1 (+Reflex framing?) | James direct? — fork F6 |
| Alok | **L14** | MLE | Real-Time · Reflex ~50% (giving up PhP/DT) | UPP+Reflex (Leo rec) — fork F4 |
| Yali | **L15** | MLE | LWS | LWS pod → Daniel (fork F1) |
| Hedi | **L15** | MLE | LWS (+ paper work) | with LWS pod |
| Zili | **L14** | MLE | LWS (perf case — stays w/ James) | with LWS pod |
| Bella | **L16** Staff | MLE | **RecGPT/GenRet · Reflex** (~30–50% — pin the split) | James direct |
| Hanlin | ? | MLE? | RecGPT (+ ME GPU serving) | James direct — fork F5 |
| Yuke | L15 | MLE | RecGPT (single stream; PIP) | James direct through PIP window |
| Chuxi | L14 | MLE | pUIC model-based · pUIC LLM-based (TL ramp) | **Alim** |
| Yidi | ? | MLE? | pUIC model-based | **Alim** |
| Zihao | ? | MLE? | Content Exploration ~50% · UPP fractional (succession hedge) | **Alim** ⟨confirm⟩ |
| **Lionel** | **L14** | **SWE** | RR pod plumbing (Charlie backfill; **Toronto**; starts **7/27**) | **Alim** (profile below) |
| **REQ-1 (open)** | **L15** | MLE | — (new headcount, granted ~7/11) | unallocated — fork F8 |
| **REQ-2 (open)** | **L13** | MLE | — (new headcount, granted ~7/11) | unallocated — fork F8 |

### Daniel's team (7 + intern)
| IC | Level | Family | Main project(s) | Draft destination |
|---|---|---|---|---|
| Balaji | **L16** Staff | MLE | team TL; day-to-day work **unknown** | fork F2 (Daniel TL vs Alim Staff anchor) |
| Roderick | **L15** | SWE | UEB (driving well) | **Alim** (UEB goes with RR/exploration) |
| Ling Lan | **L14** | MLE | LLM-pUIC inference pipeline | **Alim** (already inside the work) |
| Yang Liu | **L15** | MLE | UIC (pre-parental-leave; Roderick took over) | **Alim** ⟨return date/ramp?⟩ |
| Kim Toy | **L15** | MLE | UPP foundational (loaned to Dhruvil) · CLR (pointed, not started) | **Daniel** (CLR bridge); wind down loan |
| Yongwoo Noh | **L15** | MLE | **UNKNOWN** | Daniel (default) |
| Felix Yang | **L14** | SWE | **UNKNOWN** | Daniel (default) |
| Rita Lyu | intern | — | — (~2 months left) | ignore for design |

## Profile: Lionel (new hire — L14 SWE, Toronto, starts 7/27)

Charlie's backfill, now **hired** (Toronto flag resolved — he's there, req landed). Starts the **same day as Alim**. No history; blank slate; the only dedicated SWE in the anticipation space.

- **Option A — Alim's pod, dedicated RR/exploration SWE (recommended).** pUIC serving plumbing + UEB backend work alongside Roderick. **Why it works:** the pod is MLE-heavy and its bottleneck all year has been *serving* (pUIC online serving is what stalled under Yuke) — an SWE is exactly the missing trade; Roderick is a natural senior-SWE mentor line; and starting the same day as Alim means the whole team forms at once — Lionel is a founding member, not "the new guy on someone's old team." **Risks:** triple-fragility onboarding (new hire + new EM + remote Toronto). Mitigations: named onboarding buddy (Roderick), James 30/60/90 skip check-ins, EST/PST overlap is manageable (3h) but meeting hygiene needs setting early.
- **Option B — Daniel's platform pod** (R-a-B/Unity Board services or LWS serving). **Why it could work:** genuinely SWE-shaped service work lives there; Felix as same-level peer; Daniel runs execution steadily. **Why it doesn't:** reneges the req's purpose (the RR push loses its only SWE in the exact month serving work must land); Daniel's team is itself mid-onboarding into a new org — the worst environment for a fresh remote hire; mentor line is weaker (Felix is L14 too).
- **Verdict: A, strongly.** B only becomes interesting if the RR serving work turns out thinner than expected.

## Profile: Daniel Liu (inherited EM — placement options)

Full background in `daniel_liu_team_2026-07.md` (ex-CG TL; Dylan's historical not-management-fit read; left/returned; technical, straightforward, delivers, diplomatic, thinks deeply; **wants AI work**; Anna's RR veto; encroachment confound on the lean-in question; develop-or-document is James's real second job here).

- **Option A — Scoring & Serving Platform EM, phased (recommended).** Day 1: his remainder (Kim, Yongwoo, Felix, ±Balaji) + inherited maintenance (R-a-B live models, Unity Board) + first platform pod per F1; settle state: CLR + LWS (+later UPP per F3). **Why it works:** matches everything verified about him (deep technical, delivers, no product-instinct dependency — Anna-veto-safe); Kim already bridges to CLR; Devin's L16 path (CLR+UPP) lives coherently in this org; it's an honest, measurable develop-or-document test with real scope. **The real risk: motivation.** A serving/scoring platform is the least AI-shiny charter in the org, handed to a man whose stated interest is AI and whose lean-in is already the open question — this could *manufacture* the disengagement we're testing for. **Mitigation that makes it work:** build "AI-leveraged engineering practices" into the charter itself — Daniel's org becomes **Reflex's first full-adoption customer** (Pinvestigator/Pinkerton in their oncall + migration workflows), i.e., he gets to *use and showcase* AI without owning the AI frontier. His diplomatic, systematic profile fits an early-adopter-evangelist role well.
- **Option B — AI-Leveraged Engineering arm (Reflex productization + his current IB/exploration remainder).** **Why it tempts:** maximal motivation alignment; Reflex gets execution capacity it has never had; his interest is genuine. **Why it fails now, on three separate grounds:** (1) it collides head-on with where James personally spends time — Dylan just ratified James-on-Reflex, and delegating the build to Daniel means James's justification for his own direct pod evaporates; (2) Reflex's scaffolding is external to this org (Dafang is overall Reflex TL from Dylan's Sr-Staff line; Andrew funding thread still open) — an EM charter built on unfunded, externally-TL'd scope is sand; (3) it hands the single most Director-critical narrative James owns to an unevaluated EM. **Verdict: A now — and fold B's energy into A** (Reflex-adoption showcase inside the platform charter). Revisit B genuinely if Daniel passes the observe window *and* Reflex funding lands — that could even be the growth story that motivates him through A.

## The three legs (draft shape)

### Alim — Anticipation & Exploration (~8)
Chuxi (TL ramp, unannounced) · Yidi · Ling · Roderick (UEB) · Yang · Zihao · **Lionel (L14 SWE, Toronto, starts 7/27)** · [+Balaji if F2-Alim].
**Mission:** anticipate what a Pinner wants next — pUIC substrate (model-based + LLM-based) + exploration surfaces (UEB, Content Exploration/MDD). **Measured on:** retention + fresh-content discovery.
**Why it works:** focused (Dylan's underutilization fix lands here), delivers the 1-month RR push, Chuxi gets support (Ling delivery + Roderick seniority), Alim gets a real mission on day one.
**Gap vs. what Alim was promised (~8–9, Staff anchor, 2 seniors):** count ≈ 7–8 ✓; seniors = Roderick + Yang ✓ (different names than promised); **Staff anchor = only via Balaji (F2)** — otherwise none. Handle in pre-start call, no damage-control energy.

### Daniel — Scoring & Serving Platform (phased; ~7 day-1 → ~10 settled)
**Day 1:** his remainder (Balaji [if F2-Daniel], Kim, Yongwoo, Felix) + inherited maintenance scope (Recommend-a-Board live models, Unity Board) + **first platform pod per fork F1** (LWS or CLR).
**Settled state (post-observe, if develop-test passing):** both CLR (Devin, Yichi, Ryan) + LWS (Yali, Hedi, Zili) → coherent scoring/serving platform charter; Kim already the CLR bridge. UPP possibly joins later (F3) making it retrieval+scoring platform; Devin's L16 path (CLR+UPP) lives here.
**Why phased:** James's own worry — too much scope at start + team onboarding; also keeps the develop-or-document evaluation honest before charter-core (CLR) transfers.

### James direct — Reflex + GenRet incubation (~6–7, each justified)
| Person | Justification to Dylan |
|---|---|
| JJ | Reflex core (RT/L1 background); IC16 evidence engine |
| Ray | Reflex framing (confirm) — else L1 maintenance, revisit |
| Alok | Reflex 50% + UPP 50% (F4); tight-leash profile needs James |
| Bella | Staff retention (manager continuity = her stay condition); GenRet + Reflex ~50% |
| Hanlin | GenRet delivery pair with Bella (or F5: move with GenRet later) |
| Yuke | PIP containment — time-boxed; James holds so no EM inherits it |
| Piyush | UPP spine — transitional; endgame F3 |
**Time story for Dylan:** majority on Reflex (charter-building — "AI-Leveraged Engineering"); GenRet = incubation + Staff retention + PIP, explicitly time-boxed with sunset criteria (post-PIP, post-Daniel-onboarding, structure revisits).

## Open forks (the actual decisions left)

- **F1 — Daniel's day-1 platform pod: LWS-first or CLR-first?** LWS-first: self-contained, lower blast radius, protects Devin transition, keeps CLR until Daniel proves out (but Zili complication + LWS has 2 seniors who barely know Daniel). CLR-first: Kim synergy is real, Devin+Yichi+Ryan is a real team… but hands charter-core to an unevaluated EM + Devin retention risk on day one. **Leo lean: LWS-first, CLR at the settle point.**
- **F2 — Balaji: Daniel's TL or Alim's Staff anchor?** Daniel-side: continuity, fair to Daniel, anchors the platform charter. Alim-side: fixes the Staff-anchor promise, gives Balaji a fresh natural-experiment (initiative test) under a new EM. **Leo lean: hold until the Daniel conversation + workstream map; decide in observe window.**
- **F3 — UPP endgame:** stays James-direct vs joins Daniel's platform (Devin L16 path hints this). Not a day-1 decision.
- **F4 — Alok:** UPP 50% + Reflex 50% (Leo rec) vs RR. RR is staffed without him.
- **F5 — Hanlin** if GenRet ever stops being James-direct: follows GenRet wherever it goes; parked.
- **F6 — Ray:** genuinely Reflex, or L1 maintenance that needs a longer-term home? Affects the "every direct justified" story.
- **F7 — DT/PhP disposition:** Alok gives it up — dies, or lands where?
- **F8 — allocation of 2 new reqs (granted ~7/11): 1× L15 MLE + 1× L13 MLE.** Options for the L15: (a) **Alim** — fixes the seniority/promise gap *without* spending the Balaji fork (F2 decouples: Balaji can stay Daniel's TL and Alim's senior story still improves); (b) **GenRet hedge** — RecGPT continuity insurance if the Yuke PIP resolves in an exit (pod would drop to Bella+Hanlin); (c) **Daniel platform** — but he's absorbing scope, not short on seniors. Options for the L13: pairs under a senior wherever growth capacity exists — Alim's pod (under Ling/Chuxi — cheap delivery leverage for the pUIC push) or CLR (peer for Yichi). **Leo lean: L15 → Alim (posting now, arrival naturally lands mid-observe-window), L13 → hold until the settle-state call, then place where the structure says.** Note for the Dylan doc: reqs strengthen the "scope first, people follow" frame — mention them as allocated-by-charter, not as spoils.

## Gaps register (close before Dylan proposal ships)

**Per-person gaps (levels/family/projects — James to fill):**
- **Piyush** L16 or L15? second project (any Reflex fraction)? — **Devin** confirm L15; CLR only or CLR+GULP? — **Yichi** level + family + full-time CLR? — **Ryan** level/family; actual CLR-vs-UPP split; lands with CLR pod? — **JJ** SWE or MLE? who inherits L1/RT maintenance when he goes Reflex-full? — **Ray** level/family; real Reflex role or L1 maintenance (F6)? — **Alok** level/family; DT/PhP disposition (F7)? — **Yali/Hedi** levels; anything besides LWS? — **Zili** level/family; perf-case state + timeline? — **Bella** confirm L16 Staff; RecGPT-vs-Reflex % split? — **Hanlin** level; ME GPU serving done or ongoing? — **Yidi** level; model-pUIC only? — **Zihao** level; OK to move exploration→Alim given his UPP succession-hedge role?
- **Daniel's side:** **Balaji** what does he actually do day-to-day (title says TL — of what, concretely)? — **Roderick** confirm L15; UEB only? — **Ling** confirm L14; LLM-pUIC full-time? — **Yang** return date + ramp? — **Kim** loan % to Dhruvil + wind-down terms (raise w/ Dylan — reorg gives cover)? — **Yongwoo** workstream entirely unknown — **Felix** workstream entirely unknown (both: ask Daniel, first post-announcement conversation).

**Structural unknowns:**
1. Whether R-a-B/Unity Board maintenance is chartered work or quiet deprecation (shapes Daniel's mission story + headcount need).
2. Alim pre-start call: reset the promise gap (Staff anchor story now runs through F2/Balaji or doesn't exist) without damage-control energy.
3. Daniel's own read: what does HE think his team's charter is / wants it to be? (Feeds F1/F2 and the motivation risk in his Profile Option A.)

---

# Dylan-facing drafts (2026-07-10) — three registers, same substance

> Draft A = James's voice. Draft B = seasoned engineering executive register. Draft C = calibrated to Dylan specifically (scope-over-resourcing, her 7/7 questions answered as headers, two binary asks). Pick one or blend; all three are cold-reader-safe (no PIP language, no retention specifics, no evaluation framing on Daniel). Shared open items regardless of version: Balaji (F2) and Kim's loan wind-down are the two input asks; Ray is written as L1/RT operational owner (resolves F6 — flag if you want him kept on Reflex framing instead).

---

## DRAFT A — James's voice

Dylan, here is the structure proposal you asked for on 7/7. The shape first, then the detail. Section 2 is what your announcement can safely lock; everything else I am holding provisional through a 30 to 60 day observe window and will revisit with you as the teams settle.

**1. The shape in one view**

One org: **P13N Retrieval** — the pre-ranking funnel end to end, from user signal to what the ranker sees. Ranking starts where we end; surfaces belong to Experiences. Three legs inside it:

- **Alim — Anticipation and Exploration (~8).** Chuxi, Yidi, Ling, Roderick, Yang, Zihao, Lionel (L14 SWE, Toronto, starts 7/27 with Alim). Mission: anticipate what a Pinner wants next. The pUIC substrate (model based and LLM based) plus the exploration surfaces (UEB, Content Exploration). Measured on retention and fresh content discovery.
- **Daniel — Scoring and Serving Platform (phased: ~7 day 1, ~10 at settle).** His current team, the inherited maintenance scope (Recommend a Board live models, Unity Board), and the LWS pod on day 1. CLR joins at the settle point. Measured on platform reliability, cost, and the velocity of every team that builds on top.
- **Me, direct — Reflex plus GenRet incubation (7, each justified in section 3).** The majority of my time goes to Reflex. GenRet is a time boxed incubation with explicit sunset criteria.

**2. What your announcement locks vs what stays provisional**

Locks: Daniel, his team, and his scope come to me; Alim starts 7/27 with the named pod above; the org operates as P13N Retrieval from the announcement. That is the whole announcement. Provisional through the observe window: internal pod placements, CLR transfer timing, Balaji's placement, and the UPP endgame. I would rather tell you exactly what is settled than announce detail we might move in 60 days.

**3. The three legs**

*Alim.* Focused on the thing we hired him for, and it delivers immediately: both pUIC experiments land inside his first month. Chuxi steps up with real support around her (Ling on delivery, Roderick's seniority). One risk: the pod differs from what Alim heard during closing, mainly on the Staff anchor. I will handle that directly in his pre start call, and the Staff anchor question is one of the two decisions I want your input on below.

*Daniel.* Day 1 scope is deliberately phased: his team is onboarding a whole new org, and I do not want to hand him charter core scope before his footing is set. The honest risk is motivation. Platform is the least AI shiny charter in the org and Daniel wants AI work. So the charter builds it in: his org becomes Reflex's first full adoption customer, running the first AI leveraged oncall at Pinterest, with Pinvestigator as the default first responder and time to diagnosis as the measure. He gets to use and showcase AI while the platform stays the backbone.

*My directs, each justified:*

| Person | Why they report to me |
|---|---|
| JJ | Reflex Build lead; my Reflex time and his overlap daily |
| Ray | L1/Real Time operational owner as JJ shifts to Reflex; sits where the architecture context sits |
| Alok | Reflex 50% plus UPP 50% |
| Bella | Staff lead for the GenRet incubation; continuity through the transition |
| Hanlin | GenRet delivery pair with Bella |
| Yuke | RecGPT single stream after the role change we discussed; I hold his management so no new EM starts with an open thread |
| Piyush | UPP spine; transitional pending the UPP endgame call |

My time story: majority on Reflex, which is where you have asked me to spend it. GenRet is incubation plus continuity, and it is time boxed: post Daniel onboarding and post transition, the structure revisits and it moves.

**4. Operational ownership**

No pager gap at any point in the transition:

| Rotation | Day 1 owner | Settle state |
|---|---|---|
| LWS | Daniel (oncall moves with the pod) | Daniel |
| CLR | Me | Daniel |
| L1/Real Time | Me (Ray primary; JJ consults, carries no pager) | Daniel |
| pUIC serving (new surface) | Alim (Lionel ramps deliberately, no day 1 pager) | Alim |
| R a B / Unity Board | Daniel (KTLO vs deprecation call inside the observe window) | Daniel |
| Reflex / Pinvestigator tooling | Me | Me |

One carry over: Zili's rotation moves with LWS, but I retain his performance management. No new EM inherits an open case.

**5. Routing: who is responsible for what**

| Domain | Front door | Technical owner |
|---|---|---|
| Anticipation / Retentive Recs | Alim | Chuxi |
| Exploration surfaces (UEB, Content Exploration) | Alim | Roderick |
| Generative Retrieval / RecGPT | Me (incubation) | Bella |
| Reflex and AI tooling (Build agents, Pinvestigator, Pinkerton) | Me | JJ (Build); Dafang overall TL |
| UPP retrieval | Me (transitional) | Piyush |
| Scoring/serving platform | Daniel | Devin (CLR) |
| L1/Real Time maintenance | Me, Daniel at settle | Ray |

For product partners this doubles as a front door map: every domain has a named owner, so PMs get answers faster than pinging individual engineers, and I will pair it with self serve tooling we are scoping. For Andrew's org specifically: Reflex routes through me and Tim, In Session Responsiveness through JJ, feedback tooling through the self serve framework. Three channels by design, not fragmentation. I plan to walk Michael through this map during his onboarding week.

**6. Calls I have made**

(1) LWS first for Daniel's platform pod; CLR at the settle point. Lower blast radius while his team lands, and it protects the Devin transition. (2) Lionel joins Alim's pod: the RR bottleneck all year has been serving, and he is the only dedicated SWE in that space; starting the same day as Alim makes him a founding member rather than the new guy on an old team. (3) Alok goes Reflex 50 plus UPP 50; RR is staffed without him. (4) Ray becomes the L1/Real Time operational owner as JJ moves to Reflex full time.

**7. Where I want your input**

(1) Balaji: Daniel's TL, or Alim's Staff anchor? It touches what Alim was promised, so your read matters. I lean toward deciding inside the observe window once I have had the first real conversation with Daniel about his team. (2) Kim's loan to Dhruvil: I want to wind it down as CLR spins up under Daniel. The reorg gives natural cover, and it would land best coming from you.

**8. Sequencing after your announcement**

Same day: I talk to Daniel first, framing every move as scope following people. Same week: Anna hears the RR front door change from me directly; Bella, Chuxi, and Yuke conversations in that order; then the team announcement. 7/27: Alim and Lionel start together. Checkpoints at 30, 60, 90 days on the observe window, and I will bring you a settle state recommendation no later than day 60.

**9. Appendix: full IC table** (attached)

---

## DRAFT B — seasoned engineering executive register

**Subject: Proposed operating model for the expanded organization**

**Recommendation.** Reorganize the expanded 24 engineer organization as **P13N Retrieval** — the pre-ranking funnel end to end — spanning three charters: Anticipation & Exploration (Alim Virani), Scoring & Serving Platform (Daniel Liu), and Reflex/GenRet incubation (direct), with a phased transfer of platform scope and a 30–60 day observation window before internal placements finalize. The announcement commits outer reporting lines only.

**Design principles.** Charter coherence over headcount; single threaded ownership for every workstream and every pager; phased scope transfer to protect two simultaneous onboardings (a new EM and an inherited team); my direct reports minimized and individually justified, with my time concentrated on Reflex.

**Structure.**

1. *Anticipation & Exploration — Alim Virani (~8).* Owns the pUIC substrate and exploration surfaces end to end. Success metrics: retention and fresh content discovery. Immediate deliverable: both pUIC experiments online within 30 days of start. Risk: expectation gap vs. hiring conversations on senior anchoring; addressed pre start, with one open decision (Balaji) flagged below.

2. *Scoring & Serving Platform — Daniel Liu (~7 → ~10).* Day 1: current team, inherited maintenance surface, LWS. Settle state: CLR consolidates, yielding a coherent platform charter measured on reliability, unit cost, and dependent team velocity. The charter includes an operational modernization mandate: first full adoption of agentic tooling in oncall (Pinvestigator as first responder; time to diagnosis as the metric). This is deliberate — it aligns the charter with Daniel's stated interest in AI while the platform remains the core.

3. *Direct — Reflex + GenRet incubation (7).* Reflex is where the organization has asked me to spend my time; the direct pod exists to serve it (Build lead, operational owner for the vacated L1/Real Time surface, fractional Reflex/UPP capacity). GenRet is an explicit incubation: Staff led, time boxed, with structural sunset criteria (post transition review no later than day 60).

**Operational continuity.** Every rotation has a named day 1 owner and a named settle state owner; no pager gaps. LWS oncall transfers with the pod on day 1. CLR and L1/Real Time transfer at settle. New pUIC serving surface staffed with a deliberate ramp for the incoming SWE. One management carry over is retained by me by design.

**Interface contract.** A routing table (appendix) gives Dylan, Andrew's organization, and product partners a named front door per domain. Product asks route to the owning EM rather than to individual engineers, paired with a self serve tooling framework in scoping. Andrew's organization retains three deliberate channels: Reflex (me + PM), In Session Responsiveness (JJ), feedback tooling (framework).

**Decisions requested.** (1) Balaji placement: platform TL vs. Anticipation Staff anchor — recommend deciding inside the observation window; input requested given hiring commitments. (2) Sponsor the wind down of the Kim loan as CLR spins up.

**Transition plan.** Announcement (outer lines) → Daniel conversation same day → partner and team conversations sequenced within the week → new starts 7/27 → 30/60/90 checkpoints → settle state recommendation by day 60.

---

## DRAFT C — calibrated to Dylan

**What next week's announcement can lock**

- Daniel, his team, and his scope report to me.
- Alim starts 7/27 owning Anticipation & Exploration, with a named pod.
- The org's name: **P13N Retrieval** (retires "HF CG"). Everything the ranker sees comes from here; pairs with P13N-Experiences.
- Nothing else. Internal placements stay provisional through a 30 to 60 day observe window. I would rather give you a smaller announcement that holds than a detailed one we walk back.

**Your three questions, answered**

*Who TLs each space?* Chuxi steps up on Anticipation (Ling and Roderick around her), Devin stays CLR lead on the platform side, Bella runs GenRet as Staff lead, JJ leads Reflex Build, Piyush holds the UPP spine. Every workstream has a named technical owner; the full routing table is below.

*Where does my time go?* Majority on Reflex, per our 7/7 conversation. My direct pod is seven people and exists to serve that: each row in the table below has a one line justification, and GenRet incubation is time boxed with sunset criteria so the pod shrinks as the structure settles.

*Who owns the pager?* Every rotation has a day 1 owner and a settle state owner; no gaps. LWS oncall moves with the pod to Daniel on day 1. CLR and L1/Real Time follow at settle. The one carry over: I keep Zili's performance management even as his rotation moves. No new EM inherits an open case.

**Why these three charters**

Each is coherent enough to scope and fund on its own terms, which is the frame you gave me: scope first, people follow.

- *Alim: Anticipation & Exploration.* Your underutilization fix lands here: Ling, Roderick, and Yang go where their work already is. It delivers fast — both pUIC experiments land in his first month — and it is the team most directly attached to the anticipation strategy and its retention metrics.
- *Daniel: Scoring & Serving Platform.* Phased on purpose: his team is absorbing a new org, and I am watching the load so we do not burn people during a transition. The charter has a modernization edge that fits him: first AI leveraged oncall at Pinterest, Pinvestigator as first responder, measured on time to diagnosis. Platform reliability and cost stay the backbone.
- *Me: Reflex + GenRet incubation.* Reflex is the compounding bet and where my hands on time goes. GenRet stays with me only while it incubates; it moves at the settle point.

**Routing (who is responsible for what)**

| Domain | Front door | Technical owner |
|---|---|---|
| Anticipation / Retentive Recs | Alim | Chuxi |
| Exploration (UEB, Content Exploration) | Alim | Roderick |
| GenRet / RecGPT | Me (incubation) | Bella |
| Reflex + AI tooling | Me | JJ (Build); Dafang overall |
| UPP retrieval | Me (transitional) | Piyush |
| Scoring/serving platform | Daniel | Devin |
| L1/Real Time maintenance | Me → Daniel at settle | Ray |

PMs get a named front door per domain instead of pinging engineers; I will walk Michael through this map his first week. Andrew keeps three deliberate channels: Reflex through me and Tim, In Session Responsiveness through JJ, feedback tooling through the self serve framework we are scoping.

**Two asks**

1. **Balaji** (Staff, Daniel's team): platform TL under Daniel, or Staff anchor under Alim? It touches the Alim hiring conversation, so I want your read. Default: decide inside the observe window after my first real conversation with Daniel.
2. **Kim's loan to Dhruvil:** as CLR spins up under Daniel I want the loan wound down. Cleanest if you set it up with Dhruvil; the reorg gives natural cover.

**Sequence**

Your announcement → Daniel from me the same day (scope following people) → Anna, Bella, Chuxi, Yuke conversations that week → team announcement → Alim and Lionel start 7/27 → 30/60/90 checkpoints, settle recommendation to you by day 60.
