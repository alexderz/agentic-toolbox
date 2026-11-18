# DER-800 r2 delta re-review (same reviewer)

**Verdict: MEETS REQUIREMENTS.** The fix closes R1, the only required correction from my r1 review. Everything else I accepted in r1 still stands.

**SECURITY CLEAR** for the text-only scope. There is no security blocker.

## Correction items

**R1 (out-of-scope prune cases reported through `findings`): Closed.**
- **What changed:** `review-r2-source/skills/tdd/SKILL.md:69` now ends "Do not edit a prune case outside that scope." The stage-result link and "so the manager can file it" are gone.
- **Nothing left behind:** I searched the r2 skill for `findings`, `stage-result`, `manager` and "file it". The only hits are the four places I already accepted in r1:
  - L82: keep an unclear case and list it.
  - L89: step 4, list each deleted or rewritten test.
  - L98 and L99: the two failing-test mismatch rows.
  - None of these promises that the manager files or reads anything on a pass.
- **No widening:** `stage-result.md` is not in the candidate, and the delta adds no new channel, step or process.
- **Scope still holds:** the in-scope pruning rules, the coverage rules (regression tests, required absences, contract calls, other-boundary tests), the never-hide-a-regression rule and the TDD cycle all match r1. L3 and L65–L168 are unchanged apart from L69.

**R1 follow-on edits (SOURCES, CHANGELOG, change map MQ2): Closed.**
- **`SOURCES.md:30`** now says "prune cases outside that scope are not edited".
- **`CHANGELOG.md:35`** now says "The builder prunes only tests in the item's scope and does not edit others."
- **Change map:**
  - Adaptations row (`skills-tdd.md:28`) now says "prune cases outside that scope are not edited … no approval gate and no report duty added".
  - MQ2 (`skills-tdd.md:55-57`) now says the rule "adds no report duty or channel for out-of-scope cases; they are left unedited".
- All three match the skill text.

**Pin and edit-order provenance: Closed.**
- **Wording now factual:** `SOURCES.md:30` and the change map header (`skills-tdd.md:13`) both say the source pin and body are "included in the same change before landing". The false claim that the pin came first is gone.
- **History kept:** `author-r3-report.md:28-31` says the author edited the `tdd` body first and the SOURCES row afterwards, so intake step 4 ("pin SHA in SOURCES before the body") was not followed in authoring order. It claims no retroactive compliance and says no body has landed. That matches the disposition and does not rewrite history.
- **Pin unchanged:** `bd73b2ea…`, blob `7821d52f…`.

**MQ3 / O4 (does the checklist apply to pruning?): Closed.**
- `skills-tdd.md:61-64` now says the unchanged "Before calling the work done" checklist (old L114–121, confirmed against the base file) still applies to pruning. It also says this commissions no new whole-suite or mutation run beyond the item's agreed checks.
- The statement is factual, and no TDD rule text changed.
- Wording note, not required: the earlier sentence in MQ3 still says old L119 "governs the red → green cycle". The new sentence settles the effect correctly, so this is cosmetic.

## Scanner evidence (r3 capture)

- **Direct, unfiltered runs:** the r3 capture in `author-r3-evidence/` holds the author's own scans of the four changed paths, run with no pipe.
  - Each `.exit` file reads `0`.
  - Every stdout shows SAFE, risk 0/100 and 0 findings.
  - The scanner's own line counts are 176, 92, 225 and 70.
  - Every stderr file is empty.
- **Scanner and whitespace:** the scanner checkout is HEAD `b1476498…` with 0 dirty entries. `git diff --check` exited 0, but it covers tracked files only, so the untracked change map was not checked. The author says so.
- **Not a security clear on its own:** the scans are evidence, not my verdict. My own read of the delta found only deleted text and reworded bookkeeping. Nothing executable, no URLs and no permission changes were added.

## New risks from this delta

None. The delta removes a promise and corrects bookkeeping. It adds no rule, gate, channel, link or executable content. Leaving out-of-scope prune cases unedited, with no report duty, is the smallest form the disposition asked for. The DoD's "no silent scope leftover" still holds, because those cases were never part of the item's own scope.

## Optional items carried forward

O1, O2 and O3 from r1 remain optional. This delta did not introduce any defect that would make them required.

## Verification limits

- **Read-only:** Read, Grep and Glob only.
- **Not recomputed:**
  - The new body blob `4c698cd7…`.
  - Whether the worktree files the author scanned are byte-identical to `review-r2-source/`. The paths and line counts are consistent, but I did not hash them.
- **Not re-checked:** I did not re-sweep links. The only link that was in L69 has been removed.
- **Bookkeeping:** "security intake: pending" in SOURCES stays as it is until final clearance is recorded.
