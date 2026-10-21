"""POSIX repository path validation for remote GitHub writes."""

from pathlib import PurePosixPath


def validate_remote_path(value: str) -> str:
    if not value or "\\" in value or "\x00" in value:
        raise ValueError("Invalid repository path")
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in {".", ".."} for part in value.split("/")):
        raise ValueError("Repository path must not escape the root")
    if path.suffix != ".py" or value.startswith("."):
        raise ValueError("Only visible Python source files may be modified")
    if any(part in {".github", ".git", "vendor", "node_modules"} for part in path.parts):
        raise ValueError("Protected repository directory")
    return value
