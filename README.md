# Officina

[Japanese](README.ja.md)

Agents asked for original ideas regress to generalities and word mashups:
"Notion for agents", "AI-powered memory", "Durable Objects but for X".

Officina is a Skill that forces Labs-grade primitive extraction instead.
Before an agent promotes a product idea, it has to name a seat, a
constraint it inverts, a category that should collapse into a five-line
API, prior art (including this author's already-struck primitives), an
OSS wedge, and a kill-probe. Cards that cannot do that are killed in
public.

Here, a Skill is a small agent-loadable package: one `SKILL.md` file plus
optional references, examples, evals, and scripts.

Status: experimental. The package includes one saved baseline comparison,
not a benchmark suite. On the generic-idea fixture, Officina scored
16/16 against a baseline at 0/16; the measured gain was mashup
suppression and primitive sharpness, not proof that the surviving cards
will work. See [evals/runs/generic-comparison.md](evals/runs/generic-comparison.md).

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

The name is Latin *officina*: a workshop. The bench is for striking a
primitive, not for brainstorming.

## Why This Exists

Ordinary idea tools, and mutation-style ideation, produce combinations:

```txt
agents + memory + dashboard -> AI-powered memory copilot
edge + database -> "like Durable Objects"
Notion + agents -> Notion for agent thoughts
```

That is useful when the user wanted a list of pitches. It is expensive
when the user wanted the next thing that should exist: Workers, R2, AI
SDK, Fluid, Workflow. Those were constraint inversions with a name and
an API, not mashups.

Officina is for the second case.

## What It Is Not

- Not a claim that product strategy is new.
- Not a replacement for market research, evals, or shipping.
- Not a universal prompt to use on every task.
- Not a way to make idea lists longer.
- Not mutation-style "break the default basin" ideation.
- Not proof of market value by itself.

The narrower claim is:

```txt
Labs-style primitive extraction can be packaged as an agent-executable
Skill, with a kill-gate, claimed-primitive list, and evaluation hooks.
```

## Where It Helps

Use it when accepting the first idea list would create real cost:

- what to build next in a Labs / OSS wedge sense
- platform-primitive design without owning a CDN
- stopping X-for-Y and AI-powered X
- reviewing a "this should exist" pitch before a spike

Do not use it for direct implementation, small factual questions, simple
rewrites, or tasks where the solution is already chosen. Do not use it
when the user asked for wild alternatives to a known approach.

## Install

Requires Node.js 20 or newer.

After npm publication, install into both Codex and Claude Code skill
directories:

```bash
npx officina-skill install --all
```

Install into only one runtime:

```bash
npx officina-skill install --codex
npx officina-skill install --claude
```

Check local install status:

```bash
npx officina-skill doctor
```

The installer copies the package into:

```txt
~/.codex/skills/officina
~/.claude/skills/officina
```

Before npm publication, run the same CLI from a GitHub repo:

```bash
npx --package github:OWNER/officina officina-skill install --all
```

Replace `OWNER` with the GitHub owner that hosts the repository.

From a cloned repository, run the bundled installer directly:

```bash
node bin/officina-skill.js install --all
```

Then ask the agent to use `officina` on an idea, Labs, or "what to build"
question. If your agent runtime does not support Skills, use `SKILL.md`
as the process prompt and load the reference files only when needed.

## Example

Prompt: the fixture in [evals/fixtures/generic-vs-primitive.md](evals/fixtures/generic-vs-primitive.md).

Common shallow answer: a list of mashups and relabeled platform
products.

Officina-shaped answer: a short catalog. In the saved showcase, the
survivors are `staple` (compaction cannot drop pinned constraints) and
`seal` (a hidden oracle process is the default judge). Durable-agent
workflow, Notion-for-thoughts, agent-vcr, and MCP capability tokens are
killed as known primitives or X-for-Y.

See [examples/showcase.md](examples/showcase.md) for the full pass.

## What Changes In Practice

The output usually becomes less like:

```txt
AI-powered memory, durable agents, Notion for thoughts, a dashboard.
```

and more like:

```txt
Seat: the assembler of coding-agent sessions.
Inversion: dropping a constraint becomes illegal, not cheap.
Collapse: session-summary / memory SaaS as the way to keep vetoes.
API: staple.put / budget / compact (throws) / assemble.
Kill: if rejected paths reopen at the same rate, stop.
```

The point is not to make the answer longer. The point is to make the
path to a primitive reviewable, and to keep mashups in the kill column.

## Package Layout

```txt
officina/
  SKILL.md
  README.ja.md
  package.json
  bin/
    officina-skill.js
  agents/openai.yaml
  references/
    labs-canon.md
    anti-patterns.md
    claimed.md
    seat.md
  examples/
    showcase.md
  evals/
    rubric.md
    value-metrics.md
    runs/
      generic-comparison.md
    fixtures/
      generic-vs-primitive.md
      x-for-y.md
      known-platform.md
  scripts/
    check_package.py
  LICENSE
```

`SKILL.md` is the runtime instruction file. The canon, kill-gate,
claimed list, and evaluation material are loaded only when needed.

## Evidence Base

The design copies the *shape* of known Labs primitives, not the
products. Dissections of Durable Objects, R2, AI SDK, Fluid, and
Workflow live in [references/labs-canon.md](references/labs-canon.md).

The market case is intentionally bounded. Developers clearly want
"the next Workers / R2 / AI SDK". That does not prove this Skill beats
a baseline at producing it. That claim has to be measured.

## Evaluation

Use [evals/value-metrics.md](evals/value-metrics.md) to compare:

```txt
baseline: normal agent answer
terse: normal agent answer with concise-output instruction
officina: answer using this Skill
```

Primary metrics:

- generic-solution suppression
- primitive sharpness
- inevitability
- kill-probe
- OSS-wedge honesty
- seat honesty
- prior-art honesty
- human approval readiness

The current bar for a useful result is:

- at least 12/16 on the value metrics
- at least +4 over baseline
- at least +3 over terse on suppression plus primitive sharpness

Run package checks with:

```bash
npm run check
npm run pack:dry
```

The saved run in [evals/runs/generic-comparison.md](evals/runs/generic-comparison.md)
is intentionally narrow: it shows that a mashup list scores zero, while
Officina makes inversions, APIs, kills, and disconfirmation tests
explicit.

## Status

This is an early Skill package, not a benchmarked product.

What is already present:

- runtime Skill instructions
- Labs canon
- genericness kill-gate
- claimed-primitive list
- seat guide
- evaluation rubric
- value metrics
- regression fixtures
- worked showcase catalog
- package self-check script

What still needs real proof:

- blinded human preference tests
- repeated baseline vs Officina evals
- kill-probes actually run on staple and seal
- downstream "did anyone spike this" measurement

## One Sentence

Officina is a primitive compiler for AI agents: it turns an idea request
into a small catalog of named, killable Labs cards, or it refuses to
promote anything.

## License

MIT. See [LICENSE](LICENSE).
