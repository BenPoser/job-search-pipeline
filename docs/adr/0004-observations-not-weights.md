# 4. The feedback loop produces observations, not weights

Date: 2026-08-10

## Status

Accepted

## Context

The tool promises to learn from what happens. The obvious reading of that promise is that
outcomes adjust the weighting of the scoring model over time.

There is no weighting model. Scoring is a language model reading a job advert against a profile.
There are no numeric knobs to turn.

More importantly, the data does not support anything statistical. A serious job search produces
perhaps thirty to sixty applications. The dominant outcome is silence, and silence is close to
uninformative: it may mean the CV was weak, or that the role was filled internally before the
application was read, or that an agency never opened it. Fitting parameters to forty
observations dominated by a non-signal is not analysis.

Three options:

1. Read the outcome log as context at scoring time and let the model adjust its judgement.
2. Derive explicit plain-language observations that the user can read, correct and delete, and
   have the scoring and generation steps read them.
3. Maintain numeric weights over matching criteria.

## Decision

Option 2. `/log-outcome` writes observations in plain language to `my/learnings.md`.
`/find-jobs` and `/apply` read that file. The user can edit or delete any line.

Separately, the difference between a generated document and the version the user actually sent
is captured and treated as the primary feedback signal.

## Consequences

**Numeric weights were rejected as fake precision**, and shipping them to other people would
have meant shipping a lie. A tool that claims to have learned a model of someone's job search
from forty noisy observations is not being honest with a user who is under real pressure and
inclined to trust it.

**Reading the raw log as context was rejected for being unauditable.** The user could never see
why a score moved, or disagree with the reason. An explicit observation can be argued with,
which matters because the user knows things about their own search that the log does not
contain.

**Observations degrade honestly.** With three applications logged, the correct output is "not
enough data yet", and that is stated rather than papered over with an invented pattern.

**Edit capture carries more weight than outcomes**, which is worth stating plainly because it
inverts the intuitive design. Edits are produced by every single application, arrive within
minutes, and are uncontaminated by whether the employer had already decided. Outcomes are
sparse, delayed by weeks, and confounded. The consequence is that `/apply` must retain its
generated output from the first release, even before anything reads it, because a diff cannot be
reconstructed later from an application that was never recorded.

**Whenever a ratio is shown to the user, the base rate is shown with it.** Not for reassurance,
but because a response rate reported without the market context is a true number that misleads.
