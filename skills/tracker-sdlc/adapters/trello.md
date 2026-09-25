# Adapter — Trello

Verified: no — vendor docs as of 2026-09-24

Vendor facts for `sdlc-onboarding` and for repair. Not loaded at
runtime. Facts only: recipes live in the product repo's
`.agents/tracker/SKILL.md`. Facts marked `(unverified)` have no primary
vendor source yet; prove them live before relying on them.

## Hierarchy

- Trello has no issue hierarchy: a board holds lists, a list holds
  cards. Every level above the card is a convention of this contract.
- Track: one board per track, or a label per track on a shared board
  (convention, unverified).
- Epic, pick one per repo: a card carrying an epic label, or a parent
  card whose checklist lists its work items (convention, unverified).
  The work item card links back to its Epic in its description.
- Type (Task, Bug, Epic) = a label, or a dropdown custom field.
  Custom fields need the Standard plan or higher (not Free); a board
  holds at most 50 custom fields. A board with the feature disabled
  returns no fields.
- Label colors are a fixed set (green, yellow, orange, red, purple,
  blue, sky, lime, pink, black); the name is free text.
- Sub-items stay off: there is no level below the card besides
  checklist items.

## Blockers

- No native dependencies. Power-Ups add them (for example Card
  Dependencies by Screenful), but Power-Up data is read-only over the
  REST API; only the Power-Up's own client can write it. An agent cannot
  set such a blocker.
- Convention (this contract's design, unverified): the blocked card
  carries a `Blocked-by:` line in its description naming the blocker
  card's `shortLink` or URL, plus a `blocked` label. A card-URL
  attachment to the blocker is an optional extra.
- Direction: recorded only on the blocked card (blocked id ← blocker
  id). The blocker card holds nothing; compute "blocks" by reading the
  `Blocked-by:` lines of other cards.
- The blocker is resolved when its card sits in a list mapped to `done`
  or `canceled`. Nothing updates the line or label automatically;
  agents never remove blockers.

## Text format

- Card descriptions and comments are markdown (unverified in vendor
  docs).

## States and transitions

- State = the list a card sits in. Onboarding reads the board's lists
  and maps each list to a canonical state; list names go only into the
  repo skill's Mapping cells.
- A transition is a move of the card to another list, set directly;
  there is no workflow or transition step.
- Cards are archived, not deleted. The official MCP server cannot delete
  at all.
- Comments are card comments. PR and commit links go on the card as a
  URL attachment or in a comment.

## Gotchas

- `idShort` (the card number) is board-scoped and changes when the card
  moves. Never use it as the ticket id or in branch
  names; use the card's 8-character `shortLink`.
- Card and board ids are 24-hex strings; cards and boards both carry a
  `shortLink`, `shortUrl` and `url`.
- Rate limits apply per API key and per user token. 300 requests
  per 10 s per key, 100 per 10 s per token; the members resource
  allows 100 per 900 s. Over the limit returns 429 with a
  limit-exceeded error name for key or token. More than 200 429s on
  one key block it for the rest of the window. Requests that ask for
  too many cards fail: read cards first, then their actions
  separately. Responses carry rate-limit headers.
- Official MCP server capabilities: boards (view, create), lists (view,
  move), cards (view, create, update, move, archive, complete),
  checklists, attaching and detaching existing labels, search. It
  cannot read or write comments, read or write custom fields, add
  attachments, or create or edit labels (vendor says planned). So over
  it alone an agent cannot record PR links or read comments; that needs
  the REST API or a community server. Onboarding records this as a gap.
- The official server connects one workspace per connection, over OAuth.
  Workspace admins can restrict its permissions (read, write, search)
  and allowed domains.
- The official server's repo offers a skill-installer command.
  Never `npx skills install` it; connect the MCP server directly, and
  add any vendor skill only through INTAKE.
- No official Trello CLI was found (unverified).
- The Atlassian remote MCP server does not cover Trello.

## Discovery hints

- MCP config naming the host `mcp.trello.com` (host name only; read no
  other config value).
- An MCP config entry for a community Trello server (name only).
- Env var **names** `TRELLO_API_KEY`, `TRELLO_TOKEN` (community
  convention; names only, never values).
- Card links `trello.com/c/<shortLink>/<idShort>-<slug>` and board links
  `trello.com/b/<shortLink>/...` in PRs, commits or docs (URL shape
  unverified beyond the documented fields).
- Branch names or PR titles carrying an 8-character `shortLink`.

## Sources

- https://support.atlassian.com/trello/docs/connect-trello-to-ai-assistants-with-trello-mcp/
- https://github.com/atlassian/trello-mcp-server
- https://github.com/delorenj/mcp-server-trello
- https://developer.atlassian.com/cloud/trello/guides/rest-api/authorization/
- https://developer.atlassian.com/cloud/trello/guides/rest-api/getting-started-with-custom-fields/
- https://developer.atlassian.com/cloud/trello/guides/rest-api/object-definitions/
- https://developer.atlassian.com/cloud/trello/rest/api-group-cards/
- https://developer.atlassian.com/cloud/trello/guides/rest-api/rate-limits/
- https://support.atlassian.com/trello/docs/using-custom-fields/
- https://trello.com/power-ups/5cf76de9dd07a8533f281b34/card-dependencies-by-screenful
- https://community.developer.atlassian.com/t/modifying-plugindata-with-rest/38152
- https://developer.atlassian.com/cloud/trello/power-ups/client-library/getting-and-setting-data/
