# Rule map — `AGENTS.md`

Item: DER-774 (pstack formal verification and statechart, incoming item).

Old: `AGENTS.md` at c82318b, lines 1–77. New:
[`AGENTS.md`](../../../../AGENTS.md) (79 lines).

Key: **kept** (same rule, this file), **route** (the owner keeps the rule; this file links it),
**dropped** (owner named), **changed** (with the ruling that decides it), **added** (new line,
with its source). Source for the new rows: manager ruling 3 for DER-774.

Protected rows touched: the Public-repo rule (L16–33) is **kept**.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–60 | Title; Public repo; How to load rows through Web platform | kept | L1–60 |
| — | Formal verification row: architect at Spec when the design has concurrency, retries, ordering, state machines, protocols, parsers or unsafe code; builder when its ticket names a verify target or the change touches code a project-local verify skill covers; verifier runs that verify skill | **added** (ruling 3) — a route; the procedure and its policies are owned by `skills/formal-verification/SKILL.md` | L61 |
| — | Statecharts row: designer charting a user flow; architect or verifier reading a model checker's results; builder reading TLC results while following a verify skill | **added** (ruling 3; r1 #7 adds the builder reading TLC results while following a verify skill) — a route; owned by `skills/statechart/SKILL.md` | L62 |
| 61–77 | Branches and lands through Minecraft rows; Intake (security); Related | kept | L63–79 |

## Meaning questions

None open. The new rows add no role, gate or ask; each names when a role reads one skill, as
the UI craft and Web platform rows do. "verifier" is a step job acting in a role per
`skills/sdlc/SKILL.md#roles`, not a new role. File stays under the 100-line cap (79).
