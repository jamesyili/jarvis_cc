---
name: Subfolder for multi-file session artifacts
description: When a session produces 3+ related files on one topic, propose a subfolder proactively instead of flat-dumping
type: feedback
originSessionId: 044981b7-20dd-4393-bf32-f368bb56ec34
---
When a single session is going to produce 3 or more files on a single topic, propose a subfolder proactively at the first multi-file moment. Don't flat-dump into the parent directory and let James reorganize.

**Why:** In the 2026-04-18 Charlie CPP session, I saved four Charlie-PIP-related files (`charlie_cpp_draft.md`, `charlie_pip_project1_onepager.md`, `charlie_pip_project2_onepager.md`, `charlie_pip_project2_oncall_source.md`) directly into `work+self/people/`. James manually moved them into `work+self/people/charlie_pip/` subfolder afterward. That reorganization was cleanup work I could have saved him.

**How to apply:**
- When the second file on a topic is about to be created, propose the subfolder: "Saving to `work+self/people/charlie_pip/charlie_pip_project1_onepager.md` — I'll move the existing `charlie_cpp_draft.md` into the same subfolder for grouping. OK?"
- Use a topic-prefix naming convention within the subfolder so files remain searchable by prefix.
- Skip for topics where existing files already live at the parent level under an established convention (don't reorganize just because a new sibling landed).
