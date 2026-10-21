"""Validate candidate diversity before showing ranked remediation options."""


def validate_ranked_options(options: list) -> None:
    if len(options) != 3:
        raise ValueError("Expected exactly three remediation options")
    if [option.rank for option in options] != [1, 2, 3]:
        raise ValueError("Remediation ranks must be 1, 2, 3")
    strategies = [option.strategy for option in options]
    if len(set(strategies)) != 3:
        raise ValueError("Remediation strategies must be distinct")
