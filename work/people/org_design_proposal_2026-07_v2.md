# P13N Retrieval & Anticipation ML — Org Design

**For:** Dylan · **From:** James · **Date:** 2026-07-14
**Status: WORKING DRAFT (v2, new section framing). Audience = Dylan only — cold-reader-safe, but the Personnel section does not travel.** Supersedes v1 (`org_design_proposal_2026-07.md` — the 9-section skeleton + Drafts A/B/C), which was **deleted 2026-07-14**; v1's Master IC table is preserved in the Appendix at the bottom of this file. The Rollout Messaging & Meeting Plan section (also below) is **internal — James's rollout playbook, not part of the Dylan doc.**

**The org:** **P13N Retrieval & Anticipation ML** — the pre-ranking funnel end to end, from user signal to what the ranker sees, plus the anticipation modeling built on top of it (Retentive Recs, pUIC, boards/exploration ML). Ranking starts where we end; surfaces belong to P13N-Experiences. This name retires "HF CG." *(Renamed from "P13N Retrieval" 2026-07-17: retrieval modeling is only part of the org's work, and the narrower name invited retrieval-team-to-retrieval-team comparisons in calibration that Dylan had to correct verbally. Naming note: **Anticipation Foundations** remains the cross-org program name, co-owned with partner surfaces — this org name refers to the org's anticipation ML work, not the program.)* Three legs inside it — the *target* shape I'm proposing, phased into on my own clock (see Transition Phase):

- **Alim — Anticipation & Exploration (~8).** Anticipate what a Pinner wants next: the pUIC substrate (model-based + LLM-based) and the exploration surfaces (UEB, Content Exploration). Measured on retention and fresh-content discovery.
- **Daniel — Scoring & Boards Modeling (phased scope).** Frontier ML modeling that drives metric gains and publishes (KDD, RecSys): the boards surfaces he retains (Recommend-a-Board, Intelligent Boards) plus LWS, which he inherits. He sheds the retentive-recs part of his team to Alim. Measured on modeling metric gains across his surfaces, with publications as a secondary signal.
- **Me, direct — Reflex + the UPP framework, plus Foundations & Efficiency (JJ) and the GenRet incubation (~7, each justified).** Majority of my time on Reflex; UPP is the shared framework CLR and LWS build on (Piyush); Foundations & Efficiency (responsiveness, L1 utility, cost — ~half of JJ) stays here per Dylan's "don't divest small things"; GenRet is time-boxed with sunset criteria.

---

## Key Charter Synergies

**Why this merger is good for the business.** Cupcake was the proof of concept: HF CG, Tim's team, and P13N-Experiences shipped as one EPD group across shared surfaces at high clock speed — strong UX, strong backend wins, executive visibility. The lesson underneath the wins is the one that matters for this reorg: **almost all of the friction we hit was seam friction — the cost of ownership being built while we shipped, not the cost of the wrong people.** This merger removes several of those seams outright and lets us install the connective tissue deliberately instead of improvising it mid-quarter.

**The friction the current workstreams face (drawn from the Cupcake look-back).** Five patterns recurred, and every one of them is a seam problem:

- **Ownership was in motion and it was felt on the ground.** Work landed on teams by adjacency rather than by design, because the answer to "who owns this" was genuinely changing week to week. A predictable transition cost — but a cost we kept paying because the boundaries never resolved.
- **Cross-team asks had no default path.** Operational asks — holdout additions, experiment configs, data pulls, scoping, dashboards — went to whoever seemed most available, and the responses were improvised: sometimes helpful, sometimes a redirect, sometimes friction. A system gap, not a people gap.
- **Signal and cross-surface changes rippled further than expected.** Changes to signals, ranking inputs, or candidate generation that touch multiple surfaces caught downstream teams off guard, because the "who needs to know, how far ahead, who has veto vs. input" protocol didn't exist.
- **Interaction norms don't transfer across boundaries.** Slack vs. ticket, direct-ping vs. EM-routing, sync vs. async, how much notice before an experiment change — these are implicit within a team and invisible across teams. Both sides guessed, and guessing produced avoidable friction.
- **No single unified roadmap with clear prioritization across workstreams.** Capacity was fixed while the set of ideas and process overhead kept growing, so ICs and leads absorbed prioritization decisions locally — churn and diluted focus.

**How the reorg solves the biggest of these and accelerates outcomes.** The merger converts cross-org negotiation into intra-org design:

- It **consolidates end-to-end backend/ML ownership of anticipation into a single cohesive team**, and empowers strong technical leads to grow under one mandate — the boundary that improvised in Cupcake becomes an internal design decision I control.
- It gives us **one roadmap and one prioritization surface** across anticipation, exploration, boards, and platform, instead of several teams each locally triaging.
- It lets us **install the routing / notification / notice norms as org policy** (see Ownership below) rather than rediscovering them each quarter — the structural answer to the exact friction Cupcake exposed, and to Andrew's XFN-partnership feedback.
- It keeps a **small, nimble Reflex vTeam** dedicated to accelerating recsys improvements across every leg, which grows SWE/MLE range naturally.
- It **minimizes disruption to the CG model team** so metric wins keep landing, and it **strengthens the peer seams** — a cleaner contract with Dhruvil (ranking) and Yan (surfaces / consumption) because our side of the seam finally has one owner.

*Honest boundary: the reorg doesn't dissolve the Tim / Yan cross-org seams that Cupcake also surfaced — those stay cross-org and get the notice/notification norms below. What it dissolves is the intra-anticipation seams, which were the more expensive ones.*

---

## Consolidation of Key Technological Investments

The reorg is also a chance to stop building the same thing three times. Across P13N today, anticipation, retentive recs, and intelligent boards are advancing on parallel — often near-duplicate — foundations. One org lets us converge the investment:

- **A single personalization backbone.** Anticipation (pUIC), Retentive Recs, and Intelligent Boards increasingly depend on the same user-representation and retrieval substrate — anchored by **UPP, which becomes the shared framework that both CLR and LWS build on.** Owning UPP centrally (with me, Piyush anchoring) while the modeling charters consume it lets us build the substrate once instead of maintaining variants that drift apart.
- **Shared LLM needs.** LLM-based pUIC, RecGPT / Generative Retrieval, and board recs all lean on the same LLM inference and serving needs. Consolidated, they share one investment in LLM serving infrastructure and one set of hard-won lessons, rather than each team standing its own up.
- **Reflex + AI tooling as a shared accelerator.** A single nimble vTeam productizes AI-leveraged engineering (Pinvestigator, Pinkerton) as internal platform that every leg adopts — the highest-leverage way to spend the discretionary craft time, and the charter Dylan asked me to concentrate on.
- **Modeling synergy between board recs and retrieval modeling.** Board retrieval and core retrieval modeling are close cousins; under one org their modeling investment can be shared rather than duplicated. Concretely, Daniel's leg co-locates board-recs modeling with LWS scoring modeling, so the synergy lives inside one charter instead of across a team seam.

The through-line: **one personalization substrate, one LLM-serving investment, one AI-tooling accelerator, shared modeling** — the technical case for the merger, and the Director-track story for what this org becomes.

---

## Additional Design Considerations

Beyond the transition phase, the design converges to **a minimal set of direct reports for me, each individually justified** — the shape you and I discussed on 7/7.

- The two **standing modeling charters run under Alim and Daniel.** They carry the durable business.
- **My time goes to Reflex**, per your feedback; my direct pod exists to serve that, and every seat in it has a one-line justification (see Ownership → the direct pod).
- **I keep the UPP framework** (Piyush) as a standing direct — it's the shared retrieval substrate CLR and LWS build on, and the right thing for me to anchor rather than push into a consumer charter.
- **GenRet is an explicit, time-boxed incubation** under me, with sunset criteria — it moves at the settle point (and CLR moves to Alim then too), and the direct footprint shrinks as it does.

So the beyond-transition footprint is two EMs on the standing modeling charters, and a deliberate James-direct footprint = the Reflex frontier + the UPP framework + Foundations & Efficiency (JJ/Rui) — not a wide span I hold indefinitely.

---

## Key Personnel Considerations

### Alim Virani (he/him) — incoming EM, Anticipation & Exploration
Alim is motivated by growth into senior leadership and by running a team that visibly delivers; his stated management instinct — *make myself useless as fast as possible* — fits a strong-delegation, strong-TL model well, and his interview structure on people-leadership (perf handling, promo cases, day-90 outcomes) was the cleanest of the loop. The one thing I'm watching is that he frames ambition self-first; I'll coach that toward org-needs-first, which is the register this culture rewards.

How I'll set him up to drive: a **focused, deliverable-rich charter on day one** — both pUIC experiments land inside his first month — with named senior support around Chuxi's ramp (Roderick's seniority, Ling's delivery). One honest gap: the pod differs modestly from what he heard while closing, mainly on senior anchoring. I'll reset that directly in his pre-start call with no damage-control energy, and Balaji's placement (one of my two input asks below) bears on it.

### Daniel Liu — inherited EM, Scoring & Boards Modeling
Daniel is technical, straightforward, diplomatic, delivers, and thinks deeply, and he genuinely wants his team on AI/ML modeling work — which is exactly what his charter is. His area is **frontier ML modeling** that both drives metric gains and publishes (KDD, RecSys): the boards surfaces he retains (Recommend-a-Board, Intelligent Boards) plus **LWS**, which he inherits. He sheds the retentive-recs part of his current team to Alim, so his team consolidates around one coherent modeling charter instead of being split across anticipation and boards.

Because he's onboarding a whole new org, I'm **phasing the scope** — he keeps his boards modeling and picks up LWS on day one, with any further consolidation settled in the observe window — rather than reshuffling everything while his team is landing. His motivation is fed by the charter itself: it's the frontier modeling work he's asked for, with a real metric and publication surface. First real conversation right after your announcement, every move framed as scope following people.

### Piyush Maheshwari — retrieval framework anchor (TL)
Piyush is motivated by senior-TL scope, and the retrieval architecture is his proving ground. He holds the full retrieval-architecture context post-Bowen and is effectively the TL-of-TLs across CLR, LWS, and UPP today. Rather than let the reorg fragment that (LWS going to Daniel, CLR toward Alim over time), I'm resolving it by role: **UPP stays with me as the org's shared retrieval framework, and Piyush anchors it** — the substrate that both CLR and LWS build on. He isn't split across EMs; he owns the foundation the modeling charters consume, which is a stronger and more durable senior-TL story than uber-TL-by-adjacency. He's the single point of failure on UPP today.

How I'll set him up to drive: keep UPP as the framework spine under me, grow his cross-cutting architecture role (the thing that builds his senior-TL case), and hedge the UPP SPOF via Zihao's ramp.

---

## Proposal

### Ownership

The design assigns accountability cleanly along four axes:

1. **Metrics.** Each leg owns named business metrics with a single-threaded owner: Alim on retention + fresh-content discovery; Daniel on modeling metric gains across his surfaces (boards + LWS scoring); my direct pod on Reflex adoption and the GenRet incubation milestones. No metric with two owners.
2. **0-to-1 initiatives.** The frontier bets — Reflex, Generative Retrieval, LLM-based pUIC — each get a named incubation owner and explicit graduation/sunset criteria, so they don't drift into orphan science projects. GenRet in particular is time-boxed with a settle-point review.
3. **Prioritized support for other Pinterest workstreams.** A routing / front-door model gives Dylan, Andrew's org, and PMs a named owner per domain, so cross-team asks land with context instead of being improvised — the structural fix for the Cupcake routing gap and Andrew's XFN feedback. For Andrew specifically: three deliberate channels — Reflex via me + Tim (PM), In-Session Responsiveness via JJ, feedback tooling via the self-serve framework we're scoping. I'll walk Michael through the map his first week.

   | Domain | Front door (EM) | Technical owner |
   |---|---|---|
   | Anticipation / Retentive Recs | Alim | Chuxi (ramping) |
   | Exploration (UEB, Content Exploration) | Alim | Roderick |
   | Generative Retrieval / RecGPT | Me (incubation) | Bella |
   | Reflex + AI tooling | Me | JJ (Build); Dafang overall |
   | UPP framework (supports CLR + LWS) | Me | Piyush |
   | Boards + LWS scoring modeling | Daniel | boards + LWS TLs |
   | CLR retrieval modeling | Me day-1 → Alim at settle | Devin |
   | Foundations & Efficiency (responsiveness, L1 utility, cost) | Me | JJ · Rui |

4. **Oncall.** Every rotation has a day-1 owner and a settle-state owner — **no pager gap at any point.** LWS oncall moves to Daniel on day 1; boards oncall stays with Daniel (his retained scope); L1/Real-Time oncall to Rui (under the Foundations & Efficiency charter JJ co-owns); the new pUIC serving surface staffs with a deliberate ramp for the incoming SWE. One carry-over by design: I keep Zili's performance management even as his rotation moves — no new EM inherits an open case.

**The direct pod, each seat justified** (the "where does my time go" answer):

| Person | Why they report to me |
|---|---|
| JJ | Reflex Build lead (~half) + Foundations & Efficiency (~half): responsiveness, L1 utility, cost savings |
| Rui | L1 / Real-Time operational owner, under the Foundations & Efficiency charter JJ co-owns |
| Alok | Reflex + Retentive Recs (primary) — ⚠️ seat justification open: RR is Alim's charter |
| Bella | Staff lead for the GenRet incubation; continuity through the transition |
| Hanlin | GenRet delivery pair with Bella |
| Yuke | Single RecGPT stream; I hold his management so no new EM starts with an open thread |
| Piyush | UPP — the shared retrieval framework CLR and LWS build on; a standing direct, not transitional |

### Transition Phase — decoupled reorgs (Dylan's now; my internal proposal on my own clock, ~Q3)

**Dylan's reorg comes first (finalized this week after calibrations, announced shortly after).** It moves the org chart: Daniel and his team + scope report to me; Dhruvil gets the blending team (Rahul + ~5–6 engineers). Only Dhruvil and I take headcount this cycle. On my side, the only immediate change is the inheritance itself — Daniel keeps managing his team and now reports to me. (Other EMs hear ~1–2 days before the announcement; the decision audience until then is you, me, and Dhruvil.)

**My internal reorg is decoupled and runs on my own clock.** You explicitly gave me room to observe, think, and propose the internal structure separately rather than execute it simultaneously. So the three legs above are the *target* I'm proposing — not a day-1 event. This is the deliberate, depth-of-thinking version: stage the moves, don't big-bang them.

**Initial state (right after Dylan's reorg + Alim's 7/27 start) — minimal reporting-chain changes:**
- **Alim onboards with a subset of *my current* reports** — the retentive-recs nucleus (**Chuxi, Yidi, Alok**) plus **Lionel** (starts 7/27). I'm deliberately *not* moving Daniel's reports to Alim yet — too drastic a change while everyone's landing. **Zihao stays with me** (7/15): he leads UPP cross-surface training and is the UPP succession hedge behind Piyush — his centre of gravity is the framework, not exploration. Content Exploration matrixes or waits for the settle.
- **Daniel's team stays intact under Daniel.** The RR-shed and the anticipation consolidation come later, out of the observation.
- **CLR and UPP stay with me** — we aligned that handing them to Alim or Daniel right away is too much context to transfer cleanly.
- **LWS** (split from CLR) is the natural first ramp for Daniel — you flagged it as a good onboarding surface; exact timing I'll propose from the observation.

**Goals for the observation period:**

1. **Business continuity** — every workstream and pager keeps a named owner; nothing drops.
2. **Minimize disruption** — move as little as possible initially; the bigger internal moves (CLR → Alim, the anticipation consolidation, LWS → Daniel) come after I've observed, not on day one.
3. **Understand the inherited Curation-ML scope** (Intelligent Boards, Recommend-a-Board, Unity Board, exploration) before locking structure around it.
4. **Read how the EMs are doing** (Alim onboarding, Daniel's charter fit) before finalizing.

**Checkpoints:** I'll bring you the internal-reorg proposal after the observation period, with 30/60/90 touch-points along the way — on our clock, not tied to the announcement.

### Longer Term: Q4 2026 / Q1 2027

Possible team setups, depending on how Q3 resolves:

- **CLR → Alim at settle.** CLR stays with me transitionally (Devin leading), then moves to Alim's anticipation leg, whose Retentive Recs work it's most synergistic with. Not going to Daniel — would overload his onboarding. *Gate: Daniel + Alim both landed; the observe read.*
- **UPP stays with me as the framework.** UPP is the shared retrieval framework both CLR and LWS build on; Piyush anchors it. A standing direct, not a transitional one — it's the substrate the org consumes.
- **GenRet graduates** — moves out of my direct pod to its durable home once the incubation criteria are met. *Gate: settle-point review.*
- **Boards modeling depth** — how far Intelligent Boards / Recommend-a-Board grow as a frontier surface under Daniel, and whether board-modeling shares a pod with LWS scoring. *Gate: the Curation-ML learning in goal 3 above.*
- **Balaji** — Daniel's platform TL or Alim's Staff anchor. *Gate: my first real conversation with Daniel + the workstream map.*

The point of naming these as longer-term: the day-1 shape is deliberately the low-regret starting state, and each of these converges on evidence from the observe window, not on a guess made today.

### Workstreams & Leads

How each workstream evolves, mapped to the three legs:

| Workstream | Leg / front door | Technical lead | How it evolves |
|---|---|---|---|
| **UPP** | Me | Piyush | The framework/substrate that supports CLR + LWS; stays with me as the unifying retrieval foundation (a standing direct, not transitional) |
| **CLR + GULP** | Me day-1 → Alim at settle | Devin | Frontier retrieval modeling; NOT added to Daniel's day-1 load (digestion). Longer-term → Alim, given CLR↔Retentive synergy |
| **LWS** (inherited by Daniel) | Daniel | Yali | Lightweight-scoring modeling; oncall moves to Daniel day-1 |
| **L1 Utility / Real-Time** | Me | Rui (ops) · JJ | Sits inside the Foundations & Efficiency charter (JJ + Rui), James-direct. Your image paired it with LWS, but LWS → Daniel and L1 stays here — different owners |
| **Retentive Recs** (+ Unified Explore Backend) | Alim | Chuxi (ramping) · Roderick (UEB) | Both pUIC experiments land month-1; UEB consolidates into the anticipation leg; **CLR joins Alim at settle** (CLR↔Retentive synergy) |
| **Reflex** | Me | JJ (Build) · Dafang overall | Nimble vTeam; my primary time; the AI-tooling accelerator every leg adopts |
| **RecGPT / Generative Retrieval** | Me (incubation) | Bella | Time-boxed incubation; graduates/moves at settle |
| **Intelligent Boards** | Daniel | boards TL TBD | Retained; frontier boards modeling (metric gains + publications) |
| **Recommended Boards** | Daniel | boards TL TBD | Retained; live surfaces (Related Pins, Search) + frontier boards modeling |
| **Foundations & Efficiency** (Responsiveness, Cost savings) | Me (JJ) | JJ · Rui | ~half JJ's scope; kept as scope per Dylan's "don't divest small things." Includes L1 utility + RT responsiveness + cost savings |

### Calls I've made

1. **LWS → Daniel on day 1** (he inherits its oncall and scoring-modeling work); any CLR consolidation is a settle-point call. Keeps blast radius low while his team lands and protects the Devin transition.
2. **Lionel → Alim's pod** (L14 SWE, Toronto, starts 7/27 with Alim). The RR bottleneck all year has been serving, and he's the only dedicated SWE in that space; starting the same day as Alim makes him a founding member, not the new guy on an old team.
3. **Alok → Retentive Recs (primary) + Reflex.** Alok chose RR himself, and I want him there: **RR loses Yuke** to the single RecGPT stream, so Alok is load-bearing for that pod alongside Chuxi and Yidi. *(Corrected 7/15 — supersedes the earlier "Reflex 50% + UPP 50%; RR is staffed without him," which was wrong on both counts.)*
4. **JJ splits ~half Reflex / ~half Foundations & Efficiency** (responsiveness, L1 utility, cost — kept per Dylan's "don't divest small things"); **Rui is the L1/Real-Time operational owner** underneath.
5. **CLR is not part of Daniel's day-1 scope.** Adding CLR on top of LWS + boards would overload his onboarding. CLR stays with me transitionally (Devin leading), targeted to Alim at settle given the CLR↔Retentive synergy. **UPP stays with me as the framework** both CLR and LWS build on.

### Where I want your input

1. **Balaji** (Staff, Daniel's team): platform TL under Daniel, or Staff anchor under Alim? It touches what Alim was promised, so your read matters. Default: decide inside the observe window, after my first real conversation with Daniel.
2. **Kim's loan to Dhruvil:** as the reorg settles I want the loan wound down so her time comes back to our side. Cleanest if you set it up with Dhruvil — the reorg gives natural cover.

### Sequencing

**Dylan's announcement** (this week, after calibrations; other EMs ~1–2 days prior) → **I talk to Daniel first**, framing the inheritance as scope following people → **Alim + Lionel start 7/27**, Alim taking his initial nucleus from my current reports → **observation period** (Daniel's team intact, CLR/UPP with me) → **my internal-reorg proposal to you** after I've observed, staging the deferred moves (CLR → Alim, RR consolidation, LWS → Daniel) deliberately. The Anna (RR front door), Chuxi (grow-in-place), and Bella conversations sequence with *those* moves — not the initial announcement. No need to socialize changes that aren't happening yet.

---

## Draft notes — strip before sending (for the grill)

Open items / decisions this draft is carrying that the grill should resolve:

1. **Framing adjustments (CONFIRMED 7/14 — kept):** (a) added Calls / Input / Sequencing under Proposal so the doc closes the loop Dylan opened; (b) routing table folded into Ownership; (c) name + scope-definition line up top. James approved all three.
2. **Responsiveness / GULP (RESOLVED 7/14).** Responsiveness KEPT under Foundations & Efficiency (JJ, ~half) per Dylan's "don't divest small things" — reverses the May-26 divest. GULP rides with CLR (Me/Devin now → Alim at settle).
3. **Daniel's leg = frontier modeling (RESOLVED 7/14).** His area is frontier ML modeling (metric gains + KDD/RecSys papers), NOT infra/KTLO. Leg = boards (retained) + LWS (inherited); sheds RR people to Alim. Working name **"Scoring & Boards Modeling"** (→ "Retrieval & Boards Modeling" if CLR folds in — confirm the name). NOTE: supersedes the v1 working doc's "Scoring & Serving Platform / least-AI-shiny / AI-leveraged-oncall-as-motivation" framing — wrong premise; update `daniel_liu_team_2026-07.md` + v1 proposal at end-session.
4. **CLR placement (RESOLVED 7/14).** NOT to Daniel (would overload onboarding). CLR stays with me transitionally (Devin), → **Alim** at settle (CLR↔Retentive synergy). **UPP stays with me as the framework** supporting both CLR and LWS (Piyush anchors — resolves the Piyush seam). Daniel's leg name stays "Scoring & Boards Modeling." Open sub-item: Kim's CLR-bridge loan-wind-down ask to Dylan — still valid, but reframe since CLR isn't spinning up under Daniel (it's staying with me). Revisit the Kim ask (footer relates to §Input ask 2).
5. **Audience (CONFIRMED 7/14): Dylan-only** for now. Later *maybe* Rajat + other leadership — to show depth of thinking on work design — but that's farther away; when it comes, generate a stripped version (Personnel + Input-asks removed) and separate messaging. Immediate audience = Dylan.
6. **Piyush as named personnel (CONFIRMED 7/14 — kept).** Answers Dylan's "who TLs each space"; the retrieval-framework anchor is the one IC worth naming at her altitude.
7. **Boards technical leads = TBD** (three rows). From Daniel's roster, Yongwoo/Felix workstreams are unknown — these fill after your first Daniel conversation.
8. **Yuke line (RESOLVED 7/14):** all role-change phrasing removed — the pod table now reads "single RecGPT stream" only, no reference to his role change (per James, 7/14).
9. **"LWS + L1 Utility" pairing (RESOLVED 7/14).** Not co-owned: LWS → Daniel; L1 utility → JJ/Rui under Foundations & Efficiency (James-direct). "Consolidating" read as pulling L1-utility scope together, not merging with LWS.
10. **Foundations & Efficiency owner (RESOLVED 7/14).** → JJ, ~half his scope (other half Reflex); James-direct; Rui on L1/RT ops. Kept per Dylan's "don't divest small things." Justifies Rui as a direct.
11. **Dylan conversation 7/14 — timeline + initial-state reconciled (see Transition Phase).** Her reorg first (Daniel→me; Dhruvil→blending team Rahul+~5–6); my internal reorg **decoupled, my clock**. Initial state = minimal changes: Alim takes a subset of MY reports (not Daniel's) + Lionel; Daniel's team intact; CLR+UPP stay with me (she's aligned); LWS = Daniel's ramp (she's aligned); more Reflex time (she's aligned). Only Dhruvil + I get headcount. Political backing: HR/Andrew/Rajat prefaced + happy, framed as my path to the next level. Comms: other EMs ~1–2 days prior; audience Dylan+me+Dhruvil; finalized this week after calibrations.
12. **Roster reconciliation — initial vs. target. Alim's INITIAL POD LOCKED 7/15 = Chuxi / Yidi / Alok / Lionel** (4; no Staff, no L15). **Zihao removed** — stays with James on UPP (cross-surface training lead + Piyush succession hedge); the ⟨confirm⟩ on him was never confirmed and had been carried forward from the 6/30 Track-A/B split, whose sorting key was Content Exploration. **Alok added** (RR primary, his own call; RR loses Yuke). *Target* adds Daniel's anticipation folks (Ling/Roderick/Yang) later. Daniel *initial* = his intact team; *target* = +LWS (Yali/Hedi/Zili), boards retained. James-direct *initial* also holds the CLR pod (Devin/Yichi/Ryan) transitionally. The "~8 Alim / ~7 James" counts in the doc are TARGET, not initial — reconcile both columns.

---

# Rollout Messaging & Meeting Plan — INTERNAL (2026-07-14)

**Do not send to Dylan. James's private playbook for cascading the reorg to the teams once Dylan's announcement lands.**

## Calibrations (things the messaging must NOT assume)

- **"Underutilized" is Dylan's private read for James, not a narrative in anyone's head.** Do not use it as a talking point — don't hand Daniel's team a grievance they weren't carrying, don't imply to Daniel his team's been failing.
- **The team already knows Alim is joining** (they've been asking; James has already discussed layering vs. not, and how he's thinking about it). So these meetings *continue* a conversation, not open one.
- **The new news at Dylan's announcement is the Daniel inheritance** (Daniel's team reports into James). Alim's actual start is 7/27, later and separate.
- **Reporting lines:** Daniel reported to **Yann (Senior EM), not Dylan** — so his move is a *lateral re-parenting* (Sr EM → Sr EM), not a new layer inserted above him. No demotion shape; the real work is new-manager-relationship + team-changing-orgs, not de-layering.

## Meeting structure — decision: **all 3, sequenced (not simultaneous)**

Two groups (James's existing team + Daniel's inherited team); three possible structures (A combined-only / B separate-only / C both-separates + a combined). **Verdict: C, sequenced.**

The two separate meetings do **opposite emotional jobs**, which is why they can't be collapsed:
- **Existing team** needs *rally + continuity*: "we're inheriting a team and real scope; day-to-day, almost nothing changes for you."
- **Daniel's team** needs *respect + don't-spook*: "glad to have you; Daniel keeps leading you; nothing's getting reshuffled; I want to learn before I touch anything." **Daniel runs this meeting; James is the guest.**

Combined-only (A) is out: each audience hears the message meant for the other (Daniel's team feels like the acquired company at the acquirer's all-hands). Separate-only (B) is incomplete: never convening everyone signals two permanent camps. So do both separates first, and the **combined identity all-hands later — after the observation period**, when there's a real joint roadmap. Doing it in announcement week would contradict the minimal-change posture locked with Dylan on 7/14.

**Sequence — Wave 1 (announcement week):** (1) Daniel 1:1 first → (2) existing team, separate → (3) Daniel's team, separate, Daniel-run. Keep (2) and (3) close in time to avoid an info-asymmetry gap. **Wave 2 (post-observe):** combined all-hands.

**Governing rule for all reporting-change messaging:** the people actually moving (**Chuxi / Yidi / Alok / Lionel → Alim**) get a **1:1 before any group meeting** — they walk in already knowing. Never let someone learn in a group room that they're being moved. *(Updated 7/15: Zihao is no longer moving; Alok is.)*

## Existing-team proactive message

The real anxiety Daniel's arrival triggers: **the group who thought they were "safe" (staying with James) now does the math — James's span just ballooned, so I'm probably getting moved too.** Get ahead of *that specific inference*:

1. **Name the news and the inference out loud.** "Daniel's team is joining and will report to me. The natural next thought is 'James's org just got bigger, so my reporting line's about to change.' For most of you: no."
2. **Give the mechanism.** Daniel's team stays *under Daniel* — so the org got bigger but James's direct span did **not** jump. That's the most reassuring true thing available; say it plainly.
3. **Promise process, not permanence.** James *can't* promise everyone reports to him forever (target direct pod is deliberately focused; CLR pod, Alim nucleus, GenRet-at-graduation do move). So the durable promise is: **"No one's line changes without hearing it from me first, in a 1:1, with the reasoning — never as a surprise, never in a room like this."** The real fear isn't change; it's finding out you were moved without being in the conversation.
4. **Kill attention-dilution.** "Org's bigger, but Daniel runs his team day-to-day — my attention to you isn't halved."
5. **Answer the unasked 'did something go wrong?'** "This isn't a reaction to anything anyone did — the org's being *trusted with more.*"
6. **Close on what's in it for them.** More senior leadership per person = more coaching, clearer charters, more room to grow — not dilution, not scope competition.

## Project stability — the mirror (both teams ask "is my project safe?", opposite root fears)

The fact that the fears are *opposite* is itself the strongest argument for separate rooms — the reassurance each needs slightly contradicts the other.

- **Existing team = fear of dilution by the newcomer.** Concrete threats live in the proposal's own logic: consolidation ("stop building the same thing three times" → one UPP backbone → substrate-variant owners fear losing ownership); **GenRet is explicitly time-boxed with sunset criteria** (Bella/Hanlin *know* it can be sunset); **CLR is transitional → Alim** (Devin/Yichi/Ryan hear reprioritized + re-homed). Unifying fear: *where does my thing land in the new priority stack now that boards/RR compete for it?*
- **Daniel's team = fear of deprioritization as the newcomer.** *We're the incoming team in a retrieval/anticipation org — does our boards/RR/LWS work still matter, or get redirected onto the host's priorities?* Boards carries extra dread (surface hasn't moved metrics in ~6 months → fear of quiet wind-down; the notif "wow" collab is the bright spot to affirm). RR folks may sense the eventual Alim shed; LWS folks get a new charter home under Daniel.

James can't tell both rooms "you're the priority." To his team: scope is *additive, not substitutive.* To Daniel's team: their work is *valued, not sidelined.* Both true; said in one room, each side discounts its own reassurance → separate meetings in Wave 1; combined only once one integrated roadmap makes "one priority stack" a promise, not a threat.

## Daniel — the retention conversation (the priority)

**Dylan's actual mandate:** not "inform Daniel" — **assess his retention and learn what motivates him.** Dylan pre-confirmed the hypothesis: **LLM-based work excites him.** So the 1:1 is a two-way *retention* conversation (listen first), and it exposes a design problem to resolve **before** the meeting:

**The charter–motivation mismatch (flag to verify, not asserted).** Daniel's assigned leg — **boards + LWS scoring modeling** — is "frontier ML modeling" but **not obviously LLM-based** (LWS is lightweight/efficient scoring, arguably the opposite of LLM-heavy; boards modeling is classical unless deliberately made generative). Meanwhile the LLM-shiny work — **RecGPT/Generative Retrieval, LLM-based pUIC** — currently sits with **James (GenRet) and Alim (LLM-pUIC), not Daniel.** If his motivation is LLM work and his charter isn't, that's the retention gap — and it's James's design to fix.

**James's decision (2026-07-14): don't close it with a charter change now.** Daniel is **not** the right lead for **Retentive Recs** (Anna's product-instinct veto) and **not** the right lead for **Reflex** (too much context to transfer). So the LLM-motivation is *not* satisfied by handing him a new charter on day one. Instead it's a **trajectory play**: the inheritance is his opening to *get more involved over time* in the direction he wants, plus **future things James + Daniel build together** — something to *work on*, not change now. Keeps the minimal-change posture and lets the 1:1 stay authentic: listen for what he wants, then paint an honest growth path + partnership, not an over-promised LLM leg.

*The GenRet-home / LLM-boards / LWS-distillation ideas become **future collaboration seeds**, not day-1 moves.* Stance for the "will I get LLM work?" question below: honest — not by leading RR or Reflex, but here's the path to grow into it and build together over time.

**Questions Daniel will ask (retention-weighted):**
- *Will I actually get to work on LLM/generative modeling, or is that happening elsewhere while I'm on classical boards/scoring?* ← the driver, maybe unspoken
- Is this charter *frontier*, or is boards-that-hasn't-moved-metrics a backwater with a nice label?
- Growth path — can I make Senior EM here, or does reporting into another Sr EM cap me?
- Do I keep my team intact and my autonomy? *(reshuffle fear — RR shed is deferred; hold it)*
- Is the KDD/RecSys publication support real or lip service?
- Why me — opportunity or a place things got parked?
- Yann situation — leaving on good terms? Was I consulted?
- Headcount for my charter? *(honest: not this cycle — the scope is the growth)*

**Questions JAMES should ask Daniel (the actual assignment — surface motivation, gauge flight risk):**
- What work energizes you most right now — where do you *want* your technical time going?
- If you could shape your team's charter for the next year, what would it be? *(does "LLM/generative" come out unprompted?)*
- What's felt blocked or underleveraged lately? *(lets the feeling surface from him)*
- What would make this move a clear win for you? A bad outcome?
- Where do you want to grow; what's the next level look like?
- Who on your team is critical or a flight risk, and what do they need?

**Flight-risk watch-fors:** flat affect on the charter; "I need to think about it"; steering to level/comp early; strong attachment to Yann; treating boards as a dead end; fishing about external optionality. Two+ → signal to Dylan + accelerate option 1.

## Question banks — Wave 1 meetings

Landmines flagged **→ stance.**

### Existing team
- **Who exactly reports to Alim vs. stays with you?** *(have the specific list ready)*
- **Did I get a say in a new manager?** → don't pretend it was participatory; "you didn't pick this — react honestly in our 1:1; my job is to make it a good setup, here's why it is."
- **Does my promo case reset with a new manager?** → **big one:** promo continuity, you + Alim co-own the case, no lost runway.
- Why a new EM — did something go wrong / did I? → additive, not corrective.
- What's Alim like / his background?
- **Layoffs coming? Prelude to cuts?** → don't dodge: "this is growth — *adding* a team + scope, not trimming."
- What happens to my project (CLR / UPP / Reflex / GenRet)?
- Are we absorbing Daniel's team, over/under/parallel?
- More work / competition for scope at same headcount?
- **Are you getting promoted, James? A director thing?** → keep altitude: "the org's being invested in," not "I'm going for director."
- Team name/identity changing (P13N Retrieval & Anticipation ML)? Day-to-day / oncall / roadmap change, and when?

### Daniel's team *(Daniel runs it; James is guest)*
- **Why are we moving to James's org — what was wrong with Yann's?** → forward-framing; not a reaction to anything.
- **Is Daniel still our manager? Did he get demoted?** → clear no: lateral move; Daniel leads you; his charter is *elevated* to frontier modeling.
- **Are we being split up / absorbed?** → **landmine (RR shed deferred):** "No changes to this team now; anything structural is deliberate, with Daniel + the people affected in the room first." Don't pre-announce the RR shed; don't promise "never."
- What happens to our projects (boards, RR, LWS) — valued or killed?
- Who is James / what does he care about / like to work for?
- Level / promo / comp / skip-level change?
- LWS moving under Daniel — what does that mean for us?
- Change how we work (tools, process, oncall)? Keep our identity or fold into P13N Retrieval & Anticipation ML?
- What changes day one vs. later? Timeline?

### Daniel (1:1)
*(see the retention section above — full list there; landmines: LLM/generative work, team-stays-intact, growth/cap, headcount, Yann.)*

---

# Appendix — Master Roster (authoritative, James 2026-07-15)

> **Replaces** the v1-migrated table. Levels, families, and current projects are now **James-confirmed** (previously several were inferred/`?`). The old "Draft destination" column is **dropped** — it carried pre-7/14 fork thinking (CLR→Daniel, "Scoring & Serving Platform") that the v2 body supersedes, and placement is the subject of the pending **initial-vs-target roster reconciliation**, not a settled fact to table here.
>
> **Naming correction (2026-07-15):** the engineer this repo called **"Ray"** is **Rui Wang** — a dictation/preferred-name artifact, corrected throughout. One person, not two.

### Engineering Managers
| Name | Level (Family) | Role | Notes |
|---|---|---|---|
| **James Li** | **M17** MLE | EM lead for the organization | — |
| **Daniel Liu** | **M16** MLE | (current) EM on Curation ML | Supports 7 ICs |
| **Alim Virani** (he/him) | **M16** MLE | — | **Joins 7/27/2026** |

### IC level distribution (26 ICs incl. 2 open reqs)
| Level | Count | People |
|---|---|---|
| **L16** | 3 (12%) | Piyush, Bella, Balaji |
| **L15** | 12 (46%) | JJ, Zihao, Yali, Devin, Hedi, Yuke, Roderick, Yang, Kim, Yongwoo, **Ryan**, Req-1 |
| **L14** | 8 (31%) | Chuxi, Ling, Hanlin, Rui, Felix, Alok, Lionel, Zili |
| **L13** | 3 (12%) | Yichi, Yidi, Req-2 |

### Full IC roster
> "Reports to" = **current** line (Daniel's 7 come to James's org via Dylan's reorg; Alim's pod forms 7/27). Not the target state.

| Name | Level | Family | Current main projects | Reports to | Notes |
|---|---|---|---|---|---|
| Piyush Maheshwari | **L16** | MLE | UPP · CLR (advisory) · LWS (advisory) | James | Single point of failure on UPP |
| Bella Huang | **L16** | MLE | RecGPT · Reflex | James | Staying; top-lab leave-trigger |
| Balaji Rengarajan (he/him) | **L16** | MLE | **Intelligent Boards** | Daniel | Day-to-day now known — was "unknown"; feeds fork F2 |
| Devin Kreuzer | **L15** | MLE | CLR · GULP | James | CLR lead |
| Ryan Kam | **L15** | SWE | CLR · LWS (dev-velocity focused) | James | Joined ~May 2026 |
| J.J. Hu | **L15** | MLE | Responsiveness · L1 · Reflex | James | IC16 package submitted 7/10 |
| Yali Bian | **L15** | MLE | LWS | James | De facto LWS owner |
| Hedi Xia | **L15** | MLE | LWS | James | — |
| Yuke Yan | **L15** | MLE | Retentive Recs · RecGPT | James | **Will move to RecGPT only**; PIP track, stays under James |
| Zihao Chen | **L15** | MLE | UPP · Content Exploration | James | UPP succession hedge vs. Alim's exploration charter |
| Roderick Gao | **L15** | SWE | Unified Explore Backend | Daniel | — |
| Yang Liu | **L15** | MLE | **Parental leave** | Daniel | Return date / ramp open |
| Kim Toy | **L15** | MLE | UPP foundational (loaned to Dhruvil) · CLR | Daniel | Loan wind-down = Dylan ask #2 |
| Yongwoo Noh | **L15** | MLE | **Not sure** | Daniel | Fill after first Daniel conversation |
| **REQ-1 (open)** | **L15** | MLE | — | James | New headcount ~7/11; unallocated |
| Rui Wang | **L14** | SWE | Reflex · L1 | James | **= the "Ray" of prior docs.** Joined ~late June 2026 |
| Alok Malik | **L14** | MLE | **Retentive Recs (primary)** · Reflex | James | RR = his own call; needed as Yuke exits RR. §Calls #3 corrected 7/15. ⚠️ RR is Alim's charter — reporting line open |
| Zili Li | **L14** | MLE | LWS | James | Open perf case — James keeps it |
| Hanlin Lu | **L14** | MLE | RecGPT | James | — |
| Chuxi Wang | **L14** | MLE | Retentive Recs | James | Supported, unannounced TL ramp |
| Lionel Bewa | **L14** | SWE | — | James | **Joins 7/27**; Toronto; Charlie backfill |
| Ling Lan | **L14** | MLE | **Retentive Recs · Intelligent Boards** | Daniel | Straddles Alim's charter + Daniel's boards; Chuxi's daily partner |
| Felix Yang | **L14** | SWE | **Not sure** | Daniel | Fill after first Daniel conversation |
| Yichi Wang | **L13** | MLE | CLR | James | — |
| Yidi Wang | **L13** | MLE | Retentive Recs | James | Carrying most of model-based pUIC |
| **REQ-2 (open)** | **L13** | MLE | — | James | New headcount ~7/11; unallocated |

*Not in the 26: Rita Lyu (intern, Daniel's team, ~2 months left — ignore for design). Departed: Sophia, David, Charlie (exiting).*
