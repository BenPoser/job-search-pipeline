# Roadmap

Current state: scaffolded. Documentation, vocabulary, decisions and command specifications are
written. No command is implemented.

---

## Phase 1 — One person who is not the author can go end to end

The bar is a real user, in a field that is not software, getting from nothing to a sent
application without the author sitting next to them.

- [ ] `/setup` — the whole thing, resumable. The largest single piece of work.
- [ ] `/find-jobs` — manual paste first, then Adzuna, then Reed
- [ ] `/review-jobs`
- [ ] `/apply` — including the claim check, both output formats, and the `generated/` snapshot
- [ ] `/status`
- [ ] At least two CV templates, PDF and DOCX paths

Build order is that order. Nothing can be tested until `/setup` exists, and the manual paste path
in `/find-jobs` unblocks everything downstream without needing an API key.

### One constraint that spans the phases

`/apply` must write its `generated/` snapshot from the first release, even though nothing reads
it until Phase 2. Edit capture is the primary feedback signal and it cannot be reconstructed
later from applications that were never recorded. It is nearly free to write now and impossible
to recover later.

---

## Test with a real person before starting Phase 2

Everything in the setup design is a hypothesis about how someone with no evidence corpus talks
about their own career. One session with a real person in a real other field will invalidate more
of this design than another month of planning.

Pick the least technical friend available, not the most forgiving one.

---

## Phase 2 — The learning loop

- [ ] `/log-outcome`, including questions actually asked at interview
- [ ] Edit capture: diff `generated/` against what was sent
- [ ] `my/learnings.md` observations, and reading them back in `/find-jobs` and `/apply`
- [ ] `/prep-interview`, opening from the weak claims list
- [ ] `/update-profile`, including narrative generation

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
