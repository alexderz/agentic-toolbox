---
name: verify-before-done
description: use this when about to claim work is complete, fixed, or passing — before commit, PR, or “landed+verified” — run fresh verification and read the evidence first.
---

# Verify before done

Rewrite of obra/superpowers `verification-before-completion` @ `b36e0829`. Compress, not a paste. Id: `verify-before-done`.

Pairs with SDLC **Build**: notify **landed+verified** on **project-main**
(or trunk if that was the land target), not “pushed to an item branch”
and not LGTM without evidence.

The **proving command** is always re-run. The **verifier subagent** is
not: first verify of a work item is a clean verifier; later verifies of
that item **resume** it. Never use the builder as the verifier. See
[docs/SDLC.md](../../docs/SDLC.md) (Subagents per work item).

## Iron law

**No completion claims without fresh verification evidence.**

If you have not run the proving command in this turn, you cannot claim pass, fixed, green, or done.

## Gate

Before any success claim, commit, PR, or “next task”:

1. **Identify** the command (or check) that proves the claim.
2. **Run** it fresh and complete — not a remembered earlier run.
3. **Read** full output, exit code, failure count.
4. **Match** output to the claim. If not, report actual status with evidence.
5. **Only then** claim success — and cite the evidence.

Skip a step = claiming, not verifying.

## Always / Ask first / Never

| Always | Ask first | Never |
| --- | --- | --- |
| Fresh command for this claim | Softening verify for throwaway spikes you will delete | “Should pass” / “probably” / “seems” |
| Full suite or scoped command that actually covers the claim | Partial checks when full suite is expensive — name what you skipped | Trusting agent “success” without VCS/diff or independent run |
| Red-green proof for new regression tests | HITL when evidence is ambiguous or flaky | Satisfaction (“Great!”, “Done!”) before evidence |
| Line-by-line checklist for requirements DoD | Unsupervised push to protected / prod deploy / secret rotate | Extrapolating from linter to build, or build to product fix |

**HITL:** run verification for evidence — bots oversee workers. Do **not** unsupervised destructive/irreversible actions (push to protected branches, prod deploy, secret rotate) without the operator. If **security** or CI marks a check flaky/MEDIUM, do not self-clear — show the operator the output and wait.

## Claim → evidence

| Claim | Requires | Not enough |
| --- | --- | --- |
| Tests pass | Test run: 0 failures | Prior run, “should pass” |
| Linter clean | Linter: 0 errors | Partial path |
| Build succeeds | Build exit 0 | Linter green |
| Bug fixed | Symptom repro now passes | Code changed |
| Regression test works | Fail without fix, pass with fix | Passes once |
| Agent finished | Diff on project-main or trunk (the land target) shows the change | Agent said success; item branch only |
| Requirements met | Checklist against plan/ticket | Tests alone |

## Roles

| Role | Owns | Does not own |
| --- | --- | --- |
| **builder** | Running this gate before ship claims | Skipping **security** on skill-home PRs |
| **tester** | CI that produces evidence; verifier subagent for the item | Claiming product DoD from fmt-only green; minting a new verifier every loop |
| **security** | Intake / PR security clear | Day-to-day verify coaching |
| **manager** | After-act landed+verified | Blessing without evidence |

## Red flags

- Wording that implies success without a command in this turn
- “Just this once” / “I’m tired” / “agent said it’s fine”
- Moving on because the diff “looks right”
- Using the builder as the verifier, or minting a new verifier every loop
- Calling the item landed when it only exists on an item branch

Stop. Run the proof. Or say what is still unverified.

## Upstream pin

Intent pin: obra/superpowers `verification-before-completion` @ `b36e0829c6d0140e93cfef2ca599b1b07d4a7797`. See [SOURCES.md](../../SOURCES.md).
