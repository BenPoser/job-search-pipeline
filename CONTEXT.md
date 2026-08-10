# Domain Glossary

The shared vocabulary of this project. Terms are defined here and used consistently everywhere
else: in commands, documents, and conversation with the user.

This file is a glossary and nothing else. No implementation details, no decisions, no plans.
Decisions live in [docs/adr/](docs/adr/).

---

## Command

One of the eight things a user can invoke: `/setup`, `/status`, `/find-jobs`, `/review-jobs`,
`/apply`, `/prep-interview`, `/log-outcome`, `/update-profile`.

The word **skill** is deliberately never used for these, because "skills" already means
something on a CV and the collision is confusing. Commands are commands; skills are the
competencies a person has.

## Profile

A person's complete structured career record. Contains their Roles, and personal details such as
contact information and location. The Profile is the source of truth from which every generated
document is built.

A Profile grows over time. It is never complete.

## Role

One position a person has held: an employment, a period of study, a volunteer post, a freelance
engagement. Has a title, an organisation, a date range, and a set of Achievements.

## Achievement

Something the person did, recorded in a structured form rather than as a finished CV bullet:

- **action**: what they did
- **result**: what changed because of it
- **metric**: the quantified measure, where one exists
- **context**: the situation, scale, or constraint that makes it meaningful
- **capabilities**: what it demonstrates they can do
- **tags**: terms from the person's own Taxonomy
- **provenance**: where this came from

An Achievement is raw material. It is not written in CV language, because the same Achievement
is phrased differently for different applications.

## Capabilities

What an Achievement demonstrates the person can do. Field-neutral by design: a nurse, a teacher
and an engineer all have capabilities, whereas only one of them has a tech stack.

## Taxonomy

The set of tags used to classify a person's Achievements, generated for that person during
setup from their own CV and interview. An engineer's Taxonomy and a teacher's Taxonomy share no
terms. The Taxonomy is what makes Achievement selection repeatable rather than improvised.

## Provenance

The record of where a fact came from: `cv`, `linkedin`, `interview`, or `manual`, along with
enough detail to answer the question "where did this come from?" in a useful way.

Provenance is load-bearing, not metadata. Nothing reaches a generated document without it.

## Narrative

A themed grouping of Achievements with a headline claim and a ranked shortlist, used to select
material quickly when a Profile has grown too large to consider whole.

Narratives do not exist in a new Profile. They are generated later, once there is enough
material to be worth organising.

## Voice Profile

A description of how a person writes, derived from writing samples they provide and then edited
by them. Has separate sections for CV bullets, cover letters, and application answers, because
the same person's register differs across the three.

The Voice Profile expresses personal taste. It is distinct from Quality Rules.

## Quality Rules

Craft standards that apply to everyone's documents regardless of taste: no unexplained
acronyms, active voice, no inflated descriptions of a role, and the requirement that a stranger
reading the document can understand every line.

Quality Rules ship with the tool and are the same for every user. Where a Voice Profile
conflicts with a Quality Rule, the Quality Rule wins.

## Job

A specific advertised role that has entered the pipeline, whether found by searching a Job
Source or pasted in by hand. Identified by its Source and Source ID together.

## Job Source

Where a Job came from. Either a job board that can be queried (`adzuna`, `reed`) or `manual`,
meaning the user supplied the link or the text themselves.

`manual` is a fully supported permanent mode. A user who never configures a job board API can
use every part of this tool.

## Suitability

An assessment of fit between a Job and a Profile:

- **score** (1 to 10)
- **fit type** (see below)
- **rationale**: why, naming specific strengths and the most important gap

Suitability is honest rather than encouraging. A low score with a clear reason saves more time
than a generous one.

## Fit Type

How far a Job sits from what the person currently does. Defined relative to *their* Profile, not
to any fixed industry:

| Type | Meaning |
|---|---|
| `core` | The job they already do |
| `adjacent` | A step up, or a sideways move into neighbouring work |
| `pivot` | A change of field |

Fit Type drives both which searches surface a Job and how a CV is framed for it.

## Search Cluster

A named group of search terms targeting one career direction, each mapping to a Fit Type of the
same name. Built primarily from example job adverts the user pastes in, rather than from
keywords they invent.

## Status

Where a Job has got to:

| Status | Meaning |
|---|---|
| `new` | Found, not yet reviewed |
| `dismissed` | Reviewed, not applying |
| `shortlisted` | Intending to apply |
| `applied` | Application sent |
| `interviewing` | Process underway |
| `closed` | Offer, withdrawal, rejection, or gone quiet |

## Application

Everything produced for one Job: the tailored CV in both formats, the cover letter, any
application answers, the interview preparation, and the Sent Version. One Application belongs to
exactly one Job.

## Sent Version

The version of a document the user actually sent, as distinct from the version that was
generated. The difference between the two is the clearest signal available about where the
tool's judgement was wrong, and it arrives within minutes rather than weeks.

## Outcome

What happened after applying: `interview`, `rejection`, `silence`, or `offer`, with a date.
Where an interview took place, the Outcome also records which questions were actually asked.

## Observation

A plain-language statement about a pattern in the search, written into `my/learnings.md` and
readable, editable, and deletable by the user.

Observations are noticed, not calculated. There is never enough data in a single job search for
anything statistical, and the tool says so rather than inventing precision.
