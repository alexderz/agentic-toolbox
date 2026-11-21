---
name: migrate
description: use this when an existing project or active session still follows an older toolbox playbook, especially a separate verifier agent — adapt its instructions and pending work to the current playbook without restarting completed steps or adding migration test runs.
---

# Migrate an existing playbook consumer

Keep accepted work. Change the instructions for the next work, not the
history of how earlier work was accepted. This is an instruction migration,
not an application upgrade, a new SDLC step, or a test campaign.

## Inputs

Read the project's governing instructions, current task and handoff,
accepted decisions, and the toolbox revision being adopted. Inspect the
actual prompts, role assignments and workflow configuration the project
uses; do not assume it uses a particular harness or file layout.

## Procedure

1. **manager**: identify the project's current step, retained workers,
   accepted outputs and available evidence. Note the previous toolbox
   revision if known; an unknown revision does not require archaeology.
2. Read the target [SDLC](../sdlc/SKILL.md), its current-step file and the
   applicable owners below. Use the target text, not remembered rules.
3. Map obsolete instructions to their current owner. Adjust project-local
   prompts, role assignments and references within the authorized scope.
   Replace contradictory old instructions rather than appending a second
   process. Let the model work out the project's concrete file changes.
4. **manager**: apply the new instructions at the next invocation boundary.
   Let active work finish without restarting it just to change policy.
   Give retained workers the target revision and their updated assignment;
   reload their applicable instructions before their next work.
5. Record the target revision, changed instructions, current step and any
   unresolved product-specific issue in the existing handoff. Preserve
   accepted outputs, approvals and usable evidence without backfilling a
   new proof bundle for historical work.
6. Continue the next real task from its current step. Do not require a
   migration rehearsal, test matrix, repeated passing suite, new approval
   round, or worker acknowledgment ceremony to adopt these instructions.

## Changes to recognize

| Previous instruction | Migration action and current owner |
| --- | --- |
| A separate agent repeats the builder's mechanical checks | Assign check execution and direct evidence to the builder. Retire the separate verifier assignment; retain the independent reviewer and security read. [Proofs](../sdlc/references/proofs.md) owns the checks, evidence and sharing rules. |
| Every review starts another test run | Give the reviewer evidence and the frozen diff, not the builder's transcript. [Review](../sdlc/references/build-review.md#review) owns the evidence-first read. Existing usable evidence need not be regenerated just to change its format. |
| Per-item tests are the only integration coverage | Carry touched journeys and meaningful midpoints into pending work. [Journeys](../sdlc/references/proofs.md#journeys) and [After integration](../sdlc/references/proofs.md#after-integration) define span coverage and runs on the actual landed revision. These test changed or combined behavior; they are not migration tests. |
| Ask the operator about every reversible implementation detail | Use [Asking the operator](../sdlc/SKILL.md#asking-the-human): keep settled answers, decide implementation details within scope, and keep questions only for matters the current rules reserve. Do not infer auto mode or new release permission. |
| Repeat Brief on already groomed work or restart the ladder after a tooling change | Resume the existing step under [Grain](../sdlc/SKILL.md#grain). Retain accepted scope and approvals; a real scope change still follows the normal process. |
| Run speculative extra checks or retain tests that guard no behavior | Apply [Prune tests that guard no behavior](../tdd/SKILL.md#prune-tests-that-guard-no-behavior) only inside the current item's scope. Migration is not permission to delete failing tests, regressions or required coverage. |
| Old names or document paths are treated as new products or IDs | Use the current [Playbooks](../../README.md#playbooks) terminology and SDLC entry point. Keep existing repository identities, `sdlc` and `sdlc-process`, compatible paths and stored identifiers. |

## Limits

1. Keep project-specific constraints, ownership, security and permission
   boundaries. Retiring duplicate execution does not retire independent
   review or turn a blocked check into a pass.
2. If adoption requires an application, workflow-engine, credential or
   live-service change outside the assignment, record that separate need.
   Do not silently deploy it as an instruction edit or block unrelated work.
3. If the project also changes its stage-result harness contract, use the
   existing [stage-result migration](../sdlc/references/stage-result-migration.md)
   for that separate change. Do not invoke it solely to merge verification
   into the builder or adopt the other instruction simplifications.

## Completion

The next assignment uses the current owners and the handoff identifies
what changed. Report actual adoption limits; a checked-in instruction does
not prove that a separate consuming application's runtime was changed.
No additional migration test run is required. Normal checks for the next
real change still belong to its builder.
