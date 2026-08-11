---
name: apply
description: Produce the application pack for one job - a tailored CV as PDF and DOCX, a cover letter, and any application answers - including the claim check that cannot be skipped. Use when the user runs /apply or is ready to apply for a shortlisted role.
---

# /apply

Build everything needed to apply for one job.

Read [SELECTION.md](SELECTION.md) before choosing what goes on the CV, and
[CLAIM-CHECK.md](CLAIM-CHECK.md) before finalising anything. [DOCUMENTS.md](DOCUMENTS.md) has
the mechanics of producing each file. [TEMPLATES.md](TEMPLATES.md) covers building a template
from the user's own CV, or from one they like.

---

## Invocation

`/apply <job-file>`, or `/apply` and offer the shortlist, strongest and soonest-closing first.

## Read

The job file, `my/profile.yaml`, `my/voice.md`, `my/learnings.md`, `docs/quality-rules.md`, and
the template named in `preferences.cv_template`.

**No profile** → stop, send them to `/setup`.

**Job already has an `application_folder`** → warn and ask before doing anything. Overwriting a
CV they have hand-edited destroys work, and the edited version is also the feedback signal that
`/log-outcome` depends on.

---

## 1. Get the full advert

If the job file has `description_truncated: true`, or the description is obviously a summary,
**get the real advert before doing anything else.** Follow the ladder in
[../../../docs/fetching-pages.md](../../../docs/fetching-pages.md).

Tailoring a CV against 500 characters produces a document aimed at a job nobody advertised. The
body also routinely contradicts the metadata: a listing whose structured location said Central
London turned out, in the text, to be based near Edinburgh. That kind of thing decides whether
to apply at all.

If the full advert cannot be got and the user does not want to paste it, say plainly that the
tailoring will be shallow, and let them choose whether to continue.

## 2. Read the role properly

Before writing anything, work out four things and say them out loud in a sentence or two, so the
user can correct you before you spend effort on the wrong reading:

**What this employer actually wants.** Not the keyword list, the job. What appears first, and
what is repeated, is what they care about.

**The framing**, from `fit_type`:
- `core` — lead with the identity they already have
- `adjacent` — lead with the transferable spine and make the step look small
- `pivot` — lead with what transfers, and do not bury the change of field. A reader spots it in
  four seconds, and a CV that appears to be hiding it reads worse than one that owns it

**The gaps**, from the job file's `suitability.gaps`. The cover letter addresses them. It does
not pretend they are absent.

**The application format**, from `application.format`. Check this before writing a cover letter
nobody asked for. If the advert wants structured answers, the questions are already in the job
file.

## 2. Ask for what is missing

Where the role clearly wants something the profile does not cover, ask rather than writing
around it:

> They want experience of managing a budget and I cannot see any in your profile. Have you? Even
> informally, signing off spend or owning a cost line?

Whatever they answer goes into `my/profile.yaml` with provenance `interview` and today's date,
so it is asked once and never again. This is one of the main ways a profile grows.

Do not ask more than two or three of these. It is an application, not a second setup.

## 3. Select

Read [SELECTION.md](SELECTION.md). Choose the achievements, order the sections, and decide the
page split before writing any HTML.

## 4. Write the documents

Apply `my/voice.md` and `docs/quality-rules.md` together. **Quality rules win on conflict.**

See [DOCUMENTS.md](DOCUMENTS.md) for how each file is produced. In summary:

- **CV as HTML**, from the chosen template, then printed to PDF by the user
- **CV as DOCX**, single column and parser-safe, built by `scripts/build_docx.py`
- **Cover letter**, in their voice, where one is wanted
- **Application answers**, where the employer asks questions instead

## 5. The claim check

**Read [CLAIM-CHECK.md](CLAIM-CHECK.md) and run it. This step cannot be skipped**, shortened, or
deferred to the end of the conversation where it will be ignored.

It produces two things: questions for the user where the draft has outrun the evidence, and a
weak-claims list saved with the application for `/prep-interview` to open from.

## 6. The stranger test

Reread the whole pack as someone who has never met this person and knows nothing about their
employers or their field's internal language. Apply section 2 of `docs/quality-rules.md`.

The three that catch people every time: internal project names, employer-specific acronyms, and
numbers that are precise without being meaningful.

## 7. Write it out

```
my/applications/{slug}/
  cv.html            styled, for printing to PDF
  cv.docx            single column, parser-safe
  cover-letter.md    or answers.md
  weak-claims.md     what to expect to be asked about
  application.yaml   job reference, date, what was selected and why
  generated/         a copy of everything above, exactly as generated
```

The slug is kebab-case from organisation and job title, five words at most.

**`generated/` is not optional.** Nothing reads it yet, but the difference between what was
generated and what the user actually sends is the primary feedback signal (`docs/adr/0004`), and
it cannot be reconstructed later from an application that was never recorded. It costs a copy.

Then update the job file: `status: shortlisted`, and set `application_folder`.

## 8. Report

Say what was produced, and **which file to send where**, because most people do not know this
and it materially affects their chances:

> **DOCX** for agencies, large employers, and any application through a portal. Their systems
> read the file automatically and anything designed gets mangled.
>
> **PDF** for emailing a person directly, or a small organisation.

Then the print step, which is manual:

> Open `cv.html` in Chrome, File > Print > Save as PDF. Tick **Background graphics** or the
> colour disappears. Check the page break falls where you want it.

Then one next step: review it, edit anything that does not sound like them, and run
`/log-outcome` when something happens.

Do not claim the pack is finished or ready to send. It is a strong draft, and the user is the
author.
