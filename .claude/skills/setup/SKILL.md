---
name: setup
description: One-time setup for the job search pipeline. Builds the user's career profile from their CV and an interview, derives their writing voice, and configures job search settings. Use when the user runs /setup, is starting out, or needs to resume an unfinished setup.
---

# /setup

Build the user's profile, voice, and search settings. Runs once, resumably, in eight phases.

Read [INTERVIEW.md](INTERVIEW.md) before phase 2. Read [API-KEYS.md](API-KEYS.md) only if the
user wants job board keys in phase 6.

---

## Before you start

**Check for an existing setup.** Read `my/setup-state.yaml`.

- **Missing** → this is a fresh run. Start at phase 0.
- **Present and incomplete** → resume. Summarise what is done in one or two lines, say what is
  next and roughly how long, and ask if they want to carry on. Do not repeat completed phases.
- **Present and complete** → do not rerun. Say setup is done, ask what they actually want, and
  point them at `/update-profile` for adding experience or `/status` for what to do next.

**Create `my/` and its subfolders** (`my/inbox/`, `my/samples/`, `my/jobs/`,
`my/applications/`) if they do not exist.

---

## How to run this

**Do everything yourself.** The user is not a developer. Never ask them to create a file, edit
YAML, or run a command. If something needs writing, write it.

**Save state after every phase.** People stop halfway. `my/setup-state.yaml`:

```yaml
started: 2026-08-10
last_updated: 2026-08-10
complete: false
phases_done: [0, 1, 2]
notes:
  - "LinkedIn export requested 10 Aug, not yet arrived"
  - "Interview covered roles 1-3 of 5"
```

**This is a conversation, not a form.** Follow interesting answers. Skip what does not apply.
Someone in a field where CV bullets are not the norm should not be walked through questions
built for one where they are.

**Always show where they are.** This is a long process and it feels longer when you cannot see
the end of it. Open every phase with a one-line marker, and close every phase with what is left:

```
Step 3 of 7 — Themes. About 5 minutes.
```

The user-facing numbering runs 1 to 7 and maps to phases 1 to 7. Phase 0 and phase 8 are
orientation and wrap-up; do not number them, they are not work.

> Done. Five roles, nineteen achievements. Three short steps left, about fifteen minutes.

Inside the interview, which is by far the longest phase, mark each role the same way:
"Role 2 of 5". Someone who knows there are three left will keep going. Someone who does not
know assumes it is endless.

**Keep reminding them this is not their only chance.** People slow down because they are trying
to remember everything now. Say, more than once and in your own words, that the profile is meant
to grow and that anything forgotten can be added later with `/update-profile`. It speeds them up
and it is true.

**Offer the stopping point rather than waiting to be asked.** At any natural boundary, if they
have been going a while: "Good place to stop if you want one. `/setup` picks up here."

**Tone**: see `docs/tone.md`. Plain and useful. No cheerleading.

---

## Phase 0 — Orientation

**Show them the whole map before starting.** Knowing what is coming is most of what makes a long
process bearable, and it lets people prepare: someone who knows step 4 wants writing samples can
have one ready.

> Here's the whole thing. About an hour, and you can stop at any point and pick up where you
> left off.
>
> ```
> 1. Your CV and anything else you have      5 min
> 2. The interview, one role at a time      30-45 min   ← the long one
> 3. Themes from your career                 5 min
> 4. How you write                           5 min
> 5. What you're looking for                10 min
> 6. Job board accounts (optional)          10 min
> 7. Backing up your profile                 2 min
> ```
>
> Step 2 is most of it. The rest is quick.

Say plainly that nothing here is one-shot: the profile is designed to grow, and anything they
forget can be added later.

Then ask two things:

1. What kind of work do they do?
2. What kind of move are they making: more of the same, a step up, or a change of field?

The answer shapes the interview, the taxonomy, and the search clusters. A career changer needs
different questions from someone going for the next rung.

Write `my/setup-state.yaml`.

## Phase 1 — Documents  ·  announce as "Step 1 of 7, about 5 minutes"

Ask for their current CV. They can drag it into the chat or drop it in `my/inbox/`. PDF or DOCX
both fine. Read it.

Then offer these, without pressure, in this order:

1. **LinkedIn.** Ask for the URL and try fetching it. Public profiles sometimes work; often you
   get an authentication wall. If it fails, say so plainly and ask for screenshots instead,
   which is the reliable path. This is normal, not a failure.
2. **A LinkedIn data export**, only if they want to go deep. Settings → Data Privacy → Get a copy
   of your data. It takes up to 24 hours. **Never block on this.** Note it in the state file and
   carry on; a later session can read it whenever it lands.
3. **Anything else** useful: an old application, a performance review, a job description they
   once wrote.

Extract roles, dates, education, and any achievement-shaped statements. Write
`my/profile.yaml` using `templates/profile.yaml` as the shape. Set provenance `cv` or
`linkedin` on everything, with today's date.

Then tell them what you have, honestly:

> That gives me five roles going back to 2014, and about twelve things you did. Most are
> one-line claims with no detail, which is what a CV is. That's what the next part is for.

## Phase 2 — The interview  ·  announce as "Step 2 of 7, 30 to 45 minutes"

**Read [INTERVIEW.md](INTERVIEW.md) now.** It has the technique, the question bank, and how to
handle overstatement.

This is the core of setup and where the value is. Budget 30 to 45 minutes. Work role by role,
most recent first, because recent work matters most and energy fades.

Save state after each role, noting which are done.

## Phase 3 — Taxonomy  ·  announce as "Step 3 of 7, about 5 minutes"

Generate this person's taxonomy from the profile you now have: domains, capabilities, and career
stages, in their own field's language.

Do not use a preset list and do not import terms from another field (`docs/adr/0003`). Aim for
roughly 8 to 15 domain and capability terms in total. Too few and selection cannot discriminate;
too many and nothing groups.

Show it to them in plain language, not as YAML:

> From your history, the recurring themes are: service delivery, safeguarding, operations,
> managing volunteers, funding bids. And the things you do repeatedly: process redesign,
> stakeholder negotiation, training people. Anything wrong or missing?

Two or three corrections here improve every later selection. Write it into `my/profile.yaml`.

## Phase 4 — Voice  ·  announce as "Step 4 of 7, about 5 minutes"

Ask for a few things they have written: an email they were pleased with, an old cover letter, a
report, anything. Two or three is plenty. Say clearly it is optional.

Save what they give you in `my/samples/`.

Derive an explicit style guide using `templates/voice.md` as the shape, and **show them what you
concluded**:

> You write short sentences. You almost never hedge, no "I believe" or "I feel". You prefer
> concrete nouns over abstractions. British spelling, no serial comma. Does that sound like you?

If they give you nothing, write a minimal voice profile from how they have talked during the
interview, and tell them that is what you did.

Explain what the file is for: it is theirs, and it is what to change when a generated document
does not sound like them.

## Phase 5 — Search settings  ·  announce as "Step 5 of 7, about 10 minutes"

**Lead with example adverts.** Ask for two or three real job adverts they would genuinely apply
for. A link or pasted text. This is much easier than inventing keywords and produces better
settings: real titles, real salary bands, and the start of the scoring criteria.

If they have none to hand, ask them to describe one role they would take tomorrow, and work from
that.

Derive `my/search-config.yaml` using `templates/search-config.yaml` as the shape. Fill only the
clusters that apply and mark the rest inactive. Someone not considering a change of field does
not need a pivot cluster.

Also ask, and set:

- **Country.** Check it against Adzuna's supported list. If unsupported, say so plainly and
  configure manual-only. Do not let them discover it later as an empty result set.
- **Location and commute**, or remote preference.
- **Salary floor**, framed as "below this, do not even show me".
- **Which job boards they already use**, including ones with no API. Record in `manual_boards`
  so `/find-jobs` can remind them to check and paste anything worth having.
- **Page target**, with the convention explained: two pages for UK industry, one for a US
  résumé, more for academic.

## Phase 6 — Job board keys  ·  announce as "Step 6 of 7, about 10 minutes, and optional"

Frame it honestly and briefly: about ten minutes, free, and it means jobs get found without them
looking. Then say just as clearly that pasting job links in by hand works just as well and plenty
of people never do this.

If they want to, **read [API-KEYS.md](API-KEYS.md)** and walk them through it one screen at a
time. Write the keys to `.claude/settings.local.json` under `env` yourself, and set the matching
`sources` flags in the search config.

If they decline, set `sources.manual: true` only and move on without comment. Do not raise it
again on later runs.

## Phase 7 — Backing up your profile  ·  announce as "Last one, 2 minutes"

Ask explicitly rather than leaving it to the README, because the people who would benefit are
the ones least likely to read that section.

Be accurate about the risk, which is small and entirely within their control. A private
repository does not become public by accident; publishing one is a deliberate change in its
settings. And private does not mean private to them: they can give specific people access
without it being public at all.

> Right now your profile only exists on this computer. I can also keep it in a **private**
> GitHub repository, which gives you a backup and a history of how it grows.
>
> Private means only you can see it, unless you deliberately invite someone. It won't become
> public on its own. The one thing to keep in mind is that this file has your full career
> history, contact details and salary expectations, so it's not one to publish later.
>
> Want me to set that up, or leave it as files on this machine?

**If they choose backup and there is a remote:** check it is private
(`gh repo view --json visibility`). If it is public, do not commit. Explain, and offer to make
it private. If private, remove the `my/*` line from `.gitignore`, commit, and confirm it is done.

**If they choose backup and there is no remote yet:** offer to create a private repository for
them. If they would rather not deal with GitHub now, say that is fine and it can be set up any
time later, then leave the default. This is not a now-or-never decision and should not be
presented as one.

**If they decline:** leave the default and mention once, without labouring it, that the `my/`
folder is worth copying somewhere occasionally.

## Phase 8 — Finish

Mark `complete: true` in the state file.

Show them what now exists, in plain terms: how many roles and achievements, that they have a
voice profile and search settings.

Then give **exactly one next step**, not a menu:

> You're set up. Type `/find-jobs` and paste in a job you're interested in, or let it search for
> you. If you ever lose track, `/status` will tell you where you are.

Finally, set the expectation that matters most:

> Your profile isn't finished, and it isn't meant to be. It gets better as you use this: when
> `/apply` needs a detail it doesn't have it'll ask you, interview prep tends to shake loose
> better versions of your own stories, and `/update-profile` is there whenever you remember
> something.
