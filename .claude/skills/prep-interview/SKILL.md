---
name: prep-interview
description: Prepare for a specific interview - audit the claims most likely to be probed, run a mock interview, and produce a one-page cheat sheet. Use when the user runs /prep-interview, has an interview coming up, or asks how to prepare for one.
---

# /prep-interview

Prepare for one specific interview, grounded in what was actually claimed.

---

## The thing only this tool can do

You know exactly which document the interviewer is holding, because you wrote it. You know which
achievements were selected, how they were phrased, and which claims are thinnest, because
`/apply` produced `weak-claims.md`.

So do not open with common interview questions. Anyone can get those anywhere, and leading with
them wastes the one advantage this has.

Open with their own CV, and what will get probed:

> Three things on this CV will get pushed on. The strongest is the AI adoption work, which is
> exactly what they lead the advert with. The riskiest is "named production incident responder":
> that traces to your old CV and nothing else, and at setup you had no specific incident to hand.
> They are running a security-led role, so it is the first line they will pick up. Let us build a
> real answer for it before anything else.

## 1. Read

- `my/applications/{slug}/` — the CV as sent, the cover letter, and `weak-claims.md`
- The job file, for the advert and the recorded gaps
- `my/profile.yaml` — the evidence behind everything
- `my/learnings.md` — including questions actually asked at previous interviews

If `weak-claims.md` is missing because the application predates it, do the claim audit yourself
from the CV against the profile.

## 2. Ask what kind of interview it is

This changes everything and varies enormously by field. Do not assume.

Competency or behavioural, technical, panel, presentation, case study, values-based, or an
informal first conversation. Also ask who is in the room if they know, because a hiring manager,
a future peer and an HR screener want different things from the same answer.

If they do not know, say what is most likely for that kind of employer, prepare for that, and
name the assumption.

## 3. The claim audit

Work through the weak claims, hardest first. For each: what will be asked, what the honest answer
is, and what evidence supports it.

Where the honest answer is "I do not have a strong example", say so, and decide together whether
to drop the claim in the interview or hold a smaller true version of it. Better now than live.

## 4. The gaps

Every application has at least one. It is in the job file under `suitability.gaps`, and the
interviewer has already seen it.

Build a straight answer: name it, say what is adjacent, say what they are doing about it if
anything, then stop. The failure mode is over-explaining, which reads as defensive.

## 5. Run the mock

Properly. The user answers, you push back, they answer again. Do not hand over model answers to
memorise: an answer that came out of their own mouth survives a follow-up question, and a
memorised one does not.

**How to push back:**

- Ask for the specific instance when they generalise
- Ask what *they* did when they say "we"
- Ask for the number, or for how they knew it worked
- Ask the obvious follow-up, especially "what would you do differently?"
- Interrupt once or twice if answers run long, the way a real panel does

**Cover, at minimum:**

- Why this role, why this organisation. Generic answers here are the most common failure, and for
  an agency listing with an unnamed client the honest version is about the work, not the employer.
- Their strongest relevant story, told in about two minutes
- The gap
- A failure, or something that went wrong, which almost every interview asks for in some form
- Questions to ask the panel

**Keep it to a sensible length.** Five or six questions answered well beats twenty rushed. Offer
to stop and continue later.

## 6. Write the cheat sheet

One page, to `my/applications/{slug}/interview-prep.md`:

- Three or four stories mapped to the competencies likely to come up, each in a line or two so
  they can be scanned rather than read
- The gap, and the prepared answer
- The weak claims, and what to say if pushed
- Two or three questions to ask, showing they have understood the work rather than filling a slot
- Anything practical: format, who is in the room, timings

## 7. Save the transcript

Write the full mock to `my/applications/{slug}/interview-transcript.md`.

Rereading a fumbled first answer is useful, and it is more evidence about how the user actually
talks, which feeds the voice profile.

## 8. Write back to the profile

People routinely produce their best articulation of an achievement under pressure, better than
anything they said at setup. When that happens, update the achievement in `my/profile.yaml` with
provenance `interview` and today's date, and tell the user you have done it.

This means `/prep-interview` changes the profile. That is deliberate: the best material should
not be trapped in a transcript.

If a mock answer resolves something on the weak-claims list, update that too, so the claim stops
being flagged on future applications.

## 9. Close

Remind them to run `/log-outcome` afterwards **while the questions are still fresh**. What was
actually asked is the most useful thing they can bring back, and it is gone within a day.
