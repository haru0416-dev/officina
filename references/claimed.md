# Claimed primitives

Do not rewrap these as new Labs cards. They are already struck, in this
author's public line of work or as adjacent skills.

When a candidate is one of these with a new coat of paint, label
`known primitive` and stop. A sibling in a *different seat* may still
be a spark if the API is not the same object.

## coffer

- Inversion: oversized tool output is held byte-exact, not truncated.
- Collapse: naive head/tail windows and lossy "summarize the tool
  result" as the default response to context caps.
- Mental model: a content-addressed handle plus exact compute beside
  the bytes.
- Repo: `https://github.com/haru0416-dev/coffer`

Rewraps to kill: "smart context compression", "RAG over tool output",
"summarize kubectl better", another MCP that truncates with style.

## quaere

- Inversion: an agent may not act on a plausible claim. It has to
  produce evidence first.
- Collapse: "just let the agent code" as a workflow, and a class of
  prompt-only "be careful" instructions.
- Mental model: claim -> evidence -> probe -> scoped patch.
- Repo: `https://github.com/haru0416-dev/quaere`

Rewraps to kill: "better system prompt for agents", "AI code review
SaaS", "checklist copilot".

## ad-radicem

- Inversion: the observed symptom is not the problem. Reconstruct the
  problem space before solutioning.
- Collapse: generic solution basins (add RAG, add memory, add tests,
  add onboarding email).
- Mental model: a problem-space compiler for agents.
- Repo: `https://github.com/haru0416-dev/ad-radicem`

Rewraps to kill: "root-cause chatbot", "strategy copilot", another
skill that only lengthens answers.

## munou

- Inversion: dialogue does not require an LLM. Closed, explainable
  machinery is the default for that job.
- Collapse: "wrap a chat model" as the only way to ship a character
  or a companion.
- Mental model: an inspectable dialogue engine with no hidden weights.
- Repo: `https://github.com/haru0416-dev/munou`

Rewraps to kill: "local LLM chatbot", "persona layer on GPT".

## dubito

- Inversion: one solver formulation is not an answer. Independent
  formulations have to agree.
- Collapse: "trust the optimizer output" and single-shot MILP
  pipelines.
- Mental model: cross-check across independent encodings of the same
  claim.
- Repo: `https://github.com/haru0416-dev/dubito`

Rewraps to kill: "AI for operations research", a second wrapper around
one solver, "explain the LP with a model".

## parvix

- Inversion: images entering an agent hook are shrunk to a budget
  before they blow the window.
- Collapse: "attach the PNG and hope".
- Mental model: a single binary that enforces an image token budget.
- Repo: `https://github.com/haru0416-dev/parvix`

Rewraps to kill: "AI image optimizer", another compressor without a
hook-shaped seat.

## Officina itself

This skill is the process for minting primitives. Do not emit a card
that is "a better idea generator". That is this package, and it is
explicitly not an idea generator.

## How to extend this file

When a primitive is promoted out of a catalog into a repo, add it
here on the next Officina pass. Claimed means "already inverted", not
"famous".
