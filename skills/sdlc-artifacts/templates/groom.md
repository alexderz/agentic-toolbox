# Groom — <chunk title>

DRAFT (pre-review)

<!-- At freeze, replace the marker above with: Frozen record of the
plan as reviewed at Groom on <YYYY-MM-DD>. Not live: the tracker is the
source of truth for tickets, blockers and state. -->

- Chunk: `<epic id>` · LLD: `<path>` · Date: `YYYY-MM-DD`
- Review: `<groom reviewer label>` — pass on `<date>` at `<commit SHA>`
- Tickets: `G1` = `<id>`, … (filled at freeze)

## Items

### G1: <title>

<Self-contained body copied into the ticket as-is: task.md / bug.md
Required fields. `Blocked by`: G ids, each with a one-clause reason, or
`none`. No secrets or private URLs.>

## Graph

- Wave 1: G1, G2
- Wave 2: G3 ← G1
- Wave 3: G5 ← G1, G3

Gates: `none`, or `G<n>` — <the integration or bottleneck need>
