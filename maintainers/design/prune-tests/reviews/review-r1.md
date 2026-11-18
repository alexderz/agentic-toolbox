# DER-800 review: prune-tests folded into `tdd` (r1 frozen candidate)

**Verdict: CHANGES REQUIRED.** One concrete defect needs fixing: the new text promises the manager will see out-of-scope prune cases, and the unchanged stage-result contract stops that on a normal passing Build.

**SECURITY CLEAR** for the text-only scope. There is no security blocker.

## Required correction

**R1. The hand-off to the manager does not happen on a passing stage.**
- **Where:** `review-r1-source/skills/tdd/SKILL.md:69`.
  - It says: "Do not edit a prune case outside that scope; list its path and table row in your stage result `findings` … so the manager can file it."
- **Conflict:** `worktree/skills/sdlc/references/stage-result.md:94-99` is unchanged. It tells the reader to open `findings` only when `status` is `fail` or `blocked`, or a required evidence field is missing. Otherwise: "Do not open `findings`."
- **Effect:** A Build that prunes in scope and finds an out-of-scope case normally ends `pass`. The manager never reads the list and never files it. A small local model will believe the hand-off is done.
- **Also affected:** The change map's resolution of MQ2 (`rule-maps/skills-tdd.md:55-57`, "routes out-of-scope cases to the existing stage result `findings` field") is incorrect for the same reason. So is its upstream-adaptations row (`skills-tdd.md:28`).
- **Fix, smallest first:**
  - **Recommended:** remove the filing promise.
    - Keep "Do not edit a prune case outside that scope."
    - Either drop the reporting duty, or keep a plain note in `findings` that claims no effect.
    - Update the change map MQ2 row, `CHANGELOG.md:35` ("reports other prune cases in the stage result") and the `SOURCES.md:30` adaptation note to match.
  - **Alternative:** route the cases through a channel the manager does read.
    - Don't widen this item to change `stage-result.md`. That would be a separate contract change.
- **Not affected:**
  - `SKILL.md:82` and `SKILL.md:89` also write to `findings` on what may be a pass. Line 82 keeps the test, which is safe whether or not anyone reads it. Line 89 is backed by the diff the reviewer reads anyway.
  - `SKILL.md:99` ("Change neither; report the mismatch") leaves the item's checks red, so the stage ends `fail` and `findings` is read.

## Acceptance mapping

**Q1. Useful pruning is kept, discoverable, and adds no second lifecycle: Met.**
- The guidance is one section in `tdd` (`SKILL.md:63-108`), plus the description at L3 and one checklist line at L168.
- There is no new skill id, no `AGENTS.md` row and no new process.

**Q2. Coverage, scope, and stale vs regression: Met.**
- These are kept:
  - Regression tests (L73).
  - Absences that a ticket, LLD, **security** finding or caller requires, such as a removed endpoint staying gone (L74-75).
  - Contract calls and orders: sent message, write, charge, protocol step (L80).
  - Tests through a different boundary, or that catch a fault the other misses (L81).
  - Unclear cases (L82).
- Scope is bounded at L69: tests of behavior the ticket changes, or tests a pruning ticket names. Editing a file does not put its tests in scope.
- Stale vs regression is handled at L93-101. A test is checked against the accepted contract. A stale expected value is updated only when the ticket or LLD shows the contract changed. "Never delete or weaken a test to hide a regression" names the allowed action, per writing standard 7.

**Q3. No campaigns, gates or extra authority; agreed checks still apply: Met.**
- L88: "Verify with the checks the item already uses; pruning adds no test runs of its own." There is no mutation or full-suite mandate and no new ask or approval gate.
- The wording does not waive a real requirement. The checklist line "Suite is green" (L166) and the DoD's tests or verification evidence stay.

**Q4. Coexistence with TDD, roles and stage-result rules: Met except R1.**
- I checked MQ1-MQ4 against the source:
  - **MQ1** is sound. L60 governs writing new tests; L80 is conditioned on caller-observable effects.
  - **MQ3** is sound for the skill text (see O4 for the change-map wording).
  - **MQ4** is sound. The iron law is untouched because updating a stale expected value adds no production code.
  - **MQ2** is wrong (R1).
- Role and authority are fine. The builder writes no tracker state and leaves filing to the manager, consistent with `sdlc/SKILL.md#tracker`.
- The condition → action tables suit smaller models. See O1 for row precedence.

**Q5. Third-party intake: Acceptable.**
- **Pin:**
  - Commit `bd73b2ea…` and blob `7821d52f…` match the quarantine. Both objects are present in the upstream clone's `.git/objects`.
  - The pin matches `source.json` and is recorded in the `SOURCES.md:30` `tdd` row.
- **Rewrite and caps:**
  - The section is a real rewrite. The 5-file upstream example became a 4-line diff, and the shared snippets are trivial.
  - The file is 175 lines, under the 250 cap. The base is 127 lines; both counts match the change map.
- **What was not carried:** no `scripts/`, siblings, `marketplace.json`, `npx` or `/plugin` text, hooks, network use or auto-update. The upstream `skills/prune-tests/` folder holds only `SKILL.md`.
- **Provenance and licence:**
  - Provenance is truthful: `SKILL.md:65`, `SOURCES.md:30` and the change map all say the same thing.
  - The MIT obligations are met under the repo's existing policy. `NOTICE:22-23` says MIT rewrites keep upstream copyrights as pinned in `SOURCES.md`. `SOURCES.md:30` records "MIT (root `LICENSE`, copyright 2026 Maze)". The repo `LICENSE` carries the identical MIT permission text. This matches how the `obra/superpowers` rewrites are handled.
- **Status:** "security intake: pending" is the intended pre-verdict state.

**Q6. GR16, public text and other defects: No issues.**
- None of the four candidate paths touches `brief.md`, an asks file, `## Autonomy` or an `AGENTS.md`.
- Public text is clean. `CHANGELOG.md:35` names no people. The only name is the upstream copyright holder in `SOURCES.md`, which is licence attribution. There are no URLs, hosts or paths that would trip the K10 public-text check.
- No new trust boundary is introduced.

## Security

- **Scan:** the `obielin/skillshield` raw outputs show `SAFE`, risk 0/100 and 0 findings for all four files (`candidate-scan/0.stdout` to `3.stdout`). The stderr files are empty. `index.json` shows the argv with `python3 -I` and return code 0 for each file.
- **My own read:** the content is prose only. There are no executable blocks; the diff example is illustrative test code, not a run step. There are no install commands and no permission broadening.
- **Production code:** the one place that deletes production code (`SKILL.md:87`) is limited to code that only existed for a deleted test, and requires a repo-wide search for other callers first.

## Optional issues (not blocking)

- **O1. Row precedence (`SKILL.md:71-82`).** Rows can overlap, for example a regression test that is also a same-boundary copy. A line such as "If more than one row fits, a Keep row wins" would help small models.
- **O2. Exported hooks (`SKILL.md:87`).** A repo-wide search cannot find outside users of an exported symbol in a published package. Consider "and it is not part of a published API".
- **O3. Unresolved mismatch (`SKILL.md:99`).** It could say outright that the stage then ends `fail`, or point to Mid-build returns ("two requirements cannot both be met").
- **O4. MQ3 wording (`skills-tdd.md:58-61`).** It says old L119 "Suite is green" governs only the red → green cycle. That checklist is headed "Before calling the work done" and still applies to a pruning-only item. The skill text is fine; only the change-map wording is off.

## Verification limits

- **Static review only:** a read-only review of the frozen candidate, base, quarantine and context. Nothing was executed and no model eval was run; the baseline has zero model rows.
- **Blob hashes:** I could not recompute the new body blob `9abc2f66…` cited in `SOURCES.md:30`.
- **Links:** I checked that `../sdlc/references/stage-result.md#schema` and `../sdlc/SKILL.md#asking-the-human` resolve, by reading the headings.
- **No campaigns:** no product, browser or integration runs, as instructed.
