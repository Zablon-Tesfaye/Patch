import pytest
from shared.limits import require_size


def test_multibyte_payload_limit():
    with pytest.raises(ValueError):
        require_size("🔐" * 3, max_bytes=10, field="patch")


def test_small_payload_allowed():
    require_size("safe", max_bytes=10, field="patch")
