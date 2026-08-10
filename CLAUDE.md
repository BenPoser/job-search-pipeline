# job-search-pipeline — instructions

## What this is

A job search assistant that people run locally with Claude Code. Not industry-specific: users
may be nurses, teachers, marketers, project managers or engineers.

Two kinds of person open this repo, and you need to tell which you are talking to:

- **A user**, running `/setup` or `/apply` to get a job. They are not developers. Never ask them
  to edit a file, run a command, or understand the repo layout. Do everything for them.
- **A maintainer**, changing how the tool works.

If it is ambiguous, assume user.

## Read these before working on anything

- `CONTEXT.md` — the vocabulary. Use these terms exactly. In particular: the eight things a user
  invokes are **commands**, never "skills", because "skills" means CV competencies here and the
  collision is confusing. An achievement's field is `capabilities`, never `tech` or `skills`.
- `docs/pipeline.md` — how the whole process fits together
- `docs/quality-rules.md` — applies to every generated document
- `docs/tone.md` — how commands talk to users
- `docs/adr/` — why things are the way they are. Read the relevant one before reversing a
  decision.

## Structure

Everything is either shipped machinery or user data, split by directory, with no overlap
(`docs/adr/0002`).

```
.claude/skills/<command>/SKILL.md   the eight commands, plus reference files alongside
docs/                               shipped documentation and decisions
templates/                          shapes of user files, never read at runtime
my/                                 100% user data, gitignored, never touched by an update
```

Each command is a directory containing `SKILL.md` with `name` and `description` frontmatter.
That layout is what makes `/setup` work as a typed command; a flat `setup.md` does not register
and only works if someone tells Claude to go and read it. Long commands keep their detail in
sibling reference files that `SKILL.md` points to, so the main file stays readable and the
detail loads only when needed.

**Never put anything personal outside `my/`. Never put machinery inside it.** This is what makes
`git pull` safe for a user with a live profile.

## Rules that are not negotiable

**The claim check in `/apply` cannot be skipped or weakened.** Every line traces to provenance;
anything phrased more strongly than the evidence gets put to the user. The worst thing this tool
can do to someone is put a confident claim on their CV that collapses in an interview.

**Never invent detail about an employer.** Placeholder over plausible fabrication.

**Never claim the tool learns statistically.** It notices patterns and shows them. At forty
applications dominated by silence, anything more is a lie shipped to someone under pressure
(`docs/adr/0004`).

**No performed empathy in any command.** See `docs/tone.md`.

## Writing style for this repo

Plain English throughout, including in the command files, because users read them. Avoid em
dashes. Avoid jargon in anything user-facing: "pipeline" is fine as a repo name and wrong in a
sentence aimed at a user.

## Current state

`/setup` is written and untested. Everything else is a specification only, marked as such at the
top of its `SKILL.md`. See `ROADMAP.md`.

Nothing here has been run against a real person yet, so treat the setup design as a hypothesis
about how someone talks about their own career, not as settled.
