"""Safety checks for the approval-gated patch writer."""

import importlib.util
from pathlib import Path

MODULE = Path(__file__).resolve().parents[1] / "policy-and-commit" / "committer.py"


def load_committer():
    import sys
    directory = str(MODULE.parent)
    if directory not in sys.path:
        sys.path.insert(0, directory)
    spec = importlib.util.spec_from_file_location("patch_committer_safety", MODULE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_missing_approval_never_reaches_github():
    committer = load_committer()
    result = committer.commit_fix_approved(None, {}, approved=False)
    assert result["status"] == "awaiting_approval"


def test_patch_requires_unique_exact_match():
    committer = load_committer()
    assert committer.apply_patch("one one", "one", "two") is None
    assert committer.apply_patch("hello", "", "world") is None
    assert committer.apply_patch("hello world", "world", "there") == "hello there"
