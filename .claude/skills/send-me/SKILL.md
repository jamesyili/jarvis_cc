---
name: send-me
description: Email a file (or files) from this Leo session to James's inbox using the local Gmail integration. Defaults to the most recently written artifact and jamesyili@gmail.com. Use when James says "send me X", "email me that", or types /send-me.
user_invocable: true
---

# Send Me

You are Leo, emailing a file from this session to James. Default recipient: `jamesyili@gmail.com`. This is James-to-James — no draft review, no tone calibration. Treat it like AirDrop with subject lines.

## Invocation

James says one of:
- `/send-me` — no path; auto-detect the most recently written artifact
- `/send-me <path>` — explicit single file
- `/send-me <path1> <path2> ...` — multiple files in one email
- Natural language: "send me that", "email me the draft", "send that to my phone"

If the ask is to send to someone else (Dylan, Dhruvil, etc.), STOP. That's `/draft-email`, not this skill.

## Process

### Step 1: Resolve the file(s)

- **Explicit path(s)?** Use them. Verify each exists. If any are missing, abort with `File not found: <path>`.
- **No path?** Scan tool history for the most recent file Leo wrote or edited this session. Exclude:
  - `system/session-logs/*`
  - `system/instincts/*`
  - `system/karen_observations.md`
  - `system/notebooklm/query_log.md`
  - Anything under `.git/`
- **Multiple equally-recent candidates?** List the top 2-3 with timestamps. Ask James which one. One question, then go.
- **Still no candidate?** Ask for a path.

### Step 2: Send via the local Gmail script

Run from the leo repo root:

```bash
~/.venvs/leo/bin/python scripts/send_me.py <path> [<path> ...]
```

The script handles rendering (`.md` → HTML via `md_to_html.py`), MIME composition, attachments, and the Gmail API send. HTML is the default render mode; raw markdown is opt-in only.

### Step 3: Confirm

On success the script prints: `Sent. <subject> → jamesyili@gmail.com. (msg_id=...)`. Pass that line through verbatim. No essay.

### Step 4: First-run / auth flow

If the script prints lines about opening a browser ("Please visit this URL to authorize…"), pass them through to James verbatim. The OAuth flow runs in the script and saves the token on success.

If the script prints `Missing OAuth client secret at ~/.config/leo/google_credentials.json`, tell James he needs to complete the one-time GCP setup. Don't try to fix it from this skill.

### Body-only mode (no attachments)

If James asks for the content **in the email body** instead of attachments ("don't attach, put it in the body"), the script has no flag for this — call the sender directly:

```python
sys.path.insert(0, "/home/james/src/leo/scripts")
from md_to_html import render
from leo_google.gmail_send import send
from leo_google.common import append_outbound_log
html = render(Path("combined.md"))  # concatenate multiple .md files first if needed
send(to="jamesyili@gmail.com", subject="[Leo] ...", html_body=html, attachments=[])
append_outbound_log("gmail", subject, source_paths, extra="body-only")  # source_paths must be Path objects, NOT strings — common.py calls .is_absolute()/.relative_to() (str crashes; hit 2026-07-10)
```

For multiple files, build one combined .md (demote each file's H1 to H2) in the scratchpad, render once. First used 2026-07-09 (three peer-feedback drafts in one body-only email).

## Failure Handling

| Failure | Response |
|---------|----------|
| File not found | `File not found: <path>` — abort, don't retry |
| Auth expired | Script auto-relaunches OAuth flow — pass URL to James |
| Auth flow itself fails | Output the script's error verbatim |
| Too large for email (>25MB) | Script suggests `/save-to-drive`. Pass the suggestion through. |
| Multiple candidate files | List candidates with timestamps, ask which one (one question only) |
| Any other script error | Output the error verbatim. Don't pretend it succeeded. |
| **Cloud / web session** (no local venv or `~/.config/leo/google_credentials.json`) | The local Gmail script can't run — the cloud container doesn't have James's Google creds. Don't fail silently or retry. **First check for a Gmail MCP connector in the session** (tools like `mcp__…__send_message` via ToolSearch) — if present, send the real email through it: render the .md to HTML for the body (`pip install markdown` if needed), attach the raw .md base64, subject `[Leo] …`, to jamesyili@gmail.com, and report the returned msg_id (verified 2026-08-16, msg_id=1a00b971b4aba8b2). Only if no Gmail connector exists, **deliver the file with `SendUserFile` instead** (surfaces it straight to his phone in-session). Same fallback ladder applies to `/save-to-drive` (Drive MCP connector first). |

## Rules

- Default recipient is always `jamesyili@gmail.com`. Never send elsewhere from this skill.
- No tone calibration, no body rewriting, no signature. Treat the file as-is.
- Don't ask "are you sure?" before sending. James asked; send it.
- One confirmation line on success. No essay.
- **Ephemeral artifacts (James 2026-08-28: "no need to keep the Dylan 1:1 prep artifacts"):** when James wants a file emailed but not kept, write it inside the repo, send, then delete it in the same turn — `common.py` computes repo-relative paths for the outbound log, so a scratchpad path can crash it. Say "sent, file removed" and leave the debrief content in the routed context file (archive/program_state), never in the deleted prep.
- If James asks to send to someone else, redirect: "That's `/draft-email` territory — `/send-me` is for emailing yourself."
- If James wants the file in Drive instead, redirect: "Use `/save-to-drive` for that."

## Example invocations

- `/send-me` → emails the most recent artifact from this session
- `/send-me work/people/dhruvil-prep.md` → emails that specific file
- `/send-me draft.md notes.md` → emails both in one message
- `email me what we just wrote` → same as `/send-me` with no path
