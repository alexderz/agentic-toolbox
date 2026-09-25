# Adapter — Jira

Verified: no — vendor docs as of 2026-09-24

Vendor facts for `sdlc-onboarding` and for repair. Not loaded at
runtime. Facts only: recipes live in the product repo's
`.agents/tracker/SKILL.md`. Facts marked `(unverified)` have no primary
vendor source yet; prove them live before relying on them. Facts are for
Jira Cloud unless marked **Data Center**.

## Hierarchy

- Track = Jira **project**. Structural choice of this contract.
- Epic = issue of the Epic type. Work item = Task or Bug whose `parent`
  field holds the Epic key. Cloud: Epic Link and Parent Link are
  deprecated; reparenting shows in changelogs as `IssueParentAssociation`.
- **Data Center**: Epic Link is still a custom field whose id
  (`customfield_NNNNN`) differs per instance; read it, never hard-code it.
- Required fields vary by project and issue type. Read the create
  metadata for that project and type before the first create. The old
  all-projects create-metadata call is removed (Cloud, and **Data
  Center** 9.0+).
- Projects are team-managed (configured per project) or company-managed
  (shared schemes). How each exposes hierarchy and custom fields over
  the API is (unverified).
- Sub-tasks stay off unless the project already uses them.

## Blockers

- Native link type **Blocks**: outward text "blocks", inward text "is
  blocked by".
- Reading issue X: a link with `inwardIssue` Y means X is blocked by Y;
  `outwardIssue` Y means X blocks Y. Atlassian warns not to infer meaning
  from the field names alone. The repo skill records it one way:
  blocked id ← blocker id.
- Creating: `inwardIssue` = blocker, `outwardIssue` = blocked
  (third-party quote only, unverified). Prove it live; read the link
  back from the blocked issue.
- JQL cannot isolate one direction (the link type name equals the
  outward text), and cannot tell whether the linked blocker is resolved.
  Fetch the links and filter client-side for open blockers.

## Text format

- REST v3 descriptions, comments, and textarea fields are ADF JSON, not
  markdown. Minimal paragraph:
  `{"version":1,"type":"doc","content":[{"type":"paragraph","content":[{"type":"text","text":"..."}]}]}`
- REST v2 wiki markup and MCP markdown-to-ADF conversion: (unverified).

## States and transitions

- Status cannot be set directly. List the transitions available on the
  issue, then apply one by transition id.
- Workflows (and so status names) come from the project (team-managed)
  or its shared scheme (company-managed). Onboarding maps each status to
  a canonical state; names go only into the repo skill's Mapping cells.
- `statusCategory != Done` as the open filter is (unverified).
- The development panel fills itself when the uppercase issue key is in
  a branch name, commit message, or PR title. Smart commits must be
  enabled by an admin. Whether PR events move status is (unverified).
- PR or commit links: remote links need `url` and `title`; `globalId` upserts.

## Gotchas

- Rate limits: points-based quotas since 2026-03-02. Burst 100 req/s
  for GET and POST, 50 for PUT and DELETE; per issue, 20 writes per 2 s
  and 100 per 30 s. Over a limit: HTTP 429 with `Retry-After`,
  `X-RateLimit-*`, and `RateLimit-Reason`; wait for `Retry-After`.
  Documented for apps; whether they bind API-token or MCP users is
  (unverified). The official MCP server bills Rovo credits instead.
- JQL search pages with `nextPageToken` (no `startAt`, no total). The
  old search call is removed. The official MCP search tool is reported
  not to return the token, so paging stops at page one. Some users
  report endless token chains: cap the pages.
- Calls obey the user's project roles; writes also need the OAuth scope.
- Keys are uppercase `ABC-123`. The pattern `[A-Z][A-Z0-9]+-[0-9]+`
  also matches Linear keys; use other hints to tell Jira from Linear.
- **Data Center**: the official MCP server is Cloud only; the community
  `mcp-atlassian` server supports Cloud and Data Center 8.14+.

## Discovery hints

- A site host ending in `atlassian.net` means Cloud. Another host
  suggests **Data Center** (unverified).
- MCP config naming the host `mcp.atlassian.com` (official, Cloud) or
  the server `mcp-atlassian` (community). Host and server names only;
  read no other config value.
- Env var **names** `JIRA_URL`, `JIRA_USERNAME`, `JIRA_API_TOKEN`,
  `JIRA_PERSONAL_TOKEN`, `JIRA_AUTH_TYPE`, `JIRA_CONFIG_FILE` (names
  only, never values).
- A `~/.config/.jira/.config.yml` file (community CLI config): presence
  only; read host names only, never tokens.
- Uppercase keys (`ABC-123`) in branch names, commits, or PR titles.

## Sources

- https://support.atlassian.com/atlassian-rovo-mcp-server/docs/getting-started-with-the-atlassian-remote-mcp-server/
- https://support.atlassian.com/atlassian-rovo-mcp-server/docs/supported-tools/
- https://github.com/atlassian/atlassian-mcp-server
- https://github.com/atlassian/atlassian-mcp-server/issues/118
- https://github.com/sooperset/mcp-atlassian
- https://github.com/ankitpokhrel/jira-cli
- https://github.com/ctreminiom/go-atlassian/issues/319
- https://confluence.atlassian.com/jirakb/run-jql-search-query-using-jira-cloud-rest-api-1289424308.html
- https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/
- https://support.atlassian.com/jira-software-cloud/docs/what-are-team-managed-and-company-managed-projects/
- https://community.developer.atlassian.com/t/deprecation-of-the-epic-link-parent-link-and-other-related-fields-in-rest-apis-and-webhooks/54048
- https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-issue-reparenting-changelogs/
- https://developer.atlassian.com/cloud/jira/platform/issue-linking-model/
- https://www.speakeasy.com/use-cases/mcp-governance/catalog/atlassian-rovo
- https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-remote-links/
- https://support.atlassian.com/jira-software-cloud/docs/reference-issues-in-your-development-work/
- https://community.atlassian.com/forums/Jira-questions/filter-out-all-blocked-issues/qaq-p/1400998
- https://developer.atlassian.com/cloud/jira/platform/apis/document/structure/
- https://developer.atlassian.com/cloud/jira/platform/rate-limiting/
- https://community.developer.atlassian.com/t/issuelinktype-jql-field-works-incorrectly/69736
- https://community.atlassian.com/forums/Jira-questions/REST-The-new-rest-api-3-search-jql-endpoint-is-a-complete/qaq-p/3101716
- https://support.atlassian.com/jira/kb/update-epic-link-via-rest-api/
- https://jira.atlassian.com/browse/JRASERVER-74965
