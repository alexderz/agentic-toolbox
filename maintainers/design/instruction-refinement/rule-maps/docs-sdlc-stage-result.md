# DER-529: typed stage-result rule map

Old: `docs/sdlc/stage-result.md` absent at main 7a11696.
Review baseline: `docs/sdlc/stage-result.md` at 5704a58, lines 1–148.
New: `docs/sdlc/stage-result.md`. New-file additions implement DER-529.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–3 | Identity and ticket hierarchy | kept | Opening |
| 5–10 | Stage definitions, output file, common schema, and ACP distinction | kept; clarify per-invocation output directory outside source checkout | Opening |
| 12–27 | Closed statuses; tracker and decision owners | kept; route tracker and decisions; include the operator’s written delegate | Status |
| 29–41 | Required fields and JSON validity | kept; add explicit duplicate-key rejection | Schema |
| 43–50 | Conditional evidence | kept; name evidence members fields consistently | Schema |
| 52–65 | Failure and disagreement rules | kept; clarify reader rejection, structured errors, and missing evidence | Rules |
| 67–75 | Emit on every path; wrapper owns verdict; model may add findings | kept; harness persists results for read-only roles; protect command evidence; explicitly permit script findings | Rules |
| 77–84 | Prose reading restricted to fail, blocked, or missing evidence | kept | Rules |
| 86–144 | Four valid status examples | kept; add a passing model example | Examples |
| 146–148 | Exclude flow, Pi command, and session resume | kept | Out of scope |

## Meaning questions

- The operator rejected Spec finding 1 on 2026-10-17: scripts can
  populate findings from CI job links or captured errors. The existing
  permission for models is not exclusive. Explicit wording preserves it.
- The operator requested fixes for both Minor and Important findings
  on 2026-10-17. Invalid or disagreeing results are rejected without
  extending permission to open prose. Harness persistence preserves the
  read-only reviewer rule without editing that skill.

No open meaning questions.
