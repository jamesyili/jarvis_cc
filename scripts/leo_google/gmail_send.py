"""Gmail send: build MIME message, send via Gmail API, return message ID."""
from __future__ import annotations

import base64
from email.message import EmailMessage
from pathlib import Path

from googleapiclient.discovery import build

from .auth import get_credentials
from .common import guess_mime

GMAIL_MAX_BYTES = 25 * 1024 * 1024  # Gmail's 25MB raw-message cap


def _build_message(
    to: str, subject: str, html_body: str, attachments: list[Path]
) -> EmailMessage:
    msg = EmailMessage()
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content("This message contains HTML. View in an HTML-capable client.")
    msg.add_alternative(html_body, subtype="html")
    for p in attachments:
        data = p.read_bytes()
        mt = guess_mime(p)
        maintype, _, subtype = mt.partition("/")
        msg.add_attachment(
            data,
            maintype=maintype or "application",
            subtype=subtype or "octet-stream",
            filename=p.name,
        )
    return msg


def send(
    to: str,
    subject: str,
    html_body: str,
    attachments: list[Path] | None = None,
) -> str:
    """Send and return the Gmail message ID. Raises ValueError if over 25MB."""
    attachments = attachments or []
    msg = _build_message(to, subject, html_body, attachments)
    raw_bytes = bytes(msg)
    size_mb = len(raw_bytes) / 1024 / 1024
    if len(raw_bytes) > GMAIL_MAX_BYTES:
        raise ValueError(
            f"Message is {size_mb:.1f} MB — over Gmail's 25 MB cap. "
            "Use /save-to-drive for large files."
        )
    encoded = base64.urlsafe_b64encode(raw_bytes).decode()
    creds = get_credentials()
    service = build("gmail", "v1", credentials=creds, cache_discovery=False)
    result = (
        service.users()
        .messages()
        .send(userId="me", body={"raw": encoded})
        .execute()
    )
    return result.get("id", "")
