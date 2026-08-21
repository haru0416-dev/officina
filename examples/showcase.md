# Showcase

This file is the first catalog produced by following `SKILL.md` on the
prompt in `evals/fixtures/generic-vs-primitive.md`. It is not a backlog
of products. Claimed primitives (coffer, quaere, ad-radicem, munou,
dubito, parvix) are treated as already struck.

## Shallow Baseline

A normal idea tool, asked for "original Labs-like OSS", emits:

```txt
1. Notion for agent thoughts
2. AI-powered memory that never forgets
3. Durable Objects for agents (workflow DSL + dashboard)
4. Uber for GPU time
5. Figma for prompts
6. GitHub Copilot but for architecture
7. Blockchain provenance for LLM outputs
8. A better context compressor
9. An agent that reviews other agents
10. Observability suite with a timeline
```

That list is generalities and noun combinations. It has no seat, no
inversion, no five-line API, and it rewraps claimed work ("better
context compressor") plus known platform primitives (durable execution).
Officina exists to stop this list from being the answer.

## Officina Catalog

### Seat

Coding-agent sessions this author already sits in: MCP tool results,
skill loading, patches, and compaction. The lever is the assembler of
those sessions (hooks, wraps, skill packages), not a model vendor and
not a global network.

### Friction

Observed, not vibed:

- Long sessions drop "do not do X" and reopen rejected paths. The
  ad-radicem package exists because summaries lose negative constraints.
- Agents declare done after checking their own writer. The quaere
  parquet case is the type specimen: a homemade encoder verified against
  itself.
- Skill hosts pick skills by feeding descriptions to the same model that
  wants to act. Wrong skill, or no skill, is a silent routing failure.
- Claimed work already inverted hold-don't-truncate (coffer),
  claim-then-evidence (quaere), LLM-free dialogue (munou), solver
  cross-check (dubito), and image budgets (parvix). Those are not open
  seats.

### Constraint inversion

Today, keeping a constraint is expensive (it burns window, so compaction
drops it) and checking a patch is cheap to fake (the same transcript
writes the test and the code). Invert both: pinned constraints become
illegal to drop, and a hidden oracle becomes the default judge.

## Cards

### C-001 staple

Status: experiment
Novelty: category collapse

Category collapse: session-summary products and "agent memory" SaaS as
the way to keep decisions.

One-liner: Pinned paths are outside the compaction budget. Dropping them
is a hard error, not a quality issue.

Five-line API:

```txt
staple.put("veto/no-rewrite-auth", bytes)   // never GC'd, not in budget
const { stapled, working } = staple.budget()
const view = staple.compact(history)        // throws if a staple would drop
assemble(stapled, view)
```

Mental model: R2 for constraints. Egress (loss) is the thing that
becomes free to avoid, and expensive to do.

Inevitability: after `staple.put`, "we summarized the session" looks
like deleting the lock file to save disk.

Genericness gate: pass. Not X-for-Y. Not a memory chatbot. The
inversion is budget accounting, not "store more embeddings".

Prior art:

- Claimed: ad-radicem's compression contract is the *skill* that asks
  the model to keep fields. This card dies if the only implementation
  is another prompt. It lives only as assembler enforcement.
- `akslcw/dsh-negative-ledger`, tombstone/graveyard memory, ADR logs:
  stores the model is *asked* to read. Different object if the
  assembler cannot omit the bytes.
- Claude Code cache breakpoints: stable vs dynamic for *prefill cost*,
  not a forbid-loss contract.
- CLAUDE.md / AGENTS.md: manual always-include, no budget type.

OSS wedge: a tiny library plus a file format (`.staple.jsonl`) any host
can load. Hosted plane is optional (shared staples across machines).
The public thing is the contract: compact() throws.

Kill-probe: twenty long sessions with stapled vetoes vs ordinary
summary. Kill signal: rejected paths reopen at the same rate, or hosts
refuse to call compact() because throwing is annoying. Cost: one
weekend wrap around an existing agent's summary step.

### C-002 seal

Status: experiment
Novelty: category collapse

Category collapse: eval dashboards and "AI code review" as the way to
know a patch is done. Also the everyday habit of letting one transcript
write the tests and the code.

One-liner: The judge is a hidden tree the implementer process cannot
read. Done is a receipt from that process, not a model utterance.

Five-line API:

```txt
seal.hide("oracle/")              // not on the implementer's filesystem
seal.run(implCmd)                 // no oracle in env or prompt
const r = seal.judge(diff)        // AGREE | DISAGREE + receipts
```

Mental model: a programming-contest judge, as a default git hook, not
as a benchmark.

Inevitability: after `seal.judge`, "I ran the tests I just wrote" looks
like grading your own exam.

Genericness gate: pass. Not a copilot. The inversion is isolation, not
"a smarter reviewer".

Prior art:

- Claimed: dubito is independent *solver formulations*. This is the
  sibling for *patches*. Do not rewrap dubito as "AI for OR".
- SWE-bench hidden tests, contest oracles, `sebuzdugan/agent-eval-harness`:
  the primitive already exists in *evaluation*. The Labs move is
  collapsing that harness into the daily agent CLI.
- quaere's parquet lesson is the friction, not the primitive.

OSS wedge: a CLI that hides a directory, runs a command, then judges in
a second process. Later product: a CI gate that refuses merge without
a seal receipt. The public thing is the two-process protocol.

Kill-probe: take ten tasks where the same-transcript agent already
"passes" its own tests. If seal.judge agrees with those self-passes,
isolation did nothing (the public spec leaked the oracle, or the
oracle was too thin). Kill. Cost: wrap pytest/cargo test behind hide +
judge on one repo.

### C-003 signpost

Status: spark
Novelty: recombination

Category collapse: embedding routers and "ask the model which skill to
load" as skill discovery.

One-liner: Skill dispatch is a closed matcher. The acting model does
not choose the skill that constrains it.

Five-line API:

```txt
signpost.add({ name: "officina", when: { all: ["labs", "primitive"] } })
signpost.match(task)  // -> [{ name, rule, why }]
signpost.load("officina")
```

Mental model: a mail sorter. Not an embedding index.

Inevitability: mixed. Hosts already put skill descriptions in the
prompt and let the model pick. A closed matcher is munou-shaped
routing. It may be a small inversion, not a Labs-sized one.

Genericness gate: pass as spark only. Kill if the API grows a dashboard
or "AI routing".

Prior art:

- Claimed: munou (closed dialogue) and this package's own frontmatter
  discovery. Sibling, not a rewrap, only if the matcher is
  mechanical and inspectable.
- Claude Code / Codex skill descriptions, Cursor globs, ordinary
  classifiers.

OSS wedge: a 200-line matcher plus a test corpus of tasks. No hosted
plane required.

Kill-probe: fifty labeled tasks. If keyword/glob F1 is not better than
the host's built-in description matching on the misses that hurt (wrong
skill loaded), kill. Cost: an afternoon corpus.

### C-004 durable-agent-workflow

Status: kill
Novelty: known primitive

Category collapse: none available. Temporal, Inngest, Cloudflare
Workflows, and Vercel WorkflowAgent already collapsed "keep the agent
alive across timeouts" into a function annotation.

One-liner: (killed) long-running agents with a DSL and a control plane.

Genericness gate: kill (`known primitive`, `fake-seat` if it needs a
hosted fabric, `surface-first` if it starts with a dashboard).

Prior art: see `references/labs-canon.md` under Workflow. Do not remix.

OSS wedge: n/a

Kill-probe: n/a (already killed by prior art)

### C-005 notion-for-agent-thoughts

Status: kill
Novelty: incoherent

Category collapse: none. This is X-for-Y.

One-liner: (killed) Notion for agent thoughts.

Genericness gate: kill (`x-for-y`, `surface-first`).

Prior art: every idea generator. Included so the filter is visible.

OSS wedge: n/a

Kill-probe: n/a

### C-006 agent-vcr-default

Status: kill
Novelty: known primitive

Category collapse: already done by VCR, Polly, Playwright tapes, and
several agent-vcr projects (CI cassettes for tool calls and MCP).

One-liner: (killed) record/replay of tool calls as the Labs primitive.

Genericness gate: kill (`known primitive`). A cassette default is a
good engineering habit. It is not an open primitive for this seat.

Prior art: `vcr/vcr`, `ajayvnkt/agent-vcr`, Capital One Agent VCR for
MCP, `matsurih/agentape`.

OSS wedge: n/a

Kill-probe: n/a

### C-007 mcp-capability-tokens

Status: kill
Novelty: known primitive

Category collapse: object capabilities for tools. Semgrep's 2026 note,
macaroons, biscuits, `agent-authority`, AIP already occupy this.

One-liner: (killed) unforgeable per-step MCP tokens.

Genericness gate: kill (`known primitive`). Adjacent to coffer-wrap's
transport seat, but minting a new cap system would be a reimplementation,
not an inversion.

Prior art: object capabilities (1970s), macaroons, biscuits, MCP OAuth
2.1, Semgrep "Security Like It's 1977".

OSS wedge: n/a

Kill-probe: n/a

## Residual risk

- C-001 dies if staple is implemented as "please keep these fields" --
  that is ad-radicem, already claimed.
- C-002 dies if the hidden tree is guessable from the public spec, or
  if nobody will run two processes locally.
- C-003 is the weakest live card. It is allowed to die first.
- Numeric firewalls (PCN, SHOR, helix-grounding) and hold-don't-truncate
  (coffer) were considered and not promoted.
- This catalog is one pass on one seat. It is not a roadmap.

If C-001's kill-probe fires, the next Officina pass should look for a
different inversion in the same seat (assembler), not a new brand for
memory.
