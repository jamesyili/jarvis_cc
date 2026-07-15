# P13N Retrieval — Org Design

**For:** Dylan · **From:** James · **Date:** 2026-07-14
**Status: WORKING DRAFT (v2, new section framing). Audience = Dylan only — cold-reader-safe, but the Personnel section does not travel.** Supersedes the 9-section skeleton + Drafts A/B/C in `org_design_proposal_2026-07.md` (that file remains the working notes / IC table / forks reference).

**The org:** **P13N Retrieval** — the pre-ranking funnel end to end, from user signal to what the ranker sees. Ranking starts where we end; surfaces belong to P13N-Experiences. This name retires "HF CG." Three legs inside it — the *target* shape I'm proposing, phased into on my own clock (see Transition Phase):

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

So the beyond-transition footprint is two EMs on the standing modeling charters, and a deliberate James-direct footprint = the Reflex frontier + the UPP framework + Foundations & Efficiency (JJ/Ray) — not a wide span I hold indefinitely.

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
   | Foundations & Efficiency (responsiveness, L1 utility, cost) | Me | JJ · Ray |

4. **Oncall.** Every rotation has a day-1 owner and a settle-state owner — **no pager gap at any point.** LWS oncall moves to Daniel on day 1; boards oncall stays with Daniel (his retained scope); L1/Real-Time oncall to Ray (under the Foundations & Efficiency charter JJ co-owns); the new pUIC serving surface staffs with a deliberate ramp for the incoming SWE. One carry-over by design: I keep Zili's performance management even as his rotation moves — no new EM inherits an open case.

**The direct pod, each seat justified** (the "where does my time go" answer):

| Person | Why they report to me |
|---|---|
| JJ | Reflex Build lead (~half) + Foundations & Efficiency (~half): responsiveness, L1 utility, cost savings |
| Ray | L1 / Real-Time operational owner, under the Foundations & Efficiency charter JJ co-owns |
| Alok | Reflex 50% + UPP 50% |
| Bella | Staff lead for the GenRet incubation; continuity through the transition |
| Hanlin | GenRet delivery pair with Bella |
| Yuke | Single RecGPT stream after the role change we discussed; I hold his management so no new EM starts with an open thread |
| Piyush | UPP — the shared retrieval framework CLR and LWS build on; a standing direct, not transitional |

### Transition Phase — decoupled reorgs (Dylan's now; my internal proposal on my own clock, ~Q3)

**Dylan's reorg comes first (finalized this week after calibrations, announced shortly after).** It moves the org chart: Daniel and his team + scope report to me; Dhruvil gets the blending team (Rahul + ~5–6 engineers). Only Dhruvil and I take headcount this cycle. On my side, the only immediate change is the inheritance itself — Daniel keeps managing his team and now reports to me. (Other EMs hear ~1–2 days before the announcement; the decision audience until then is you, me, and Dhruvil.)

**My internal reorg is decoupled and runs on my own clock.** You explicitly gave me room to observe, think, and propose the internal structure separately rather than execute it simultaneously. So the three legs above are the *target* I'm proposing — not a day-1 event. This is the deliberate, depth-of-thinking version: stage the moves, don't big-bang them.

**Initial state (right after Dylan's reorg + Alim's 7/27 start) — minimal reporting-chain changes:**
- **Alim onboards with a subset of *my current* reports** — the anticipation/exploration nucleus (Chuxi, Yidi, Zihao) plus Lionel (starts 7/27). I'm deliberately *not* moving Daniel's reports to Alim yet — too drastic a change while everyone's landing.
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
| **L1 Utility / Real-Time** | Me | Ray (ops) · JJ | Sits inside the Foundations & Efficiency charter (JJ + Ray), James-direct. Your image paired it with LWS, but LWS → Daniel and L1 stays here — different owners |
| **Retentive Recs** (+ Unified Explore Backend) | Alim | Chuxi (ramping) · Roderick (UEB) | Both pUIC experiments land month-1; UEB consolidates into the anticipation leg; **CLR joins Alim at settle** (CLR↔Retentive synergy) |
| **Reflex** | Me | JJ (Build) · Dafang overall | Nimble vTeam; my primary time; the AI-tooling accelerator every leg adopts |
| **RecGPT / Generative Retrieval** | Me (incubation) | Bella | Time-boxed incubation; graduates/moves at settle |
| **Intelligent Boards** | Daniel | boards TL TBD | Retained; frontier boards modeling (metric gains + publications) |
| **Recommended Boards** | Daniel | boards TL TBD | Retained; live surfaces (Related Pins, Search) + frontier boards modeling |
| **Foundations & Efficiency** (Responsiveness, Cost savings) | Me (JJ) | JJ · Ray | ~half JJ's scope; kept as scope per Dylan's "don't divest small things." Includes L1 utility + RT responsiveness + cost savings |

### Calls I've made

1. **LWS → Daniel on day 1** (he inherits its oncall and scoring-modeling work); any CLR consolidation is a settle-point call. Keeps blast radius low while his team lands and protects the Devin transition.
2. **Lionel → Alim's pod** (L14 SWE, Toronto, starts 7/27 with Alim). The RR bottleneck all year has been serving, and he's the only dedicated SWE in that space; starting the same day as Alim makes him a founding member, not the new guy on an old team.
3. **Alok → Reflex 50% + UPP 50%.** RR is staffed without him.
4. **JJ splits ~half Reflex / ~half Foundations & Efficiency** (responsiveness, L1 utility, cost — kept per Dylan's "don't divest small things"); **Ray is the L1/Real-Time operational owner** underneath.
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
8. **Yuke line** ("single RecGPT stream after the role change we discussed") — confirm this is the safe phrasing you want in a doc, vs. omitting him from the visible pod table entirely.
9. **"LWS + L1 Utility" pairing (RESOLVED 7/14).** Not co-owned: LWS → Daniel; L1 utility → JJ/Ray under Foundations & Efficiency (James-direct). "Consolidating" read as pulling L1-utility scope together, not merging with LWS.
10. **Foundations & Efficiency owner (RESOLVED 7/14).** → JJ, ~half his scope (other half Reflex); James-direct; Ray on L1/RT ops. Kept per Dylan's "don't divest small things." Justifies Ray as a direct.
11. **Dylan conversation 7/14 — timeline + initial-state reconciled (see Transition Phase).** Her reorg first (Daniel→me; Dhruvil→blending team Rahul+~5–6); my internal reorg **decoupled, my clock**. Initial state = minimal changes: Alim takes a subset of MY reports (not Daniel's) + Lionel; Daniel's team intact; CLR+UPP stay with me (she's aligned); LWS = Daniel's ramp (she's aligned); more Reflex time (she's aligned). Only Dhruvil + I get headcount. Political backing: HR/Andrew/Rajat prefaced + happy, framed as my path to the next level. Comms: other EMs ~1–2 days prior; audience Dylan+me+Dhruvil; finalized this week after calibrations.
12. **Roster reconciliation (next task) — now initial vs. target.** Alim *initial* = Chuxi/Yidi/Zihao/Lionel (my reports); *target* adds Daniel's anticipation folks (Ling/Roderick/Yang) later. Daniel *initial* = his intact team; *target* = +LWS (Yali/Hedi/Zili), boards retained. James-direct *initial* also holds the CLR pod (Devin/Yichi/Ryan) transitionally. The "~8 Alim / ~7 James" counts in the doc are TARGET, not initial — reconcile both columns.
