---
name: Reflex 4-stage pipeline + RLHF team formation (2026-04-15)
description: Andrew's formal Reflex pipeline (Detect → Build → Simulate → Prove), RLHF team composition, and where Pinkerton's leverage grows over time
type: project
originSessionId: 9e230339-b1e1-4bbc-bb0b-2c1b357804cc
---
On 2026-04-15, Andrew Yaroshevsky formalized Reflex's 4-stage pipeline publicly in Slack with Dylan + James. This reframes what was previously "Reflex = autonomous hypothesis generation" into a multi-stage system:

**The 4 stages:**
1. **Detect** — find opportunities (current state, "good enough" per Andrew)
2. **Build** — Reflex Eng agents construct interventions (NEXT to build)
3. **Simulate** — test interventions as a real user via UI (Andrew sketching this now)
4. **Prove** — validate in production (existing experimentation system)

**Andrew's 2026-04-15 9:03am message:** "Zooming out: we need to decide when is 'good enough' for Detect to prove its value as a source of opportunities to be passed to the Build stage – and start building Reflex Eng agents for Build." Dylan endorsed ("yeah that would be epic, having build agent").

**RLHF expert team formed 2026-04-15 (Andrew initiated):**
- **Andrew's side:** Anna Kiyantseva, Matt Chun, Tim Chu
- **Dylan's side:** James, Dhruvil Deven Badani, Rahul Goutam (for diversity), Dylan herself

Dylan's inclusion of Rahul (likely IC) does NOT violate her earlier "no ICs" guidance to James — distinction is that SHE can pull in ICs for specific expertise; James doesn't proactively bring his own.

**Why:** Formalizing the pipeline raises Reflex's ceiling from "tool" to "system" — and specifically surfaces where Pinkerton becomes load-bearing. Build agents need to understand the system end-to-end to construct interventions = James's domain. Simulate stage generating UI events that cascade into engagement signals = FVL territory.

**How to apply:**
- Don't push Pinkerton integration into Build/Simulate discussions. Let it surface naturally when Andrew starts Build planning.
- For RLHF kickoff meeting (Andrew will schedule), James's contribution = failure-mode library + codepath knowledge. Walk in with clear scope on what he reviews (CG codepath accuracy, deprecated CGs, holdout status, retrieval architecture) vs what he doesn't.
- UI evaluation brainstorm (Dylan flagged 2026-04-15) — Anna/Andrew-driven. James engages only with backend hooks (e.g., "if Simulate generates UI events, here's where they cascade in FVL").
- Hold role-scope question ("how are you thinking about my role as Reflex expands into Build/Simulate stages?") for next Dylan 1:1 — not Slack.
- Pinkerton narrative stays SEPARATE from Reflex (decision reconfirmed 2026-04-15). Technical integration happens wherever it helps both work. Don't subordinate Pinkerton under Reflex in Slack framing.
