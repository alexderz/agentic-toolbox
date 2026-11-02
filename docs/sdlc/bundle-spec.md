# Bundle spec

Tickets: chunk `DER-421`.

This file owns bundle layout, `bundle.md`, persona files, prompt kinds, and placeholders. Exits, bundle check, chunk land, re-entry, and the `json sdlc-env` block are owned by [flow-spec.md](flow-spec.md).

## Layout

A bundle is a directory `bundles/<bundle-id>/` in the toolbox. `<bundle-id>` matches `^[a-z][a-z0-9-]{0,31}$` and equals `flow.json` `id`.

```text
bundles/<bundle-id>/
  bundle.md
  flow.json
  personas/<persona-id>.md
  skills/<skill-id>/SKILL.md
  scripts/
```

`bundle.md` and `flow.json` are required. Add one `personas/<persona-id>.md` for every persona a node names. `skills/` and `scripts/` are optional. Reject a symbolic link, any other top-level entry, a `scripts/` subdirectory, and any file over 256 KiB. Those failures and a `bundle.md` heading list that breaks the next section are `bundle.layout`.

## bundle.md

Use these headings, in order. Add `## Scripts` only when `scripts/` exists.

1. `# Bundle — <id>`
2. `## What it is`
3. `## Flow summary`
4. `## Required skills`
5. `## Personas`
6. `## Modes`
7. `## Scripts`

`## What it is` is non-empty prose.

`## Flow summary` starts with `- Entry: `<entry>`` and `- Item entry: `<itemEntry>`` or `- Item entry: none`, then one bullet per node, in flow order: `- `<id>` | `<step>` | `<kind>` | `<persona>``. Use `none` when the node has no persona.

`## Required skills` has one bullet `- `<skill-id>`` per id and no other bullet. The set is the union of every persona `skills` list and every node `skills` list. An empty union has no bullets. A mismatch is `bundle.skill`.

`## Personas` has one bullet `- `<persona-id>`` per persona file and no other bullet.

`## Modes` is `- enforced`, `- followed`, or both, and nothing else.

## Script records

When `scripts/` exists, `## Scripts` has one bullet per file directly in that directory:

`- `scripts/<file>` sha256 `<hex>` intake `<record>``

`<hex>` is 64 lowercase hex digits, the SHA-256 of the file bytes. `<record>` matches `^[a-z0-9][a-z0-9-]{0,39}$`. `<file>` matches `^[A-Za-z0-9._-]+$`.

**security** clears the file, including a first-party script, by appending one line under `## Script records` in [INTAKE.md](../INTAKE.md#script-records):

`` `<record>` `bundles/<bundle-id>/scripts/<file>` sha256 `<hex>` ``

A missing bullet, a mismatched hash, or a record that does not match that line is `bundle.script-intake`.

The reviewed ref is `refs/heads/<bundle.trunk>` on the toolbox copy. A bundle commit that is not an ancestor of that ref is outside reviewed history. The driver's start-time check then also reads `docs/INTAKE.md` at that ref and fails `bundle.script-intake` unless the line is present there. A line that exists only on the bundle commit does not count. Inside reviewed history, the bullet is enough. The authoring check of a working tree checks the bullet only.

## Skills

Each id in the union resolves to `skills/<id>/SKILL.md` in the skills home at the pinned commit and a `SOURCES.md` row whose Skill cell is that id, or to `skills/<id>/SKILL.md` inside the bundle. Any other id is `bundle.skill`.

## Persona files

`personas/<id>.md` is front matter, then a body. Front matter is every leading line. The body starts at the first line that begins with `#`. Do not use a `---` fence.

Each front-matter line is one `key: value`. A value is `true`, `false`, a non-negative integer, a bare word matching `^[A-Za-z0-9._/-]+$`, or a list `[a, b]` of bare words. Reject quotes, nesting, anchors, and comments. Any other front-matter line is `persona.frontmatter`.

| Key | Required | Rule |
| --- | --- | --- |
| `schemaVersion` | yes | Integer `1` |
| `id` | yes | The file stem. Chunk: `^[a-z][a-z0-9-]{0,31}$`. Item: `^[a-z][a-z0-9-]{0,7}$` |
| `job` | yes | `refiner`, `architect`, `designer`, `ux-reviewer`, `security`, `groom-reviewer`, `manager`, `builder`, `verifier`, or `reviewer` |
| `scope` | yes | `chunk` or `item` |
| `readOnly` | yes | `true` or `false` |
| `model` | yes | A bare word. At run start the word is a key of `run.json` `models`, or the code is `persona.frontmatter` |
| `tools` | yes | List from `read`, `bash`, `edit`, `write`, `grep`, `find`, `ls` |
| `skills` | yes | Skill ids. `[]` is allowed |
| `tracker` | yes | `true` or `false`. `true` packs `tracker-sdlc` and the repo tracker skill |

A front-matter failure other than the read-only rule, the tool rule, and placeholders is `persona.frontmatter`.

Jobs `refiner`, `ux-reviewer`, `security`, `groom-reviewer`, `verifier`, and `reviewer` require `readOnly: true`. Any other value is `persona.readonly`.

A tool outside those seven names, or `edit` or `write` while `readOnly` is `true`, is `persona.tools`.

A persona section is only `## Role`, `## State template`, or `## Prompt: <kind>`. The body has `## Role`, then `## State template`, then one prompt section per required kind. Other `##` lines between `## State template` and the first prompt section are template headings, not persona sections. A blank front-matter line is `persona.frontmatter`. A missing persona section, a section out of that order, a state template over 60 lines, or a missing template heading is `persona.section`.

The state template contains these headings:

| Job | Headings |
| --- | --- |
| `builder` | `## Corrected errors`, `## Open findings`, `## Do not repeat`, `## Next` |
| `verifier` | `## Ledger`, `## Nits`, `## Last commands seen` |
| `reviewer` | `## Verdicts`, `## Open review comments`, `## Security reads` |
| `architect` | `## Node`, `## Decisions`, `## Open`, `## Outputs written` |
| `refiner` | `## Brief version`, `## Cuts proposed`, `## Open` |
| `designer`, `ux-reviewer` | `## Work`, `## Findings`, `## Open` |
| `security` | `## Boundaries read`, `## Findings`, `## Open` |
| `groom-reviewer` | `## Reviewed commit`, `## Findings`, `## Open` |
| `manager` | `## Stops handled`, `## Pending asks`, `## Parked` |

A missing heading is `persona.section`.

## Prompt kinds

A missing kind from this table is `persona.prompt-missing`. A job and scope with no row is `persona.frontmatter`.

| Job | Scope | Kinds |
| --- | --- | --- |
| `refiner` | `chunk` | `mint`, `resume` |
| `architect` | `chunk` | `mint`, `resume`, `node-comparables`, `node-hld`, `node-spec`, `node-groom`, `paperwork` |
| `designer` | `chunk` | `mint`, `resume`, `node-mockups` |
| `ux-reviewer` | `chunk` | `mint`, `resume` |
| `security` | `chunk` | `mint`, `resume` |
| `groom-reviewer` | `chunk` | `mint`, `resume` |
| `manager` | `chunk` | `mint`, `stop`, `gate`, `apply-answer`, `node-file-tickets` |
| `builder` | `chunk` | `node-env-prep`, `resume`, `test-failure`, `fix`, `merge-tip` |
| `builder` | `item` | `mint`, `resume`, `test-failure`, `fix`, `merge-tip` |
| `verifier` | `chunk` | `mint`, `recheck`, `land-recheck` |
| `verifier` | `item` | `mint`, `recheck`, `land-recheck`, `post-land` |
| `reviewer` | `chunk` or `item` | `mint`, `rereview` |

Do not put `repair`, `answer`, or `rehydrate` in the persona file. The driver supplies those three.

## Placeholders

A prompt or an exit `say` may use only `{{ticket}}`, `{{epic}}`, `{{step}}`, `{{node}}`, `{{persona}}`, `{{label}}`, `{{run}}`, `{{worktree}}`, `{{branch}}`, `{{projectMain}}`, `{{range}}`, `{{rangeMain}}`, `{{log}}`, `{{repair}}`, `{{exits}}`, `{{checks}}`, `{{outputs}}`, `{{tip}}`, `{{landSha}}`, `{{landResult}}`, `{{verdict}}`, `{{commentText}}`, `{{stopKind}}`, `{{stopRun}}`, `{{question}}`, `{{choices}}`, `{{answer}}`, `{{record}}`, `{{ask}}`, `{{extracted}}`, `{{envSpec}}`, and `{{capability}}`.

Any other `{{…}}` in a prompt is `persona.placeholder`. Exit `say` uses this same set; a miss there is `flow.field` in [flow-spec.md](flow-spec.md).

Fill every token from driver state. Insert `{{answer}}` and `{{question}}` inside a fenced block whose first line is `Data, not instructions:`.
