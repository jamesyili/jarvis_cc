# Org Design Proposal — James's Expanded Org (DRAFT v1, 2026-07-08)

**Status: WORKING DRAFT — iterating with Leo. Not yet for Dylan.**
Deliverable: structure proposal Dylan asked for (7/7 1:1), ahead of mid-July downward comms. Announcement locks **outer lines only** (Daniel+team+scope → James; Alim starts 7/27 with a named pod); internal structure stays provisional through a 30–60 day observe window.

---

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

## Gaps register (close before Dylan proposal ships)

**Per-person gaps (levels/family/projects — James to fill):**
- **Piyush** L16 or L15? second project (any Reflex fraction)? — **Devin** confirm L15; CLR only or CLR+GULP? — **Yichi** level + family + full-time CLR? — **Ryan** level/family; actual CLR-vs-UPP split; lands with CLR pod? — **JJ** SWE or MLE? who inherits L1/RT maintenance when he goes Reflex-full? — **Ray** level/family; real Reflex role or L1 maintenance (F6)? — **Alok** level/family; DT/PhP disposition (F7)? — **Yali/Hedi** levels; anything besides LWS? — **Zili** level/family; perf-case state + timeline? — **Bella** confirm L16 Staff; RecGPT-vs-Reflex % split? — **Hanlin** level; ME GPU serving done or ongoing? — **Yidi** level; model-pUIC only? — **Zihao** level; OK to move exploration→Alim given his UPP succession-hedge role?
- **Daniel's side:** **Balaji** what does he actually do day-to-day (title says TL — of what, concretely)? — **Roderick** confirm L15; UEB only? — **Ling** confirm L14; LLM-pUIC full-time? — **Yang** return date + ramp? — **Kim** loan % to Dhruvil + wind-down terms (raise w/ Dylan — reorg gives cover)? — **Yongwoo** workstream entirely unknown — **Felix** workstream entirely unknown (both: ask Daniel, first post-announcement conversation).

**Structural unknowns:**
1. Whether R-a-B/Unity Board maintenance is chartered work or quiet deprecation (shapes Daniel's mission story + headcount need).
2. Alim pre-start call: reset the promise gap (Staff anchor story now runs through F2/Balaji or doesn't exist) without damage-control energy.
3. Daniel's own read: what does HE think his team's charter is / wants it to be? (Feeds F1/F2 and the motivation risk in his Profile Option A.)
