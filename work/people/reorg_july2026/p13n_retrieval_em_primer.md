# P13N Retrieval — EM Primer

**From:** James Li · **To:** Daniel Liu, Alim Virani · **Date:** August 2026

This is my read of the organization as it stands: what each workstream is, who is doing what, where I think we are fragile, and what is decided versus genuinely open heading into the end-state design.

It is a starting point, not a finished picture. Some of it is wrong, and the parts about your areas are the parts I am least sure of. I would rather hand you something concrete to correct than a blank page.

---

## 1. The organization at a glance

**Name:** P13N Retrieval. Dhruvil's organization is P13N Ranking. Together we cover personalization for Homefeed and the surfaces built on it.

**Scope, in one sentence:** the pre-ranking funnel end to end — from user signal to what the ranker sees — plus the anticipation modeling built on top of it, including retentive recommendations, predictive user-interest modeling, and boards and exploration ML.

**The boundaries that matter:**
- **Ranking starts where we end.** We decide what candidates exist and which survive to scoring. Dhruvil's org ranks them.
- **Surfaces belong to P13N-Experiences.** We own the models and the retrieval path, not the product surface.
- **ATG** is a research partner across generative retrieval and pUIC, not a delivery dependency we control.

**The three teams as of the August announcement:**

| Team | EM | Center of gravity |
|---|---|---|
| **Retrieval Foundations** | James | The shared substrate every leg builds on — UPP — plus Reflex, the AI-enabled dev-velocity accelerator |
| **Curation ML** | Daniel | Frontier ML modeling across preranking and boards, and publishing |
| **Retrieval Modeling** | Alim | Anticipating what a Pinner wants next: the interests that bring someone back, with content and serving path ready |

**Where confusion reliably happens** — worth naming so we handle it deliberately rather than rediscovering it:
- **UPP is consumed, not shared.** CLR and LWS both build on UPP as a framework. That is a dependency, not joint ownership.
- **The explore→boards path crosses teams.** The pin-level exploration module introduces new concepts to a user; Intelligent Boards is the step that converts introduction into real adoption. They flow into each other and do not currently sit together.
- **Oncall follows the charter, not the reporting line.** LWS and boards paging moved with their charters on day one; L1 and real-time ops sit with Rui under Foundations & Efficiency.
- **Some people work a charter their manager does not hold.** This is real today and is on the list to resolve.

---

## 2. The nine workstreams

### UPP — Unified Personalization Platform
**TL:** Piyush, with Zihao leading cross-surface training. **Role:** substrate.
The shared retrieval framework and personalization backbone. UPP owns the cross-surface user-representation and retrieval substrate that CLR and LWS both consume, so it is built once centrally rather than drifting into variants. Measured on cross-surface adoption and the gains its models deliver on partner surfaces.
**State:** V0 beat the P2P production baseline head-to-head on engagement and successful sessions, with known semantic-relevance regressions we are managing. Launch push is live. V1 needs more time before going online. Search is adopting V0 and has flagged that GPU serving may be hard for them to resource.
**My read on the risk:** the highest-leverage thing we own, and the most externally contested. Delivery risk now sits partly in another org's capacity.

### CLR + GULP
**TL:** Devin, with Yichi; Ryan and Rui joining on the engineering side this half. **Role:** engine.
Frontier retrieval modeling on the main candidate-generation stack, including GPU-served retrieval in production. GULP rides with CLR.
**State:** stable and historically one of our most reliable sources of gains — and **deliberately under-funded in H1** while capacity went to UPP and Retentive Recs. Ryan and Rui come in on engineering tasks this half, likely starting with serving efficiency.
**My read on the risk:** we have been harvesting an engine we stopped investing in. That is a choice with a shelf life.

### LWS + L1 Utility
**TL:** Yali, with Hedi. **Role:** engine.
Lightweight preranking — the reliable gains engine of the org — plus L1 Utility (mid-funnel utility selection: shopping, freshness and safety knobs, diversity controls) and in-session responsiveness. Oncall moved with the charter on day one.
**State:** consistently delivering. GPU serving productionized and stable. Training pipeline re-architected, cutting training time from over forty hours to about seven. The RecSys preranking paper was accepted with an oral. See More / See Less has its retrieval-side home here.
**My read on the risk:** concentration. A great deal of reliable output depends on a small number of people.

### Retentive Recs Retrieval
**TL:** Chuxi. **Role:** bet-heavy.
Retention-optimized recommendations: predict the interests that bring a Pinner back and have the content ready when they arrive. Two predictive user-interest-cluster tracks — model-based and LLM-based — plus the feedback loop.
**State:** a deliberate launch lull with effort concentrated on the two pUIC tracks. Model-based is ahead but carries serving-path debt; the LLM-based track is not performing yet. Both experiments land in the next few weeks.
**My read on the risk:** this leg carries retention, and it has not yet put a win on the board.

### Unified Explore Backend & LLM pUIC
**Anchor:** Roderick, with Lionel ramping as backend partner; Ling contributing. **Role:** bet.
Consolidates the explore surfaces into the anticipation leg, plus the LLM-based user-interest track.
**State:** Lionel is ramping now. Roderick is the technical anchor.
**My read on the risk:** thin coverage on a workstream we are counting on.

### Reflex
**Leads:** Dafang overall, JJ on Build, Tim on product. **Role:** accelerator.
The AI-enabled dev-velocity accelerator — productizing AI-leveraged engineering practice as internal platform that every workstream can adopt. Deliberately a small, nimble team. Measured on adoption and measurable velocity gains.
**State:** funded, with active integration interest from Search. Simulate V0 demo mid-August. Pinvestigator is in regular investigative use.
**My read on the risk:** it needs a visible, working demonstration more than it needs another plan.

### RecGPT / Generative Retrieval
**TL:** Bella, with Hanlin. **Role:** engine.
Generative retrieval in production on Homefeed. **This is a gains-producing engine, not an experiment.** The job now is to raise its share of candidate impressions and make it produce more.
**State:** launched and contributing. Serving migrated to Manas with real cost savings. Candidate budget expanded. An early collaboration is exploring whether a generative model could retrieve and rank in a single pass — genuinely early, and I am not planning around it yet.
**My read on the risk:** its ceiling has been set by impression share more than by model quality. That is a solvable constraint we were slow to attack.

### Intelligent Boards
**TL:** Balaji. **Role:** bet.
The frontier boards bet, funded under the anticipation vision. The thesis is a funnel: the exploration module is top-of-funnel, introducing new concepts to a user; **Intelligent Boards is the mid-funnel step that converts introduction into serious adoption.** Balaji is running a sprint on the initial prototype now.
**State:** flat on top-line metrics for roughly six months, but a recent notification collaboration produced step-change improvements.
**My read on the risk:** we do not yet know whether the upside comes from the boards modeling or from the surface pairing. That question is worth answering deliberately, and I have a read planned.

### Recommended Boards
**TL:** to be determined. **Role:** mature live surface.
Board recommendations serving production traffic on Related Pins and Search, with several small models keeping them alive.
**State:** no metric movement in about six months, and very little top-down pull. Product direction here is genuinely unclear to me.
**My read on the risk:** the honest version is that I am not sure what this should become. I would rather understand it properly before deciding.

---

## 3. Cross-org asks and seams

- **NLFU (New Low Frequency Users)** — supporting a Growth-led effort. Our posture is to fund via named deliverables on existing engines, never ringfenced headcount. Note the authorization for the associated metric trade-off expires end of September.
- **See More / See Less** — a co-ownership seat: Yali on retrieval, Raymond Hsu on the front end, no primary or secondary. High visibility.
- **Content Quality** — appears on the cross-org list; scope and counterpart are still thin. Flagged so it does not ship empty.
- **The UPP ownership seam** — there is an active discussion above us about where the personalization substrate should live. I am handling it; you should know it exists.

---

## 4. Where I think we are fragile

1. **August is compressed.** The announcement, performance delivery, and the design kickoff all stack into three weeks, and most of it routes through me. If something slips, tell me early — there is no slack built in.
2. **Single points of failure with thin hedges.** UPP depends heavily on Piyush. CLR depends heavily on Devin. LWS depends heavily on Yali. We have named backups in each case, but not proven ones.
3. **The anticipation leg has no delivering engine yet.** Retention is the metric it owns, and the first evidence is still ahead of us. That is by design, and it is still a risk.
4. **Parts of Curation ML are unmapped to me.** I do not yet have a clear picture of what Yongwoo, Felix, and Yang are working on, or what they should be. This is the single biggest gap in my understanding of the org, and it is the first thing I want to fix.
5. **Two workstreams have unclear product direction** — Recommended Boards most obviously, and Content Quality.
6. **The exec clocks are real.** Cost savings, GenAI placement, and the NLFU window all run on timelines set outside the team.

---

## 5. What is decided, and what is open

**Decided — not reopening:**
- The interim team structure announced in August, and the current reporting lines.
- Team charter cores: curation quality is Daniel's center of gravity; retentive recommendations is Alim's; UPP and Reflex stay with me.
- The clock: we design the end state together and decide in early November. No ad-hoc structural moves before then.

**Open — this is the agenda:**
- The organizing principle for how the three charters divide.
- Where CLR ends up.
- Where generative retrieval lands.
- Whether Intelligent Boards stays where it is, decided on where its gains actually originate.
- Consolidating the Unified Explore Backend so its charter and its reporting lines agree.
- Balaji's scope.
- The profile of the two open requisitions.
- The remaining reporting lines that sit with me today.

**How I will decide:** on criteria we agree first, not on advocacy. Final calls are mine — what I want from the two of you is aligned principles, your honest read, and disagree-and-commit once we land.

---

## 6. What happens next

| When | What |
|---|---|
| Mid-August | EM staff sync kicks off. We agree decision rights, principles, and what is settled versus open — before we map a single person or project. |
| Mid-August → late September | Each of us gathers evidence in our own areas. Deep dives on the boards workstreams. The first retention results land. |
| Early October | We decide the end state together. |

**What I want from each of you:** tell me where this document is wrong. Mark up your own areas, and mark up mine — you will both see things I cannot. And come to the kickoff with a view on what your team should be famous for by the middle of 2027.

That question is the real one. Everything else is mechanism.
