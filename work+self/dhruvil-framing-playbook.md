# How Dhruvil Would Frame It

> A reference for James: Dhruvil's communication patterns distilled from observed interactions. Use this as a pre-flight check before any leadership-visible thread, office hours, or senior meeting.

Last updated: 2026-04-18 (added April 5 P6 incident case study)

---

## The Core Pattern: Observation, Not Advocacy

Dhruvil never pitches. He surfaces. He frames contributions as observations from the field, not arguments for a position. Leadership comes to him — he doesn't go to them with asks.

**The formula:**
1. One observation connected to a priority leadership already has
2. One proof point or specific example
3. Stop. Let them pull.

**What's always absent:** "My vision." "We need." "I think we should." Ownership claims. Resource asks. Explanations of why this matters. If it matters, they'll ask.

---

## Dhruvil vs. James Default

| Dimension | Dhruvil | James (default) |
|-----------|---------|-----------------|
| Initiates vs. reacts | Creates the thread, tags up | Joins after the thread is resolved |
| Framing | Business impact, 2 sentences | Technical detail, full context |
| Ask style | Doesn't ask — surfaces, gets pulled | Builds the case, then makes the ask |
| Leadership tags | Tags CTO, VP directly | Waits for invitation |
| Inclusion | Generous ("James can confirm") | Credits others but doesn't create the moment |
| In meetings | Observation-as-contribution, 1-2 sentences | Silence (safe) or advocacy (effective but costly) |
| After contributing | Stops. Doesn't expand unless pulled | Keeps explaining |

---

## Templates: How Dhruvil Would Say It

### On-call / debuggability gap
**James default:** "Our team has a significant on-call burden. X% of pages are upstream pipeline noise we can't fix. The infra AI tooling isn't addressing this. We need help — either a partnership with infra or temporary resourcing to bridge the migration."

**Dhruvil version:** "We're spending [X] engineer-days per quarter on pipeline debugging that's mostly upstream noise. We've been experimenting with agentic tooling that cuts investigation time from days to minutes. Feels relevant to the AI-native engineering push."

### Cross-surface UPP wins
**James default:** "UPP delivered 5 LRs across Notifs and HF. The cross-surface architecture is working. We proved that unified approaches work where we expected them to break. In Q2 we should default to unified-first."

**Dhruvil version:** "Interesting signal from UPP — unified models are working across surfaces where we expected to need divergent solutions. Notifs and HF both improved from the same base. Could simplify the cross-surface roadmap significantly."

### Agentic AI tools
**James default:** "I've built PINvestigator, an agentic investigation tool. It reads logs, builds timelines, synthesizes root causes. Dylan is using it. We have an eval harness with 8 golden-set examples. I think this could be a template for the broader org."

**Dhruvil version:** "Dylan's been running PINvestigator on live incidents — it's cutting investigation time from days to minutes. Dhruvil on my team is using it for ranking debugging too. Might be worth showing at the next AI forum."

### Resource / capacity constraints
**James default:** "My team is stretched across 5 major workstreams with 17 directs and no second EM. I need help accelerating the backfill or getting temporary resourcing for the indexing migration."

**Dhruvil version:** "Quick flag — the indexing pipeline migration would cut our on-call pages by [X]% and free up [Y] engineer-weeks per quarter. We're capacity-constrained on it right now. Worth discussing timing."

### Retentive Recs / Anticipation
**James default:** "The Anticipation holdout is showing positive WAU impact in UCAN. The CTO called it out. We built UIC x CLR, Frontier Sampling, pUIC, and a feedback loop. The team delivered across the full stack."

**Dhruvil version:** "The Anticipation holdout is WAU-positive in UCAN. Matt called it out as one of the projects he's most excited about. The feedback loop we built should generalize to how Blending does explore/exploit going forward."

---

## The Three Rules

1. **Connect to their priority, not yours.** Every observation should land on something leadership is already tracking. "AI-native engineering," "platform velocity," "cross-surface expansion" — use their language.

2. **Two sentences, then stop.** The instinct to explain is the enemy. If they want more, they'll ask. Getting pulled is 10x more powerful than pushing.

3. **Tag up, don't wait.** Dhruvil tagged the CTO directly on a P6 GPU ask. He didn't wait for the right moment or the right forum. He created the moment. The worst that happens is no response — which is better than never being seen.

---

## Pre-Flight Checklist

Before any leadership-visible message, meeting contribution, or office hours visit:

- [ ] Am I initiating or reacting? (If reacting, find the initiation angle)
- [ ] Can I say this in two sentences?
- [ ] Am I connecting to a priority they already have?
- [ ] Am I making an observation or an argument?
- [ ] Am I asking for something, or surfacing something? (Default to surfacing)
- [ ] Have I tagged the right people, or am I waiting to be invited?
- [ ] Will I stop after saying it, or will I keep explaining?
- [ ] Do I have the specifics ready in case they pull (numbers, IG tags, program names)?
- [ ] Is my framing wrapped in business impact (growth, engagement, unblocking vision) — not technical need?
- [ ] Am I including others generously ("X can confirm") to position as peer-surfacer, not solo-claimant?

---

## Case Study: April 5, 2026 — Dhruvil's P6 / AI Tooling Ask

**What happened:**
Dhruvil initiated a Slack thread tagging Dylan + Matt Madrigal (CTO) with two asks — P6 GPUs for ranking (framed as "critical for user growth/engagement, unblocks the long-term vision for UPP") and AI tooling (Claude Code / Codex for MLE dev velocity). Dylan immediately escalated to Jeff with zero friction. James joined ~10 min after the thread was resolved with a "+1" validation and an explanation of why retrieval didn't have P6 requests.

### Dhruvil patterns observed (all six fire in one thread)

| Pattern | What he did |
|---------|-------------|
| **Initiates, doesn't react** | Created the thread; tagged leadership; set the agenda |
| **Tags up boldly** | Matt Madrigal (CTO) tagged directly — builds visibility at the highest level |
| **Business-impact framing** | "Unblocks long-term vision for UPP" — NOT "we need GPUs for model training" |
| **Specifics ready** | When Dylan asked for program names, he had three IG numbers immediately |
| **Generous inclusion** | "James can confirm" — positions James as peer with context, not competitor |
| **Observation-as-contribution applied to async** | Not pitching himself — surfacing a need that benefits the whole org |

### Dylan patterns observed (the mechanism by which this works)

- **Zero-friction escalation for clean asks.** A well-framed ask with business justification → immediately *"I'm pinging Jeff to approve it."* No questions, no pushback.
- **"Good timing and good reminder."** She rewards people who surface things she should be tracking. The "subtracts cognitive load" pattern in action. Dhruvil made her job easier.
- **She became Dhruvil's escalation engine.** She did the political work (pinging Jeff) so he didn't have to. This is what peak trust looks like with Dylan — she moves for you when you bring clean asks.

### James's default pattern (to replace)

- **Reactive, not initiating.** Joined after the thread was resolved. "+1" energy.
- **Explained rather than created.** *"We didn't put in P6 requests since we're not quite there on Retrieval"* — technically accurate but reads as justifying absence from the conversation.
- **Gratitude where Dhruvil got partnership.** "Thanks again Dylan!" vs. Dhruvil's "thank you!" after Dylan moved for him.

### The key insight

The "warmer reception" James senses from Jeff / Rajat toward Dhruvil isn't about personality or style. It's about **who creates the conversation vs. who joins it.** Dhruvil initiates; James reacts. The fix is structural: be the one who starts the thread, tags up, and frames the business case — not the one who validates after the ball is rolling.

### How to apply — the "Dhruvil move" template

When James spots a resource / partnership / AI-native capability that benefits multiple teams:

1. **Start the thread yourself.** Don't wait for a forum or an invitation.
2. **Tag up at the altitude that moves the ask.** Dylan minimum; CTO/VP if the ask is big enough.
3. **Frame it as unblocking a priority leadership already has** — UPP velocity, AI-native engineering push, Retentive Recs scaling — not as a technical resource need.
4. **Have two-to-three specifics ready** (IG numbers, program names, specific asks) for when someone pulls.
5. **Include peers generously** by name ("X and Y can confirm the detail"). Don't claim sole ownership.
6. **Stop after the initial ask.** Do not explain further unless pulled.
7. **When the escalation happens, thank cleanly.** Don't over-gratitude — Dhruvil said "thank you!" once, not "thanks again."

### What this means for Tuesday's 1:1 and onward

This is the missing motion in James's default. The Dylan 1:1 pre-share Slack message structure (send before the meeting, frame as "three threads executing on directions you opened, want you to see before Tuesday") is the first clean application of Dhruvil-style initiation to the manager relationship. The same motion should apply to Rajat and Jeff office hours: walk in with something James is about to do, not with a status update on what James has done.
