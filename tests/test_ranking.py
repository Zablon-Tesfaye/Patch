from dataclasses import dataclass
import pytest

from shared.ranking import validate_ranked_options


@dataclass
class Option:
    rank: int
    strategy: str


def test_three_distinct_options():
    validate_ranked_options([Option(1, "a"), Option(2, "b"), Option(3, "c")])


def test_rejects_duplicate_strategy():
    with pytest.raises(ValueError):
        validate_ranked_options([Option(1, "a"), Option(2, "a"), Option(3, "c")])
