# /update-profile

Add experience, go deeper on something already recorded, and generate narratives once the
profile has earned them.

**Status: Phase 2. Designed, not yet built. This file is the specification.**

---

## Why it matters

What comes out of an hour of setup is a starting point. The tool gets better as the profile gets
richer, and this is the main deliberate way that happens. The others are incidental: `/apply`
asking for detail it needs, and `/prep-interview` capturing a better articulation produced under
pressure.

---

## Modes

**Add a role.** New job, promotion, contract, volunteering, course. Same interview approach as
setup phase 2: get the result, the metric, the context, and specifically what was *their* part.

**Add an achievement** to an existing role. Often something they only realised was notable later.

**Deepen an achievement.** Take a thin entry and make it real. Prioritise anything that appeared
on a `weak-claims.md` list, because those are the ones already known to be causing problems in
generated documents.

**Correct something.** Including correcting an overstatement. Make this easy and unremarkable.

**Regenerate the taxonomy.** After significant additions, or after a change of direction. New
work can introduce domains the original taxonomy has no term for.

Record everything with provenance and date, as ever.

---

## Narrative generation

Narratives do not exist in a new profile, deliberately (`docs/adr/0003`). They are a retrieval
layer for a profile too large to consider whole, and clustering a dozen achievements into a
dozen themes is ceremony rather than value.

Watch for the point at which selection starts being lossy: the profile is large enough that
`/apply` cannot weigh everything properly. Then suggest it, do not impose it:

> You now have 40 achievements across 6 roles. That is more than I can weigh properly on every
> application. Worth spending twenty minutes grouping them into themes, so selection gets
> sharper. Now, or later?

A narrative is a theme with a headline claim and a ranked shortlist of the achievements that
best evidence it. Derive them from the user's actual history, not from a standard list, and show
them for correction. The user's sense of what their career is about is better than any
clustering.

---

## Suggest it at the right moment

The tool should notice and offer, rather than waiting to be remembered:

- `/apply` had to ask for something the profile should have contained
- A weak claim has come up on more than one application
- Nothing added since setup and several applications have gone out
- The user mentions in passing that they have started a new job
