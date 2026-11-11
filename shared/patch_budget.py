"""Bound patch size and change surface before allowing a review."""

from shared.limits import require_size


def validate_patch_budget(search: str, replace: str, *, max_bytes: int = 16_384,
                          max_changed_lines: int = 120) -> None:
    if isinstance(max_changed_lines, bool) or not isinstance(max_changed_lines, int) or max_changed_lines < 1:
        raise ValueError("Maximum changed lines must be positive")
    if not search:
        raise ValueError("Patch search anchor cannot be empty")
    if search == replace:
        raise ValueError("Patch must change the source")
    require_size(search, max_bytes=max_bytes, field="search")
    require_size(replace, max_bytes=max_bytes, field="replacement")
    if max(len(search.splitlines()), len(replace.splitlines())) > max_changed_lines:
        raise ValueError("Patch exceeds maximum reviewed line count")
