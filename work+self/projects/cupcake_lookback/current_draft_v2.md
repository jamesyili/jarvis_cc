# Cupcake Lookback Doc — Draft v2

This is the v2 draft from the other LLM after the Yan ownership transition addendum was applied. Source of truth for the next iteration. Apply Wes Kao edits (see `wes_kao_review.md`) and James's content fill-ins, then move to v3.

---

# Q1 / Cupcake Lookback + Look-Forward — [PLACEHOLDER: Team Name]

**Authors:** James Li, Tim Leung, Yan Li
**Audience:** Engineers, PMs, Designers, TPMs across HF CG, [PLACEHOLDER: Tim's team name], and P13N-Experiences
**Status:** Seed draft from engineering leadership — intended for cross-EPD input before the joint retro session. This is a starting point, not a finished product.
**Joint EPD retro session:** [PLACEHOLDER: date]

---

## Why this doc exists

Cupcake was the first quarter where HF CG, [Tim's team], and P13N-Experiences worked as a combined EPD group across shared surfaces. We shipped real results — strong UX, strong backend wins, executive visibility. We also moved fast enough that some of the seams between our teams became visible in ways they hadn't been before.

The three of us started talking about those seams independently and realized we were seeing the same patterns. Rather than let separate narratives form, we wanted to write one doc together — and then open it up.

This draft is the engineering leadership perspective. It's incomplete by design. PMs, designers, and TPMs experienced Q1 too, and we know there are friction patterns and wins we didn't see from where we sit. We want those perspectives in this doc before we finalize anything or commit to forward practices that affect everyone's workflow.

This is also the first of what we'd like to make a recurring practice: a quarterly joint retro across the full EPD group. The doc seeds the conversation. The live retro session is where it gets real.

---

## What we shipped together

Cupcake hit. This was a combined effort across engineering, product, design, and program management — and the results reflected it.

**UX wins**
- [PLACEHOLDER: 3-5 specific UX features shipped]

**Backend wins**
- [PLACEHOLDER: 3-5 specific backend wins]

**Executive visibility**
- [PLACEHOLDER: 1-3 moments — e.g., Matt callout, SVP-level recognition]

**Cross-EPD collaboration moments worth calling out**
- [PLACEHOLDER: 2-3 specific moments — joint debugging, fast scope calls, shared launches, PM-eng coordination that worked well]
- This was the first quarter where Explore/IB had a leadership-aligned ownership story across CG and P13N-Experiences. Yan's team stepping into surface-side ownership is a big deal — it means surfaces get the dedicated engineering investment they deserve, and CG can go deeper on the ML/retrieval core. That didn't happen by default. It happened because Yan and his team leaned in, and because all three teams were willing to work through the ambiguity of building that alignment in real time while also shipping.
- [PLACEHOLDER: anything PMs, designers, TPMs want to add here — what wins did we undercount?]

---

## What worked

Patterns worth keeping.

- **High clock speed with real scope discipline.** We cut scope when we needed to and didn't relitigate it. PMs, eng, and design were aligned on the cuts. That's a big part of why Cupcake landed on time.
- **Daily cross-team standups during the push.** [PLACEHOLDER: confirm cadence detail]. Three teams sharing a critical path need daily visibility. This worked.
- **Shared Slack channels with real signal.** [PLACEHOLDER: name channels if relevant]. Decisions were visible. People could follow along without being in every meeting.
- **EM-level alignment on ownership direction.** When cross-team ownership questions started creating confusion on the ground, the engineering leads got aligned quickly. That alignment is now the foundation for Q2.
- **PM and TPM coordination across the launch.** [PLACEHOLDER: specific callouts — are there coordination wins from the PM/TPM side we should name here?]
- [PLACEHOLDER: anything else from Tim, Yan, or XFN partners]

---

## How we're thinking about ownership going forward

This quarter was the first time our three engineering teams operated across shared surfaces as a combined group. A lot of what we got right — and a lot of what produced friction — traces back to the fact that ownership boundaries were being built at the same time we were shipping. The friction we experienced was the friction of building alignment, not the friction of misalignment.

Ownership clarity is a leadership responsibility. Where routing was ambiguous in Q1, that's on the three of us to fix — not on the ICs, PMs, or designers who were trying to get work done in the middle of a transition.

Here's the direction we're aligned on. Operational details are still being worked through and will be communicated as they're finalized.

**Surface ownership lives with the team owning the surface.** Routing, surface-specific glue, and surface-level logic follow that ownership. P13N-Experiences is moving into primary ownership of new Explore/IB surface backend development as the next phase of our partnership. CG continues to own the ML/retrieval core.

**ML/retrieval ownership lives with the team owning the model.** Cross-surface ML services, candidate generation, and retrieval-layer work remain with CG. The contract between CG and surface teams is at the retrieval API level.

**Maintenance and development are different.** CG continues to maintain what it built during Q1 — keeping the lights on, fixing bugs, supporting oncall. New development on surfaces moves with development ownership. This distinction gives ICs a clear framework for categorizing work and routing questions.

**Transitions get structured onboarding.** When ownership moves between teams, the outgoing team provides 30/60/90-day onboarding: documentation, walkthroughs, office hours. Generous and time-bounded. The goal is full self-sufficiency by day 90 — no shadow ownership lingering.

**Architectural disagreements resolve at TL+EM altitude.** When engineers on different teams disagree about the right technical approach for a shared workstream, that disagreement gets escalated to TLs and EMs. The leads make the call. ICs shouldn't have to negotiate boundary questions that are leadership's job to sort out.

*PMs and designers — does this ownership framing make sense from your side? Where does it create clarity, and where does it create new questions? We want to know before we lock it in.*

---

## Where we saw friction

This is how Q1 looked from the engineering side. We know it's one lens. PMs, designers, and TPMs saw things we didn't — and we want those observations in this doc before we treat this section as complete.

**Ownership was in motion, and that was felt on the ground.**
Our teams were building the ownership model and shipping Cupcake at the same time. ICs, PMs, and designers didn't always know who to route to — not because anyone wasn't paying attention, but because the answer was genuinely changing. Work landed on teams by adjacency rather than by design. That's a predictable cost of a transition, and one we should absorb more deliberately in Q2.

**Cross-team asks didn't have a clear default path.**
When it's not obvious who owns a request, everyone improvises — the person making the ask and the person receiving it. In Q1, that meant operational asks (holdout additions, experiment configs, data pulls) sometimes went to whoever seemed most available, regardless of team boundaries. The responses were also improvised — sometimes helpful, sometimes a redirect, sometimes friction. Both sides acted reasonably given the inputs they had. That's a system gap, not a people gap.

**Experiment disruption norms weren't explicit.**
Q1 saw experiment changes communicated with notice, but without shared norms for how much or who decides. That produced discomfort even when the decisions were sound.

**Signal and cross-surface changes rippled further than expected.**
Changes to signals, ranking inputs, or candidate generation that touch multiple surfaces need a lightweight protocol: who needs to know, how far in advance, and who has veto vs. input rights. Some changes in Q1 caught downstream teams off guard — not because anyone was careless, but because the protocol didn't exist yet.

**Interaction norms don't transfer across team boundaries.**
Within a single team, PMs and engineers build implicit norms — Slack vs. ticket, direct ping vs. EM routing, sync vs. async. Those norms don't automatically carry across team boundaries. What feels normal on one team can read differently on another. Without shared cross-team norms, both sides were guessing, and that produced avoidable friction.

*What did we miss? PMs — what friction looked like from your side? Designers — where did cross-team ambiguity hit your workflows? TPMs — what coordination gaps were most expensive? Please add inline.*

---

## Forward principles (proposed)

These are starting proposals based on the friction patterns above. Some of them touch PM, design, and TPM workflows directly — we don't want to commit to practices that affect your work without your input. Push back on what doesn't work. Tell us what's missing.

1. **Every cross-team workstream has a named owner per team — in writing, in the workstream channel.** Not "we all own it." One engineer, one PM, one designer per team where applicable — named in the channel topic or a pinned doc. When you don't know who to ask, the named owner is the default.

2. **Cross-team asks route through the named owner or EM-of-record when ownership is unclear.** Not gatekeeping — routing. The goal is that the right person gets the ask with context so it resolves faster, not slower.

3. **Two-week notice norm for experiment-disrupting changes.** If a change will end, modify, or interfere with a running experiment owned by another team, two weeks' written notice in the shared channel is the default. Exceptions happen — escalated to EM level, not handled in a DM.

4. **Signal and ranking input changes get a cross-team notification.** When a team changes what a signal means — reclassification, new input, deprecation — the originating team posts: what changed, who's affected, what downstream teams need to do (if anything).

5. **Decision logs for cross-team scope changes.** Any scope change that affects another team's plan gets a one-line entry in a shared log: date, decision, who made it, who was consulted. Async, lightweight, written down.

6. **Quarterly joint retro across EPD.** This doc is the first. Next: [PLACEHOLDER: Q2 date]. Format: async doc seeded by leads, live session open to everyone, ICs and PMs and designers contribute in both.

7. [PLACEHOLDER: open slot — proposals from Tim, Yan, PMs, designers, TPMs]

*Which of these would actually change your day-to-day? Which ones are overhead? What practice would help you that isn't on this list?*

---

## Forward practices (proposed)

How the principles become operational — if the group agrees they're the right ones.

| Practice | Cadence | Owner | Details |
|---|---|---|---|
| Cross-team workstream roster | Updated at project kickoff and mid-quarter | All three EMs + PM leads | Pinned in shared Slack channel. Names, roles, routing expectations. |
| Shared decision log | Continuous | Rotating — one entry per decision | [PLACEHOLDER: Google Doc? Slack canvas? Notion?] Format: date / decision / decider / consulted. |
| Experiment disruption notice | As needed, 2-week default | Originating team's EM | Posted in shared channel. If <2 weeks, escalate to EM-of-record on affected team. |
| Signal change notification | As needed | Originating team's TL or EM | Posted in shared channel. Format: what changed / who's affected / what's needed. |
| Ownership transition onboarding | 30/60/90 during active transitions | Outgoing team EM + TL | Runbooks, walkthroughs, office hours. Documented milestones at 30/60/90. |
| Quarterly EPD retro | Quarterly | Rotating across James, Tim, Yan + XFN leads | Async doc + live session. Next: [PLACEHOLDER: date]. |
| [PLACEHOLDER: additional practices from XFN input] | | | |

---

## Where we're leaning as leads

These are commitments we're prepared to make. We're sharing them here before the retro session so the group can see where our heads are — and push back if any of this doesn't match what you need from us.

**James:** I'll make CG's cross-team routing expectations explicit in writing at every project kickoff — who to reach out to, how asks should flow, where to escalate. I'll be the first point of contact for cross-team asks into CG so they land with context. And through the ownership transition, CG will provide structured onboarding — documentation, office hours, and direct access to the engineers who built the systems being handed over. Generous, thorough, time-bounded.

**Tim:** [PLACEHOLDER — Tim writes]

**Yan:** [PLACEHOLDER — Yan writes]

---

## How to contribute to this doc

This draft is from three engineering managers. It is not the final version. The final version has your thinking in it.

**Inline comments are open.** Agree, disagree, add context. If something doesn't match your experience of Q1, say so. If a proposed principle would make your life harder instead of easier, flag it.

**Specifically, we want to hear:**
- What friction patterns did we miss or underweight?
- Which of the forward practices would actually change your day-to-day? Which ones are theater?
- What worked in Q1 that we should protect, not just what we should fix?

**Joint EPD retro session: [PLACEHOLDER: date]**
A live conversation across all three teams — engineers, PMs, designers, TPMs. The doc is the seed. The session is where the harder stuff gets talked through.

— James, Tim, Yan
