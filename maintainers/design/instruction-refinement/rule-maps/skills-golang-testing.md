# Change map: skills/golang-testing/SKILL.md (DER-327, light pass)

Old: `skills/golang-testing/SKILL.md` at project-main 120d298 (= 7a11696 for this file, 186 lines). New: 184 lines.
Changed lines only. No upstream text added. Pin, SHA, license, tools unchanged.

| Old L | Change | Kind | New L | Where the rule lives now |
| --- | --- | --- | --- | --- |
| 8 | Dropped the provenance line (pin, "not verbatim", "not a pack install", "no evals/scripts/clawhub", id) | dedupe | — | Pin + MIT: `## Upstream pin` (new L184, unchanged); pack install: `## Never` row (new L59); evals/scripts/clawhub: `## Never` row (new L60); id: frontmatter `name` |
| 9 | Blank line dropped with L8 | — | — | — |
| 10 | "Pairs with `tdd` … `verify-before-done` … **builder owns.** Do not install the rest of the samber pack" → one route line to the load-with list | dedupe / route | 8 | Load-with: `skills/language-router/SKILL.md#load-with-list` (owner). `tdd` still named at new L66, `verify-before-done` at new L32. builder ownership: `## Roles` builder row (new L164). Pack install: `## Never` (new L59), `## Roles` (new L164) |
| 171 | "Workers do not bypass intake." → "Workers do not bypass **security**: [Roles](../../docs/SDLC.md#roles)." | naming / route | 169 | Owner `docs/SDLC.md#roles` (writing-standard Rule owners: "Workers do not bypass security"). Rest of the line unchanged |

## SOURCES.md

Only row `golang-testing` (L31), Notes cell: appended the LLD vendor-derived note
`Wording edit DER-288, pins unchanged; security-cleared <YYYY-MM-DD>.`
Upstream, SHA and License cells unchanged. `<YYYY-MM-DD>` is left for **security** to fill at Review.

## Checks

- K2: 184 ≤ 186 (`git show 7a11696:skills/golang-testing/SKILL.md | wc -l`); SOURCES.md line count unchanged.
- K3: no hit in the new file.
- K7: `../language-router/SKILL.md#load-with-list` (heading `## Load-with list`), `../../docs/SDLC.md#roles` (heading `## Roles`), `../../SOURCES.md` resolve.
- K10: no added line matches (no URL, host, path, port or token).

## Not changed, noted for review

- New L55 `stdversion` "Go 1.27+ default vet", L126 `httptest.NewTestServer`, L138 `synctest.Sleep`: version claims not verifiable without upstream; left as is (no fetch).
- New L112 condition in parentheses and L83 "genuinely unwieldy" fall under standard 2/8, outside a light pass.
