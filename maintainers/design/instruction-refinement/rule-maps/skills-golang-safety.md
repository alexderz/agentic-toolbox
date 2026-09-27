Old: skills/golang-safety/SKILL.md at main 7a11696, lines 1–173. New: skills/golang-safety/SKILL.md.

Light pass (vendor-derived, DER-329): change map, changed lines only. Also
`SOURCES.md` row `golang-safety`, Notes cell only: "pair golang-testing +
golang-security" → "do not merge with golang-testing or golang-security"
(same fix as L26), and the note `Wording edit DER-288, pins unchanged;
security-cleared <YYYY-MM-DD>.` appended. Upstream, SHA and License cells
unchanged.

Key: **kept**, **route**, **dropped** (owner named), **fix** (real defect).

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 10 | Attackers → `golang-security`, `security-hardening`; proof → `golang-testing`, `tdd`; "(separate PR)" | **dropped** (owner `language-router` `#map` and `#load-with-list`; routed at New L26); stale "(separate PR)" removed; "SKILL only. Safety is *our* bugs." **kept** | L10 |
| 26 | "Pair, do not merge the three Go skills"; attackers and proof stay in their skills | **kept** (do not merge), now naming `golang-testing`, `golang-security`, `golang-safety`; "Pair" **fix** (contradicts `language-router` iron law: one language skill per turn); which Go skill loads → **route** to `language-router` `#map` | L26 |
| 80–82 | Typed-nil example | **fix**: unused `var h *MyHandler` does not compile (declared and not used); line removed; comment reads "return plain nil; a nil *MyHandler in an interface is != nil" | L79–81 |
| 92 | Nil map Len/cap = 0 | **fix**: `cap` is not defined on a map; cell reads `` `len` 0; no `cap` `` | L91 |

Lines 173 → 172. No upstream text added; upstream pin line (L173 old) unchanged.

## Meaning questions

None.
