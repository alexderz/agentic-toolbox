# Change map (light pass) — `skills/modern-web-guidance/`

Item: DER-755. Vendor-derived skill: SOURCES Upstream names GoogleChrome/modern-web-guidance,
so this is a light-pass change map per `maintainers/writing-standard.md` Rule maps step 6.

Old: upstream `skills/modern-web-guidance/` at 4dd968349e54ca45a05dd5c818fb035c9054b022
(`SKILL.md` lines 1–91; 209 guides). New: `skills/modern-web-guidance/` (new skill id).

## Entry `SKILL.md` (toolbox rewrite, not a paste)

| Upstream L | Content | Disposition (intake id) |
| --- | --- | --- |
| 1–3 | Frontmatter name, description | changed: new description in toolbox form (R1) |
| 4 | "MANDATORY: Execute FIRST" priority claim | dropped (R1) |
| 5–6 | Trigger and do-not-trigger lists | kept in new words: When to load steps 2–4 (R1, R10) |
| 11 | Purpose sentence | changed: intro and Actors |
| 13–37 | `npx` search and retrieve workflow | dropped (R1); replaced by Lookup over the local index (R4) |
| 39 | Large-output temp-file note | dropped (R1) |
| 41–46 | Builder self-check; no unrequested features | kept as Self-check, marked not a replacement for verifier, reviewer, security (Ask less §4) |
| 48–54 | `### Modern Web Guidance` response contract | dropped (R1); Never row forbids re-adding it |
| 56–70 | `legacy-scan` flow | dropped (R1) |
| 72–76 | `npx`/`pnpx`, allowlist, `NPM_CONFIG_CACHE`, `--offline` | dropped (R1); Never row |
| 80 | "preferred local standard" claim | dropped (R1); Iron law states guides are reference data |
| 81–84 | Framework adaptation tips | kept in new words, minus the `as any` recipe (R1); typed declaration instead |
| 88–89 | Browser support default and custom policies | kept: Decisions table rows (R1, Ask less §4) |
| 90 | Suggest writing a policy into `AGENTS.md`/`CLAUDE.md` | dropped (R1); Never row, log a ruling instead |
| — | Precedence list | added (R2, corrected by the item brief: Never and security bind first) |
| — | Decisions table: developer asks, browser policy, product consent, covered topics | added (R6, R7, Ask less §4) |
| — | Dependencies and third-party loads | added (R5) |
| — | Experimental status: Origin Trial token is the operator's; WebMCP early preview | added (R7) |
| — | Attribution | added (R8) |

## `index.md` (new)

209 rows, id → path → one line (R4). 203 lines adapted from upstream `README.md` (first
sentence of each entry); 6 toolbox-written lines for `accessibility`, `prompt-api`, `forms`,
`html`, `performance`, `security`, which that README omits. `verify-email-ownership` marked as
needing an Origin Trial token (R7); `webmcp` marked early preview.

## `guides/` (209 files)

Byte-identical to the pin except one mechanical rewrite (R3): each
`` `npx -y modern-web-guidance@latest retrieve "<id>"` `` became `[<id>](<relative path>)`,
resolved by unique file stem. 198 references, 164 lines, 65 files, 99 ids, none missing.
`guides/NOTICE.md` added (R8).

## `LICENSE` (new)

Apache-2.0 header naming the pin and scope (entry and index only), then the full upstream
Apache-2.0 text (R8).

## Meaning questions

None open. The precedence order follows the item brief's corrected R2 (manager ruling selecting
the troubleshooter's fix): R2's prose order is not read as letting a brief override a Never row.
