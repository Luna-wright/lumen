from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Commit:
    sha: str
    date: str
    author: str
    subject: str


def _run_git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=repo,
        check=True,
        text=True,
        capture_output=True,
    )
    return result.stdout


def repository_name(repo: Path) -> str:
    output = _run_git(repo, "rev-parse", "--show-toplevel").strip()
    return Path(output).name


def commits(repo: Path, days: int = 30) -> list[Commit]:
    fmt = "%H%x1f%aI%x1f%an%x1f%s%x1e"
    output = _run_git(repo, "log", f"--since={days} days ago", f"--format={fmt}")
    result: list[Commit] = []
    for record in output.strip("\x1e\n").split("\x1e"):
        if not record.strip():
            continue
        sha, date, author, subject = record.strip().split("\x1f", 3)
        result.append(Commit(sha, date, author, subject))
    return result


def numstat(repo: Path, days: int = 30) -> tuple[int, int, int]:
    output = _run_git(repo, "log", f"--since={days} days ago", "--numstat", "--format=")
    additions = deletions = files = 0
    for line in output.splitlines():
        parts = line.split("\t")
        if len(parts) != 3 or not parts[0].isdigit() or not parts[1].isdigit():
            continue
        additions += int(parts[0])
        deletions += int(parts[1])
        files += 1
    return files, additions, deletions
