# Rule map — `stage-result.md` (A2, DER-734)

Old: `docs/sdlc/stage-result.md` at main c26f424, lines 1–150. New: `skills/sdlc/references/stage-result.md`.

Two lines change in place; no line is added or removed.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–53 | Identity, statuses, schema, evidence fields before `question` | kept | same lines |
| 54 | `question`: required when `status` is `needs_input`; the decision the stage waits on | changed (R15): the asks it waits on, written `asks: <path> <ids>` | L54 |
| 55–140 | Omit rule, Rules, Examples up to the `needs_input` question | kept | same lines |
| 141 | `needs_input` example: a retry-limit question | changed (R50): `asks: .agents/design/payments-retry/asks.md Q3 Q4` | L141 |
| 142–150 | Rest of the `needs_input` example; Out of scope | kept | same lines |

## Meaning questions

None. The `question` field's meaning changes only as R15 and R50 decide; the schema adds no field.
