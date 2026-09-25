# Adapter — Trello

Verified: no — vendor docs as of 2026-09-24

Vendor facts for `sdlc-onboarding` and for repair. Not loaded at
runtime. Facts only: recipes live in the product repo's
`.agents/tracker/SKILL.md`. Facts marked `(unverified)` have no primary
vendor source yet; prove them live before relying on them.

## Hierarchy

- No hierarchy: board → list → card; below the card only checklist
  items, so sub-items stay off. Levels above the card are this
  contract's convention (unverified). Track: a board, or a track label.
- Epic: a card with an epic label. Each work item card carries a
  `Parent: <shortLink>` line in its description; that line is the
  record. A checklist on the Epic card may only mirror it.
- Type (Task, Bug, Epic) = a label, or a dropdown custom field.
  Custom fields need the Standard plan or higher (not Free); at most
  50 per board; a board with the feature disabled returns none.

## Blockers

- No native dependencies. Power-Ups add them (for example Card
  Dependencies by Screenful), but their data is read-only over REST.
- Convention (this contract's design, unverified): the blocked card
  carries one `Blocked-by: <shortLink>` line per blocker in its
  description, plus a `blocked` label as a visual cue.
- Direction: only on the blocked card (blocked id ← blocker id);
  "blocks" = other cards' `Blocked-by:` lines. Open-blocker check:
  parse the lines, then read each blocker's list and archived flag.
  Never trust the label: nothing clears it, so it goes stale
  (unverified). A description update replaces the whole text
  (unverified): set-blocker reads, appends, writes back. Agents never
  remove blockers.

## Text format

- Descriptions (≤16384 chars) and comments: the editor accepts most
  Markdown; API storage as Markdown: (unverified).

## States and transitions

- State = the list a card sits in. Onboarding maps each list to a
  canonical state; list names go only into the repo skill's Mapping
  cells. Map `done` and `canceled` to lists only, never to archiving.
- A transition is a direct move to another list; no workflow (unverified).
- Archive (`closed: true`) is separate from the list: an archived card
  keeps its list, and archiving a list or board does not archive its
  cards. Board card reads return open cards only by default: archived
  cards vanish, and an archived blocker read by list alone looks open.
- "Mark complete" (`dueComplete`) is a flag separate from list and
  archive, no due date needed; the official MCP "mark done" sets it
  (unverified). Onboarding records how archives and this flag map, or a Gap.
- Archive, not delete (official MCP cannot). PR and commit links: a URL
  attachment or a comment on the card.

## Gotchas

- `idShort` (the card number) is board-scoped and can change when the
  card moves to another board. Never use it as the ticket id or in
  branch names; use the card's 8-character `shortLink`. Card and board
  ids are 24-hex; both carry `shortLink`, `shortUrl` and `url`.
- Rate limits: 300 requests per 10 s per API key, 100 per 10 s per
  user token; members 100 per 900 s. Over: 429 with a limit-exceeded
  error name; over 200 429s blocks the key for the rest of the window.
  Read cards and their actions separately.
- Done before verified: automation (formerly Butler) can archive or mark
  complete a card moved into "Done"; the GitHub Power-Up attaches PRs
  (moving cards: unverified). Report as Gap.
- REST auth is an API key plus a user token that grants the user's
  whole account. As query parameters both sit in the request URL, so
  an echoed URL or error leaks them. Prefer the Authorization header;
  never paste request URLs into tickets, comments or reports.
- Official MCP server: boards (view, create), lists (view, move), cards
  (view, create, update, move, archive, mark done), checklists, attach
  and detach existing labels, search. Not comments, custom fields,
  attachments, or label create or edit (planned). Fallback for PR links and
  comments: REST or an already-configured community server, else a PR
  link line in the description (read, append, write back; the 16384
  limit caps appended lines) and a Gap.
- Claim: comments are `commentCard` card actions with a `date`, 50 per
  page, newest first (unverified): page, then reverse. No native agent
  field; members share the operator's account. The official MCP lacks
  comments: REST, a community server, or operator-made agent labels.
- Official server: OAuth, one workspace per connection, admins can
  restrict it. The Atlassian remote MCP server skips Trello. No official
  CLI (unverified). Never run its repo's skill installer; connect the
  MCP server directly (vendor skills go through INTAKE).

## Discovery hints

- MCP config naming the host `mcp.trello.com` (host name only; read no
  other config value); or an entry for a community Trello server.
- Env var **names** `TRELLO_API_KEY`, `TRELLO_TOKEN` (community
  convention; names only, never values).
- Card links `trello.com/c/<shortLink>/<idShort>-<slug>`, board links
  `trello.com/b/<shortLink>/...` (URL shape unverified); branch names
  or PR titles with an 8-character `shortLink`.

## Sources

- https://support.atlassian.com/trello/docs/connect-trello-to-ai-assistants-with-trello-mcp/
- https://github.com/atlassian/trello-mcp-server
- https://github.com/delorenj/mcp-server-trello
- https://developer.atlassian.com/cloud/trello/guides/rest-api/authorization/
- https://developer.atlassian.com/cloud/trello/guides/rest-api/getting-started-with-custom-fields/
- https://developer.atlassian.com/cloud/trello/guides/rest-api/object-definitions/
- https://developer.atlassian.com/cloud/trello/rest/api-group-cards/
- https://developer.atlassian.com/cloud/trello/guides/rest-api/nested-resources/
- https://developer.atlassian.com/cloud/trello/rest/api-group-boards/
- https://developer.atlassian.com/cloud/trello/guides/rest-api/rate-limits/
- https://support.atlassian.com/trello/docs/using-custom-fields/
- https://support.atlassian.com/trello/docs/mark-a-card-as-complete/
- https://support.atlassian.com/trello/docs/archiving-cards-automatically/
- https://support.atlassian.com/trello/docs/using-the-github-power-up/
- https://support.atlassian.com/trello/docs/how-to-format-your-text-in-trello/
- https://trello.com/power-ups/5cf76de9dd07a8533f281b34/card-dependencies-by-screenful
- https://community.developer.atlassian.com/t/modifying-plugindata-with-rest/38152
- https://developer.atlassian.com/cloud/trello/power-ups/client-library/getting-and-setting-data/
