# GDoc Fill — "P13N Retrieval and Anticipation Org Discussion" (2026-07-27)

**Purpose:** deliverable 2 of the 7/27 session — paste-ready content for each section of the live GDoc (photographed 7/27), in its structure and order. Sort/trim as you paste; sourced from the 7/24 exec-voice doc + v2 + 7/25 decisions. **Internal-only annotations are in blockquotes — strip them.**

> **Two string patches before anything ships (follow-up #14):**
> 1. Title: "P13N Retrieval and Anticipation" → **"Personalization Retrieval and Anticipation"** (LOCKED 7/25, supersedes the P13N string).
> 2. Charter table + section heading: "Anticipation ML" → **"Anticipation Modeling"** (team names locked 7/24: Retrieval Foundations / Retrieval Modeling / Anticipation Modeling).
>
> **Audience check:** the GDoc is a *Discussion* doc for alignment week. The Key Personnel and direct-pod content below is calibrated Dylan-only — if this doc travels wider (Rajat/Jeff/Christina/Andrew/Mira per the alignment-week roster), strip Personnel + the per-seat pod table + the Decisions asks.
---

## Executive Summary

> Already written in the doc (three synergies). Two optional additions if you want them:

**The proof-point sentence (after "three key synergies"):** Anticipation Cupcake demonstrated that this group can deliver a complex, cross-surface initiative with urgency and quality — and gave us a precise read on where execution cost lives: ownership boundaries negotiated while we shipped, cross-team asks with no default routing, decision rights settled conversation by conversation. This merger converts that cross-org negotiation into intra-org design.

**The honest-boundary sentence (closing):** One boundary worth stating plainly: the cross-org seams with Tim's and Yan's organizations remain cross-org, governed by explicit notice norms. What this merger dissolves is the internal anticipation seams, which have been the more expensive ones.

---

## Key Outcomes

> The doc has no prose under "Key Outcomes" — the six numbered outcomes from the 7/24 doc fit here:

1. A single point of ownership for anticipation across ML and backend: pUIC (model-based and LLM-based) and its serving path owned end to end by one organization.
2. One prioritized roadmap spanning anticipation, exploration, boards, and platform.
3. One personalization substrate: CLR and LWS build on UPP rather than maintaining divergent variants.
4. One consolidated LLM-serving investment across LLM-based pUIC, RecGPT / Generative Retrieval, and board recs.
5. Reflex tooling adopted across every workstream, with dev-velocity gains we can measure.
6. Named front doors for every partner organization, and continuous pager coverage throughout the transition.

## Establish Clear Charter — table fill

| Subteam Name | EM | Mission | Ownership |
|---|---|---|---|
| **Retrieval Modeling** | Daniel Liu | Frontier ML modeling that drives metric gains across preranking and boards, and publishes at venues like KDD and RecSys | LWS (lightweight preranking — the reliable gains engine) · Intelligent Boards (frontier bet, placement gated) · Recommended Boards (live traffic: Related Pins, Search) |
| **Anticipation Modeling** | Alim Virani (He Him) | Anticipate what a Pinner wants next: model the interests that bring them back and have the content and serving path ready when they arrive. Measured on retention and fresh-content discovery | pUIC (model-based + LLM-based) · Retentive Recs · Unified Explore Backend / Explore Page · Generative Retrieval joins at the settle point as the team's proven gains engine |
| **Retrieval Foundations** | James Li | Own the substrate the organization builds on: the shared UPP retrieval framework, AI-enabled dev velocity (Reflex), and platform efficiency | UPP · CLR (transitional, → Anticipation Modeling at settle) · Reflex + agentic dev-velocity systems · Foundations & Efficiency (responsiveness, L1 utility, cost) |

> Boundary sentence worth adding under the table: *The two "Retrieval" teams split cleanly: Foundations owns the framework and substrate the org builds on; Modeling owns the models that run on it.* And: *each team pairs a workstream reliably producing gains with frontier bets — no team is all-risk, no team is all-maintenance.*

### Anticipation Modeling (section body)

Anticipation Modeling owns the full anticipation stack from user signal to candidate: the predictive-UIC substrate (model-based and LLM-based), Retentive Recs, and the exploration surfaces (Unified Explore Backend, Explore Page). Both pUIC experiments land within the team's first month, with named senior support around the TL ramp (Chuxi, with Ling's delivery partnership and Roderick's seniority on UEB). At the settle point the team gains Generative Retrieval as its proven gains engine and CLR, whose synergy with Retentive Recs is strongest. Topline: retention and fresh-content discovery.

### Retrieval Modeling (section body)

Retrieval Modeling puts the inherited team on the org's marquee craft: frontier modeling that drives metric gains and publishes. Portfolio: LWS preranking as the reliable gains engine (inherited day one, oncall moves with it), Intelligent Boards as the 0-to-1 bet (the recent notification collaboration showed step-change improvements — the deciding read on its durable home runs over the next two months), and Recommended Boards as mature ballast with live production traffic. Boards modeling and LWS preranking are adjacent disciplines; co-locating them lets techniques and infrastructure transfer directly. Near-term LLM seeds: LWS distillation, LLM-boards.

### Retrieval Foundations (section body)

Retrieval Foundations is a deliberately minimal direct pod, each seat individually justified. It owns UPP — the shared framework CLR and LWS build on, anchored by Piyush — plus Reflex and agentic dev-velocity systems (my primary personal time), Foundations & Efficiency (responsiveness, L1 utility, cost; kept per your guidance against divesting small things), and two time-boxed transitionals: CLR until the settle point and the Generative Retrieval incubation until it graduates. As the incubations graduate, my direct footprint shrinks further: the end state is a lean span held for clear reasons, not a wide span held indefinitely.

---

## Setting Accountability for Impact

**Top Line Metrics — split across the three subteams**

| Subteam | SSv2 (of 4.5%) | Cost Savings (of $2M) | Rationale |
|---|---|---|---|
| **Retrieval Modeling** (Daniel) | **2.0%** | **$0.6M** | Carries the org's most reliable gains engine (LWS preranking) plus boards upside from surface pairings. Cost lane: LWS serving efficiency — early merge + dedupe, GPU scale-up efficiency, distillation cutting preranking cost — and consolidation of the small boards models. Moderate 0-to-1 load (IB only). |
| **Retrieval Foundations** (James) | **1.5%** | **$1.2M** | CLR production gains (day-1 home) + UPP cross-surface launches converting candidates to top-line + responsiveness support. Carries the org's explicit cost charter: Foundations & Efficiency (L1 utility consolidation, GPU serving efficiency, responsiveness) — aligned with the budget investigation's >$1.8M trim opportunity. |
| **Anticipation Modeling** (Alim) | **1.0%** | **$0.2M** | Deliberately the lightest on both: this is the 0-to-1-heavy team (both pUIC incubations + exploration), so capacity is invested in bets, not trims. SSv2 carry = model-pUIC candidate landing in month one; cost accountability = efficiency hygiene on the new pUIC serving surface (right-sized ramp, no duplicate LLM-serving stacks). Also the primary WAU/retention carry. |

- WAU (retention / fresh-content discovery) — Anticipation Modeling's primary carry; all teams share the topline per the charter.

> **Design logic of the split:** cost-savings shares run *inverse* to 0-to-1 load — teams spending capacity on incubations shouldn't also carry heavy trim targets; the team owning the efficiency charter (F&E) carries the bulk. **Settle-point re-balance:** accountability moves with charters — CLR → Alim at settle shifts ~0.5% SSv2 from Foundations to Anticipation Modeling, and GenRet's graduation adds engine capacity to Alim's number. State the split as *initial-state* allocations with a settle review, not fixed-for-the-year. ⟨Numbers are Leo's proposal from the portfolio evidence — sanity-check the 2.0/1.5/1.0 split against H1 actuals (LWS + CLR gain history) before this reaches Dylan.⟩

**New Initiatives**
- Anticipation User Interest Exploration (pUIC model-based + LLM-based; exploration surfaces)
- Anticipation Intelligent Boards (placement settles on the gains-origin read)
- SM / SL (retrieval side staffed: Yali, alongside Raymond Hsu; LWS lane = strategic home)
- Generative Retrieval / RecGPT (time-boxed incubation, explicit graduation/sunset criteria)
- Reflex (AI-enabled dev velocity; adoption across every workstream)

**Cross Org**
- NLFU (H2 support: named deliverables on existing engines — Responsiveness follow-ups, RR offsite-signal iterations, NLFU-targeted RR experiments, LLM-pUIC × PinnerSpark)
- Content Quality
- Cost / budget investigation (driving for Dylan; feeds the $2M savings line)
- Front-door routing model: every partner org gets a named owner per domain (table under Proposal → Ownership)

---

## Guidance on Technological Investments

Across P13N today, anticipation, retentive recs, and intelligent boards are advancing on parallel and often duplicative foundations. A single organization converges that investment along four lines:

- **A single personalization backbone.** Anticipation, Retentive Recs, and Intelligent Boards increasingly depend on the same user-representation and retrieval substrate. UPP becomes the shared framework on which CLR and LWS both build — built once, owned centrally, consumed by the modeling charters, rather than maintained as variants that drift apart.
- **Shared LLM infrastructure.** LLM-based pUIC, RecGPT / Generative Retrieval, and board recs draw on the same LLM inference and serving needs. Consolidation means one investment and one accumulating body of operational lessons.
- **AI-enabled engineering velocity.** Reflex productizes AI-leveraged engineering practice (Pinvestigator, Pinkerton) as internal platform. Every leg adopts it; the vTeam stays small and fast by design.
- **Unified modeling investment across boards and retrieval.** Board-recommendation modeling and retrieval modeling are adjacent disciplines. Locating boards modeling and LWS preranking in one subcharter lets techniques and infrastructure transfer directly.

---

## Key Personnel Considerations

> Dylan-only calibration — strip if the doc travels. Full versions in the 7/24 exec-voice doc; condensed for paste:

**Alim Virani (he/him), incoming EM, Anticipation Modeling.** Motivated by growth into senior leadership and visible team delivery; management instinct (teams that don't depend on him) matches the strong-delegation model this charter needs; strongest people-leadership in the loop. Coaching focus: orienting ambition toward organizational needs first. Set up to drive: focused, deliverable-rich charter — both pUIC experiments land in month one, named senior support around Chuxi's ramp. The initial pod differs modestly from what he heard during closing (senior anchoring); addressed directly in the pre-start call; the Balaji question bears on it.

**Daniel Liu, inherited EM, Retrieval Modeling.** Technical, straightforward, diplomatic, delivers. Explicit that he wants his team on ML modeling work — which is exactly his charter: frontier modeling with a real metric and publication surface. Retains boards, inherits LWS, sheds the retentive-recs portion to Alim at settle. Scope phased deliberately: nothing reshuffles while his team lands; every move framed as scope following people.

**Piyush Maheshwari, retrieval framework anchor (TL).** Deepest retrieval-architecture context in the org; de facto senior TL across CLR, LWS, and UPP. Resolved structurally rather than fragmented: UPP stays central and Piyush anchors it — he owns the foundation the modeling charters consume, a durable senior-TL mandate. UPP single-point-of-failure hedged via Zihao's cross-surface-training ramp.

**Bella Huang, Staff, Generative Retrieval.** Staff anchor for the RecGPT incubation and continuity anchor through the transition; motivated by frontier generative work; clear mandate with explicit graduation criteria.

**Balaji Rengarajan (he/him), Staff, Intelligent Boards.** Senior Staff engineer joining with Curation ML. Two natural placements: platform TL within Retrieval Modeling, or Staff anchor for Anticipation Modeling. Placed inside the observation window, after mapping the inherited workstreams with Daniel; your read valued.

---

## Proposal

### Ownership

> The doc's bracket asks for exactly this framing — accountability on Metrics, 0-to-1, prioritized support, oncall:

Accountability runs along four axes:

1. **Metrics.** Each team carries named business metrics with a single-threaded owner: Alim on retention and fresh-content discovery, Daniel on modeling gains across boards and LWS preranking, my direct pod on Reflex adoption and incubation milestones. No metric has two owners.
2. **0-to-1 initiatives.** Each frontier bet — Reflex, Generative Retrieval, LLM-based pUIC — has a named incubation owner and explicit graduation or sunset criteria. Generative Retrieval is time-boxed with a settle-point review.
3. **Prioritized support for other Pinterest workstreams.** A front-door model gives leadership, partner organizations, and PMs a named owner per domain, so cross-team asks arrive with context and receive a consistent response — the structural resolution of the routing gap Cupcake exposed. It routes asks originating outside the organization; it is not a gate on our own pods.

   | Domain | Front door (EM) | Technical owner |
   |---|---|---|
   | Anticipation / Retentive Recs | Alim | Chuxi (ramping) |
   | Exploration (UEB, Content Exploration) | Alim | Roderick |
   | Generative Retrieval / RecGPT | James (incubation) | Bella |
   | Reflex + AI tooling | James | JJ (Build); Dafang overall |
   | UPP framework (supports CLR + LWS) | James | Piyush |
   | Retrieval Modeling (boards + LWS preranking) | Daniel | boards + LWS TLs |
   | CLR retrieval modeling | James day 1, Alim at settle | Devin |
   | Foundations & Efficiency (responsiveness, L1 utility, cost) | James | JJ · Rui |

4. **Oncall.** Every rotation has a day-one owner and a settle-state owner, with continuous pager coverage guaranteed through the transition. LWS oncall moves with the charter to Daniel on day one; boards oncall remains with Daniel; L1 / Real-Time operations sit with Rui under Foundations & Efficiency; the new pUIC serving surface staffs through a deliberate ramp for the incoming SWE. One deliberate carry-over: I retain Zili's performance management as rotations move, so no incoming EM inherits an open case.

> Optional (Dylan-only): the per-seat direct-pod justification table from the 7/24 doc (JJ / Rui / Alok / Bella / Hanlin / Yuke / Piyush). Also the 7/25 org-proposal additions belong in this section: **per-project EM-POC + TL-POC table** (= Workstreams & Leads below) and a **QC mechanism per workstream** (weekly experiment ledger + pinned priority list — the RecGPT template, generalized to every pod).

### Transition Phase: Early Q3 2026

> Replaces the doc's bracket. Its asks (explicit goals, business continuity, minimizing disruption, stakeholder perspectives, how the EMs are doing, broad charter shape clear now with room for adjustment) map 1:1:

The two reorganizations are deliberately decoupled. Yours moves the org chart: Daniel and his team report to me, and Dhruvil takes the blending team. My internal reorganization runs on its own clock, using the room you gave me to observe before proposing. The three-team structure above is the target state; the broad charter shape is clear today, and the design leaves room for adjustment as the observation window teaches us.

**Initial state — following your announcement and Alim's July 27 start, with minimal reporting-chain changes:** Alim onboards with a nucleus drawn from my current reports (Chuxi, Yidi, Alok, plus Lionel, who started the same day as Alim and joins as a founding member). Zihao remains with me as UPP cross-surface training lead and the succession hedge behind Piyush. Daniel's team remains intact under Daniel. CLR and UPP remain with me, and LWS forms Daniel's natural first ramp, with timing proposed from observation.

**Explicit goals for this phase:**

1. **Business continuity.** Every workstream and every pager keeps a named owner; nothing drops.
2. **Minimal disruption to key initiatives on both teams.** The larger internal moves — CLR toward Alim, the anticipation consolidation, LWS to Daniel — follow the observation window rather than the announcement.
3. **Understanding the inherited scope.** A first-hand read of the Curation ML portfolio and of stakeholder perspectives on what could be improved on that side.
4. **Reading the EMs.** Alim's onboarding trajectory and Daniel's fit with his charter both inform the final structure.

I will bring you the internal reorganization proposal at the close of the observation period, with 30/60/90-day touch points along the way.

### Longer Term: Q4 2026 / Q1 2027

> Replaces the bracket ("possible team setups depending on different outcomes in Q3"). Keep the existing line about direct time on Reflex and UPP — it matches the record.

Team setups resolve on evidence from Q3 rather than on guesses made today:

- **CLR** transitions to Alim at the settle point, where its synergy with Retentive Recs is strongest. It does not go to Daniel — that would overload his onboarding. *Gate: both EMs landed.*
- **UPP** remains with me as the framework the organization consumes, anchored by Piyush.
- **Generative Retrieval** graduates to Anticipation Modeling once incubation criteria are met — the proven gains engine that balances that team's frontier-heavy portfolio.
- **Intelligent Boards** stays with Daniel initially; the deciding signal over the next two months is whether IB gains originate in modeling improvements (stays in Retrieval Modeling) or in surface pairings — notifications, Explore (moves to Anticipation Modeling at settle).
- **Boards modeling depth:** how far Intelligent Boards and Recommend-a-Board grow as a frontier surface under Daniel, and whether boards modeling and LWS preranking share a pod. *Gate: the inherited-scope learning.*
- **Balaji** lands as either Daniel's platform TL or Alim's Staff anchor, decided inside the observation window.
- **Two open requisitions (L15, L13)** remain unallocated until the above resolve, preserving flexibility.
- Post-transition, my own direct time concentrates on two areas: Reflex and UPP.

### Workstreams & Leads

> The doc's bracket asks for "named POCs and team charter for each workstream." The doc's bullet list vs. this table: the doc lists "LWS + L1 Utility (consolidating the scope here)" as one item — they are **separate owners** (LWS → Daniel; L1 Utility → JJ/Rui under Foundations & Efficiency, James-direct). Split the row when pasting.

| Workstream | Team / front door | Technical lead | Evolution |
|---|---|---|---|
| UPP | James | Piyush | The framework supporting CLR + LWS; the organization's unifying retrieval foundation |
| CLR + GULP | James day 1 → Alim at settle | Devin | Frontier retrieval modeling; deliberately excluded from Daniel's day-one load |
| LWS | Daniel | Yali | Lightweight preranking modeling; oncall moves with the charter day one; SM/SL strategic home |
| L1 Utility / Real-Time | James | Rui (ops) · JJ | Consolidated within Foundations & Efficiency |
| Retentive Recs + Unified Explore Backend | Alim | Chuxi (ramping) · Roderick (UEB) | Both pUIC experiments land in month one; UEB consolidates into the anticipation leg |
| Reflex | James | JJ (Build) · Dafang overall | Small vTeam, my primary time; the accelerator every leg adopts |
| RecGPT / Generative Retrieval | James (incubation) | Bella | Time-boxed incubation; graduates to Anticipation Modeling at settle |
| Intelligent Boards | Daniel | Balaji | Frontier boards modeling; placement settles on the gains-origin read (~60 days) |
| Recommended Boards | Daniel | boards TL TBD | Live surfaces (Related Pins, Search) plus frontier boards modeling |
| Foundations & Efficiency (Responsiveness, Cost savings) | James (JJ) | JJ · Rui | ~half of JJ's scope; kept per your guidance against divesting small things |

---

## Not in the photographed doc — add if wanted

**Decisions I need from you** (closes the loop the doc opens; Dylan-only):
1. **Balaji placement** — platform TL under Daniel, or Staff anchor under Alim. Intersects what Alim heard during closing, so your read matters.
2. **Kim's loan to Dhruvil** — wind down so her time returns to this organization; cleanest if you set it up with Dhruvil directly, with the reorg as natural cover.
