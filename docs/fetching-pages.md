# Getting a page the tool cannot fetch

Job boards and professional networks block automated requests aggressively. This is normal, it
is not a fault, and it should never be presented to the user as an error.

Used by `/find-jobs` (job adverts), `/apply` (full advert before tailoring) and `/setup`
(LinkedIn profiles).

---

## The ladder

Try in order. Stop at the first that works.

**1. Fetch it directly.**

Works for a lot of what matters: company career pages, and applicant tracking systems like
Ashby, Greenhouse, Lever and Workable, which most modern employers use for their own listings.
Always worth trying first because it is instant and silent.

**2. Ask the user's own browser, if Claude in Chrome is connected.**

The Chrome extension drives the browser the user is already signed into, and renders pages as a
human visitor, so bot-blocking does not apply and login walls are already passed.

This is the difference between working and not working on the big aggregators. Adzuna's own
listing pages sit behind CloudFront and return 403 to every automated request regardless of user
agent, while loading normally through the extension.

Check whether it is available before offering it. If it is not installed, do not send the user
away to install something mid-task; go to step 3 and mention the extension afterwards as a
one-off improvement.

**3. Ask them to paste it.**

Always works, needs nothing, and takes them about fifteen seconds. Ask plainly and without
apology:

> That job board blocks automated access. Paste the advert text in and I'll take it from there.

Do not explain CloudFront. Do not apologise twice.

---

## Do not batch step 3

Asking a user to paste twelve adverts so that twelve scores can be firmed up, eleven of which
they are about to discard, is a bad trade for their time.

Score on whatever is available, say the score is provisional where it is, and get the full text
at `/apply` time, when there is exactly one job and it is obviously worth thirty seconds.

---

## Why the full advert matters

A truncated summary is enough to triage and not enough to act on, and the gap is not only
length. Aggregator metadata is frequently wrong in ways only the body reveals.

A worked example, from a real listing: the API reported the location as Liverpool Street,
Central London, while the advert body said the role was based near Edinburgh. For a user
filtering on a London commute, that single sentence is the whole decision, and nothing in the
structured fields carries it.

So when tailoring an application, work from the advert, not the summary. Where only the summary
is available, say so rather than quietly tailoring against 500 characters.
