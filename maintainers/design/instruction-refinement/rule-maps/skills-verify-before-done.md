# Change map: `verify-before-done`

Old: skills/verify-before-done/SKILL.md at main 7a11696, lines 1–81. New: skills/verify-before-done/SKILL.md.

Light pass (LLD area F): changed lines only. Every other old line is
unchanged. No upstream text added; no upstream fetch. The SHA pin,
license and tools are unchanged.

Key: **kept** (same rule, new words), **route** (one line to the
owner), **dropped** (owner named).

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 10–12 | Notify only when landed+verified on project-main or trunk; not an item-branch push; not LGTM without evidence | route; the land target is in the SDLC index `#names` (landed+verified); item-branch and no-evidence claims stay in this file (Claim → evidence row "Agent finished", Red flags, Iron law) | L10–11 → `docs/sdlc/build-review.md#definition-of-done` |
| 14 | Re-run the proving command on every verify | kept | L13 |
| 14–17 | Verifier: clean on first verify, resumed later; never the builder; prose section name "(Subagents per work item)" | route; fixes the stale prose section name | L13–14 → `docs/sdlc/subagents.md#item-agents` |
| 43 | Ask first: human in the loop when evidence is ambiguous or flaky | kept; "HITL" expanded to "Operator in the loop" (SDLC index role name) | L40 |
| 46 | Label "HITL" | kept; expanded to "Operator in the loop" | L43 |
| 46 | No unsupervised destructive or irreversible actions without the operator | dropped; owner is this file's Ask first column (old L44, unchanged). Also fixes the missing verb | L41 |
| 46 | Run verification for evidence; do not self-clear flaky/MEDIUM; show the operator and wait | kept, text unchanged | L43 |
| 64 | builder does not own: skipping **security** on skill-home PRs | kept; "skill-home PRs" → "changes to skill homes, reviewed at Review" (no internal PRs; Review is the gate) | L61 |
| 65 | tester does not own: minting a new verifier every loop | dropped; owner `docs/sdlc/subagents.md#item-agents` (Never list), routed at L13–14 | L62 (rest of row unchanged) |
| 66 | security owns: intake / PR security clear | kept; "PR security clear" → "security clear at Review" (no internal PRs) | L63 |
| 74 | Red flag: builder as verifier; new verifier every loop | dropped; owner `docs/sdlc/subagents.md#item-agents`, routed at L13–14 | — |

`SOURCES.md` L28, `verify-before-done` Notes cell: "HITL" → "operator
in the loop", the body's rename; appends the LLD vendor-derived note,
`Wording edit DER-288, pins unchanged; security-cleared 2026-09-27.`
Upstream, SHA and License cells unchanged.

## Meaning questions

None open. MQ1: does dropping old L46's destructive-actions sentence
lose a rule? Resolved from the text: old L44 (Ask first, unchanged)
holds the same three actions — push to protected branches, prod deploy,
secret rotate.
