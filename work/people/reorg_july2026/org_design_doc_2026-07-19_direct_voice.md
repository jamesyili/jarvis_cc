# P13N Retrieval & Anticipation ML — Org Design (Version A: direct)

**July 19, 2026 · James Li · Draft for Dylan**

*Naming note: Anticipation Foundations remains the cross org program name, co owned with partner surfaces. This document names the org.*

## Key Charter Synergies

Merging Curation ML and P13N CG unlocks faster innovation on anticipation and persona based representation, streamlines our modeling efforts, and gives AI enabled dev velocity a dedicated home under Reflex. Cupcake proved this group can execute a complex, cross surface initiative with urgency and quality. It also showed where the cost was: nearly all of the friction we hit was seam friction. Ownership boundaries were in motion, cross team asks had no default path, and decision rights were negotiated mid quarter. The same work surfaced a large amount of common emerging technology that, improved once, benefits every application. This charter removes the unneeded boundaries and consolidates the investment in the common technology.

What the merger buys us:

- End to end backend and ML ownership of anticipation in one team. The boundary we improvised during Cupcake becomes an internal design decision.
- One roadmap and one prioritization surface across anticipation, exploration, boards, and platform, instead of several teams triaging locally.
- Routing and notification norms installed as org policy (see Ownership below) instead of rediscovered each quarter. This is the structural answer to the XFN partnership feedback.
- A small, nimble Reflex vTeam accelerating recsys improvements across every leg.
- Cleaner peer seams with ranking (Dhruvil) and surfaces (Yan), because our side of each seam has one owner.
- Pods that own a Pinner problem end to end, with the decision rights to move on it without cross team permission.

Honest boundary: the cross org seams with Tim and Yan stay cross org and get the notice norms below. What this merger dissolves is the intra anticipation seams, which were the more expensive ones.

## Charter

The org runs three subcharters, all carrying the same topline goals: **SSv2, WAU, and Cost Savings.**

| Subcharter | Scope |
|---|---|
| **Anticipation & Exploration** | pUIC (model based and LLM based), Retentive Recs, Unified Explore Backend |
| **Retrieval Modeling** | Intelligent Boards, Recommended Boards, LWS (lightweight scoring) |
| **UPP & Reflex** | UPP, the shared retrieval framework the modeling charters build on; Reflex and agentic dev velocity; Foundations & Efficiency (responsiveness, L1 utility, cost) |

CLR converges into one of the first two subcharters at the settle point, sized by where headcount lands.

## Clear Outcomes

1. Anticipation has a single point of ownership across ML and backend: one org owns pUIC (model based and LLM based) and its serving path end to end.
2. One prioritized roadmap across anticipation, exploration, boards, and platform.
3. One personalization substrate: CLR and LWS build on UPP rather than maintaining variants that drift apart.
4. One LLM serving investment shared by LLM based pUIC, RecGPT / Generative Retrieval, and board recs.
5. Reflex tooling adopted by every leg, with measured dev velocity gains.
6. Named front doors for partner teams, and no pager gap at any point in the transition.

## Consolidation of Key Technological Investments

Today, anticipation, retentive recs, and intelligent boards advance on parallel, often near duplicate foundations. One org converges the investment:

- **A single personalization backbone.** pUIC, Retentive Recs, and Intelligent Boards depend on the same user representation and retrieval substrate. UPP becomes the shared framework both CLR and LWS build on. We build the substrate once, centrally, and the modeling charters consume it.
- **Shared LLM needs.** LLM based pUIC, RecGPT / Generative Retrieval, and board recs lean on the same LLM inference and serving stack. Consolidated, that is one investment and one set of hard won lessons instead of three.
- **Reflex and AI tooling as a shared accelerator.** One vTeam productizes AI leveraged engineering (Pinvestigator, Pinkerton) as internal platform that every leg adopts.
- **Modeling synergy between board recs and retrieval modeling.** They are close cousins. The Retrieval Modeling subcharter colocates board recs modeling with LWS scoring modeling, so the synergy lives inside one charter instead of across a team seam.

## Additional Design Considerations

Beyond the transition, the design converges to a minimal set of direct reports for me, each seat individually justified (the shape we discussed on 7/7):

- The two standing modeling charters run under Alim and Daniel. They carry the durable business.
- My time goes to Reflex. My direct pod exists to serve that, plus the UPP framework (Piyush) and Foundations & Efficiency (JJ, Rui).
- GenRet is a time boxed incubation under me with sunset criteria. It moves at the settle point, and my direct footprint shrinks as it does.

## Key Personnel Considerations

**Alim Virani (he/him), incoming EM, Anticipation & Exploration.** Alim is motivated by growth into senior leadership and by running a team that visibly delivers. His stated management instinct, make himself unnecessary as fast as possible, fits a strong delegation model, and his people leadership answers were the cleanest of the interview loop. The one thing I am watching: he frames ambition self first, and I will coach it toward org needs first. Setup: a focused, deliverable rich charter on day one, with both pUIC experiments landing inside his first month, and named senior support around Chuxi's ramp (Roderick's seniority, Ling's delivery). One honest gap: the initial pod differs modestly from what he heard while closing, mainly on senior anchoring. I will reset that directly in his pre start call, and Balaji's placement (input ask below) bears on it.

**Daniel Liu, inherited EM, Retrieval Modeling.** Daniel is technical, straightforward, diplomatic, and delivers, and he wants his team on AI and ML modeling work, which is exactly what his charter is: frontier ML modeling that drives metric gains and publishes (KDD, RecSys). He retains his boards surfaces (Recommend a Board, Intelligent Boards) and inherits LWS. He sheds the retentive recs part of his team to Alim at the settle point, so his team consolidates around one coherent modeling charter. Because he is onboarding a whole new org, I am phasing his scope rather than reshuffling everything while his team lands. His motivation is fed by the charter itself. First real conversation happens right after your announcement, with every move framed as scope following people.

**Piyush Maheshwari, retrieval framework anchor (TL).** Piyush is motivated by senior TL scope, and the retrieval architecture is his proving ground. He holds the full retrieval architecture context post Bowen and is effectively the TL of TLs across CLR, LWS, and UPP today. Rather than let the reorg fragment that, I am resolving it by role: UPP stays with me as the org's shared retrieval framework, and Piyush anchors it. He owns the foundation the modeling charters consume, which is a stronger and more durable senior TL story than TL by adjacency. He is the single point of failure on UPP today, so I am hedging with Zihao's ramp on cross surface training.

**Bella Huang, Staff, Generative Retrieval.** Bella is the Staff anchor for the RecGPT / Generative Retrieval incubation and a continuity anchor through the transition. She is motivated by frontier generative work; the incubation gives her a clear mandate with explicit graduation criteria, and her scope grows as the bet matures.

**Balaji Rengarajan (he/him), Staff, Intelligent Boards.** Balaji is the senior Staff engineer on Intelligent Boards, joining with the Curation ML team. Two placements fit: platform TL within Retrieval Modeling, or Staff anchor under Anticipation & Exploration. I will place him inside the observation window, after mapping the inherited workstreams with Daniel; it touches what Alim heard while closing, so your read matters.

## Proposal

### Ownership

Accountability runs along four axes:

1. **Metrics.** Each leg owns named business metrics with a single threaded owner: Alim on retention and fresh content discovery, Daniel on modeling metric gains across boards and LWS scoring, my direct pod on Reflex adoption and GenRet incubation milestones. No metric has two owners.
2. **0 to 1 initiatives.** Reflex, Generative Retrieval, and LLM based pUIC each have a named incubation owner and explicit graduation or sunset criteria, so they do not drift into orphan science projects. GenRet is time boxed with a settle point review.
3. **Prioritized support for other Pinterest workstreams.** A front door model gives you, Andrew's org, and PMs a named owner per domain, so cross team asks land with context instead of being improvised. This is the structural fix for the routing gap Cupcake exposed and for the XFN feedback. It is a routing map for asks originating outside the org, not a gate on our own pods; internally, each pod owns its Pinner problem and moves on it directly.

   | Domain | Front door (EM) | Technical owner |
   |---|---|---|
   | Anticipation / Retentive Recs | Alim | Chuxi (ramping) |
   | Exploration (UEB, Content Exploration) | Alim | Roderick |
   | Generative Retrieval / RecGPT | Me (incubation) | Bella |
   | Reflex + AI tooling | Me | JJ (Build); Dafang overall |
   | UPP framework (supports CLR + LWS) | Me | Piyush |
   | Retrieval Modeling (boards + LWS scoring) | Daniel | boards + LWS TLs |
   | CLR retrieval modeling | Me day 1, Alim at settle | Devin |
   | Foundations & Efficiency (responsiveness, L1 utility, cost) | Me | JJ · Rui |

4. **Oncall.** Every rotation has a day 1 owner and a settle state owner. No pager gap at any point. LWS oncall moves to Daniel on day 1; boards oncall stays with Daniel; L1 / Real Time goes to Rui under Foundations & Efficiency; the new pUIC serving surface staffs with a deliberate ramp for the incoming SWE. One deliberate carry over: I keep Zili's performance management even as rotations move, so no new EM inherits an open case.

**My direct pod, each seat justified:**

| Person | Why they report to me |
|---|---|
| JJ | Reflex Build lead (about half) + Foundations & Efficiency (about half): responsiveness, L1 utility, cost |
| Rui | L1 / Real Time operational owner, under the Foundations & Efficiency charter JJ co owns |
| Alok | Retentive Recs (primary, his own call) + Reflex; load bearing for the RR pod as Yuke moves to RecGPT |
| Bella | Staff lead for the GenRet incubation; continuity through the transition |
| Hanlin | GenRet delivery pair with Bella |
| Yuke | Single RecGPT stream; I hold his management so no new EM starts with an open thread |
| Piyush | UPP, the shared retrieval framework CLR and LWS build on; a standing direct, not transitional |

### Transition Phase: Early Q3 2026

Two decoupled reorgs. Yours comes first and moves the org chart: Daniel and his team report to me, and Dhruvil takes the blending team. My internal reorg runs on my own clock, per the room you gave me to observe and propose separately. The three leg target above is where I am steering; it is not a day one event. The broad charter shape is clear now, and I am leaving room for adjustments.

**Initial state, right after your announcement and Alim's 7/27 start. Minimal reporting chain changes:**

- Alim onboards with a subset of my current reports: Chuxi, Yidi, Alok, plus Lionel, who starts 7/27 with him and becomes a founding member of the pod.
- Zihao stays with me. He leads UPP cross surface training and is the succession hedge behind Piyush.
- Daniel's team stays intact under Daniel. The RR shed and anticipation consolidation come later, out of the observation.
- CLR and UPP stay with me. LWS is Daniel's natural first ramp; I will propose exact timing from the observation.

**Goals for the observation period:**

1. Business continuity: every workstream and pager keeps a named owner, nothing drops.
2. Minimize disruption to key initiatives on both teams: move as little as possible initially; the bigger internal moves (CLR to Alim, anticipation consolidation, LWS to Daniel) come after I have observed.
3. Understand the inherited Curation ML scope, including stakeholder perspectives on what could be improved on that side.
4. Read how the EMs are doing (Alim's onboarding, Daniel's charter fit) before finalizing structure.

I will bring you the internal proposal after the observation period, with 30/60/90 touch points along the way.

### Longer Term: Q4 2026 / Q1 2027

Possible team setups depending on how Q3 resolves:

- **CLR moves to Alim at settle**, given the synergy with Retentive Recs. Not to Daniel; it would overload his onboarding. Gate: both EMs landed, plus the observe read.
- **UPP stays with me** as the framework the org consumes. Piyush anchors. Standing, not transitional.
- **GenRet graduates** to its durable home once incubation criteria are met. Gate: settle point review.
- **Boards modeling depth**: how far Intelligent Boards and Recommend a Board grow as a frontier surface under Daniel, and whether boards modeling shares a pod with LWS scoring. Gate: what I learn from the inherited scope.
- **Balaji** lands as Daniel's platform TL or Alim's Staff anchor. Gate: my first real conversation with Daniel.
- **Two open reqs (L15, L13)** stay unallocated until the observe window resolves the above.

### Workstreams & Leads

| Workstream | Leg / front door | Technical lead | How it evolves |
|---|---|---|---|
| UPP | Me | Piyush | The framework supporting CLR + LWS; stays with me as the unifying retrieval foundation |
| CLR + GULP | Me day 1, Alim at settle | Devin | Frontier retrieval modeling; not added to Daniel's day one load |
| LWS | Daniel | Yali | Lightweight scoring modeling; oncall moves to Daniel day 1 |
| L1 Utility / Real Time | Me | Rui (ops) · JJ | Sits inside Foundations & Efficiency; consolidates the L1 utility scope |
| Retentive Recs + Unified Explore Backend | Alim | Chuxi (ramping) · Roderick (UEB) | Both pUIC experiments land in month one; UEB consolidates into the anticipation leg |
| Reflex | Me | JJ (Build) · Dafang overall | Nimble vTeam; my primary time; the accelerator every leg adopts |
| RecGPT / Generative Retrieval | Me (incubation) | Bella | Time boxed incubation; graduates or moves at settle |
| Intelligent Boards | Daniel | boards TL TBD | Retained; frontier boards modeling, metric gains plus publications |
| Recommended Boards | Daniel | boards TL TBD | Retained; live surfaces plus frontier boards modeling |
| Foundations & Efficiency (Responsiveness, Cost savings) | Me (JJ) | JJ · Rui | About half of JJ's scope, kept per your guidance not to divest the small things |

### Where I want your input

1. **Balaji** (Staff, Daniel's team): platform TL under Daniel, or Staff anchor under Alim? It touches what Alim heard while closing, so your read matters. Default: decide inside the observe window, after my first real conversation with Daniel.
2. **Kim's loan to Dhruvil**: as the reorg settles I want the loan wound down so her time comes back to our side. Cleanest if you set it up with Dhruvil; the reorg gives natural cover.
