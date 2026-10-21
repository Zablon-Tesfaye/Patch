import pytest
from shared.paths import validate_remote_path


def test_accepts_normal_python_path():
    assert validate_remote_path("app/main.py") == "app/main.py"


@pytest.mark.parametrize("path", ["../secret.py", "/etc/passwd", ".env", "vendor/a.py", "a\\b.py"])
def test_rejects_unsafe_path(path):
    with pytest.raises(ValueError):
        validate_remote_path(path)
