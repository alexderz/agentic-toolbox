# Change map — `skills/golang-security/SKILL.md`

Item: DER-328 (F, light pass). Vendor-derived: samber/cc-skills-golang.

Old: `skills/golang-security/SKILL.md` at main 7a11696, lines 1–155.
New: [`skills/golang-security/SKILL.md`](../../../../skills/golang-security/SKILL.md).
Light pass: changed lines only. 155 lines old, 155 new. No new upstream
text; no upstream fetch. Every security rule keeps its meaning.

Protected rows touched: none. Operator clarifications (2026-09-27): none
of their subjects occur in this file.

| Old L | Change | Why | New L |
| --- | --- | --- | --- |
| 10 | "Pairs with `golang-testing` (race/fuzz proof) and `golang-safety` (…)" → one route to [`language-router`](../../../../skills/language-router/SKILL.md#map), which picks one Go skill per turn | Dedupe: which Go skill loads is a `language-router` rule. The scope split stays at old L119 ("Not this skill"); race proof stays at L39 and L50 | L10 |
| 10 | "Do not install the samber pack." dropped | Dedupe: Never row old L71 keeps it; red flag old L149 also names it | — |
| 10 | "Separate PRs OK." | kept verbatim | L10 |
| 139 | "Workers do not bypass." → "Workers do not bypass **security**; see [Roles](../../../../docs/SDLC.md#roles)." | Defect: the sentence had no object. Owner `docs/SDLC.md#roles` says "They do not bypass **security**"; this line routes there | L139 |

`SOURCES.md` row `golang-security`: Notes cell appends the LLD note
`Wording edit DER-288, pins unchanged; security-cleared 2026-09-27.`
SHA, Upstream, License cells and pins unchanged.

## Meaning questions

None.
