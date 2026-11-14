# Rule map — `maintainers/writing-standard.md`

Item: DER-740 (G9, source item A8 of DER-712). A later item that edits this file appends its own
section.

Old: `maintainers/writing-standard.md` at main c26f424, lines 1–150.
New: [`maintainers/writing-standard.md`](../../../writing-standard.md).
Key: **kept** (same rule, same place), **route** (the rule lives in its owner; this file links it),
**dropped** (owner named), **changed** (with the brief, ruling or LLD id that decides it). "Old L"
= line in the old file. Design: [LLD A8](../lld.md#a8--writing-standard-and-maintainer-rules) and
[overlay G9](../opus-rebuild.md#g9--writing-standard-and-maintainer-rules-a8).

A0 (DER-730) rewrote paths in this file without moving any line, so each Old L below is also the
line number on the item's base tip. A0's path rewrites are recorded in its
[path map](a0-path-map.md), not here.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1 | Title | kept | L1 |
| 3–4 | Write agent text to these rules; source DER-288 HLD and LLD | kept | L3–4 |
| 6 | `## Names` | kept | L6 |
| 8–9 | Agent text (`$AT`) list | changed (LLD A8 edit 1; HLD A0 item 6): one line; `skills/` holds the SDLC | L8 |
| 10 | Old; Old L; SDLC index | changed (R163; overlay G9 edit 11): Old is the chunk's base commit | L9 |
| 11–15 | Owner, Route, Rule map, MQ definitions | kept | L10–14 |
| 17–18 | SDLC index `#names` defines names; write the Use name | kept | L16–17 |
| 20–25 | Banned names table | kept | L19–24 |
| 27 | `## Standard` | kept | L26 |
| 29–46 | Standards 1–8 | kept | L28–45 |
| 47–53 | Standard 9: caps; growth; new files; drops | changed (R45, R48, R164; overlay G9 edit 2): SDLC index cap 250; a rewrite may grow to its cap; never drop a rule to fit a cap; an operator-asked drop is raised per `#asking-the-human` | L46–52 |
| 54–55 | Standard 10: rule map per edited agent file | kept | L53–54 |
| 57 | `## Rule owners` | kept | L56 |
| 59–63 | Table header; roles, tracker, security rows | kept | L58–62 |
| 64 | When to ask the operator; AFK pick | changed (HLD "Retired" AFK row; R166; overlay G9 edit 3): AFK pick retired; rulings, guardrails, auto mode, escalation, touchpoints added with full paths | L63 |
| 65 | Ask message shape | changed (LLD A8 edit 4): batch and touchpoint shape added | L64 |
| — | Liaison; asks file; `needs_input` pointer | changed, new row (LLD A8 edit 5; R166; overlay G9 edit 5) | L65 |
| — | Refiner job; three buckets; defer, don't delete | changed, new row (LLD A8 edit 5) | L66 |
| 66–81 | Other owner rows | kept | L67–82 |
| 83–98 | `## Protected rules`, its intro and table | kept | L84–99 |
| 100 | `## Rule maps` | kept | L101 |
| 102, 104 | Step 1: one map per edited agent file; slug rule | kept | L103, L105 |
| 103 | Step 1: rule-map folder | changed (R44; LLD A8 edit 6): the chunk's own folder | L104 |
| 105 | Step 2: header | changed (R44; LLD A8 edit 7): the chunk base commit | L106 |
| 106 | Step 3: key | changed (R163; overlay G9 edit 12): **changed** added, never on a Protected rule; DER-265, DER-271 kept for DER-288 maps | L107 |
| 107–108 | Step 4: table shape | kept | L108–109 |
| 109–110 | Step 5: Meaning questions | changed (R162; overlay G9 edit 13): resolved by a cited design line or by the operator | L110–111 |
| 111–113 | Step 6: light passes | kept | L112–114 |
| 115–117 | MQ paragraph | changed (R162 as amended by R188; overlay G9 edit 14): a protected-rule MQ stops the item, keeps the old text and raises an Always-theirs ask; any other MQ resolves by step 5 or is raised per `#asking-the-human` | L116–118 |
| 119–123 | Operator clarifications (2026-09-27) | kept | L120–124 |
| 125 | `## Checks` | kept | L126 |
| 127 | K1 caps | changed (R165; overlay G9 edit 15): the files the item or chunk rewrote or added | L128 |
| 128–129 | K2 never grow | changed (R64; LLD A8 edit 8): retired; growth checked by K1 | L129 |
| 130–136, 138 | K3–K5; K6 tracker-skill diff and contract version | kept | L130–136, L138 |
| 137 | K6 template shapes | changed (R92; LLD A8 edit 9): `ask-human.md` and `asks.md` exempt | L137 |
| 139–144, 146–147 | K7–K9; K10 intro and outcome | kept | L139–144, L146–147 |
| 145 | K10 pattern | changed (R87; LLD A8 edit 10): also matches `xai-` keys | L145 |
| 149–150 | Every item's set; integrated check | kept | L149–150 |

The Protected rules table (old L88–98) is **kept**: no row changed.

## Meaning questions

None. Each changed row is decided by the ruling or LLD edit it cites; no protected rule changed.
