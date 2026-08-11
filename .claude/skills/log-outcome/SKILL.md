---
name: log-outcome
description: Record what happened after an application, capture what the user changed before sending, and update the learnings file. Use when the user runs /log-outcome or mentions a rejection, an interview invitation, an offer, or that they have heard nothing back.
---

# /log-outcome

Record the result, learn what can honestly be learned, and stop.

---

## Tone

This command exists mostly to record rejections. `docs/tone.md` applies with particular force.

Record it and move on. No cushioning, no encouragement, no exclamation marks on bad news. The
user knows what the process is like and does not need a piece of software to acknowledge it.

---

## 1. Find the application

`/log-outcome <slug>`, or with no argument list applications with no outcome recorded, oldest
first, and ask which. If they have just told you what happened ("heard back from Acme, no luck"),
match it yourself rather than making them pick from a list.

## 2. Record the outcome

Ask what happened, unless they have already said. One of `interview`, `rejection`, `silence`,
`offer`. Write it to the job file's `outcome` block with today's date.

**If they were interviewed, ask what they were actually asked.** Do it now, in the same breath,
while they still remember:

> What did they actually ask you? Even roughly. It makes the next prep session much better.

This is the densest, cleanest data the system ever gets: immediate, specific, and not confounded
by anything. Store it in `outcome.questions_asked`.

**If the employer gave feedback, capture it verbatim.** It is rare and worth more than any
inference drawn from silence.

**Silence is a valid outcome and should be recordable without ceremony.** Do not push someone to
categorise a non-response as a rejection.

Update `status` on the job: `closed` for a rejection or a declined offer, `interviewing` where a
process is live, `applied` where it is still silence.

## 3. Capture the edits

**This is the more valuable half of this command**, and the user does not have to do anything for
it.

Compare the files in the application folder against their copies in `generated/`. The difference
is what the user changed before sending, which is a direct correction of the tool's judgement,
arriving within minutes rather than weeks and uncontaminated by whether the employer had already
decided.

```bash
diff -u my/applications/{slug}/generated/cv.html my/applications/{slug}/cv.html
```

Read the differences for meaning, not as a patch. Four things to look for:

- **An achievement swapped out or removed.** The selection was wrong. Which tags or reasoning led
  you to it? Note it, because selection errors repeat.
- **Rephrasing that keeps the meaning.** The voice profile is off. Update `my/voice.md` and say
  that you have. This is the fastest way that file gets good.
- **Cuts.** Something read as irrelevant, or the document ran long.
- **Additions.** Something was missing from the profile. Offer to add it properly with
  provenance.

If nothing changed, that is information too: say so briefly and move on. Do not manufacture a
finding.

Where a pattern appears across several applications, act on it rather than only noting it. If the
user has rewritten the same kind of bullet three times, the voice profile needs changing, not the
learnings file.

## 4. Write observations

Append to `my/learnings.md` in plain language. Never numeric weights, never a claimed model
(`docs/adr/0004`).

```markdown
## 11 Aug 2026
Every role that reached interview named stakeholder management in the first three lines of the
advert. The two that went quiet did not. Worth weighting that higher in scoring.
```

Rules:

- **Written so the user can argue with them.** They know things about their own search that the
  log does not contain.
- **Say when there is not enough data.** With four applications logged, "not enough yet to see a
  pattern" is the correct output. Inventing one is worse than saying nothing.
- **Do not build an observation on silence** unless the pattern is stark. Silence is the normal
  outcome and usually says nothing about the candidate.
- **Separate the two kinds.** An observation about what employers respond to is different from an
  observation about what the tool got wrong. Both are useful; conflating them is not.

## 5. Report

Short. What was recorded, anything learned, and the base rate if a ratio comes up:

> Recorded: rejection, 11 Aug. You cut two bullets and rewrote the summary before sending, both
> toward shorter sentences, so I have tightened that in your voice profile.
>
> That is 2 responses from 22 applications. Within the normal range; most applications go
> unanswered regardless of the candidate.

Then one next step, usually `/review-jobs` or `/find-jobs`. If there is nothing to do, say so.
