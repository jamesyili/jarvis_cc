# P13N Retrieval — EM Primer

**From:** James Li · **To:** Daniel Liu, Alim Virani · **Date:** August 2026

This is my read of the organization as it stands: what each workstream is, who is doing what, where I think we are fragile, and what is decided versus genuinely open heading into the end-state design.

It is a starting point, not a finished picture. Some of it is wrong, and the parts about your areas are the parts I am least sure of. I would rather hand you something concrete to correct than a blank page.

*[Square-bracketed italics are gaps I know about. Part of what our walkthroughs are for.]*

---

## 1. How we'll operate — ground rules for this table

We're basically strangers starting over together, all three of us. That's not a problem to manage; it's the founding condition. These are the rules I want us to run by, starting Monday. Push back on any of them at the table.

**1. First Team.** This table is your first team; your own team is your second. When your team's interest and this table's interest pull apart, we say it here and settle it here — not in the hallway. That means each of us will sometimes carry home a decision our team wouldn't have picked, and own it as ours.

**2. We cut once.** We're in observe mode through the fall. Around November we make the structure calls together, on criteria we agree in advance, and then the structure stands. Moving people between managers is expensive for everyone underneath us; after we settle, it's reserved for serious exceptions. (The interim state stays as announced: a starting state, cheap to adjust. The stability promise attaches to what we settle in November.)

**3. Every team gets a scoreboard, a flag, and its share of the plumbing.** Each team inherits metric goals spanning top-line engagement, retention, and cost; a mission — a year from now, each of these teams is known across Pinterest for something; and org obligations, named explicitly rather than discovered. No team gets to be all-glory or all-plumbing.

**4. We start from strength — and act like it.** This is a high-performing group: end-to-end systems experts, deep modeling experts, and a real IC15/IC14 bench. The obligation that creates is a standing question at this table, every week: who are our best people, what energizes them right now, and what would make them leave?

**5. No ceilings from us on our best people.** Time, opportunities, visibility: my job is to remove every limit that's mine to remove, and to go fight the ones that aren't. The cost we accept: investment follows talent and energy, and the most exciting problems will not be spread evenly.

**6. Decision rights, said once.** Final calls are mine. What I want from this table is your honest reads and disagree-and-commit when we land. We won't re-litigate this.

**7. Nothing leaves this table as a maybe.** While we're building the map — and especially while structure is open — teams hear decisions, from their own manager, with notice. Never scenarios, never previews. That's what makes it safe for the three of us to think out loud in this room.

**8. AI-first operations.** We operate AI-first as a norm, not a slogan: before we add process, meetings, or headcount, the default question is "what does this look like AI-leveraged?" This isn't aspiration — we're already doing it. Reflex is the program-level bet, and PINvestigator and Pinkerton are live examples of engineering leverage in regular use. Daniel's Pin tools are the same pattern from the Curation side. The cost we accept: we spend real time building leverage a quarter-driven team would skip — and all three of us work this way ourselves; it doesn't get delegated downward.

**9. We don't fund everything — because we can't.** That's arithmetic, not philosophy. So we're selective and decisive: fewer things, funded properly, with named owners. And what we don't fund gets an explicit no — said out loud, with a reason — not a slow starvation. The cost we accept: we will decline or kill work that is genuinely good, and we'll own that call rather than letting things die of neglect.

---

## 2. The organization at a glance

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

## 3. The nine workstreams

This is the section I most want you to mark up. For each one: what it is, who's on it, where it stands, how risky it is, what kind of work it is, the politics around it, where AI leverage pays, and what leadership room the space has in it. When I don't know something, I say so.

### UPP — Unified Personalization Platform

UPP is the bet that we build personalization once, centrally, instead of every surface training its own variant. It owns the cross-surface user representation and the retrieval substrate that CLR and LWS consume. If it works, every leg of this org gets faster and cheaper at the same time. That is also why it's the most contested thing we own — when a substrate starts winning, everyone develops an opinion about where it should live.

Where we are: V0 beat the P2P production model head-to-head. SSv2 wins in US and Canada, engagement wins globally. We are not launched. Semantic relevance regressed, and the launch is gated on recovering b2.5pre@4 (organic) to above −0.3% — it sits at −2.17% today. The P2P team is on it: bundling the post-ranking utility relevance change with our experiment, pushing irrelevant pins down per CG, and testing a different sampling scheme in parallel. One to two weeks before we know. The P10 WAU drop is the second blocker. Meanwhile Search is adopting V0 and is worried about GPU capacity on their side. Training time used to be the concern; the V1 improvements made it roughly neutral.

- **Staffing:** Piyush (TL) with Zihao on cross-surface training. Partner side: Yifan Li, Fan Jiang, Jiaxing Qu from P2P — Jiaxing is at 50% and I'm resolving whether that becomes 100% or two people, with Sai Xiao next week. *[Full contributor map: fill in at walkthrough.]*
- **Launch history:** none yet on P2P — V0 is the first launch candidate. *[Experiment-by-experiment history: I'll walk you through it live.]*
- **Risk:** high. Ambitious modeling, contested ownership, and delivery now partly dependent on other orgs' capacity (P2P eng, Search GPUs).
- **Work type:** genuinely both. Deep modeling (cross-surface training in a batch, weighting, loss functions, optimizers) and serious systems work (serving paths, GPU efficiency).
- **Strategic weight:** the highest-leverage thing we own. It's also the org's most visible story upward — treat anything UPP-related as exec-facing by default.
- **Politics:** there's an active discussion above us about where the personalization substrate should live; I'm handling it, but you should know it exists. The launch is deliberately being run through the new decision process as an exemplar, which means the trade-off calls get made above me — that's protection, not exposure, as long as we disclose first. Relevance-side partners (Kurchi's team) are warm as of this week; keep them that way.
- **AI leverage:** *[honest placeholder — the training/eval loop has room for it; I haven't mapped this.]*
- **Leadership runway:** the Search extension is a real second act for whoever drives it, and the cross-org seat on this work is the most visible IC platform in the org.

### CLR + GULP

Frontier retrieval modeling on the main candidate-generation stack, including GPU-served retrieval in production. GULP rides with CLR. This has historically been one of our most reliable sources of gains — and we deliberately under-funded it in H1 while capacity went to UPP and Retentive Recs. We've been harvesting an engine we stopped investing in. That's a choice with a shelf life, and part of why Ryan and Rui come in on the engineering side this half, likely starting with serving efficiency.

- **Staffing:** Devin (TL) with Yichi; Ryan and Rui joining on engineering this half.
- **Launch history:** *[fill in — the CLR launch record is long and I want the walkthrough to do it justice.]*
- **Risk:** low on delivery, real on concentration — too much of it lives in Devin's head.
- **Work type:** deep modeling at the core, with a meaningful GPU-serving systems layer.
- **Strategic weight:** the workhorse of the main stack. Retention of gains here buys us the room to place bets elsewhere.
- **Politics:** quiet today. Its end placement is an open design question, which makes it the workstream most likely to be discussed by people not in this room — rule 7 applies.
- **AI leverage:** *[placeholder — candidate: AI-assisted experiment triage; not mapped.]*
- **Leadership runway:** a TL bench question more than a TL question — who backs Devin up is an org-level gap we've named but not proven.

### LWS + L1 Utility

Lightweight preranking — the reliable gains engine of the org — plus L1 Utility (mid-funnel utility selection: shopping, freshness and safety knobs, diversity controls) and in-session responsiveness. It just keeps delivering: GPU serving productionized and stable, the training pipeline re-architected from forty-plus hours down to about seven, and the preranking paper accepted at RecSys with an oral. See More / See Less has its retrieval-side home here. Oncall moved with the charter on day one.

- **Staffing:** Yali (TL) with Hedi.
- **Launch history:** *[fill in — the H1 record is strong; I want the specifics on paper here.]*
- **Risk:** concentration. A great deal of reliable output depends on two people.
- **Work type:** modeling-led with a solid serving-systems spine.
- **Strategic weight:** the steadiest scoreboard we have, and now a publishing flag too (the RecSys oral).
- **Politics:** See More / See Less is a co-ownership seat with the front end (Yali with Raymond Hsu, no primary or secondary) and it's high-visibility. Success criteria for that seat are still being firmed up — I own that conversation.
- **AI leverage:** *[placeholder.]*
- **Leadership runway:** Hedi is having a real moment (lead author, oral at RecSys). The question of who presents, and how we stage it, is open and worth doing deliberately.

### Retentive Recs Retrieval

Retention-optimized recommendations: predict the interests that bring a Pinner back, and have the content ready when they arrive. Two predictive user-interest tracks — model-based and LLM-based — plus the feedback loop that closes it. We're in a deliberate launch lull while both tracks converge: model-based is ahead but carries serving-path debt; LLM-based isn't performing yet. Both experiments land in the next few weeks. I'll be blunt about the stakes: this leg carries retention, retention is the metric the anticipation vision was funded on, and it has not yet put a win on the board. That's by design. It's still a risk.

- **Staffing:** Chuxi (TL). Alim's pod — Yidi, Alok, Lionel — staffs the surrounding work. On the LLM track, Ling has been critical (she built much of the LLM inferencing pipeline), with Zoudu, and Ru Chen just joined.
- **Launch history:** *[thin by design this half — fill in the pre-lull record.]*
- **Risk:** high, and time-boxed — the next few weeks of experiment results tell us a lot.
- **Work type:** deep modeling, with the LLM track adding a prompt/inference engineering layer.
- **Strategic weight:** this is Alim's charter core and the retention story for the whole org. First evidence here changes every conversation we have upward.
- **Politics:** exec attention on retention is real and personal — results here get read at levels above Dylan. Handle readouts with care: disclose early, frame honestly.
- **AI leverage:** the LLM-pUIC track *is* an AI-leverage bet on the modeling itself.
- **Leadership runway:** Chuxi is TL on the hardest open problem in the org — the support structure around her is something I want this table to own together.

### Unified Explore Backend & LLM pUIC

Consolidating the explore surfaces into the anticipation leg so the charter and the systems agree, plus the LLM-based user-interest track's serving side. Roderick is the technical anchor and has been driving UEB proactively; Lionel is ramping as his backend partner; Ling contributes on the LLM side.

- **Staffing:** Roderick (anchor), Lionel (ramping), Ling (contributing).
- **Launch history:** *[n/a mostly — this is consolidation work; list the milestones instead.]*
- **Risk:** thin coverage on a workstream we're counting on. One senior anchor plus a ramping partner.
- **Work type:** systems-heavy — backend consolidation — with the LLM serving path attached.
- **Strategic weight:** unglamorous and load-bearing: the anticipation leg doesn't scale without it.
- **Politics:** its charter and its reporting lines don't currently agree — that's explicitly on the open list, and until it's resolved this is the workstream where "who decides" questions will surface first.
- **AI leverage:** *[placeholder.]*
- **Leadership runway:** Roderick is exactly the strong IC15 shape we need more of; this space is his to grow in.

### Reflex

The AI-enabled dev-velocity accelerator: productizing AI-leveraged engineering practice as an internal platform every workstream can adopt. Deliberately small and nimble, measured on adoption and measurable velocity gains. This is the program behind ground rule 8 — PINvestigator is already in regular investigative use, Pinkerton is folded in, and Simulate demos mid-August. Search has active integration interest. My honest read: what Reflex needs most right now is a visible, working demonstration — shown, not announced. That's on me to stage.

- **Staffing:** Dafang overall, JJ on Build, Tim on product; Alok owns the Pinkerton line.
- **Launch history:** n/a — adoption milestones are the record here. *[List them: PINvestigator regular use, Pinkerton fold, Simulate V0.]*
- **Risk:** moderate — the risk isn't technical, it's attention. Programs like this die of quiet neglect, not failure.
- **Work type:** systems and platform work, plus the craft of making AI leverage real in day-to-day engineering.
- **Strategic weight:** this is my flag for the org and it stays with me. It's also the thing Dylan named me the EM point-of-contact for — exec visibility is built in.
- **Politics:** we're absorbing Shifu on a strengths framing — Shifu was ahead on Build, Reflex ahead on discovery. Use that framing, always. No spiking the ball; the people involved read everything we say about it.
- **AI leverage:** it *is* the AI-leverage play.
- **Leadership runway:** JJ's Build ownership is a real leadership lane, and every workstream that adopts Reflex creates an adoption-champion role inside it.

### RecGPT / Generative Retrieval

Generative retrieval in production on Homefeed. I want to say this plainly because it gets miscast: this is a gains-producing engine, not an experiment. It launched, it contributes, serving migrated to Manas with real cost savings, and the candidate budget expanded. The job now is to raise its share of candidate impressions and make it produce more — its ceiling so far has been set by impression share, not model quality, and that's a solvable constraint we were slow to attack. There's an early collaboration exploring whether a generative model could retrieve and rank in a single pass; genuinely early, and I'm not planning around it.

- **Staffing:** Bella (TL) with Hanlin.
- **Launch history:** launched and contributing on Homefeed; Manas migration with cost savings; candidate budget expansion. *[Exact gains record: fill in at walkthrough.]*
- **Risk:** low-to-moderate as an engine; the open question is ambition — how hard we push impression share.
- **Work type:** deep modeling, with ATG as the research partner on the frontier end.
- **Strategic weight:** our clearest claim to a Pinterest-leading LLM-era rec stack. It shows up in how this org is described upward.
- **Politics:** ATG collaboration boundary — partner, not dependency. And where GenRet lands at the settle is on the open list; same rule-7 discipline as CLR.
- **AI leverage:** the modeling is the leverage; the interesting second-order question is what the single-pass exploration implies if it works.
- **Leadership runway:** the engine needs a scaling champion, and the landing question means real influence for whoever builds the strongest case with evidence.

### Intelligent Boards

The frontier boards bet, funded under the anticipation vision. The thesis is a funnel: the exploration module is top-of-funnel, introducing new concepts to a user; Intelligent Boards is the mid-funnel step that converts introduction into serious adoption. Balaji is running the dogfooding sprint now and says we'll deliver what we promised roughly on time.

Here's my honest framing of where this really is, and it's sharper than what's usually said in the room: dogfooding polishes design and UX, but it doesn't test the real hypothesis. Nobody seriously doubted an LLM can assemble a decent board. The real questions are whether users click, whether it moves top-line, and whether the Explore funnel gives it enough volume to matter — the Auto Org history (board creation up meaningfully, top-line unmoved) is the cautionary analogue. On top of that, quality currently rides on very long prompt-engineering instructions and big context windows, and we haven't tested open-source models, which are probably the answer on cost. And we have not yet aligned explicit success metrics with Product. That conversation needs to happen before dogfooding momentum hardens into "quality was the goal."

- **Staffing:** Balaji (TL) running the sprint; Amon on prompt/quality work; Ling contributes on the LLM prediction side. *[Full sprint roster: fill in.]*
- **Launch history:** none — pre-launch. Auto Org is the relevant history lesson, not a predecessor.
- **Risk:** high. Classic 0-to-1: unvalidated user hypothesis, volume gated by a funnel we don't fully control, cost model unproven.
- **Work type:** an unusual blend — LLM/prompt engineering, product design judgment, and the systems to serve it. This is the workstream where product taste matters most.
- **Politics:** exec interest in boards runs high, which cuts both ways — attention when it works, scrutiny when it doesn't. The missing Product metrics alignment is the live item.
- **AI leverage:** LLM-native end to end; also the natural place to trial open-source models for cost.
- **Leadership runway:** Balaji is doing genuinely strategic thinking here — the metrics-alignment conversation with Product is a leadership opening, not a chore.

### Recommended Boards

Board recommendations serving production traffic on Related Pins and Search, with several small models keeping them alive — including BoardRanker behind the board-picker API. Top-line hasn't moved in about six months, but a recent notification collaboration produced step-change improvements — which tells me the latent upside is real and it unlocks through surface pairings. Worth knowing: BoardRanker sat untouched for two years until Ling recently found and fixed a major data-pipeline error, and there's an H2 plan behind it now.

I'll say the honest version: I do not yet know what this should become, and product direction here is genuinely unclear to me. I'd rather understand it properly before deciding — this is a walkthrough-week conversation, and Daniel, it's one where I'm mostly listening.

- **Staffing:** TL to be determined. Ling on BoardRanker. *[Who else keeps the lights on: fill in.]*
- **Launch history:** *[fill in — the six-quiet-months story needs its prior history for context, plus the notification-collab numbers.]*
- **Risk:** low operationally, high directionally — a live surface with no agreed future.
- **Work type:** mature ML maintenance today; the upside case (surface pairings) is modeling plus partnership work.
- **Politics:** unclear product direction means unclear sponsorship — the risk isn't interference, it's neglect.
- **AI leverage:** *[placeholder — the two-year-untouched-model story suggests AI-assisted model archaeology could pay here.]*
- **Leadership runway:** an unowned TL seat on a live production surface. For the right person that's a gift.

---

## 4. Cross-org asks and seams

- **NLFU (New Low Frequency Users)** — supporting a Growth-led effort. Our posture is to fund via named deliverables on existing engines, never ringfenced headcount. Note the authorization for the associated metric trade-off expires end of September.
- **See More / See Less** — a co-ownership seat: Yali on retrieval, Raymond Hsu on the front end, no primary or secondary. High visibility.
- **Content Quality** — appears on the cross-org list; scope and counterpart are still thin. Flagged so it does not ship empty.
- **The UPP ownership seam** — there is an active discussion above us about where the personalization substrate should live. I am handling it; you should know it exists.

---

## 5. Where I think we are fragile

1. **August is compressed.** The announcement, performance delivery, and the design kickoff all stack into three weeks, and most of it routes through me. If something slips, tell me early — there is no slack built in.
2. **Single points of failure with thin hedges.** UPP depends heavily on Piyush. CLR depends heavily on Devin. LWS depends heavily on Yali. We have named backups in each case, but not proven ones.
3. **The anticipation leg has no delivering engine yet.** Retention is the metric it owns, and the first evidence is still ahead of us. That is by design, and it is still a risk.
4. **Parts of Curation ML are unmapped to me.** I do not yet have a clear picture of what Yongwoo, Felix, and Yang are working on, or what they should be. This is the single biggest gap in my understanding of the org, and it is the first thing I want to fix.
5. **Two workstreams have unclear product direction** — Recommended Boards most obviously, and Content Quality.
6. **The exec clocks are real.** Cost savings, GenAI placement, and the NLFU window all run on timelines set outside the team.

---

## 6. What is decided, and what is open

**Decided — not reopening:**
- The interim team structure announced in August, and the current reporting lines.
- Team charter cores: curation quality is Daniel's center of gravity; retentive recommendations is Alim's; UPP and Reflex stay with me — and that's an end-state decision, not an interim one. I'm telling you now so nobody spends design cycles on options that aren't real. The why, briefly. UPP: it's a substrate with multiple consumers and an active ownership discussion above us — it has to be neutral ground, not report into one of its customers, and the work right now is mostly managing up and across, which is mine to do. Reflex: Dylan named me the point of contact, and a norm that applies to every team gets sponsored from the level that spans every team. Notice what I kept — the two most contested, least-harvestable things we own; you two inherit the engines and the clean charters. And neither is forever: when UPP is boring and the seam is settled, it's transferable. When Reflex is demonstrated and adopted, it gets a home.
- The clock: we design the end state together and decide around early November. No ad-hoc structural moves before then.

**Open — this is the agenda:**
- The organizing principle for how the three charters divide.
- Where CLR ends up.
- Where generative retrieval lands.
- Whether Intelligent Boards stays where it is, decided on where its gains actually originate.
- Consolidating the Unified Explore Backend so its charter and its reporting lines agree.
- Balaji's scope.
- The profile of the two open requisitions.
- The remaining reporting lines that sit with me today.

How we decide is ground rule 6, and how we talk about it outside the room is ground rule 7. Every project walkthrough ends with the same question — *where does this naturally live, and is that settled or open?* — and the running list we build together is the raw material for November.

---

## 7. What happens next

| When | What |
|---|---|
| Mon 8/10 | First trio meeting: ~20 minutes on the ground rules, then we start the walkthroughs. |
| Weeks of 8/10 + 8/17 | My scope, project by project — I drive. Alim owns the running onboarding artifact: questions, follow-ups, and the settled/open tags as we go. |
| Week of 8/24 | Daniel's scope — Daniel drives, same format. (And Alim is in Palo Alto that week; the three of us should get a meal.) |
| Sept → late October | Steady state: each of us gathers evidence in our own areas. Deep dives on the boards workstreams. The first retention results land. |
| ~Early November | We decide the end state together. |

**What I want from each of you:** tell me where this document is wrong. Mark up your own areas, and mark up mine — you will both see things I cannot. And come Monday with a view on one question: what should your team be famous for by the middle of 2027?

That question is the real one. Everything else is mechanism.
