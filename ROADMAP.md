# Roadmap

Current state: scaffolded. Documentation, vocabulary, decisions and command specifications are
written. No command is implemented.

---

## Phase 1 — One person who is not the author can go end to end

The bar is a real user, in a field that is not software, getting from nothing to a sent
application without the author sitting next to them.

- [x] `/setup` — written, including the interview guide and the API key walkthrough.
      Run once by the author, including a resume across two sittings.
- [x] `/find-jobs` — manual path, with the scoring rubric in SCORING.md
- [x] `/find-jobs` — Adzuna and Reed. Adzuna verified against the live API; Reed is written
      from documentation only and has never been run.
- [x] `/review-jobs`
- [x] `/status`
- [x] `/apply` — claim check, both output formats, and the `generated/` snapshot
- [x] Two CV templates (classic, plain), plus a stdlib DOCX builder. DOCX package verified
      valid and extracting cleanly. Both templates verified through a real HTML to PDF print,
      page breaks landing correctly.
- [x] User-supplied CV designs, defaulted or overridden per application

Build order is that order. Nothing can be tested until `/setup` exists, and the manual paste path
in `/find-jobs` unblocks everything downstream without needing an API key.

### One constraint that spans the phases

`/apply` must write its `generated/` snapshot from the first release, even though nothing reads
it until Phase 2. Edit capture is the primary feedback signal and it cannot be reconstructed
later from applications that were never recorded. It is nearly free to write now and impossible
to recover later.

---

## Phase 1 is done and verified end to end

Run on live Adzuna listings, 11 Aug 2026: find, score, review, apply, print. Three design
failures found and fixed in the process (page fetching, contract day rates annualised into
salary, metadata contradicting the advert body). See docs/fetching-pages.md.

Still unverified: the Reed source, which has never been run for want of a key.

## Test with a real person before starting Phase 2

Everything in the setup design is a hypothesis about how someone with no evidence corpus talks
about their own career. One session with a real person in a real other field will invalidate more
of this design than another month of planning.

Pick the least technical friend available, not the most forgiving one.

---

## Phase 2 — The learning loop

- [x] `/log-outcome`, including questions actually asked at interview
- [x] Edit capture: diff `generated/` against what was sent
- [x] `my/learnings.md` observations, and reading them back in `/find-jobs` and `/apply`
- [x] `/prep-interview`, opening from the weak claims list
- [x] `/update-profile`, including narrative generation

All written, none exercised. They cannot be properly tested until real applications have been
sent and come back, which takes weeks rather than a session. Expect the first real
`/log-outcome` run to find things, the way the first end-to-end run did.

---

## Not scheduled

- Further profile sources beyond a CV, LinkedIn and the interview. Build one when a user turns
  up who has something richer to import, and design it so the interview works over the imported
  material rather than being skipped, since raw records rarely carry the result or the metric.
- More job sources. Add one when a real user needs it, not before. Sector boards matter more
  than aggregators in several fields: NHS Jobs, Teaching Vacancies, CharityJob, jobs.ac.uk.
- Scheduled background searching.
- Pipeline analytics beyond what `/status` shows.

---

## Open questions

- What actually triggers the suggestion to generate narratives? Currently a judgement call in
  `/update-profile` with no defined threshold.
- How much does `/apply` output really need editing in practice? Until several real applications
  have gone through, the honest description of this tool is unknown: does it generate a finished
  draft, or a strong starting point? Do not claim the stronger version until it is true.
- Does the DOCX path need a library, or is a minimal Word-compatible document generated directly
  good enough?
