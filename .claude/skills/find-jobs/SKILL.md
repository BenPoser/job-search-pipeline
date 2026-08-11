---
name: find-jobs
description: Add a job to the pipeline and score it against the user's profile, from a link or pasted advert text. Use when the user runs /find-jobs, pastes a job advert, or mentions a role they have seen and want to consider.
---

# /find-jobs

Take a job, score it honestly against the profile, and write it to `my/jobs/`.

Read [SCORING.md](SCORING.md) before scoring anything. The rubric is the whole point of this
command; without it scores drift generous and stop being useful for triage.

---

## Invocation

- `/find-jobs <url>` — one job from a link
- `/find-jobs` then pasted advert text — one job from text
- `/find-jobs` with nothing — ask what they have. Offer both, and mention that several at once
  is fine.

Several jobs in one go is normal and better than one at a time. Process them all, then report
once.

**Automatic searching is not built yet.** If `sources.adzuna` or `sources.reed` is true in the
config, say so plainly rather than pretending to search:

> Searching the job boards automatically isn't wired up yet, even though your keys are saved.
> Paste me a link or the text of an advert and everything after that point works normally.

---

## Before you start

Read `my/profile.yaml`, `my/search-config.yaml`, and `my/learnings.md` if it exists.

**If there is no profile**, stop and send them to `/setup`. Scoring without a profile produces
confident nonsense.

**If setup is incomplete**, say which parts are missing and that scores will be rough until it is
finished, then carry on. A partial profile still beats nothing.

List `my/jobs/` to build the seen-already set.

---

## 1. Get the advert

**From a URL:** fetch it. If the fetch is blocked, returns a login wall, or returns a page with
no advert on it, say so in one line and ask them to paste the text. Do not make a production of
it; job boards block automated fetching all the time and it is not a fault.

**From pasted text:** use it as given.

Keep the URL either way. It is how they apply later.

## 2. Extract

Fill the fields in `templates/job.yaml`. Take particular care over three:

**Salary.** Record what the advert says. If it does not state one, `salary_min` and `salary_max`
are null and `salary_note` says so. Never infer a range from the job title, and never carry over
an estimate from a job board, which are frequently wrong.

**Requirements**, split into essential and desirable as the advert splits them. This drives the
blocker check below and the targeting in `/apply`.

**Application format.** Look for whether they want a cover letter, structured answers, or just a
CV. If the advert lists the questions, capture them verbatim. Knowing this before anything is
written saves the user from producing a cover letter nobody reads.

If the advert is vague on any of these, leave the field null rather than filling it with a
plausible guess. A null is honest and visible; a guess silently becomes fact.

## 3. Deduplicate

Derive `source_id` from the URL where there is one, otherwise from organisation plus title,
slugified. If `manual-{source_id}` already exists in `my/jobs/`, do not write a second file. Say
which one it is and what its status is, in one line.

## 4. Score

**Read [SCORING.md](SCORING.md).** Produce `score`, `fit_type`, `strengths`, `gaps`, `blocker`,
and `rationale`.

Read `my/learnings.md` and let it influence the score where it genuinely applies. When it does,
say so in the rationale, so the user can see the influence and disagree with it.

Jobs below `minimum_score` in the config still get written when the user supplied them by hand.
They chose this job; silently discarding it is confusing. Say the score is below their threshold
and let them decide.

## 5. Write

One file per job at `my/jobs/manual-{source_id}.yaml`, `status: new`,
`search_cluster: manual`.

## 6. Report

For a single job, give the assessment directly rather than a summary table:

> **Senior Analyst, Acme Trust**, Manchester, hybrid, £42-48k. Closes 29 August.
>
> **7 out of 10.** Ten years of directly relevant delivery work, and they want someone who has
> run services rather than just worked in them, which is your whole record. The gap is the
> professional qualification, which they list as essential rather than desirable, so it needs
> addressing head on rather than hoping.
>
> They want structured answers, not a cover letter. Four questions, saved with the job.

For several, list them compactly, ordered by score, then give one next step.

Where a deadline is within about a week, say so plainly. It is the one fact that changes what
they should do today.

End with a single next step, normally `/review-jobs`, or `/apply` when there is one obvious
strong job.

## If the config lists boards you cannot search

Mention it once per session, not per job:

> You listed NHS Jobs and CharityJob as boards you use. Worth a look when you have a minute,
> and paste anything interesting straight in here.
