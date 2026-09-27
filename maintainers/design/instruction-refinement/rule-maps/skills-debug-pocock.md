# Change map — `skills/debug-pocock/SKILL.md`

Item: DER-322 (F, vendor-derived light pass).

Old: `skills/debug-pocock/SKILL.md` at main 7a11696, lines 1–35.
New: [`skills/debug-pocock/SKILL.md`](../../../../skills/debug-pocock/SKILL.md).
Light pass: changed lines only; every other line is unchanged. "Old L" =
line in the old file; "L" = line in the new file. 35 lines old, 35 new.

Protected rows touched: none. Operator clarifications (2026-09-27): none
apply. No new upstream text; SHA, license, tools and pins unchanged.

| Old L | Change | Kind | New L |
| --- | --- | --- | --- |
| 8 | "Rewrite of mattpocock/skills `diagnosing-bugs` @ `74ca5fe0`" dropped: L35 names the same upstream with the full pin; "Rewrite of" moves there | dedupe | 35 |
| 8 | "Compress, not a paste." dropped: "Rewrite of" at L35 states it | dedupe | 35 |
| 8 | "Load **one** debug skill." dropped: owner is `## Never` L29 and the description | dedupe | 29 |
| 8 | "No `scripts/`." dropped: owner is `## Never` L30 | dedupe | 30 |
| 8 | "**Alternative** to default `debug`." | kept | 8 |
| 12 | "You have already run that command once" stated a fact, not an instruction → "Run that command once and show its output before the first hypothesis." | defect | 12 |
| 12 | "(secrets redacted)" dropped: owner is `## Always` L25, "Redact secrets in anything you show" | dedupe | 25 |
| 35 | "Rewrite of " prepended; SHA and license unchanged | dedupe | 35 |

`SOURCES.md`: the `debug-pocock` Notes cell appends the LLD vendor-derived
note; Upstream, SHA and License cells unchanged.

## Meaning questions

None. No kept rule changes its condition or action.
