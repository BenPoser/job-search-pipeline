# Making a template from the user's own CV

The two shipped templates are starting points, not a house style. Most people already have a CV
whose look they are attached to, or have seen one they want to copy. Both are supported, and a
user should never feel stuck with a design that is not theirs.

Read when the user supplies an example, asks for a different look, or says a generated CV does
not look like their CV.

---

## What can be used as a source

**Their existing CV.** The most common case, and the easiest, because `/setup` already has it.
Someone who has used the same CV for years is usually attached to it and will trust a generated
one more if it looks familiar.

**A CV they admire.** A friend's, a template they downloaded, something they saw online. Take it
as a design reference only. Never carry across another person's content, and say so if any is
present.

**A description.** "Something cleaner, single column, no colour, my name bigger." Perfectly
workable, and often what someone means when they say they do not like the output.

**A required format.** Some employers, agencies and academic bodies mandate a structure. Follow
it exactly; it is a constraint, not a preference.

---

## Building it

1. **Read the source** and describe back what you see, so the user can correct you before you
   build anything: layout, typeface, colour, how sections are separated, how dates are placed,
   whether skills are chips or prose, how dense it is.
2. **Start from whichever shipped template is closer** rather than from nothing. They already
   carry the print CSS, the page architecture, and the constraints that make a PDF work.
3. **Keep the structural parts** even while changing the look:
   - `@page` sizing and margins
   - the page split architecture, and no `break-inside: avoid` on `.section`
   - `print-color-adjust: exact` on anything relying on a background colour
   - the class names, so future generation knows where content goes
4. **Write it to `my/templates/{name}.html`.** User templates live under `my/`, so they survive
   updates and are never overwritten (`docs/adr/0002`).
5. **Fill it with their real content and show them a printed page**, not a screenshot of the
   markup. A template is judged printed. Iterate from what they say.
6. **Offer to make it the default**, and set `preferences.cv_template` if they want that.

## What not to carry across

**Anything that breaks a parser.** If their old CV has a two-column layout, a sidebar, a photo,
or icons, reproduce it for the PDF only. The DOCX stays single column and plain regardless of
the template, because it exists to be machine read. Say this once rather than silently diverging:

> I can match that layout for the PDF. The Word version stays single column whatever the design,
> because that is the one employers' systems read automatically, and columns confuse them.

**A photo**, unless the user's country and sector expect one. In the UK, US and Ireland it is
normally a liability. In parts of Europe and Asia it is standard. Ask rather than assuming, and
do not editorialise about it.

**Their old content.** A template is layout. Content comes from the profile, through selection
and the claim check, every time.

---

## Per-application templates

Anything in `my/templates/` can be used for one application by setting `cv_template` on the job
file, without changing the default. Useful for someone applying across sectors with different
conventions, which is common during a career change.
