"""Redact credential-shaped strings before diagnostic output."""

import re

_PATTERNS = (
    re.compile(r"(?i)(authorization:\s*bearer\s+)[^\s]+"),
    re.compile(r"(?i)((?:api_key|token|password|secret)\s*[=:]\s*)[^\s,;]+"),
)


def redact(text: str) -> str:
    for pattern in _PATTERNS:
        text = pattern.sub(r"\1[REDACTED]", text)
    return text
