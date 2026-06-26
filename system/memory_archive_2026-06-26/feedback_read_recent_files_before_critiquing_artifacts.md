---
name: read-recent-files-before-critiquing-artifacts
description: "Before critiquing stakeholder artifacts (1:1 notes, draft memos, talking points), check recently-modified files in the same directory for companion docs. Compressed talking points almost always sit on top of a longer worked artifact — critiquing without that context produces uncalibrated reviews that impose risks the artifact already resolves."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 185ce05c-734e-4ed2-984d-e14cdea323f3
---

When James shares a screenshot or short doc for stakeholder communication review (Dylan 1:1 notes, draft memo, talking points), **check recently-modified files in the relevant directory before giving the review**. Specifically:

- `ls -lat work+self/people/` and `find . -newer <last-session-log> ...` are the right opening moves
- Talking-points or 1:1-notes formats are almost always compressed-from-artifact — the artifact (often 10-50KB) carries the substantive thinking and the talking points are the meeting-day distillation
- Without reading the artifact, critique tends to (a) impose risks the artifact already resolved, (b) propose framings that conflict with established artifact framing, (c) ask questions about load-bearing facts already decided

**Why:** 2026-05-25 session — James shared 1:1 notes for Dylan tomorrow asking for review. I critiqued the screenshot directly without reading `dylan_team_design_artifact_draft_v1.md` (19KB worked artifact, modified yesterday) or `recsplanations_magic_dimensions.md` in the same directory. Critique was off-base: (a) flagged Recsplanations add as territorial when artifact framed it as substrate ownership formalization per April 3 consensus, (b) proposed Engine/Accelerator framing that conflicted with artifact's AI personalization + AI-Leveraged Engineering language, (c) asked about Andrew alignment and 4/3 1-pager that were established context. James called it out: "You're way off track. Look up what happened yesterday." Recalibrated after reading the artifact, gave real critique at right altitude. Sequence wasted his time and forced re-review.

**How to apply:**

- **Before any review of a stakeholder-facing artifact** (1:1 notes, memo, deck, talking points), run `ls -lat <relevant-directory>` and check for companion docs modified in the last few days
- Especially when the artifact is brief/compressed — assume there's a longer worked doc behind it
- Read the longer artifact BEFORE writing the critique, not after being corrected
- If you write the critique without checking and later find the artifact, **own it openly** (don't smoothly pivot as if you had the context all along) and recalibrate
- For high-stakes stakeholder work (Dylan, Jeff, Rajat, Andrew, Faisal), default to reading 2-3 most-recently-modified files in `work+self/people/` and `work+self/projects/<relevant>/` before any substantive review
- Related: [[stakeholders-before-strategic-analysis]] (read stakeholders.md before multi-stakeholder analysis), [[check-team-context-first]] (read team_members.md before team-Slack analysis), [[verify-load-bearing-facts]] (verify load-bearing strategic facts before propagating)

**The deeper pattern:** Stakeholder communication artifacts are layered — magical-dimensions doc, team-design artifact, 1:1 talking points, calibration messages — each builds on prior work. Treating any single layer as standalone produces uncalibrated review. The first move is always "what's the artifact stack on this topic, and what's most recent."
