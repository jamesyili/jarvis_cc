---
name: feedback-inbox-no-read
description: "Never read file contents inside /home/james/src/leo/inbox/ — it's a Google Drive sync folder, not session context"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: b0fbefa4-8ba4-418f-b525-55fb0373888f
---

Never read the contents of any file inside `/home/james/src/leo/inbox/` (the symlink to `/mnt/g/My Drive/Leo Inbox`). Listing the directory (`ls`) is fine; reading file bodies is not.

**Why:** `inbox/` is a Google Drive dropbox James uses to move files onto the PC from elsewhere (phone, other machines, web). Contents are arbitrary and frequently large/binary/irrelevant. Auto-reading would pollute the context window with material James never intended for the session. See [[project_agents_md_split]] for the broader principle that not all repo contents are session context.

**How to apply:**
- Do not use Read, cat, head, tail, grep, or any content-extracting tool on paths under `inbox/`.
- Do not pass `inbox/` paths to subagents (Explore, Search, etc.) for content analysis.
- If James explicitly asks to read a specific file from `inbox/` (e.g. "read inbox/foo.pdf"), that's an explicit override — proceed. The rule blocks proactive/incidental reads, not requested ones.
- Listing the directory (`ls inbox/`) is allowed and useful when James asks what's in there.
- Same rule applies to anything James adds under `inbox/` in the future, including subfolders.
