# Job board keys

Read only if the user wants automatic job searching in phase 6. Skip entirely otherwise.

---

## Frame it honestly first

This is the most likely point in setup for someone to give up, because it is the only part that
sends them to another website to register for something. So be straight about the trade:

> Two job boards let me search for roles automatically, so jobs turn up without you looking.
> Setting that up takes about ten minutes and it's free.
>
> You don't have to. Pasting a job link in by hand works exactly as well, and everything after
> that point is identical. Plenty of people never bother.

If they hesitate at all, suggest skipping it. They can come back to it any time, and a user who
has actually applied for something is far more likely to invest ten minutes later than a user
who is still in setup.

**Never treat declining as a lesser path.** Manual entry is a permanent, fully supported mode.

---

## Adzuna (most countries)

Covers around twenty countries. Gives two values, an ID and a key.

Walk them through it one step at a time. Wait for them to confirm each step before giving the
next one. Do not paste the whole list at once.

1. Go to https://developer.adzuna.com/ and choose to sign up.
2. Register with an email address. It is free and there is no card involved.
3. Confirm the email if they are asked to.
4. Sign in. There is a dashboard page showing an **Application ID** and an **Application Key**.
5. Ask them to paste both to you.

The two values look like: an ID of about eight characters, and a key of about thirty two.
If they paste something that does not look like that, ask them to check they have both.

## Reed (United Kingdom only)

One value. Skip this entirely if the user is not in the UK.

1. Go to https://www.reed.co.uk/developers/jobseeker
2. Sign up for an API key. Free, and no card.
3. The key arrives on screen or by email.
4. Ask them to paste it.

---

## Storing them

Write them yourself to `.claude/settings.local.json`, creating the file if it does not exist and
merging into it if it does:

```json
{
  "env": {
    "ADZUNA_APP_ID": "...",
    "ADZUNA_APP_KEY": "...",
    "REED_API_KEY": "..."
  }
}
```

That file is gitignored, so the keys are never committed. Say so, briefly. People are right to
be wary about pasting credentials.

Then set the matching flags in `my/search-config.yaml`:

```yaml
sources:
  manual: true
  adzuna: true
  reed: true
```

Only set a flag true if you actually have the key for it.

---

## Check it works before moving on

Run one small search against each configured source, a single common term, a couple of results.
Do not score anything or write any job files. You are only proving the key works.

If it returns results:

> Adzuna's working, it found roles straight away.

If it fails, do not leave them to discover it later:

- **401 or 403** — the key is wrong. Offer to try re-entering it once. If it fails again, set
  that source back to false and move on. Setup must not stall here.
- **No results** — usually the country code. Check it against Adzuna's supported list. If their
  country is not covered, say so plainly and configure manual-only.
- **Anything else** — note it in the state file, set the source false, carry on.

A failed key is not a reason to interrupt setup. The manual path works regardless, and they can
retry later.
