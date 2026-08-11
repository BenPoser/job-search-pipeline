---
name: status
description: Report the state of the job search and recommend a single next step. Use when the user runs /status, asks what to do next, or seems unsure where they are in the process.
---

# /status

Say where the search is and what to do next.

---

## Why this exists

Someone who opens this tool once a week will not remember eight commands. They will remember
one. `/status` is what makes the rest discoverable, and it is the command most likely to be run
in a low moment. `docs/tone.md` is binding here, particularly the parts about not scolding and
about giving base rates.

---

## Read

- `my/setup-state.yaml` — is setup finished, and if not, where did it stop
- `my/profile.yaml` — how many roles and achievements, when last changed
- `my/jobs/` — counts by status, and any deadline inside two weeks
- `my/applications/` — what exists, and how long since each was sent
- `my/learnings.md`

Missing files are not errors. A user who has only run `/setup` has no jobs folder yet.

---

## Print

Short. State, then **exactly one** recommended next step.

```
6 jobs waiting review
3 applications sent, oldest 12 days ago
Profile: 5 roles, 19 achievements, last added to 12 days ago

Two deadlines inside a week:
  Senior Analyst, Acme Trust        closes 16 Aug
  Programme Lead, Northern Alliance closes 18 Aug

Next: /review-jobs
```

If more than one thing is worth doing, name the most important as the next step and mention the
others in a single line underneath. Never present a menu of eight; that is the problem this
command exists to solve.

## Choosing the next step

In order. Take the first that applies:

1. Setup incomplete → resume `/setup`
2. An interview coming up → `/prep-interview`
3. A shortlisted job with a deadline inside a week and no application → `/apply`, named
4. Jobs waiting review → `/review-jobs`
5. Shortlisted jobs with no application → `/apply`, named
6. Applications older than three weeks with no outcome recorded → `/log-outcome`
7. Nothing waiting and nothing found in the last week → `/find-jobs`
8. Nothing to do → say so

---

## Rules

**Never editorialise about pace.** "Nothing applied since 1 August" is a fact and is fine. "You
have been inactive for ten days" is an accusation from a tool they opened voluntarily. There is
no version of nagging that helps here.

**Give the base rate whenever a ratio appears.** This is accuracy, not reassurance. A response
rate of five to ten percent is ordinary in a competitive market, and silence usually carries no
information about the candidate at all.

> 2 responses from 22 applications. That is within the normal range; most applications go
> unanswered regardless of the candidate.

**Say when there is nothing to do.** That is a complete and useful answer:

> Nothing waiting. Everything you have sent is recent enough that silence means nothing yet.
> Worth checking back in a week.

**Do not manufacture activity.** If the honest recommendation is to wait, recommend waiting.

**No encouragement and no commiseration.** Report, recommend, stop.
