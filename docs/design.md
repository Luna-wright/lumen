# Design notes

## The first boundary: observation vs interpretation

`lumen` begins with a narrow promise: report signals that can be derived directly from local Git history.

It intentionally does not claim to know why a project changed, whether a change was good, or what a maintainer should do next.

That boundary matters because a useful instrument should make its observations inspectable.

## v0.1 signals

The first release reports:

- commit count
- active days
- contributor count
- changed-file count
- additions
- deletions
- recent commit subjects

These are deliberately simple. More sophisticated signals should earn their place through a concrete use case.

## Non-goals for v0.1

- hosted dashboards
- telemetry
- remote repository access
- AI-generated explanations
- project health scores
- predictive claims

The project can evolve, but the smallest useful instrument comes first.
