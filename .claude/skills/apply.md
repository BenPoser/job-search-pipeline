# /apply

Produce the application pack for one specific job: tailored CV in both formats, cover letter,
and application answers where the employer asks for them.

**Status: designed, not yet built. This file is the specification.**

---

## Invocation

`/apply <job-file>`, or `/apply` and pick from the shortlist.

## Reads

The job file, `my/profile.yaml`, `my/voice.md`, `my/learnings.md`, `docs/quality-rules.md`,
`docs/tone.md`, and the CV template named in `preferences.cv_template`.

---

## 1. Read the role

From the advert and the suitability rationale, work out:

- Which parts of the profile actually matter here. Use the taxonomy to select, so that two
  applications to similar roles surface consistent material rather than independent
  improvisations.
- **Framing by fit type.** `core`: lead with the identity they already have. `adjacent`: lead
  with the transferable spine and make the step look small. `pivot`: lead with what transfers,
  and do not bury the change of field, because a reader will spot it in four seconds and a CV
  that seems to be hiding it reads badly.
- The genuine gaps named in the rationale. The cover letter addresses them; it does not pretend
  they are absent.
- Whether the employer wants a cover letter or structured answers. Check before writing a cover
  letter nobody asked for. Structured competency questions are the norm in large parts of the
  public and charity sectors.

## 2. Ask for what is missing

Where the role clearly wants something the profile does not cover, ask rather than working
around it. The answer goes into the profile with provenance `interview`, so it is asked once.
This is one of the main ways a profile grows.

## 3. Write the documents

Apply `my/voice.md` and `docs/quality-rules.md` together. **The quality rules win on conflict.**

**CV**, in two forms from the same content:
- Styled PDF, within `preferences.page_target`
- Plain DOCX: single column, standard headings, no tables or text boxes or images. This is the
  one that survives automated parsing, and the one the user can edit in Word.

**Cover letter**, in their voice. Anything specific about the organisation must come from the
advert or from something the user has said. If there is nothing genuine, leave a visible
placeholder rather than inventing an admiration they do not have.

**Application answers**, where asked for, matching the employer's competency framework and the
answers section of the voice profile.

## 4. The claim check

**This step cannot be skipped.** It is the most valuable thing this tool does.

Trace every line back to the profile. Look specifically for strengthening in the rewriting:
*contributed to* becoming *led*, *helped with* becoming *owned*, *was part of a team that*
becoming *delivered*. This drift is easy to introduce and hard to catch on a reread.

Where the draft is stronger than the evidence, stop and put it to the user:

> Your profile says you contributed to the supplier migration. This draft says you led it.
> Which is right? If you led it, I will update your profile too.

Then act on the answer, and write the confirmation into the profile so the same question is not
asked on the next application.

Also produce a **weak evidence list**: claims that survived but rest on thin support, a single
sentence with no metric or corroboration. Store it in the application folder. `/prep-interview`
opens with it, because those are the lines most likely to be probed.

Why this is non-negotiable: the worst thing this tool can do to someone is put a confident claim
on their CV that collapses when an interviewer asks about it. The check catches the
overstatement, keeps the user as the author of their own claims, and improves the profile
whenever the stronger version turns out to be true.

## 5. The stranger test

Reread the whole pack as someone who has never met this person and knows nothing about their
employers or their industry's internal language. Apply `docs/quality-rules.md` section 2. Cut
internal names, unexplained acronyms, and detail that is specific without being informative.

## 6. Write out, and record

```
my/applications/{slug}/
  cv.html
  cv.pdf
  cv.docx
  cover-letter.md
  answers.md            (if applicable)
  generated/            snapshot of everything as generated
  weak-claims.md
  application.yaml      job reference, date, fit type, what was selected and why
```

**`generated/` must be written from the first release**, even though nothing reads it yet.
The difference between what was generated and what the user actually sends is the primary
feedback signal (`docs/adr/0004`): it exists for every application, arrives within minutes, and
is not confounded by whether the employer had already decided. It cannot be reconstructed later
from an application that was never recorded.

If the folder already exists, warn and ask before overwriting. Overwriting a hand-edited CV is
destructive.

Update the job to `status: shortlisted` and link the application folder.

## 7. Report

State what was produced and **which file to send where**: the DOCX for agencies, large employers
and public sector portals whose systems parse the file; the PDF for emailing a person or applying
to a small organisation.

Then one next step: review it, edit it, and run `/log-outcome` when something happens.
