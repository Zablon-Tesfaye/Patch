import pytest
from shared.patch_validation import preview_replace, safe_target


def test_preview_replaces_unique_span():
    assert preview_replace("a = 1\nb = 2", "a = 1", "a = 3") == "a = 3\nb = 2"


def test_ambiguous_patch_is_rejected():
    with pytest.raises(ValueError):
        preview_replace("bad\nbad", "bad", "good")


def test_path_traversal_is_rejected(tmp_path):
    with pytest.raises(ValueError):
        safe_target(tmp_path, "../outside.py")


def test_symlink_escape_is_rejected(tmp_path):
    outside = tmp_path.parent / "external-test-target"
    outside.write_text("secret")
    (tmp_path / "link.py").symlink_to(outside)
    with pytest.raises(ValueError):
        safe_target(tmp_path, "link.py")
    outside.unlink()
