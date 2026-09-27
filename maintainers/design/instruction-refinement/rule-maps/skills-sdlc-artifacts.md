# Rule map — `skills/sdlc-artifacts/SKILL.md`

Item: DER-311 (D3).

Old: `skills/sdlc-artifacts/SKILL.md` at main 7a11696, lines 1–72.
New: [`skills/sdlc-artifacts/SKILL.md`](../../../../skills/sdlc-artifacts/SKILL.md).
Disposition: **kept** (same rule, this file), **route** (the rule lives in
its owner; this file links it), **dropped** (duplicate, owner named),
**DER-265**, **DER-271**. "Old L" = line in the old file; "L" = line in
the new file. Wording only: no template shape changes (K6).

Protected rows touched: none. Operator clarifications (2026-09-27): "a
person" does not occur; the other subjects do not occur in this file.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–4 | Front matter: name, description (when to use, when not) | kept verbatim | L1–4 |
| 6 | Title | kept | L6 |
| 8–10 | Templates are fill-in shapes; process lives in `docs/SDLC.md`; copy a template, do not paste the SDLC; no `scripts/` | kept verbatim; the link resolves to the SDLC index | L8–10 |
| 12–15 | Iron law: one template per artifact; fill every required field or `n/a` and why; no parallel outline | kept verbatim, still first | L12–15 |
| 17–36 | Map heading and rows through Changelog | kept verbatim | L17–36 |
| 37 | PR / land lands in "PR body or merge message" | kept; "merge message" → "land commit message" (one name: the index says "land commits") | L37 |
| 38–39 | Monthly, Human doc rows | kept verbatim | L38–39 |
| 40 | Ask the human: "The message to the person" | kept; "the person" → "the operator" (index `#roles` names the person in the loop **operator**) | L40 |
| 41–42 | AGENTS stub, Repo tracker skill rows | kept verbatim | L41–42 |
| 44–46 | Always heading; copy the file, delete unused optional sections, keep required ones | kept verbatim | L44–46 |
| 47–48 | Link the layer above and below; changelog line cites ticket + "land SHA or PR" | kept; "land SHA or PR" → "the ticket ID and the land SHA" (MQ1) | L47–48 |
| 49–52 | The orchestrator files a ticket body with `create`, later fields or a design path with `comment` (no edit verb), blockers with set-blocker, not only as text | writer rule → route to `docs/SDLC.md#tracker` (item 2, "Only the **manager** writes to the tracker"); "orchestrator" → "manager" (banned name, K3); the filing verbs kept | L49–52 |
| 53 | Dates ISO-8601; slugs lowercase hyphen | kept verbatim | L53 |
| 55–58 | Ask first: new artifact type not in the map; skipping a required field other than `n/a` + why | kept verbatim | L55–58 |
| 60–66 | Never: second outline; cloning the brief; empty acceptance or trust-boundary section; language skills on a templates-only turn | kept verbatim | L60–66 |
| 68–72 | Red flags | kept verbatim | L68–72 |

## Meaning questions

- **MQ1** — does dropping "or PR" change what a changelog line cites?
  Resolved from text: `docs/sdlc/conventions.md#changelog-and-connection`
  (owner) says "Changelog line | ticket ID + land SHA", and
  `docs/sdlc/branches-and-lands.md#land-path` lands by local merge with
  no PR. The HLD and LLD area D3 name this change. No open MQ.

## DER-344 (G51)

Wording fixes from the integrated check DER-339. Changed lines only.
Old = project-main 44d6842; "Old L" = line there; "L" = line in the new
file. No rule changes meaning.

| Old L | Change | Why | L |
| --- | --- | --- | --- |
| 38 | Monthly lands in "Ticket or `docs/monthly/`" → "`docs/monthly/`, or a Task once filed" | F7: matches owner `trunk-changelog-monthly.md#monthly` (a recurring note until the manager or operator files a Task) | L38 |
| 40 | Row name "Ask the human" → "Ask the operator"; template path kept | F10: index `#roles` names the person in the loop **operator** | L40 |
