# Rule map — `skills/sdlc-artifacts/templates/changelog.md`

Item: DER-311 (D3).

Old: `skills/sdlc-artifacts/templates/changelog.md` at main 7a11696, lines 1–23.
New: [`skills/sdlc-artifacts/templates/changelog.md`](../../../../skills/sdlc-artifacts/templates/changelog.md).
Disposition: **kept**, **route**, **dropped** (owner named), **DER-265**,
**DER-271**. "Old L" = line in the old file; "L" = line in the new file.
Headings and section order unchanged (K6).

Protected rows touched: none. Operator clarifications (2026-09-27): none
of their subjects occur in this file.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1 | Title | kept | L1 |
| 3–4 | Newest first; skip empty sections; board, git and this file agree "(see SDLC Conventions)" | kept; the prose name → the path `<skills-home>/docs/sdlc/conventions.md#changelog-and-connection` (LLD Links: `templates/changelog.md` L4). Code form, not a link: the template is copied into a product repo | L3–4 |
| 6–16 | Unreleased heading, four section headings; Added line `(<ticket-id>, <PR or SHA>)` | kept; `<PR or SHA>` → `<land SHA>` (MQ1) | L6–16 |
| 18 | Dated chunk heading | kept | L18 |
| 20–21 | Changelog step: move Unreleased lines here; link tickets and the Trunk merge "(or the item's trunk SHA if there was no project-main)" | kept; the condition leaves the parenthesis (standard 8): "If there was no project-main, link the item's land SHA." With no project-main the item lands on trunk, so its trunk SHA is its land SHA (MQ2) | L20–21 |
| 23 | Promoted line `(<ticket-id>, <merge SHA>)` | kept; `<merge SHA>` → `<land SHA>` (MQ1) | L23 |

## Meaning questions

- **MQ1** — is `<land SHA>` the same thing the old placeholders meant?
  Resolved from text: `docs/sdlc/conventions.md#changelog-and-connection`
  (owner) says "Changelog line | ticket ID + land SHA"; the HLD row D and
  LLD area D3 name `<merge SHA>` → `<land SHA>`. The chunk heading still
  links the Trunk merge (L20–21). No open MQ.
- **MQ2** — does "the item's land SHA" differ from "the item's trunk
  SHA"? Resolved from text: `docs/SDLC.md#names` "landed+verified …
  When trunk was the land target: merged onto trunk"; with no
  project-main, `docs/sdlc/branches-and-lands.md#land-path` Land row
  merges the item into trunk. Same commit. No open MQ.
