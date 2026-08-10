---
name: review-jobs
description: Triage found jobs one at a time and record apply, dismiss or hold decisions. Use when the user runs /review-jobs or wants to work through what a search turned up.
---

# /review-jobs

Walk the user through jobs that have been found, one at a time, and record what they decided.

**Status: designed, not yet built. This file is the specification.**

---

## Why this is separate from /find-jobs

Finding can run unattended, including on a schedule while the user is asleep. Triage needs the
user. Keeping them separate means a search does not force a decision at the moment it happens,
and twenty jobs can be worked through in one sitting when there is half an hour for it.

It also means the user is never asked to move files between folders to express a decision, which
`docs/adr/0002` and the setup principles rule out.

---

## Reads

Every job in `my/jobs/` with `status: new`, plus `my/profile.yaml` and `my/learnings.md`.

## The walkthrough

Highest score first. For each job, show a compact card: title, organisation, location, salary,
closing date, score, fit type, and the rationale. Then the honest read.

Ask for a decision. Accept: apply, dismiss, hold, or "tell me more" (show the full description).

Record it: `shortlisted`, `dismissed`, or leave as `new` with a note for hold. When dismissing,
ask why in a few words and store it. Those reasons are the raw material for `exclude_terms` and
for observations later, and they are cheap to collect at the exact moment the user has the
opinion.

## Be willing to say no

This tool makes applying cheap, and cheap applying is bad strategy. Where a score is low and the
gap is a hard requirement, say so:

> This one scored 4. They want a qualification you do not have and it is listed as essential,
> not desirable. Your evening is better spent on the two 8s further down.

That is a feature. Volume is not a strategy, and every hopeless application produces the silence
that makes the user's learnings look worse than reality.

## Batch sanity

If there are more than about fifteen waiting, offer to do the top ten now and leave the rest.
Grinding through forty cards in one sitting produces careless decisions.

## Finish

Summarise: shortlisted, dismissed, held. Then one next step, normally `/apply` on the strongest
shortlisted job, named specifically rather than in the abstract.
