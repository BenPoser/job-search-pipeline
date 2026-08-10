# 2. Sharp split between shipped machinery and user data

Date: 2026-08-10

## Status

Accepted

## Context

Users obtain this tool from GitHub, which means git is already configured and pointing at a
remote before they have entered a single fact about themselves. Within an hour of running
`/setup` the working tree contains their full career history, home location, contact details,
salary expectations, and quite possibly their reasons for leaving a current employer.

Separately, the tool needs to be updatable. When a command improves, existing users should be
able to take the improvement without losing their data and without resolving merge conflicts on
files they have deliberately hand-edited. The intended audience includes people who have never
used git and will not debug a conflict.

## Decision

Every file in the repository is either shipped machinery or user data, with no overlap, split by
directory. All user data lives under `my/`. Nothing outside `my/` contains anything personal;
nothing inside `my/` is ever modified by an update.

`my/` is listed in `.gitignore` by default.

Updates are a plain `git pull`, which is conflict-free by construction.

## Consequences

**The safe default is automatic.** A user who never thinks about privacy cannot publish their
career history by accident, because the files are not tracked.

**The default costs them a backup.** An ignored `my/` folder exists only on one laptop. Losing
it means losing an hour of setup interview plus months of accumulated achievements and
application history, and the users least likely to have a backup habit are exactly the ones this
tool is aimed at.

This is resolved by making it an explicit choice rather than a README footnote: `/setup` asks
whether to commit `my/` to a private repository, states the trade-off in a sentence, and acts on
the answer. A user who chooses backup gets version history over their own career record, which
is genuinely valuable. A user who does not choose stays safe.

Relying on the README for this would not work, because the people at risk are the ones who will
not read that section.

**A residual risk remains: a user who enables committing and later makes the repository public.**
Mitigated by the README, by `/setup` stating the requirement plainly at the moment of choice,
and by commands checking remote visibility where it is cheap to do so. It cannot be eliminated,
because a user can always run git themselves.

**Customisation now has two flavours.** Editing files under `my/` survives updates. Editing
shipped files under `.claude/skills/` or `docs/` is encouraged, but may conflict on a later
pull. This is an acceptable trade for keeping the commands readable and editable in place,
rather than hiding them behind a configuration layer.
