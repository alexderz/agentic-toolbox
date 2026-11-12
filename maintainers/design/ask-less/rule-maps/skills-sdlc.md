# Rule map — `skills/sdlc` (A1)

Item: DER-733 (A1 of DER-712).

Old: `docs/SDLC.md` at main c26f424, lines 1–174. New: `skills/sdlc/SKILL.md`.

Key: **kept** (same rule), **route** (the owner holds it; this file
links it), **replaced** (the accepted A1 text is the rule),
**reconciled** (each part moves to the owner the cell names),
**dropped** (owner named in New location).

Rows old L104–146, except L109, are the A1 dispositions. L109 is the
heading those rows skip; it is a non-blank line, so it is mapped
**kept**. Old L15–17 is edit 1. The row after old L170 is edit 4.
Protected `#roles` and `#tracker` sit in old L18–103 and stay **kept**,
untouched. `CHANGELOG.md` carries the one A1 line under `## Unreleased`;
it is not agent text and has no rows here.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–14 | Title through How to read steps 1–2 | kept | unchanged by A1 (A0 moved the file) |
| 15–17 | Manager also reads branches-and-lands and subagents | kept; also read liaison.md | How to read step 3 |
| 18–103 | Roles, Names, Tracker, Grain through the split-from-Spec bullets. Includes protected `#roles` and `#tracker` | kept | unchanged by A1 |
| 104–105 | Build finds a shape change → ask the operator | replaced (W4) | `#escalation` |
| 107 | Anchor | kept | `#asking-the-human` |
| 109 | Heading Asking the operator | kept | `## Asking the operator` under `#asking-the-human` |
| 111–113 | Ticket id plus slug | route (R96) | `ask-human.md` question line |
| 115–117 | A decision needs the operator | replaced (A1) | three-pile table |
| 118 | Stop and say so; do not hide the ask | route | `ask-human.md`: questions first |
| 119–121 | Template `ask-human.md`, fill every part | kept | first paragraph |
| 122–123 | Everyday words | route (R96) | `ask-human.md` question line |
| 124 | Recommendation and why | route (R96) | `ask-human.md` "I recommend" line |
| 125–126 | One question per message; number several | replaced (A1, L4) | one batch, each item by ask id (`ask-human.md`) |
| 127 | Wait | replaced (W1) | While a question is open |
| 129–132 | Required asks | reconciled (A2, A3, W4, R13, R75) | approvals → Touchpoints 1 and 3; waiving a check, Ask-first row → Always theirs; money, destructive → one-way row; open blocker, three failed fixes → Escalation triggers |
| 134–135 | Never "Please advise." … | kept | first paragraph ("never a bare LGTM?") |
| 136 | Never proceed after silence | replaced (L6, W1) | Answers; While a question is open |
| 138–141 | The wait blocks that issue; others move | kept | While a question is open 1–2 |
| 142–146 | AFK pick between two item fixes | dropped (T2) | Auto mode; item Brief step 4 two-way row |
| 148–174 | Steps section | kept; one new row after old L170 | Steps |
| — | Manager: liaison: asks from agents, one batch, push and pull | new | Steps table, after Manager: subagents |

## Meaning questions

No open MQ. The replaced, dropped and reconciled rows are the accepted
A1 dispositions.
