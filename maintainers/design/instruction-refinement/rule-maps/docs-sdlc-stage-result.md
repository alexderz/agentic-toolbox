# DER-529: typed stage-result rule map

Old: `docs/sdlc/stage-result.md` absent at main 7a11696.
Review baseline: `docs/sdlc/stage-result.md` at 5704a58, lines 1–148.
New: `docs/sdlc/stage-result.md`. New-file additions implement DER-529.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–3 | Identity and ticket hierarchy | kept | Opening |
| 5–10 | Stage definitions, output file, common schema, and ACP distinction | kept; clarify per-invocation output directory outside source checkout | Opening |
| 12–24 | Closed statuses | kept; include the operator’s written delegate | Status |
| 25–27 | Tracker states and decision owners | route to `docs/SDLC.md#tracker` and `#asking-the-human` | Status |
| 29–41 | Required fields and JSON validity | kept; add explicit duplicate-key rejection | Schema |
| 43–50 | Conditional evidence | kept; name evidence members fields consistently | Schema |
| 52–53, 56–65 | Failure and disagreement rules | kept; clarify reader rejection, structured errors, and missing evidence | Rules |
| 54 | A file can match both validation and prose rules | kept in substance; separate validation from prose permission | Rules, disagreement paragraph |
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

## Re-review corrections

- Define harness, reader, wrapper, and evidence at first use.
- Keep file-write restrictions with their existing role owner; the
  harness persists reports without modifying role rules.
- Treat wrong invocation identity and conditional-field violations
  as reader failures. Protect stage kind from model substitution.
- Normalize abnormal command completion in the wrapper; the harness
  supplies model failure results when output is missing or invalid.
- Keep the required non-empty failure findings rule explicit for
  deterministic wrappers. Scripts need no model to populate it.

These are clarifications of the every-path contract, not driver code.

## Final closure suggestions

The final independent review found no Important or Critical findings.
Apply its two optional suggestions: separate the example headings with
a blank line and scope missing/invalid model-output fallback to model
stages. Command stages retain their wrapper verdict and evidence.
