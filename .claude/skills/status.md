# /status

Report the state of the search and say what to do next.

**Status: designed, not yet built. This file is the specification.**

---

## Why this exists

Someone who opens this tool once a week will not remember eight commands. They will remember
one. `/status` is the single entry point that makes the rest discoverable.

It is also the most likely command to be run in a low moment, which makes `docs/tone.md`
particularly binding here.

---

## What it reads

- `my/setup-state.yaml` (is setup finished?)
- `my/profile.yaml` (when was it last added to?)
- `my/jobs/` (counts by status)
- `my/applications/` (what is in flight, and how long since each was sent)
- `my/learnings.md`

## What it prints

A short state summary, then **exactly one recommended next step**. Not a menu of eight. If more
than one thing is worth doing, name the one that matters most and mention the others in a line.

```
6 jobs waiting review
3 applications sent, none more than 2 weeks old
Profile last updated 12 days ago

Next: /review-jobs
```

## Rules

**Never editorialise about pace.** "Nothing applied since 1 August" is a fact and is fine. "You
have been inactive for 10 days" is an accusation from a tool the user opened voluntarily. There
is no version of nagging that helps.

**Give the base rate whenever a ratio appears.** "2 responses from 22 applications" without
context reads as a verdict on the user. A five to ten percent response rate is ordinary. This is
accuracy, not reassurance.

**Say when there is nothing to do.** "Nothing waiting. Everything sent is recent enough that
silence means nothing yet." is a complete and useful answer.

**No encouragement, no commiseration.** Report and stop.

## Decision order for the recommendation

1. Setup incomplete, resume it
2. An interview is coming up, `/prep-interview`
3. Jobs waiting review, `/review-jobs`
4. Shortlisted jobs with no application, `/apply`
5. Applications older than three weeks with no outcome logged, `/log-outcome`
6. Nothing waiting and no jobs found recently, `/find-jobs`
7. Nothing to do, say so
