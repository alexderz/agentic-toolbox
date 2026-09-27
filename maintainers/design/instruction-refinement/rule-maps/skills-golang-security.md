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
| 135 | Builder row "pairing `golang-testing` / `golang-safety`" → "loading the one Go skill `language-router` picks"; rest of row kept | Dedupe: "pairing" contradicted the L10 route (one Go skill per turn) | L135 |
| 139 | "Workers do not bypass." → "Workers do not bypass **security**; see [Roles](../../../../docs/SDLC.md#roles)." | Defect: the sentence had no object. Owner `docs/SDLC.md#roles` says "They do not bypass **security**"; this line routes there | L139 |

`SOURCES.md` row `golang-security`, Notes cell only:

| Old | New | Why |
| --- | --- | --- |
| "pairs with golang-testing / golang-safety" | "language-router picks it, golang-testing or golang-safety, one per turn." | Matches the L10 route |
| — | appends `Wording edit DER-288, pins unchanged; security-cleared 2026-09-27.` | LLD vendor-derived note |

SHA, Upstream and License cells and pins unchanged.

## Meaning questions

None.

## DER-344 (G51)

Wording fixes from the integrated check DER-339. Changed lines only.
Old = project-main 44d6842; "Old L" = line there; "L" = line in the new
file. No rule changes meaning.

| Old L | Change | Why | L |
| --- | --- | --- | --- |
| 10 | "Separate PRs OK." → "Each Go concern may be its own item." | F1: internal lands use no PRs; the split is per item | L10 |

SOURCES row unchanged.
