# Labs Canon

Dissect known Labs and platform primitives into the Officina fields.
The point is not admiration. The point is to copy the *shape*, not the
product.

Each entry is a teaching object. When a candidate cannot be written at
this density, it is not a primitive yet.

## Durable Objects (Cloudflare)

- Seat: a global Anycast network that already routes a request to an
  isolate near the user, plus a storage plane beside that isolate.
- Friction: WebSocket servers, game rooms, and per-user state required a
  sticky process. The usual answer was Redis plus a regional VM.
- Constraint inversion: coordination is no longer a regional database
  hop. Strongly consistent storage is local to a named actor that lives
  at the edge.
- Category collapse: "realtime backend" products, sticky-session app
  servers, and a class of Redis-as-lock patterns.
- Five-line API:

```txt
export class Counter {
  constructor(state) { this.state = state; }
  async fetch() { let n = (await this.state.storage.get("n")) || 0;
    await this.state.storage.put("n", n + 1); return new Response(String(n + 1)); }
}
```

- Mental model: a single-threaded actor with a name and disk, addressable
  from anywhere.
- Inevitability: after you see `idFromName("room-42")`, a fleet of chat
  servers looks like accidental complexity.
- OSS wedge: the programming model and docs are public; the storage and
  routing stay on the network.
- Why this is not a mashup: it does not mix "edge" and "database" as
  words. It inverts the location of consistency.

## R2 (Cloudflare)

- Seat: a CDN that already pays to move bytes, plus customers who were
  paying a second tax to read their own objects back out of S3.
- Friction: S3-compatible storage was cheap to write and expensive to
  leave. Egress was the product.
- Constraint inversion: egress to the internet is zero. The expensive
  thing becomes the default-free thing.
- Category collapse: "S3 but cheaper" startups whose only wedge was a
  discount on bandwidth.
- Five-line API:

```txt
await env.MY_BUCKET.put(key, body);
const obj = await env.MY_BUCKET.get(key);
return new Response(obj.body);
```

- Mental model: object storage whose bill does not punish reads.
- Inevitability: once egress is free, keeping a second origin "for
  storage" is a habit, not an architecture.
- OSS wedge: S3 API compatibility is the public interface; the network
  is the product.

## AI SDK (Vercel)

- Seat: a deploy platform for TypeScript web apps, sitting next to a
  Cambrian explosion of model vendors.
- Friction: each provider shipped a slightly different streaming
  protocol, tool-call encoding, and UI hook. Apps locked to one vendor
  in the first afternoon.
- Constraint inversion: provider choice is a one-line swap, not a
  rewrite. Streaming and tool calls are the default, not an integration
  project.
- Category collapse: per-vendor SDKs as the thing an app is written
  against; a class of "AI backend" glue services.
- Five-line API:

```txt
import { generateText, openai } from "ai";
const { text } = await generateText({
  model: openai("gpt-4.1"),
  prompt: "Say hello",
});
```

- Mental model: `fetch` for generation.
- Inevitability: writing `openai.chat.completions.create` in application
  code starts to look like writing `mysql.query` in a React component.
- OSS wedge: the SDK is the public primitive; Gateway, Fluid, and
  Sandbox are the paid plane.

## Fluid compute (Vercel)

- Seat: functions that were billed for wall-clock time, now running
  token-slow agent workloads.
- Friction: a request that waits on a model still occupied a full
  instance. People moved agents off the platform to save money.
- Constraint inversion: you pay for active CPU, not for waiting. Long
  idle-in-request work becomes cheap enough to keep in-function.
- Category collapse: "always-on agent server" as the default shape for
  anything that calls a model.
- Five-line API: no new userland API. The primitive is a billing and
  scheduler change that makes existing functions fit the workload.
- Mental model: serverless that does not charge you for thinking time.
- Inevitability: after active-CPU pricing, keeping a process warm "for
  the agent" is an old invoice, not a design.
- Note: some primitives invert a bill, not a function signature. Still
  require a mental model and a collapsed category.

## Workflow (Vercel) / WorkflowAgent

- Seat: functions with timeouts, plus agents that pause for tools and
  humans.
- Friction: a deploy or timeout erased in-flight agent state. The usual
  answer was Temporal, a queue, and a homemade state machine.
- Constraint inversion: suspend/resume is the default. Process death is
  not process amnesia.
- Category collapse: custom durable-execution wrappers around every
  agent loop.
- Five-line API:

```txt
export async function agent(input: string) {
  "use workflow";
  const result = await generateText({ model, prompt: input });
  return result.text;
}
```

- Mental model: a function that can sleep across deploys.
- Inevitability: once `'use workflow'` exists, a hand-rolled job table
  for "the agent is still going" looks like accidental infrastructure.
- Prior art honesty: Temporal, Inngest, Cloudflare Workflows, and
  durable queues already occupy this basin. The Labs move is collapsing
  that category *into the framework the app is already written in*.

## How to use this file

When a candidate is ready, write it at this density. If you cannot, it
is still a product idea. Send it back through inversion and collapse, or
kill it.

Do not copy these products. Copy the fields.
