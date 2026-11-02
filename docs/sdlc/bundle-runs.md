# Bundle runs

Owner of every HLD rule change (solo-dlc design HLD, "Rule changes")
for a driven or followed bundle run. Other SDLC files keep their rules
off that path and carry a one-line route here. Run-root formats belong
to [Run state](run-state.md). Exits, chunk land, re-entry, and the
`json sdlc-env` block belong to [Flow spec](flow-spec.md). Worker
output belongs to [Stage results](stage-result.md).

## Order

Accepted LLD (`spec-gate` accept), then `env-prep` through `env-land`,
then Groom, then Build. Groom writes prove lines against that proven
environment. Human gates are Brief, UX, Plan, Trial choice, Trial
completion, mockup, Spec, env, and re-Spec. A worker cannot accept one.
Groom is accepted by its clean groom reviewer with `file`; tickets are
filed only after that review passes.

## Tracker

Workers write tracker state per the
HLD tracker table (solo-dlc design HLD, "Tracker").
Prompts carry those instructions. The driver also runs the repo tracker
skill `read` with no model for the tracker-state check.

Each persona claims under its own label, the persona folder name. In
Claim steps 1 and 4, a marker or assignee whose label is `builder-`,
`verifier-`, or `reviewer-` plus the claiming persona's own suffix is
the same item, not a collision. No other label counts. Contract version
stays 2. The local adapter changes only that assignee test:
[Tracker](../../skills/tracker-sdlc/SKILL.md#claim).

The reviewer sets `in_review` at the start of each pass. The post-land
verifier sets `done` and comments the land SHA, verifier result, and
verdict. The driver deletes the item branch only after it reads `done`.

The architect posts the HLD or LLD path on the Epic after the driver
commits and pushes that record. The architect writes Plan and Spec into
its run folder and scans them; the driver commits and pushes. The
driver follows Groom plan order. It does not ask the manager to set
land order.

## Git

The driver pushes item branches, the env branch, and project-main.
Workers commit locally. The one push a worker makes is the tracker
recipe's own push to `tickets`; a worker never pushes another branch
or deletes a remote ref. The post-stage `refs` check stops a stage
after any other remote change.

In-flight builders merge project-main into the item branch and never
rebase a pushed branch. A builder `blocked` result is a stop. While the
item tree equals the mechanical clean merge, only the proving commands
and the verifier re-run. Any other tree, including a conflict
resolution or a later fix, re-runs Review before land.

## Sessions

Context pressure does not replace a persona. Compact from `state.md`.
A missing session file is rehydrated from the compiled file, `state.md`,
and driver facts. An unloadable session is a stop. Only the operator
approves a replacement.

## Asks

User-visible ids are `ask-N`. N comes from a counter that does not
reset. The same decision keeps the same N when evidence is reworded. A
different decision takes the next unused N. Keep that N. Never
renumber an ask to anonymous Q1 or Q2. Never reuse an N for a
different decision. Internal files, the names the
accepted driver writes, are `asks/ask-N.json` and `asks/ask-N.md`. Gate
evidence is `operator-answer: asks/ask-N`. Silence is not acceptance.

## Ledger

Each verifier writes `ledger.json`. The row id is `V<n>`. For each
item, and for the chunk during env-prep, n comes from that scope's own
counter and the counter does not reset. Criticality is `breaking`,
`critical`, `major`, `minor`, or `nit`. Do not allocate
`<item-key>-v<issueBase>-<k>`. Keep every row and mark it fixed.
Never renumber or delete a row. A pass
has no open row above `nit`. Nits are not sent to the builder as open.

## Repairs

One counter per item, and one on the chunk for env-prep, across every
check. It does not reset. A red run of the land proving commands counts
as a failed fix. The third failed fix is an operator stop. Invalid
model output gets one repair attempt, then `fail`. Added result fields
`schemaVersion`, `choice`, `ticket`, and `artifact` are defined in
[Stage results](stage-result.md).

## Public git

Transcripts and prompts stay in the local run root. They are not
tracker comments and they are not mirrored. Secrets and `passEnv`
values are not written into tracker comments, `result.md`, `state.md`,
asks, or any other file the state branch publishes. Command evidence
replaces each `passEnv` value with `<passEnv NAME>`. At `pushed`,
mirrored files are public on a public repo. This file does not clear
security intake.
