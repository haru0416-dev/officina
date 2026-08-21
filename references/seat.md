# Seat

A seat is the friction you already sit beside. It is not a platform
you wish you owned.

Vercel can invert function timeouts because they run the functions.
Cloudflare can invert egress because they run the network. You can
still mint primitives without that. You cannot mint them by pretending.

## What a seat is

A seat has three parts:

1. A repeating job you actually do (or that your users already hand
   you).
2. A cost, failure, or default that shows up in that job.
3. A lever you can pull without a hypothetical global fabric.

Examples that count:

- You write coding-agent skills, so you sit beside claim/evidence
  drift, context rot, and premature solutioning.
- You wrap MCP servers, so you sit beside huge tool results.
- You debug solver output, so you sit beside single-formulation trust.
- You ship a closed dialogue engine, so you sit beside "this had to be
  an LLM" as a default.

Examples that do not count:

- "Once we have a CDN..."
- "If we were AWS..."
- "After we raise, we build a gateway..."
- Any sentence that starts with a platform you do not operate.

## Personal Labs vs corporate Labs

Corporate Labs mint primitives that monetize the platform. Personal
Labs mint primitives that monetize *or* spread from the seat you
already have.

Valid personal OSS wedges:

- A file format, CLI, or protocol that becomes the public interface.
- A local runtime whose hosted plane can come later, or never.
- A skill or library that collapses a SaaS category for one developer
  first.

Invalid personal wedges:

- "We will be the Cloudflare of X."
- A primitive whose only implementation path is someone else's
  control plane.

## How to write the Seat section

One short paragraph. Name the job, the repeating pain, and the lever.
Do not name a vision.

```txt
Seat: coding-agent sessions that already emit tool results, patches,
and summaries. The lever is the assembler of those sessions (hooks,
MCP, skills), not a new model vendor.
```

If two seats are honest, pick the one that makes the five-line API
smaller. Split catalogs rather than blending seats.

## Fake-seat test

Delete every sentence that mentions infrastructure you do not run.
If the card still has an inversion and an API, the seat was real.
If the card vanishes, it was a wish. Kill it.
