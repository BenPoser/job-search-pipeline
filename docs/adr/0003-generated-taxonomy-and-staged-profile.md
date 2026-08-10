# 3. Per-user generated taxonomy, and narratives deferred until earned

Date: 2026-08-10

## Status

Accepted

## Context

Achievements need classifying, so that selecting material for an application is repeatable
rather than improvised each time. A tag taxonomy built for one field does not transfer: the
terms that organise an engineer's career are meaningless for a nurse, a teacher or a marketer.

So the first question is what a per-user taxonomy comes from. Three options:

1. Generate one per user, from their own CV and setup interview.
2. Ship presets per field, and have setup ask which field the user is in.
3. Have no taxonomy, and rely on the model reading everything at generation time.

Achievements also need grouping into themes once there are enough of them to make selection
lossy. That is the second question: whether a new user gets narratives immediately or later.

## Decision

Generate the taxonomy per user (option 1).

Defer narratives. `/setup` produces only a Profile. Narratives are generated later by
`/update-profile`, once the Profile is large enough to need them, and the tool tells the user
when that point has arrived.

## Consequences

**Field presets were rejected as a maintenance trap.** Five bundled taxonomies would be subtly
wrong for everyone and would need extending for every new field a user arrives from. Worse, they
force a choice of box at the exact moment it is least appropriate: a large share of users are
mid-pivot, with hybrid careers that no single preset represents. Generating from the user's own
history costs one setup step and is correct by construction.

**No taxonomy at all was rejected** because tags are what make achievement selection repeatable.
Without them, every generated CV is an independent improvisation over the whole profile, and two
applications to similar roles can surface different material for no reason the user can see or
correct.

**A generated taxonomy is only as good as the setup interview.** A thin interview produces vague
tags, which degrades every later selection. This raises the stakes on `/setup` quality and is
the main reason setup reads documents before interviewing rather than after.

**Deferring narratives means the retrieval layer is missing early on**, and generation must work
directly against the raw Profile. This is fine, because an early Profile is small enough to
consider whole. That is precisely why narratives are unnecessary at that stage: they are a
retrieval optimisation for a corpus too large to hold at once, and clustering a dozen
achievements into a dozen themes is ceremony that makes the tool feel bureaucratic on the first
day.

**Something must decide when narratives are worth generating.** Currently a judgement made by
`/update-profile` and surfaced as a suggestion, not an automatic threshold.
