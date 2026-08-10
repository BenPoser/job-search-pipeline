# The full process

How the pieces fit together, and why the process has the shape it does.

You do not have to read this to use the tool. `/status` will always tell you the next step. Read
it when you want to understand what is happening, or when you want to change it.

---

## The shape of it

```
  /setup  ──────────────►  your profile, your voice, your search settings
     │                              │
     │                              ▼
     │                        /update-profile  ◄──── grows over time
     │                              │
     ▼                              │
  /find-jobs  ─────►  /review-jobs  │
     ▲                     │        │
     │                     ▼        ▼
     │                    /apply  ──────►  CV + cover letter + answers
     │                        │
     │                        ▼
     │                 /prep-interview
     │                        │
     │                        ▼
     └──────────────  /log-outcome  ─────►  learnings
```

The loop at the bottom is the point. Most job search advice is generic because it has no idea
what happened to you last time. This does.

---

## 1. Setup

Runs once, takes about an hour, and you can stop and resume as often as you like.

It reads your CV first, then interviews you. That order matters: an interview that has already
read your CV asks *"your CV says you redesigned the intake process, what actually changed and
how did you know it worked?"* rather than *"tell me about your career."* The first is a
conversation. The second is a form.

You can also point it at your LinkedIn profile or give it screenshots. If you want to go
further, LinkedIn will export your full data on request and setup can read that too, but it is
not expected.

Setup produces four things:

- **Your profile.** Roles and achievements, each recorded with where it came from.
- **Your taxonomy.** A set of tags built from *your* career, not from a preset list. This is
  what lets the tool pick relevant material reliably instead of rereading everything and
  guessing.
- **Your voice.** If you give it a few things you have written, it works out how you write and
  shows you what it concluded so you can correct it.
- **Your search settings.** Built mainly from two or three real job adverts you paste in.
  Inventing search keywords is hard. Recognising a job you would apply for is easy.

Setup also asks about backing up your profile, and about job board API keys. You can say no to
both and everything still works.

### The profile is never finished

What you produce in an hour is a starting point. The tool gets better as the profile gets
richer, and the profile gets richer through `/update-profile`, through interview preparation
(people often articulate an achievement best under pressure), and through the questions `/apply`
asks you when it needs detail it does not have.

---

## 2. Finding jobs

Two ways in, and they are equally supported.

**Paste one in.** Give it a link or paste the text of an advert. This works with any job board
in the world, including ones with no API, including a role a friend forwarded you.

**Let it search.** If you have set up a job board key, it will search for you against your
search clusters and score everything it finds.

Either way, every job gets a suitability score, a fit type, and a short honest rationale that
names the real gap rather than talking you into it.

There are job boards it cannot search, and in some fields they are the important ones: NHS Jobs,
Teaching Vacancies, CharityJob, jobs.ac.uk. Setup asks which boards you already use and records
them, so `/find-jobs` can remind you to check them and paste anything worth having.

---

## 3. Reviewing

`/review-jobs` walks you through what has been found, one at a time, and records what you
decided. It is a separate step from finding, so that a search can run while you are asleep and
be triaged when you have half an hour.

It is willing to tell you not to bother. A role that scored 4 out of 10 with a hard requirement
you do not meet is not worth an evening. Volume is not a strategy, and the tool that makes
applying cheap has a duty not to encourage spraying.

---

## 4. Applying

`/apply` produces, for one specific job:

- A **styled PDF CV**, for emailing a person or applying directly to a small company.
- A **plain DOCX CV**, single column with standard headings, for agencies, large employers, and
  public sector portals whose systems parse your CV automatically and mangle anything fancy. It
  is also the one you can open in Word and edit yourself.
- A **cover letter**, in your voice.
- **Application answers**, if the employer asks structured questions instead of a cover letter.

Then it checks itself.

### The claim check

Before anything is finalised, every line is traced back to your profile. Where the draft has
phrased something more strongly than your evidence supports, it stops and asks you:

> Your profile says you contributed to the supplier migration. This draft says you led it.
> Which is right? If you led it, I will update your profile too.

This cannot be skipped. It is the single most valuable thing the tool does, because the worst
possible failure is a confident claim on your CV that collapses when someone asks about it. The
check catches the overstatement, keeps you as the author of your own claims, and improves your
profile whenever the stronger version turns out to be true.

Anything specific about the employer, in a cover letter, must come from the advert or from
something you said. It will not invent an admiration for their work that you do not have.

### Edit capture

The generated version is kept. When you edit before sending, that difference is the clearest
information the tool ever gets about where its judgement was wrong: which achievement it should
have picked, how you actually phrase things, what you cut. It arrives in minutes rather than
weeks, and unlike a rejection it is not confounded by anything.

---

## 5. Interview preparation

`/prep-interview` knows something no general-purpose assistant does: exactly which document the
interviewer is holding, because it wrote it.

So it does not start with common interview questions. It starts with the claims on your CV that
are most likely to be probed, ranked by how thin the evidence behind them is. That list already
exists, because the claim check produced it.

Then it asks what kind of interview it is, because that changes everything and varies enormously
by field: competency and STAR, technical, panel, presentation, case study. Then it runs a real
mock, where you answer and it pushes back for specifics, rather than handing you model answers
to read.

You get a one-page cheat sheet: your stories mapped to the competencies likely to come up, your
honest gap and what you will say about it, and questions worth asking them.

The transcript is kept. Rereading your own first fumbled answer is useful, and when you produce
a much better articulation of an achievement under pressure, that goes back into your profile.

---

## 6. Outcomes, and what the tool can honestly learn

`/log-outcome` records what happened. If you were interviewed, it also asks which questions
actually came up, while you still remember, because that is dense uncorrupted information that
makes every future preparation session better.

Then it writes observations in plain language into `my/learnings.md`. Things like:

> Every role that has reached interview mentioned stakeholder management in the first three
> lines of the advert. The two that went quiet did not.

You can read every observation, correct it, or delete it. `/find-jobs` and `/apply` read them
and adjust.

### What it will not do

It will not claim to have learned a statistical model of your job search, because it cannot. A
serious search produces perhaps forty applications, most of which end in silence, and silence
tells you almost nothing: the role may have been filled internally before you applied. Nobody
can fit weights to that, and a tool that pretends otherwise is lying to you.

What it can do is notice patterns and show them to you, which is genuinely useful and honestly
described.

Relatedly, when it shows you a ratio it will tell you the base rate. A five to ten percent
response rate is ordinary in a competitive market. Reporting "two responses from twenty two"
without that context is accurate and misleading at the same time.

---

## Changing any of this

Every step above is defined in a Markdown file in `.claude/skills/`. They are meant to be read
and changed. See [customising.md](customising.md).
