---
name: update-profile
description: Add new experience to the profile, deepen an existing achievement, correct something, or generate narratives once the profile is large enough. Use when the user runs /update-profile, mentions experience that is not recorded yet, or wants to fix something in their profile.
---

# /update-profile

Grow the profile. This is what makes everything else get better over time.

The setup interview produces a starting point, not a finished record. Profiles also grow through
`/apply` asking for detail it needs and `/prep-interview` capturing a better articulation under
pressure, but this is the deliberate route.

Read `.claude/skills/setup/INTERVIEW.md` before interviewing. The technique is the same:
restore the result, the metric, the context, and what was specifically theirs.

---

## Work out what they want

Ask, or infer from what they have said. Do not present a menu of five modes to someone who has
just told you they got promoted.

### Add a role

New job, promotion, contract, volunteering, a course. Capture the basics, then interview for two
or three real achievements. Do not try to fill it in one sitting.

A promotion within the same organisation is usually a new role, not an edit, because the scope
changed. Ask.

### Add an achievement

To an existing role. Often something they only recognised as notable later, or something a
`/apply` session reminded them of.

### Deepen an achievement

Take a thin entry and make it real.

**Prioritise anything that has appeared on a `weak-claims.md` list.** Those are known to be
causing trouble in generated documents, and fixing one improves every future application rather
than just this conversation. Say so, because it makes the work feel worth doing:

> "Named production incident responder" has now been flagged on two applications, and it came up
> in your last interview prep with no story behind it. Worth ten minutes on it now?

### Correct something

Including correcting an overstatement. Make this easy and unremarkable. Someone who feels
awkward correcting their own profile will leave the overstatement there, which is the worst
outcome.

If a correction contradicts a `confirmed_wording` set by an earlier claim check, clear it and say
you have.

### Regenerate the taxonomy

After significant additions, or a change of direction. New work introduces domains the original
taxonomy has no term for, and selection quietly degrades when the vocabulary no longer fits.

Show the changes rather than the whole list, so the user can see what moved.

---

## Recording

Same schema, same discipline. `templates/profile.yaml` is the shape.

Every addition gets provenance with today's date. Keep raw structure, not CV prose: `action`,
`result`, `metric`, `context`, `capabilities`. Capture their own words as a quote where they say
something well.

**Never invent a metric.** If they do not know, the metric is absent.

---

## Narrative generation

Narratives do not exist in a new profile, deliberately (`docs/adr/0003`). They are a retrieval
layer for a profile too large to consider whole, and clustering a dozen achievements into a dozen
themes is ceremony rather than value.

**Watch for the point where selection starts being lossy**: the profile has grown enough that
`/apply` cannot weigh all of it properly, and roughly the same few achievements keep surfacing
regardless of the role. Around thirty achievements is where this usually starts, but the signal
matters more than the number.

Then suggest it. Do not impose it:

> You have 38 achievements across 6 roles now. That is more than I can weigh properly on every
> application, and I have noticed the same five keep coming up. Worth twenty minutes grouping
> them into themes so selection gets sharper. Now, or another time?

**A narrative is** a theme with a headline claim and a ranked shortlist of the achievements that
best evidence it. Derive them from the user's actual history, not from a standard list of career
themes, and show them for correction. The user's sense of what their career is about is better
than any clustering you will produce.

Aim for five to nine. Fewer and they do not discriminate; more and they stop being themes.

Write them into the `narratives` block of `my/profile.yaml`. `/apply` will use them as the first
place it looks.

---

## Suggest it at the right moment

Do not wait to be remembered. Offer when:

- `/apply` had to ask for something the profile should have contained
- The same weak claim has been flagged on more than one application
- Nothing has been added since setup and several applications have gone out
- They mention in passing that they have started something new, finished a course, or changed role
- A `/prep-interview` session produced a much better version of a story than the profile holds

Keep the offer to one line, and take no for an answer.
