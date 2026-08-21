# Anti-Patterns

This is the genericness kill-gate. Read it when a card starts to sound
clever, busy, or fundable instead of inevitable.

A killed card is a successful use of Officina. A catalog with no kills
is not being filtered.

## Instant kill

Promote none of these. Label `kill` with the matching reason.

### X-for-Y

"Uber for dentists." "Notion for agents." "Figma for prompts."

The structure is a known product plus a new customer noun. It does not
invert a constraint and does not collapse a category. It relocates a
UI.

Kill reason: `x-for-y`.

### Word or trend mashup

"AI plus blockchain plus sustainability." "Agents plus WASM plus
edge." Concatenating fashionable nouns is not inversion.

If the only mechanism is "combine A and B", the novelty label is
`recombination` at best, and the card is still a kill unless an
inversion and a five-line API survive without the mashup words.

Kill reason: `mashup`.

### AI-powered X

Prefixing an existing category with AI does not mint a primitive.
"AI-powered analytics", "AI code review", "AI memory for chats" are
features looking for a model.

Kill reason: `ai-powered-x`.

### Dashboard / copilot / platform as first artifact

If the first five-line API is a settings page, a timeline, a feed, or
"a copilot that sits on top of your tools", there is no primitive.
Those are coats of paint.

Kill reason: `surface-first`.

### Mutation theatre

Assumption lists and operator passes (invert, subtract, transfer) can
be useful elsewhere. They are not this skill. If the card exists only
because an operator was applied to a default basin, it is an idea, not
a primitive.

Kill reason: `mutation-only`.

### Seat fiction

"If we were Cloudflare..." or "once we have a global network..." is
not a seat. A seat is a friction you already sit beside. Borrowed
infrastructure you do not have is a wish.

Kill reason: `fake-seat`.

### Feature-shaped

"Add export to CSV." "Add SSO." "Add a marketplace." Incremental
product work can be good. It is not a Labs card.

Kill reason: `feature`.

### Volume

Ten live cards with thin APIs is worse than two with kill-probes.
Cut until each remaining card could be the only experiment this
quarter.

Kill reason: `volume` (applied to the extras, not to the survivors).

## Soft kills (usually kill, sometimes spark)

### Known primitive, new coat

Durable execution, provider-agnostic SDKs, object storage without
egress, single-threaded actors, append-only logs: these already have
names. Restating them in a new domain is `known primitive`. You may
keep a spark only if the *seat* forces a different API. Otherwise kill.

### Recombination that cannot drop a part

If removing either half of the idea leaves nothing, it was a mashup.
If removing one half leaves a still-valid primitive, keep that half
and kill the rest.

### Inevitability by adjective

"This is unique / inevitable / what people actually wanted" with no
mechanism is marketing. Inevitability has to point at a habit that
becomes embarrassing after the API exists.

## What passing looks like

A passing card can be read as:

```txt
Because we sit at <seat>,
<expensive thing> can become the default,
so <category> becomes <five-line API>,
and if <kill signal> happens we stop.
```

If that sentence needs a second product, a trend, or a hypothetical
platform, it has not passed.

## Novelty labels (fixed)

Use only these. They are findings, not compliments.

- `known primitive` -- already named; do not promote.
- `category collapse` -- a product category becomes a short API. This is
  the target label.
- `recombination` -- a mix of known parts. Rarely promote.
- `incoherent` -- does not hold together; drop.

Forbidden in output: self-rated originality, unique moat, 10x, unicorn.

## Relationship to other ideation

If the user asked for "wild alternatives" or "break the obvious
approach", that is mutation-style ideation. Officina will mis-serve
that request. Say so, and either switch or refuse to emit a catalog
of alternatives.
