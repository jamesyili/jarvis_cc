# Jeff Office Hours Prep

**Purpose:** Self-contained prep for James's next office hours with Jeff Harrell (VP Engineering, Core — Rajat's manager).
**Last updated:** 2026-04-23
**Status:** Pending Dylan's OK via DM / next 1:1. Target: before Reflex-CTO demo if possible.

---

## Who Jeff is (short)

- VP of Engineering — Core. Rajat's manager. Reports to Matt Madrigal (CTO).
- DISC: High I/D. Loves demos, "cool work," engineering culture modernization.
- **Buys:** shipped tools, tangible artifacts, working things other people use.
- **Does NOT buy:** strategic decks, architect-of-transition narrative, abstract AI leadership framings.
- **Canonical reference:** Jeff's March 2026 org-wide email celebrated Roberto (Search Debugger), Phil, Aravindh — people with shipped tools that other teams used. NOT strategic-coordinator moves. **This is the dispatch rule.** See `journals_and_growth.md` Lesson 1.

---

## Where Jeff's mental model of James currently sits

**~0-10% per 2026-04-23 VP-consolidation audit.** Current association: "AI work in HF, that PINvestigator tool."

**What Jeff already knows:**
- PINvestigator demoed previously (all 5 post-demo follow-ups delivered by 2026-04-17)
- Dhruvil onboarded as PINvestigator user
- Eval harness shipped
- General "AI in HF" association

**What Jeff does NOT yet know about James (the consolidation gap):**
- RR is James's flagship — cross-org, metric-moving (WAU + holdout), CTO+CEO buy-in via Andrew's anticipation vision
- Pinsight is the data substrate for Reflex
- Cross-org Pinsight adoption happening organically — Dimitra (Notifications EM) forked James's repo and built HF+Notif+Search version, Darren's team contributing, Francisco's team joining, Dafang interested
- James is the technical anchor of Reflex per Andrew's 4/21 public designation
- Reflex-CTO demo is coming (Andrew setting up with Matt Madrigal)
- Execution-agent prototype in flight (cross-project blocker, Dylan is unblocking)

**Target state after OH:** Jeff's mental model of James = "RR lead + Pinsight-as-Reflex-substrate + technical anchor of Andrew's vision." Target 75%+ consolidation.

---

## Canonical DON'Ts

- ❌ **Do NOT re-demo PINvestigator.** He's seen it. Repeating is no new information; wastes the slot.
- ❌ **No Director timeline / calibration questions.** Office hours is not that conversation.
- ❌ **No Krishna / Roberto / Dhruvil / Yan / Kurchi comparisons.** Ever.
- ❌ **No Reddit or external optionality.** Irrelevant here.
- ❌ **No strategic deck / slides / 1-pager.** Lesson 1.
- ❌ **No complaints about visibility.** Not even framed politely.
- ❌ **No ask in first OH.** Install associations + named things first. Asks come later once Jeff is advocate.
- ❌ **No more than 50% of the talking.** Jeff is high-I. Let him engage.
- ❌ **Never use the word "escalation"** (locked from Jan 2026 UPP/Matthew incident — applies across all leadership conversations, not just Dylan).

---

## The opening line (memorize)

If Jeff says "what's going on?" or "what's new?" — your open is:

> *"A lot. Let me give you the short version on three things — RR is now cross-org with real metric movement, Pinsight is getting organic pull from three teams, and Andrew and I are demoing Reflex to Matt in a few weeks. Which one do you want to go deeper on?"*

**Why this works:**
- Three sentences, three associations Jeff doesn't currently have.
- Names three things by name (RR, Pinsight, Reflex) — installs them as James-adjacent in his head.
- Ends with him choosing. Di engages; Jeff picks the thread that interests him most.
- Avoids pitch mode. You're offering, not pushing.

**Rambling index watch:** any additional sentence after "Which one do you want to go deeper on?" is anxiety talking. Stop. Let him choose.

---

## Three primary topics (Jeff picks what to go deep on)

### Topic 1: Retentive Recommendations — business impact + cross-org ownership (NEW to Jeff)

**If Jeff picks this:**

> *"My team's been driving RR for ~6 months. We're moving WAU and holdout in shadow — the first recsys initiative at Pinterest to have a clear mechanism rather than a one-off launch. Three orgs are now building roadmaps around it: Dylan's team (me driving), Bo Zhao's org in Content Quality (partnering on UIC signal quality), and ATG (building the predicted UIC model — that's where anticipation vision goes from metric-moving to paradigm shift). Paper in draft for KDD 2026, Engineering Blog post in review."*

**What this does:**
- Establishes James as THE lead ("my team's been driving this"). Not "I've been contributing to." Direct ownership language.
- Gives him a metric (WAU + holdout) — Jeff buys numbers.
- Names three orgs — cross-org pull, the calibration-relevant signal.
- Names the next proof point (predicted UIC) — invites him to track follow-up.
- KDD + blog = durable artifacts — Jeff respects shipped writing.

**If he asks follow-ups:** answer concretely, numbers-first. Keep each answer to 2-3 sentences.

**Candidate follow-up question from you:** *"Retention is company-level KPI territory — would it be useful to brief you on the mechanism before predicted UIC lands, or would you prefer to see the proof point first?"* (Lets him choose pace; signals you respect his time.)

---

### Topic 2: Pinsight — cross-org adoption (NOT a re-demo, a narrative update)

**If Jeff picks this:**

> *"PINvestigator turned out to be the v0. We built Pinsight on top — the data substrate for Andrew's Reflex vision. Something interesting happening organically — Dimitra in Notifications cloned it and built her own version for notif + HF + search. Darren's team is contributing. Francisco's team is joining. Dafang is joining. Nobody asked them to. That's pull, not push."*

**What this does:**
- Immediate Lesson 1 payoff: you're not pitching what you built — you're telling him other teams are using it unprompted.
- Names four cross-org contributors by name (Dimitra, Darren, Francisco, Dafang). Names = narrative stickiness.
- "Pull not push" is Jeff-coded — he remembers Roberto for this exact shape.
- Connects Pinsight → Reflex → Andrew → anticipation vision (chain of pre-existing exec buy-in).

**Key discipline:** do NOT open the tool and demo. He's already seen PINvestigator. This is a *narrative update about propagation,* not a demo.

**If he asks "what's Pinsight specifically":** 2 sentences.
> *"It's the sensing + diagnosis layer for the recommendation stack. Detects funnel issues, diagnoses root causes in natural language, surfaces specific experiments to run. It's what PINvestigator was trying to be, built more structurally."*

---

### Topic 3: Reflex-CTO demo teaser (the positioning move)

**If Jeff picks this:**

> *"Andrew's setting up a Reflex demo with Matt in the next few weeks. He's asked me to present the technical side alongside him. Wanted to flag it so you're not surprised."*

**What this does:**
- Tells Jeff CTO-level exposure is coming without making you look like you're bragging (you're just flagging for operational courtesy).
- "Andrew's asked me" frames Andrew as the sponsor — you're not self-designating, someone more senior than you is. This is Dylan's own sponsor pattern reflected here.
- Leaves Jeff room to ask substantive questions about Reflex (which he will, because he's high-I and curious about AI).
- Respects the reporting hierarchy — he's Matt's direct report, so you briefing him before the fact is operationally correct.

**If he asks "what's Reflex":**
> *"Andrew's anticipation vision — the full sensing → simulation → build → prove loop for our recommendation experiments. Pinsight is the Detect + Diagnose layer. The demo will show how the loop works end-to-end on a real HF investigation."*

**Watch-out on this topic:** don't over-narrate Reflex's strategic importance. Andrew owns that narrative. You own the technical anchor piece. Stay in your lane.

---

## Bonus (only if time and if he's engaged): Execution-agent prototype

**Only offer if:**
1. Prototype is actually working as of demo day
2. Jeff has leaned into the conversation and time remains
3. He's asked something that connects naturally

**The pitch:**

> *"Dylan and I identified execution agents — the coding agent that implements recsys experiments end-to-end — as the cross-project blocker for both Pinsight and Reflex. I've been heads-down prototyping one. Want to show you the build-stage prototype?"*

**If yes:** open the laptop, run one end-to-end execution. ~3 min. Let the tool speak.

**If he doesn't bite:** drop it cleanly. Don't force it. You have other slots.

**Why this could land:** it's the 2026 Roberto-parity move — shipped tool, novel capability, clear cross-org applicability. If it lands with Jeff, it cements you as an AI-native builder-leader. But only if it's demonstrably working. Do not demo something half-working.

---

## Close the OH (last 30 seconds)

**ONE curious question that pulls Jeff into talking.** Pick one:

1. *"What are you seeing across the Core ML orgs on AI-native engineering culture? Where do you think we're under-investing as an org?"*
2. *"I've been thinking about what 'excellent senior ML EM' looks like in 2027 — what are you looking for as you think about bench depth?"*
3. *"If you could wave a wand and have one AI-native capability land at Pinterest by end of year, what would it be?"*

**Recommended: #1.** It invites his strategic read on org-wide AI culture — high-I VPs love sharing this. And it positions you as someone thinking at that altitude.

**Then thank him, no ask, leave room for HIM to offer.** If he volunteers something (*"you should come talk to X"* / *"I'll watch for the predicted UIC result"*) — accept gracefully. If not — also fine. First OH post-consolidation-reset is about installing the mental model, not extracting asks.

---

## Pre-OH checklist (do the day before)

- [ ] Confirm the opening line out loud until it's natural
- [ ] Confirm the three topics — each 3-4 sentences max, rehearsed out loud
- [ ] Have numbers ready for RR: WAU delta (shadow experiment), holdout movement, timeline
- [ ] Have the Pinsight contributor names ready: Dimitra (Notifications), Darren, Francisco, Dafang
- [ ] Know Andrew's current Reflex pitch framing so you don't contradict him
- [ ] Close the laptop and walk before you walk in — Tai Chi base, not hyped
- [ ] Remember: Jeff is a peer-to-Matt who reports to CEO. High-I but very busy. Respect his time.

---

## Post-OH debrief (write up within 1 hour)

Capture:
- What Jeff picked to go deep on (tells you what his mental model now prioritizes about James)
- Any specific language he used (file it — that's his current frame)
- Any follow-ups he suggested or offers he made
- Your read on how RR / Pinsight / Reflex registered
- Any adjustment for the Reflex-CTO demo

Update:
- `dylan_career_conversation_prep.md` — VP consolidation plan (Jeff % moved where?)
- `stakeholders.md` — Jeff section if not already rich enough
- This file — what worked, what to adjust next time

---

## Reminders: the dispatch rules that apply here

1. **Jeff buys demos and shipped tools, not strategy.** (Lesson 1)
2. **Show, don't narrate.** (Lesson 4)
3. **Pull not push.** (Lesson 1 corollary)
4. **Rambling index scales with stakes — cap each answer at 2-3 sentences.** (communication.md)
5. **No "escalation" language — ever.** (Jan 2026 lock)
6. **Match altitude to audience appetite.** (Lesson 1, foundational)
7. **Three-beat managing up is for Dylan, not for Jeff.** Jeff is higher-altitude, less cognitive-load-sensitive than Dylan. Don't force the frame.
