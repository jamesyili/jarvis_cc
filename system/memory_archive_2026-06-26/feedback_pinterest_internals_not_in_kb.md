---
name: Pinterest internals (stakeholder names, situations) don't go in kb/
description: Files containing Pinterest-specific stakeholder context (Dylan, Rajat, Jeff, peers, situational details) belong in work+self/, not kb/, because the KB hierarchy may eventually be indexed/shared more broadly.
type: feedback
originSessionId: d6312f4c-5043-42ed-a478-1283dd16250f
---
When generating files that contain Pinterest-specific internals — stakeholder names (Dylan, Rajat, Jeff, Andrew, Kartik, Faisal, Krishna, Dhruvil, etc.), team-internal situations, calibration narratives, peer comparisons, sponsor cultivation drafts — they go in `work+self/`, never in `kb/soft/raw/{author}/` or any other KB subtree.

**Why:** James course-corrected mid-session 2026-04-25f. Initially generated `ethan-james-situations.md` in `kb/soft/raw/ethan-evans/` alongside the 8 framework files. James moved it to `work+self/` with reasoning: KB content may eventually be uploaded to NotebookLM, indexed by external tools, or shared more broadly than personal Leo, and Pinterest-internal context (even with names anonymized to "my manager" / "VP of Product") leaks situational fingerprints. Same call applied immediately to `wes-james-situations.md` from creation. Generic-author content (Ethan's frameworks, Wes's frameworks, blog posts, podcast transcripts) is fine in KB; James-specific situational application is not.

**How to apply:**
- KB hierarchy = generic, external, framework-level. Examples: `kb/soft/raw/ethan-evans/ethan-three-personal-standards.md` (Ethan's voice, generic), `kb/hard/raw/AgenticRecommendations/summaries.md` (paper summaries).
- `work+self/` = James-specific, internal, situational. Examples: `work+self/people/H1_career_convo.md`, `work+self/wes-james-situations.md`, `work+self/projects/upp/cross_org_operational_model/`.
- Test: if the file contains a Pinterest stakeholder name OR describes a Pinterest-internal situation in a way that would be recognizable to anyone familiar with Pinterest, it goes in `work+self/`.
- When in doubt, default to `work+self/` and flag it for James's confirmation.
