# lumen

> A small local tool for turning Git history into readable project field notes.

`lumen` is the first instrument in the Luna-wright collection: a deterministic command-line tool that observes a local Git repository and turns recent history into a compact, human-readable report.

It does not try to explain *why* a project changed. It records what can be observed directly from the history.

## Why lumen?

Software projects leave traces.

Commits, files, additions, deletions, dates, and authors form a kind of project weather. `lumen` makes those traces easier to read without sending repository data anywhere.

**Observation before interpretation.**

## Quick start

Requires Python 3.10+ and a local Git installation.

```bash
pip install -e .
lumen .
```

You can also point it at another local repository:

```bash
lumen /path/to/repository
```

Limit the history window:

```bash
lumen . --days 30
```

## Example

```text
LUMEN / FIELD REPORT
────────────────────────────────

Repository     first-light
Period         22 Sep — 06 Oct 2026

ACTIVITY
  commits       17
  active days    8
  contributors   1

MOTION
  files changed  31
  additions     642
  deletions     118

RECENT WORK
  documentation  42%
  experiments    31%
  infrastructure 18%
  other           9%
```

The exact report is derived from the repository history. The example above is illustrative.

## Design principles

- **Local first** — repository contents stay on the machine running `lumen`.
- **Deterministic** — the same Git history should produce explainable results.
- **Small** — no database, hosted service, account, or API key.
- **Readable** — output is intended for people, not dashboards.
- **Observable before interpretive** — facts are kept separate from later conclusions.

## Project status

`lumen` is an early experiment. The initial release focuses on a useful core: reading Git history and producing a concise field report.

Future work may explore richer repository signals, report formats, and comparisons across time. Interpretation should remain a separate layer rather than being silently mixed into the observations.

## Documentation

- [Design notes](docs/design.md)
- [Changelog](CHANGELOG.md)
- [Contributing](CONTRIBUTING.md)
- [Security](SECURITY.md)

## Luna-wright

`lumen` is Publication #002 in the Luna-wright collection.

**experiments · tools · notes · research · things worth making**

> Make something. Understand it. Document it. Share it.
