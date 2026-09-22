from pathlib import Path

from lumen.analysis import analyze
from lumen.git import Commit
from lumen.report import render


def test_render_contains_field_report():
    analysis = analyze([Commit("a", "2026-09-22T10:00:00+00:00", "Luna", "build: test")])
    output = render(Path("demo"), analysis, 30, 2, 10, 3)
    assert "LUMEN / FIELD REPORT" in output
    assert "demo" in output
    assert "commits       1" in output
    assert "files changed 2" in output
