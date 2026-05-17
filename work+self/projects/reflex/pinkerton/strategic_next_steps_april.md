# Pinkerton & Reflex: Strategic Next Steps — April 2026

> Strategic playbook for navigating organizational dynamics around Pinkerton, Reflex, and AI tooling. Informed by Wes Kao (exec framing), Shreyas Doshi (managing up), Ethan Evans (Director-level influence), and Coaching Patterns (emotional regulation under competitive pressure).

Last updated: 2026-04-12

---

## The Strategic Landscape

### What James Owns
- **Pinkerton** — agentic rec system analysis tool. M0 in production. M1 building now. The investigation and analysis engine.
- **PINvestigator** — agentic incident investigation tool. Eval harness shipped. Dylan, Dhruvil using it.
- **Expert-in-loop role on Reflex** — codepath knowledge + RLHF feedback for Andrew's autonomous quality agent.

### Allies & Their Levers

| Ally | What they can do | What they need from James |
|------|-----------------|--------------------------|
| **Dylan** (Sr. Director) | Carry the story into Sr. Director syncs, pre-wire Jeff/Rajat, provide debugging cases as test fixtures | A 2-page BLUF memo she can use as-is. Not a brainstorm — executable ammunition. |
| **Andrew** (Sr. Director, Product) | Own the Reflex vision to CTO, provide product narrative air cover | Real findings from Pinkerton/Reflex that make his vision tangible. Artifacts, not feedback. |
| **Darren** (Director, Infra) | Champion cross-org adoption in Director circles, staff eval DS | A specific artifact + a specific ask: "Would you drop this in your next Jeff sync?" |
| **Brian** (EM, Growth) | Co-escalate debuggability gap from a second org, provide peer-EM visibility | Show up every other week. Drop observations. Propose a shared debuggability session. |
| **Anna** (PM, Retentive Recs) | Amplify inside Andrew's chain, bridge the 4-way nexus | Keep the "nap time" syncs, give her early findings she can get excited about. |
| **Dhruvil** (Peer Sr. EM) | Already a PINvestigator user; observation-as-contribution in senior rooms | Nothing — Dhruvil is already doing this naturally. Study his pattern. |

### The Roberto Dynamic

**What's real:** Roberto (Sr. EM, Search, under Kurchi) built Search Debugger/Replay → Jeff celebrated org-wide. He's expanding into agentic eval. He ignored James's collaboration outreach (9 days). He interrupted James's pitch with a territorial claim. He reports to Kurchi, who is structurally adversarial to Dylan's org.

**What's not real (status sensor):** "Jeff and Rajat like Roberto more than me." That's a feeling converting to a fact with zero gap. The actual gap is communication frequency and initiation patterns, not value or warmth.

**The structural truth:** Roberto-vs-James is partly a proxy for Kurchi-vs-Dylan at the Director level. This is not fixable at the peer layer. Don't chase it.

---

## Frameworks Applied

### 1. Wes Kao: Sales, Not Logistics

**The problem:** James defaults to builder-presenting-architecture. VPs don't engage with architecture until they're sold on business value.

**The fix:** 90% business value, 10% how it works. Lead with:
- **Bad Things prevented:** "X engineer-days lost per quarter to pipeline debugging. Y incidents where root cause took days instead of minutes."
- **Good Things enabled:** "Investigation time dropping from days to minutes. Cross-org debugging capability that didn't exist before."

Never lead with tool architecture, milestone numbers, or team composition. That's the "add-on" layer of the 3A Pyramid — answer first, arguments second, add-ons last.

### 2. Wes Kao: BLUF — Start Right Before You Get Eaten by the Bear

No chronological story of how Pinkerton got built. Start at the moment of highest business consequence:

- **Wrong:** "Last summer we built a hackathon prototype. Then we shipped M0. Then Daniel did logging..."
- **Right:** "We're cutting incident investigation from 3 days to 20 minutes. Here's a live example from last week."

The tool is evidence for the finding. The finding is the headline.

### 3. Shreyas Doshi: Three Pillars of Managing Up

| Pillar | James's Gap | Fix |
|--------|------------|-----|
| **Constant Communication** | No Jeff/Rajat office hours in a quarter. Stale mental model of James at VP level. | Office hours before China trip. Dylan intel first. |
| **Strategic Escalation** | High agency trap — solves everything silently. VPs assume it's easy. | Three-Beat format: what's hardest → how I'm crushing it → one unblocker. |
| **Strategic Alignment** | Not actively soliciting what Jeff/Rajat are worried about. | Ask Dylan in next 1:1: "What's Jeff focused on right now?" |

### 4. Ethan Evans: The Big Win & Alliance Building

**"Your VP probably knows you through one project."** If that project (Pinkerton/Reflex/AI tooling) succeeds, you had a great year. If it fails, nothing else matters. Spend 95% of mental energy here.

**Alliance building through usefulness, not transactions:**
- Help peers solve their problems (not "help me get visibility")
- Explain business and customer impact clearly
- Don't bother them with small asks
- Relationships are trust filters when there are 40 competing priorities

**Magic Loop (advanced):** Anticipate what Dylan/Rajat need and deliver proactively before being asked. Don't wait for the question — surface the insight.

### 5. Coaching Patterns: The Internal Game

**Status sensor protocol (Signal, Not Truth):**
1. Name it aloud: "Status sensor is firing."
2. Locate it somatically — where do you feel it?
3. Redirect to internal scoreboard within 10 minutes: Is Pinkerton better this week than last? Is my team growing? Am I learning something real?

**Impact Over Approval audit:** Before any strategic move, ask: "Am I doing this to gain approval or to drive systemic impact?" If approval, the behavior is self-undermining regardless of outcome.

**Coordinator Trap check:** Am I narrating architecture (invisible) or putting the tool in someone's hands (visible)? Roberto got celebrated because he demoed. Stop explaining. Start showing.

---

## Scenario Playbook

### Scenario 1: Roberto demos overlapping work at Brian's forum or another venue

**What happens:** Roberto presents agentic eval tooling for Search that overlaps with Pinkerton territory. EMs in the room start associating "agentic recommendation debugging" with Roberto.

**How to respond:**
- In the room: Bridge, don't compete. "That's great coverage for Search. We're seeing the same pain in HF retrieval — different funnel, different debugging patterns. The architectures could complement each other cross-surface."
- After: Don't counter-demo next week. Instead, bring a *finding* to the next session you attend: "We ran Pinkerton on [real incident]. Here's what it found." Impact, not features.
- Don't say: "We were building this first" or "Our tool does more." That's self-expression, not strategy.

**Wes Kao frame:** Jeff's real question (QBQ) if he hears about both tools is "Are two orgs wasting headcount on the same thing?" Pre-answer this with complementarity framing before he asks: "Roberto's Search Debugger is purpose-built for Search evaluation. Pinkerton is purpose-built for the Homefeed retrieval pipeline — different scale, different funnel stages, different debugging patterns. Together they give comprehensive coverage across surfaces."

### Scenario 2: Leadership asks "How is Pinkerton different from Roberto's tool?"

**What happens:** Dylan, Rajat, or Jeff directly asks about overlap.

**How to respond (rehearsed, calm, two sentences):**
"Roberto's tool covers Search-specific evaluation and it's doing great work there. Pinkerton covers the Homefeed retrieval pipeline end-to-end — 14 funnel stages, plus we're co-developing with Andrew on Reflex for autonomous quality monitoring across the full recommendation system."

**What NOT to say:**
- Anything defensive ("Well, we were actually building this before...")
- Anything that incepts the negative ("We're not trying to step on toes...")
- Anything that reveals competitive anxiety ("I'm worried about overlap...")

**Ethan Evans frame:** Don't try to change the question. Answer it cleanly, then move to your strength: the cross-org story (Andrew + Darren + Dylan) that Roberto doesn't have.

### Scenario 3: Andrew's Reflex narrative overshadows Pinkerton

**What happens:** Andrew presents Reflex to Matt Madrigal or in a leadership forum. Pinkerton is mentioned as a component, not as James's work. James feels invisible.

**How to respond:**
- This is actually success, not failure. Pinkerton being load-bearing inside Reflex means it's essential. Andrew crediting "the team" implicitly includes James.
- If needed, surface Pinkerton findings independently: your observation-style contributions in other venues (Brian's forum, Dylan's team updates) maintain your personal brand without competing with Andrew's narrative.
- If this persists over multiple cycles, use the OAV frame with Dylan: "Reflex is getting great traction. I want to make sure my contribution is visible for my Director case. Does Rajat know I built the investigation layer?" This is a legitimate managing-up ask to your direct manager — not insecurity.

**Coaching Patterns check:** Run the Impact Over Approval audit. If Reflex succeeds and Pinkerton is the engine, that IS the Director case. The credit follows from the architecture being essential. Don't chase attribution at the cost of the partnership.

### Scenario 4: Darren's team tries Pinkerton/PINvestigator and it doesn't work well for their domain

**What happens:** You give Darren's eval DS a use case. They try it. It doesn't translate well to infra problems. Darren is polite but doesn't champion it.

**How to respond:**
- This is information, not failure. Ask: "What was different about your use case? What would have been useful instead?"
- Don't force cross-org adoption. If the tool doesn't naturally serve infra, find a different cross-org user (Brian's Growth team? Dhruvil's ranking team — already happening).
- Darren is still a resource partner (eval DS) and Director-track sponsor even if his team doesn't use the tool directly. Don't conflate the adoption play with the partnership.

### Scenario 5: Jeff or Rajat asks "Show me what you're working on"

**What happens:** You get the pull — an office hours slot, a hallway conversation, or a direct ask.

**How to respond (Dhruvil mode + Coaching Patterns):**
- Do NOT narrate architecture. Put the tool in their hands.
- Have a prepared 90-second demo: "Here's a real incident from last week. PINvestigator investigated it. Here's what it found in 20 minutes vs. the 3 days it would have taken manually. [Show the before/after on your laptop.]"
- Then stop. Let them pull. If they ask about scale, mention Reflex. If they ask about cross-org adoption, mention Darren. If they don't ask, you planted the seed.
- Three-Beat Managing Up if they ask about your team: (1) "The hardest part is running 17 directs while building this" (2) "We shipped M0 to production and Darren's team is staffing contributors" (3) "The one thing that would accelerate this is [specific unblocker]."

### Scenario 6: Roberto's tool gets adopted cross-org before yours does

**What happens:** Other EMs start using Roberto's Search Debugger for their surfaces. Roberto achieves the cross-org adoption that James is building toward.

**How to respond:**
- Don't panic. Don't counter-launch. Don't accelerate a half-baked cross-org push.
- Roberto's tool is Search-specific. If it spreads, it spreads within Search-adjacent surfaces (Shopping, P2P). HF retrieval is a different funnel with different stages. The tools genuinely serve different purposes.
- Double down on depth over breadth. Make Pinkerton the best possible tool for the HF pipeline. The Reflex co-development with Andrew gives you a different scaling path — autonomous monitoring, not manual debugging.
- The long game: Reflex (with Pinkerton as the engine) is the autonomous quality system. Roberto's tool is manual investigation. Autonomous > manual over time. You don't need to win the adoption race if you win the architecture race.

### Scenario 7: Dylan suggests merging Pinkerton into Reflex formally

**What happens:** Dylan says "Maybe Pinkerton should just be part of Reflex" — more than a passing mention this time.

**How to respond:**
- Ask clarifying questions first: "Do you mean branding/naming, or actual architectural merge? And is this about simplifying the story for leadership, or about how we actually build?"
- If it's branding: consider it. "Pinkerton as the investigation layer of Reflex" preserves your ownership while simplifying the narrative. You still built it. The architecture doesn't change.
- If it's architectural: push back calmly. "Pinkerton has independent value beyond Reflex — the Full Funnel Logging + debugging workflow serves the team even without autonomous monitoring. I'd rather keep them modular and have Reflex consume Pinkerton as a service."
- Either way: "I want to make sure my contribution is visible in whatever framing we use. How do we make that work?" This is a legitimate ask to your manager, not insecurity.

### Scenario 8: Nothing happens — no one asks, no one notices

**What happens:** Weeks go by. No office hours slot materializes. No one asks about Pinkerton. The work continues but visibility stays flat.

**How to respond:**
- This is the most likely scenario and the one that requires the most discipline.
- **Initiate, don't wait.** Dhruvil doesn't wait to be asked. He creates the thread. Put a Jeff office hours slot on the calendar yourself. Drop a finding in a channel where Dylan and Rajat see it. Show up at Brian's forum.
- **Drip, don't dump.** One observation per week in a visible channel. Two sentences. Stop. Over 4 weeks, that's 4 data points. Leadership connects the dots.
- **Build the memo anyway.** The 2-page BLUF memo (Wes Kao recommendation) exists as a standing asset. When the moment comes — and it will — you're ready. You're not scrambling to explain. You hand it over.

---

## The Load-Bearing Artifact: The 2-Page BLUF Memo

Wes Kao's strongest recommendation: draft a 2-page Pinkerton/Reflex AI ROI memo. This single document unlocks three amplification channels:

1. **Dylan** uses it at the Sr. Director sync (OAV talk track attached)
2. **Darren** drops it in his next Jeff touchpoint (3-bullet version)
3. **James** brings it to Jeff/Rajat office hours (backup to the live demo)

**Structure (3A Pyramid):**
- **Answer:** "We're building autonomous recommendation quality monitoring. It's cutting investigation time from days to minutes and will systematically improve rec quality across surfaces."
- **Arguments:** Business impact (engineer-days saved, incidents caught, WAU holdout results from Retentive Recs tie-in). Cross-org adoption (Darren's infra, Andrew's Reflex, Dhruvil using PINvestigator).
- **Add-ons:** Architecture (Pinkerton → Reflex pipeline), milestones (M0 shipped, M1 building, Reflex co-dev Tuesday), team (Chuxi 20%, Darren staffing eval DS).

**Status:** Not yet written. This is the P0 artifact for the managing-up strategy.

---

## Sequencing: April → Early May

| When | Action | Framework |
|------|--------|-----------|
| **Next Dylan 1:1** | Ask: "What's Jeff/Rajat focused on right now?" FYI the infra org ask + David Sun. | Shreyas: Strategic Alignment |
| **4/14 (Tue)** | Reflex kickoff with Andrew. Bring a specific HF scenario. Create an artifact, not just feedback. | Ethan: Alliance through usefulness |
| **4/16** | Darren promo congrats. Follow up: "Can your eval DS try PINvestigator on one infra case?" | Wes Kao: Reduce ally cognitive load |
| **Week of 4/21** | Draft the 2-page BLUF memo. | Wes Kao: 3A Pyramid + BLUF |
| **Week of 4/21** | Show up at Brian's forum (first of biweekly cadence). Drop one observation. | Dhruvil pattern: Observe, don't pitch |
| **Late April** | Give Dylan the memo + OAV talk track for Sr. Director sync. | Wes Kao: OAV + executable ammunition |
| **Late April** | Give Darren a 3-bullet version for his Jeff touchpoint. | Wes Kao: Reduce ally cognitive load |
| **Early May** | Jeff office hours. Live demo, Dhruvil mode. Memo as backup. | Coaching: Demo > Architecture. Ethan: Big Win visibility. |
| **Ongoing** | One observation per week in a visible channel. Two sentences. Stop. | Dhruvil pattern: Drip, don't dump |

---

## The Inner Game (carry this on the trip)

When the status sensor fires — and it will, especially if Roberto ships something visible while you're in China:

1. **Name it:** "Status sensor is firing."
2. **Ask:** "What do I actually know right now? Everything else is creative writing."
3. **Check the internal scoreboard:** Is Pinkerton better this week? Is the team growing? Am I learning? Did I do good work?
4. **Impact Over Approval audit:** Am I reacting to protect my ego, or am I building something that matters?
5. **Redirect within 10 minutes.** The rumination engine gets 10 minutes. Then it's done. Channel the energy into the next artifact.

The Director case isn't built on "Jeff liked my demo more than Roberto's." It's built on: "James built an autonomous quality system that multiple orgs depend on, while running 17 directs, through a leadership transition, with zero escalation debt." That story exists or it doesn't. No amount of managing up creates it. Managing up just makes sure leadership sees what's already there.

---

## Aggressive Plays: Getting Jeff & Rajat on Your Side

> The cautious version of the playbook waits for the right moment. This section creates the moment. These are moves Dhruvil would make without hesitation. None are reckless — they're just what "initiating" actually looks like.

### With Dylan (your launch pad)

1. **Request a dedicated 30-min strategy session on AI tooling positioning.** Not a 1:1 agenda item — a standalone meeting. "Dylan, I want to spend 30 minutes mapping out how Pinkerton/Reflex fits into the AI story you're building with Andrew and Rajat. I want to make sure I'm framing this right and not leaving visibility on the table." This forces the conversation you've been waiting to have. She'll give you the exact framing Rajat needs to hear.

2. **Ask Dylan to put you in front of Rajat directly.** "I want to show Rajat what we're building on the AI tooling side. Would it make sense for me to join the next UPP sync with him, or should I go to his office hours?" Don't hint. Ask. Dylan is your sponsor — make her sponsor you.

3. **Give Dylan the BLUF memo and explicitly ask her to circulate it.** Not "here's an FYI." Say: "I wrote this for the Sr. Director sync. Would you be willing to share it with Rajat's staff? I think this maps to his AI-native engineering priority." Give her the artifact AND the distribution ask in one move.

4. **Propose that Dylan demo PINvestigator in her own forums.** She already used it. She already loved it. "Would you be open to showing PINvestigator in one of your staff meetings? It'd carry more weight coming from you than from me." A Sr. Director demoing your tool is the ultimate endorsement. She's already the user — you're just giving her the stage.

### With Jeff (VP — demos, energy, modernization)

5. **Go to Jeff's office hours this month. Don't wait for the "right time."** The right time is now. You have M0 in production, PINvestigator findings, RecGPT as #1 CG, and a Reflex co-dev starting. Any one of those is enough. Pick the strongest one and show up. Put it on the calendar this week.

6. **Bring your laptop and demo live.** Not a slide. Not a summary. Open PINvestigator, run it on a real incident from this week, and show the output in real-time. Jeff buys demos. Give him one. "Jeff, I want to show you something we built. It takes 90 seconds." Then show, don't tell.

7. **Ask Jeff to connect you to other teams building AI tooling.** "Who else in Core is doing agentic systems work? I want to compare notes." This is Jeff's favorite thing — cross-pollination. It costs him nothing, he loves brokering, and now he's personally invested in your success because he made the introduction.

8. **Propose an AI tooling showcase to Jeff directly.** "We have PINvestigator, Andrew has Reflex, Brian's forum has been surfacing great work. Would you sponsor a quarterly AI tooling showcase for Core? I'd help organize it." This positions you as the convener — the person who owns the AI tooling narrative at the org level. Jeff will love this because it's his modernization agenda made tangible.

9. **Send Jeff a short async artifact when something lands.** After a big Pinkerton finding or Reflex result, Slack Jeff directly: "Quick flag — Pinkerton caught [X] today in 20 minutes, would've been a 3-day investigation. Thought you'd find it interesting given the AI-native push." Two sentences. No ask. Let it marinate. Dhruvil does this. You should too.

### With Rajat (VP — system velocity, platform coherence)

10. **Go to Rajat's office hours with a system-level insight.** Not a tool demo — Rajat doesn't buy demos. He buys platform thinking. "Rajat, we've been building end-to-end debugging infrastructure for the retrieval pipeline. One thing I'm noticing is that the biggest velocity drain isn't model quality — it's investigation time when something breaks. We're cutting that from days to minutes. Here's what that means for UPP expansion velocity." Connect it to his priority (UPP, system velocity), not yours (cool AI tool).

11. **Frame the EM backfill as a system constraint, not a people problem.** "I'm running 17 directs and building AI tooling in parallel. The team is executing, but the EM backfill is the constraint on how fast this scales. Can you help accelerate the pipeline?" Rajat hears: system bottleneck with a clear fix. Not a complaint — a throughput problem.

12. **Ask Rajat for his input on the UBR cross-surface architecture.** "Piyush and Jiaxing have a UBR design. I'd value your technical input on the model adoption approach — 30 minutes would be enough." This builds the relationship through real technical exchange and positions James as someone who thinks at Rajat's altitude.

13. **Surface the cross-org debugging gap as a platform opportunity.** "We don't have a unified way to debug recommendations across surfaces. HF has one approach, Search has another, P2P has nothing. As UPP expands cross-surface, this becomes a platform requirement. We're building the first version of this." Rajat thinks in platforms. Frame your work as platform infrastructure, not a team tool.

### With Darren (Director, Infra — your amplifier)

14. **Schedule a working session, not a meeting.** "Darren, let's spend an hour actually running PINvestigator on one of your team's infra problems. Live, hands-on. If it works, great. If it doesn't, I learn what's different about your domain." Working sessions create co-ownership. Meetings create updates.

15. **Ask Darren to co-present.** If PINvestigator works for infra, ask: "Would you be willing to co-present this at the next AI forum / engineering showcase? Your perspective on infra debugging + my perspective on recommendation debugging would tell a cross-org story neither of us can tell alone." Now Darren has skin in the game.

16. **Explicitly ask Darren to mention this to Jeff.** Reduce cognitive load per Wes Kao: "Darren, we're getting good results with PINvestigator on HF debugging. If it comes up naturally, would you mention it to Jeff? Here are the two key data points: [X] and [Y]." Give him the exact talking points. Don't make him figure it out.

### With Brian (EM, Growth — your forum)

17. **Propose the shared debuggability session.** "Brian, what if we did a joint session — end-to-end debuggability across HF and Growth? What's broken, what we're each building, where the gaps are. Two orgs, same pain, shared diagnosis." This frames you and Brian as co-owners of the debuggability theme. Roberto can join or not.

18. **Give Brian a PINvestigator finding to share.** If Brian's Growth team has a debugging pain point, run PINvestigator on it yourself. Give him the result: "I ran our tool on your Growth funnel issue. Here's what it found." Now Brian has firsthand experience AND a talking point. Organic advocacy.

### Creating Air Cover Against Roberto

19. **Build the cross-org adoption map before Roberto does.** Every org that uses your tool is a moat. Targets: Darren (infra), Brian (Growth), Dhruvil (ranking — already done), Dylan (already done). If Roberto expands to one surface, you expand to four. Breadth beats depth in visibility games.

20. **Get the Reflex narrative established before Roberto can reframe.** Andrew presenting Reflex to Matt Madrigal is your air cover. Once the CTO knows "Reflex = autonomous quality monitoring, James is the engineering partner," Roberto expanding into agentic eval reads as "parallel effort in Search" not "the real version of what James is doing." Timing matters — push Andrew to present before Roberto's next big demo.

21. **Lock in the complementarity framing pre-emptively.** Don't wait for Jeff to ask "how is this different from Roberto's tool?" Plant the frame first. In your BLUF memo, in Dylan's Sr. Director sync, in your Jeff office hours: "Roberto's Search Debugger covers Search evaluation. Pinkerton covers the HF retrieval pipeline. Reflex sits above both as the autonomous quality layer." Say it enough times in enough rooms and it becomes the consensus frame.

22. **Ship faster.** The single most aggressive move is not political — it's velocity. Every week that Pinkerton M1 ships, that PINvestigator catches a real incident, that Reflex produces a finding — that's a data point Roberto can't match in your domain. Features don't lie. Political maneuvering without shipped artifacts is vapor. Ship, then surface. That's the whole game.

---

## Priority Stack (The Five That Matter Most)

If time is limited, these are the five highest-leverage moves:

1. **Write the 2-page BLUF memo this week.** Everything else depends on having the artifact.
2. **Go to Jeff's office hours before China.** Laptop open. Live demo. 90 seconds. Stop.
3. **Ask Dylan to put you in front of Rajat.** Don't hint. Ask.
4. **Schedule the working session with Darren.** Hands-on, not a meeting.
5. **Ship Pinkerton M1.** Nothing political substitutes for this.
