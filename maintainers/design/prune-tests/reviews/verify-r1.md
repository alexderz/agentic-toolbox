# DER-800 prune-tests verify: mechanical and captured-evidence assessment

**Verdict: MECHANICAL PASS.** No correction is required before landing. There is one provenance-wording contradiction (item A), which I recommend fixing but which does not block. Five report-precision limits are listed under "Optional".

This is a mechanical check only. The security decision belongs to the other lane, and SOURCES still correctly says "**security** intake: pending".

## 1. Paths, size, pins, blob and line ranges

- **Paths:** `candidate-paths.json` lists four paths. All four are in `review-r1-source/`. Three modify existing files and the change map is a new file, as expected.
- **What changed:** I compared each file with `base-source/`.
  - **`skills/tdd/SKILL.md`:**
    - L3: the `description` gains one clause.
    - L63–109: a new section is inserted.
    - L168: one checklist box is added.
    - No old line is removed or reworded.
  - **`SOURCES.md`:** only the `tdd` row changes.
  - **`CHANGELOG.md`:** one line is added under Unreleased → Changed.
- **Diffstat:** the author's r2 ledger records "CHANGELOG 1+, SOURCES 2+-, SKILL.md 50+-; 51 insertions, 2 deletions" (ledger L1235), which agrees with my comparison.
- **Size:** the frozen SKILL.md has 175 lines, under the 250 cap. The author's `wc -l` gave 175 (ledger L1210), and the old file has 127 lines. Hunks `@@ -3 +3 @@`, `@@ -62,0 +63,47 @@` and `@@ -120,0 +168 @@` add up to 175.
- **Upstream pin:**
  - `source.json` sha `bd73b2ea…f82` matches the SOURCES row.
  - The upstream checkout printed HEAD `bd73b2ea…` and `ls-remote` `refs/heads/main` showed the same SHA (ledger L237).
  - The upstream blob `7821d52f…83b9` came from `git rev-parse HEAD:skills/prune-tests/SKILL.md` (ledger L630). It matches SOURCES and exists in `upstream-clone/.git/objects/78/`.
- **License:** MIT, copyright 2026 Maze. This matches the upstream LICENSE text captured at ledger L42. The upstream tree holds only `skills/prune-tests/SKILL.md`, with no scripts.
- **Final body blob:** `9abc2f66b3d3fbf60f8254e33f6e614d92a2a254`, from `git hash-object` at ledger L1210. The ledger records no later edit to SKILL.md; the only later edits are to the change map. I did not recompute the hash (read-only lane). The base blob `47d2478b…` (ledger L630) matches the earlier DER-712 note in the base SOURCES row.
- **Cited line numbers:** I checked them against the frozen files.
  - Old file: L12, L36, L48, L60, L110 and L119 all match.
  - New file: L63–108 is the section from heading to closing fence, L67 is the "guards behavior" definition, L88 is step 3 and L168 is the checklist box. All match.

## 2. Links, anchors and routing

- **New link** `../sdlc/references/stage-result.md#schema`: the target has `## Schema` at L33, and `findings` is a schema field at L45.
- **Existing link** `../sdlc/SKILL.md#asking-the-human`: `<a id="asking-the-human">` is at L109. This link is unchanged from base.
- **Change map link** `../../../../skills/tdd/SKILL.md`: resolves to the skill file.
- **Author's link check (K7):** it checked all four files and printed only "K7 done", with no MISSING or BADANCHOR lines (ledger L1391).
- **Routing still reaches `tdd`:**
  - the AGENTS.md Debug row says "Then `tdd` + `verify-before-done`";
  - `build-review.md:76` says "Load `tdd`";
  - `subagents.md:111` lists `tdd`.
- **No dangling skill names:** the new text names `debug` and `yagni`, and both exist in `skills/`. `prune-tests` appears only as upstream provenance in code font. It is not a new id or a link.

## 3. Scans and source metadata

- **Independent capture (`candidate-scan/index.json`):**
  - The exact command, run once per file on all four frozen files: `python3 -I -c "…skillshield.cli main…" <scanner>/src <file>`.
  - Each run's own exit code was 0.
  - Each output says "SAFE, Risk 0/100, Findings 0".
  - All four stderr files are empty.
- **Scanner origin:** the scanner checkout's git remote is `obielin/skillshield`, at HEAD `b1476498…` (ledger L313, and again in r2 at L1391).
- **Upstream file:** it was scanned in r1 with an unfiltered command: SAFE, exit 0 (ledger L953).
- **Metadata:** the SOURCES row carries the upstream, both pins, the blob ids and the license.

## 4. What the author actually ran vs what was authorized

- **Read-only inventory:** `cat`, `ls`, `grep`, `sed`, `git log`, `git show`, `git status`.
- **One failed command, which was not a test:** ledger L92 exited 1 because the glob `skills/tdd/*/*` matched nothing, so `wc` failed. It was an inventory command.
- **Network:** exactly one fetch. It used `git fetch --depth 1` at the pin into a new quarantine directory, with hooks disabled (ledger L227). That is intake step 1. There was no `npx`, no marketplace install, and nothing from upstream was executed.
- **Edits:**
  - Through the Edit and Write tools: SKILL.md, SOURCES, CHANGELOG and the change map.
  - Through Bash: a `python3 -I` heredoc string replacement on SOURCES and CHANGELOG, guarded by `assert count==1` (ledger L1226).
  - Index changes: `git add -N` on the change map, later undone with `git reset`. The status at session start shows the change map untracked again.
- **Focused checks:** whitespace (`diff --check`), line counts (K1), banned-names grep on changed files only (K3), public-text and local-path grep (K10), links (K7), the citation check, and the scanner.
- **Not run:** no full test suites, model evals, browser or live runs, or upstream installers.
- **Denied attempts:** none. `permission_denials` is empty in both stream files.
- **Overclaim, since retracted:** r1 said a T1–T3 eval run was "still required" (author-report L141). r2 withdrew this.

## 5. Writing standard and changelog bookkeeping

- **Change map:**
  - Its path and slug follow the Rule maps section of the writing standard: `prune-tests/rule-maps/skills-tdd.md`.
  - It does a light pass of changed lines only, as step 6 allows for vendor-derived skills.
  - It has an Old/New header, dispositions marked "changed" with DER-800, and `## Meaning questions` MQ1–MQ4, all resolved.
- **CHANGELOG:** exactly one line under Unreleased, tagged DER-800.

## 6. Evals

`maintainers/evals/baseline.md` has a header and zero model rows, so there are **zero enumerated model cases**. That is not "evals passed", and it is not a missing matrix. No runs are authorized.

## Recommended correction (not a mechanical blocker)

**A. "Pinned before the body" does not match the edit order.** Both the change map (L13) and the SOURCES row ("pinned before the body") claim the pin came first. In the r1 ledger, the SKILL.md body edits (L351–576) happen before the SOURCES row edit (L671–675). Intake step 4 says "Write the row first".

Nothing has landed, so the gate on landing is met: the pin and the body arrive together. But the sentence is not accurate as history.

- **Fix:** reword it to something like "pinned in SOURCES in the same change, before landing".
- **Alternative:** the security lane accepts the current reading of "lands".

## Optional: report precision

1. **The author's r2 scan exit codes were not the scanner's.** The command was `( … python … | grep … ); echo "exit=${PIPESTATUS[0]}"`, which prints grep's exit status, and the output was filtered. The independent capture supersedes it.
2. **The author's r2 change-map evidence predates the final file.** The change map was edited (L89 → L88, ledger L1404) after the r2 scan, link check and grep (ledger L1381). Those results cover the earlier version; the independent capture covers the final one.
3. **The scanner's "Lines" figure is not a line count.** It reports 176 for SKILL.md and 67 for the change map, which does not match `wc -l`. The size cap relies on `wc -l` (175) and on inspecting the frozen file.
4. **`index.json` does not record the scanner's commit.** It uses the same path as the checkout at `b1476498…` but does not prove that checkout was unchanged.
5. **Minor change-map form:** it says "after 61" where the hunk inserts after old L62, which is a blank line. Its table column is named "Change" where the standard says "Rule".

## Limits of this assessment

- I did not recompute the blob hash or rerun any check; everything above comes from captured evidence and file inspection.
- I did not review the instruction text for correctness or security; that is the other lane's job.
