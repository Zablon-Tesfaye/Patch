"""Tamper-evident audit chain for local approval decisions."""

import hashlib
import json


def append_event(previous_hash: str, event: dict) -> dict:
    canonical = json.dumps(event, sort_keys=True, separators=(",", ":"), default=str)
    digest = hashlib.sha256((previous_hash + canonical).encode()).hexdigest()
    return {"previous_hash": previous_hash, "event": event, "hash": digest}


def verify_chain(records: list[dict]) -> bool:
    previous = ""
    for record in records:
        expected = append_event(previous, record["event"])
        if record.get("previous_hash") != previous or record.get("hash") != expected["hash"]:
            return False
        previous = record["hash"]
    return True
