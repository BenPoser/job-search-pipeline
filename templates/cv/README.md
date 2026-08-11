# CV templates

Two outputs are produced for every application, from the same profile data.

These two designs are starting points, not a house style. A user can supply their own CV, or one
whose look they like, and have a template built from it into `my/templates/`. See
`.claude/skills/apply/TEMPLATES.md`. A user template can be the default or used for a single
application.

## The PDF path (`*.html`)

For emailing a person, or applying directly to a small organisation. Design freedom within the
user's page target.

- **`classic.html`** — colour accent, skill chips. Industry, commercial, tech, charity, design.
  Verified through a real print to PDF.
- **`plain.html`** — serif, no colour, conservative. Academia, law, medicine, finance, most
  public sector, and the safer choice when the reader is unknown. Also supports running past two
  pages, which academic and clinical CVs routinely do. Verified through a real print to PDF.

Rules any template must follow:

- A4 by default, page size configurable
- Page breaks must be structural, not negotiated with the print engine. Split page content into
  sibling top-level containers and force the break between them, rather than relying on
  `break-inside: avoid` inside nested elements, which browsers apply inconsistently.
- Backgrounds and colour must survive PDF export (`print-color-adjust: exact`)
- Respect `preferences.page_target` from the profile
- Respect `preferences.page_mode`: `split` chooses the break deliberately, `flow` lets content
  run on and break where it lands without splitting an entry

## The DOCX path

For agencies, large employers, and public sector portals, whose systems parse the file
automatically. Also the version a user can open in Word and edit themselves, which matters for
anyone who cannot edit HTML.

Hard constraints, from `docs/quality-rules.md`:

- Single column
- Standard heading names a parser recognises: Experience, Education, Skills
- No tables, text boxes, images, icons, or multiple columns
- No content in headers or footers

Anything clever here loses information for the candidate.
