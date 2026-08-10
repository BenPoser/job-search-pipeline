# /setup

Build the user's profile, voice, and search settings. Runs once, resumably.

**Status: designed, not yet built. This file is the specification.**

---

## Principles

**The user never edits a file or runs a command.** You write everything. If you need a file
moved, moved it yourself. Never say "now open search-config.yaml and set salary_min".

**Resumable is a hard requirement.** A good setup takes 45 to 90 minutes and almost nobody does
that in one sitting. Track phase state in `my/setup-state.yaml` after every phase. On invocation,
read it and resume, opening with a one-line summary of what is already done rather than starting
again.

**Read documents before interviewing.** An interview that has read the CV asks about specifics.
An interview that has not asks "tell me about your career", which is a form, and feels like one.

**This is not a form.** Follow interesting answers. Skip what does not apply. A user in a field
where CV bullets are not the norm should not be pushed through questions built for one that is.

---

## Phase 0 — Orientation

Say what is about to happen and how long it takes. Confirm they can stop any time and resume
with `/setup`.

Ask what field they work in and what kind of move they are making. This shapes every later
phase, particularly the taxonomy and the interview questions.

Write `my/setup-state.yaml`.

## Phase 1 — Documents

Ask for their current CV. They can drop it in `my/inbox/` or drag it into the chat. PDF or DOCX.
Read it.

Offer, without pressure, in this order:

1. **LinkedIn.** Ask for the URL and try to fetch it. Public profiles sometimes work; often the
   fetch returns an authentication wall. If it fails, say so and ask for screenshots instead,
   which is the reliable path. Do not make this feel like a failure, it is normal.
2. **A LinkedIn data export**, only for someone who wants to go deep. Settings, Data Privacy,
   Get a copy of your data. It arrives by email within 24 hours. **This must never block
   setup.** Note it in the state file and carry on. A later session can ingest it.
3. **Anything else** they think is useful: an old application, a performance review, a job
   description they wrote.

Extract roles, dates, education, and any achievement-shaped statements. Record provenance
`cv` or `linkedin` against everything.

Tell them what you found: "That gives me 5 roles from 2014 to now, and about 12 things you did.
Most of them are one-line claims with no detail, which is normal for a CV. That is what the
interview is for."

## Phase 2 — The interview

The core of setup and where the value is. A CV bullet is a compressed claim with the result,
metric and context stripped out. Restore them.

Work role by role, most recent first, since recent work matters most and energy fades.

For each achievement-shaped claim already found, probe for what a CV strips:

- What actually changed because of it?
- How did anyone know it worked? Is there a number, and is it a real one?
- What made it hard? Scale, constraints, resistance, who else was involved?
- What was your part specifically, as against the team's?

That last question is the important one, and it is the beginning of the truthfulness guardrail.
Ask it neutrally, as a question about accuracy rather than a challenge. See "Gentle overstatement
flagging" below.

Then ask what is missing. Most people leave their best work off their CV because it did not fit,
or because it did not feel like an achievement at the time. Ask directly: what are you proud of
that is not on here? What did people come to you for?

Record everything with provenance `interview`, the date, and the user's own words as a quote
where they said something well.

### Gentle overstatement flagging

Inflation enters the profile here, and a claim fixed at setup is fixed once rather than caught
on every application afterwards.

But do not interrogate someone in their first hour. When a claim is clearly stronger than what
they have just described, ask once, lightly, and record whichever answer they give:

> Just so I get this right, were you running that or were you part of the group doing it? Either
> is fine, I just want the profile to match what you would say out loud in an interview.

Do not push twice. `/apply` will catch anything that survives.

## Phase 3 — Taxonomy

From the profile you now have, generate this person's taxonomy: domains, capabilities, and
career stages, in their own field's language. Do not use a preset and do not import terms from
another field. See `docs/adr/0003`.

Show it to them. Two or three corrections here improve every later selection.

## Phase 4 — Voice

Ask for a few things they have written. Anything: an email they were pleased with, a previous
cover letter, a report, a blog post. Two or three is plenty. Say it is optional.

If they provide samples, derive an explicit style guide using `templates/voice.md` as the shape,
and **show them what you concluded**:

> You write short sentences, you almost never use "I believe" or "I feel", you prefer concrete
> nouns, and you use British spelling with no serial comma. Does that sound like you?

If they provide nothing, write a minimal voice profile from how they have talked during the
interview, and say that is what you have done.

Explain that this file is theirs and changes anything they dislike about generated documents.

## Phase 5 — Search settings

**Lead with example adverts.** Ask for two or three real job adverts they would genuinely apply
for. Paste or link. This is far easier than inventing keywords, and it produces better settings:
real titles, real salary bands, and the beginnings of the scoring criteria.

Derive `my/search-config.yaml` using `templates/search-config.yaml` as the shape. Fill the
clusters that apply and mark the rest inactive. A user not considering a career change does not
need a pivot cluster.

Ask their country and check it against Adzuna's supported list. If unsupported, say so plainly
and configure manual-only. Do not leave them to discover it as an empty result set.

Ask which job boards they already use, including ones with no API, and record them in
`manual_boards`. `/find-jobs` will prompt them to check those and paste anything worth having.

Ask the page target, with the convention explained: two pages for UK industry, one for a US
résumé, more for academic.

## Phase 6 — Job board keys (optional)

Frame honestly: it takes about ten minutes, it is free, and it means jobs get found without them
looking. Then say clearly that pasting job links in by hand works just as well and plenty of
people never do this.

If they want to, walk them through it one screen at a time:

- **Adzuna**: https://developer.adzuna.com/ , gives an app ID and an app key
- **Reed** (United Kingdom only): https://www.reed.co.uk/developers/jobseeker , gives one key

Write them to `.claude/settings.local.json` under `env` yourself. That file is gitignored.
Set the relevant `sources` flags in the search config.

If they decline, set `sources.manual: true` only and move on without comment. Do not ask again
on later runs; `/find-jobs` can mention it once if they ever seem to want more volume.

## Phase 7 — Backup choice

Ask this explicitly. Do not leave it to the README, because the people at risk are exactly the
ones who will not read that section.

> Your profile lives only on this computer. I can commit it to a **private** GitHub repository
> instead, which gives you a backup and a history as it grows. The only risk is if that
> repository is ever made public, since this file has your full history, contact details and
> salary expectations. Which would you prefer?

If they choose backup: remove `my/` from `.gitignore`, verify the remote is private, commit.
If the remote is public, refuse and explain.

If they decline: leave the default and mention, once, that the folder is worth copying somewhere
occasionally.

## Phase 8 — Finish

Show them what exists now. Then give exactly one next step, not eight:

> Your profile is ready. Type `/find-jobs` and paste in a job you are interested in, or let it
> search for you. If you ever forget where you are, `/status` will tell you.

Tell them their profile is not finished and is not supposed to be. It grows through
`/update-profile`, through interview preparation, and through the questions `/apply` asks when it
needs detail it does not have.

---

## Resuming

On invocation, read `my/setup-state.yaml`. If it exists and is incomplete:

> You are part way through setup. Done: profile from your CV, the interview for your two most
> recent roles. Next: the remaining roles. About 20 minutes. Carry on?

If it is complete, do not rerun. Ask what they actually want and point them at
`/update-profile` if they want to add experience.
