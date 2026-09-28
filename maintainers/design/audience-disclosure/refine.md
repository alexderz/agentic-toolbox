# DER-286 refine, round 1

Refiner (not the gatherer), worktree `instruction-refinement` at `88455d8`, `yagni` only.

## Simplifications (none change an operator decision)

- **S1. D11 into D2.** D11 fires only on D2's chunk-Brief re-check. It becomes one clause:
  "flip `no`→`yes` → warn that all history is now public; cleanup is DER-350".
  Merge the two Verify lines. This also fixes the D11-before-D10 order.
- **S2. D1 into D2.** The bit and where it lives are one decision.
- **S3. Cut D9.** "No deny-list" is already in Out of scope.
- **S4. D5 into D4.** Where the companion is announced belongs with the companion.
- **S5. D8 is a clause, not a new gate.** Onboarding Propose step 6
  (`sdlc-onboarding/SKILL.md:122-128`) already asks for a yes to the `tickets`
  bootstrap on its own line. Add: "remote is public: every ticket is published
  forever; private context goes only to the companion."
- **S6. D10 is one clause.** No repo text mentions sops or git-crypt. D3 already
  covers readable file names and commit messages. Put "on request, explain the limits"
  next to D3's ban in security-hardening. That Verify line covers it.

## Precision fixes (Verify aligned with decisions; no decision change)

- **P1.** The Verify line "Tracker host names are not written" is wider than D3,
  which bans only *internal* hosts. As written, it forbids `mcp.linear.app` (E10). Say
  "internal". A self-hosted tracker uses an env var name instead (`SKILL.md:196`
  allows it). That is a Plan detail.
- **P2.** The pre-push-read Verify line leaves out the local adapter's ticket write,
  which pushes on every write (`adapters/local.md:132-161`). D3 and D6 already cover it.
- **P3.** In D7, "tracker" means a *private* tracker. With a public local tracker,
  only the companion is left. With no companion, drop the text or ask. This follows
  from D3.

## Checks

- Each remaining decision and Verify line closes a leak path. No requirement died:
  "security reads every diff" became the pushing agent's read (D6, operator Q4).
  No new unresolved point: P1–P3 follow from decisions already made.

**Verdict: CONFIRM-READY** with S1–S6 and P1–P3. Decisions: D1+D2+D11, D3+D10, D4+D5, D6,
D7, D8 clause; D9 cut (11 → 6).
