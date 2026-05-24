# Personal Blog — Topic Ideas

**Constraints:** Public, under James's own name, **not** Pinterest-affiliated. Topics centered on (a) technical and (b) engineering management, with real research depth + lived reflection — not hot takes. Pinterest-internal specifics (stakeholders, codebase, situational context) stay out; the underlying *patterns* can be written at higher altitude.

---

## Priority topics (James-named)

### P1. How to lead by doing in the current transition age of AI
**Launch post candidate.** Lived experiences from the past few months — Pinvestigator, Pinkerton, Reflex, Folio. The thesis: in this transition era, managers can't lead AI-leveraged work credibly without doing it themselves. Sleeves rolled up, tooling fluent, shipping with the team. Personal narrative + sharp argument + topical urgency. Voice-establishing for the blog identity.

### P2. Components of a high-performing applied ML team
Broader-than-recsys version of the 2-2-1-1 framing below. What roles, what proportions, what kind of people, what dynamics. Research-backed (recent 8-source synthesis) + lived reps managing the actual thing. The 2-2-1-1 recsys piece (Tech #5) becomes a tighter sibling deep-dive.

---

## Technical

### 1. Eval harnesses are the AI engineer's real moat
The "routing is commoditizing; per-customer quality calibration is not" thesis, expanded. Why golden-path datasets + regression detection on model swaps will outlast every router startup. Hands-on credibility: 12-week Pinvestigator reps, Folio production reps, Curb strategic posture work.

### 2. The dark factory metaphor for AI-leveraged recsys teams
The Detect → Build → Simulate → Prove pipeline as a way to organize an AI-leveraged engineering function. Original framing, backed by recent 8-source research synthesis (Stripe Minions, Shopify Roast, Netflix LLM-as-judge, Spotify Parallel Fusion Router, Meta Andromeda). Big claim, defensible.

### 3. Why generative video pipelines need TTS-driven timing (not video-driven)
Specific Folio production lesson: word-aligned captions, native gen-video audio stripped, beat duration from TTS not from Kling/Seedance output. Concrete, runnable, useful to anyone building short-form AI video pipelines.

### 4. Anticipation vs. reactive personalization
Higher-altitude version of the Anticipation / Retentive Recognitions thesis — foundation user representations that anticipate intent vs. systems that react to engagement events. Writeable without any Pinterest internals; deep research + lived reps.

### 5. The 2-2-1-1 team composition for AI-leveraged recsys
2 recsys-native ML + 2 agent eng + 1 substrate + 1 eval. From the recent research synthesis. Concrete, deployable hiring template — useful to other engineering managers building similar teams.

### 6. Tokenmaxxing as a failure mode
DORA 2025 findings (bugs/dev +54%, incidents/PR >3x, PR review time +441%) + Meta "Claudeonomics" + Salesforce $170/month floor. Cautionary tale on AI-leveraged engineering done poorly. Well-researched.

---

## Engineering Management

### 1. Action sponsors vs. strategic sponsors
Distinction worth a post: the sponsor who unblocks/resources/forwards vs. the sponsor who co-thinks strategy with you. They're different people, different asks, different rhythms. Original framing, lived reps.

### 2. What actually changes between Senior EM and Director
Lived inquiry post — what the framework (Ethan Evans, etc.) says vs. what's actually true in practice. Altitude, scope, peer set, what gets harder, what gets easier. Personal but generalizable.

### 3. Peer friction is usually structural, not personal
The pattern: you vent about a peer; the real fix is upstream structural ambiguity, not a tactical conversation. Strong original insight, broadly useful, anonymizable.

### 4. The expectation-gap engine
Why ratings don't drive unhappiness — gaps between expectation and reality do. From your Sept 2024 + Snap experience, generalized. Distinctive framing about manager-managee dynamics that most management writing misses.

### 5. PIPs done well: performance reset, not punishment
How to run a performance plan that's actually about giving someone a real chance, not pre-deciding the outcome. Anonymized from lived experience. Practical, generalizable.

### 6. Hiring against the 2-2-1-1 composition
Companion to technical post #5, but management-flavored: how to actually interview for substrate engineers, agent engineers, recsys ML, eval — what to test, what good looks like, what to avoid.

### 7. Why "do great work" is not enough at Sr EM altitude
The cultivation thesis: at this altitude, sponsorship + altitude-shifting + cross-org visibility are the load-bearing moves. Doing the work is table stakes. Synthesized from Ethan Evans + your own experience.

### 8. Using AI as an EM
What an engineering manager's own AI-leveraged workflow looks like. Not the IC-coding-with-Claude version — the EM version: prep, debrief, drafting up, stakeholder synthesis, decision memos, calibration. Lived reps; differentiated from the 100 "using AI as an IC" posts.

### 9. What I wish my ICs did with AI (and what frustrates me when they don't)
Opinionated. The manager's view on IC AI adoption — patterns that compound, patterns that look fast but burn the team, the eval-discipline gap, the "I shipped 10 PRs this week" failure mode. Direct, lived, useful.

### 10. How I wished my reports managed up
Broader EM topic — what good managing-up looks like from the receiving chair. Could intersect with AI (e.g., showing the manager what AI-leveraged work actually shipped, calibrating expectations on speed) or stand alone. Strong opinion territory.

### 11. As EMs, disagreements are usually structural, not personal
The broader umbrella for EM #3 (which was peer-friction-specific). Generalizes the structural-not-personal frame to *any* disagreement an EM finds themselves in — with peers, leadership, reports, cross-functional partners. Most "I'm frustrated with X" is unowned scope, ambiguous accountability, or mis-set expectations dressed up as personality conflict. EM #3 (peer friction) becomes one case study within this essay; could collapse into one post or stay as paired posts (broad umbrella + focused deep-dive).

---

## More candidates (Tech ↔ EM hybrid territory)

### H1. Managing through the speed asymmetry
When ICs ship 5x faster with AI tooling, what's a manager's actual lever? The old levers (scope, prioritization, unblocking) compress; new levers (eval quality, taste-as-bottleneck, blast-radius scoping) emerge. Lived in real time.

### H2. From "owns code" to "owns substrate" — the AI-era seniority shift
What senior ICs and EMs are now responsible for: not the code itself but the substrate that lets agents produce code reliably. Eval, observability, harness, guardrails. Sharpening of the Pinkerton-as-substrate thinking.

### H3. What I learned scoping a 12-week agentic eval project
Concrete project post-mortem (Pinvestigator). Decisions that worked, decisions that didn't, the harness shape that emerged. Specific enough to be useful to anyone scoping similar work.

### H4. The agentic blast-radius question
How much autonomy to grant an agent, and when. Lived through Claude Code reps, rate-limit failures, exit-code-0-but-failed runs. Practical, runnable framework.

### H5. Reading the recsys org chart in the LLM era
What's still recsys, what's now LLM, what's hybrid. Useful to anyone trying to make sense of how recommendation organizations are restructuring around foundation models. Research-grounded.

### H6. Eval-first development
When the eval is the spec — a development pattern that emerges naturally with agentic systems. Original framing, hands-on credibility.

---

## Picking the first 3

A working filter for which to write first:
1. **Highest-conviction take** — where do you have a real thesis you'd defend?
2. **Lowest-Pinterest-leakage risk** — which can you write fully without disclaimers?
3. **Best concept-fit for "Folio"** as a publication identity (analytical, manuscript-coded).

Updated picks given P1/P2 + hybrid additions:
- **Launch:** P1 (lead by doing in the AI transition age) — voice-establishing, topical, lived
- **Tech:** Eval harnesses are the AI engineer's real moat (Tech #1)
- **EM/Hybrid:** P2 (components of a high-performing applied ML team) — research-backed + lived authority

Strong 4th if you want a fourth: H1 (speed asymmetry) — pairs naturally with P1 and extends the same thread.

---

## Open questions

- **Blog platform:** Substack, personal Ghost, custom Next.js, Medium? (Defaults toward Substack for distribution + ease.)
- **Domain / handle:** Is this under jamesli.dev / jamesli.ai / something Folio-adjacent?
- **Cadence:** monthly, biweekly, "when ready"? Cadence floor matters more than ceiling, same logic as Folio video drops.
- **Cross-pollination:** Is Folio (the video studio) and the blog (the writing presence) one umbrella identity, or two distinct things?
