"""Prevent writes to repositories outside an explicitly configured allowlist."""


def require_allowed_repository(full_name: str, allowed: set[str]) -> str:
    normalized = full_name.strip().lower()
    approved = {name.strip().lower() for name in allowed}
    if not normalized or normalized not in approved:
        raise PermissionError("Target repository is not on the approved allowlist")
    return full_name
