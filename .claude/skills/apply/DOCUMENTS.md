# Producing the documents

Mechanics for each file in the application pack.

---

## The CV, as HTML

Copy the template named in `preferences.cv_template` from `templates/cv/` and fill it in.

- **`classic.html`** — colour accent, skill chips. Industry, commercial, tech, charity, design.
- **`plain.html`** — serif, no colour, conservative. Academia, law, medicine, finance, most
  public sector, and the safer choice when the reader is unknown.

Fill the placeholders. Do not restructure the CSS, and in particular do not add
`break-inside: avoid` to `.section`, which stops the forced page break working.

**Put page one content in `.cv-page-1` and the rest in `.cv-page-2`.** The split is a decision
made in the HTML, per [SELECTION.md](SELECTION.md). On screen a dashed red line shows where the
break falls, so overflow is visible before printing.

Printing is manual and must be explained every time, because two of the three steps are not
obvious:

> Open `cv.html` in Chrome, then File > Print > Save as PDF. Tick **Background graphics**,
> otherwise the colour drops out. Check the break falls where you want it.

---

## The CV, as DOCX

For agencies, large employers, and portals that parse the file automatically. Also the version
the user can edit in Word, which matters for anyone who cannot edit HTML.

Build it with the bundled script, which uses only the Python standard library:

```bash
python3 scripts/build_docx.py my/applications/{slug}/cv.docx < cv.json
```

The JSON is documented at the top of `scripts/build_docx.py`. Same content as the HTML, minus
anything decorative.

**Constraints, from `docs/quality-rules.md` section 5.** Single column. Standard heading names a
parser recognises: Experience, Education, Skills. No tables, text boxes, images, icons, columns,
or content in headers and footers. Contact details on one line, pipe separated. Anything
cleverer loses information for the candidate, which is the opposite of the point.

**If Python is not available**, say so plainly and write an RTF instead:

> Python isn't installed, so I can't build a .docx. I've made an .rtf instead. Word opens and
> edits it normally and application systems read it fine. If you'd rather have a .docx, install
> Python 3 and I'll rebuild it.

RTF is plain text and needs no runtime at all. Keep it equally plain: headings in bold, bullets
as a simple list, no tables.

Do not silently skip the second format. A user who sends a designed PDF to a parsing system and
hears nothing back will never know why.

---

## The cover letter

Only when `application.format` calls for one. Check first.

Four paragraphs, around 350 words, in the user's voice per the cover letter section of
`my/voice.md`.

1. **Why this role and this organisation.** Specific and genuine. Never open with "I am writing
   to apply for". If there is nothing genuine to say about the employer, leave the placeholder
   from [CLAIM-CHECK.md](CLAIM-CHECK.md) rather than inventing admiration.
2. **The fit.** Two or three sentences mapping their strongest relevant achievements to what the
   advert asks for. Specifics, not categories.
3. **The differentiator, and the gap.** What separates them from a competent generic applicant.
   Then address the most important gap from `suitability.gaps` directly: name it, and say what
   they have that substitutes or what they are doing about it. Do not pretend it is absent; the
   reader has already noticed.
4. **Close.** One sentence. No platitudes.

Leave `[HIRING MANAGER NAME]` as a placeholder where it is not known, and say it is worth two
minutes to find.

## Application answers

Where the employer asks structured questions instead. The questions are already captured in the
job file.

- **Answer the question asked**, not the one that would be convenient.
- **Follow the stated word limit.** Going over gets truncated by the form, usually mid-sentence.
- **Use the framework they use.** Competency questions in public and charity sectors normally
  expect a situation, the actions the candidate personally took, and the result. Follow the
  answers section of `my/voice.md` for whether to do that explicitly or narrate it.
- **One story per answer**, told properly. Two half-stories is the most common failure.
- **Different stories across answers.** Reusing the same example makes a career look thin.

---

## application.yaml

Written alongside, and read later by `/log-outcome` and `/prep-interview`:

```yaml
job: my/jobs/manual-acme-senior-analyst.yaml
organisation: Acme Trust
job_title: Senior Analyst
date_generated: 2026-08-11
fit_type: core
template: classic
page_target: 2

selected:
  - id: ach-004
    why: directly evidences the service redesign they lead the advert with
  - id: ach-011
    why: the only achievement with a hard number

left_out:
  - id: ach-002
    why: same point as ach-004 and weaker

gaps_addressed:
  - gap: no formal qualification
    how: cover letter paragraph 3, argued experience substitutes

format: cover-letter
```

## generated/

Copy every produced file into `generated/` before handing over. Nothing reads it yet.

It exists because the difference between what was generated and what the user actually sends is
the primary feedback signal (`docs/adr/0004`): it arrives within minutes, exists for every
application, and unlike an outcome it is not confounded by whether the employer had already
decided. It cannot be reconstructed later from an application that was never recorded, and it
costs a copy now.
