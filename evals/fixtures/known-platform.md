# Fixture: known platform primitive

The user asks for something that already has a Labs name. Officina
must stop, not remix it.

## Prompt

```txt
I want to build the next Durable Objects: long-running agents that
survive deploys and timeouts, with a workflow DSL, queues, and a
hosted control plane. Make it original and open source, like Vercel
Workflow or Temporal, but for AI agents. Also add a dashboard.
```

## Baseline failure to watch

- A new brand for Temporal/WorkflowAgent.
- "AI-powered durable execution."
- A fake seat ("once we have a global network").

## Officina expectation

- Status `kill` (or `known primitive` with no promote).
- Kill reasons: `known primitive`, probably `fake-seat` and
  `surface-first` for the dashboard.
- Optional: if the author's real seat suggests a *different*
  inversion (not durable execution), one spark card that does not
  borrow the control plane.
- Five-line API is not required on a killed known primitive, but the
  canon dissection (seat / inversion / collapse) should still be
  named so the reader sees why it already exists.
