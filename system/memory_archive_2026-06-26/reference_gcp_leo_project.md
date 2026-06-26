---
name: reference-gcp-leo-project
description: "Google Cloud project for Leo's Gmail + Drive API integration. Powers /send-me and /save-to-drive skills."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 6d10c65e-48cc-44a1-b554-02c45a633d95
---

GCP project for Leo's Google API integration (Gmail send + Drive upload via `scripts/leo_google/`):

- **Name:** `leo-api`
- **Project ID:** `project-d54a6ea0-6ff7-4eb1-ac9`
- **Project number:** `1097604819612`

Created 2026-05-21 for the `/send-me` v2 + `/save-to-drive` migration off the Anthropic-hosted Gmail/Drive MCPs (which had context-size + draft-only limitations).

**APIs enabled:** Gmail API, Google Drive API.
**Scopes requested:** `gmail.send`, `drive.file` (narrow — app only sees files it created).
**OAuth client type:** Desktop app, name "Leo CLI".
**Test user:** jamesyili@gmail.com.

**Credentials location:** `~/.config/leo/google_credentials.json` (per-machine, NOT in repo).
**Token location:** `~/.config/leo/google_token.json` (per-machine, regenerated via OAuth flow on each new machine).
