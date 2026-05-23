# Dylan Team-Design Input — Director-Path Chapter (May 2026)

**Status:** Active — drafting James's input back to Dylan on team setup. Dylan is in the design phase, already gave heads-up to stakeholders, asked James for input. Decision window open but closing once charters lock.
**Started:** 2026-05-19 (post-H1 career convo)
**Anchor file:** [H1_career_convo.md](../H1_career_convo.md) — pre-convo prep; this file is the post-convo continuation
**Draft artifact:** [dylan_team_design_artifact_draft_v1.md](dylan_team_design_artifact_draft_v1.md) — the 1-2 page input doc for Dylan, derived from this chapter's analysis
**Cross-refs:** [dylan_archive.md](dylan_archive.md), [dylan_1on1_log.md](dylan_1on1_log.md), `work+self/projects/reflex/reflex_pinkerton_strategy_051626.md`, `work+self/projects/reflex/reflex_pinkerton_interface_design_051626.md`

---

## 2026-05-23 Update — Anna + Tim convos + revised preferred shape (READ THIS FIRST)

**Major refinement to Scenario E based on two stakeholder conversations + Slack-verified org chart.** Artifact v1 below now requires substantive rewrite to reflect this — flagged but not yet executed (next-session work).

### Anna conversation (PM, Recsplanations / Anticipation)

Anna confirmed: **she's not opposed to James working on anticipation front-end experience right now. She thinks there's scope here.** This unblocks the "I own end-to-end" language in the artifact — the Recsplanations-maturity probe lands in James's favor.

### Broader anticipation UX convergence (not just Anna)

The current anticipation UX affordances:
1. **Explore module** — new module in home feed; the "explanation" work (Recsplanations branding internally)
2. **Intelligent Boards effort** — new boards
3. **Interest exploration** — pin-level within home feed

**Convergence everyone is recognizing:** UIC (signal) + pUIC (prediction) become the *single substrate* powering ALL three affordances. UIC is the unified user-state representation; pUIC is the anticipation mechanism. The Explore module, IB, and Interest exploration all consume from this single pipe.

**Director-narrative implication:** James's team builds the substrate (UIC + pUIC) that powers all anticipation UX surfaces. That's not "James owns one thing under anticipation" — that's "James owns the model layer that the entire anticipation product depends on." Architecturally central, business-critical, AI-leveraged, leveraged-through-others.

### Tim conversation (presentation EM, currently reports directly to Dylan)

**Tim owns BOTH ngAPI backend AND Android/iOS client engineering** (not just frontend as prior org map suggested). Verified via Slack org chart 5/23 — Tim is L16 (Manager II), direct report to Dylan.

Tim's observations:
- **His backend engineers have too little scope** — stuck on ngAPI only.
- **Natural scope extension** for them: Unity layer, where James's engineers have the most knowledge.
- **Client engineering has a lot of legacy code** and is hard to make progress on.

James's read on Tim's points:
- Backend engineers extending into Unity = good org move; strengthens that linkage.
- **Client engineering: firm NO.** Doesn't make sense unless James takes Tim entirely AND grows client scope — but that breaks the natural Yan pull on presentation. Not interested, doesn't need it for Director, "not what I'm signing up for." Closed.

### Slack-verified org chart (2026-05-23 screenshots)

**Dylan Wang's 8 direct reports:**
| # | Person | Title | Level | Notes |
|---|---|---|---|---|
| 1 | Dhruvil Deven Badani | Sr. Manager, ML | L17 | Ranking / foundations |
| 2 | Olafur Gudmundsson | Sr. Staff ML Eng | IC line | Direct to Dylan |
| 3 | Dafang He | Sr. Staff ML Eng | IC line | Direct to Dylan |
| 4 | Francisco Navarrete | Sr. Manager, Eng | L17 | Exiting to Kurchi |
| 5 | Yan Li | Sr. Manager, Eng | L17 | P13N |
| 6 | Tim Leung | Manager II, Eng | **L16** | **Presentation broadly: ngAPI + Android/iOS client.** Reports directly to Dylan (currently — not under Yan). |
| 7 | James Li | Sr. Manager, ML | L17 | CG |
| 8 | Rahul Goutam | Manager II, ML | L16 | Blending. (Surname corrected from earlier "Goldam" to "Goutam" per Slack.) |

**Yan Li's team has 2 named sub-EMs** (verified):
- **Daniel Liu** — Manager II, ML Engineering (L16). 8 directs: Kim Toy, Yang Liu, Yongwoo Noh, Ling Lan, Balaji Rengarajan (Staff), Felix Yang, Roderick Gao, Rita Lyu (intern). **NOT under ATG — under Yan.** His team works WITH James's team and WITH ATG team on UIC/pUIC pipeline. James's read: "barely helping" on the substrate build itself.
- **Edward Zhuang** — Manager I, Eng (L15). 7 directs: Josh Arriola, Jiaqi Tong, Tianhao Shen, Allen Pan, Yutong Jin, Yash Patil, Sreesha Venkat. All SWE — backend pool.

**Critical name correction (2026-05-23):** Daniel Liu is the real name — NOT Daniel Lu. Previous Leo sessions scrubbed this backwards. All live files now corrected.

### James's revised preferred shape (today's read)

**Three-EM peer L17 split with coherent verticals:**

| EM | Owns | Notes |
|---|---|---|
| **James** | ML/AI personalization platform (CG + Anticipation + RR + UIC/pUIC + LWS + UPP cross-surface) + **Daniel Liu's ML team consolidated in** + Recsplanations / Explore module / IB / Interest exploration ML-product surfaces (end-to-end) | Gives up: some SWE-heavy scope TBD which |
| **Yan** (he/him) | **Unity ownership + PWT (Pinner Wait Time) + latency + Tim reports to him** (so Yan owns ngAPI backend + Android/iOS client + Unity through Tim, plus PWT/latency as his own vertical). May absorb some of James's SWE-heavy scope. | Substantial scope expansion in a different domain (presentation + performance, not ML) |
| **Dhruvil** | Foundations + ranking (unchanged) | Clean Director-track peer shape |
| **Francisco** | Exiting to Kurchi (unchanged) | — |

**What changes from artifact v1 Scenario E:**
- **Tim's reporting line moves** from Dylan direct → under Yan
- **Daniel Liu's ML team** (8 ppl) consolidates into James
- **Edward Zhuang's team** — likely stays under Yan as backend support for his PWT/latency/Unity vertical, OR partial absorption into James for Unity SWE work (TBD — depends on what "SWE-heavy scope" James gives up)
- **Client engineering** explicitly stays with Yan (via Tim), NOT with James

### Strategic strengths of this shape

1. **Each EM has a coherent vertical** — no territorial overlap, no scope ambiguity.
2. **AI/ML personalization is the high-energy, highest-leverage vertical** — James is the natural owner given Anticipation foundations + UIC/pUIC + cross-surface UPP + Recsplanations + 5 launches in past 6 months.
3. **Yan's vertical (presentation + performance) is critical infrastructure** — PWT/latency are user-facing business outcomes, not "frontend support." This is a meaningful scope, not a consolation prize.
4. **Anna confirmed** Recsplanations product maturity supports "James owns end-to-end" framing.
5. **Convergence-on-UIC-as-single-substrate** is the killer pitch — *"My team builds the model layer that all three anticipation UX surfaces depend on."*

### Open strategic questions / load-bearing variables

(Dylan asked what JAMES wants. Yan/Tim acceptance is Dylan's problem to navigate, not James's pre-validation work. The questions below are about *James's own preference clarity*, not org-feasibility hedging.)

1. **What SWE-heavy scope does James give up?** Open variable — could be Edward Zhuang's team, could be specific Unity workstreams currently under James, could be something else. Affects sizing and what James's headcount footprint looks like in the proposal.
2. **Daniel Liu consolidation — full or partial?** Does Daniel Liu himself move under James as a sub-EM? Does the whole 8-person team come? Or does James cherry-pick certain workstreams/people?
3. **Does the "give up some SWE scope" leave James with enough headcount for the AI Tooling / Pinkerton org-level investment?** The 4-6 engineers AI-Leveraged Engineering charter ask from artifact v1 may need refresh based on what gets traded.
4. **Pronoun cleanup needed:** Yan uses he/him (corrected 5/23) — scrub any remaining "her/she" references in chapter + artifact files.

### Next steps for artifact v1 rewrite

The artifact at [dylan_team_design_artifact_draft_v1.md](dylan_team_design_artifact_draft_v1.md) needs substantive update to reflect:
- Three-EM peer L17 split as recommended shape (replacing Scenario E framing)
- Daniel Liu name (already auto-corrected in this session)
- Tim's actual scope + proposed reporting move under Yan
- UIC + pUIC as single substrate convergence point
- Anna-confirmed Recsplanations maturity supporting end-to-end ownership claim
- Refined headcount ask (post-SWE-trade)
- Updated open variables (LWS + Blending + SWE-trade-question)

**Recommend NOT auto-rewriting until James directs.** This is substantive proposal work; James leading the next iteration.

---

## 2026-05-23 PM — Three Shapes framing + honest "end-to-end" check + Dylan-signal read

After the morning's "revised preferred shape" exploration, the pathfinding converged on a sharper framing: **three plausible shapes that all contain the locked spine**, differing only on the add-on James takes. Then a deeper honest check on what "end-to-end" actually means without Tim's team. Then a read on what Dylan is actually signaling vs. what James might be tempted to propose.

### The Three Shapes (locked spine + add-on)

**Locked spine across all three shapes:**
- CG modeling core (CLR, LWS, UPP cross-surface, RecGPT, adjacent CGs)
- Anticipation Foundations (UIC, pUIC, Feedback Loop)
- Reflex AI (at minimum a small wedge — 2 ML + 2-3 Backend SWE)
- Daniel Liu's 8-person ML team consolidated under James

**Give-ups (locked across all three):**
- ML in Front → Dhruvil's team (they're dominating; clean handoff)
- GULP → Dhruvil's team (Devin gets a new role)
- Client engineering: firm NO at any depth
- Ranking + Blending → stay with Dhruvil

**Shape 1 — Anticipation Product Owner.** Add Anticipation UX surfaces (Recsplanations module / Explore module / IB / Interest Exploration). Anna green-lit. Story: *"I own the anticipation outcome end-to-end — ML substrate + product direction + cross-team orchestration."*

**Shape 2 — Cross-Org Platform Lead.** Add formal cross-org UPP charter (Search / P2P / Ads / T&S) + Notification personalization scope pull-in. Story: *"I'm the cross-org AI personalization platform Director — surfaces consume from us by design."*

**Shape 3 — AI-Leveraged Engineering Director.** Add big Reflex investment (10+ engineers via Rajat, formal AI-Leveraged Engineering org). Story: *"I lead Pinterest's AI tooling capability — compounds across engineering org-wide."*

The three shapes map roughly to Dylan's three named angles in the H1 convo (product/PM, eng foundations, infra+AI).

### Honest "end-to-end" check — Shape 1 caveat

The Anticipation stack, layer by layer:

| Layer | Owner |
|---|---|
| Data + foundation models (OmniSage, CLIP, multimodal) | ATG / Faisal |
| CG retrieval (CLR), UIC, pUIC, Feedback Loop, RR bandit | **James** |
| L2 ranking, blending | Dhruvil |
| **ngAPI serving** (model outputs → client) | **Tim's backend engineers** |
| **Client rendering** (Recsplanations mini-grid, Explore module UI, IB module UI, Interest Exploration UI on Android/iOS) | **Tim's client engineers** |
| Design | Mira |
| PM | Anna |

**Without Tim's team, James owns substrate-to-API-output. He does NOT own the actual pixels-on-the-phone-screen.** "End-to-end" as originally written in Shape 1 overclaims by collapsing the last two layers.

What James can legitimately claim:
- "End-to-end ML/AI ownership of anticipation" ✓ true
- "End-to-end product strategy for anticipation" ✓ true (with Anna)
- "End-to-end *engineering* ownership of anticipation" ✗ false without Tim's team
- "End-to-end *outcome* ownership of anticipation" ✓ true if framed as Director-altitude (orchestrate outcomes, partner across teams; don't conflate with maximizing direct headcount)

**The honest Shape 1 framing:** *"I own the anticipation outcome end-to-end — ML substrate + product direction + design partnership + cross-team execution including Tim's client engineers as explicit partners (not reports)."*

This is Director-altitude framing — owning the outcome, orchestrating the partnerships — not engineering-headcount maximization. It requires explicitly naming Tim's team as a partner in the artifact, not implying absorption.

### Read on what Dylan is actually signaling

Pulling from the H1 convo transcript:

| Dylan signal | Read |
|---|---|
| *"End-to-end experiences in this area are where I see you shine a lot"* | Direct signal toward Shape 1 territory (the experience, not just substrate) |
| *"AI, for sure, is something I'm very passionate about. I do want to double down on that"* | AI as the differentiating theme — pulls toward Shape 1 OR Shape 3 |
| *"UPP is great and we are already strong in that"* | UPP is locked in / not the differentiator — **Shape 2 is probably NOT what she's pointing at** |
| *"I'm trying to think of whether I should try to react on the presentation side"* | She's thinking about the presentation problem as *hers*, not handing it to James. Yan + Tim reshape is her org-design problem to solve in parallel. |
| *"Selfishly I want to give you a path forward"* | Actively designing for James to land Director-shaped scope |

**Read:** Dylan wants James to own **the AI-driven anticipation user-experience outcome**, with AI as the differentiating capability, leveraging UPP as backbone (not centerpiece), and presentation-side execution accessible via Tim's team as a partner (not under James).

Pattern: Dylan owns the *what* (AI doubling-down + anticipation experiences are the bet). She invites James to own the *how* (ML substrate + product direction + cross-team orchestration). She solves the presentation-side org problem in parallel (likely Yan + Tim consolidating), so Tim's team is accessible to James via partnership, not under his tree.

### The two-variant move — revised

If Dylan's signal read is correct, the two shapes she's pointing at are **Shape 1 + Shape 3** — both AI-themed, neither requiring James to take client engineering.

**Shape 2 (Cross-Org Platform Lead) becomes the WRONG one to present.** She explicitly said UPP is "already strong" — translating that into "let me formally lead UPP cross-org expansion" reads as a James-want, not a Dylan-signal-read. UPP cross-surface expansion happens implicitly through the locked spine; the formal cross-org charter is over-pitching scope she hasn't signaled hunger for.

**Recommended pairing for the artifact:**
- **Primary recommendation: Shape 1 (reframed honestly as Anticipation Outcome Owner)**
- **Alternative: Shape 3 (AI-Leveraged Engineering Director)**

Both contain AI. Both align with Dylan's named themes. Shape 1 maps to "end-to-end experiences" + "presentation side" angles. Shape 3 maps to "infra + AI" angle. Together they show James has thought across the angles Dylan herself named.

### Open: what does "predict where AI/personalization is going" actually mean for these two shapes

The Director-altitude framing James wants is "I saw this coming," not "this is what I want." For the artifact rewrite, each shape's pitch should include the *predictive vision* claim that demonstrates James saw where things were heading:

- **Shape 1 predictive claim:** UIC + pUIC become the single substrate powering ALL anticipation UX surfaces — this convergence is happening now, the org needs single ownership of the substrate AND the experiences it powers, or fragmentation continues. *"The model layer and the experience layer are converging into one architecture; without unified ownership, every surface re-solves the same problem."*
- **Shape 3 predictive claim:** AI-leveraged engineering is going to reshape how every engineering org operates within 2-3 years. Pinterest needs a foundational capability that compounds across engineering — not a feature, a substrate. *"The teams that have a real AI-leveraged engineering capability in 2027 will outpace those that treat AI as a tool. We need to build that capability now, with Reflex as the seed."*

Both predictive claims need sharpening — they're directionally right but not yet sentence-level deployable.

---

## What this file is

The H1 career conversation with Dylan happened (week of 5/20 window). She opened the team-design door: she's actively designing the next charter, already given heads-up to stakeholders, and asked James for input — preferences, energy reads, secondary-scope candidates, and scope outside his current team he'd be interested in.

This file is the working artifact for James's response. It captures:
1. The cleaned transcript of the convo
2. Signals extracted
3. Dylan's three explicit questions James owes input on
4. James's current scope inventory (HF CG Next 6 months) + clarifications
5. Energy reads (in progress)
6. Strategic framing for the response
7. Open questions / next moves

---

## Cleaned transcript (Dylan ↔ James, H1 career convo)

> **Dylan:** Even I'm thinking about the kind of team setup and everything. I would love to understand from your perspective. Of course we're going to have the CG team with the modeling team but I do want to give you a path and I do want to make sure that we structure the team in a way that aligns with business. You will be helpful to let me know. This is very early and we are still toying around with different ideas and your kind of preferences. Let's say if you are, I think there are a few different directions I'm thinking about. For you I can see that you are really good in terms of utilizing and building a relationship with the product side. That's one angle we can do. The other angle is about, let's say, the engineering foundations and also all the platform initiatives. Another angle is in terms of other things, like Infra as well as AI. Those are two leads, so those are different angles.
>
> I don't think it would be great to actually stuff everything all in one place because that's going to stretch too many things. It will be helpful at least for you to let me know what are the specific things besides you that you are getting the most energy or learnings from in the short term. At the same time we can enable business and strong talents. That's where my head is. Thank you.
>
> **James:** Sorry just to clarify this more though because I'm not sure I understand the full implications of a lot of these, so is it possible to give a little more details on how some of this will work? Just put it more transparently but between us.
>
> **Dylan:** I'm trying to think of whether I should try to react on the presentation side. Part of the reason is that it will be more efficient from a product strategy and business alignment perspective. The other part is that selfishly I just want to make sure that I provide you a path forward. I do want to make sure that is happening hopefully in the short term and I already gave some heads up to some stakeholders so I'm making my way through it.
>
> At the same time it might be helpful because I don't want to have anything that I find out is structured. I think it's good but then the people who are on the ground don't like it at all so that would actually be defeating the purpose. It is kind of letting me know that I cannot guarantee it's going to happen for sure the way you want but at least getting your input will help me understand and inform my decision.
>
> **James:** What kind of parameters will be helpful for you? What kind of input would be helpful? The projects or directions and also your current scope.
>
> **Dylan:** What are the things you think are secondary to you that you want to actually potentially trim down? What scope would you actually be interested in that is not exactly under your team? Those are the types of questions I'm trying to think through.
>
> I don't think that we need to make a decision now but give it some thought. In our future one we can talk more about it. Also the one surprise kind of feedback will influence your judgment but I do think that you have been a tremendous partner, especially with some of those experience initiatives. End-to-end experiences in this area are where I see you shine a lot and AI, for sure, is something I'm very passionate about. I do want to double down on that. UPP is great and we are already strong in that and I feel like we can definitely make tremendous progress over there. It reflects the future not only for us but also for Pinterest. I think that is also another angle of it but then again don't let my feedback influence what you actually want to achieve three or five years from now. It is very important. The focus area. I also don't think it would be a great idea to just put everything in a very very thin team because that would actually stretch you as a team. Let's figure out what makes sense or not. Things can always move around, like projects, etc., but once we set up team charters and everything, you will be stable for a while.
>
> Try to list out the business, the components, and the needs, and I map the team first. Then of course there are a few strong people I really really want to map to, and then I put those in, but the rest of them are, I would say, a secondary effect. We could not say that, okay, because this person has been managing this person for so long, they're going together or that. Those are things that are kind of nice to have but not my principles.

### Growth Areas section

> **Dylan (on "walking on eggshells" perception):** For that one I do suggest that if you have good trust with some people, at least getting their transparent perspective will be very helpful. Often times it's also just perceived as whether it is enough, kind of support and trust in the past, and then people are just making some assumptions. In general of course I felt like this area would be helpful to do it but then also not the cause of the projects or progress, right? Often times people really appreciate you being very transparent and having very direct decision-making, which is great.
>
> I think we need to find the balance over the years. In general I also want to see if that's something you perceive that you are actually applying pressure in those conditions or you felt like it was a surprise on your end and you didn't say or do anything differently. It's definitely a surprise and I think it's more how I say things rather than any intent. I think for example the one tactic you gave me was really helpful, which is labeling my intent upfront, like "Here's what I'm trying to do." That was actually really helpful because what I've noticed is that people at least understand what I'm trying to do, they understand where I'm at, and they're not taken off guard, like "Why is...?" People have different ways of communicating. Some people calibrate differently so you can't cater to everyone. At least for the people I work closely with and some of the high performers I want to make sure we have a good alignment.
>
> **James:** I kind of hear you. I'm not sacrificing effectiveness or anything like that in doing this so I'm just trying to find ways. If you're not hearing anything, that's fine. The two examples I'm thinking about:
> 1. With Matthew I think there was a little bit of that. I think things are great now between us and myself and Matthew and the team in general.
> 2. Really with some of the newer PMs but I think we've also smoothed things over there.
>
> I'm going to go check in with Yali after this whole cupcake thing, see how she's doing, but let me know if you hear anything else. Appreciate it.

### Building relationships

> **Dylan (Faisal):** It's very important for him to be looked in especially also because he has quite strong opinions for projects like NPP etc., which is great.
>
> **Dylan (Manu):** Another person I'm trying to actually also continue building some new relationship with is Manu. He actually presents a lot in terms of how the team is doing, making decisions, etc. He has a very strong opinion coming from a good place and that's someone that I am trying to, over time, see how we can actually get and facilitate each other.
>
> **Dylan (Shipeng, Tom, Ryan):** Shipeng, of course, it's been great for me. Everything's great with the girls' team, both Shipeng and Tom. We have very regular things with each other and the same thing with Ryan and everyone. I got most of the people covered so that's what I mean. It doesn't mean that you don't need to build a relationship. It just means that you don't have to do it for me because at this point I care more about how you and the team develop. Of course I won't make the off look good but I felt like there's so much great work coming from you and the team. I don't have to go like a salesperson so if you have specific priorities you think make sense, right, so definitely go for it.
>
> **Dylan (Roger et al.):** Roger and all those people, I have regular check-ins with them. They come to me with different asks so I don't have too many concerns. If you are curious and thinking there are certain parts where the person can benefit from building a relationship, please do that. Yeah I'd be more than happy to build a bridge.
>
> **James:** Thank you. Yeah let me think about this a bit more. I think we collaborate very closely with the signal team, so Bo Zhao and Faisal. This is a great area. They also seem to be quite invested in the AI space. That's another opportunity on the ad side. I just don't have much visibility, honestly, and I don't know the usefulness of establishing this yet. You let me know.
>
> **Dylan (ads side):** It's not very productive. Their retrieval stack is very different. I've actually talked to a few people there. I know a few people personally. Their retrieval stack and infra are very different and there are legacy reasons why they're not migrating off that infra. That's another reason. If we really want to do stuff there, it's not just talking. You have to make stuff happen so it's going to be hard and it's going to be solving their problem that's not necessarily helping ours necessarily. That's just another thing I felt very weird about the ad for. That's why I suggest proceeding with caution. Whenever you reach out to them about certain things, they feel very defensive. If they're a new year and come up with something, they reach out to you, which is much much easier organically.
>
> If there are people on your team with hidden points and then for them I'm talking to a young town this afternoon and then having them propose the ideas and effort in some reaching to the manager is actually much more productive. I just don't know any really high-performing and no ender and my managers met, except something left. Yeah so there was a point where I'm at, let's just wait for the dust to all settle. If you do have something, this thing, connections, or some people you thought could be useful connections, that's what we do. Go but I don't suggest spending time with them too much right now. Make sense?
>
> **James:** Thank you. Appreciate those are my two growth areas I was thinking about. Let me know if you see others that I should be focusing on as well.
>
> **Dylan (endorsement):** Let's say if you're going for your career here, we would need someone to endorse you. To think about that as well so I think joining is great. Also if you started building relationships, that's great but then at least two people from the [garbled] side would be very helpful to sponsor your career, probably, as I'm not concerned so it's just about the [garbled] side. Got it, makes sense. Yeah yeah, cool, thank you.

### Pinterest leaders thesis question

> **James:** Maybe the next topic is I would love to hear your perspective on what Pinterest needs in the next set of leaders. Where are we going? Do we still want leaders who are mostly leading a very large team of people or is it that we're also moving into a world where leaders are more expected to be more influential on the technical side? That means, do we still consider a more traditional path or is it more something that's evolving in your opinion?
>
> **Dylan:** I think it's definitely evolving. I mean anyone who said that working with actually continuing to do the anti-building, having managers the same way as they've performed in the past, will be blindfolded. The people who are overseas right now, whether they have enough judgment to say that the new persons out of themselves are performing and then they will half down now, but that can say it doesn't mean that you should put yourself in your lower bar. Usually evolving itself then, if the pressure is coming from, let's say, the new person in your team, the new year in your team, it is extremely important that person very much knows what the future looks like. He's there just to stay in the past, right? I've seen that happening even in my own home so this is important that we have the kind of excitement and passion about where the world is heading.
>
> **Dylan (sponsor builds):** It's very important for you to build connection with Jeff, as I mentioned. If there are other dogged points you think can be helpful, actually meeting with Faisal tomorrow. If you want, I can definitely drop him a line for you. If you don't mind Faisal is very busy, very busy for obvious reasons. There are so many build escalations or trust and safety and everything but it doesn't occur.
>
> **James:** Yes. I'll connect with I think Qinglong is his delegate for some of this ML stuff so I'll connect with him beforehand. I would love to kind of connect with Faisal at some point. I was planning on doing that after I come back from vacation but you let me know.

---

## Signals extracted

1. **Dylan is designing, not exploring.** She's already given heads-up to stakeholders. Decision window open but closing once team charters lock — *"once we set up team charters and everything, you will be stable for a while."*

2. **The fork — three angles named:**
   - **(a) Product side** — leaning into PM relationships
   - **(b) Engineering foundations + platform**
   - **(c) Infra + AI**
   - **Her lean:** presentation side with AI doubling-down. Evidence: *"react on the presentation side"*, *"end-to-end experiences are where I see you shine"*, *"AI is something I'm very passionate about — I want to double down. UPP is great."*

3. **Load-bearing line: sponsorship in motion.** *"Selfishly I just want to make sure that I provide you a path forward... I already gave some heads up to some stakeholders so I'm making my way through it."* Dylan is structuring the org partly to create James's Director runway. She named it explicitly.

4. **Implicit endorsement of the AI-leveraged-leader thesis.** Pinterest-next-leaders question → Dylan: managers performing as before will be *"blindfolded"*; future leaders must *"know what the future looks like"* with *"excitement and passion about where the world is heading."* This maps directly onto James's 5/16 Accelerator commitment (Reflex+Pinkerton as AI-leveraged-leader proof). Strongest direct-from-Dylan validation of the thesis to date.

5. **Walking-on-eggshells got soft-landed.** Dylan owns it as *"how I say things, not intent."* James's *"label your intent upfront"* tactic was the operationally useful give. Matthew resolved, newer PMs smoothed, Dylan checking with Yali. She's asking James to keep flagging, not to fix her.

6. **Sponsorship architecture concrete:**
   - Build connection with **Jeff** (re-emphasized)
   - **Faisal** — Dylan offering to drop a line; James planning post-vacation timing; Qinglong as ML delegate (intermediate step)
   - Dylan referenced "two people from [garbled] side" as endorsement model — garbled term, not actionable as a category; see *Sponsorship architecture (James's read, 2026-05-20)* below for the concrete two-sponsor plan.

7. **Subtractive reads (what Dylan is NOT asking):**
   - Not asking James to fix her eggshells
   - Not asking James to chase ads-side connections (explicit *"proceed with caution"* — Bo Zhao / Faisal-ads-side path is low ROI right now)
   - Not asking James to do peer-relationship salesperson work for her — *"I got most of the people covered... if you have specific priorities you think make sense, definitely go for it"*

---

## Names + ambiguities

| Heard / transcribed | Resolved as | Notes |
|---|---|---|
| "Father" | **Faisal** | Confirmed by James 2026-05-19 |
| "Nannu" | **Manu** | Cleaned transcript |
| "Shigong" | **Shipeng** | Cleaned transcript |
| "Bowen" | **Bo Zhao** | Cleaned transcript; signal-team peer |
| "react on the presentation side" | **Unresolved** | Could mean "respond to / make a move on" presentation side. Either way: Dylan is considering a presentation-side play that involves James. |
| "[garbled] side" (endorsement context) | **Garbled transcription, not a meaningful category** | James confirmed 2026-05-20: garbled transcription, not a real Pinterest division. Removed from forward analysis. See *Sponsorship architecture* section for the concrete two-sponsor plan. |
| "young town" (in ads-side discussion) | **Unresolved** | Likely a person's name, but unclear; context is Dylan talking to "a young town this afternoon" about ads-side outreach. Skip unless it matters. |

---

## Dylan's three explicit questions to James

| # | Question | Answer status |
|---|---|---|
| Q1 | *"What are the specific things besides you that you are getting the most energy or learnings from in the short term?"* | **In progress** — working through energy reads of current scope |
| Q2 | *"What are the things you think are secondary to you that you want to actually potentially trim down?"* | **Partially answered** by Proposed Cuts table (see below). May need to layer energy reads on top — some current "0% SSv2" rows might be cuttable but high-energy (or vice versa). |
| Q3 | *"What scope would you actually be interested in that is not exactly under your team?"* | **Not yet answered** — this is the wildcard. Dylan literally gave permission to name outside-scope. Sponsorship-coded invitation. |

---

## HF CG Next 6 Months (verbatim from James 2026-05-19)

Prioritized by business value. Headcount in parens shows allocation %.

| Area | People | Projects | Expected SSv2 | Notes |
|------|--------|----------|---------------|-------|
| **UPP** | Piyush Maheshwari, Zihao Chen (50%), Ryan Kam (very new, 50%) | Extend to Notif (almost done); Extend to P2P; Infra | 0% | Stretched; non-trivial; requires IC15+ deeply familiar with stack |
| **RecGPT** | Bella Huang (80%), Hanlin Lu, Chuxi Wang (50%), Yuke Yan (30%) | User Profile features; RecGPT with SID | +0.5% | Good-sized investment. Promising gains post-v1, Manas migration, recent diversity gains |
| **Retentive Recs / Anticipation** | Yuke Yan (60%), Chuxi Wang (50%), Yidi Wang (50%) | UIC improvements; pUIC model-based; pUIC LLM-based; CG quota tuning; ramping P13N up on RR; Unity to be used in Intelligent Boards; exploration module | +0.4% (base); +0.6% (+1 eng); +0.8% (+2 eng) | Ideally +2 MLEs for both Anticipation vision and SSv2 gains |
| **HF CLR** | Devin Kreuzer (80%), Yichi Wang (joining June 15) | FM (almost done, +0.2% SSv2); 16k for Retrieval; SearchSage CLR Feature adoption; OmniSage v2; board sequence features | +0.3% (base); +0.6% (+1 eng) | Ideally 1 more MLE for gains |
| **LWS** | Yali Bian (80%), Hedi Xia (80%), Zili Li | Foundation Model; Unimpressed Data Iterations; LWS Data pipeline re-design | +0.5% (base); +0.8% (+1 eng) | Many promising things recently unlocked. Ideally 1 more MLE |
| **L1 Utility** | J.J. Hu (50%), Ray Wang (joining June 1) | Pinnability last batch efficiency; Shopping CLR update | +0.2% | |
| **Dynamic Triggering** | Alok Malik (50%) | All organic CG dynamic tuning model | +0.2% | |
| **Responsiveness** | J.J. Hu (50%) | IPFY and PinCLR adopting in-session signals; onboarding subchunk new CG; working with ranking folks to adopt in-session signals | +0.3% | |
| **AI Tooling / General dev velocity** | J.J. Hu (20%), Alok Malik (50%), Chuxi Wang (20%) | **Reflex, Pinkerton, Pinvestigator** | +0.1-0.2% (already showing from initial PRs) — AND multiplier on every other row's velocity over 12-24 months | Initial PRs already producing gains. Accelerator well-staffed at current size. |
| **Content Exploration / MDD** | Bella Huang (20%), Zihao Chen (40%), Yidi Wang (50%) | Content exploration corpus embedding & serving infra; cross-surface exploration corpus exp | 0% | |
| **Multi-embedding** | Yuke Yan (10%) | Roll out GPU migration to save costs | +0% | |
| **GULP** | Devin Kreuzer (10%), Ryan Kam (very new, 50%) | Debugging Notif Landing Page; logging; consulting; investigations | 0% | |
| **Growth / LFU** | Zihao Chen (10%), Chuxi Wang (10%) | Helping Activation team (3 MLEs onboarding) | 0% | |

**Note:** Doc previously listed "Pinsight" in the AI Tooling row — corrected to **Pinkerton** per 5/16 rebrand.

### Proposed Cuts (to refocus on SSv2 gains)

| Area | Current allocation | Proposed | Net flow |
|------|-------------------|----------|----------|
| Content Exploration / MDD | Bella (20%), Zihao (40%), Yidi (50%) | Bella (20%) only | Zihao → UPP or CLR; Yidi → Anticipation. Delivery funnel is becoming self-serve, so other teams can take this with senior-engineer consultation. |
| Multi-embedding | Yuke (10%) | None | Yuke → Anticipation (no further iteration planned on Multi-embedding) |
| GULP | Devin (10%), Ryan (50%) | Devin (10%) | Aligned with Matt Chun: Devin stays for consultation/direction; Ryan → UPP Infra or LWS Infra |
| Growth / LFU | Zihao (10%) | None (?) | Unclear if cuttable given Growth priorities; if cut → senior engineer focus on UPP |

**Open allocation decisions ("or" placements):** Zihao → UPP **or** CLR; Ryan → UPP Infra **or** LWS Infra. Status: TBD (asked James 2026-05-19, not yet resolved.)

### Clarifications James added on the inventory (2026-05-19)

- **Reflex is already producing measurable SSv2** (0.1-0.2% range from initial PRs). The "+0.1% ???" in the original doc undersold it. Real position: *Accelerator is BOTH near-term SSv2 driver AND multiplier on every other row's velocity over 12-24 months.* This row needs reframing before going to Dylan — drop the question marks, lead with conviction.
- **Don't over-index on incremental-HC SSv2 math.** Numbers are prioritization signal, not precise plans.
- **UPP at 0% SSv2** = platform extension work (Notif, P2P, infra). UPP value lands downstream through Anticipation, RecGPT, etc. Not a real-zero, an attribution-zero.
- **Yichi (CLR, June 15) and Ray (L1 Utility, June 1) confirmed inbound.**
- **Accelerator is well-staffed at current ~0.9 FTE.** Bottleneck isn't headcount.

---

## Energy reads (locked 2026-05-19)

Per Dylan's Q1: where is the energy *real*, *forced*, or *plateauing into maintenance*?

| Grade | Areas | Rationale |
|---|---|---|
| **HIGH** | Anticipation, AI Tooling (Reflex/Pinkerton), LWS, **UPP**, **HF CLR**, **RecGPT** | The strategic stack. James pushed UPP/CLR/RecGPT up from STEADY — these are not grinding extensions, they're still architecturally generative for him. |
| **MEDIUM** | L1 Utility | Some pull but not focus-tier. |
| **STEADY** | Responsiveness, **Multi-embedding** (deprecating via Rec-GBT) | Multi-embedding is STEADY-but-cutting because Rec-GBT is the successor; not energy-driven cut. |
| **LOW** | Dynamic Triggering, Content Exploration / MDD, GULP, Growth / LFU | Metric-grinding or low-leverage. |

### Key observation: energy is broadly distributed

**6 HIGH-energy areas, not 1-3.** James's energy is *not* concentrated. Dylan said *"I don't think it would be a great idea to just put everything in a very very thin team because that would actually stretch you as a team... Let's figure out what makes sense or not."* That's a constraint: 6 HIGH areas cannot all live under one focused charter.

### Clustering of HIGH-energy areas against Dylan's three angles

**Tagging each HIGH area by ML vs AI** (see [[feedback-ai-vs-ml-distinction]] — these are distinct categories in Dylan's framing):

| Area | ML or AI | Dylan's angle |
|---|---|---|
| Anticipation / Retentive Recs | ML (recsys) | (b) ML foundations |
| UPP | ML platform | (b) ML foundations |
| HF CLR | ML (retrieval) | (b) ML foundations |
| LWS | ML (lightweight scoring) | (b) ML foundations |
| RecGPT | **AI** (GenAI for recs) | (c) Infra + AI |
| AI Tooling (Reflex / Pinkerton) | **AI** (AI-leveraged dev / agentic substrate) | (c) Infra + AI |

| Dylan's angle | HIGH areas | Notes |
|---|---|---|
| **(a) Product side / PM relationships** | — | None of the HIGH areas are PM-relationship-coded. |
| **(b) ML foundations / platform** | Anticipation, UPP, CLR, LWS | 4 of 6 HIGH areas. The ML platform doubling-down Dylan named (*"UPP is great"*) sits here. |
| **(c) Infra + AI** | RecGPT, AI Tooling (Reflex/Pinkerton) | 2 of 6 HIGH areas. Dylan's *"AI is something I'm passionate about — I want to double down"* signal. |

**Important distinction (caught by James 2026-05-19):** AI ≠ ML. Dylan's "AI doubling-down" is not generic endorsement of all of James's scope — it's specific to AI-coded areas (RecGPT, Reflex/Pinkerton). Her "UPP is great" is a separate ML-platform endorsement. Two distinct doubling-downs, not one.

### What "AI" means in Dylan's frame (James's weighting, 2026-05-19)

| Reading of "AI" | Weight | Notes |
|---|---|---|
| **(a) AI-leveraged dev tooling / agentic systems** (Reflex, Pinkerton, Pinvestigator, AI-leveraged engineering org-wide) | **Primary** | Direct match to James's Accelerator commitment; gains showing |
| **(c) LLM-powered surfaces / agentic experiences** (conversational discovery, agentic boards, AI-native UI) | **Small** | This is where the presentation-side door opens — AI surfaces are user-facing |
| **(b) GenAI for recs / product features** (RecGPT, generative retrieval, AI shopping) | **Smaller** | RecGPT already in scope |

### Operating constraints (locked 2026-05-19)

- **No direct ask to Dylan about her optimization frame.** James decided against this for now. Work from available signals + James's read; revisit "ask Dylan directly" later if needed.
- **Triangulation channel:** existing context files + James's read + Leo synthesis. Not external stakeholder probes for this phase.

**Strategic tension:** James's HIGH-energy clusters into angles (b) + (c). Dylan's lean is presentation side (closest to angle (a), product-coded). The doors don't align cleanly.

### What "presentation side" actually means (James's read, 2026-05-19)

**Per James's understanding:** Dylan's "presentation side" = **UX + Android/iOS client engineering**. Not late-stage ranking. Not AI-leveraged surfaces. Literal client/UI teams.

**James's honest reaction:**
- Far from current skill set
- Doesn't derive much energy from client/UX leadership
- Open to it *only if it's the only path to grow* — *"that's also something I should know"*
- Open strategic question: *"Why would Dylan want an ML/backend EM to look into a UX team? Sure, she has more people there."*

### Three resolutions (revised)

| Resolution | What you say to Dylan | Risk |
|---|---|---|
| **1. Decline presentation-side path** | "My energy and the Director-caliber bet sit in foundations + AI. Pure UX/client scope is dilution from where I'm strongest." | You decline the door Dylan is holding open. Reads as not-leaning-forward. Director runway narrows if foundations+AI doesn't itself create a Director charter. |
| **2. Accept UX scope as-is** | "I'll take UX/client charter for the broader scope." | Skill-mismatch energy drain. Stretches team thin (Dylan's explicit warning). Doesn't compound with existing AI/foundations bet. |
| **3. AI-leveraged full-stack wedge** *(James's proposal)* | "Anticipation-end-to-end as the wedge — own a small slice of UX through that surface. Long-run: not managing pure iOS/Android engineers, but **full-stack engineers traversing iOS + backend + ML**. AI-leveraged client engineering as the team shape." | Requires Dylan to have authority + appetite to create a charter that doesn't currently exist. Requires team-shape rebuild over time (hire/grow full-stack-AI engineers). Other UX EMs may resist losing engineers to a re-shaped charter. |

### Why James's counter (Resolution 3) is structurally interesting

- **Anticipation is already e2e-coded** — recommends pins → user renders + engages → loop closes. Owning Anticipation-end-to-end means already owning a slice of UX surface logic.
- **Reflex/Pinkerton's diagnostic substrate is cross-surface** — Pinkerton already sees what users experience. The UX layer is downstream of the substrate James is building.
- **Director-altitude charter that doesn't yet exist at Pinterest** — the AI-leveraged full-stack EM. If James can articulate it, it could be Pinterest's first one (and his Director case).
- **Maps to Dylan's signal** — *"end-to-end experiences are where you shine"* + *"AI is something I'm passionate about — I want to double down"*. The full-stack-AI shape is the most coherent read of those two endorsements combined.
- **Doesn't ask James to be a UX expert** — asks him to lead an AI-leveraged team that includes UX engineers. The leverage is in the *team shape*, not in James's personal UI expertise.

### Dylan's current org (revised per James 2026-05-19)

**James's narrower picture** (updates organization.md which was last refreshed 2026-04-01):

| EM | Scope | ~Reports | Composition / Notes |
|---|---|---|---|
| **James Li** | HF Candidate Generation (ML) | 17 | Current home |
| **Dhruvil Deven Badani** | HF Ranking (ML) | ~25 | ML — peer; "also being set up for success" (James) |
| **Rahul Goldam** | HF Blending | ~7 | Direct report to Dylan per James 2026-05-19 (org map had him under Dhruvil — likely stale or recent change) |
| **Yan Li** | P13N-Experiences | ~30 | Composite team: Daniel Liu's ML sub-team (~8) + Edward's backend sub-team (~5) + Android/iOS engineers (remainder) |
| **Tim Leung** | Frontend / Client | ~11-12 | 2-3 full-stack + some backend + rest iOS/Android (mostly mobile) |
| **Francisco Navarrete** | Labeling/Platform | ~16 | **Trajectory: moving to Krishna's org** (Dylan agreed; pending) — see decision filter below |
| Olafur Gudmundsson | IC, Sr. Staff MLE | — | — |

### James's framing (verbatim)

> *"I'm being set up for success, and so is Dhruvil. I obviously don't know."*

→ James's assumption, not verified intel. Treat as a working hypothesis that Dylan is structuring the org such that her strong ML EMs (at minimum James + Dhruvil) get strong charters — not just James-as-special-case. **But do not treat Dhruvil's expansion as known.**

### Dylan's decision filter (from 5/7 DM thread on Francisco's labeling team)

Dylan made her org-shaping filter explicit when Kurchi proposed moving Francisco's labeling team to her org:

> *"Well it's fine, I don't feel this worth my energy anyway. I will just give to her and let her have fun."*
> *"I am just cleaning up debt. What's the point us owning it. You never hear anything about it in anticipation."*
> *"Business wise it makes sense."*
> *"I haven't discussed with Francisco and team. I'm sure this wouldn't be great."*

**Filter: anticipation-relevance + business sense.** She gives up scope that doesn't connect to anticipation/SSv2/business priorities (Francisco's labeling team). She fights for scope that does (Sophia backfill same week — escalated to Rajat with risk callouts). She prioritizes business sense over peer-EM preferences ("Francisco wouldn't be great" but she does it anyway).

**Implication:** Her presentation-side suggestion for James will also pass through this filter. Whatever scope ends up under James must be **anticipation/SSv2/business-relevant**, not just "more reports." That's a sharper constraint than I was holding.

### Structural observations

1. **ML-side EMs Dylan is investing in:** James (CG), Dhruvil (Ranking), Rahul (Blending). Three ML/backend leaders — the recsys stack end-to-end (retrieve → rank → blend).
2. **Eng/UX side EMs:** Yan, Tim. Francisco is on the way out (to Krishna's org).
3. **Yan's team is composite** — not "frontend + 6 ML" as organization.md said, but Daniel Liu (8 ML) + Edward (5 backend) + Android/iOS engineers. Possibly the 5/15 Yan/IB ML redeployment intel refers to Daniel Liu's sub-team — **needs verification, not assumption.**
4. **Tim's team is mostly mobile** (iOS/Android) with some full-stack/backend.

### Possible sources of presentation-side scope (hypotheses, not predictions)

Holding these loosely. None of these are "the read" — they're variants to keep live as evidence accumulates.

| Hypothesis | What it would look like | What would need to be true |
|---|---|---|
| H1: Yan's UX side consolidates under James | If Daniel Liu's ML sub-team (~8) redeploys to CG/Ranking per 5/15 intel, Yan retains Edward's backend (~5) + Android/iOS — James could absorb part or whole | Yan/IB redeployment paperwork lands; Yan's own trajectory clarifies; Edward + Android/iOS people are anticipation-relevant per Dylan's filter |
| H2: Tim's team partially consolidates under James | Tim's 11-12 (mostly mobile) gets restructured; James absorbs the full-stack/backend slice; Tim either reports to James or pure-mobile team stays separate | Dylan sees Tim's current shape as not anticipation-relevant in current form; James proposes a reshape that IS |
| H3: A new full-stack-AI charter is created | Slice of Yan + Tim + James's current CG, re-shaped into AI-leveraged client + ML team | Dylan has authority + appetite to create a charter type that doesn't exist at Pinterest today; speculative |
| H4: Cross-org consolidation with Karina/Kaanon | Rajat-level reorg merges AI initiatives across Dylan + Karina + Kaanon orgs | Rajat-level decision; cross-VP politics; outside Dylan's unilateral authority |
| H5: Something else entirely | Dylan has a frame Leo hasn't surfaced yet | — |

**Dylan's anticipation-relevance + business-sense filter applies to all of these.** Whatever scope ends up under James must clear that filter, which means UX/client work that's *connected to anticipation/SSv2 outcomes*, not UX/client work in general.

### Re-anchor on 5/15 Yan/IB intel — what we know vs. don't

**Known:** Yan's ML engineers possibly being redeployed onto James's + Dhruvil's projects per Andrew thinking — *paperwork prepared, not yet approved* (5/15 high-fragility, no propagation).

**Don't know yet:**
- Whether "Yan/IB ML engineers" specifically means Daniel Liu's ~8-person sub-team or some other subset
- Whether the paperwork has progressed since 5/15
- Whether Yan stays as EM post-redeployment, moves laterally, gets promoted, or exits
- Whether Yan herself has been told yet

Treat these as open variables. The H1 hypothesis above depends on multiple of these landing a specific way. **Hold loosely.**

### Krishna Kamath cautionary check

The empirical Pinterest pattern is: **failed promo → timeline pushed → scope rebalanced away → flight.** Krishna's SSJ Platform charter ("connective tissue for experience and relevance teams") is the warning.

**James's situation is structurally different** — Dylan's sponsorship signal is loud, work + numbers are strong, signals are pulling-toward not pushing-away, NO failed-promo precursor. But the guardrail still applies: if the proposed charter ever starts to feel like "connective tissue" without a real metric/business spine, push back.

### Critical upstream uncertainty: what is Dylan optimizing for?

Until this is resolved, James can't choose between resolutions confidently. Three candidate readings:

| # | Dylan is optimizing for | Best-fit resolution | Evidence |
|---|---|---|---|
| (i) | **UX EM gap** — too many UX/client teams, not enough strong EMs there. Needs someone to absorb. | Resolution 2 (accept as-is) | *"She has more people there"* (James) |
| (ii) | **Director runway construction** — give James broader scope to qualify for Director. UX = "broader" without crossing other VPs. | Resolution 3 (AI-leveraged hybrid) might land; or Resolution 2 might satisfy | *"Selfishly I want to give you a path forward"* + *"I already gave heads-up to stakeholders"* |
| (iii) | **AI-first reorg** — consolidate AI investment under James as AI-leveraged-leader bet. Presentation = where AI lands for the user. | Resolution 3 (AI-leveraged hybrid) | *"AI is something I'm passionate about — I want to double down"* + *"end-to-end experiences are where you shine"* |

**Status:** Locked energy grading. Strategic-tension fork mapped. Upstream optimization question OPEN.

---

## Strategic framing for the response

**Operating principle:** *Org-needs frame first, genuine preference underneath.* See [feedback_org_needs_frame.md](../../../.claude/projects/-Users-jamesli-code-leo/memory/feedback_org_needs_frame.md) (memory).

The response must do **both**:
- **Wrapper (org-needs):** What is the business needing in the next 18 months? Where does James's shape serve it? Where is James NOT the best fit and Dylan should map someone else?
- **Substance (preference):** Where is the energy real? What outside-scope is genuinely interesting? Be genuine — Dylan asked for preferences.

**Wrapper alone** = strategy without James in it. **Preference alone** = wishlist without business in it.

**Dylan's mapping order, in her words:**
> *"Try to list out the business, the components, and the needs, and I map the team first. Then of course there are a few strong people I really really want to map to, and then I put those in, but the rest of them are, I would say, a secondary effect."*

→ James's input should mirror Dylan's order: lead with business + components + needs, then where James + strong-people-on-team fit.

**Reframing the AI Tooling row** before this goes to Dylan: Accelerator is near-term SSv2 driver + multiplier across other rows. Drop the "???". This is the strongest piece of the AI-leveraged-leader case.

---

## Scenarios for James's input back to Dylan (sketches)

Four candidate shapes, each different in scope, team composition, energy fit, and Director story. None of these are "the recommendation" yet — they're walk-through candidates.

### Scenario A — ML + AI deepening (within current shape, expand sideways)

**Shape:** James keeps HF CG. Absorbs Yan's ML side (Daniel Liu's ~8 ML engineers, *if* the 5/15 redeployment lands). Possibly absorbs Edward's backend (~5) since adjacent to CG infra. Team grows ~17 → ~25-30. Mostly ML + AI infra.

**What's added vs current:** Daniel Liu's ML engineers + optionally Edward's backend.

**Director story:** *"I run the foundation layer of Pinterest's AI personalization stack — ML platform (UPP) + AI infrastructure (Reflex/Pinkerton) + GenAI for recs (RecGPT). I closed the loop from ML platform to AI agents to user features."*

**Serves Dylan's signals:** *"UPP is great"* ✓, AI doubling-down (a) ✓, Yan/IB redeployment ✓. Doesn't serve presentation-side lean.

**Pros:** Highest skill+energy fit. Compounds 5/16 commitment cleanly. Politically lowest-risk (consolidates within ML side).
**Cons:** Doesn't take the presentation-side door. Director story rests on depth, not breadth. May read as not-leaning-forward into Dylan's offer.

### Scenario B — AI-leveraged full-stack wedge (James's counter-proposal, built out)

**Shape:** James keeps CG core. Adds **Anticipation-end-to-end** as the surface wedge — owns surface logic for Anticipation (rendering, UX behavior, end-to-end loop). Absorbs Yan's ML side (Daniel Liu's ~8). Absorbs Edward's backend (~5). Selectively absorbs Tim's full-stack/backend slice (the 2-3 non-mobile). Mobile-only engineers stay under Tim or move to another EM. Team grows ~17 → ~30-35 with new full-stack-AI shape.

**What's added vs current:** Daniel Liu's ML + Edward's backend + Tim's full-stack slice + surface logic ownership for Anticipation.

**Director story:** *"I lead Pinterest's first AI-leveraged full-stack team — ML + AI agents + AI-native client engineering, traversing the whole stack to deliver AI-native user experiences. Anticipation is the proof case: end-to-end from retrieval through agentic generation through user-facing surface."*

**Serves Dylan's signals:** *"UPP is great"* ✓, AI doubling-down (a) ✓, *"end-to-end experiences are where you shine"* ✓, presentation-side lean (partial) ✓, Yan/IB redeployment ✓. Most signals served.

**Pros:** Creates a Director-altitude charter type that doesn't exist at Pinterest today. Genuinely yours — built from your strengths and energy. Combines AI (a) + AI surface (c).
**Cons:** Politically complex (Tim's team reshape requires Dylan and possibly Tim's consent). Requires charter authority Dylan may not have unilaterally. Requires team rebuild over 12-18 months (hiring/growing full-stack-AI engineers). Speculative — Pinterest may not have appetite for a new charter type.

### Scenario C — Lean fully into presentation-side as offered

**Shape:** James moves substantially toward Yan + Tim's territory. Absorbs Yan's full team (post-redeployment, or as-is) + Tim's mobile team. Possibly drops some CG ML work to make room — RecGPT to Dhruvil or Bella as EM-track; LWS consolidated elsewhere. Team becomes presentation/surface-coded.

**What's added vs current:** Yan's team (Edward backend + Android/iOS) + Tim's team (mostly mobile) — net add ~30-40 reports. Net drop: some ML/AI scope.

**Director story:** *"I run AI-native user experiences end-to-end — surfaces, client engineering, AI-leveraged experience design."*

**Serves Dylan's signals:** Presentation-side lean ✓ (literal). Sponsorship motive ✓ (broadest scope). Other signals (UPP, AI doubling-down) less so.

**Pros:** Cleanest match to Dylan's literal lean. Broadest scope. Director-runway by surface count.
**Cons:** Lowest skill fit (James is ML/backend, not mobile/UX). Lowest energy alignment (per the energy reads). Risks scope-for-scope's-sake — Krishna-pattern guardrail applies, must have real metric spine. Drops AI infrastructure (Reflex/Pinkerton) momentum unless explicitly carried over.

### Scenario D — Stay deep, push AI Tooling cross-org / Pinterest-wide

**Shape:** James keeps CG largely as-is (modest expansion via Yan/IB redeployment). Treats Reflex/Pinkerton as a **Pinterest-wide AI substrate** — extends it beyond CG, becomes the AI-leveraged-leader for Core engineering broadly. Director case = AI Tooling adoption across orgs + CG impact.

**What's added vs current:** Daniel Liu's ML (~8) for CG depth. Reflex/Pinkerton scope explicitly extended cross-org with Rajat/Jeff sponsorship.

**Director story:** *"I built Pinterest's AI-leveraged engineering substrate. Reflex/Pinkerton is used across all of Core. CG is best-in-class because of it. I'm the AI-leveraged-leader pattern."*

**Serves Dylan's signals:** AI doubling-down (a) ✓ strongly. *"UPP is great"* ✓. Doesn't serve presentation-side lean.

**Pros:** Highest leverage on the AI = (a) reading. Aligns with discretionary craft-time investment. Doesn't require absorbing UX scope. Compounds 5/16 commitment most directly.
**Cons:** Requires Rajat/Jeff sponsorship for cross-org Reflex/Pinkerton adoption. Longer timeline (charter spans multiple orgs). Declines Dylan's offered door for presentation. Risks being read as not-taking-the-runway. Sponsorship architecture (Jia Jing + Faisal/Bo) becomes load-bearing.

### Scenario E — James's preferred shape (sketch, 2026-05-19)

James's actual preference, drawn directly:

**What James wants to keep / gain:**
- All of **Anticipation** scope
- **Recsplanations** scope *(new addition — needs definition, not in current inventory)*
- **UPP**
- Anticipation **foundations / core**
- **All CGs**
- **LWS models** James currently owns
- *(Implicit, not stated but presumed: Reflex/Pinkerton/Pinvestigator — the AI Tooling Accelerator. RecGPT — current scope.)*

**What James can give up:**
- **Unity** *(needs definition — is this the "Unity to be used in Intelligent Boards" from the Retentive Recs/Anticipation row?)*
- **Responsiveness** (J.J. 50% — in-session signal adoption)
- **ML foundations** *(needs definition — subset of UPP platform extension? L1 Utility? Dynamic Triggering?)*

**People ask:** **Daniel Liu's team** — the ~8 ML engineers currently under Yan. Connects directly to 5/15 Yan/IB redeployment intel.

**Shape characterization (refined post-clarifications):** Sits between Scenarios A and B. ML/AI-personalization-focused, with a **bounded surface wedge** via Recsplanations:
- **Deepens** into Anticipation + Recsplanations end-to-end (personalization narrative, end-to-end personalization story)
- **Adds** Daniel Liu's ML team (consolidates ML where it's anticipation-relevant per Dylan's filter)
- **Adds (implicit, via Recsplanations end-to-end)** a small UX/client engineering wedge — must be sourced from Tim's full-stack slice or Yan's team
- **Sheds** Unity-for-IB + Responsiveness + ML Infra (UPP third pillar, going to Dhruvil)
- **Does NOT reach** for the bulk of Tim's mobile team or Yan's whole UX surface

**Director story (sketch):** *"I run Pinterest's AI personalization layer — the full personalization stack from candidate generation through anticipation through generative recs through user-facing explainability. All ML and AI personalization for Homefeed lives in my team."*

**Serves Dylan's signals (initial read):**
- *"UPP is great"* ✓ strong
- AI doubling-down (a) ✓ via Reflex/Pinkerton + RecGPT + Recsplanations
- *"End-to-end experiences"* ✓ partial — Anticipation is e2e but James isn't taking surface engineering
- Presentation-side lean ✗ — declines this door
- Yan/IB redeployment ✓ — Daniel Liu's team is the explicit ask

**Trade-off characterization:** Closer to Scenario A than to B/C/D, but **more focused** than A (drops more current scope to make room for personalization-specific additions).

**Definitions clarified (2026-05-19):**

#### Recsplanations (new scope James wants to own)

A rich product surface, not just LLM-generated explanation text. **Each recsplanation answers "why this, what is it"** and gives Pinners a calm, knowledgeable next step that piques interest and supports continued exploration.

**Visual elements:**
- **Stack of reference pins + explanatory text** — visual "recsplanation" connecting pins the Pinner already engaged with to exploratory recommendations
- **"Mini grid" of exploratory content** — differentiated HF layout (signals "Pinterest is breaking up my feed to show me something special")
- **Proactive feedback flyout** — selecting feedback options elevates or fatigues the entire *interest cluster* associated with the exploratory pins

**End-to-end shape (what owning Recsplanations actually entails):**
- **Backend / ML:** clustering exploratory pins into interest groups, generating explanation copy (LLM-driven), interest-cluster fatigue/elevation logic, candidate selection
- **Surface / UI:** mini-grid layout in HF, differentiated rendering, flyout interaction
- **Product / design partnership:** copy tone calibration, interaction design

**Key implication for scope design:** **Owning Recsplanations end-to-end *requires* some UX/client engineering capacity.** Either:
- (i) James owns Recsplanations end-to-end → needs surface engineers (small slice from Tim's full-stack/backend or Yan's team)
- (ii) James co-owns Recsplanations with surface team (Yan or Tim owns UI, James owns ML/AI/backend) — bounded interface

**This is the natural Scenario B wedge inside Scenario E.** Recsplanations is the most concrete "end-to-end experience" James already wants to own — it ties AI (LLM-generated copy, fatigue logic) to surface (mini-grid, flyout) to Anticipation (interest clusters from RR). Serves Dylan's signals more strongly than the rest of Scenario E does.

#### ML Infra (what James can give up)

**Third pillar of UPP.** Training data optimizations and related ML platform plumbing. **Dhruvil's team now has a few people working on it** — natural transfer target. Giving this up = aligning ownership with where the team energy already sits.

#### UPP scoping clarification (from James, 2026-05-19)

> *"For UPP, the expansions to the other surfaces are the work — so if I own CGs and Retrieval, then I do need to own that as well."*

UPP cross-surface expansions (Notif, P2P, etc.) = CG/Retrieval work on other surfaces, not separable from CG/Retrieval ownership. **Dylan's "UPP is great" endorsement is effectively a CG/Retrieval-cross-surface endorsement.** James owns this naturally.

#### Unity (still open)

James listed Unity among the give-ups but didn't define. Best guess from current context: the *"Unity to be used in Intelligent Boards"* mentioned in the Retentive Recs/Anticipation row of the HF CG inventory. If so, "give up Unity" = let Yan's team / IB team own Unity adaptation for IB, while James keeps core Anticipation Unity work. **Treating as IB-Unity unless James corrects.**

### Tonal calibration for the input (James's call, 2026-05-20)

> *"The more realistic of a plan I show her, the more it demonstrates that I've been thinking about it, and I can then lead with more conviction that it will be successful."*

**Lead with conviction, not tentativeness.** Show a realistic plan. Demonstrate prior thinking. Don't soft-pedal as "preferences shared" — that undersells. The artifact should read as *"here's the plan I've worked through; here's how it serves the business; here's what I'm willing to give up; here's the headcount I need. Push back where you see it differently."*

This still respects Dylan's mapping order (business → components → needs → strong people → secondary effects) — but the *posture* is Director-altitude, not asking-for-permission.

### Ethan Evans frame to bake in (recalibration, 2026-05-20)

Per Ethan Evans's analysis of the H1 career convo (see [[feedback-director-track-org-thesis-framing]]):

**The Dylan convo was NOT a stretch-project ask — it was a future-scope DESIGN test.** Her language (*"give you a path," "mapping teams and strong people," "what should be trimmed," "what energizes you"*) is Director-level terrain. She's implicitly testing whether James can reason about capabilities, team topology, coordination seams, and long-term business ownership.

**The altitude required for the response:**

> *"Pinterest needs an explicit cross-surface AI personalization capability, and my current work is naturally converging toward owning that space."*

This is the organizing thesis. **Not a career demand — an org thesis.** The artifact must lead with this altitude, not with preference.

**Critical structural shifts to bake into the draft:**

1. **Lead with org thesis** (Pinterest needs X), not personal preference (I want X).
2. **Show 2-3 org-shape options with tradeoffs**, then recommend one. Single-recommendation artifacts read as preference; options-with-tradeoffs read as operating-model design. Director-altitude leaders show reasoning across alternatives.
3. **Add Design Principles section** (3-5 principles) — makes the operating frame visible.
4. **Add Capability Map section** — separate the building blocks (production CG, frontier AI, platform interfaces, product/E2E partnership) so the reader sees reasoning in capabilities, not team names.
5. **Explicit scope trims are non-negotiable** — propose ownership AND name what you stop/delegate/simplify. Without trims, the artifact reads as ambition without operating discipline.
6. **Success metrics tied to Dylan's business outcomes** — topline (SSv2, WAU/MAU), experiment velocity, quality/regression control.
7. **Protective opening sentence:**
   > *"Per our conversation, I wrote up a few org-shape options and tradeoffs to help pressure-test the business, resourcing, and coordination implications. These are options, not a pitch — sharing to reduce coordination tax."*

**The deeper point (Ethan):** *"Your opportunity is not to ask Dylan for promotion. Your opportunity is to show her that you can think like the owner of a capability, not just the manager of a team. That means clear thesis, tradeoffs, scope discipline, and sponsor-aware execution."*

### Design principles (to populate, working list)

The artifact will lead with 3-5 principles that name the operating filter. Working candidates:

| Principle | Rationale |
|---|---|
| **Optimize for topline growth (SSv2, WAU/MAU)** | Aligns with Dylan's anticipation-relevance + business-sense filter |
| **Keep charters durable; reduce coordination tax** | Director-altitude lens — clean boundaries beat clever org structures |
| **Couple ML and AI investment where they compound** | Reflex/Pinkerton + Anticipation + RecGPT + Recsplanations live in one team because they reinforce each other |
| **Create growth paths under each EM** | Strong people retention is org capability, not HR detail |
| **Bound scope to the team's actual capacity** | Honor Dylan's "don't put everything in a thin team" constraint |

### Capability map (to populate, working layers)

Separating the building blocks of HF Relevance, independent of which team owns what:

| Capability layer | Building blocks | Why it matters |
|---|---|---|
| **Production personalization (ML)** | CG, Retrieval, Anticipation, LWS, CLR | Where SSv2 comes from; metric-defensible |
| **Frontier AI for recs** | RecGPT, Recsplanations, agentic generative recs | The doubling-down Dylan named |
| **AI-leveraged engineering substrate** | Reflex, Pinkerton, Pinvestigator | Multiplier on every other layer |
| **Platform interfaces** | UPP cross-surface (Notif, P2P, etc.), UPP foundations, ML foundations | Where Core teams plug in |
| **Product / E2E partnership** | Anticipation surface logic, Recsplanations UX, P13N-Experiences integration | Where ML/AI meets the user |
| **Ranking + blending** | HF Ranking, Blending | Dhruvil's coherent foundation |
| **Surface engineering** | Frontend, mobile, client | Yan + Tim's reshape |

### LWS and Blending — two open variables (noted, not yet resolved)

**LWS** — Yali (80%) + Hedi (80%) + Zili. GPU serving + architecture unlocks now landing; ready to "pluck fruits." Tight coupling with Ranking (Dhruvil) downstream. James developed from scratch.

**Blending** — Rahul Goldam (= "Rohu", L16 Manager II), ~7 reports, currently understaffed. James was Rahul's onboarding buddy — close relationship. Heavy collaboration with James's team on Anticipation/RR + content merit-driven distribution.

**Level context (key constraint):** Rahul is L16 (sub-EM altitude). James + Dhruvil are L17 (peer-EM altitude). **Rahul should report through James or Dhruvil, not standalone direct to Dylan.** This bounds the org-shape options for Blending.

**Open variables — surface in the artifact, don't unilaterally resolve:**

| Variable | Possible homes | Notes |
|---|---|---|
| LWS (3 engineers) | Stays under James; or moves to wherever late-stage scoring/blending consolidates | James plucks fruits if stays; coordination tax minimized if moves with Blending |
| Blending (Rahul + ~7) | Sub-team under James; or sub-team under Dhruvil | Rahul reports through one of the two peer EMs (not standalone) |

**Default for the artifact:** note these as two variables Dylan should weigh in on. Don't solve them unilaterally. The reader sees James thinking about org coupling + L-level constraints + Rahul's growth path — Director-altitude framing without overreach.

**Dynamic Triggering — locked as cut.** James doesn't want to fund it anymore (2026-05-20).

### Org-shape options to show Dylan (2-3, with tradeoffs)

Three candidates from our walkthrough. The artifact would summarize each in ~50-80 words with tradeoffs and recommend one.

| Option | Shape | Tradeoffs |
|---|---|---|
| **Option 1: Two-track within HF CG** (production + frontier under James) | Internal restructure only — production track (CG/Retrieval/LWS) and frontier track (RecGPT/Reflex/Pinkerton/Recsplanations) as sub-teams under James. Minimal external scope change. | Pros: easy to land; coherent within current scope. Cons: doesn't serve Dylan's "AI as real funded project" signal; doesn't address Yan/Tim reshape; smaller Director story. |
| **Option 2 (RECOMMENDED): AI personalization as cross-surface capability** (Scenario E) | James owns the AI personalization stack end-to-end: CG, Anticipation, RecGPT, Recsplanations, UPP cross-surface, LWS. Daniel Liu's ML team consolidates. Recsplanations UX wedge (small surface engineering slice). AI Tooling becomes real funded sub-team (4-6 engineers). | Pros: serves Dylan's signals strongly; creates coherent Pinterest-wide capability; clean peer story with Dhruvil; enables Yan to reshape as presentation EM. Cons: requires Rajat-sign-off on AI headcount; Recsplanations surface scope is the political pressure point. |
| **Option 3: AI acceleration as horizontal program** (Scenario D) | Reflex/Pinkerton becomes Pinterest-wide AI engineering substrate (Core-org-spanning). James owns or co-owns with Karina/Kaanon. James's CG team stays as-is or modestly expands. | Pros: highest leverage on AI; Pinterest-wide engineering culture impact. Cons: requires Jeff/Rajat-level decision; longer timeline; declines Dylan's presentation door; sponsorship architecture (Jia Jing + Faisal/Bo) becomes load-bearing immediately. |

### What does the organization get? (Director value prop)

> *"I should also be willing to answer the question, or answer an implicit question: what does the organization get with me stepping up as its leader, as a leader over this group? That's what every leader wants to know and will be above me is: what do they get? What do they get by setting this work structure up? I know what I get, but what do they get?"*

The implicit question every reader above Dylan (Rajat, Jeff) will ask of this proposal. The artifact must answer it explicitly or implicitly throughout. Working list:

1. **End-to-end AI personalization stack delivered coherently.** CG → Anticipation → RecGPT → Recsplanations → Reflex/Pinkerton substrate. No team boundaries fragment the personalization story. ML system and user-facing surface co-evolve under one technical leader. Pinterest's personalization narrative becomes a single defensible thing, not a stitched-together set of teams.

2. **AI-leveraged-leader pattern at Director scale.** James operates as the proof case that AI tools (Reflex/Pinkerton) multiply engineering output across a Director-scale org. This is exactly what Dylan's *"blindfolded if managing as before"* statement was gesturing at. Pinterest needs this pattern to scale into the AI-native operating model — James proves it works on a real personalization team with real metric delivery, then it generalizes.

3. **Strong people-growth engine.** Multiple promotion paths underneath: Daniel Liu (growth in new context if he opts in), incoming EM (real charter for an EM-track candidate), Bella (EM-track on AI sub-team), Yuke (TL → sub-EM on Anticipation), Piyush (IC16 → staff growth on UPP retrieval), J.J. (IC16 promo Q2). When senior performers see growth paths under James, recruitment and retention compound — Pinterest keeps the bench.

4. **Clean org boundaries enabling sister-team success.** Yan reshapes to coherent presentation-side EM (Tim consolidates under him — clear Director-track candidacy for Yan). Dhruvil owns foundations + ranking + possibly Blending — also coherent. The Scenario E rebalance is *structurally elegant*: every EM gets a clear charter, no overlap, no dilution. **This is the part Rajat and Jeff will value most** — Director candidates who design org-rebalances that strengthen peers signal a different altitude.

5. **Concrete metric delivery.** Scenario E is bounded and metric-defensible: ~2-3% SSv2 from the personalization stack (Anticipation, RecGPT, CLR, LWS) + WAU/MAU retention gains via Retentive Recs + cost/velocity gains via AI Tooling once funded. Stack ranks among the largest SSv2 producers in Core.

6. **AI-leveraged engineering substrate for Pinterest.** Reflex/Pinkerton with proper headcount becomes a *Pinterest-wide AI engineering pattern*. Other Core teams adopt. This is direct Jeff/Rajat value (engineering culture modernization) — beyond what HF CG would normally deliver.

7. **A Director-track candidate who scopes realistically.** This proposal: bounded scope, gives up real things (ML foundations to Dhruvil, Unity to Yan side, Responsiveness elsewhere), names the people, asks for specific net-new headcount (4-6 AI engineers, not "more headcount"). Easy to fund, easy to defend upward. Signals the *exec-presence operating model* — outcomes over activity, influence over control, narrative over details.

### Sponsorship architecture (James's read, 2026-05-20)

The two-sponsor plan James is operating against. Both are outside Dylan's direct chain — independent validators of James's Director case.

| # | Sponsor | Role | Status / Path |
|---|---|---|---|
| 1 | **Jia Jing** | Sr. Director, ATG (Advanced Technology Group) | **Clear primary.** Already a natural fit — ATG ↔ recsys / GenAI / Reflex-Pinkerton alignment. Path: build through existing ATG-CG collaboration surface (RecGPT, YiPing connection). |
| 2 | **Faisal** | VP, Trust & Safety + Signals (under Jeff) | **Primary preference.** Path: Qinglong (Faisal's ML delegate) as intermediate step → Faisal direct. Dylan offered to drop a line. James's planned post-vacation timing. |
| 2 (fallback) | **Bo (Bo Zhao)** | Sr. Director under Faisal | If Faisal isn't inclined, Bo Zhao is the fallback. Existing collaboration channel via Anna K (Bo Zhao intel asks already routine per stakeholders.md). |

**Implication for the team-design input:** The Jia Jing + Faisal/Bo plan is concrete enough to NAME in the input to Dylan if asked. Don't lead with it (Dylan didn't ask), but have it ready as the answer to *"how are you thinking about endorsement?"*

### People-setup angle for the input (James's framing, 2026-05-20)

> *"I should also name a few key team members whose careers will be set up for success here, and ideally name a few high performers... I need to take care of my EMs and TLs a bit more."*

Dylan said it explicitly: *"there are a few strong people I really really want to map to, and then I put those in, but the rest of them are, I would say, a secondary effect."* The input should mirror this — name the people whose careers Scenario E sets up.

**Initial roster (working list, to refine):**

**Dylan's "protected" tier (James's read, 2026-05-20):** Dhruvil, James, **probably Tim**. Daniel Liu is *desirable-not-essential* — push for him in the ask but be willing to accept if he resists or Dylan doesn't make him available.

**Strong TLs Dylan would protect:** **Daofeng** and **Olafur (Oliver)** — both Sr. Staff MLE tier. James works closely with both. Neither needs to move under James in Scenario E — they likely stay under Dhruvil / IC-line to Dylan, which is correct.

| Person | Current state | How Scenario E sets them up |
|---|---|---|
| **Daniel Liu** | Currently in Yan's team (~8 ML engineers under him) | Comes into James's org as TL/sub-lead for the Anticipation/RR ML cluster — **if he opts in.** Concrete growth path under a senior EM with anticipation-aligned charter. *Not in Dylan's protected tier — push for him but don't ship the plan dependent on him.* |
| **Incoming EM** (Vaidehi/Prashan pipeline) | Hiring in flight, close expected soon | Owns a sub-charter within James's expanded team (likely RecGPT/Recsplanations cluster or AI Tooling sub-team if option A lands). Manager-of-managers altitude. |
| **Bella** (RecGPT TL) | TL with 80% allocation, ramping leadership | EM-track candidate; could own RecGPT + Recsplanations LLM-copy cluster as sub-EM if charter grows. |
| **Yuke** (Anticipation TL) | 60% Anticipation, 30% RecGPT — heavy ramp | TL → potential sub-EM for Retentive Recs cluster as Anticipation deepens. |
| **Piyush** (UPP TL, IC16) | Most performant IC | Core retrieval owner; possible IC-staff growth path with cross-surface impact. (UPP foundations moves to Dhruvil; Piyush stays in James's retrieval team.) |
| **J.J.** (multi-hat) | Across L1 Utility, Responsiveness, AI Tooling | Promotion to IC16 by end of Q2 (per organization.md). Refocused on AI Tooling sub-team if option A lands — clear charter for promo. |

### Dhruvil's setup (refined per James, 2026-05-20)

**Dhruvil doesn't need more scope — he needs more people + another EM.** Current scope (Ranking, ~25) is already sizable. The expansion under Scenario E:

| What Dhruvil owns under Scenario E | Source |
|---|---|
| **Ranking** (existing) | Current |
| **UPP foundations** | Transferred from James (the platform-infra side of UPP, not cross-surface expansions) |
| **ML foundations** (UPP third pillar — training data optimizations etc.) | Transferred from James; Dhruvil's team already has people here |
| **Blending** (option) | If Rahul's team folds under Dhruvil — clean if Rahul moves under him; Rahul stays direct-to-Dylan otherwise |
| **Another EM under him** | New ask: Dhruvil gets a sub-EM to match James's altitude |

**Total Dhruvil shape:** ~25-32 reports, foundations + ranking + (possibly) blending + sub-EM. **Clean Director-track shape that mirrors James's.**

**The two strong ML EMs (James + Dhruvil) under Dylan now look like:**

| | James | Dhruvil |
|---|---|---|
| Charter | ML/AI personalization (CG, Anticipation, RecGPT, Recsplanations, AI Tooling, UPP cross-surface, LWS) | Foundations + ranking (UPP foundations, ML foundations, ranking, possibly blending) |
| Size | ~25-30 | ~25-32 |
| Sub-EM | Incoming Vaidehi/Prashan hire | New hire ask |
| Director-track | Yes | Yes |
| Overlap | None — clean charter boundary | None |

**Strategic read:** This is the strongest part of the proposal. **Dylan gets two coherent ML EMs running peer-altitude teams with clean charter boundaries.** No fights, no overlap, no dilution. Both have growth paths. Both have AI exposure (James leads, Dhruvil supports via ML foundations). Pinterest's HF Relevance ML side is operationally serious.

### Org-rebalance implied by Scenario E (working sketch, 2026-05-19)

If James lands Scenario E, the rest of Dylan's org rebalances. James's concerns mapped:

#### Yan's path — actually IMPROVES under Scenario E
- **Loses:** Daniel Liu's ML sub-team (~8) to James + a few UX engineers for Recsplanations
- **Gains (potential):** Tim's team consolidates under Yan (~11-12) — Tim reports to Yan as Manager II under Sr. Manager
- **Net:** Yan's scope reshapes from "mixed-bag composite (ML + backend + mobile)" to **"pure presentation-side EM with mobile + UX consolidated"**
- **Strategic read:** This is **structurally elegant**. Yan's scope becomes coherent (presentation surfaces, end-to-end). James's scope becomes coherent (ML + AI personalization). Dylan's "presentation side" lean is served — *by Yan, not James*. Yan's Director-track candidacy clarifies.

#### Dhruvil's path — narrower than James's framing suggests
- **Absorbs:** ML Foundations (UPP third pillar — Dhruvil's team already has people there)
- **Possibly absorbs:** Some HF CLR / retrieval-adjacent work *(speculative; not certain Dhruvil wants or needs this)*
- **Net:** Mostly stable. Modest absorption.
- **James's concern is real but bounded:** Dhruvil's "set up for success" may be stability + headcount fills rather than scope expansion. Not every strong EM needs scope growth in the same cycle.

#### Tim's path — likely consolidates under Yan
- Tim is Manager II. Yan is Sr. Manager. **Natural consolidation pattern.** Tim → TL or Manager II reporting to Yan.
- This creates the presentation-side consolidation point Dylan may have been gesturing at, without requiring James to take the role.
- James can also absorb parts of Tim's work (e.g., surface engineers for Recsplanations).

#### Francisco's path — outside James's input scope
- **Team moves to Kurchi.** Already decided per 5/7 DM thread (Dylan's anticipation-relevance + business-sense filter).
- **Francisco personally** — unknown. Could move with team to Kurchi, stay under Dylan with a different team, or move out. **Outside James's input scope** — this is Dylan's call, not James's.

#### AI capacity — the org-level question, not the personal-time question

**Reframe (James, 2026-05-19):**
> *"I'm not looking at AI capacity for myself. I'm looking at AI capacity for the organization. You want to have people be able to work on this, treated as a real project, with funding like the real project."*

**The load-bearing question is NOT "how does James free his time" — it's "how does the org allocate real funded headcount to AI."** Currently AI Tooling runs on borrowed cycles: J.J. 20% + Alok 50% + Chuxi 20% = ~0.9 FTE. That is a side project, not a real bet. Dylan's *"I want to double down on AI"* signal only matters if it converts into actual headcount + charter.

**Managerial bandwidth is already being addressed independently** — James has an open EM headcount in flight (Vaidehi + Prashan pipeline, expected to close soon). The sub-EM solves manager-of-managers altitude. **It does not solve AI engineer capacity.**

**Concrete options for sourcing AI capacity:**

| Option | What it looks like | Who needs to say yes |
|---|---|---|
| **A. Net new headcount allocated to AI** | Dylan sponsors 4-6 MLEs/SWEs dedicated to AI Tooling sub-team within James's org; new charter ("AI-Leveraged Engineering" or similar) | Dylan → Rajat; possibly Jeff for the bigger ask |
| **B. Reallocation within Dylan's org** | Engineers shift from existing teams (e.g., parts of Yan, parts of Francisco's exit, parts of platform/labeling) to AI under James | Dylan unilaterally, with peer-EM negotiation |
| **C. Cross-org consolidation** | Karina/Kaanon's AI initiative under Rajat consolidates with Reflex/Pinkerton under James (or a joint charter) | Rajat-level decision; cross-VP politics |
| **D. Pinterest-wide AI substrate funding** | Reflex/Pinkerton becomes Pinterest-wide bet with funding from Core/CTO budget; James owns or co-owns | Jeff/Rajat/CTO-level decision; biggest ask |

**Each option produces a different charter shape for AI within Scenario E:**

| Option | AI sub-team size | Charter altitude | Sponsorship cost |
|---|---|---|---|
| A | 4-6 engineers | Sub-charter within James's team | Medium — Dylan needs Rajat sign-off |
| B | 3-5 engineers | Sub-charter within James's team | Low — Dylan can do this internally |
| C | 6-10 engineers | Cross-org charter, James leads or co-leads | High — Rajat-level decision |
| D | 8-15 engineers, Pinterest-wide | Director-altitude charter spanning Core | Highest — Jeff/CTO-level |

**Strategic read:** Option A is the cleanest "make AI a real project" move. It's bounded, fits Scenario E, and Dylan has the authority to sponsor upward. Options C and D are higher-altitude but require sponsorship architecture James is still building (Jia Jing + Faisal/Bo two-sponsor plan — see Sponsorship section). **Option B is fallback if A doesn't get Rajat sign-off** — Dylan can do it unilaterally by reallocating within her org.

**Recommended ask framing:**
*"For Reflex/Pinkerton to deliver on the AI doubling-down, we need 4-6 dedicated engineers as a sub-team with a real AI Tooling / AI-Leveraged Engineering charter. Current 0.9 FTE pulled from cycles is undersized for the strategic bet. If you can sponsor the headcount allocation, I'll deliver a Director-altitude AI engineering capability for HF and as a substrate other Core teams can adopt."*

This converts Dylan's signal ("double down") into a concrete, defensible ask with deliverables tied to it.

### Scenario comparison at a glance

| Dimension | A: Deepen | B: Full-stack wedge | C: Lean presentation | D: Cross-org AI | **E: James's preferred** |
|---|---|---|---|---|---|
| Skill fit | ★★★★★ | ★★★★ | ★★ | ★★★★★ | ★★★★★ |
| Energy fit | ★★★★★ | ★★★★ | ★★ | ★★★★★ | ★★★★★ |
| Dylan signals served | ★★★ | ★★★★★ | ★★★ | ★★★ | ★★★ (pending definitions) |
| Director-altitude novelty | ★★ | ★★★★★ | ★★★ | ★★★★ | ★★★ |
| Political feasibility | ★★★★★ | ★★★ | ★★ | ★★★ | ★★★★ |
| Timeline to land | 3-6mo | 12-18mo | 6-12mo | 12-24mo | 3-6mo |
| Sponsorship dependence | Low | Medium | Medium | High | Low-Medium |

## Open questions / next moves

### Open (James to resolve)
- **Q1 energy reads** — confirm/adjust the HIGH/STEADY/LOW grading above
- **Q2 cuts layered with energy** — are the proposed cuts still right after energy lens?
- **Q3 outside-scope wildcard** — what scope outside current team is genuinely interesting? Sponsorship-coded; load-bearing for Director path. (Dylan's *"react on the presentation side"* lean suggests this is the door she's holding open.)
- **The "or" allocations** — Zihao → UPP or CLR? Ryan → UPP Infra or LWS Infra?
- **Andrew-Pinkerton naming alignment** (carried from 5/16) — substrate framing may want different architectural-layer name

### Next moves
- **Draft the input document for Dylan** — once Q1/Q2/Q3 land, structure as: business+components+needs → where James fits → energy reads → cuts → outside-scope ask
- **Update `H1_career_convo.md`** — convo has happened; lock the post-convo state
- **Update `dylan_archive.md`** — new signals to log (presentation-side lean, sponsorship-in-motion, Faisal/Qinglong intro path, Manu relationship build)
- **Update `stakeholders.md`** — Manu profile (new key stakeholder Dylan is building with)
- **Faisal connection** — Dylan offered to drop a line; James planned post-vacation; decide whether to accelerate
- **Reframe the HF CG inventory doc** — fix Pinsight → Pinkerton; reframe AI Tooling row before sending to Dylan

### Carried items
- 5/16: rebrand + new docs committed (verify); Andrew share artifact still pending
- 5/15: Yan / IB redeployment still high-fragility; Vaidehi + Prashan onsite scheduling

---

## Feedback memories updated this chapter

- **[feedback_dylan_pronouns.md](../../../.claude/projects/-Users-jamesli-code-leo/memory/feedback_dylan_pronouns.md)** — Dylan uses she/her; correct any historical "his/him" references in older files when noticed.

---

## Changelog

- **2026-05-19** — File created. Captures cleaned transcript, signals extracted, ambiguity resolution, HF CG scope inventory (verbatim), proposed cuts, Leo's energy reads (to be confirmed), strategic framing, open questions.
