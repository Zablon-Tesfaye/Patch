from shared.diff_summary import change_counts, unified_diff


def test_diff_exposes_changed_lines():
    diff = unified_diff("a = 1\n", "a = 2\n", "app.py")
    assert "-a = 1" in diff
    assert "+a = 2" in diff
    assert change_counts("a = 1\n", "a = 2\n") == {"added": 1, "removed": 1}
