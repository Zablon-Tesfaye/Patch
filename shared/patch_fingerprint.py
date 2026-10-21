"""Stable digest binds review decisions to exact patch bytes."""

import hashlib
import json


def patch_digest(file: str, search: str, replace: str) -> str:
    payload = json.dumps(
        {"file": file, "search": search, "replace": replace},
        sort_keys=True, separators=(",", ":"),
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()
