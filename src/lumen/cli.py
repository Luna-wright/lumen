from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .analysis import analyze
from .git import commits, numstat
from .report import render


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="lumen",
        description="Turn Git history into readable project field notes.",
    )
    parser.add_argument("path", nargs="?", default=".", help="local Git repository")
    parser.add_argument("--days", type=int, default=30, help="history window in days (default: 30)")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.days < 1:
        print("error: --days must be at least 1", file=sys.stderr)
        return 2

    repo = Path(args.path).expanduser().resolve()
    try:
        history = commits(repo, args.days)
        analysis = analyze(history)
        files, additions, deletions = numstat(repo, args.days)
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"error: could not read Git repository: {exc}", file=sys.stderr)
        return 1

    print(render(repo, analysis, args.days, files, additions, deletions))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
