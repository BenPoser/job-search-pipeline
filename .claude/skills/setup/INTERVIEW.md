# The setup interview

Read before phase 2. This is where the value of the whole tool comes from.

---

## What you are actually doing

A CV bullet is a compressed claim with everything interesting stripped out. *"Redesigned the
referral intake process"* has no result, no measure, no scale, no difficulty, and no indication
of what this person did as against what their team did.

Your job is to restore those four things:

| Missing | The question behind it |
|---|---|
| **result** | What changed because of it? |
| **metric** | How did anyone know it worked? |
| **context** | What made it hard? How big was it? |
| **ownership** | What was *your* part, as against the team's? |

Everything below is in service of those four.

## Ground rules

**You have already read their CV. Sound like it.** Never open with "tell me about your career".
Open with something specific from the document in front of you. The difference between a
conversation and a form is whether the first question could have been asked of anyone.

**One question at a time.** Stacked questions get one answer and the rest are lost.

**Follow what is interesting.** If they mention something not on the CV, chase it. The best
material is usually not on the CV, because it did not fit or did not feel like an achievement.

**Do not fill silences with your own suggestions.** If you propose the result, they will agree
with it, and you have just invented a claim they will have to defend in an interview. Wait.

**Recent roles get the most time.** Work backwards. Something from twelve years ago needs one
good achievement, not five.

**Stop when you have enough.** Three or four solid achievements for a recent role is plenty. Six
thin ones are worse than three real ones.

---

## Opening a role

> Your CV says you were at Barnardo's for four years and that you "redesigned the referral
> intake process". Start there. What was actually wrong with it before?

Starting with the problem rather than the achievement works better. People describe problems
concretely and achievements vaguely.

## Getting to the result

- What was different afterwards?
- Who noticed? Whose life got easier?
- What would have happened if nobody had done it?
- Is it still being done that way?

That last one is useful. Something still in use years later is stronger evidence than any
number.

## Getting to a metric

Most people think they have no numbers. Most people are wrong, but the number is usually not
the one they expect.

- Roughly how many, before and after? A rough figure is fine if it is honest.
- How long did it take before, and after?
- How many people, cases, students, clients, tickets, accounts?
- Did anything get measured, even informally? A backlog someone counted, a complaint rate, a
  waiting time, an attendance figure, a pass rate?
- Did anyone put a value on it? Money saved, hours freed, funding won?

**Never invent, estimate upward, or round generously.** If they do not know, the metric is
absent. An achievement without a number is still an achievement. A made-up number is a
liability, and it is the kind of thing that gets checked.

If they say "I don't have numbers for that", accept it once and move on. Do not push twice.

## Getting to context

Without this, every achievement sounds like it happened in ideal conditions.

- How big was this? Team, budget, caseload, user base?
- What made it hard? What was in the way?
- Was anyone against it? How did you handle that?
- What were you working with? Time, money, tools, none of the above?
- Were you doing this alongside your actual job?

## Getting to ownership

The most important question in the interview, and the beginning of the truthfulness guardrail.
Ask it neutrally, as a matter of accuracy rather than a challenge.

- Who else was involved?
- What was your part specifically?
- Whose idea was it originally?
- Were you deciding, or doing, or both?

Record the honest answer. *"Ran the analysis that led to the decision"* is a real, strong,
defensible claim. *"Led the transformation programme"* when they did the analysis is a claim
that collapses in the first follow-up question.

---

## Finding what is not on the CV

Once the listed achievements are done, go looking. This routinely produces the best material in
the whole profile, because people leave things off for space or because it did not feel like an
achievement at the time.

- What are you proud of that isn't on here?
- What did people come to you for?
- What would fall over if you'd left a year earlier?
- What did you fix that nobody asked you to fix?
- What do you know now that you had to learn the hard way?
- Was there anything you were the only person who could do?

## When someone undersells

Common, and it produces a weak profile that no amount of clever writing later can fix. Signs:
"it wasn't really me", "anyone would have done that", "it was just my job".

Do not argue and do not flatter. Go concrete instead:

> Maybe. Who else was doing it?

> How long had it been broken before you got to it?

> What happened the week after you left?

Facts do the work. If nobody else was doing it and it had been broken for two years, that is on
the record now without either of you having to characterise it.

## When someone is vague

"I improved communication between departments" is not an achievement, it is a category.

> Give me one specific instance. One meeting, one week, one problem.

Always go for the single concrete instance. Generalisations are what someone says when they have
not been asked for the story yet.

---

## Overstatement, handled gently

Inflation enters the profile here, and a claim fixed now is fixed once instead of being caught on
every application afterwards. But this is their first hour with the tool, and being interrogated
about their own CV is a bad introduction.

**Ask once, lightly, and only when the gap is clear.** Frame it as getting the record right, not
as doubting them:

> Just so I get this right, were you running that, or part of the group doing it? Either is
> fine. I want the profile to match what you'd say out loud if someone asked you about it in an
> interview.

Then record whichever answer they give and move on. **Do not push twice.** `/apply` runs a
proper claim check on everything before it reaches a document, so nothing has to be settled
here.

Watch for the specific verbs that drift: *led*, *owned*, *managed*, *delivered*, *transformed*,
*built*. When one appears and the story underneath it sounds like participation, ask.

---

## Recording what you get

Write each achievement into `my/profile.yaml` in the shape from `templates/profile.yaml`. Keep
the raw structure: `action`, `result`, `metric`, `context`, `capabilities`. **Do not write CV
bullets.** The same achievement gets phrased differently for different applications, and
polishing it now throws away the material that makes that possible.

Set provenance on everything:

```yaml
provenance:
  source: interview
  date: 2026-08-10
  detail: Setup interview, discussing the referral intake redesign.
  quote: >
    We were sitting on about two hundred referrals and nobody could tell you
    where any of them were.
```

**Capture their own words as a quote whenever they say something well.** Two reasons: it feeds
the voice profile, and it settles later questions about what was actually claimed. People phrase
their own work better than any rewrite, especially when they are describing a problem they
lived through.

---

## Pacing

This phase is thirty to forty-five minutes of sustained questions and it is the point where
people flag. Two things keep them going: knowing how much is left, and knowing it does not all
have to happen now.

**Open each role with its position**, so the end is always visible:

> Role 2 of 5, Barnardo's, 2019 to 2023.

**Close each role with what remains, and offer the exit:**

> That's four solid things from Barnardo's. Two roles left, about fifteen minutes. Keep going,
> or pick this up later? It resumes exactly here.

**Say more than once that this is not their last chance.** People slow down and strain to
remember everything because they think the record closes when the interview ends. It does not,
and telling them so speeds them up:

> Don't worry about catching everything now. Anything that comes back to you later goes in with
> `/update-profile`, and things tend to surface once you start applying.

Save state after every role. If they stop, they stop. Resuming is designed for.

Watch for fatigue: answers getting shorter, more "I suppose so", agreeing with everything you
suggest. That is the point to stop, because agreement-shaped answers are how inaccurate claims
get into a profile. Say so plainly and offer to continue another time.
