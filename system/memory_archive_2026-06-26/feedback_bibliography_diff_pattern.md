---
name: Bibliography diff pattern for paper reviews
description: When reviewing an academic paper's citations, run a structured diff agent over the existing bibliography against deep-search recommendations — surfaces misattributions and self-inflicted citation gaps faster than any single review pass
type: feedback
originSessionId: 8a82b336-94a0-40ca-b514-4a07a67cc9b8
---
When reviewing an academic paper for citation completeness, structured-diff is more reliable than asking a single reviewer agent to assess "are the citations complete." The pattern that worked: separate agents for (1) deep-search of recent literature, (2) bibliography diff, (3) reference cross-verification.

**How to apply:**

When the task is "review this paper for RecSys / KDD / NeurIPS / etc.":

1. Capture the paper's bibliography verbatim into the working file.
2. Spawn a deep-search agent for the relevant literature window.
3. Spawn a separate **diff agent** with explicit instructions: read the existing bibliography + deep-search output, produce a 3-section diff (confirmed additions / already-cited / KEEP-RECONSIDER-DROP verdict on each existing ref).
4. The diff agent will catch errors no single reviewer will: misattributions (wrong lead author, wrong venue), duplicate-looking entries with overlapping author lists, vestigial padding refs, references analyzed in the team's own internal docs but not cited.

**Why:**

In session 2026-04-25b, the bibliography_diff agent caught the highest-impact single error in an hour of agent work: reference [23] was attributed to "Kai Zhang et al. 2024 SIGIR" but the actual citation is "Kai Zheng et al. WWW 2024" (arXiv 2405.04844). Wrong lead author + wrong venue. An area chair who notices this reads it as sloppiness signal. The error was invisible to the editor agent (which read the bibliography but didn't cross-check authoritative sources) and to the deep-search agent (which surfaced the correct citation but didn't compare against the existing list). Only the explicit-diff agent caught it.

The diff agent also found self-inflicted citation gaps: Gu et al. RCS 2022 was analyzed at length in the team's own internal background doc but not cited in the paper — direct attack-surface material. And it produced a KEEP/RECONSIDER/DROP verdict on each existing ref, flagging vestigial padding (refs from before 2015 with no load-bearing in-text citation).

The 90-second cost of a structured diff agent is worth more than a longer single-reviewer pass.
