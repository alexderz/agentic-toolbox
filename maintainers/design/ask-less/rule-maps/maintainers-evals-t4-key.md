# Rule map — `maintainers/evals/t4-key.md`

Old: `maintainers/evals/t4-key.md` at 0abd4db9e5053da6b0e5ad2ef4dfa338561fc985, lines 1–106. New: [maintainers/evals/t4-key.md](../../../evals/t4-key.md).
Item: DER-748. This map records the scoring correction in `1e9b8a2a315594a7e1c948b6f1aa75dd41f9e2e0`.
Authority: [LLD A6](../lld.md#a6--onboarding), as overridden by
[overlay G7 edit 3](../opus-rebuild.md#g7--onboarding-a6): Tracker Write
waits for the proposal reply; Execution Write runs now and goes in the
onboarding commit at a first tracker touch. See the existing
[onboarding map](skills-sdlc-onboarding.md), rows for old L38–40.

Provenance: this is a new per-item map, not a rewrite of the T4 design
snapshot [rebuild/t4-key.md](../rebuild/t4-key.md). That snapshot is
historical; the linked live eval key is the New target.

Key: **kept**; **route**; **dropped** with the owner named; **changed** with its deciding id.
New locations refer to the current eval key.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–24 | Title, scorer-only and PR-head notices; Entry, Gather, Refine, onboarding check, touchpoint 1 | kept | L1–24 |
| 25–29 | After replies: project-main, brief and records; onboarding with Tracker, repo skill and Execution through Review and landed; Epic and Entry comment | kept (MQ1): describes the reviewed and landed onboarding after replies, not a ban on earlier uncommitted Execution | L25–29 |
| 30–58 | Plan, Trial, Spec, design gate, Groom, Build, report; expected end state; required-ask header, N1 and N2 | kept | L30–58 |
| 59 | N3: Tracker, Execution, repo skill, tickets and Epic wait for reply; any pre-reply write fails C1 | **changed** (DER-748; overlay G7 edit 3; MQ1): only Tracker-area writes wait for N3's reply; Execution needs no answer, may be written before the reply, and is committed in the onboarding commit | L59 |
| 60–95 | N4 design gate; counts and guardrail disclosures; deviations heading, header and game-code-before-N4 row | kept | L60–95 |
| 96 | Any tracker or repo write before N3's reply fails C1 | **changed** (DER-748; overlay G7 edit 3; MQ1): only Tracker-area writes (`## Tracker`, repo skill, tickets, Epic) before N3's reply fail C1 | L96 |
| 97–106 | Execution question O6 and other over-asks fail C6; remaining deviations, Entry comment and completion rule | kept | L97–106 |

## Meaning questions

- **MQ1 (DER-748), resolved:** Does N3 or step 6 forbid early Execution
  Write? No. [Overlay G7 edit 3](../opus-rebuild.md#g7--onboarding-a6),
  lines 637–642, separates the Tracker reply gate from immediate Execution
  Write and retains the first-touch onboarding commit. Early Execution is
  uncommitted until that commit, not a standalone early commit. Step 6
  still describes onboarding through Review and landed after the replies.
  [LLD A6](../lld.md#a6--onboarding) supplies the retained branch and
  Execution Write rules. N1, N2 and N4 remain unchanged; this correction
  neither authorizes arbitrary repo writes nor relaxes Review, security,
  item-branch or C6 requirements. No new gate is added.
