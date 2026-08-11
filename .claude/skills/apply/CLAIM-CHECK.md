# The claim check

Run before any document is finalised. **Not skippable.**

---

## Why this exists and why it is not optional

The worst thing this tool can do to someone is put a confident claim on their CV that collapses
when an interviewer asks about it. That is worse than a weak application, because it wastes an
interview they earned and it makes them look dishonest when they were only trusting their tools.

The risk is structural, not occasional. A language model writing a CV reaches for the strongest
available phrasing, because that is what CV prose looks like. The user, handed a polished
document about themselves for a job they want, is not well placed to argue with it. Nobody
checks a flattering claim as hard as an unflattering one.

So the check runs every time, and the user is asked rather than told.

---

## Trace everything

Every line on the CV, and every factual claim in the cover letter or answers, must trace to an
achievement in `my/profile.yaml` with provenance on it.

If a line cannot be traced, it is one of three things:

- **Invented.** Cut it.
- **A real thing the user said in this conversation.** Add it to the profile with provenance,
  then it is traceable.
- **An inference from two other facts.** Say so and check it. Inferences are where plausible
  falsehoods come from.

---

## Watch the verbs

Strengthening happens in the rewriting, not in the original claim, and it is easy to miss on a
reread because the sentence looks fine. Look specifically for movement along these lines:

| Profile says | Draft says |
|---|---|
| contributed to, was part of, supported | led, drove, spearheaded |
| helped with, assisted | owned, ran |
| worked on a team that delivered | delivered |
| was involved in the decision | made the decision |
| suggested | implemented |
| covered for the manager | managed |
| trained two colleagues | built the training programme |

Also watch scope creep in the nouns: a team becoming a department, a project becoming a
programme, a region becoming a country.

And watch invented precision. If the profile says "about a fifth" the CV cannot say 20%. If the
profile has no number, the CV has no number.

---

## Ask, do not adjust

When the draft has outrun the evidence, **put it to the user**. Do not silently soften it, which
loses a possibly true claim, and do not silently keep it, which is the failure this exists to
prevent.

> Your profile says you contributed to the supplier migration. This draft says you led it. Which
> is right? If you led it, I'll update your profile too so it doesn't come up again.

Rules for asking:

- **Show both versions.** People judge better with the alternatives side by side than in the
  abstract.
- **Make either answer comfortable.** The point is accuracy, not confession. Nothing in the
  phrasing should suggest they were caught at something.
- **Batch them.** Three or four questions at the end of the draft, not one interruption per
  bullet. A per-line interrogation makes the tool exhausting and trains people to click through.
- **Act on the answer both ways.** If the stronger version is true, update
  `my/profile.yaml` and set `confirmed_wording` so this is settled permanently. If it is not,
  use the weaker version.

If more than about five claims need asking about, something is wrong upstream: either the
profile is too thin for this role, or the selection has reached for material that does not fit.
Say so and reconsider the selection rather than negotiating line by line.

---

## The employer paragraph

Cover letters invite a specific kind of fabrication: enthusiasm about the organisation.

*"I have long admired your work on..."* is exactly the sentence a model invents, it is
unverifiable, and it is embarrassing if the interviewer follows up.

Anything specific about the employer must come from the advert, from their own site if it was
actually read, or from something the user said. If there is nothing genuine, leave a visible
placeholder:

> [WHY THIS ORGANISATION - tell me what draws you to them and I'll write it, or write this line
> yourself]

A visible gap is honest and gets filled. A plausible invention gets sent.

---

## The weak-claims list

Separately from the questions, produce a list of claims that survived but rest on thin evidence:
a single sentence with no metric, no corroboration, nothing behind it if pressed.

These are not errors. They are the lines most likely to be probed at interview, and knowing
which they are is valuable. Write them to `weak-claims.md` in the application folder:

```markdown
# Claims most likely to be probed

## "Led the supplier migration"
Evidence: one sentence from the setup interview. No metric, no timeline, no named
outcome. Confirmed by the user on 11 Aug as accurate.
Prepare: what the migration involved, who else was on it, what it changed.

## "Cut waiting times by 40%"
Evidence: the user's recollection, no document. The number is the strongest thing on
the CV and the most likely to be tested.
Prepare: how it was measured, over what period, what caused it.
```

`/prep-interview` opens from this file. It is the thing that makes preparation specific to them
rather than generic advice, so it is worth writing properly.
