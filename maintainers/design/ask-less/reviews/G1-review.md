# G1 review — DER-730 (A0, SDLC move)

- Verdict: **approve**
- Commit: `61c1a718c377bee3157f0e3e0bc52ae62d11ca8d` (`item/der-730-sdlc-move` HEAD)
- Range: `integrate/ask-less` (`5cb77594294d7298da1bf3b8850f64673da0bdde`)...HEAD. The merge base is `integrate/ask-less` itself. Commits: `02c69b9` (the move) and `61c1a71` (a merge of integrate, which adds only the R110 `lld.md`/`rulings.md` fix; `git diff 02c69b9 61c1a71 --stat` shows those 2 files). A0 base `c26f424` exists (`git cat-file -t` → `commit`).
- Reviewer: clean. I did not build this item and did not read the builder's transcript. Loaded `pr-review`, `yagni` and `docs-google-style`.

## Independent reports: coverage at this HEAD

| Report | Covered commit | Result |
| --- | --- | --- |
| `G1-verify.md` | `61c1a718c377…` = HEAD | **pass** |
| `G1-security.md` (required: body `G1.md` Acceptance bullet 3) | `61c1a718c377…` = HEAD | **accept** |

Both reports cover this exact HEAD, and the tree is clean (`git status --porcelain` → 0 lines), so no later edit falls outside them. I used them as evidence only and re-ran the key checks myself (below).

## Spec

Ticket `G1.md` Outcome and Acceptance, against LLD `lld.md:26-220`:

| Requirement | Result | Evidence |
| --- | --- | --- |
| Steps 0–3, file map (`lld.md:28-41`) | met | `git diff -M --name-status`: 10 `docs/sdlc/*.md` → `skills/sdlc/references/*.md` (R090–R100) and `docs/INTAKE.md` → `skills/sdlc/references/intake.md` (R097). `skills/sdlc/SKILL.md` added, `docs/SDLC.md` modified to the pointer. `skills/sdlc/` holds only `SKILL.md` and the 11 references; no executable files. |
| Step 4, frontmatter (`lld.md:60-65`) | met, exact | `diff` of `lld.md:61-63` against `skills/sdlc/SKILL.md:1-3` is empty; `:4` is `---`; `:5` is `# SDLC`. |
| Step 5, link rules per file class (`lld.md:109-141`) | met | A0 check parts 1 and 2 print nothing beyond their named values. |
| Step 6, pointer (`lld.md:72-78`) | met, exact | `diff` with `docs/SDLC.md` is empty; 7 lines. |
| Step 7, `sdlc` row (`lld.md:85`) | met | `SOURCES.md:20`, directly above `tracker-sdlc` at `SOURCES.md:21`; date filled `2026-11-11`. |
| Step 8, path-edit notes and blobs (`lld.md:88-95`) | met | All 9 named rows end with the sentence before ` \|`. `git hash-object`: `tdd` `47d2478b…`, `security-hardening` `ce33e4c9…`, matching their rows. The security read dated 2026-11-11 (`G1-security.md`). |
| Step 9, writing-standard L141 (`lld.md:96-98`) | met, exact | `maintainers/writing-standard.md:141` reads `[file map](design/ask-less/lld.md#a0-file-map) exist.`; the part 2 diff count is `2`. |
| Step 10, one Unreleased line (`lld.md:1779`) | met, exact | `CHANGELOG.md:24-26`, `### Changed` under `## Unreleased`; part 2 count `1`. |
| Step 11, A0 check | met | All 6 parts pass (see Commands). |
| Path map with protected rows, all `kept` (R47) | met | `maintainers/design/ask-less/rule-maps/a0-path-map.md:54-64` matches `lld.md:210-220` row for row. Its anchor lists (`:16-27`) match the headings I listed from each moved file. MQ: none (`:66-68`). |
| **security** read: skill id, protected rows, SOURCES notes and blobs | met | `G1-security.md` §2–§4, at HEAD. |
| Verify: `wc -l < skills/sdlc/SKILL.md` = 178 | met | Printed `178`. |
| Out of scope: wording changes, A1–A9 | respected | Parts 1–2 prove the edits are path-only. No other file changed. |

Frozen records: HLD, LLD and Groom are not changed by this item. `git diff --name-only integrate/ask-less...HEAD -- maintainers/design` lists only the new path map. Part 2's `git diff --quiet c26f424 -- docs/engineering-with-ai/log.md maintainers/evals maintainers/design ':!maintainers/design/ask-less'` exits 0.

Scope creep: none. All 51 changed files are either in the LLD table (`lld.md:130-141`) or the moved set, or they are the pointer, the path map, or `CHANGELOG.md`.

## Standards

- K1 caps: index 178; references within caps (conventions 100/100, stage-result 150/150, plan-trial-spec 148, groom-step 139, subagents 136, entry-brief-repo 134, build-review 102, stage-result-migration 83, branches-and-lands 69/120, trunk-changelog-monthly 34/80, intake 55/55). `AGENTS.md` 76/100, `maintainers/writing-standard.md` 150/150. Every edited `SKILL.md` is ≤250.
- K2: retired (settled); not run.
- K3: the only hit is the allowed `(per orchestrator …)` contract text (`writing-standard.md:130-132`). The hit count matches `integrate/ask-less`.
- K4: every edited file is mapped in the path map, no MQ is open, and the protected checks are part 6.
- K7: my own link and anchor checker over the changed `.md` files outside `maintainers/design/`, plus the path map, printed nothing. No missing targets and no unresolved anchors, including no later-item anchors, which are deferred to G15 anyway.
- `docs-google-style`: the human-facing files (`README.md`, `CONTRIBUTING.md`, `SECURITY.md`, `docs/ARCHITECTURE.md`, `docs/SDLC.md`, `CHANGELOG.md`) change only paths, or take text the LLD fixes. There is no item-authored wording to judge.
- `yagni`: nothing beyond the ask. No new files except the ones the LLD names and the R47 path map.
- `git diff --check integrate/ask-less...HEAD`: empty, exit 0. Commit subjects cite `[DER-730]`.

## Findings

No blocking findings. No change is required in G1.

Notes only (none is a defect of this item; no action in G1):

1. **The LLD's Claim check tests nothing (confirms security F1).** At `maintainers/design/ask-less/lld.md:190`, the pattern `'^[1-5]\. '` counts 0 lines in the `tracker-sdlc` Claim section, while `'^ *[1-5]\. '` counts 5, because the steps are indented. The row is still proven `kept`: part 2 shows the whole `skills/tracker-sdlc/SKILL.md` equals its old text after `skl`. The LLD is frozen, so the smallest fix belongs to whoever owns the integrated check (E5): use `'^ *[1-5]\. '`.
2. **`SOURCES.md:35`, security-hardening row: "…not a vendor body Path edit DER-712…" has no period between the sentences.** This is the literal result of LLD step 8 (the old cell had no closing period), and part 2 depends on it. It is cosmetic. A9 may add the `.`; G1 must not.
3. **`skills/host-config-pyinfra/SKILL.md` is 276 lines, over the 250 cap.** It was already over the cap before this item, and it is not in this diff.

## Commands and results

From the worktree root, at HEAD `61c1a71`:

- `git rev-parse HEAD` → `61c1a718c377bee3157f0e3e0bc52ae62d11ca8d`; `git rev-parse integrate/ask-less` = merge-base = `5cb77594294d7298da1bf3b8850f64673da0bdde`.
- A0 check: I extracted the link-rules block (`lld.md:109-128`) and the check block (`lld.md:149-193`) from the file at HEAD into `<scratch>/scratch/g1-review/full.sh`, and ran it with `bash`. Full output, exit 0:
  ```
  name: sdlc
  2
  1
  7
  1
  ```
  - Part 1: `name: sdlc` only.
  - Part 2: `2` and `1`, with every other diff empty.
  - Parts 3, 4 and 6: nothing.
  - Part 5: `7` and `1`.
  - A separate run of the part 2 frozen-paths `git diff --quiet` exited 0.
- `wc -l < skills/sdlc/SKILL.md` → `178`.
- Exact-text diffs: frontmatter against `lld.md:61-63` and pointer against `lld.md:72-78` are both empty.
- `git hash-object` for `tdd` and `security-hardening` matches the blobs recorded in `SOURCES.md`.
- Claim indentation: `grep -cE '^ *[1-5]\. '` → 5; `grep -c '^[1-5]\. '` → 0.
- `git diff --check` → empty; `git status --porcelain | wc -l` → 0; executable files under `skills/sdlc` → 0.
- K3 over `$AT` → only the allowed hit; the count matches integrate.
- K7 (`<scratch>/scratch/g1-review/k7.py`, run with `python3 -I`) → no output.

## Limitations

- My K7 slugger approximates GitHub heading slugs. GitHub's renderer is the final authority.
- Later-item anchors are not checked here; they are checked at G15, as the body says.
- I did not repeat the **security** read. I relied on `G1-security.md` at this HEAD for the security-specific checks: secrets and K10, and pins in columns 1–4. I re-ran the protected-row and blob checks myself.
- I edited no repo files, made no commits or pushes, and wrote nothing to the tracker. My only writes are this report and `<scratch>/scratch/g1-review/`.
