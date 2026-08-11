# Job board sources

Reference for the automatic search path. Read when `/find-jobs` runs a search.

---

## Credentials

Keys live in `.claude/settings.local.json` under `env`, which puts them in the environment as
`ADZUNA_APP_ID`, `ADZUNA_APP_KEY` and `REED_API_KEY`.

**Always pass them as shell variables, never as literal values.** A command containing the
actual key prints the key into the conversation, where it stays. Write `"$ADZUNA_APP_KEY"`, not
the key itself. The same applies when reporting errors: say "the Adzuna key was rejected", never
quote the key back.

Check what exists before searching:

```bash
[ -n "$ADZUNA_APP_ID" ] && [ -n "$ADZUNA_APP_KEY" ] && echo "adzuna ok"
[ -n "$REED_API_KEY" ] && echo "reed ok"
```

If a variable is empty but the config says the source is active, the keys were never saved or
the environment has not picked them up. Say so, skip that source, carry on.

---

## The shape of a source

Four things, and nothing more elaborate is needed until there are more than three:

1. **Endpoint** and query parameters
2. **Authentication** method
3. **Field mapping** to `templates/job.yaml`
4. **Paging** rule

There is no plugin framework and there should not be one yet.

---

## Adzuna

Multi-country. **The country is a path segment, not a parameter.**

```bash
curl -s --get "https://api.adzuna.com/v1/api/jobs/${COUNTRY}/search/1" \
  --data-urlencode "app_id=$ADZUNA_APP_ID" \
  --data-urlencode "app_key=$ADZUNA_APP_KEY" \
  --data-urlencode "what=senior analyst" \
  --data-urlencode "results_per_page=20" \
  --data-urlencode "max_days_old=14" \
  --data-urlencode "salary_min=40000"
```

`--data-urlencode` with `--get` handles encoding, so multi-word terms need no escaping.

**Pipe the response, do not write it to a file.** On Windows this is `curl.exe`, which does not
understand Git Bash paths like `/tmp/x.json` or `/c/Users/...` and fails with a file-not-found
that looks like a network problem. Piping straight into whatever parses the JSON avoids the
whole class of problem and works identically on every platform.

**Do not pass `where` for a country-wide search.** The path segment already scopes it, and
passing a country name returns zero results with no error: `where=United Kingdom` against
`/gb/` gives `count: 0` while the same query without it gives hundreds. Use `where` only to
narrow to a city or region, and only when the user's config has a city.

**An unsupported country returns 404 with the authoritative list in the response**, so there is
no need to hardcode one:

```json
{"exception":"UNSUPPORTED_COUNTRY",
 "display":"The currently supported ISO 3166 country codes are at, au, be, br, ca, ch, de,
            es, fr, gb, in, it, mx, nl, nz, pl, sg, us, za"}
```

Read the list out of the error and tell the user which countries are covered, rather than
guessing or repeating a list that may have gone stale.

**Field mapping**

| Response | Job file |
|---|---|
| `id` | `source_id` |
| `title` | `job_title` |
| `company.display_name` | `organisation` |
| `location.display_name` | `location` |
| `salary_min` / `salary_max` | salary, subject to the rule below |
| `created` | `date_posted` |
| `redirect_url` | `url` |
| `description` | `description`, though it is usually truncated |
| `category.label` | `sector` |

**Treat a predicted salary as absent.** `salary_is_predicted` is the **string** `"1"`, not a
boolean, so a truthiness check on it is always true and would discard every salary. Compare
against `"1"` explicitly. When it is set, put null in both salary fields and "not stated in
advert" in `salary_note`. A predicted figure is easy to spot by eye too, because it arrives with
decimals: a real advert does not offer £47,993.64.

**The description is truncated to 500 characters**, cut mid-word.

**And `redirect_url` usually cannot be fetched.** Adzuna sits behind CloudFront, which returns
403 to automated requests regardless of user agent. Assume refetching will fail rather than
building a step around it.

The consequence is unavoidable and must be handled honestly: **scores from an Adzuna search are
provisional**, based on a 500-character summary rather than the advert. Say so in the report,
and do not ask the user to paste a dozen adverts at search time to fix it. Get the full text at
`/apply` time instead, when there is exactly one job and it is worth the thirty seconds.

**Multi-word `what` terms narrow hard**, apparently matching all words rather than any. A search
for `senior software engineer C# .NET` in London returned a single result where broader terms
return hundreds. Prefer two or three distinctive words per search and run more searches, rather
than one long precise-looking string that quietly returns nothing.

**Contract day rates are annualised into `salary_min`**, with nothing in the structured fields
saying so. A six-month contract at £500 per day appears as `salary_min: 130000`, which reads as
an exceptional permanent salary and will float to the top of any ranking. `contract_type` is
frequently absent, so it cannot be relied on to catch this.

Detect it from the title and description instead: day rates, "IR35", "inside"/"outside",
"3 months", "6 months", "interim", "fixed term". Where the user's config lists only `permanent`
in `employment_types`, filter these out before scoring rather than letting an inflated figure
distort the shortlist.

**`/jobs/land/ad/...` links are interstitial redirect pages**, not adverts. They bounce to the
original board, which is where the real text lives. Read the page after the redirect completes,
not the moment it loads, or all you get is "You are now being redirected".

**Fields come and go.** `contract_time` and `contract_type` are absent from many records rather
than null. Read defensively and do not assume a key exists.

**Paging**: the final path segment is the page number, starting at 1. One page is almost always
enough; only page further if the user explicitly wants more volume.

## Reed

United Kingdom only. Skip entirely for users elsewhere.

**Untested.** Everything documented for Adzuna below was checked against the live API. Reed was
not, for want of a key. Treat the details here as likely rather than confirmed, and verify on
first use.

```bash
curl -s --get -u "$REED_API_KEY:" "https://www.reed.co.uk/api/1.0/search" \
  --data-urlencode "keywords=senior analyst" \
  --data-urlencode "locationName=Manchester" \
  --data-urlencode "minimumSalary=40000" \
  --data-urlencode "resultsToTake=20"
```

The trailing colon after the key matters: Reed uses Basic auth with the key as username and an
empty password. `curl -u` handles the encoding.

**Field mapping**

| Response | Job file |
|---|---|
| `jobId` | `source_id` |
| `jobTitle` | `job_title` |
| `employerName` | `organisation` |
| `locationName` | `location` |
| `minimumSalary` / `maximumSalary` | salary |
| `date` | `date_posted` |
| `expirationDate` | `deadline` |
| `jobUrl` | `url` |
| `jobDescription` | `description`, truncated |

Reed dates come as `DD/MM/YYYY`. Convert to ISO before writing.

Reed has no "posted within N days" parameter. Filter on `date` after fetching.

**Paging**: `resultsToSkip`, with `resultsToTake`. Same advice: one page is normally enough.

---

## Errors

Handle per source and never stop the whole run:

| Symptom | Meaning | Do |
|---|---|---|
| 401 or 403 | Key wrong or not activated | Say which source, suggest re-running `/setup` to re-enter it, skip |
| 404 on Adzuna | Country not supported | Read the supported list out of the response, tell the user, fall back to manual-only |
| 429 | Rate limited | Wait a few seconds, retry once, then skip |
| Empty results everywhere | Usually `where` passed for a country search, or too high a salary floor | Check both before reporting "no jobs" |
| Timeout or network error | Transient | Retry once, then skip |

A failed source is a line in the report, not an interruption. The manual path always works.
