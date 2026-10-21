from shared.patch_fingerprint import patch_digest


def test_digest_is_stable_and_change_sensitive():
    original = patch_digest("a.py", "x", "y")
    assert original == patch_digest("a.py", "x", "y")
    assert original != patch_digest("a.py", "x", "z")
