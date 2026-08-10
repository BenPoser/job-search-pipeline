# Making it yours

The default process is opinionated so that it works on day one. It is not meant to stay that
way, and you do not need to be technical to change it.

**The easiest way to change anything is to say so.** Open this folder in Claude Code and ask:

> My cover letters are too long. Make them three short paragraphs from now on.

> I want a section on my CV for publications, before Experience.

> Stop searching for contract roles, I only want permanent.

> Add a step after `/apply` that reminds me to follow up after ten days.

Claude will find the right file and change it. You do not have to know which file that was.

---

## What lives where, if you want to look

Everything is plain Markdown or YAML. Nothing is compiled, hidden, or magic.

| File | What changing it does |
|---|---|
| `my/voice.md` | How generated documents sound. Separate sections for CV bullets, cover letters, and application answers. |
| `my/search-config.yaml` | What roles get searched for: titles, locations, salary floor, remote preference, and your search clusters. |
| `my/profile.yaml` | Your career record. Edit directly if you prefer, or use `/update-profile`. |
| `my/learnings.md` | What the tool thinks it has noticed. Delete anything you disagree with. |
| `docs/quality-rules.md` | The craft standards applied to every document. |
| `docs/tone.md` | How the commands talk to you. |
| `templates/cv/` | What your CV looks like. |
| `.claude/skills/<command>/SKILL.md` | The commands themselves, in full. |

---

## The guardrails, and turning them down

Some behaviour is deliberately firm out of the box. All of it is visible and most of it is
adjustable, but each one exists for a reason worth knowing before you remove it.

**The claim check in `/apply` cannot be skipped.** Every line on a generated CV is traced back
to your profile, and anything phrased more strongly than your evidence supports is put to you
before the document is finished. This is the one thing the tool will not let you turn off,
because a claim that collapses in an interview is the worst outcome it could produce for you.
You can make it quieter by making your profile more precise, which is the better fix anyway.

**Your `my/` folder is excluded from version control by default.** If you turn that off, make
absolutely sure the repository is private. It contains your full career history, your contact
details, and your salary expectations.

**Quality rules override your voice profile.** If you write a voice rule that contradicts a
quality rule, the quality rule wins. If you disagree with a quality rule, change the quality
rule rather than fighting it from the voice file.

**Suitability scoring is blunt on purpose.** It is meant to save you evenings, not to encourage
you. If you want it gentler, say so, but understand that you are asking to be sent on more
applications that will not go anywhere.

---

## Adding a job board

The tool can search Adzuna and Reed. Plenty of fields have better sources that it cannot search:
NHS Jobs, Teaching Vacancies, CharityJob, jobs.ac.uk, and many industry-specific boards.

Two options:

1. **Paste jobs in by hand.** Fully supported, works with any board on earth, and nothing
   downstream cares where a job came from.
2. **Ask Claude to add the board.** If it has a public API, say so and Claude can add it to
   `/find-jobs`. Each source needs an endpoint, an authentication method, a mapping from its
   fields to ours, and a paging rule. Look at how Adzuna and Reed are described in
   `.claude/skills/find-jobs/SKILL.md` for the shape of it.

---

## Going further

Nothing about this tool assumes you use it the way it was designed. People have different
searches. If the sensible process for you is three commands and a spreadsheet, delete the rest.
It is your folder.
