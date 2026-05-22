"""Drive upload: ensure 'Leo Outbox' folder, convert .md → Google Doc, upload."""
from __future__ import annotations

import json
from pathlib import Path

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

from .auth import CONFIG_DIR, get_credentials
from .common import guess_mime

FOLDER_CACHE = CONFIG_DIR / "drive_folders.json"
GOOGLE_DOC_MIME = "application/vnd.google-apps.document"
DRIVE_FOLDER_MIME = "application/vnd.google-apps.folder"


def _load_folder_cache() -> dict:
    if FOLDER_CACHE.exists():
        try:
            return json.loads(FOLDER_CACHE.read_text())
        except Exception:
            return {}
    return {}


def _save_folder_cache(cache: dict) -> None:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    FOLDER_CACHE.write_text(json.dumps(cache, indent=2))


def _ensure_folder(service, folder_name: str) -> str:
    cache = _load_folder_cache()
    if folder_name in cache:
        try:
            f = service.files().get(fileId=cache[folder_name], fields="id,trashed").execute()
            if not f.get("trashed", False):
                return cache[folder_name]
        except Exception:
            pass
    q = (
        f"mimeType='{DRIVE_FOLDER_MIME}' and name='{folder_name}' and trashed=false"
    )
    resp = service.files().list(q=q, fields="files(id,name)", pageSize=10).execute()
    files = resp.get("files", [])
    if files:
        folder_id = files[0]["id"]
    else:
        meta = {"name": folder_name, "mimeType": DRIVE_FOLDER_MIME}
        folder_id = service.files().create(body=meta, fields="id").execute()["id"]
    cache[folder_name] = folder_id
    _save_folder_cache(cache)
    return folder_id


def upload(
    path: Path,
    convert_md: bool = True,
    folder_name: str = "Leo Outbox",
) -> tuple[str, str]:
    """Upload to Drive. Return (file_id, web_view_link)."""
    creds = get_credentials()
    service = build("drive", "v3", credentials=creds, cache_discovery=False)
    folder_id = _ensure_folder(service, folder_name)

    is_md = path.suffix.lower() == ".md"
    if is_md and convert_md:
        body = {
            "name": path.stem,
            "mimeType": GOOGLE_DOC_MIME,
            "parents": [folder_id],
        }
        media = MediaFileUpload(str(path), mimetype="text/markdown", resumable=False)
    else:
        body = {"name": path.name, "parents": [folder_id]}
        media = MediaFileUpload(str(path), mimetype=guess_mime(path), resumable=False)

    result = (
        service.files()
        .create(body=body, media_body=media, fields="id,webViewLink")
        .execute()
    )
    return result["id"], result["webViewLink"]
