# Adapter — Asana

Verified: no — vendor docs as of 2026-09-24

Vendor facts for `sdlc-onboarding` and for repair. Not loaded at
runtime. Facts only: recipes live in the product repo's
`.agents/tracker/SKILL.md`. Facts marked `(unverified)` have no primary
vendor source yet; prove them live before relying on them.

## Hierarchy

- Track = Asana **portfolio** or **project**. A portfolio holds
  projects, so list-ready on a portfolio track iterates its projects.
- Epic = parent task. Work item = subtask of that parent. Subtasks are
  the item level, so extra sub-items below them stay off.
- Subtasks do not inherit the parent's projects. A subtask is in a
  project (and has a section there) only if added to it.
- Type (Task or Bug) = enum custom field or tag. Convention of this
  contract (unverified).
- Custom fields are a paid (Premium) feature. On a free
  workspace, use tags for type and sections for state.

## Blockers

- Native task **dependencies**. A task's dependencies and dependents
  together are capped at 30.
- Direction: adding dependencies to task X records the listed tasks as
  X's dependencies, so X waits on them. The repo skill records it one
  way: blocked id ← blocker id.
- The reverse view (dependents) and the remove operations exist in the
  API but were not checked (unverified).
- Plan tier: dependencies need Starter and up, not free Personal
  (unverified).
- Completing a blocker ends the "waiting" on its dependents
  (unverified).

## Text format

- Rich text is HTML, not markdown: `html_notes` on tasks and projects.
  Comments are **stories**, as plain `text` or `html_text`.
- The value must be valid XML wrapped in `<body>`, with balanced tags
  and only allowed tags. Only `<a>` takes attributes. Invalid markup
  fails with 400.
- PR links go in a comment or as an `<a>` in `html_notes`.
- The GitHub integration links a PR when the task URL is in the PR
  description, and syncs PR status to the task (unverified).

## States and transitions

- State = **section** (list header or board column) in the project, or
  an enum custom field (paid). Sections always work; custom fields do
  not exist on free workspaces.
- A task's section is in its `memberships` property: one section per
  project, and a task can be in several projects. Read state from the
  mapped project's membership only. Moving state means adding the task
  to another section of that project.
- Done is a separate `completed` flag on the task, apart from the
  section. There is no native canceled. Onboarding maps `done` and
  `canceled` to a section **and** the flag, or records a Gap.
- An enum custom field is set by option GID, not by option name. Each
  option has `gid`, `name`, and `enabled`; the task's value is in
  `enum_value`.
- Onboarding maps each section (or option) to a canonical state; names
  go only into the repo skill's Mapping cells.

## Gotchas

- Listing a project's tasks omits subtasks not added to it. The repo
  skill adds each item subtask to the project, or lists by parent.
- Merge automation that completes a task (GitHub Actions, rules) can
  mark it done before landed+verified; report it as a gap
  (unverified).
- Custom fields are paid. The error a free workspace returns is not
  documented; the vendor says to program defensively.
- Task search is paid too. On a free workspace, list tasks by
  project, section, or parent instead.
- Pagination: `limit` 1–100 (default 20); the next `offset` is in
  `next_page` (null on the last page). Offsets expire: page promptly.
  Unpaginated results truncate at about 1,000 objects.
- Rate limits: 150 requests per minute on free, 1,500 on paid; search
  60 per minute; at most 50 concurrent reads and 15 concurrent writes;
  a cost-based quota also applies. Over the limit: 429 with
  `Retry-After`. Rejected requests still count.
- Ids are long numeric GIDs, no human key; `item/<ticket-id>-<slug>`
  carries the task GID. Parse either URL shape for the task GID.

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
- A long number in a branch name is weak alone; confirm with an
  `app.asana.com` URL or the operator's statement.

## Sources

- https://developers.asana.com/docs/using-asanas-mcp-server
- https://developers.asana.com/docs/connecting-mcp-clients-to-asanas-v2-server
- https://developers.asana.com/docs/mcp-tools-reference
- https://developers.asana.com/docs/personal-access-token
- https://developers.asana.com/docs/object-hierarchy
- https://developers.asana.com/reference/tasks
- https://developers.asana.com/reference/sections
- https://developers.asana.com/docs/custom-fields-guide
- https://developers.asana.com/reference/adddependenciesfortask
- https://help.asana.com/s/article/task-dependencies?language=en_US
- https://developers.asana.com/docs/rich-text
- https://developers.asana.com/docs/pagination
- https://developers.asana.com/docs/rate-limits
- https://help.asana.com/s/article/github-and-asana-integration?language=en_US
- https://asana.com/apps/github
- https://forum.asana.com/t/upcoming-new-v1-asana-url-format-in-the-browser/1011489
- https://github.com/roychri/mcp-server-asana
