# Officina Evaluation Rubric

Use this rubric when reviewing an Officina catalog or comparing baseline
vs skill-assisted answers.

## Evaluation Setup

Run at least two conditions:

```txt
baseline: answer the task normally without Officina
officina: answer using this Skill
```

A third condition is required when the user asked for "ideas":

```txt
terse: normal agent answer with a concise-output instruction
```

The skill should not win by being longer. It should win by killing mashups
and leaving a primitive with an API.

## Hard Failures

Any hard failure means the output should be revised before scoring:

- A product idea appears before a seat and a constraint inversion.
- Friction is a vibe, a trend, or "people want X".
- No category is named, or the category is "a useful tool".
- The five-line API is a slide, a dashboard, or a copilot pitch.
- An X-for-Y, mashup, AI-powered X, or mutation-only card is promoted.
- A claimed primitive from `references/claimed.md` is rewrapped as new.
- Novelty uses marketing adjectives instead of the four labels.
- No card is killed, so the filter cannot be inspected.
- The kill-probe can only confirm the idea.
- More than eight live cards.
- Output would fit many unrelated "give me ideas" prompts unchanged.

## Scorecard

Score each item 0-2.

```txt
0 = missing or wrong
1 = present but generic, weak, or partially unsupported
2 = specific, seat-grounded, and useful
```

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Seat honesty | fake platform | named but vague | job + lever, no borrowed CDN |
| Friction evidence | vibe | anecdote | observed cost or failure |
| Constraint inversion | extra feature | cheaper version of X | expensive thing becomes default |
| Category collapse | no category | fuzzy market | one named product class becomes an API |
| Primitive sharpness | pitch deck | named, mushy API | five lines a developer could type |
| Inevitability | "interesting" | plausible | a current habit looks embarrassing |
| Genericness suppression | mashups promoted | some kills | kills are labeled and the survivors passed |
| Prior-art honesty | none | name-drops | claimed list + search, known primitives stopped |
| OSS wedge | "we will be a platform" | vague open core | public interface vs later product |
| Kill-probe | confirmation test | weak metric | a result that would destroy the card |
| Novelty discipline | self-rated novel | mixed language | only the four labels |
| Catalog hygiene | volume list | too many live cards | few cards, at least one kill |

Maximum score: 24.

Passing bar:

- No hard failures.
- At least 19/24 for substantial catalogs.
- At least 14/18 in Minimal Mode, excluding inapplicable rows.

## Comparative Questions

Ask these after scoring:

- Did Officina refuse the baseline's X-for-Y or mashup list?
- Did a surviving card have a shorter API than the baseline's product?
- Did it name a category that should die, not a customer to sell to?
- Did it admit a known primitive instead of relabeling it?
- Did it sit in a real seat, or borrow Vercel/Cloudflare's?
- Would the kill-probe actually be run, or is it decorative?

## Fixture Use

Use prompts in `evals/fixtures/` as regression cases:

- `generic-vs-primitive.md`: ordinary idea-tool request.
- `x-for-y.md`: explicit mashup bait.
- `known-platform.md`: request that should die as a known primitive.

For each fixture, compare baseline vs Officina and write:

```md
Baseline failure:
Officina improvement:
Remaining weakness:
Score:
Decision:
```
