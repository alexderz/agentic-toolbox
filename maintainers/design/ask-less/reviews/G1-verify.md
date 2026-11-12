# G1 verify — DER-730 (A0, SDLC move)

- Verdict: **pass**
- Commit: `61c1a718c377bee3157f0e3e0bc52ae62d11ca8d` (`item/der-730-sdlc-move`)
- Compared: `integrate/ask-less` (`5cb7759`)...HEAD; A0 base `c26f424` (ancestor of integrate: yes)
- Verifier: clean, did not build; builder transcript not read.

## Findings

None blocking. No fix required.

Observations (no action needed):

1. `skills/host-config-pyinfra/SKILL.md` is 276 lines (>250 SKILL cap,
   `maintainers/writing-standard.md:47`). It is 276 at `c26f424` too and
   is not in this item's diff, so it falls outside the scoped K1.
2. The A0 changelog line (`CHANGELOG.md:26`) and pointer
   (`docs/SDLC.md:1-7`) write paths without code font. That text is
   copied exactly from the LLD (`lld.md:72-80`, `lld.md:1781`), so it
   is not a finding against this item.
3. The `security-cleared 2026-11-11` dates (`SOURCES.md:20` plus the 9
   notes) say when **security** read the item. The read itself happens
   at Review, so this check doesn't cover it.

## Acceptance

| Bullet | Result | Evidence |
| --- | --- | --- |
| Step 0–3 file map, `git mv` | pass | `git diff -M --name-status`: 11 `docs/sdlc/*` → `skills/sdlc/references/*` (R090–R100), `docs/INTAKE.md` → `references/intake.md` (R097); `skills/sdlc/SKILL.md` A, `docs/SDLC.md` M (pointer) |
| Step 4 frontmatter | pass | `diff` of the LLD yaml block (`lld.md:57-61`) with `head -4 skills/sdlc/SKILL.md`: empty; line 5 is `# SDLC` |
| Step 5 link rules per class | pass | A0 check parts 1–2 empty |
| Step 6 pointer | pass | `diff` of the LLD block (`lld.md:72-80`) with `docs/SDLC.md`: empty; 7 lines |
| Step 7 `sdlc` row | pass | `SOURCES.md:20`, directly above `tracker-sdlc` `SOURCES.md:21`, first table row; matches LLD text with the date filled in |
| Step 8 notes and blobs | pass | All 9 rows end with the sentence before ` \|`; 9 matches. Blobs `tdd` 47d2478b…, `security-hardening` ce33e4c9… equal `git hash-object` of the current files |
| Step 9 writing-standard L141 | pass | The only diff after `mnt` is 141c141 old→new, exactly as in `lld.md:93-94` |
| Step 10 changelog | pass | One `+- ` line, under `## Unreleased` / `### Changed` (`CHANGELOG.md:24-26`), text equal to `lld.md:1781` |
| Step 11 A0 check | pass | see below |
| Path map (R47) | pass | `maintainers/design/ask-less/rule-maps/a0-path-map.md`; protected-rows table equals LLD's (`lld.md:208-220`), every row `kept`; MQ "None". Anchor lists checked against the files: all present (`needs_input` heading at `stage-result.md:135`) |
| security read at Review | n/a here | Review step; see limitation 3 |

Scope: 51 files changed. Every one is in the LLD table or the path map
(37 edited + 12 moved + pointer + path map). `hld.md`, `lld.md`,
`groom.md`, `rulings.md`, `comparables.md` and `reviews/` are unchanged
against integrate (`git diff --quiet` exit 0). The commits cite
`[DER-730]`. The tree is clean (`git status --porcelain` shows 0 lines).

## Commands and results

`lldblock` is defined from `groom.md:34` and reads `integrate/ask-less:lld.md`.
It extracts the rule sets (`#### A0 link rules`, 18 lines) and the check block
(`#### A0 check`, 43 lines). Both ran in one bash script, with part markers added.

- Part 1: printed only `name: sdlc` (expected).
- Part 2: printed `2` (writing-standard, L141 only) and `1` (changelog entry);
  root, SOURCES, skl, arc, ssp, kn and mnt diffs were empty. The frozen-records
  `git diff --quiet` exited with 0.
- Part 3: printed nothing.
- Part 4: printed nothing.
- Part 5: `7` (≤8), `1`.
- Part 6: printed nothing (security-hardening and tracker-sdlc Never and
  Ask first rows, Claim 1–5, intake 6 steps, K5 local.md).
- Script exit 0. `wc -l < skills/sdlc/SKILL.md` printed `178` (expected 178).
- `git diff --check integrate/ask-less...HEAD` printed nothing, exit 0.
- K1 (scoped): index 178 ≤200; references ≤ caps (conventions 100/100,
  stage-result 150/150, plan-trial-spec 148, branches-and-lands 69/120,
  trunk 34/80, intake 55/55); AGENTS.md 76 ≤100; writing-standard 150 ≤150;
  every edited SKILL.md ≤250.
- K2: retired (settled); not run.
- K3 over `$AT`: one hit, `skills/tracker-sdlc/SKILL.md:76` `(per orchestrator …)`,
  the allowed contract exception (`writing-standard.md:131`). The same hit is at base.
- K4: every edited file is mapped in the path map; no open MQ; protected
  checks = part 6. The public-repo rule (`AGENTS.md:16-31`) has no diff hunks.
  The `AGENTS.md` hunks start at L38 and change links only.
- K7: a Python check over the 50 changed `.md` files, without
  `maintainers/design/`. Every relative link target exists, and every
  `#anchor` matches a heading slug or `<a id>`. It found 0 bad links and
  0 later-item anchors. Later anchors (liaison, `#refine`, `#escalation`,
  `#touchpoints`, `#while-a-question-is-open`) are deferred to G15.
- Tone check (human deliverables): `docs/SDLC.md`, `README.md`,
  `CONTRIBUTING.md`, `docs/ARCHITECTURE.md` and `CHANGELOG.md` changed
  paths only, or took LLD-fixed text. No item-authored wording to judge.

## Limitations

- The K7 anchor slugger is my own approximation of GitHub slugs. It
  strips `_`, so it first flagged `needs_input`. I checked that heading
  by hand.
- I didn't verify that the **security** read happened. It is a Review
  step.
- Scratch files are in `<scratch>/scratch/G1v/`.
