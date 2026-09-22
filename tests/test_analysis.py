from lumen.analysis import analyze
from lumen.git import Commit


def test_analyze_counts_activity():
    commits = [
        Commit("a", "2026-09-22T10:00:00+00:00", "Luna", "one"),
        Commit("b", "2026-09-22T12:00:00+00:00", "Luna", "two"),
        Commit("c", "2026-09-23T12:00:00+00:00", "Other", "three"),
    ]
    result = analyze(commits)
    assert result.commits == 3
    assert result.active_days == 2
    assert result.contributors == 2
