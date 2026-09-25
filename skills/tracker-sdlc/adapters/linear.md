# Adapter — Linear

Verified: no — vendor docs as of 2026-09-24

Vendor facts for `sdlc-onboarding` and for repair. Not loaded at
runtime. Facts only: recipes live in the product repo's
`.agents/tracker/SKILL.md`. Facts marked `(unverified)` have no primary
vendor source yet; prove them live before relying on them.

## Hierarchy

- Track = Linear **Project**. Structural choice of this contract.
- Epic = parent issue labeled with the Epic type label (for example a
  `Type` label group holding Epic and Task). Structural choice; the
  parent and sub-issue fields over the API are (unverified).
- Work item = issue under its Epic, labeled Task or Bug. Labels can be
  grouped; a type group may not hold every type label, so onboarding
  checks where each one lives.
- Issues belong to a team; creating one needs the team (unverified).
- Sub-items (sub-issues under a work item) stay off unless the
  workspace already uses them. The one parent field links item → Epic
  and sub-issue → item: tell the levels apart by the parent's type
  label.

## Blockers

- Native relations: **blocks** / **blocked by**, **related**,
  **duplicate**. Relation type values are `blocks`, `duplicate`, and
  `related`.
- Direction: the blocker lists the other issue under **Blocking**; the
  blocked issue lists it under **Blocked by**. That one relation shows
  on both issues (observed on a live workspace 2026-09-24). The repo
  skill records it one way: blocked id ← blocker id.
- A resolved blocker **stays** listed as "blocked by": observed on a
  live workspace 2026-09-24 (an issue still listed its blocker while
  that blocker was Done). Recipes check each blocker's state; the list
  alone never proves an open blocker.
- Marking a duplicate moves the issue into the reserved **Duplicate**
  status. Map it to `canceled`.
- A community report says adding a relation can convert an existing one
  instead of adding a second (unverified). Read relations back after
  set-blocker.

## Text format

- Descriptions and comments are markdown (unverified in vendor docs).

## States and transitions

- Statuses are per team (unverified). Onboarding reads the team's list
  and maps each status to a canonical state; names go only into the
  repo skill's Mapping cells.
- Duplicate is a reserved status (see Blockers).
- Status is set directly on the issue. There is no separate transition
  step (unverified).
- Auto-transitions from the Git integration: closing words in a PR
  (closes, fixes, resolve, complete, implement) apply the team's
  "on merge" status. Non-closing words (ref, references, part of,
  contributes to) move status without the merge step. "relates to" /
  "related to" only link.
- Default automation: In Progress when the PR opens, Done when it
  merges. Teams can change it per team. Done on merge can precede
  landed+verified; onboarding reports this as a gap.

## Gotchas

- Rate-limit numbers are not published (unverified). The docs warn that
  polling individual issues risks hitting limits: batch reads, do not
  poll.
- Done on merge may mark an item `done` before verification (see
  States and transitions).
- A Duplicate issue is not `done`; it is `canceled`.
- "Blocked by" lists done and canceled blockers too (see Blockers):
  resolve every blocker's state before list-ready or claim.
- Claim: agents that act through the operator's account share one
  assignee (observed on a live workspace 2026-09-24), so the default
  claim comment applies. Comments carry a creation timestamp; order by
  it, oldest first (unverified).
- Native agent field: assigning an issue to an agent application sets
  its **delegate**, not the assignee, and keeps the human owner. Only an
  agent installed as its own Linear application has one; an agent on
  the operator's account cannot use it.
- Keys are `ABC-123` (team key + number). Suggested branch names put
  the key in lowercase (for example `abc-123-short-title`). The SDLC branch `item/<ticket-id>-<slug>` also carries
  the key; the integration links branches that contain it.
- The key pattern `[A-Z][A-Z0-9]+-[0-9]+` also matches Jira keys. Use
  other hints to tell the two apart.

## Discovery hints

- MCP config naming the host `mcp.linear.app` (host name only; read no
  other config value).
- Env var **names** `LINEAR_API_KEY`, `LINEAR_TEAM_ID` (names only,
  never values).
- A `linear.toml` or `.linear.toml` file in the repo (community CLI
  config): presence only; read host names only, never keys.
- Branch names with a lowercase key (`abc-123-...`); PR titles or
  commits with `ABC-123`; a `Linear-issue` commit trailer.
- PR linking: the key in the branch name or PR title links the PR to
  the issue.

## Sources

- https://linear.app/docs/mcp
- https://linear.app/docs/issue-relations
- https://linear.app/docs/github
- https://linear.app/developers/graphql
- https://linear.app/developers/agents
- https://www.speakeasy.com/product/mcp-gateway/catalog/linear/
- https://github.com/schpet/linear-cli
- https://github.com/PelvicSorcerer/moviecal/issues/342
- https://github.com/CodySwannGT/lisa/issues/3605
