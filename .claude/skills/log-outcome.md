# /log-outcome

Record what happened after applying, and write what can honestly be learned from it.

**Status: Phase 2. Designed, not yet built. This file is the specification.**

---

## Tone

This command exists mostly to record rejections. `docs/tone.md` is binding here.

Record it and move on. No cushioning, no encouragement, no exclamation marks. The user is an
adult who knows what the process is like, and a piece of software saying so is worth nothing.

---

## Capture

For the application: `interview`, `rejection`, `silence`, or `offer`, with a date.

**If there was an interview, ask which questions were actually asked.** Ask it in the same
breath, while they still remember. This is the densest, cleanest data the whole system ever
gets: immediate, specific, and not confounded by anything. Store it against the application and
in the learnings file.

If they have feedback from the employer, capture it verbatim. It is rare and worth more than any
inference.

## Edit capture

Compare `generated/` against what is now in the application folder. The diff is the primary
feedback signal (`docs/adr/0004`): it exists for every application, arrives within minutes, and
unlike an outcome it is not contaminated by whether the employer had already decided.

Look for:

- **Achievements swapped out.** The selection was wrong. Which tags misled it?
- **Rephrasing.** The voice profile is off. Update `my/voice.md` and say that you have.
- **Cuts.** Something was judged irrelevant, or too long.
- **Additions.** Something was missing from the profile. Offer to add it.

## Observations

Append plain-language observations to `my/learnings.md`. Never numeric weights, never a claimed
model. See `docs/adr/0004` for why.

> Every role that has reached interview mentioned stakeholder management in the first three lines
> of the advert. The two that went quiet did not.

Rules:

- Written so the user can read, argue with, and delete them. They know things about their own
  search that the log does not contain.
- **Say when there is not enough data.** With four applications logged, "not enough yet to see a
  pattern" is the correct output. Inventing one is worse than saying nothing.
- Distinguish signal from base rate. Silence is the normal outcome and usually says nothing about
  the candidate. Do not build an observation on top of it unless the pattern is stark.
- **Whenever a ratio is shown, show the base rate with it.** A five to ten percent response rate
  is ordinary in a competitive market. Reporting "two responses from twenty two" without that
  context is a true number that misleads.

## Effect

`/find-jobs` and `/apply` read `my/learnings.md` and let it influence scoring and selection.
When it does, they say so in their rationale, so the influence is visible and can be disagreed
with.
