---
name: officina
description: "Use when the user wants original product ideas, Labs-style OSS, Vercel/Cloudflare-like primitives, or what to build next with visible future potential. Extracts a named primitive via seat, friction, constraint inversion, and category collapse. Do not use for ordinary brainstorming, word mashups, X-for-Y, or mutation-style ideation."
---

# Officina

Officina is a process-correction skill for minting Labs-grade primitives.

It is not an idea generator. It stops generic product lists, word mashups,
and mutation theatre from being promoted as original work.

The name is Latin *officina*: a workshop. The bench is for striking a
primitive, not for brainstorming.

## Core Rule

Never promote an idea. Promote a primitive, or kill the card.

A primitive has a seat, a constraint it inverts, a category it collapses,
a name, a five-line API, and a kill-probe. Anything else is a feature, a
mashup, or a wishlist.

Core flow:

```txt
Seat
-> Recurring Friction
-> Constraint Inversion
-> Category Collapse
-> Named Primitive
-> Inevitability Test
-> Genericness Kill-Gate
-> Prior-Art Scan
-> OSS Wedge
-> Kill-Probe
-> Labs Card
```

If this is too heavy, use Minimal Mode. Do not skip seat, inversion,
collapse, five-line API, kill-gate, or kill-probe.

## Use When

Use this skill when one or more are true:

- The user asks for original ideas, Labs-style OSS, what to build next, or
  future-facing product direction.
- The user names Vercel Labs, Cloudflare, platform primitives, or "the
  thing I actually wanted to build."
- Ordinary ideation would produce X-for-Y, trend mashups, or generic SaaS.
- The work is choosing a primitive to experiment on, not implementing a
  chosen design.

Do not use this skill when:

- The task is a factual lookup, rewrite, or already-chosen implementation.
- The user wants mutation-style alternatives to a known approach; that is
  a different ideation skill, not this one.
- The problem is a bug whose cause is unknown; do not invent a product
  around an unproven cause.

## Reference Loading

Keep ordinary use lightweight. Load extra files only when needed:

- `references/labs-canon.md`: how Durable Objects, R2, AI SDK, Fluid, and
  Workflow dissect into seat / inversion / collapse / five-line API.
- `references/anti-patterns.md`: genericness kill-gate, mashups, X-for-Y.
- `references/claimed.md`: primitives already struck in this author's
  line of work; do not rewrap them.
- `references/seat.md`: how to name a seat without owning a CDN.
- `evals/rubric.md`: rigorous review of an Officina output.
- `evals/value-metrics.md`: value comparison against baseline and terse.
- `examples/showcase.md`: first catalog produced with this Skill.
- `evals/fixtures/`: generic-vs-primitive regression prompts.

## Operating Discipline

1. Name the seat before naming any product.
2. Demand evidence for friction. Vibes are not friction.
3. Invert a cost, failure, or default. Do not add a feature.
4. Name one product category that should become ten lines of code.
5. Write the five-line API before the pitch paragraph.
6. Run the inevitability test: after seeing it, can you unsee it?
7. Kill X-for-Y, mashups, AI-powered X, dashboards, and mutation-only cards.
8. Search prior art, including `references/claimed.md`. If it exists, label
   `known primitive` and stop promoting it.
9. Write the OSS wedge: what is public, what could later be a product.
10. Design a probe that can kill the card, not one that can confirm it.
11. Emit Labs cards, not a brainstorm list. Volume is a defect.
12. Use only the novelty labels: `known primitive`, `category collapse`,
    `recombination`, `incoherent`. Never self-rate originality.

## Output Contract

For substantial tasks, return this structure. Multiple live cards are
allowed only when each survives the kill-gate. Include at least one
killed card so the filter is visible.

```md
# Officina Catalog

## Seat
Where this author sits. No fake platform.

## Friction
Observed, evidenced. No inferred market.

## Constraint inversion
What is expensive, slow, or default-broken today, and what becomes the
new default.

## Cards

### C-001 <name>
Status: spark | experiment | promote | kill
Novelty: known primitive | category collapse | recombination | incoherent

Category collapse: <one named category>
One-liner: <one sentence>
Five-line API: <five lines or fewer, in a txt block>
Mental model: <one short metaphor, Durable-Object short>
Inevitability: <why this is hard to unsee, or why it fails>
Genericness gate: pass | kill (<reason>)
Prior art: <what was searched; claimed hits first>
OSS wedge: <public interface vs later product>
Kill-probe: probe / kill signal / cost
```

End with residual risk: what evidence would change the catalog.

## Quality Gate

Check each item before final output. If any check fails, stop and revise:

- A product idea appeared before a seat and an inversion.
- Friction is a vibe, a trend, or an underspecified "people want X".
- No category is named, or the category is "a useful tool".
- The API is a slide, not five lines a developer could type.
- Inevitability is "this is interesting" rather than "this should exist".
- An X-for-Y, mashup, AI-powered X, dashboard, or mutation-only card was
  promoted.
- A claimed primitive from `references/claimed.md` was rewrapped.
- Novelty uses marketing adjectives instead of the four labels.
- No card is killed, and the filter cannot be inspected.
- The kill-probe can only confirm the idea, not destroy it.
- More than eight live cards. Cut to the ones with APIs.

## Minimal Mode

If the user needs a concise answer, keep one card compact:

```md
Seat:
Friction:
Inversion:
Collapse:
Primitive:
API:
Inevitability:
Prior art:
OSS wedge:
Kill-probe:
Status:
Novelty:
```

Even in Minimal Mode, do not skip seat, inversion, collapse, API,
kill-gate, or kill-probe.
