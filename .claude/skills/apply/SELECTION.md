# Choosing what goes on the CV

Read before writing any HTML. Selection decides whether a CV works; phrasing only decides how
well it reads.

---

## The principle

A CV is not a record of a career. It is an argument that this person should be interviewed for
**this** job. Everything on it either supports that argument or is taking up space that
something better could use.

So selection is subtractive. Start from the whole profile, keep what argues, cut the rest.

---

## How to select

**1. Work out what the employer needs done.** Read the advert for the job, not the vocabulary.
What is in the first paragraph, and what is repeated, is what they care about. Requirements
listed ninth of eleven are usually aspirational.

**2. For each of those needs, find the strongest achievement that evidences it.** Use the
taxonomy to search rather than rereading everything, and prefer:

- **Evidence over assertion.** An achievement with a result beats one without.
- **Recent over old**, unless the old one is dramatically stronger.
- **Specific over broad.** "Cut time to first contact from 11 days to 3" beats "improved
  processes".
- **Comparable scale.** An achievement at roughly the scale of the target role argues for it.
  One much smaller invites the reader to notice the gap.

**3. Where two achievements make the same point, keep one.** Repetition reads as padding and
costs a line that could carry a different argument.

**4. Stop when the page budget is full**, not when the profile runs out.

## Where narratives exist

If `my/profile.yaml` has narratives, use them as the retrieval layer: pick the two or three
themes this role is about and select from their shortlists first. Fall back to searching the
full profile for anything the themes miss.

If there are no narratives, search the profile directly. That is the normal case early on, and
it works because an early profile is small enough to hold whole.

---

## Framing by fit type

**`core`** — they already do this job. Lead with that identity. The CV's job is to look
inevitable: same work, same level, evidently competent. Do not oversell; a core candidate loses
by looking desperate, not by looking ordinary.

**`adjacent`** — a step up or sideways. Lead with the transferable spine, and make the step look
small. Find the achievements that already reach into the target level, even partially: the
project where they did the harder thing, the stand-in period, the piece of scope beyond their
grade. The argument is "already doing parts of this", not "ready for a challenge".

**`pivot`** — a change of field. Two rules.

First, **do not bury the change.** A reader works it out in four seconds from the job titles, and
a CV that appears to be hiding it reads as evasive. Name it in the summary, in one clause,
without apology.

Second, **translate rather than list.** Achievements from another field need their transferable
content surfaced, in the target field's language, without misrepresenting what happened. Say
what was actually done and what it demonstrates. Do not restate it as though it happened in the
new field.

---

## Ordering the sections

Whatever the strongest argument is goes highest. The reader may not get further than a third of
the page.

- **`core` and `adjacent`**: usually summary, skills, experience.
- **`pivot`**: usually summary, then skills or a capability section, then experience. Experience
  is the weakest part of a pivot case and putting it first invites a rejection before the case
  has been made.
- **Academic, clinical, and research roles**: conventions differ sharply and matter. Education,
  registration, and publications often come before experience. Follow the field, not this file.

Within skills, reorder rows so the categories the advert emphasises come first. Do not invent
skills to match the advert, and do not drop real ones to make room for keywords.

---

## The page budget

`preferences.page_target` sets the length. Two pages for UK industry, one for a US résumé, more
for academic and clinical. Overrunning a convention the reader holds is a real cost, and so is
padding to reach it.

At roughly 9.5pt with normal spacing, an A4 page holds about 55 lines. Count before writing.

**Decide the split before writing the HTML**, not afterwards. The templates put page one and
page two in separate top-level divs precisely so the split is a decision rather than a
negotiation with the print engine. Page one carries the header, summary, skills, and the most
recent role. Everything else follows.

If it overflows, cut an achievement rather than shrinking the type. A cramped CV reads as
cramped.

---

## Record what you chose

Write the reasoning into `application.yaml` in the application folder: which achievements were
selected, which themes drove it, and what was deliberately left out.

Two reasons. The user can disagree with a specific decision rather than with the whole document.
And when `/log-outcome` compares what was generated against what they actually sent, the
recorded reasoning is what makes the difference interpretable rather than just a diff.
