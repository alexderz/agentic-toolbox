# Live endpoints

Pointing an eval at a real system produces far better signal than a
mock: real payload shapes, real error semantics, real edge cases. It
also means untrusted agents are talking to something that matters.

## Read-only is usually not a token feature

Many systems issue tokens that inherit the full permissions of the user
that created them, with no scope mechanism — a "read-only token" is
simply not on offer. Home Assistant is one such system: a long-lived
access token carries the creating user's rights, and even a non-admin
user can call services.

Enforce read-only **in front of** the system instead.

## Filtering proxy

A small proxy between the agents and the real system:

- **allow only safe methods** (`GET`, `HEAD`); everything else 405
- **block write-shaped paths even on GET** — an endpoint like
  `/services/<domain>/<action>` should be refused, while the bare
  `/services` *listing* stays available so agents can still discover
  what exists
- **rate limit** so an agent in a loop cannot hammer production
- **hold the real credential in the proxy**, and give agents a
  placeholder. They then cannot leak it into generated code, a README,
  or a session transcript
- **validate the placeholder** anyway, so "handles auth correctly"
  remains a testable property
- **log every request**, which yields a behavioural metric: what each
  model actually explored, and whether it explored at all

## Let the rate limit bite

Handling `429` is part of the job. Do not raise the limit because
models are hitting it — that is the test working. Check whether each
tool detects `429`, retries with backoff, and honours `Retry-After`.
This separates the field sharply and costs nothing to measure.

## Guard the runner

The eval driver should refuse to start unless it has confirmed, at that
moment, that a write is actually refused and a read actually succeeds.
Failing closed is the difference between a safe eval and one bad config
away from an incident.

## Drift

A live target changes. Record a fingerprint alongside results —
resource counts by type, API version, date — so a later run can
distinguish a model difference from a target difference. When
qualifying a new model later, re-run a baseline model beside it rather
than comparing against a stored number.
