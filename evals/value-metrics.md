# Value Metrics

Use this file to test whether Officina creates practical value.

The goal is not to show that the catalog "sounds more original." The goal
is to measure whether the skill suppresses generic ideation and leaves a
primitive someone could actually strike.

## Evaluation Conditions

Run the same task under at least three conditions:

```txt
baseline: normal agent answer
terse: normal agent answer with a concise-output instruction
officina: answer using this Skill
```

The key comparison is not only officina vs baseline. It is also officina
vs terse, because shortening can look disciplined while still emitting
X-for-Y.

## Primary Value Metrics

Score each 0-2 unless otherwise noted.

| Metric | What it tests | How to score |
|---|---|---|
| Generic-solution suppression | Skill kills mashups, X-for-Y, AI-powered X | 0 list of products, 1 mixed, 2 kills labeled and none promoted |
| Primitive sharpness | Named primitive with a five-line API | 0 pitch, 1 name without API, 2 typed-in API |
| Inevitability | After seeing it, a current habit looks wrong | 0 "cool idea", 1 plausible, 2 hard to unsee |
| Kill-probe | A result that would destroy the card | 0 absent, 1 vanity metric, 2 falsifying signal |
| OSS-wedge honesty | Public interface vs later product, no fake platform | 0 "we are Cloudflare", 1 vague open core, 2 concrete split |
| Seat honesty | Real friction vs borrowed infrastructure | 0 fake seat, 1 fuzzy, 2 job + lever |
| Prior-art honesty | Claimed list and search stop rewraps | 0 none, 1 name-drops, 2 known primitives halted |
| Human approval readiness | Reviewer can pick one experiment | 0 no, 1 needs a rewrite, 2 one or two cards to try |

Maximum score: 16.

Passing bar:

- `officina` should score at least 12/16.
- `officina` should beat `baseline` by at least 4 points.
- `officina` should beat `terse` by at least 3 points on generic-solution
  suppression plus primitive sharpness.

## Secondary Metrics

Track these when using the skill in real work:

- Mashup count: X-for-Y or trend-combo cards that survived.
- Claimed rewraps: cards that were coffer/quaere/munou/dubito in a coat.
- Experiment start rate: catalogs that produced a repo or spike within
  one sitting.
- Kill rate: killed cards / total cards. Zero kills is a failure signal.
- API length: lines in the surviving five-line API. If it needs a README to be usable, it was a product, not a primitive.

## Value Decision

Officina has initial evidence of value for a target segment if:

- It wins human approval in at least 70% of "give me original ideas"
  tasks against baseline.
- It reduces promoted mashups/X-for-Y by at least 80% relative to
  baseline.
- Survivors have a five-line API in at least 80% of catalogs.
- It preserves a visible kill in at least 90% of substantial catalogs.
- It does not rewrap a claimed primitive in at least 90% of catalogs.

## Failure Signals

If these happen, the value claim is weak:

- Users prefer baseline because Officina feels ceremonial.
- The skill writes long canon and still emits mashups.
- Reviewers cannot tell a primitive from a startup pitch.
- Every catalog promotes "memory", "workflow", or "observability".
- The author of this package keeps rediscovering coffer.
- Kill-probes are never run.

## Evidence Template

```md
Task set:
Number of prompts:
Target segment:

Baseline average:
Terse average:
Officina average:

Human approval win rate:
Mashup reduction:
Five-line API rate:
Kill visibility:

Strongest evidence of value:
Weakest evidence:
Decision:
```
