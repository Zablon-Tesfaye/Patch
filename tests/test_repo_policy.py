import pytest
from shared.repo_policy import require_allowed_repository


def test_allowlist_is_case_insensitive():
    assert require_allowed_repository("Team/Repo", {"team/repo"}) == "Team/Repo"


def test_blocks_unapproved_target():
    with pytest.raises(PermissionError):
        require_allowed_repository("other/repo", {"team/repo"})
