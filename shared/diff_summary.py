"""Generate human-reviewable patch statistics without executing code."""

import difflib


def unified_diff(before: str, after: str, filename: str) -> str:
    return "".join(difflib.unified_diff(
        before.splitlines(keepends=True),
        after.splitlines(keepends=True),
        fromfile=f"a/{filename}", tofile=f"b/{filename}",
    ))


def change_counts(before: str, after: str) -> dict[str, int]:
    lines = unified_diff(before, after, "file").splitlines()
    return {
        "added": sum(line.startswith("+") and not line.startswith("+++") for line in lines),
        "removed": sum(line.startswith("-") and not line.startswith("---") for line in lines),
    }
