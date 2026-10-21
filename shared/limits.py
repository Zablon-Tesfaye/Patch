"""Resource limits to prevent oversized model prompts and patch payloads."""


def require_size(text: str, *, max_bytes: int, field: str) -> None:
    if max_bytes < 1:
        raise ValueError("Maximum size must be positive")
    if len(text.encode("utf-8")) > max_bytes:
        raise ValueError(f"{field} exceeds {max_bytes} bytes")
