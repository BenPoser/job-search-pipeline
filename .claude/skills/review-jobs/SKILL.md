---
name: review-jobs
description: Work through jobs that have been found, one at a time, and record whether to apply, dismiss or hold each one. Use when the user runs /review-jobs or wants to triage what a search turned up.
---

# /review-jobs

Walk the user through new jobs and record what they decided.

---

## Why this is its own command

Finding a job and deciding about it are different activities with different requirements.
Finding can happen any time, including unattended. Deciding needs the user's attention and
judgement, and works best in a batch when they have half an hour.

Splitting them also means the user never expresses a decision by moving a file. They say what
they think and you record it.

---

## Before you start

Read every file in `my/jobs/` with `status: new`, plus `my/profile.yaml` and `my/learnings.md`.

**Nothing to review** → say so and give the next step, which is usually `/find-jobs` or `/apply`
on something already shortlisted. Do not make them ask.

**More than about fifteen waiting** → offer to do the strongest ten now and leave the rest.
Grinding through forty in one sitting produces careless decisions, and a careless dismissal is
worse than no decision because it is invisible afterwards.

Open with the shape of what is coming, so they can see the end:

> Six new jobs. Two look worth your time, three are borderline, one is a clear no. About ten
> minutes. Anything closing soon gets flagged as we go.

---

## The walkthrough

**Highest score first.** People are sharpest at the start and the best jobs deserve that.

For each job, show a compact card and then the honest read:

> **3 of 6 · Senior Analyst, Acme Trust**
> Manchester, hybrid · £42-48k · closes 29 Aug (18 days)
>
> **7/10, core.** Ten years running referral services, which is the whole job. They list a
> professional qualification as essential and you do not have it, so this only works if the
> experience can be shown to substitute, and some employers will not move on that.
>
> They want four structured answers, not a cover letter.
>
> Apply, dismiss, or hold?

Rules for the card:

- **Flag a near deadline prominently.** Anything inside a week changes what they do today.
- **Say the application format**, because it changes the effort involved and people like to know
  before committing.
- **Lead with the gap, not the pitch.** They can read the score. What they need from you is the
  reason it is not a 9.

Accept: **apply**, **dismiss**, **hold**, or **more** (show the full description, then ask
again). Take conversational answers, not just the four words. "Nah, too far" is a dismissal with
a reason attached.

## Recording

- **apply** → `status: shortlisted`, `review.decision: apply`, today's date
- **dismiss** → `status: dismissed`, `review.decision: dismiss`, today's date
- **hold** → leave `status: new`, `review.decision: hold`, and note why so it is not re-presented
  cold next time

**Always capture the reason in the user's own words**, especially for dismissals. It costs one
line at the moment they have the opinion, and it is the raw material for `exclude_terms` and for
observations later. A dismissal with no reason teaches nothing.

If a reason repeats across several jobs, say so and offer to act on it:

> That's the third one you've turned down for being fully on-site. Want me to filter those out
> in future?

If yes, update `my/search-config.yaml`.

---

## Be willing to say no

This tool makes applying cheap, and cheap applying is a bad strategy. Where the score is low and
the gap is a hard requirement, say so plainly:

> This one's a 4, and the qualification is listed as essential rather than desirable. I'd skip
> it. The two 8s further down are a better use of the same evening.

Respecting their time is the feature. Volume is not a strategy, and every hopeless application
produces silence that later makes their own results look worse than they are.

The decision remains theirs. If they want to apply anyway, record it without comment and move
on. They may know something about the employer that the advert does not say.

---

## Finish

Summarise plainly: shortlisted, dismissed, held.

Then **one** next step, naming the specific job rather than the abstraction:

> Three shortlisted. Start with the Acme Trust one, it closes soonest and it is the strongest:
> `/apply`

If nothing was shortlisted, say that without softening it, and suggest `/find-jobs`. A session
that shortlists nothing is a normal outcome and often the correct one.
