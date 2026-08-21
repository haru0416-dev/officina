# Generic vs primitive comparison

Fixture: `evals/fixtures/generic-vs-primitive.md`

Conditions: `baseline`, `terse`, `officina`

The Officina side is the catalog in `examples/showcase.md`. The baseline
and terse sides are reconstructed from the shallow list in that file
plus a shortened variant. This is a small manual scorecard, not a
benchmark. It supports only the claim below.

## Claim

On this fixture, Officina suppresses mashups and leaves two experiment
cards with five-line APIs. Baseline and terse emit product lists. The
gain is auditability of kills and primitive sharpness, not a proof that
staple or seal will work.

## Baseline (reconstructed)

Ten-item list: Notion for agent thoughts, AI-powered memory, Durable
Objects for agents, Uber for GPU, Figma for prompts, Copilot for
architecture, blockchain provenance, better context compressor, agent
that reviews agents, observability timeline.

Hard failures against `evals/rubric.md`:

- No seat.
- X-for-Y and mashups promoted.
- Claimed rewrap ("better context compressor").
- Known primitive (durable execution) relabeled.
- No kill-probe.
- Novelty implied by "original ideas" with no labels.

## Terse

Same list, five items, shorter adjectives. Still X-for-Y. Still no API.

## Officina

See `examples/showcase.md`. Seat named. Two experiment cards (staple,
seal), one spark (signpost), four kills (workflow, X-for-Y, agent-vcr,
MCP caps). Claimed list consulted. Kill-probes on live cards.

## Primary metrics (0-2 each, max 16)

| Metric | baseline | terse | officina |
|---|---:|---:|---:|
| Generic-solution suppression | 0 | 0 | 2 |
| Primitive sharpness | 0 | 0 | 2 |
| Inevitability | 0 | 0 | 2 |
| Kill-probe | 0 | 0 | 2 |
| OSS-wedge honesty | 0 | 0 | 2 |
| Seat honesty | 0 | 0 | 2 |
| Prior-art honesty | 0 | 0 | 2 |
| Human approval readiness | 0 | 1 | 2 |
| Total | 0 | 1 | 16 |

Passing bar from `evals/value-metrics.md`: officina >= 12, beat
baseline by >= 4, beat terse by >= 3 on suppression plus sharpness.

This saved run: 16 vs 0 vs 1. Suppression+sharpness: officina 4, terse
0. The numbers are not surprising. The fixture is designed so that a
mashup list scores zero. Do not read 16/16 as a general capability
claim.

## Remaining weakness

- The scorecard is not blinded. The same author wrote the catalog and
  the grades.
- Live cards may still die their kill-probes. High process score is
  not product-market fit.
- C-003 (signpost) is recombination and may be ceremonial.

## Decision

Keep the package experimental. Use this run as a regression snapshot:
if a future SKILL.md rewrite starts emitting X-for-Y lists on this
fixture, the skill has regressed.
