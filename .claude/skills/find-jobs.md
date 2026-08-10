# /find-jobs

Find roles and score them against the profile. Two equally supported ways in: paste one, or
search the boards.

**Status: designed, not yet built. This file is the specification.**

---

## Invocation

- `/find-jobs` with no argument: search the configured sources
- `/find-jobs <url>`: take one job by link
- `/find-jobs` followed by pasted advert text: take one job from text

The manual path is not a fallback. It works with any job board in the world, including the ones
this tool cannot search, and a user who never configures a key can use every part of the
pipeline. See `docs/adr/0002` context and `CONTEXT.md` on Job Source.

---

## Reads

`my/search-config.yaml`, `my/profile.yaml`, `my/learnings.md`, and the filenames already in
`my/jobs/` (for deduplication).

---

## Manual path

Fetch the URL, or take the pasted text. Extract title, organisation, location, salary, closing
date, and the description. If the fetch is blocked, ask them to paste the text and do not make it
a production.

Assign `source: manual` and a stable `source_id` derived from the URL or from organisation plus
title. Then score it exactly as a searched job is scored.

---

## Search path

Only run sources marked active in the config.

### Adzuna

```
GET https://api.adzuna.com/v1/api/jobs/{country}/search/1
  app_id, app_key, what={term}, salary_min, results_per_page
```

The country code is a path segment. Do not pass `where` for a country-wide search, it returns
nothing; use `where` only to narrow to a city.

### Reed (United Kingdom only)

```
GET https://www.reed.co.uk/api/1.0/search
Authorization: Basic base64(REED_API_KEY + ":")
  keywords, locationName, minimumSalary, resultsToTake
```

### Adding another source

Each source needs four things: an endpoint, an authentication method, a mapping from its fields
to ours, and a paging rule. That is the whole abstraction. There is no plugin framework and
there should not be one until there are more than three sources.

### Missing credentials

Skip that source, note it in the report, carry on. Never stop the run. If no source is active,
that is not an error, say what the manual path is and stop.

Print the active sources at the start:

```
Sources: Adzuna active. Reed skipped, no key set. Manual always available.
```

---

## Deduplicate

Skip anything whose `{source}-{source_id}` already exists in `my/jobs/`, silently.

---

## Score

For each new job, read the advert against the profile and produce:

- **score** 1 to 10
- **fit type**: `core`, `adjacent` or `pivot`, relative to *this person's* profile
- **rationale**: two or three sentences naming specific matching strengths and the most
  important genuine gap

Be blunt. A low score with a clear reason saves an evening. Talking someone into a poor
application costs them one and produces the silence that makes their next report look worse.

Read `my/learnings.md` and let the observations there influence scoring. They are soft
guidance written in plain language, not weights (`docs/adr/0004`). If an observation applies,
say so in the rationale so the user can see the influence and disagree with it.

Apply `exclude_terms`. Broad keyword searches pull in adjacent industries that share vocabulary,
and the resulting noise makes users distrust the whole thing.

Below `minimum_score`, discard without writing a file.

---

## Write

One YAML file per job at `my/jobs/{source}-{source_id}.yaml`, with `status: new`. Store the
description trimmed to roughly 400 words at a sentence boundary, enough for later scoring and CV
generation without bloating the file.

---

## Report

```
find-jobs complete
  New:             7
  Already seen:   31
  Below threshold: 5
```

Then, if `manual_boards` is configured, remind them once:

> You listed CharityJob and NHS Jobs as boards you use. I cannot search those. Worth a look, and
> paste anything interesting in with /find-jobs.

Then a single next step: `/review-jobs`.
