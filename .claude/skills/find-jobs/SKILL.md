---
name: find-jobs
description: Find jobs and score them against the user's profile, either by searching the configured job boards or from a link or advert the user pastes in. Use when the user runs /find-jobs, pastes a job advert, or asks what is out there.
---

# /find-jobs

Get jobs into the pipeline and score them honestly.

Read [SCORING.md](SCORING.md) before scoring anything. Read [SOURCES.md](SOURCES.md) before
running a search.

---

## Two ways in, equally supported

- **Manual** — a link or pasted advert text. Works with any job board anywhere, including the
  ones with no API. Never requires a key.
- **Search** — queries the boards configured in `my/search-config.yaml`.

## Invocation

- `/find-jobs <url>` or pasted text → the manual path
- `/find-jobs` with nothing → search, if any source is configured. If none is, say so in one
  line and ask for a link or some text instead.
- `/find-jobs <words>` → treat as a one-off search term, ignoring the configured clusters

Several jobs at once is normal. Process them all, report once.

---

## Before either path

Read `my/profile.yaml`, `my/search-config.yaml`, and `my/learnings.md` if it exists.

**No profile** → stop, send them to `/setup`. Scoring without a profile produces confident
nonsense.

**Setup incomplete** → say which parts are missing and that scores will be rough until it is
finished, then carry on.

List `my/jobs/` to build the seen-already set, keyed on `{source}-{source_id}`.

---

# The manual path

## 1. Get the advert

**From a URL:** fetch it. If the fetch is blocked, hits a login wall, or returns a page with no
advert on it, say so in one line and ask them to paste the text. Job boards block automated
fetching constantly; it is not a fault and does not need explaining at length.

**From pasted text:** use it as given.

Keep the URL either way. It is how they apply later.

## 2. Extract

Fill the fields in `templates/job.yaml`. Three need care:

**Salary.** Record what the advert says. If it states none, both fields are null and
`salary_note` says so. Never infer from the title.

**Requirements**, split into essential and desirable as the advert splits them. This drives the
blocker check and the targeting in `/apply`.

**Application format.** Cover letter, structured answers, or CV only. If the advert lists the
questions, capture them verbatim. Knowing this before anything is written saves the user from
producing a cover letter nobody asked for.

Vague advert → leave the field null. A null is honest and visible; a guess silently becomes
fact.

## 3. Deduplicate

`source_id` comes from the URL where there is one, otherwise organisation plus title, slugified.
If the file already exists, do not write a second. Say which one it is and its status, in a line.

## 4. Score and write

Score per [SCORING.md](SCORING.md). Write to `my/jobs/manual-{source_id}.yaml`, `status: new`,
`search_cluster: manual`.

A job the user supplied by hand is written **even if it scores below `minimum_score`**. They
chose it; discarding it silently is confusing. Say the score is below their threshold and let
them decide.

---

# The search path

## 1. Work out what is available

Check the environment for each source's credentials (see SOURCES.md) and cross-reference the
`sources` flags in the config. Announce what is actually happening before it takes time:

```
Searching: Adzuna (gb) · Reed
Skipping:  none
3 clusters, 7 search terms
```

If a source is flagged active but its key is missing, say so and skip it. If no source is
usable, say so and ask for a link or some text instead. That is not a failure state; it is the
normal state for many users.

## 2. Search

For each active cluster in the config, for each title and keyword, query each active source
using the parameters in [SOURCES.md](SOURCES.md). Apply the config's location, salary floor and
`max_results_per_search`.

**Keep the call count sane.** Clusters times terms times sources multiplies fast. If it comes to
more than about twenty calls, use the most distinctive terms per cluster and say what you did.
Nobody needs eleven near-identical searches.

**Prefer recent postings.** Where the source supports it, limit to roughly the last two weeks.
Where it does not, filter on the posting date afterwards. Old adverts are usually filled.

## 3. Filter before scoring, not after

Scoring is the expensive step: it means reading a full advert against the whole profile. Do the
cheap eliminations first, in this order, and report the counts.

1. **Already seen** — `{source}-{source_id}` exists in `my/jobs/`. Silent.
2. **Duplicate within this run** — the same role appears on several boards under different ids.
   Match on organisation plus title plus location.
3. **`exclude_terms`** from the config.
4. **Obvious field mismatch.** Broad terms drag in other industries wholesale, because a word
   that means one thing in the user's field means something else in another. Where the title and
   description clearly belong to a different profession, drop it. Be conservative: when unsure,
   let it through and let the score deal with it.
5. **Salary floor**, where the advert states one. Never filter on an estimated salary.

What survives gets scored properly.

## 4. Score

Per [SCORING.md](SCORING.md), against the full advert.

**Adzuna descriptions are truncated.** Where a job survives filtering and looks like it might
matter, fetch the advert URL for the full text before scoring. Scoring a two-line summary
produces a meaningless number.

Below `minimum_score`, discard without writing a file. Unlike the manual path, the user did not
choose these, and writing dozens of weak jobs makes `/review-jobs` useless.

## 5. Write

One file per surviving job at `my/jobs/{source}-{source_id}.yaml`, `status: new`, with the
cluster that surfaced it in `search_cluster`.

---

# Reporting

## One job

Give the assessment directly rather than a table:

> **Senior Analyst, Acme Trust**, Manchester, hybrid, £42-48k. Closes 29 August.
>
> **7 out of 10.** Ten years running referral services, which is the whole job here. The gap is
> the professional qualification, which they list as essential rather than desirable, so it needs
> addressing head on rather than hoping.
>
> They want four structured answers, not a cover letter.

## A search

Counts first, then the jobs worth their attention:

```
find-jobs complete
  Found:            84
  Already seen:     51
  Filtered out:     19   (12 wrong field, 5 excluded terms, 2 below salary)
  Scored:           14
  Below threshold:   9
  Written:           5
```

Then list the five, one line each, highest first. Then one next step.

**Flag any deadline inside a week prominently.** It is the one fact that changes what they
should do today.

**Report failed sources plainly**, without quoting any key:

> Reed didn't run: the key was rejected. Everything below is from Adzuna. Re-run `/setup` if you
> want to re-enter it.

## Boards you cannot search

Where `manual_boards` is set, mention it once per session, not per job:

> You listed NHS Jobs and CharityJob. I can't search those. Worth a look when you have a minute,
> and paste anything interesting straight in here.
