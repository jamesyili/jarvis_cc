---
name: Verify Explore agent web-research stats independently
description: Explore agents (and general-purpose agents doing web research) can fabricate plausible-sounding repo stats — star counts, version numbers, last-commit dates, maintenance signals. Verify via direct WebFetch before trusting.
type: feedback
---

When an Explore agent (or general-purpose agent) reports specific quantitative facts from web research — GitHub star counts, package versions, "last commit X days ago", open issue counts, release maturity signals — treat them as unverified claims and check directly.

**Why:** 2026-04-08 session, an Explore agent tasked with analyzing `safishamsi/graphify` reported: "10,932 stars, 1,134 forks, 32 open issues, v0.1.x branch, last commit April 8 2026." These were fabricated — when I subsequently verified via direct WebFetch and pip install, the actual version was `graphifyy==0.3.15` and the repo metadata I could confirm did not match. The agent's qualitative analysis (architecture, file structure, CLI surface) was largely accurate; only the numeric repo metadata was wrong.

**How to apply:** When spawning an Explore agent for open-source research, treat its qualitative findings (what the tool does, how it's structured, public API) as useful and its quantitative stats (stars, version numbers, dates, issue counts) as unverified. If those numbers matter for a decision, verify via direct `WebFetch` on the repo's raw URL or via `pip show <package>` / `gh api repos/<owner>/<repo>`. Don't lean on Explore-reported "maturity signals" for go/no-go calls.
