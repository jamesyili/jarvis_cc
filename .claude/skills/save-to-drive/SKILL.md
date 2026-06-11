---
name: save-to-drive
description: Upload a file (or files) from this Leo session to James's Google Drive ("Leo Outbox" folder). .md files convert to Google Docs by default. Use when James says "save that to Drive", "put this in Drive", or types /save-to-drive.
user_invocable: true
---

# Save to Drive

You are Leo, uploading a file from this session to James's Drive. Destination: a "Leo Outbox" folder in My Drive (auto-created on first use). This is James-to-James — no tone calibration, no review.

## Invocation

James says one of:
- `/save-to-drive` — no path; auto-detect the most recently written artifact
- `/save-to-drive <path>` — explicit single file
- `/save-to-drive <path1> <path2> ...` — multiple files
- Natural language: "save that to Drive", "put this in Drive", "upload that"

If James wants to email the file instead, redirect: "Use `/send-me` for email."

## Process

### Step 1: Resolve the file(s)

Same auto-detect rules as `/send-me`:
- **Explicit path(s)?** Use them. Verify each exists. If any are missing, abort with `File not found: <path>`.
- **No path?** Scan tool history for the most recent file Leo wrote or edited this session. Exclude:
  - `system/session-logs/*`
  - `system/instincts/*`
  - `system/karen_observations.md`
  - `notebooklm/query_log.md`
  - Anything under `.git/`
- **Multiple equally-recent candidates?** List top 2-3 with timestamps. Ask which one. One question, then go.
- **Still no candidate?** Ask for a path.

### Step 2: Upload via the local Drive script

Run from the leo repo root:

```bash
~/.venvs/leo/bin/python scripts/save_to_drive.py <path> [<path> ...]
```

Default behavior:
- `.md` files convert to Google Docs (so they're editable on phone).
- Other files upload as-is.
- All files land in "Leo Outbox" at My Drive root.

Override flags (use only when James explicitly asks):
- `--raw` — upload `.md` as raw markdown (no Doc conversion).
- `--folder <name>` — upload to a different folder name.

### Step 3: Confirm

On success the script prints one line per file: `Uploaded. <name> → <link>`. Pass through verbatim. No essay.

### Step 4: First-run / auth flow

Same as `/send-me`. The OAuth token is shared between Gmail and Drive scopes, so if James has already used `/send-me` on this machine, no re-auth is needed.

If the script prints `Missing OAuth client secret at ~/.config/leo/google_credentials.json`, James needs to complete the one-time GCP setup.

## Failure Handling

| Failure | Response |
|---------|----------|
| File not found | `File not found: <path>` — abort |
| Auth expired | Script auto-relaunches OAuth flow — pass URL to James |
| Upload error | Output the script's error verbatim |
| Multiple candidate files | List candidates, ask which one (one question only) |

## Rules

- Default folder is always "Leo Outbox". Don't propose subfolders unless James asks.
- Don't ask "are you sure?" before uploading. James asked; upload it.
- One confirmation line per file. No essay.
- If James asks to share the link with someone else, that's a separate ask — this skill just uploads.

## Example invocations

- `/save-to-drive` → uploads the most recent artifact
- `/save-to-drive work/projects/anticipation-foundations.md` → that specific file as a Google Doc
- `/save-to-drive draft.md notes.md` → both, each converted
- `save that to Drive` → same as `/save-to-drive` with no path
- `put this in Drive but keep it as markdown` → `/save-to-drive --raw <path>`
