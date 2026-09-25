# Adapter — Asana

Verified: no — vendor docs as of 2026-09-24

Vendor facts for `sdlc-onboarding` and for repair. Not loaded at
runtime. Facts only: recipes live in the product repo's
`.agents/tracker/SKILL.md`. Facts marked `(unverified)` have no primary
vendor source yet; prove them live before relying on them.

## Hierarchy

- Track = Asana **portfolio** or **project**. Portfolios group projects,
  so they fit a track, not an Epic.
- Epic = parent task. Work item = subtask of that parent. Subtasks are
  the item level, so extra sub-items below them stay off.
- Type (Task or Bug) = enum custom field or tag. Convention of this
  contract (unverified).
- Custom fields are a paid (Premium) feature. On a free workspace, use
  tags for type and sections for state.

## Blockers

- Native task **dependencies**. A task's dependencies and dependents
  together are capped at 30.
- Direction: adding dependencies to task X records the listed tasks as
  X's dependencies, so X waits on them. The repo skill records it one
  way: blocked id ← blocker id.
- The reverse view (dependents) and the remove operations exist in the
  API but were not checked (unverified).
- Plan tier: dependencies need Starter or above, not free Personal
  (unverified).

## Text format

- Rich text is HTML, not markdown. Task and project descriptions use
  `html_notes`; comments use `html_text`.
- The value must be valid XML wrapped in `<body>`, with balanced tags
  and only allowed tags. Only `<a>` takes attributes. Invalid markup
  fails with 400.
- Plain `text` is the other comment form. Comments are **stories** on
  the task.
- PR links go in a comment or as an `<a>` in `html_notes`.

## States and transitions

- State = **section** (list header or board column) in the project, or
  an enum custom field (paid). Sections always work; custom fields do
  not exist on free workspaces.
- A task's section is in its `memberships` property. Moving state means
  adding the task to another section.
- An enum custom field is set by option GID, not by option name. Each
  option has `gid`, `name`, and `enabled`; the task's value is in
  `enum_value`.
- Onboarding reads the project's sections (or the field's options) and
  maps each one to a canonical state; names go only into the repo
  skill's Mapping cells.

## Gotchas

- Custom fields are paid. The error a free workspace returns is not
  documented; the vendor says to program defensively.
- Task search is paid (Premium) too. On a free workspace, list tasks by
  project or section instead.
- Pagination: `limit` 1–100 (default 20); the next `offset` comes in
  `next_page`, which is null on the last page. Offsets expire, so page
  through promptly. Unpaginated results truncate at about 1,000
  objects.
- Rate limits: 150 requests per minute on free, 1,500 on paid; search
  60 per minute; at most 50 concurrent reads and 15 concurrent writes;
  a cost-based quota also applies. Over the limit: 429 with
  `Retry-After`. Rejected requests still count.
- The 30-dependency cap covers dependencies and dependents combined.
- Ids are GIDs: long numeric strings, no human key. The SDLC branch
  `item/<ticket-id>-<slug>` carries the task GID.
- Two URL shapes (see Discovery hints). Parse either for the task GID.

## Discovery hints

- MCP config naming the host `mcp.asana.com`, or a server named
  `asana` (host name only; read no other config value).
- MCP config naming the community package `@roychri/mcp-server-asana`
  (presence only).
- Env var **names** `ASANA_ACCESS_TOKEN`, `ASANA_CLIENT_ID`,
  `ASANA_CLIENT_SECRET` (names only, never values).
- Task URLs on host `app.asana.com`:
  `app.asana.com/0/<project-gid>/<task-gid>` (V0, still supported) or
  `app.asana.com/1/<workspace-gid>/project/<project-gid>/task/<task-gid>`
  (V1).
- Branch names, PR titles, or commits carrying a long numeric GID.

## Sources

- https://developers.asana.com/docs/using-asanas-mcp-server
- https://developers.asana.com/docs/connecting-mcp-clients-to-asanas-v2-server
- https://developers.asana.com/docs/mcp-tools-reference
- https://developers.asana.com/docs/personal-access-token
- https://developers.asana.com/reference/sections
- https://developers.asana.com/docs/custom-fields-guide
- https://developers.asana.com/reference/adddependenciesfortask
- https://help.asana.com/s/article/task-dependencies?language=en_US
- https://developers.asana.com/docs/rich-text
- https://developers.asana.com/docs/pagination
- https://developers.asana.com/docs/rate-limits
- https://forum.asana.com/t/upcoming-new-v1-asana-url-format-in-the-browser/1011489
- https://github.com/roychri/mcp-server-asana
