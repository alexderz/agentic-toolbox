# Change map — `skills/docs-google-style/SKILL.md`

Item: DER-324 (F, vendor-derived light pass). Changed lines only.

Old: `skills/docs-google-style/SKILL.md` at main 7a11696, lines 1–74.
New: `skills/docs-google-style/SKILL.md`, lines 1–70.

| Old L | Change | Kind | New L |
| --- | --- | --- | --- |
| 31 | `` `i.e.` `&` `` → `` `i.e.`. `&` ``: two banned items ran together without a separator | real defect | 31 |
| 69 | `Don’t` (curly apostrophe) → `Don't`, matching the skill's own `don't` at L46 | real defect | 69 |
| 71–74 | `## Source` dropped: its URL repeats the L8–9 link; "distill, not a verbatim paste" repeats L8 "Distillation of" and L69–70 "Don't copy the guide entry-by-entry" | dedupe | — |

No new upstream text; no upstream fetch. Upstream link at L8–9 kept.
No banned name was found (K3 empty), so no naming change.

## `SOURCES.md`

Only the `docs-google-style` row's Notes cell changes. Upstream, SHA
and License cells are unchanged.

| Old | New |
| --- | --- |
| `Human how-tos + agent-facing comments. Not a vendor paste` | `Human how-tos + agent-facing comments. Not a vendor paste. Wording edit DER-288, pins unchanged; security-cleared 2026-09-27.` |

## Meaning questions

None. No change touches a role, gate, step, tracker verb, state,
template shape, operator approval or protected rule.

## Checks

- K2: 70 ≤ 74.
- K3: empty.
- K7: one link, `https://developers.google.com/style`, unchanged; the
  template path `skills/sdlc-artifacts/templates/human-doc.md` exists.
- K10: no added line in `SKILL.md` matches. The `SOURCES.md` row matches
  once: the upstream URL, already in the SHA cell, which K10 allows.
- Security: reads the new body at Review; the `security-cleared` date is
  the date of that read.
