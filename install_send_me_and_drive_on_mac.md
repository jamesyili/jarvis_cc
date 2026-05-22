# Install `/send-me` + `/save-to-drive` on Mac

Setup for getting the Python-based Gmail send + Drive upload skills working on Mac after they've been built on PC. Total time: ~5 min if you have the credentials JSON ready.

## What you need before starting

- The leo repo cloned at `~/src/leo` (or wherever — adjust paths below).
- Python 3.11+ installed (`python3 --version` to check). If missing: `brew install python@3.12`.
- The file `google_credentials.json` from PC — emailed to yourself separately, or grab from PC via 1Password / AirDrop. **Do NOT copy `google_token.json` from PC.** Tokens are per-machine; Mac authenticates fresh.

## Steps

### 1. Pull latest leo

```bash
cd ~/src/leo
git pull
```

This brings down `scripts/leo_google/`, `scripts/send_me.py`, `scripts/save_to_drive.py`, `scripts/md_to_html.py`, and both SKILL.md files.

### 2. Create the leo venv + install deps

```bash
python3 -m venv ~/.venvs/leo
~/.venvs/leo/bin/pip install --upgrade pip
~/.venvs/leo/bin/pip install \
  google-api-python-client \
  google-auth-httplib2 \
  google-auth-oauthlib \
  markdown \
  jinja2
```

Verify:
```bash
~/.venvs/leo/bin/python -c "from googleapiclient.discovery import build; import markdown, jinja2; print('venv ok')"
```

### 3. Place the credentials JSON

Save the OAuth client secret JSON (from email attachment or AirDrop) to the right location:

```bash
mkdir -p ~/.config/leo
mv ~/Downloads/google_credentials.json ~/.config/leo/google_credentials.json
chmod 600 ~/.config/leo/google_credentials.json
```

(Adjust the source path if your downloaded file has a different name, e.g., `client_secret_*.json`.)

**Then delete the email + sent folder copy** to reduce exposure of the client secret.

### 4. Run the OAuth flow

```bash
cd ~/src/leo/scripts
~/.venvs/leo/bin/python -m leo_google.auth
```

This will:
- Print an authorization URL (since `run_local_server` sometimes can't auto-open browsers in WSL/SSH contexts; on Mac it usually does open the browser automatically, but fall-through to URL print is fine either way)
- Open your default browser (or prompt you to open the URL manually)
- Show the **"Google hasn't verified this app"** warning — click **Advanced** → **Go to Leo (unsafe)** → **Continue**
- Authorize → success → token saved to `~/.config/leo/google_token.json`

### 5. Smoke test

From `~/src/leo`:

```bash
~/.venvs/leo/bin/python scripts/send_me.py work+self/goals.md
```

Expect:
```
Sent. [Leo] <title> → jamesyili@gmail.com. (msg_id=...)
```

Check your inbox.

Drive test:
```bash
~/.venvs/leo/bin/python scripts/save_to_drive.py work+self/goals.md
```

Expect:
```
Uploaded. goals.md → https://docs.google.com/document/d/.../edit?usp=drivesdk
```

Open the link to verify it's a properly rendered Google Doc.

### 6. Use from Claude Code on Mac

From any Leo session on Mac:

- `/send-me` — auto-detects most recently written artifact, emails it
- `/send-me <path>` — explicit file
- `/save-to-drive` — auto-detects, uploads to "Leo Outbox" as Google Doc
- `/save-to-drive <path>` — explicit file
- Natural language works too: "email me that", "save that to Drive"

## Troubleshooting

**`Missing OAuth client secret at ~/.config/leo/google_credentials.json`**
→ Step 3 didn't land correctly. Check the file exists with `ls -la ~/.config/leo/`.

**Browser doesn't auto-open during OAuth**
→ Copy the printed `https://accounts.google.com/o/oauth2/auth?...` URL into your browser manually. The local server is still listening on `localhost:RANDOM_PORT`; the redirect will land regardless of how the URL was opened.

**"Access blocked: This app's request is invalid"**
→ The GCP app may have been pushed back to Testing. On PC, go to GCP Console → APIs & Services → OAuth consent screen → Audience → confirm "Publishing status: In production." If Testing, click "Publish app."

**Email sends but Drive upload errors with "insufficient permissions"**
→ Token was issued before the Drive scope was added. Delete `~/.config/leo/google_token.json` and re-run step 4 to re-authenticate with both scopes.

**Token expires (very rare in Production mode)**
→ Delete `~/.config/leo/google_token.json` and re-run step 4. The credentials JSON stays valid; only the token needs refresh.

## What lives where

| Path | Purpose |
|---|---|
| `~/.config/leo/google_credentials.json` | OAuth client secret (same file on PC + Mac; per-user) |
| `~/.config/leo/google_token.json` | OAuth refresh token (per-machine, NOT shared) |
| `~/.config/leo/drive_folders.json` | Cached Drive folder IDs ("Leo Outbox" → folder ID) |
| `~/.venvs/leo/` | Dedicated venv for these skills |
| `~/src/leo/scripts/leo_google/` | Python package (auth, gmail_send, drive_upload, common) |
| `~/src/leo/scripts/send_me.py` | CLI entry point for `/send-me` |
| `~/src/leo/scripts/save_to_drive.py` | CLI entry point for `/save-to-drive` |
| `~/src/leo/system/outbound_log.md` | Audit log of all sends/uploads (committed in repo) |

## GCP reference (for context, not action)

- Project: **`leo-api`** (id: `project-d54a6ea0-6ff7-4eb1-ac9`, number: `1097604819612`)
- OAuth client: **Desktop app**, "Leo CLI"
- Scopes: `gmail.send`, `drive.file` (narrow — app only sees files it created)
- Publishing status: **Production** (unverified — Google shows "unsafe" warning on first auth; click through)
