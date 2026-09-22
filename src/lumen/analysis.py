from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from datetime import datetime

from .git import Commit


@dataclass(frozen=True)
class Analysis:
    commits: int
    active_days: int
    contributors: int
    subjects: Counter[str]


def analyze(commits: list[Commit]) -> Analysis:
    days = {datetime.fromisoformat(c.date).date() for c in commits}
    authors = {c.author for c in commits}
    subjects = Counter(c.subject for c in commits)
    return Analysis(len(commits), len(days), len(authors), subjects)
