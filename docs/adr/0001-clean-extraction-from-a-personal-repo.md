# 1. Clean extraction from the precursor, accepting duplication

Date: 2026-08-10

## Status

Accepted

## Context

This project generalises a working single-user precursor, which remains in active use by its
owner and is not part of this repository.

The two have different constraints. The precursor is tuned to one person and can hard-code
anything about them. This one has to work on first run for someone it knows nothing about, in a
field it cannot assume.

Three ways to get from a working private tool to a shareable one:

1. Extract the machinery into a clean repository and leave the original running untouched.
2. Extract, then migrate the original to sit on top of the shared core as its first user.
3. Generalise the original in place, then clone and strip the personal data.

## Decision

Option 1. A new repository containing only machinery, documentation, and empty structure. The
precursor continues unchanged and is not migrated.

## Consequences

**Accepted cost: two implementations of similar commands, which will drift.**

The alternative was worse. Option 2 requires reworking the precursor while it is the thing
actually producing its owner's applications, which risks a live process to serve a tool for
other people.

**Option 3 was rejected on data safety.** Personal data reaches the new repository through git
history even after the working tree is cleaned. Recovering from that requires history rewriting,
and getting it wrong publishes someone's full career record, contact details and salary
expectations. The failure mode is bad enough to avoid the approach entirely.

**The baseline is a CV and a conversation**, because that is the only input every user is
guaranteed to have. That is a floor, not a ceiling: richer sources are a matter for the roadmap.
What matters is that the baseline path is the good path, not a degraded one.

**Improvements do not flow back automatically.** Anything learned here that is worth having in
the precursor is ported by hand, deliberately. There is no shared package and no sync.
