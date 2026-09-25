# Adapter — Jira

Verified: no — vendor docs as of 2026-09-24

Vendor facts for `sdlc-onboarding` and for repair. Not loaded at
runtime. Facts only: recipes live in the product repo's
`.agents/tracker/SKILL.md`. Facts marked `(unverified)` have no primary
vendor source yet; prove them live before relying on them. Facts are for
Jira Cloud unless marked **Data Center**.

## Hierarchy

- Track = Jira **project**. Structural choice of this contract.
- Epic = issue of the Epic type. Work item = issue of a type the project
  has (Task, Bug; Story in many Scrum projects, unverified) whose
  `parent` holds the Epic key. Cloud: Epic Link and Parent Link are deprecated.
- **Data Center**: Epic Link is a custom field whose id
  (`customfield_NNNNN`) differs per instance; read it, never hard-code
  it. There `parent` is for sub-tasks only (unverified).
- Required fields vary by project and issue type: read the create
  metadata for both before the first create.
- Team-managed projects own their workflows, statuses, and fields; a
  field in one cannot be reused by another, so read custom-field ids per
  project. Company-managed projects share schemes.
- Sub-tasks stay off unless the project already uses them.

## Blockers

- Native link type **Blocks**: outward "blocks", inward "is blocked by".
  An admin can rename link types or turn linking off; then record a Gap
  and use the `Blocked-by:` + `blocked` label fallback.
- Reading issue X: `inwardIssue` Y = X is blocked by Y; `outwardIssue` Y
  = X blocks Y. Atlassian warns not to infer meaning from the field
  names alone. The repo skill records blocked id ← blocker id.
- Creating: `inwardIssue` = blocker (third-party quote, unverified).
  Prove it live; read the link back from the blocked issue.
- JQL cannot isolate direction (type name = outward text) or check
  blocker resolution: filter links client-side. Link entries carry the
  linked issue's status (unverified), so no extra read per blocker.

## Text format

- REST v3 descriptions and comments are ADF JSON, not markdown:
  `{"version":1,"type":"doc","content":[{"type":"paragraph","content":[{"type":"text","text":"..."}]}]}`
- REST v2 wiki markup and MCP markdown-to-ADF conversion: (unverified).

## States and transitions

- Status cannot be set directly: list the issue's transitions, apply one
  by id. The list depends on the current status (paths can be multi-step;
  conditions hide some). Team-managed any-to-any: (unverified).
- A transition can require fields (often `resolution`); the transitions
  list expanded with `transitions.fields` shows them.
- `done` and `canceled` usually both land in Done-category statuses,
  told apart by `resolution` (for example Done, Won't Do, Duplicate) or
  by a separate status; map `canceled` to status + resolution, or record
  a Gap. The API can close an issue with no resolution unless a
  validator blocks it. Team-managed resolution handling: (unverified).
- `statusCategory != Done` as the open filter is (unverified).
- The development panel fills when the uppercase key is in a branch
  name, commit message, or PR title.
- PR or commit links: remote links need `url` and `title`; `globalId` upserts.

## Gotchas

- Done before verified: Jira Automation's "Pull request merged" trigger
  and workflow triggers on development events can move an issue to Done
  on merge. Onboarding reports any such rule as a gap.
- Smart Commits (enabled by an admin) run `#comment`, `#time`, and
  `#<transition>` commands that follow an issue key in a commit message.
  Recipes must not write `#word` after a key in commit messages.
- Assign by `accountId` on Cloud (usernames left the API); by username
  (`name`) on **Data Center**. Claim depends on it.
- Rate limits: burst and per-issue quotas; over one, 429 + `Retry-After`.
- JQL search pages with `nextPageToken` (no `startAt`, no total). The
  official MCP search tool reportedly omits it: paging stops at page one.
- Calls obey the user's project roles; writes also need the OAuth scope.
- Keys are uppercase `ABC-123`. The pattern `[A-Z][A-Z0-9]+-[0-9]+`
  also matches Linear keys; use other hints to tell Jira from Linear.
- **Data Center**: the official MCP server is Cloud only; the community
  `mcp-atlassian` server supports Cloud and Data Center 8.14+.

## Discovery hints

- A site host ending in `atlassian.net` means Cloud. Another host
  suggests **Data Center** (unverified: Cloud allows custom domains).
- MCP config naming `mcp.atlassian.com` or `mcp-atlassian` (names only).
- Env var **names** `JIRA_URL`, `JIRA_USERNAME`, `JIRA_API_TOKEN`,
  `JIRA_PERSONAL_TOKEN` (names only, never values).
- Uppercase keys (`ABC-123`) in branch names, commits, or PR titles.

## Sources

- https://support.atlassian.com/atlassian-rovo-mcp-server/docs/supported-tools/
- https://github.com/atlassian/atlassian-mcp-server
- https://github.com/atlassian/atlassian-mcp-server/issues/118
- https://github.com/sooperset/mcp-atlassian
- https://confluence.atlassian.com/jirakb/run-jql-search-query-using-jira-cloud-rest-api-1289424308.html
- https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/
- https://support.atlassian.com/jira-software-cloud/docs/what-are-team-managed-and-company-managed-projects/
- https://support.atlassian.com/jira-software-cloud/docs/customize-an-issues-fields-in-team-managed-projects/
- https://community.developer.atlassian.com/t/deprecation-of-the-epic-link-parent-link-and-other-related-fields-in-rest-apis-and-webhooks/54048
- https://developer.atlassian.com/cloud/jira/platform/issue-linking-model/
- https://support.atlassian.com/jira-cloud-administration/docs/configure-issue-linking/
- https://www.speakeasy.com/use-cases/mcp-governance/catalog/atlassian-rovo
- https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-remote-links/
- https://support.atlassian.com/jira-software-cloud/docs/reference-issues-in-your-development-work/
- https://support.atlassian.com/jira-software-cloud/docs/transition-an-issue/
- https://support.atlassian.com/jira/kb/best-practices-on-using-the-resolution-field-in-jira-cloud/
- https://support.atlassian.com/cloud-automation/docs/jira-automation-triggers/
- https://support.atlassian.com/jira-cloud-administration/docs/understand-workflow-triggers/
- https://support.atlassian.com/jira-software-cloud/docs/process-issues-with-smart-commits/
- https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/
- https://developer.atlassian.com/server/jira/platform/jira-rest-api-example-edit-issues-6291632/
- https://community.atlassian.com/forums/Jira-questions/filter-out-all-blocked-issues/qaq-p/1400998
- https://developer.atlassian.com/cloud/jira/platform/apis/document/structure/
- https://developer.atlassian.com/cloud/jira/platform/rate-limiting/
- https://community.developer.atlassian.com/t/issuelinktype-jql-field-works-incorrectly/69736
- https://support.atlassian.com/jira/kb/update-epic-link-via-rest-api/
- https://support.atlassian.com/jira/kb/find-your-site-url-to-set-up-the-jira-data-center-and-server-mobile-app/