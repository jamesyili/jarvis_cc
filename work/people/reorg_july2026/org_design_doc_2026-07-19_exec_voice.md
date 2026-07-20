# P13N Retrieval & Anticipation ML — Org Design (Version B: executive)

**July 19, 2026 · James Li · Draft for Dylan**

*Naming note: Anticipation Foundations remains the cross org program name, co owned with partner surfaces. This document names the org and its structure.*

## Key Charter Synergies

Personalization at Pinterest is moving from reactive recommendation toward anticipation: modeling what a Pinner wants next and having the content and serving path ready when they arrive. That shift is currently executed across two organizations. Merging Curation ML and P13N CG puts the full anticipation stack, from user signal to what the ranker sees, under one mandate, and it does so at the moment the work most needs it.

Anticipation Cupcake demonstrated that this group can deliver a complex, cross surface initiative with urgency and quality. It also gave us a precise read on where execution cost lives. The friction we absorbed was not a talent problem; it was structural. Ownership boundaries were being negotiated while we shipped, cross team asks had no default routing, and decision rights were settled conversation by conversation. At the same time, the joint work revealed how much emerging technology these teams hold in common: technology that, improved once, benefits every application.

This merger converts cross org negotiation into intra org design. Specifically, it:

- Consolidates end to end backend and ML ownership of anticipation into a single cohesive team, and empowers strong technical leads to grow under one mandate.
- Establishes one roadmap and one prioritization surface across anticipation, exploration, boards, and platform.
- Institutionalizes routing, notification, and notice norms as organizational policy, the durable answer to the cross functional partnership feedback.
- Maintains a dedicated Reflex vTeam that accelerates recsys engineering across every workstream, growing our engineers' range in the process.
- Strengthens the peer contracts with ranking and with surfaces, because our side of each seam now has a single accountable owner.

One boundary worth stating plainly: the cross org seams with Tim's and Yan's organizations remain cross org, governed by the notice norms below. What this merger dissolves is the internal anticipation seams, which have been the more expensive ones.

## Clear Outcomes

1. A single point of ownership for anticipation across ML and backend: pUIC, model based and LLM based, and its serving path are owned end to end by one organization.
2. One prioritized roadmap spanning anticipation, exploration, boards, and platform.
3. One personalization substrate: CLR and LWS build on UPP rather than maintaining divergent variants.
4. One consolidated LLM serving investment across LLM based pUIC, RecGPT / Generative Retrieval, and board recs.
5. Reflex tooling adopted across every workstream, with dev velocity gains we can measure.
6. Named front doors for every partner organization, and continuous pager coverage throughout the transition.

## Consolidation of Key Technological Investments

Across P13N today, anticipation, retentive recs, and intelligent boards are advancing on parallel and often duplicative foundations. A single organization allows us to converge that investment along four lines:

- **A single personalization backbone.** Anticipation, Retentive Recs, and Intelligent Boards increasingly depend on the same user representation and retrieval substrate. UPP becomes the shared framework on which CLR and LWS both build. The substrate is built once, owned centrally, and consumed by the modeling charters, rather than maintained as variants that drift apart.
- **Shared LLM infrastructure.** LLM based pUIC, RecGPT / Generative Retrieval, and board recs draw on the same LLM inference and serving needs. Consolidation means one investment and one accumulating body of operational lessons.
- **AI enabled engineering velocity.** Reflex productizes AI leveraged engineering practice (Pinvestigator, Pinkerton) as internal platform. Every leg of the organization adopts it; the vTeam stays small and fast by design.
- **Unified modeling investment across boards and retrieval.** Board recommendation modeling and retrieval modeling are adjacent disciplines. Locating boards modeling and LWS scoring modeling in one charter lets the techniques and infrastructure transfer directly.

## Additional Design Considerations

Beyond the transition phase, the organization converges to a deliberately minimal set of direct reports for me, each individually justified. The durable business runs through the two standing modeling charters under Alim and Daniel. My own time concentrates on Reflex, with a direct pod scoped to serve exactly three things: the Reflex frontier, the UPP framework the org builds on, and Foundations & Efficiency. Generative Retrieval remains a time boxed incubation with explicit sunset criteria; as it graduates, my direct footprint shrinks further. The end state is a lean span held for clear reasons, not a wide span held indefinitely.

## Key Personnel Considerations

**Alim Virani (he/him), incoming EM, Anticipation & Exploration.** Alim is motivated by growth into senior leadership and by visible team delivery. His management instinct, building teams that do not depend on him, matches the strong delegation model this charter needs, and his people leadership was the strongest in our interview loop. My coaching focus will be orienting his ambition toward organizational needs first. I am setting him up with a focused, deliverable rich charter from day one: both pUIC experiments land within his first month, with named senior support surrounding Chuxi's ramp. The initial pod differs modestly from what he heard during closing, primarily on senior anchoring; I will address that directly in his pre start call, and the Balaji question below bears on it.

**Daniel Liu, inherited EM, Scoring & Boards Modeling.** Daniel is technical, straightforward, diplomatic, and delivers. He has been explicit that he wants his team on ML modeling work, and that is precisely his charter: frontier modeling that drives metric gains and publishes at venues like KDD and RecSys. He retains his boards surfaces, inherits LWS, and at the settle point sheds the retentive recs portion of his team to Alim, consolidating around one coherent modeling charter. Because he is onboarding an entire organization, his scope is phased deliberately; nothing is reshuffled while his team is landing. My first substantive conversation with him follows your announcement, and every subsequent move is framed as scope following people.

**Piyush Maheshwari, retrieval framework anchor (TL).** Piyush holds the deepest retrieval architecture context in the organization and today operates as the de facto senior TL across CLR, LWS, and UPP. The reorg could have fragmented that role; instead the design resolves it structurally. UPP remains with me as the organization's shared retrieval framework, and Piyush anchors it: he owns the foundation the modeling charters consume, a durable senior TL mandate rather than influence by adjacency. He is currently a single point of failure on UPP, which I am hedging through Zihao's ramp on cross surface training.

## Proposal

### Ownership

Accountability is assigned along four axes:

1. **Metrics.** Each leg carries named business metrics with a single threaded owner: Alim on retention and fresh content discovery, Daniel on modeling gains across boards and LWS scoring, my direct pod on Reflex adoption and incubation milestones. No metric has two owners.
2. **0 to 1 initiatives.** Each frontier bet, Reflex, Generative Retrieval, and LLM based pUIC, has a named incubation owner and explicit graduation or sunset criteria. Generative Retrieval is time boxed with a settle point review.
3. **Prioritized support for other Pinterest workstreams.** A front door model gives leadership, partner organizations, and PMs a named owner per domain, so cross team asks arrive with context and receive a consistent response. This is the structural resolution of the routing gap Cupcake exposed.

   | Domain | Front door (EM) | Technical owner |
   |---|---|---|
   | Anticipation / Retentive Recs | Alim | Chuxi (ramping) |
   | Exploration (UEB, Content Exploration) | Alim | Roderick |
   | Generative Retrieval / RecGPT | James (incubation) | Bella |
   | Reflex + AI tooling | James | JJ (Build); Dafang overall |
   | UPP framework (supports CLR + LWS) | James | Piyush |
   | Boards + LWS scoring modeling | Daniel | boards + LWS TLs |
   | CLR retrieval modeling | James day 1, Alim at settle | Devin |
   | Foundations & Efficiency (responsiveness, L1 utility, cost) | James | JJ · Rui |

4. **Oncall.** Every rotation has a day one owner and a settle state owner, with continuous pager coverage guaranteed through the transition. LWS oncall moves with the charter to Daniel on day one; boards oncall remains with Daniel; L1 / Real Time operations sit with Rui under Foundations & Efficiency; the new pUIC serving surface staffs through a deliberate ramp for the incoming SWE. One deliberate carry over: I retain Zili's performance management as rotations move, so no incoming EM inherits an open case.

**The direct pod, each seat justified:**

| Person | Rationale |
|---|---|
| JJ | Reflex Build lead (roughly half) and Foundations & Efficiency (roughly half): responsiveness, L1 utility, cost |
| Rui | L1 / Real Time operational owner within the Foundations & Efficiency charter |
| Alok | Retentive Recs (primary, at his request) and Reflex; load bearing for the RR pod as Yuke concentrates on RecGPT |
| Bella | Staff lead for the Generative Retrieval incubation; continuity through the transition |
| Hanlin | Generative Retrieval delivery pair with Bella |
| Yuke | Single RecGPT stream; management continuity through the transition |
| Piyush | UPP, the shared retrieval framework; a standing direct, not a transitional one |

### Transition Phase: Early Q3 2026

The two reorganizations are deliberately decoupled. Yours moves the org chart: Daniel and his team report to me, and Dhruvil takes the blending team. My internal reorganization runs on its own clock, using the room you gave me to observe before proposing. The three leg structure above is the target state; the broad charter shape is clear today, and the design leaves room for adjustment as the observation window teaches us.

**Initial state, following your announcement and Alim's July 27 start, with minimal reporting chain changes:** Alim onboards with a nucleus drawn from my current reports (Chuxi, Yidi, Alok, plus Lionel, who starts the same day and joins as a founding member). Zihao remains with me as UPP cross surface training lead and the succession hedge behind Piyush. Daniel's team remains intact under Daniel. CLR and UPP remain with me, and LWS forms Daniel's natural first ramp, with timing proposed from observation.

**Explicit goals for this phase:**

1. **Business continuity.** Every workstream and every pager keeps a named owner; nothing drops.
2. **Minimal disruption to key initiatives on both teams.** The larger internal moves, CLR toward Alim, the anticipation consolidation, LWS to Daniel, follow the observation window rather than the announcement.
3. **Understanding the inherited scope.** I want a first hand read of the Curation ML portfolio and of stakeholder perspectives on what could be improved on that side.
4. **Reading the EMs.** Alim's onboarding trajectory and Daniel's fit with his charter both inform the final structure.

I will bring you the internal reorganization proposal at the close of the observation period, with 30, 60, and 90 day touch points along the way.

### Longer Term: Q4 2026 / Q1 2027

Team setups will resolve on evidence from Q3 rather than on guesses made today:

- **CLR** transitions to Alim at the settle point, where its synergy with Retentive Recs is strongest. It does not go to Daniel; that would overload his onboarding. Gate: both EMs landed.
- **UPP** remains with me as the framework the organization consumes, anchored by Piyush.
- **Generative Retrieval** graduates to its durable home once incubation criteria are met.
- **Boards modeling depth**: how far Intelligent Boards and Recommend a Board grow as a frontier surface under Daniel, and whether boards modeling and LWS scoring share a pod. Gate: the inherited scope learning above.
- **Balaji** lands as either Daniel's platform TL or Alim's Staff anchor, decided inside the observation window.
- **Two open requisitions (L15, L13)** remain unallocated until the above resolve, preserving flexibility.

### Workstreams & Leads

| Workstream | Leg / front door | Technical lead | Evolution |
|---|---|---|---|
| UPP | James | Piyush | The framework supporting CLR + LWS; the organization's unifying retrieval foundation |
| CLR + GULP | James day 1, Alim at settle | Devin | Frontier retrieval modeling; deliberately excluded from Daniel's day one load |
| LWS | Daniel | Yali | Lightweight scoring modeling; oncall moves with the charter on day one |
| L1 Utility / Real Time | James | Rui (ops) · JJ | Consolidated within Foundations & Efficiency |
| Retentive Recs + Unified Explore Backend | Alim | Chuxi (ramping) · Roderick (UEB) | Both pUIC experiments land in month one; UEB consolidates into the anticipation leg |
| Reflex | James | JJ (Build) · Dafang overall | Small vTeam, my primary time; the accelerator every leg adopts |
| RecGPT / Generative Retrieval | James (incubation) | Bella | Time boxed incubation; graduates at the settle point |
| Intelligent Boards | Daniel | boards TL TBD | Retained; frontier boards modeling with metric and publication surface |
| Recommended Boards | Daniel | boards TL TBD | Retained; live surfaces plus frontier boards modeling |
| Foundations & Efficiency (Responsiveness, Cost savings) | James (JJ) | JJ · Rui | Roughly half of JJ's scope, retained per your guidance against divesting small things |

### Where I would value your input

1. **Balaji placement**: platform TL under Daniel, or Staff anchor under Alim. This intersects with what Alim heard during closing, so your read matters. Default is to decide inside the observation window, after my first substantive conversation with Daniel.
2. **Kim's loan to Dhruvil**: as the reorganization settles, I would like the loan wound down so her time returns to this organization. This lands cleanest if you set it up with Dhruvil directly; the reorg provides natural cover.
