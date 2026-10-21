"""Preflight checks for safe, deterministic search/replace patches."""

from pathlib import Path


def safe_target(root: Path, relative_path: str) -> Path:
    if not relative_path or Path(relative_path).is_absolute():
        raise ValueError("Patch target must be a relative path")
    root = root.resolve()
    candidate = (root / relative_path).resolve()
    if not candidate.is_relative_to(root) or candidate == root:
        raise ValueError("Patch target escapes repository root")
    if not candidate.is_file():
        raise FileNotFoundError(candidate)
    return candidate


def preview_replace(source: str, search: str, replacement: str) -> str:
    if not search or source.count(search) != 1:
        raise ValueError("Patch search text must occur exactly once")
    if search == replacement:
        raise ValueError("Patch must change the source")
    return source.replace(search, replacement, 1)
