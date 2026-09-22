from __future__ import annotations

from pathlib import Path

from .analysis import Analysis


def render(repo: Path, analysis: Analysis, days: int, files: int, additions: int, deletions: int) -> str:
    name = repo.resolve().name
    contributor_word = "contributor" if analysis.contributors == 1 else "contributors"
    return f"""LUMEN / FIELD REPORT
────────────────────────────────

Repository     {name}
Period         last {days} days

ACTIVITY
  commits       {analysis.commits}
  active days   {analysis.active_days}
  contributors  {analysis.contributors} {contributor_word}

MOTION
  files changed {files}
  additions     {additions}
  deletions     {deletions}

RECENT SIGNALS
  """ + _signals(analysis)


def _signals(analysis: Analysis) -> str:
    if not analysis.subjects:
        return "No commits found in the selected period."
    lines = [f"  • {subject}" for subject, _ in analysis.subjects.most_common(5)]
    return "\n".join(lines)
