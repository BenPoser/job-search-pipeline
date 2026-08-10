# /prep-interview

Prepare for a specific interview.

**Status: Phase 2. Designed, not yet built. This file is the specification.**

---

## The thing only this tool can do

It knows exactly which document the interviewer is holding, because it wrote it. It knows which
achievements were selected, how they were phrased, and which claims were thinnest, because the
claim check in `/apply` produced that list.

So this does not open with common interview questions. Anyone can get those anywhere. It opens
with the claims on the user's own CV most likely to be probed, ranked by how thin the evidence
behind them is:

> Three things on this CV will get probed. The strongest is the intake redesign, you have real
> numbers there. The riskiest is "led the supplier migration": one sentence of evidence, no
> metric, and at setup you were not sure whether you led it or co-led it. Let us build a real
> answer for that first.

Everything else in this command is commodity. That is not.

---

## Reads

The application folder (CV as sent, cover letter, `weak-claims.md`), the job advert,
`my/profile.yaml`, and `my/learnings.md` including questions actually asked at previous
interviews.

## Shape

1. **Claim audit.** The weak evidence list turned into the questions it will generate.
2. **Ask the format**, because it changes everything and varies enormously by field: competency
   and STAR, technical, panel, presentation, case study, values-based. Do not assume.
3. **Run a real mock.** The user answers, you push back for specificity, they go again. Do not
   hand over model answers to memorise. A prepared answer that came out of their own mouth
   survives follow-up questions; a memorised one does not.
4. **Cover the standard ground** for the format, grounded in their evidence rather than in
   general advice: why this role, why this organisation, the hardest thing they have delivered,
   a difficult stakeholder, their genuine gap and what they have done about it.
5. **Cheat sheet**, one page: stories mapped to likely competencies, the honest gap and its
   answer, two or three questions worth asking the panel.

## Persist

Write to the application folder:

- `interview-prep.md`, the cheat sheet
- `interview-transcript.md`, the full mock

Keep the transcript. Rereading a fumbled first answer is useful, and it is more evidence about
how the user actually talks, which feeds the voice profile.

## Write back to the profile

People routinely produce their best articulation of an achievement under interview pressure,
better than anything they said during setup. When that happens, update the achievement in
`my/profile.yaml` with provenance `interview` and the date, and tell the user you have done it.

This means `/prep-interview` mutates the profile. That is deliberate: the best material should
not be trapped in a transcript.

## Afterwards

Remind them to run `/log-outcome` after the interview **while the questions are still fresh**,
because which questions were actually asked is dense, immediate, uncorrupted information and it
makes every future preparation session better.
