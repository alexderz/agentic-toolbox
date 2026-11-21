# Builder-owned verification

## Requirements

- R1. The builder runs the mechanical checks that cover its change, including integration and end-to-end tests. A separate agent does not repeat a run against the same revision merely to confirm its result.
- R2. The reviewer receives direct evidence for each acceptance criterion: what ran, on which revision, the result, and where the reviewer can inspect it. State the limits of the evidence. Keep private workspaces and logs in the authorized review channel.
- R3. Retire the separate per-item verifier. Continuous integration, hooks, independent review, and security intake retain their existing purposes.
- R4. Review evidence against the intended behavior, then inspect the changes for concerns the evidence cannot settle. A passing check that proves the wrong property does not establish acceptance.
- R5. After an item lands, exercise the affected journeys on the actual integrated revision. For a chunk, exercise the full set on project-main before merging to trunk.
- R6. For a multi-step journey, test meaningful intermediate states as well as the complete path. Start-to-mid tests reach and assert the midpoint; mid-to-end tests start from a representative midpoint and exercise the remaining real path. Cover a touched journey even when its ticket overlooked a missing test.
- R7. Use [Agents write and check proofs](../../../docs/agents-write-and-check-proofs.md) to select evidence appropriate to the claim. A bounded proof does not replace an integration check for behavior outside the model.
- R8. Retain existing upstream pins and security review for changes to vendor-derived skill bodies.
- R9. Record the playbook change in the changelog.

## Scope

This change updates the playbook, its worker handoffs, and their documentation and evaluation criteria. It does not add a skill identifier, change public entry points, or alter a consuming application's runtime.
