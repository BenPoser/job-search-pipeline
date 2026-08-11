# Your job search, run properly

A job search assistant you run on your own computer, using Claude Code.

It keeps a structured record of your career, finds roles worth your time, writes a tailored CV
and cover letter for each one, prepares you for interviews, and learns from what actually
happens. Your data stays on your machine.

It is not built for any one industry. Whether you are a nurse, a teacher, a marketer, a project
manager or an engineer, the process is the same: know what you have done, find the right roles,
make a genuine case, prepare, and adjust.

---

## What you need

1. **Claude Code**, installed and signed in to a paid Claude plan. That is the only hard
   requirement. Install it from https://claude.com/claude-code
2. **About an hour**, once, for setup. You can stop and resume as often as you like.
3. **Your current CV**, in any format.

That is it. Job board API keys are optional and you can add them later, or never.

---

## Getting started

Open this folder in Claude Code and type:

```
/setup
```

Claude will interview you, read your CV, and build your profile. You will never be asked to edit
a file or run a command yourself. If you want to stop halfway, just stop. Running `/setup` again
picks up where you left off.

When setup finishes, type `/status` at any point and it will tell you what to do next.

---

## The commands

You do not need to memorise these. `/status` will always tell you which one you want.

| Command | What it does |
|---|---|
| `/setup` | One-time. Builds your profile, your writing style, and your search settings. |
| `/status` | Tells you the state of your search and what to do next. |
| `/find-jobs` | Finds roles. Paste a job link, or let it search the job boards for you. |
| `/review-jobs` | Walks you through what it found so you can decide what is worth applying to. |
| `/apply` | Writes a tailored CV and cover letter for one specific job. |
| `/prep-interview` | Mock interview and a one-page cheat sheet for an interview you have coming up. |
| `/log-outcome` | Records what happened after you applied. |
| `/update-profile` | Adds new experience, or goes deeper on something you already have. |

The full process, and how the pieces fit together, is described in
[docs/pipeline.md](docs/pipeline.md).

---

## Where your things live

Everything personal to you lives in one folder, `my/`. Nothing else in this repo knows anything
about you.

```
my/
  profile.yaml        your career record: roles, achievements, and where each fact came from
  voice.md            how you write, so generated documents sound like you
  search-config.yaml  what kind of roles you are looking for
  jobs/               roles that have been found, and what you decided about each
  applications/       one folder per application: CV, cover letter, interview prep
  learnings.md        what the search is telling you, in plain language
```

**By default, `my/` is excluded from version control**, so nothing personal is committed unless
you ask for it. Setup offers you the alternative: keep it in a **private** repository, which
gives you a backup and a history of how your profile grows.

Either is fine. A private repository stays private until you deliberately change that in its
settings, and you can still give specific people access without publishing it. The only thing to
keep in mind is that this folder holds your full career history, contact details and salary
expectations, so it is not one to make public later.

You can also skip git entirely and set it up whenever you feel like it.

---

## It writes nothing you did not tell it

Every claim on a generated CV traces back to something you said or a document you provided. You
can ask "where did this come from?" about any line and get a real answer.

When a draft phrases something more strongly than your evidence supports, it stops and asks you
rather than quietly softening or quietly inflating it. That check cannot be turned off, because
the worst thing this tool could do to you is put a claim on your CV that falls apart in an
interview.

---

## Making it yours

The default process is opinionated on purpose, so that it works on day one without you having to
design a workflow. It is not meant to stay that way.

Every command is a plain Markdown file in `.claude/skills/`. Every rule is a plain Markdown file
in `docs/`. You can read them, and you can ask Claude to change them. If you want your CV to look
different, your cover letters to be shorter, or an extra step in the process, say so and it will
be so.

[docs/customising.md](docs/customising.md) shows you where the useful knobs are.

---

## Updating

Improvements to the tool arrive with:

```bash
git pull
```

Nothing outside `my/` is yours, and nothing inside `my/` is ever touched by an update, so this is
always safe.

---

## A note

Job hunting is a grind, and no tool changes that. This one is meant to take away the repetitive
parts, the blank page, and the nagging sense that you are forgetting something, so that the
energy you do have goes into the applications that actually matter.
