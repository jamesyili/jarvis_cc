"""OAuth flow + token management for Leo's Gmail/Drive integration.

Token + credentials live OUTSIDE the repo at ~/.config/leo/.
First run launches a browser; subsequent runs use the saved refresh token.
"""
from __future__ import annotations

import os
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

CONFIG_DIR = Path.home() / ".config" / "leo"
CREDENTIALS_PATH = CONFIG_DIR / "google_credentials.json"
TOKEN_PATH = CONFIG_DIR / "google_token.json"

# Request both scopes up front so one token covers Gmail send + Drive upload.
SCOPES = [
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/drive.file",
]


def _save_token(creds: Credentials) -> None:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    TOKEN_PATH.write_text(creds.to_json())
    os.chmod(TOKEN_PATH, 0o600)


def _run_oauth_flow() -> Credentials:
    if not CREDENTIALS_PATH.exists():
        raise FileNotFoundError(
            f"Missing OAuth client secret at {CREDENTIALS_PATH}. "
            "Complete the GCP setup first (download OAuth desktop client JSON, "
            "save to ~/.config/leo/google_credentials.json, chmod 600)."
        )
    flow = InstalledAppFlow.from_client_secrets_file(str(CREDENTIALS_PATH), SCOPES)
    creds = flow.run_local_server(port=0, prompt="consent")
    _save_token(creds)
    return creds


def get_credentials() -> Credentials:
    """Return valid Credentials. Refresh or re-auth as needed."""
    creds: Credentials | None = None
    if TOKEN_PATH.exists():
        try:
            creds = Credentials.from_authorized_user_file(str(TOKEN_PATH), SCOPES)
        except Exception:
            creds = None
    if creds and creds.valid:
        return creds
    if creds and creds.expired and creds.refresh_token:
        try:
            creds.refresh(Request())
            _save_token(creds)
            return creds
        except Exception:
            pass
    return _run_oauth_flow()


if __name__ == "__main__":
    c = get_credentials()
    print(f"Auth OK. Token at {TOKEN_PATH}. Scopes: {c.scopes}")
