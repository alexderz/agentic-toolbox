# Rule map — `skills/sdlc/references/stage-result.md`

Item: DER-734 (A2 of DER-712).

Old: `docs/sdlc/stage-result.md` at main c26f424, lines 1–150.
New: [`skills/sdlc/references/stage-result.md`](../../../../skills/sdlc/references/stage-result.md).

Disposition key: **kept**, **route**, **dropped** (owner named), **DER-265**,
**DER-271**. "Old L" is a line at c26f424. A0 moved the file and rewrote
links. This map records A2. Edits are in place, so the line numbers match.
150 lines (cap 150).

Protected rows touched: none. Operator clarifications (2026-09-27): none of
their subjects occur in this file.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1 | Title | kept | L1 |
| 3 | Tickets DER-529 and DER-421 | kept | L3 |
| 5–14 | Stage, stage result, harness, command stage, model stage, evidence, reader, command wrapper | kept. A0 rewrote the Names link on old L6 | L5–14 |
| 16–21 | Failure definition and the four statuses | kept | L16–21 |
| 23–28 | Status table, including `needs_input` as a stop for a decision from the operator, or someone the operator names in writing | kept | L23–28 |
| 30–31 | Tracker states route to the index. Decisions route to Asking the operator | kept. A0 rewrote both links | L30–31 |
| 33–38 | JSON validity: one object, no duplicate keys, required fields, no unknown or null | kept | L33–38 |
| 40–45 | Top-level fields `step`, `status`, `evidence`, `findings` | kept. A0 rewrote the Names link on old L42 | L40–45 |
| 47–53 | Evidence fields other than `question` | kept | L47–53 |
| 54 | `question` is a non-empty string when `status` is `needs_input`, and it is the decision the stage waits on | replaced (A2, L2, R15, R50). It stays a non-empty string. The text is the asks it waits on, written `asks: <path> <ids>` | L54 |
| 56–57 | Omit an evidence field whose condition does not hold. Reject a present-but-not-required field | kept | L56–57 |
| 59–68 | Failure table | kept | L59–68 |
| 70–72 | A matching command row is a disagreement and a failure. Disagreement does not authorize opening prose | kept | L70–72 |
| 74–78 | Stage harness persists, replaces, writes for agents that do not, and fixes `step` and `evidence.kind` | kept | L74–78 |
| 80–84 | Output authority by actor and stage kind | kept | L80–84 |
| 86–92 | Normalize a missing exit code. Keep the wrapper result on a command stage. Missing files stay reader failures | kept | L86–92 |
| 94–99 | Open `findings` only for fail, blocked, or a missing required evidence field | kept | L94–99 |
| 101–116 | Examples heading and both `pass` examples | kept | L101–116 |
| 118–124 | `fail` example | kept | L118–124 |
| 126–133 | `blocked` example | kept | L126–133 |
| 135–140 | `needs_input` example through `kind` | kept | L135–140 |
| 141 | Example question is a retry choice in prose | replaced (A2, R50). The example question is `asks: .agents/design/payments-retry/asks.md Q3 Q4` | L141 |
| 142–145 | Rest of the `needs_input` example | kept | L142–145 |
| 147–150 | Out of scope: flow file, Pi command, session resume | kept | L147–150 |

## Meaning questions

None open. L54 and L141 are the LLD's exact replacements. The field type
stays a non-empty string. No open MQ.
