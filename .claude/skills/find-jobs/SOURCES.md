# Job board sources

**Not wired up yet.** `/find-jobs` currently handles the manual path only. This file holds what
is needed to build the automatic path, and the shape any future source should follow.

---

## The shape of a source

Four things, and nothing more elaborate is needed until there are more than three:

1. **Endpoint** and query parameters
2. **Authentication** method
3. **Field mapping** from their response to `templates/job.yaml`
4. **Paging** rule

There is no plugin framework and there should not be one yet.

---

## Adzuna

Covers around twenty countries. Country is a path segment, not a parameter.

```
GET https://api.adzuna.com/v1/api/jobs/{country}/search/{page}
  app_id={ADZUNA_APP_ID}
  app_key={ADZUNA_APP_KEY}
  what={search term}
  salary_min={floor}
  results_per_page={n}
```

**Do not pass `where` for a country-wide search.** The country path segment already scopes it,
and passing a country name as `where` returns zero results. Use `where` only to narrow to a city
or region.

Response fields map as: `id` → source_id, `title` → job_title, `company.display_name` →
organisation, `location.display_name` → location, `salary_min` / `salary_max` → salary,
`created` → date_posted, `redirect_url` → url, `description` → description, `category.label` →
sector.

**Treat a predicted salary as absent.** Where the response marks the salary as estimated rather
than stated, set both salary fields null and note it. Their estimates are frequently wrong and a
wrong salary is worse than none.

**Broad terms pull in other industries.** Words that mean one thing in the user's field often
mean something else elsewhere, and the aggregator does not know the difference. Filter on the
config's `exclude_terms` and score the rest honestly.

## Reed

United Kingdom only. Skip entirely for users elsewhere.

```
GET https://www.reed.co.uk/api/1.0/search
Authorization: Basic base64(REED_API_KEY + ":")
  keywords={search term}
  locationName={location}
  minimumSalary={floor}
  resultsToTake={n}
```

Response fields map as: `jobId` → source_id, `jobTitle` → job_title, `employerName` →
organisation, `locationName` → location, `minimumSalary` / `maximumSalary` → salary, `date` →
date_posted, `expirationDate` → deadline, `jobUrl` → url, `jobDescription` → description.

---

## When this gets built

**Missing credentials are not an error.** Skip that source, note it in the report, carry on. If
no source has keys, that is the normal case, not a failure.

**Validate the country against Adzuna's supported list** before searching, and fall back to
manual-only with a plain explanation rather than returning nothing.

**Deduplicate across sources.** The same role appears on multiple boards under different ids.
Matching on organisation plus title plus location catches most of it.

**Scoring is identical regardless of source.** A job found automatically and a job pasted in by
hand go through the same rubric and produce the same file.
