# EPD Demo — Reflex (Monday 2026-05-04)

**Audience:** ~3,700 — full EPD (Engineering + Product + Design) under CTO Matt Madrigal
**Format:** ~26 min demo + 8 min Q&A
**Presenters:** Andrew Yaroshevsky, Dylan Wang, James Li
**Demo title:** Reflex — self-healing discovery stack
**Origin:** Matt heard about Reflex from Andrew, Mirjam Wattenhofer, Matthias Zenger. In her 1:1, Vicky Gkiza pulled up the Asana board and showed Matt → he asked for an EPD demo.

**Strategic frame:** Single biggest VP-consolidation lever in the calibration window. CTO endorsement cascades downward. Live build-agent PR is empirical proof Reflex works (not slides about Reflex).

---

## Demo flow (locked, per Andrew + Dylan plan)

| Min | Block | Owner |
|-----|-------|-------|
| 0–2 | Agenda, who we are, goals (opener) | Andrew |
| 2–7 | Vision two-pager walkthrough → hand to Dylan at Asana board | Andrew |
| 7–11 | Asana board: 3 cards (Growth → Content/Signal → **Distribution = deepdive**) | Dylan |
| 11–16 | Build POC + system diagram | **James** |
| 16–18 | Call to action | Andrew |
| 18–26 | Q&A | All three |

Dylan only needs 4–5 min for her segment, so Andrew gets one extra min for call-to-action.

---

## James's segment (5 min — solo mock landed at 4:30)

| Beat | What | Approx time | Purpose |
|------|------|------|---------|
| 1 | Intro + opener (Variant C) | ~30s | Pull room in, personal stake, set frame |
| 2 | Asana card: DS finding → Skeptic confusion → human fix → Curator learns | ~2:30 | "This is real, integrated with how we already work" + RLHF live moment |
| 3 | Build Agent architecture (4 steps that matter) | ~1:30 | "Engineering depth underneath" |
| 4 | Handoff back to Andrew | ~10s | Smooth de-escalation into call to action |

**Energy curve:** peak at opener ("shipped its first PR to production") → relatable beat at Skeptic confusion → architectural valley/peak at safety constraints ("literally cannot write outside them") → smooth handoff.

---

## THE SCRIPT (canonical — read aloud Sunday + Monday morning)

### Beat 1 — Intro + opener

> *"Thank you, Dylan. Hi everyone — very excited to be here today! My name is James, I'm the ML Engineering Manager leading the Candidate Generation teams in Personalization."*
>
> *(brief pause — breath, let the room reset)*
>
> *"Two weeks ago, I thought Build was going to take another month to build out as part of Reflex. Today, an agent we built has shipped its first PR to production. That's what I want to show you."*

### Beat 2 — Asana card walkthrough (the story)

> *"Now, Dylan showed you what the Detect stage produces. Let me show you what happens when an idea makes its way to the Build stage."*
>
> *"First, some quick context. When you open Pinterest and see your Homefeed, every pin you see was fetched by a Candidate Generator — a CG. We have about 20 of them. Each one retrieves pins using a different signal: what you've saved, what's trending, what's semantically similar to your interests. Following Feed is a CG that surfaces pins from creators you follow."*
>
> *"Now back to Reflex. So the first thing is that the DS Agent surfaced a finding: FF has the worst engagement of any CG — 2.5 repins per thousand impressions. That's 10% the efficiency of some of our best CGs such as RecGPT. And FF serves 325 million global impressions a week."*
>
> *(scroll to comments)*
>
> *"The next agent is the Skeptic agent. It reviewed this card — and said it's not worth moving on…"*
>
> *(beat — slight smile)*
>
> *"Basically It got confused. There are two CGs with similar names — Following Feed and Followed Interest. The Skeptic applied a finding from one to the other. Basically the same mistake a new engineer would make on their first week."*
>
> *"So I went ahead and left a comment: 'Skeptic got confused. This CG is in production and doing poorly.' And then the Curator — our feedback agent — automatically picked that up, created a new check called 'CG name disambiguation,' and added it to the system. That mistake won't happen again."*
>
> *"That's the RLHF loop. Human corrects, system learns."*
>
> *(pause — look up from screen, re-engage room)*
>
> *"So now we have an approved card. Normally, this is where an engineer picks it up. Reads the context. Writes the code. That takes days. It's also not the most exciting work to be honest."*
>
> *(scroll to Build Agent comment)*
>
> *"We now have a Build Agent that did it in minutes. Three files, 23 lines of validated code. Generated end-to-end from this card."*

### Beat 3 — Build architecture diagram

> *"So what's underneath the hood? Let's quickly go there."*
>
> *(Build architecture diagram on screen)*
>
> *"This is the current Build Agent flow. We only have two so far: one for the CG Sizer Tuning PRs and one for Blending Utility Tuning PRs (thanks to Dafang). Each of them goes through a series of steps between an approved card and a production PR. Let me walk you through the ones that matter."*
>
> *"First — the agent reads the card, but opportunity cards are written for humans, not for code generation. Details are missing. So the Build Agent spawns a PM subagent — a second agent whose only job is to resolve ambiguities. 'What exact CG identifiers are we talking about? What's the budget semantics?' Agent clarifies with agent before any code is written."*
>
> *"Then it synthesizes an experiment proposal — the experiment name, the pattern, the budget math — and presents it to the human. This is important because this is where the details matter. So if anything in the plan is wrong, we try to catch it here and not in code review."*
>
> *"Once approved, it loads reference context docs, which are patterns curated from real merged PRs in the past for the same job. This is critical context for what the code typically looks like for such a task. It also reads the relevant parts of the codebase again to ensure it's up to date. Then it generates."*
>
> *"When the code changes are made, it runs a BuildValidator stage, which is not an agent but an offline test for safety. A few callouts: (1) Allowlist — the agent can only touch three files. It literally cannot write outside them. (2) Fifty-line diff cap. (3) Bazel lint. If any check fails, no PR. All of these are configurable to each type of BuildAgent. And even after all that — a human reviews every PR before merge."*

### Beat 4 — Handoff

> *"And the last step — it writes back to the Asana card so that the card has the full audit trail — from opportunity to shipped code. That's what we have today. Andrew — back to you for what's next."*

---

## Suggested refinements (optional — apply if they fit)

These are tightening/style suggestions from the line-by-line pass. Solo mock at 4:30 confirms timing isn't pressured, so apply only what feels natural in your voice.

- [ ] **CG context tightening** (saves ~15s of cushion if needed): drop the "what you've saved / what's trending / semantically similar" examples. *"Quick context: at Pinterest, every pin in your Homefeed was fetched by a Candidate Generator — a CG. We have around 20 of them, each using a different signal. Following Feed surfaces pins from creators you follow."*
- [ ] **Drop first "Basically"** ("Basically It got confused" → "It got confused"). Keep the second "Basically" — it's serving as a relatability softener.
- [ ] **PM subagent → clarifier subagent.** Avoids namespace collision with "PM Agent" in the Detect diagram. *"the Build Agent spawns a clarifier subagent…"*
- [ ] **Naming consistency:** diagram shows "Build Validator" (two words). Script says "BuildValidator." Pick one and use everywhere.
- [ ] **Sharper handoff:** *"That's Build today. Andrew — over to you for where it goes next."*

---

## Delivery / energy map

Where to peak, where to pause, where to look up from the screen:

| Moment | Delivery |
|--------|----------|
| Opener: "shipped its first PR to production" | **Energy peak.** Lean in. Strongest emphasis of segment. |
| Pause after Variant C | Let the room reset before the demo starts |
| "It got confused" (after ellipsis) | **Slight smile beat** — already in script ✓ — let room react |
| "Same mistake a new engineer would make on their first week" | Soft warmth, slight pause |
| "Created a new check called 'CG name disambiguation'" | **Concrete artifact peak** — slow down, let the name land |
| "That's the RLHF loop. Human corrects, system learns." | **Pause + look up from screen.** Re-engage room. |
| "Three files, 23 lines of validated code." | Concrete number — slight emphasis |
| "Agent clarifies with agent before any code is written" | Memorable phrase — let it ring |
| Build Validator list (1)(2)(3) | **Pace, don't rush.** Each constraint with a small pause. |
| "It literally cannot write outside them" | **Trust-earning peak.** Slow + eye contact with room. |
| "A human reviews every PR before merge" | Closing the trust argument — clear, calm |
| Handoff to Andrew | De-escalate, smile, pivot |

---

## Architecture clarifications (do NOT confuse on stage)

- **Skeptic** lives in **Detect**. Challenges *hypotheses* — semantic / idea-level: "is this opportunity worth building?"
- **Validator** lives in **Build**. Checks *code* — technical / safety-level: allowlists, diff limits, dangerous patterns.
- They are not parallel agents doing the same thing. Different kinds of verifiers for different kinds of risk.
- **Build does not have a Skeptic by design.** Hypothesis already vetted upstream; Build's job is faithful implementation of approved hypothesis.
- **PM Agent** (in Detect — runs playbooks) is different from the **PM/clarifier subagent** (inside Build — resolves ambiguities). If anyone asks: two distinct agents, similar role-name; renaming the Build one to "clarifier subagent" recommended.

---

## Q&A — anticipated questions + suggested answers

8 min Q&A with all three presenters. Andrew + Dylan field most. Questions aimed at the engineering / Build layer are yours alone. Below is a prioritized prep set.

**Defer-to-Andrew rules of thumb:**
- Vision-level "where is this going" questions → Andrew
- Strategic "why this vs other efforts" → Andrew (he owns coalition framing)
- "When does Simulate / Prove ship" → Andrew (timeline ownership)
- Build-internal mechanics, safety, validation, RLHF → **you**
- Asana board mechanics, opportunity curation → Dylan

---

### Engineering depth (most likely targeted at James)

#### Q1. *"What stops the Build Agent from interpreting the opportunity card wrong and shipping working code that does the wrong thing semantically?"* [HIGH probability — engineer or Matt]

**Suggested answer (layered defense):**
- Hypothesis already vetted by Skeptic upstream in Detect — semantic check at idea level
- Build Agent itself spawns the clarifier subagent specifically to resolve ambiguities before code generation
- **Plan-approval gate** — Build Agent presents the experiment proposal to a human BEFORE writing code. Most semantic errors get caught here.
- Validator catches technical / safety violations (allowlist, diff cap, lint)
- **Humans review every PR before merge** — final supervision layer
- Future Simulate stage adds automated offline eval / regression — closes the remaining semantic gap

**Note:** much of this is preempted in your script via the plan-approval gate. If asked, you're confirming + completing the picture, not introducing new content.

---

#### Q2. *"How is this different from Cursor / GitHub Copilot / Claude Code?"* [HIGH probability — engineer]

**Suggested answer:**
- Those are interactive coding *assistants* — engineer in the loop, typing code with AI help
- Reflex Build is *autonomous* — opportunity card in, PR out, no engineer in the typing loop
- The human-in-loop is the plan-approval gate, not the code-typing
- We do use Claude Code as the underlying agentic harness — orchestration patterns and constraints are what Reflex owns; LLM is replaceable

---

#### Q3. *"How do you scale this beyond two Build Agent types?"* [HIGH probability — Matt]

**Suggested answer:**
- Each Build Agent is a configurable framework. New types require: defining the allowlist, curating reference PRs, configuring Validator rules. That's it.
- Pattern is replicable — current 2 (CG Sizer, Blending Utility) prove the abstraction
- We're prioritizing which job types fit best: high-volume, well-patterned, low semantic ambiguity. Tuning work first, novel work later.
- The Curator's pattern library compounds — every new Build Agent benefits from past learnings

---

#### Q4. *"What's your latency? End-to-end time from card to PR?"* [MEDIUM — engineer]

**Suggested answer:**
- Agent flow: minutes (single-digit on the well-trodden paths)
- Bottleneck is human plan approval + PR review — those add hours-to-days depending on availability
- End-to-end, opportunity-to-merge is in the order of tens of minutes once humans engage
- Compare: weeks of engineer time previously

---

#### Q5. *"What about cost? How much does it cost per PR?"* [MEDIUM — Matt or finance-minded]

**Suggested answer:**
- LLM cost per PR is small relative to engineer-hour-equivalent saved
- Tracking it explicitly; happy to share exact numbers offline
- The bigger ROI lever isn't $/PR — it's cycle time and engineer attention freed for novel work

**Note:** if you don't have exact numbers tonight, the "happy to share offline" close is fine. Don't fabricate a number.

---

#### Q6. *"What about security? Could the agent leak credentials or write a vulnerability?"* [MEDIUM-HIGH — engineer or security person]

**Suggested answer:**
- Allowlist limits which files the agent can touch (3 files for current Build Agent type)
- Bazel lint catches common vulnerability patterns
- No agent has access to credential / secret files
- Final human review before merge
- Future: explicit security-scan agent in the Validator stack — this is on the roadmap, real concern, not solved

---

#### Q7. *"How does the Curator avoid memorizing one-offs vs generalizing patterns?"* [MEDIUM — sharp engineer / ML person]

**Suggested answer:**
- Curator extracts proposed patterns and surfaces them — humans validate before adoption
- Gate is human approval of the new check, not autonomous learning
- Over time, with enough validated patterns, this could move toward more autonomous extraction — but right now we want humans validating

---

### Adoption (likely from PMs / EM peers)

#### Q8. *"How does my team plug in? What's the lift?"* [HIGH probability]

**Suggested answer:**
- Detect is broadest — your team can use the PM Agent + DS Agent layer with relatively low setup
- For Build to work for your area, you need: an opportunity card schema, target codebase access, allowlist defined, reference PR pool curated. ~few engineering days of setup.
- We're actively looking for partner teams. The coordination shape is: we provide the framework + Curator-pooled patterns; you provide domain context.
- Coming from a single-team effort would be slower than joining — Curator's pattern library compounds across all participating teams.

---

#### Q9. *"Why join Reflex vs build our own?"* [MEDIUM — adjacent EM / TL]

**Suggested answer:**
- Compounding learning loop — every Build Agent benefits from every other team's Curator-validated patterns
- Shared Validator infrastructure, shared safety guardrails, shared reference PR pool
- Each team building separately repeats integration work without compound effect
- This is exactly the demo's Inclusivity principle — joining is faster than spinning

---

### Hard / political (watch register)

#### Q10. *"Does this replace engineers?"* [HIGH probability — anyone]

**Suggested answer:**
- No — it removes the most patterned, lowest-novelty work so engineers focus on harder, more novel problems
- Constraint isn't engineer headcount; it's engineer attention
- Reflex moves engineer attention from tuning to novel work — research, infra, new modeling

**Tone note:** this question often comes from anxiety. Confident + clear. Don't hedge.

---

#### Q11. *"What about [Team X]'s similar effort?"* [LOW-MEDIUM — adjacent team member]

**Suggested answer:**
- Defer to Andrew unless you know the specific overlap
- "Andrew has been driving cross-team coordination on this — Andrew, want to take that?"

**Why defer:** coalition framing is Andrew's territory. James staying tactical on engineering = the right altitude.

---

### Future stages (likely from execs)

#### Q12. *"When does Simulate ship? Prove?"* [HIGH probability — Matt]

**Suggested answer:**
- Defer to Andrew — timeline is his ownership
- If pulled in: "We're scoping Simulate now. Engineering pieces are partially in place from existing offline eval infrastructure — the work is wrapping it in the agentic shape."

---

### Curveballs (lower probability but possible)

#### Q13. *"What's the Build Agent's failure rate? What % of generated PRs need rework?"*
**Answer:** Honest number if you have it; "we're early — current sample is small but the validated PRs that have shipped have all passed human review on first or second pass." Don't fabricate a percentage.

#### Q14. *"What model are you using? Why?"*
**Answer:** Claude Code as the harness, currently Claude Opus for orchestration. Replaceable. The architecture (constraints + Validator + Curator) is what makes it work, not the model choice.

#### Q15. *"What if Matt asks: how does this connect to Pinterest's broader AI strategy?"*
**Answer:** Defer to Andrew. He owns the strategic narrative; you stay tactical.

---

## Action items / dependencies

- [ ] **Code change: Build agent writes back to Asana card** (comments + PR link). Ship before Monday demo. Verify at 9am Monday prep sync.
- [ ] **Diagram: use v4 as-is** (per "Update diagram" action from demo plan doc). No redesign.
- [ ] **Provide a few opportunities for agents** (per James's action from demo plan doc).
- [x] **Solo timed mock — 4:30 confirmed** (5/3). Cushion of 30s healthy.
- [ ] **9am Monday prep sync** with Andrew + Dylan — verify Asana card on Andrew's screen.
- [ ] **Self-grounding practice** Sunday + Monday morning.
- [ ] **Re-read Q&A list** Monday morning before demo — top 3 (Q1, Q2, Q3) are most likely.
- [ ] **Post-demo distribution kit** (60-90s clip + 1-slide + 5 bullets + 10–15 targeted DMs) — staged so Monday afternoon doesn't drift. Includes BOTH v4 and v1 diagrams as appendix.

---

## Working partnership signal (file-worthy)

Dylan offered to take the flow diagrams while James focused on the PR. James shipped the end-to-end PR Friday May 1. Dylan delivered v4 + v1 over the weekend. Clean division of labor; mutual trust compounding. Worth filing as a positive Dylan working pattern.

---

## Timing — solo mock notes

- **Solo mock duration: 4:30** (target was 5:00 — 30s cushion)
- **Why cushion is healthy, not wasted:**
  - Live-room pauses run longer than mock pauses (especially after the slight-smile beat)
  - Adrenaline at 3,700-scale adds micro-pauses
  - Validator beat will eat 5–10s if paced right
  - Tech glitches eat 5–15s without warning
  - Going SHORT > going OVER — gives Andrew full call-to-action time, no clock pressure on Q&A
- Live target: 4:45–5:00 = nailed it
