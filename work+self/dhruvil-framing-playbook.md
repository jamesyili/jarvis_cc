# How Dhruvil Would Frame It

> A reference for James: Dhruvil's communication patterns distilled from observed interactions. Use this as a pre-flight check before any leadership-visible thread, office hours, or senior meeting.

Last updated: 2026-04-12

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
