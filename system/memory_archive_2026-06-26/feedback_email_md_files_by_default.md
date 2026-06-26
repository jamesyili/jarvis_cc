---
name: email-md-files-by-default
description: "When Leo creates a new substantive .md artifact, email it to James automatically via /send-me — don't wait to be asked."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 09d278d5-9bb1-4891-abd5-d381591324b9
---

When I create a new substantive `.md` file (using the Write tool, not Edit), email it to James automatically via `~/.venvs/leo/bin/python scripts/send_me.py <path>`. No prompt needed.

**Why:** James works across phone + desktop and wants substantive artifacts in his inbox by default so he can read them on his phone without asking. The /send-me skill exists exactly for this; the friction of "do you want me to email it" is unnecessary once the artifact is worth persisting in the first place.

**How to apply:**

- **Yes — email automatically:**
  - New artifacts under `work+self/` (memos, prep docs, eval docs, drafts, narratives, stakeholder material)
  - Multi-section deliverables created in any user-facing directory (`blog/`, `learning/`)
  - Anything the user would plausibly want to read on their phone
- **No — don't email:**
  - Memory files (`/home/james/.claude/projects/-home-james-src-leo/memory/*.md`) — internal infrastructure
  - Session log entries (`system/session-logs/*.md`) — go to git, not phone
  - KB raw articles (`kb/{hard,soft}/raw/*.md`) — content-volume noise, not artifacts
  - Index files, registry files, file_index updates — infrastructure
  - Small fixups / typo-fix-only edits (the Edit tool doesn't trigger this rule; only Write does)
- **Companion behavior:** If the user asked me to save to Drive too, run both. If they only asked for one of email/Drive, follow that — but for default-no-prompt artifacts, email is the default channel.
- See [[send-me-html-default]] for the rendering convention (HTML body + attachment, raw markdown opt-in only).
