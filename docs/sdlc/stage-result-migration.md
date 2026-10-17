# Adopt stage results in an in-flight session

Item: `DER-529`. This procedure applies when a session already has an
active SDLC item under instructions that predate the
[stage-result contract](stage-result.md). It is a migration procedure,
not an extra SDLC stage or a session-resume mechanism. It changes no
tracker states, step names, role permissions, or approval gates.

## Prepare at a safe boundary

1. **manager** identifies the item, current step, owning session, and
   active child invocations.
2. **manager** records the old instruction revision and the exact target
   repository commit containing the adopted stage-result contract.
3. **manager** records already accepted outputs, evidence, and approvals
   in the item’s existing handoff or tracker record.
4. **manager** stops dispatching new invocations with the old prompts.

Do not replace instructions inside an active invocation. Let it finish
under its recorded revision, or use the existing cancellation procedure.
Record a completed old-revision invocation as legacy evidence, not as a
new-schema result. If it is rerun, the rerun adopts the target revision.
Do not discard uncommitted work, reset branches, or restart the SDLC to
perform this migration.

## Adopt the contract

1. **manager** makes the target instruction revision available to each
   affected session through the repository’s existing branch rules.
2. **manager** supplies that revision, the current step, and the existing
   handoff to each session and retained worker that will receive work.
3. **manager** directs those agents to reload the target `AGENTS.md`,
   `docs/SDLC.md`, their current step instructions, and the
   [stage-result contract](stage-result.md).
4. **manager** replaces queued, unstarted prompts that contain the old
   contract before dispatching them.
5. **manager** verifies that each affected worker acknowledges the target
   revision before assigning its next invocation.

Do not require a fresh session when an existing one can reload its
instructions. If it cannot, use the existing handoff procedure; do not
claim that this migration implements session resume.

## Check the next invocation

1. **manager** verifies that the stage harness can persist the result in
   an invocation-specific output directory outside the source checkout.
2. **manager** verifies that the harness supplies the expected step and
   stage kind and preserves the command wrapper’s verdict and evidence.
3. **manager** verifies that read-only agents return their reports to the
   harness instead of writing files or changing the reviewed checkout.
4. **manager** dispatches the next real invocation under the target
   revision, preserving the item’s current SDLC step.
5. **manager** applies the contract’s validation and prose-reading rules
   to that invocation’s result.

If the harness or wrapper cannot meet the contract, stop dispatching
affected invocations. Record the migration blocker and missing
capability on the item. Do not simulate a passing result, ask a reviewer
to write files, or claim adoption is complete. Once the capability is
available, repeat this check. This procedure does not build that tooling.

A blocked or failed next invocation can still demonstrate correct
contract adoption. Its outcome does not become a pass because migration
succeeded. Invalid or missing results do not demonstrate adoption.

## Preserve history and close the migration

Keep completed steps and accepted approvals as historical evidence. Do
not fabricate `result.json` files for them or backfill process exit
codes. A new result is valid only for an invocation that actually ran.
Rerun only work whose required evidence is missing or whose approval is
invalidated by a substantive change, following the existing gate rules.

1. **manager** records the target revision, boundary between legacy and
   adopted invocations, acknowledged workers, first validated result
   path, current step, and remaining blockers in the existing item record.
2. **manager** continues the item from that step under the target
   instructions; do not repeat completed steps merely to make files.

When this procedure is repeated, reuse the recorded migration boundary
and revision. Check any newly added workers or invocations; do not
repeat an already validated invocation solely to repeat the migration.
