# DER-800 r3 delta follow-up: mechanical/evidence assessment

**Verdict: the cumulative MECHANICAL PASS stands.** All three corrections taken in the r1 disposition are made. I found no new evidence defect and no correction is required. My r1 evidence and limitations still hold.

I compared `review-r2-source/` against `review-r1-source/` and `base-source/`. I read every tool call and result in the r3 author stream (Bash at lines 3, 10, 29 and 46; Write at line 50) and the raw files in `author-r3-evidence/`. I did not rerun anything.

## The taken items

**R1 report/filing text alignment: corrected.**
- **`skills/tdd/SKILL.md` L69** now ends "Do not edit a prune case outside that scope." The `findings` clause, the stage-result link and "so the manager can file it" are gone. This was the only link in the changed lines, so there are no new links.
- **Other `findings` mentions** remain only at L82, L89, L98 and L99. These are the in-scope result notes the disposition allows to stay.
- **CHANGELOG line 35** now reads "…does not edit others", still tagged DER-800.
- **SOURCES `tdd` row:** "prune cases outside that scope are not edited".
- **Change map:** adaptation row 1 now says "…are not edited" and "no approval gate and no report duty added". MQ2 says it "adds no report duty or channel for out-of-scope cases".
- **No contract change:** `stage-result.md` was not touched; the stream shows no edit to it.

**Mechanical A, pin-order wording: corrected, with no false claim.**
- **Candidate files:**
  - The SOURCES `tdd` row now says "(source pin and body are included in the same change before landing)".
  - The change map (L13) now says "Pinned in `SOURCES.md` (the `tdd` row); the source pin and this body are included in the same change before landing."
  - Both statements are true.
- **Leftover wording:** "before the body" still appears in SOURCES at L47–49. Base has the same three occurrences, so these are unchanged rows for other skills.
- **Edit order disclosed:** the author-r3 report (item 3) states the real r1 order: body first, SOURCES row after, so intake step 4 was not followed in authoring order. The report claims no retroactive compliance.

**O4, map-only checklist note: corrected, and the checklist is not waived.**
- **Change map:** MQ3 now says the unchanged `Checklist` ("Before calling the work done", old L114–121) "still applies to pruning too", and that this commissions no new whole-suite or mutation run.
- **Citation:** I checked old L114–121 in base; it is exactly that checklist block.
- **No rule change:** the stream shows no edit to the TDD rule text.

## Evidence for the new candidate

**Body blob.**
- **Hash:** the stream (line 29, result at line 30) shows `git hash-object skills/tdd/SKILL.md` returning `4c698cd7befba8d374ba166d029ea316e8478631`.
  - That call ran after the only SKILL.md edit (line 10).
  - It replaced the old blob string `9abc2f66…`, guarded by `assert count==1`.
  - `grep -c` then found the new hash once, and `wc -l` gave 175.
- **No later SKILL.md edit:** the only later calls are the evidence capture at line 46 and the report write at line 50.
- **SOURCES:** it records "New body blob 4c698cd7…".
- **Not recomputed:** I am in a read-only lane, so I did not hash the file myself.

**Scans of the four changed paths.**
- **What ran:** each file was scanned once, run directly with output redirected to files. The exit code was read with `rc=$?` straight after the python call, with no pipe, so each `.exit` file records the scanner process's own status.
- **Results:** all four `.exit` files contain 0. Each stdout says SAFE, risk 0/100, 0 findings, and all stderr files are empty.
- **Scanner checkout:** `scanner-checkout.txt` records HEAD `b1476498…` with 0 dirty entries.

**Whitespace check (`git diff --check`).** Run once: `diff-check.exit` reads "exit=0", and stdout and stderr are empty.

**Commands stayed in scope.**
- **Bash calls:** one read and grep pass, one guarded text replacement, the blob hash plus its SOURCES update, and the evidence capture.
- **Write calls:** only `author-r3-report.md`.
- **Not done:** no link sweeps, K-checks, test suites, evals, network or installs, and no edits to earlier reports or sources.
- **Denials:** `permission_denials` is empty.

## Limits

- **Whitespace on the change map is unchecked.** `git diff --check` covers tracked files only, so the untracked change map had no whitespace check. The author discloses this.
- **Scanned files may not be byte-identical to the frozen copy.** The r3 scans ran on the `worktree/` files, not on the frozen `review-r2-source/` copies. The text I inspected in the frozen copies matches the edits the stream applied, and nothing changed after the scans. I did not do a byte-level comparison.
- **Scanner remote is from an earlier capture.** The origin `obielin/skillshield` was not re-captured in r3; it comes from r1 (ledger L313).
- **Scanner "Lines" is not `wc -l`.** It reports 176 for SKILL.md (`wc -l` 175) and 70 for the change map; it is the scanner's own metric.
- **Earlier limits stand unchanged.** The r2 piped scan did not prove the scanner's own exit code; the r2 map citation edit came after its checks; the r1 edit order is as recorded. These are historical and were not rerun or repaired.
- **Out of my scope:** security clearance and instruction correctness belong to the other lane. SOURCES still correctly says "**security** intake: pending".
