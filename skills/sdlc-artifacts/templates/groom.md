# Groom — <chunk title>

DRAFT (pre-review)

<!-- At freeze, replace the draft marker above with this sentence and
delete this comment: Frozen record of the plan as reviewed at Groom on
<YYYY-MM-DD>. Not live: the tracker is the source of truth for tickets,
blockers and state. -->

- Chunk: `<epic id>` · LLD: `<path>` · Date: `YYYY-MM-DD`
- Review: `<groom reviewer label>` — pass on `<date>` at `<SHA of the
  reviewed draft commit>`; `pending` until filled at freeze
- Tickets: `G1` = `<id>`, … (filled at freeze)

## Items

### G1: <title>

<Self-contained body copied into the ticket as-is: the header (Type,
Parent, LLD link, Branch) and Required fields of task.md / bug.md.
`Blocked by`: G ids, each with a one-clause reason, or `none`.
`Blocks`: G ids, or `none`. No secrets or private URLs.>

## Graph

- Wave 1: G1, G2
- Wave 2: G3 ← G1
- Wave 3: G5 ← G1, G3

Gates: `none`, or `G<n>` — <the integration or bottleneck need>
