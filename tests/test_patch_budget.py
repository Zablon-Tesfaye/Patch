import pytest
from shared.patch_budget import validate_patch_budget


def test_accepts_small_patch():
    validate_patch_budget("x = 1", "x = 2")


def test_rejects_oversized_patch():
    with pytest.raises(ValueError):
        validate_patch_budget("x", "a" * 100, max_bytes=20)


def test_rejects_large_line_change():
    with pytest.raises(ValueError):
        validate_patch_budget("a", "b\n" * 10, max_changed_lines=5)
