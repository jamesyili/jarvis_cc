---
name: Verify load-bearing strategic facts before propagating across multi-turn analysis
description: When a fact (manager state, level, timing, role-arc) is about to anchor multi-turn strategic analysis, surface it explicitly to James for verification BEFORE building on it. Stale context-file facts are a regular failure mode.
type: feedback
originSessionId: 2f25dc6b-2e0b-4128-9da1-5cf6ed14f35f
---
When a strategic fact is about to become load-bearing for multi-turn analysis (e.g., "Dylan transitioning 6/12", "James is M16", "July calibration is career-relevant"), surface it explicitly to James for verification BEFORE using as the basis for recommendation chains.

**Why:** In 5/9 evening coaching session, three separate facts sourced from stale context files propagated across multiple turns of analysis before James caught them:
- "Dylan transitioning to a new role 6/12" (wrong — she's staying; just OOO 3wk PTO + 1wk India). Sourced from `ethan-james-situations.md:4241`.
- "James is M16" (wrong — M17 Sr Mgr). Sourced from same line + multiple other files.
- "July 2026 calibration" + "EOY 2026 promo timing" framed as career-meaningful (wrong — realistic Director target is 2027 H1 or EOY 2027).

Each error distorted downstream recommendations (transition-handoff probe, "5 weeks before her transition" pressure, M16-trap framing, July-calibration-as-deadline urgency). Carrying multiple wrong load-bearing facts across several turns is **costly to retract** — entire chains of reasoning have to be rebuilt, and the rebuilt analysis itself loses momentum.

**How to apply:**
- Before applying a strategic fact as the basis for multi-turn analysis (especially timing, level, role-state, manager-arc), lead with: *"Quick verification before I build on this — your read is X, right?"*
- Higher prior on staleness for facts sourced from `.md` files not touched recently; auto-loaded SessionStart context can also be stale by definition.
- Watch especially for facts that appear in BOTH context files AND memory — staleness can propagate between them. The presence of a fact in memory does NOT mean it's verified-current.
- The fact-verification beat should come BEFORE the analytical work, not after — if I'm 3 turns deep in a recommendation built on a stale fact, the cost to retract is much higher than the cost to verify upfront.
- Counter-pattern to avoid: hedging every fact unnecessarily. Verify the LOAD-BEARING ones, not every reference.
