# EPD Demo 2026-05-04 — Debrief + Follow-ups

> Canonical capture of the live EPD demo + same-day follow-up signals (Slack DMs from Faisal, Rajat, David Sun, Andrew, Dylan; Chuck/ATG invite; Asana pushback; Dylan's rescope message). Written 2026-05-04 evening before the 5/5 Dylan 1:1.

---

## Executive summary

The 30-min EPD demo to full EPD reporting under CTO Matt Madrigal) **landed materially better than expected.** Live Q&A came only from VP+ level (Faisal Farooq VP Eng + Matt Madrigal CTO + light from Andrew). Same-day DM follow-ups produced **all five Q11 sponsor-cultivation signals firing** + a sixth named sponsor (Chuck, ATG, 4/23 stretch-target VP at 0% → actively pulling) + completion of the entire 4/23 VP-target list (Jeff / Rajat / Faisal / Chuck all in motion within the calibration window). 400+ people showed up.

**Strategic posture shift:** *"how do I get sponsors?"* → *"how do I orchestrate the demo circuit + collaboration threads without burning out, breaking the team, or scope-creeping into work that doesn't compound?"* This is the question for the 5/5 Dylan 1:1.

**Two material watch-outs:** (1) Matt scheduled the **EPD all-team demo for ~June 17, mid-James's OOO (6/1 → 6/30)** — calendar conflict needs Dylan-1:1 resolution; (2) **Asana-vs-Jira tribal pushback** surfacing from engineering side (Krystal private question + Dylan public *"shall we reconsider"*) — handle as pluggable-system reframe, don't get pulled into a tooling fight.

**One coaching-pattern flag:** Reading Dylan's same-day rescope message ("I asked Andrew to rescope this project so it's not just on you anymore") **as anxiety / "is she taking me off"** is the IC-comfort instinct firing under success-pressure — same shape as Saturday's *"should I ramp UPP technically?"* and the 5/1 H1 doc over-interpretation. Pattern is now 3-for-3 in 4 days under high-stakes ambiguous sponsor signals. Surface explicitly with Coaching Patterns notebook in a future session.

---

## 1. The demo itself

**Date:** Monday 2026-05-04 (morning, ~10:00–10:30 AM PT)
**Forum:** EPD all-hands (full EPD reporting under CTO Matt Madrigal)
**Audience:** ~2,200 invited (450+ showed up)
**Slot:** 30 minutes
**Co-presenters:** James Li + Andrew Yaroshevsky (Andrew = named project owner of Reflex; James = co-driver via Engineering Agent + PinSight)
**Sponsor co-pilot in audience:** Dylan Wang

### What landed (per planned beats from prep doc)

- **Beat 1 — Intro + opener (Variant C):** Title-embedded ML EM framing (*"ML Engineering Manager leading the Candidate Generation teams in Personalization"*), *"we built"* inclusive language, *"I lead"* not *"support"* for authority at scale. Landed clean.
- **Beat 2 — Asana card continuity (Option A):** Stayed on Dylan's same screen; agent wrote back to Asana card (comments + PR link). The story moment (Skeptic-confused → human-comment correction → Curator auto-generated new check) demonstrated live RLHF — *"same mistake a new engineer would make on their first week"* framing was the human-touch moment.
- **Beat 3 — v4 systems diagram:** Visualization of Detect → Build → Simulate → Prove with Skeptic-in-Detect / Validator-in-Build architecture. Stole v1 thesis (*"humans supervise, agents execute"*) verbally. Andrew handled the systems-level framing.

### Style win: the "PM agent" moment

During rehearsal Dylan thought a planned moment about a PM agent ("which Andrew is real?" framing) would be funny and that people would ask the joke question. **They did.** Per the post-demo DM:

> **Dylan (10:34 AM):** *"I missed the party about ppl joking PM agent — as I rehearse, I thought that would be funny and ppl would ask when we will know which andrew is real"*
> **Andrew (10:35 AM):** *"they actually did ask that lol"*
> **Dylan (10:36 AM):** *"yeah I saw that later in chat hahaha"*

→ Banking as evidence of EM-level executive presence (Goal 4): humor + confidence + landing a planned beat with audience participation. Worth surfacing in self-review later.

### What didn't land or surprised

- **No Q&A from Rajat.** Rajat was the originally-targeted VP for the Engineering Agent + UPP tie-in (per backlog #78 Jeff/Rajat OH planning). Rajat instead followed up via DM with Dylan rather than asking live — but that DM follow-up was substantive (productionization tracks ask).
- **Engineering pushback on Asana surfaced privately.** Krystal Benitez asked Dylan privately during the demo: *"I would not DARE ask this live, but I'm dying to know why we chose to use Asana instead of Jira for Reflex? Not a Jira fan girl - just had to maliciously comply over the years 😂"* — surfaced 10:24 AM. Indicates **engineering-culture-tribal Jira-vs-Asana sensitivity** that has James's name on it (Dylan said *"Sorry James"*).

---

## 2. Live Q&A — verbatim

### Faisal Farooq (VP Eng) — ML Flywheel collaboration ask

> *"I just want to quickly, because the team should definitely work, I'll ask the team. ML Flywheel, if you have heard about it, was sort of our agentic system before agentic systems, where we basically identify safety gaps automatically with reports or automatically find opportunities to deploy, change, and retrain. The app models automatically deploy to shadow mode and experiment automatically.*
>
> *One of the biggest learnings we found there was how to actually do offline learning to experiment. How do our offline learnings go into experiments? At any given point in time, we had so many candidates. The key was: is there a ship-worthy candidate or not? The team has so much learning that I would really love teams to work together on what are your thoughts on some of those? Those are really tricky questions, because with agents and with ML5, which was really not an actual agent system, we have multiple candidates at any given point in time. Identifying which candidate is actually ship-worthy was not easy."*

**Translation:** Faisal is offering his team's playbook from ML Flywheel (the prior generation pre-agentic system at Pinterest he led) on the *"many candidates → which is ship-worthy"* problem. This is high-quality VP-level vouching: "we've solved an adjacent problem; let's collaborate." **Sponsor-stack signal: Credibility sponsor.**

### Matt Madrigal (CTO) — *"awesome effort"* + June 17 all-team invite + cross-EPD curiosity

> *"I just want it as an awesome effort. I love Andrew and others for taking a grassroots effort and then sharing it more broadly on something that can have huge impact.*
>
> *A couple of things:*
>
> *1. It's great. It's in this form just to see it. Like you said, get more help, open source, etc. is awesome.*
> *2. We have an EPD all team, I think Sarah listened when is that? It's like in a month from now or something. June 17th probably. It's not on anyone's calendar yet though so don't freak out."*

Followed by (Matt continued, garbled in transcript but paraphrased):

> *"Andrew, one thing would be great if you don't mind, maybe taking some of the feedback here and demoing it in [NEXT — possibly a forum name or "next" all-team]. I think we're going to make that all team probably more demoing and yes, Q&A updates and then separately I'll probably just follow up with you all.*
>
> *But I'm curious about this whole guarded pipeline, it's very interesting right? Like this idea of some of the build interventions than what you're able to do to you know some of the reweights you could take on on the data and then also the simulations. I know this is meant to be more for just personalization, I'm just curious about how this could potentially help with ranking. I mean the retrieval mechanisms are a little different but maybe we could take that one offline.*
>
> *It'd be cool to see how we could extend this you know beyond yo to other use cases and that's where I feel like you all think through this and think Kartik was asking some other questions too. But maybe if you guys that's you guys could just think through how let's get the critical mass here to solve some of these use cases around yo specifically around like personalization here. But I feel like this could be pretty powerful across all different EPD functions."*

**Translation:** (1) **June 17 EPD all-team agenda slot offered** — Platform-sponsor capital spent. (2) Cross-EPD scope expansion ("could be powerful across all different EPD functions") — Scope-sponsor signal. (3) Wants offline follow-up on ranking-side applicability. (4) Mentioned **Kartik was asking questions too** — Kartik (Chief Architect, named sponsor target on backlog #81) is engaged separately. (5) Adopted *"guarded pipeline"* as his framing of the system — light language adoption.

### Andrew Yaroshevsky — wrap

(Light wrap; primarily co-presenter framing throughout; carried the Detect → Build → Simulate → Prove systems-level explanation.)

---

## 3. Post-demo DM threads — chronological, verbatim where captured

### 3.1 Andrew + Dylan + David Sun + James — 4-member DM (David Sun cold reach-out, started 10:25 AM)

> **David Sun (10:25 AM):** *"hey, folks, I'm David work on delivery infra. As the team working on the delivery infra, beyond all the system data that the team current maintains (e.g. latency from Unity toolbox), we are building business intelligence on top. The reflux idea is very exciting! Want to see how we could collaborate.*
>
> *As a side note, the team is currently working on ForgeDev and homefeed team is using it for incident debugging:*
>
> *And this is just the starting point - want to see what's next we could build together on!"*
>
> **David Sun (11:13 AM, follow-on):** *"oh and forgot to mention, @Andrew Yaroshevsky last time I was pretty excited about the anticipation proposal - great to see the new reflux proposal from you and would love to see how we can collaborate"*
>
> **Dylan (11:13 AM):** *"This is awesome thank you so much for reaching out David! Let me add to some of our ongoing reflex meetings, we can use sometime to understand how to work across."*
>
> **David Sun (11:15 AM):** *"yeah for sure. Is there any doc I could read beforehand w.r.t. what is built and how? Want to learn more about what is built. I think forge dev or whatever technology we are building is at the forefront of utilizing agent technologies"*
>
> **Dylan (11:16 AM):** *"Here it is from @James Li: [link to James-authored Reflex doc]"*
>
> **David Sun (11:19 AM):** *"can I get comment access? For example, forge dev has a use case called PR pilot, which could drive a PR from rough shape to ready to land by code reviewing, fixing tests and addressing comments by running the loop. People can already use it in optimus, pinboard and pinconf. We also want to include more coding guidelines from various teams cc @James Li*
>
> *our plan is to gradually expand it to be the standard for all code changes at least covering Unity/AdMixer/BAO/ForgeDev"*
>
> **Dylan (11:20 AM):** *"Added you as editor*
>
> *I do think build part is where we need most effort. Thank you very much for reaching out!"*
>
> **David Sun (11:23 AM):** *"yep, if you have time - try ForgeDev out in a repo 🙂 a good working solution speaks louder. If there are gaps we could work together on improving"*

**Translation:**
- David Sun (delivery infra TL) reaching out cold = unprompted pull
- Dylan forwarded James's doc + added David as editor = forwarding behavior + sponsor capital
- David offers **PR pilot agent infrastructure used in Optimus, Pinboard, Pinconf, expanding to standard for Unity/AdMixer/BAO/ForgeDev** — solves the "build half is hardest" problem Dylan named
- David typoed *"reflux"* twice for *"Reflex"* — light language adoption, comedic
- **Soft commitment ask:** *"try ForgeDev out in a repo 🙂"* — handle as 1-hour scoping conversation, not multi-week build (Ethan's bounded-engagement principle)
- **Sponsor-stack signal:** emerging Scope/Credibility sponsor at TL altitude (not yet VP, but materially valuable)

### 3.2 Dylan + Faisal Farooq DM (started 10:33 AM)

> **Faisal Farooq (10:33 AM):** *"This is great work 👏... as I mentioned the last mile is the hardest... but at the same time capabilities are much more powerful than what we had when we built ML Flywheel (which was somewhat wannabe-agentic lol)" (edited)*
>
> *"Teams should definitely share the learnings..."*
>
> **Dylan (10:35 AM):** *"100% Thank you Faisal for the feedback and insight*
>
> *Who can we work with to learn more from your end?"*
>
> **Faisal (10:35 AM):** *"What is amazing is the amount of effort it took us to build Flywheel project and how the barrier to entry is now reduced... amazing times"*

**Translation:**
- Faisal's *"capabilities are much more powerful than what we had when we built ML Flywheel"* is **VP-built-the-prior-version vouching** — high-credibility sponsor signal
- *"Wannabe-agentic lol"* = self-deprecating about ML Flywheel = positions James's work above his own
- Dylan asked the right follow-up (*"who can we work with"*) — actively converting the offer into a working channel
- **Sponsor-stack signal: Credibility sponsor.** Faisal moved from 4/23 audit estimate "25-50%" mental-model to **actively volunteering team collaboration**.

### 3.3 Dylan + Rajat Chaturvedi DM (started 10:42 AM)

> **Rajat Chaturvedi (10:42 AM):** *"good stuff Dylan and James! lets pick up few tracks for productionization!"*
>
> **Dylan (10:44 AM):** *"Thank you for the kind words! Yes, the team is already on it. Would love to go beyond P13N and have more ppl help."*
>
> **Rajat (10:47 AM):** *"yes, lets discuss the plan when we meet next!"*

**Translation:**
- Rajat = VP skip; moved from 4/23 audit "25%" mental-model + PinSight 4/16 exposure → **actively asking for productionization tracks**
- *"Lets discuss the plan when we meet next"* = explicitly the **Wed 5/8 OH** — the OH James had on calendar is now Rajat-driven, not James-pitching
- *"Beyond P13N + more ppl help"* (from Dylan) = scope expansion + resourcing ask in flight
- **Sponsor-stack signal: Scope sponsor + Platform sponsor.** Rajat is offering ownership-line moves AND his attention/agenda.

### 3.4 Andrew + Dylan + James — 3-member DM thread

#### 3.4a Celebration + PM-agent moment (10:33–10:36 AM)

> **Dylan (10:33 AM):** *"Great discussion! Awesome to see the excitement from team*
>
> *Thanks for driving it Andrew"*
>
> **Andrew (10:33 AM):** *"🎉 Well done folks, you did amazing"*
>
> **James (10:34 AM):** *"Thank you Dylan and Andrew for this opportunity! Really excited about the next steps."*
>
> **Dylan (10:34 AM):** *"I missed the party about ppl joking PM agent*
>
> *as I rehearse, I thought that would be funny and ppl would ask when we will know which andrew is real"*
>
> **Andrew (10:35 AM):** *"they actually did ask that lol"*
>
> **Dylan (10:36 AM):** *"yeah I saw that later in chat hahaha"*

#### 3.4b Asana pushback (10:47 AM, with Krystal's private question quoted)

> **Dylan (10:47 AM, @Andrew):** *"^^ btw I got a lot questions from eng side regarding Asana. Shall we reconsider"*
>
> Quoted from private conversation — **Krystal Benitez (10:24 AM)**: *"I would not DARE ask this live, but I'm dying to know why we chose to use Asana instead of Jira for Reflex? Not a Jira fan girl - just had to maliciously comply over the years 😂"*
>
> **Andrew (12:36 PM):** *"Because JiRA sucks? That's why Krystal had to 'comply'.*
>
> *In the future we can move wherever. While we're debugging looking at Jira hurtsy eyes and motivation"*

#### 3.4c Chuck (ATG) signal — buried in same Andrew message (12:36 PM)

> **Andrew (12:36 PM, follow-on):** *"Btw, Chuck is excited, wants to get his people to contribute. Asked if would like to present to ATG as well"*

**This is the biggest sponsor-stack signal of the day** (see §4 below).

#### 3.4d Asana continuation (12:44 PM – 1:21 PM)

> **Dylan (12:44 PM):** *"ouch. right. I don't know what's the alternatives for Asana. JIRA I'm not big fan. Sorry James."*
>
> **James (1:13 PM, quoting Dylan):** *"JIRA I'm not big fan. Sorry James.*
>
> *My wife said it's ok this time, only because [Pinterest] is up after hours."*
>
> **Andrew (1:21 PM):** *"The market reacted quickly learning that our team has started looking beyond jira"*

**Translation:**
- James's humor reply diffused the "Sorry James" moment with charming Di-style move — good political instinct, didn't get defensive about Asana
- Andrew's *"The market reacted quickly"* = light deflection, but signal that Asana decision will be scrutinized
- Engineering-culture-tribal Jira sensitivity is **real and named**; James needs a substantive answer when this comes back
- **Recommended reframe (not yet deployed):** *"The system writes back to whatever ticketing platform the team uses. Asana is V0 because that's where Reflex started; Jira-mode is a swap, not a rebuild."* — subordinates the tooling debate under the system thesis

### 3.5 Dylan → James DM (10:45–10:57 AM)

> **Dylan (10:45 AM):** *"Great job driving all the hard work*
>
> *I asked Andrew to rescope this project so it's not just on you anymore. We will do it this week."*
>
> **Dylan (10:57 AM):** *"You are doing fantastic, I just don't want to burn ppl out. Both this and anticipation cupcake."*
>
> **James (12:29 PM):** *"Thank you Dylan! I decided to sprint a bit here to make sure we can land meaningful milestones on both AI stuff + Anticipation. Thank you so much for the recognition and care! I full appreciate it.*
>
> *In terms of next steps, I will definitely be scaling back some of the active dev myself and focus on scaling the efforts so that it's sustainable long run. Excited to work with you on this and again, thanks for the opportunity!!"*

**Translation (multi-variant read; see §6 below for full analysis):**

Dylan is offering the **structural altitude shift** James has been preparing for: rescope Reflex so execution flows through Andrew + team, James operates at narrative + sponsor altitude. This is the literal control / lack-of-control irony David named on 5/1. *"Rescope so it's not just on you"* is **load redistribution + altitude positioning**, not ownership transfer.

James's reply landed correctly in writing — accepted the rescope (*"scaling back some of the active dev myself"*), named the altitude shift in his own words (*"focus on scaling the efforts so sustainable long run"*), thanked the recognition without deflecting. **Anxiety surfaced AFTER the reply, not in the reply.**

---

## 4. Sponsor Stack — updated mapping (post-demo)

Per the May posture section in `pre_june_readiness.md` — Sponsor Stack typology:

| Sponsor | Asset type | Pre-demo state | Post-demo state |
|---|---|---|---|
| **Dylan Wang** (manager + Director-track sponsor) | Existing all-types sponsor | Active sponsor | **Reinforced** — proactively forwarded James's doc to David Sun, added as editor; offered Andrew rescope; protected from burnout |
| **Matt Madrigal** (CTO) | **Platform sponsor** | Unknown (pre-demo) | **Active** — June 17 EPD all-team agenda slot; *"feature this further in future forums"*; cross-EPD curiosity |
| **Rajat Chaturvedi** (VP, James's skip) | **Scope sponsor + Platform sponsor** | 25% mental-model awareness (4/23 audit) | **Active** — *"lets pick up few tracks for productionization"*; scheduled productionization conversation at Wed 5/8 OH; *"go beyond P13N"* |
| **Faisal Farooq** (VP Eng - Safety and Signals) | **Credibility sponsor** | 25–50% (4/23 audit) | **Active** — VP-built-the-prior-version vouching; ML Flywheel learnings collab offer; DM follow-up substantive |
| **Chuck** (VP Eng - ATG; Jiajing's manager) | **Platform sponsor + Scope sponsor** (potential) | **0% (4/23 stretch target)** | **Active** — wants people to contribute + ATG presentation invite — went 0% → pulling in single demo |
| **David Sun** (delivery infra TL) | **Scope sponsor + Credibility sponsor** (TL altitude, not VP) | Unknown (pre-demo) | **Active** — ForgeDev/PR pilot infrastructure offer; brings cross-org build infrastructure |
| **Kartik** (Chief Architect) | TBD | Existing soft-fan (per backlog #81) | **Engaged** — Matt mentioned Kartik was asking questions during the demo (not yet direct contact) |

**Post-demo stack: 6 named active sponsors + 1 engaged but indirect (Kartik).** Pre-demo: 1 (Dylan).

**Per Ethan's frame from the 5/2 consult:** *"will multiple executives spend political capital on you when Dylan is gone/OOO and James is OOO?"* — the Sponsor Stack is now structurally redundant. Dylan-OOO-coverage is no longer single-point-of-failure.

---

## 5. 4/23 VP-target list — completion status

From `backlog.md` #79 *"VP-level RR narrative consolidation"* — the 4/23 audit list:

| 4/23 target | 4/23 mental-model % | Today's state |
|---|---|---|
| **Jeff** (peer VP, primary) | 0–10% | Anticipation-lead OH Tue 5/7 — in motion |
| **Rajat** (VP skip) | 25% (had PinSight 4/16 exposure but not RR-specific) | **Pulling: productionization tracks ask + Wed 5/8 OH locked** |
| **Faisal** (VP Eng, partner on UU for RR) | 25–50% | **Pulling: ML Flywheel learnings offer + DM follow-up** |
| **Chuck** (VP Eng, ATG, **stretch target via Jiajing intro**) | 0% | **Pulling: ATG presentation invite + people-to-contribute** |

**All four targeted VPs in motion within the calibration window.** Per the May posture / Ethan Q11 dashboard, this is **the configuration the calibration window was designed to detect, three weeks earlier than expected.**

Per Krishna's 4/23 advice (*"take opportunities outside when they present themselves"*) and Ethan's 5/2 *"manufacturing executive reasons to pull you in"* — the demo functioned as the manufactured pull-event for all four targets simultaneously.

---

## 6. The Dylan rescope message — multi-variant read

(Critical to dispatch BEFORE walking into 5/5 Dylan 1:1 — anxiety read of *"is she taking me off"* would be the wrong frame.)

| Variant | What she means | Probability |
|---|---|---|
| **A. Literal — burnout protection** | *"I saw you running hot. Sprint is over. Spread the load."* | High. Words at face value. |
| **B. Director-altitude reframe** ⭐ | *"At your next altitude you don't drive execution; you scale through others. Rescope = formalize that shift."* | **Highest.** This is what sponsors do post-major-win for promotion candidates. |
| **C. Calibration credit-balancing** | *"The win was team work, not just James. Distribute the narrative so calibration reads it as system, not solo hero."* | Medium-high. Director-altitude positioning. |
| **D. Andrew peer-dynamic protection** | *"Andrew is the named owner. Formalizing his primary ownership keeps the peer dynamic clean."* | Medium. Plausible secondary motive. |
| **E. Pulling James off the project** | *"Replace you, free you for something else, signal of distrust."* | **Very low.** Demo just landed. Pulling the just-won author = sponsor-sabotage. Dylan's not doing that. |

**Variants A + B + C are the actual read** — probably all three at once. None are negative. All three are the structural shape of a sponsor doing right by a Director candidate.

**The pattern to recognize:** anxiety read = IC-comfort instinct firing under success-pressure. Same shape as:
- 5/2 "should I ramp UPP technically?"
- 5/1 H1 doc over-interpretation
- 5/4 "is she trying to take me off"

3-for-3 in 4 days under high-stakes ambiguous sponsor signals. **Worth dedicated Coaching Patterns notebook session in a future Leo-session.**

---

## 7. Watch-outs

### 7.1 June 17 EPD all-team — calendar conflict ⚠️

Matt Madrigal anchored this publicly: *"We have an EPD all team... It's like in a month from now or something. June 17th probably."* James is OOO 6/1 → 6/30. June 17 is mid-OOO.

**Three options:**
1. **Push for alt date** — early-June pre-OOO (pre-6/1) or July post-OOO. Matt's framing (*"It's not on anyone's calendar yet though so don't freak out"*) suggests flexibility.
2. **Andrew solos** — visibility loss for James, but Andrew is named project owner so it's appropriate.
3. **James returns temporarily** — breaks G0 OOO discipline + China travel logistics.

**Recommended:** Bring to Dylan 1:1 5/5 first. Dylan can broker date with Matt. Default position: ask for alt date, fall back to Andrew solo if calendar can't move. Do NOT break OOO.

### 7.2 Four collaboration threads needing prioritization

1. **Faisal — ML Flywheel learnings collab.** Low-cost, high-credibility. Recommended: 1-hour scoping session with Faisal's team to extract ML Flywheel learnings on *"many candidates → which is ship-worthy"*. Don't open-ended commit.
2. **Rajat — productionization tracks beyond P13N.** High-stakes, high-scope. Wed 5/8 OH = working session. **Walk in with proposed list of tracks + resourcing ask, not asking-mode.**
3. **Matt — June 17 EPD all-team demo** (see 7.1). Resolve calendar via Dylan.
4. **David Sun — ForgeDev/PR pilot integration.** Soft commitment ask (*"try it in a repo"*). Bounded engagement only — 1-hour scoping conversation, not multi-week build. Ethan's bounded-ramp logic applies. Could solve build-half infrastructure problem.

**Plus Chuck (ATG) — presentation invite.** Date TBD. Bring up with Dylan to coordinate timing (likely post-Rajat OH 5/8 once productionization tracks are clearer).

---

## 8. Implications for upcoming

### 8.1 Dylan 1:1 — Tue 5/5 (TOMORROW) — highest-leverage hour of the week

**Frame:** orchestration mode, not defensive mode. Dylan reinforced you publicly today. The 1:1 is for orchestrating the post-demo demo-circuit and de-conflicting the four threads, not defending your spot on the project.

**Bring:**
- **June 17 conflict** — ask Dylan to broker alt date with Matt (preferred) or sign off on Andrew-solo (fallback)
- **Prioritization across four threads** — Faisal / Rajat / Matt / David Sun + Chuck — what's first? what waits?
- **Chuck ATG invite** — when does this happen, who attends?
- **Rajat OH 5/8 prep** — what tracks are James's proposals for productionization?
- **JJ written endorsement** — calibration-window critical-path; Dylan's part remains. **Now is the right ask given today's momentum.**
- **Headcount-back conversation** (was on backlog as pre-5/8 OH item) — bring it. The momentum gives leverage.
- **Anti-bring (don't lead with):** anxiety about "am I being taken off." Walk in already-resolved. The rescope is altitude promotion — accept it cleanly and move to orchestration.

### 8.2 Jeff OH — Tue 5/7

Per the 5/2b OH prep update (`work+self/people/jeff_rajat_office_hours_prep.md`): Jeff lead = **Anticipation 4-beat install spine** (WAU/representation → pin polysemy → CLR portability to Notif + Intelligent Boards → LLM-pUIC frontier); Reflex/EPD as fallback only. AI-leveraged-leader Q deferred to Rajat 5/8 → Dylan → DM Jeff 5/16-5/20.

**Today's demo doesn't change that.** Jeff isn't the right audience for the Reflex/Engineering-Agent narrative; he's the audience for Anticipation. Brief mention: *"EPD demo went well; the Engineering Agent execution layer is one piece of the broader Anticipation Foundations system"* — then back to the install spine.

### 8.3 Rajat OH — Wed 5/8

Per the 5/3 OH prep update: Q1 anchored on snorkel/scuba framework, Director-path-stays-under-Dylan locked, Q2-Q6 fully rewritten.

**Today materially changes the OH posture: it's now a working session, not a sales pitch.** Rajat himself said *"lets discuss the plan when we meet next."* James walks in with:
- Proposed list of productionization tracks (3–5 specific, not exhaustive)
- Resourcing ask (named heads, not vague ask)
- Cross-org coordination shape (who owns what, base team vs surface team boundaries from the cross_org_operational_model doc)
- The Dhruvil-co-pillar seam: *"Dhruvil owns depth; I own cross-org application + outcomes + scaling mechanism"*
- The June OOO coverage handoff for the productionization tracks

### 8.4 June 17 EPD all-team

See 7.1. Dylan-1:1 broker first.

### 8.5 ATG presentation (Chuck invite)

Date TBD. Coordinate via Andrew + Dylan after Rajat OH 5/8 (so productionization tracks are settled before adding ATG presentation surface area).

### 8.6 ForgeDev/PR pilot scoping with David Sun

1-hour conversation, not multi-week build. Bounded engagement. Likely week of 5/12 or later. Lower priority than Jeff/Rajat OHs.

---

## 9. Banking for self-review (Goal 4 evidence)

- **Live demo to ~3,700 with planned humor moment landing** (PM-agent / "which Andrew is real")
- **Live Q&A from CTO + VP Eng + cross-EPD curiosity** with no questions James couldn't handle (none came that exceeded the 15-question Q&A bank)
- **Same-day all five Q11 sponsor-cultivation signals firing**
- **All four 4/23 VP targets in motion within calibration window**
- **Dylan offered structural altitude shift** (rescope = altitude promotion, accepted cleanly)
- **Humor diffusion of Asana pushback** ("my wife said it's ok this time")

These are concrete Goal 4 (executive presence) and Goal 1.5 (narrative ownership) evidence for end-of-cycle self-review.

---

## 10. Cross-references

- `work+self/projects/pinsight/epd_demo_2026-05-04_prep.md` — pre-demo prep + Q&A bank (15 anticipated)
- `work+self/people/pre_june_readiness.md` — May posture section (Sponsor Stack typology, Q11 5-signal dashboard, calibration-window framework)
- `work+self/people/jeff_rajat_office_hours_prep.md` — 5/2b + 5/3 prep updates
- `work+self/H1_career_convo.md` — Dylan career convo (week of 5/20)
- `work+self/people/stakeholders.md` — full stakeholder profiles
- `backlog.md` #79 — VP-level RR narrative consolidation (4/23 list now complete)
- `backlog.md` #81 — Director-advocate cultivation (Andrew Y / Kartik / Faisal targets)
- `notebooklm/query_log.md` — Ethan Evans 5/2 consult (Sponsor Stack typology, 5-signal dashboard, bounded-ramp principle)
- `system/session-logs/2026-05-04.md` — today's session log (TBD when written)
