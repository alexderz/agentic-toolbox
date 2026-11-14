# G1 (DER-730, A0 SDLC move) — security read

- **Verdict: accept**
- **Commit:** `61c1a718c377bee3157f0e3e0bc52ae62d11ca8d` (`item/der-730-sdlc-move` HEAD)
- **Range read:** `integrate/ask-less...HEAD`. The merge base is `5cb77594294d7298da1bf3b8850f64673da0bdde` (= `integrate/ask-less`). There are 51 files, all `.md`: commit `02c69b9` plus merge `61c1a71`. The merge brings in only integrate's `lld.md`/`rulings.md` R110 fix, and `git diff integrate/ask-less HEAD -- maintainers/design ':!…/rule-maps'` is empty.
- **Security-read date (America/Chicago):** 2026-11-11. `TZ=America/Chicago date` printed `Wed Nov 11 10:49:27 PM CST 2026`. This is the same date the builder wrote in `SOURCES.md`, so the `security-cleared 2026-11-11` stamps are correct.
- **Reader:** clean security reader. I did not build this item and did not read the builder's transcript.

## What I read

- `<scratch>/build/bodies/G1.md`, `AGENTS.md`, `maintainers/AGENTS.md`, `maintainers/writing-standard.md`.
- `maintainers/design/ask-less/lld.md`:
  - A0 file map, steps, link rules and check (L26–220)
  - Trust boundaries (L1671–1685)
  - Guardrails (L1744–1764)
  - Changelog lines (L1773–1790)
- `skills/security-hardening/SKILL.md` and `skills/sdlc/references/intake.md` (the post-G1 intake).
- The whole item diff, in particular the files below.
  - `SOURCES.md`, `docs/SDLC.md`, `CHANGELOG.md`
  - `skills/security-hardening/SKILL.md`, `skills/tracker-sdlc/SKILL.md`, `skills/grok-acp/SKILL.md`
  - `maintainers/writing-standard.md`
  - the new `skills/sdlc/SKILL.md` frontmatter
  - `maintainers/design/ask-less/rule-maps/a0-path-map.md`

## Scoped checks and results

### 1. LLD A0 check, parts 1–6

I ran it verbatim: LLD L110–127 plus L150–192, extracted to `<scratch>/scratch/G1-sec/a0check.sh`, run from the repo root. Exit 0. Full output:

```
name: sdlc
2
1
7
1
```

- **Part 1:** every moved file equals its old file after its rule set. The output above has no diff lines.
- **Part 2:** every edited file equals its old file after its rule set. The writing standard has `2` changed lines (L141 only). `CHANGELOG.md` has `1` entry. A separate run of `git diff --quiet c26f424 -- docs/engineering-with-ai/log.md maintainers/evals maintainers/design ':!maintainers/design/ask-less'` exited 0.
- **Part 3:** no old path is left outside the exempt files.
- **Part 4:** every relative link in a changed file resolves.
- **Part 5:** `docs/SDLC.md` is `7` lines, and `id="asking-the-human"` appears `1` time.
- **Part 6:** the protected-row counts match:

| Protected section | Old count | New count |
| --- | --- | --- |
| `security-hardening` Never | 11 | 11 |
| `security-hardening` Ask first | 10 | 10 |
| `tracker-sdlc` Never | 12 | 12 |
| `tracker-sdlc` Ask first | 4 | 4 |
| `tracker-sdlc` Claim | 0 | 0 (see F1) |

  The intake checklist has 6 steps. `adapters/local.md` is unchanged.

### 2. Skill id `sdlc` (first-party)

- `skills/sdlc/SKILL.md:1-4` matches the LLD step 4 frontmatter byte for byte (diffed against `lld.md:61-64`). It has `name: sdlc` and no `allowed-tools`, commands, hooks or network.
- `skills/sdlc/` holds only `SKILL.md` and `references/*.md`: 12 prose files, no `scripts/`, and no executable files (`find -perm -u+x` found none).
- `SOURCES.md:20`: the `sdlc` row matches LLD step 7 (`lld.md:85`) exactly, with `YYYY-MM-DD` filled as `2026-11-11`.
  - It sits directly above `tracker-sdlc` (`SOURCES.md:21`).
  - Upstream is `first-party (this repo)`, SHA is `first-party`, license MIT.
  - This satisfies intake checklist step 4 (`skills/sdlc/references/intake.md:24-26`).
- No other skill id was added or reminted.

### 3. Protected rows: each disposition `kept`

The path map (`rule-maps/a0-path-map.md:54-64`) matches LLD `lld.md:210-220` row for row. I checked each row directly, beyond what part 6 counts:

| Row | Evidence |
| --- | --- |
| `security-hardening` Never and Ask first: kept (links only) | Both sections are byte-identical to `c26f424` after the path rule. The only hunks are `skills/security-hardening/SKILL.md:71` and `:79` (Roles links). |
| Intake checklist: kept | `## Checklist` differs only at `skills/sdlc/references/intake.md:24`: `../SOURCES.md` → `../../../SOURCES.md`. |
| `tracker-sdlc` Claim, Never, Ask first: kept (links only) | Claim (`skills/tracker-sdlc/SKILL.md:37-81`) is byte-identical (`diff` empty). Never equals old after `skl`. Ask first is identical. The only hunks are at `:9`, `:18`, `:23`, `:156`, `:165-166` (links). |
| `adapters/local.md` recipe: kept (untouched) | No diff. K5 awk recipe compare is empty. |
| `grok-acp` posture, labels, own-item limits: kept (links only) | 4 link-only hunks at `skills/grok-acp/SKILL.md:89,110,114,119`. |
| Public-repo rule, `AGENTS.md`: kept (untouched) | `## Public repo` section (`AGENTS.md:16-32`) is byte-identical to `c26f424`. The `AGENTS.md` changes elsewhere are only the `root` path rule (part 2). |
| SDLC index `#roles`/`#tracker`, `branches-and-lands.md#never`, `subagents.md#tracker-writes`: kept | Covered by part 1: each whole file equals the old one after the path rule. |

### 4. `SOURCES.md` notes, pins and blobs

- I compared columns 1–4 (Skill, Upstream, SHA, License) of every row on `integrate/ask-less` against HEAD, excluding the new `sdlc` row. The diff is empty, so **pins are unchanged**.
- The DER-712 note appears on exactly the 9 rows LLD step 8 names: `ux-design`, `tdd`, `pr-review`, `security-hardening`, `shell-safety`, `verify-before-done`, `golang-testing`, `golang-security`, `ui-craft`.
- New body blobs, checked with `git hash-object`:
  - `skills/tdd/SKILL.md` → `47d2478bfb11e2b07344c8bad960f8cc7aa22f2b`. This matches `SOURCES.md` (tdd row).
  - `skills/security-hardening/SKILL.md` → `ce33e4c93167abf513ef617222fe99dd0c350b1f`. This matches `SOURCES.md` (security-hardening row).
- Every edit to a vendor-derived body is path-only: part 2 covers it with the `skl` set. I cleared these bodies for this move: `tdd`, `pr-review`, `shell-safety`, `verify-before-done`, `golang-testing`, `golang-security`, `ux-design`, `ui-craft`. Their upstream SHAs stay pinned. No intake re-scan is needed, because no third-party content changed.

### 5. Trust boundaries, authority, gates

- **No new gate or permission bypass.**
  - No Never or Ask-first row was added, removed or reworded.
  - No intake step changed.
  - Nothing new grants permission to install, `npx`, push or write to the tracker.
  - `docs/SDLC.md` is the exact 7-line pointer from LLD step 6 (`diff` against `lld.md:72-78` is empty). It carries no instruction beyond the redirect.
- **Authority change (accepted design, not reopened).** Intake and the SDLC now sit under `skills/`. They therefore fall under "Changing a skill body is maintainer work: Intake plus a new **security** cut" (`AGENTS.md:55`) and the `sdlc` `SOURCES.md` row. This is what the LLD intends (`lld.md:17-20`, step 7). It is not a new guardrail.
- **Frozen records.** HLD, LLD and Groom are unchanged against integrate. The only file added under `maintainers/design/` is the rule map. `maintainers/evals/**`, `docs/engineering-with-ai/log.md` and `packages/` are unchanged. No file outside `.md` changed.

### 6. Secrets and private content

- K10 regex on the item diff gives 1 hit. `knowledge/ai/vendors/security-skill-packs-2026-10-18.md` contains `https://github.com/cisco-ai-defense/skill-scanner`. That URL is already in the file and is an allowed upstream reference; only the relative intake link on that line changed (the `kn` rule).
- A wider grep for keys, tokens, private keys, credential prefixes, private filesystem paths, the host user, and the user's domain found 0 hits. Search patterns are paraphrased for publication.
- No names, hosts or private paths were added.

### 7. Writing-standard checks (scoped to this ticket)

- **K1 caps:** all within cap.

| File | Lines | Cap |
| --- | --- | --- |
| `skills/sdlc/SKILL.md` | 178 | ≤250 (A8 cap; also ≤200 under the current standard 9) |
| `branches-and-lands.md` | 69 | ≤120 |
| `build-review.md` | 102 | ≤150 |
| `conventions.md` | 100 | ≤100 |
| `entry-brief-repo.md` | 134 | ≤150 |
| `groom-step.md` | 139 | ≤150 |
| `plan-trial-spec.md` | 148 | ≤150 |
| `stage-result.md` | 150 | ≤150 |
| `stage-result-migration.md` | 83 | ≤150 |
| `subagents.md` | 136 | ≤150 |
| `trunk-changelog-monthly.md` | 34 | ≤80 |
| `intake.md` | 55 | ≤55 |
| `docs/SDLC.md` | 7 | ≤8 |
| `maintainers/writing-standard.md` | 150 | ≤150 |
| `AGENTS.md` | 76 | ≤100 |

- **K2:** retired, so not applied.
- **K3:** one hit, `skills/tracker-sdlc/SKILL.md:76` `(per orchestrator …)`. This is the documented contract-text exception (`writing-standard.md:130-132`).
- **K4:** the path map is present, has no open MQ (`a0-path-map.md:66-68`), and the protected checks pass.
- **K7:** my anchor checker (`<scratch>/scratch/G1-sec/anchors.py`, GitHub-style heading slugs plus `<a id>`) runs over every `.md` changed since `c26f424` outside `maintainers/design/`. It prints nothing. The file-map anchor `design/ask-less/lld.md#a0-file-map` (`writing-standard.md:141`) resolves. Anchors that later items create are deferred to G15, as the body says.
- **Changelog:** exactly 1 A0 entry, in the LLD's exact text, under `## Unreleased` → `### Changed` (`CHANGELOG.md:24-26`).

## Findings

No finding blocks acceptance. Both observations are low severity and none needs a change in this item.

- **F1 (low, check strength; no fix in G1):** the LLD part 6 Claim check `rows 'Claim' '^[1-5]\. '` (`maintainers/design/ask-less/lld.md:190`) passes without testing anything.
  - In `skills/tracker-sdlc/SKILL.md`, the Claim steps are indented (`  1.`; there are 5 matching `^ +[1-5]\. `). The unindented pattern counts 0 in both the old and the new file, so the check passes whatever the Claim section says.
  - The row is still proven `kept` for G1: the Claim section is byte-identical to `c26f424` (`diff` empty), and part 1/2 cover the whole file.
  - The LLD is frozen, so I am not asking G1 to change it. Smallest fix, for whoever owns the integrated check (E5 / the writing standard's protected-rules row): use `'^ *[1-5]\. '`.
- **F2 (cosmetic, LLD-literal; no fix required):** at `SOURCES.md` (security-hardening row), the old Notes cell had no closing period, so the appended note reads "…not a vendor body Path edit DER-712…".
  - This is exactly what LLD step 8 produces (`lld.md:88-95`, "append … before its closing ` |`"), and A0 check part 2 depends on it.
  - It has no security impact, and the pin, blob and clear date are correct.
  - If a later item (A9 touches `SOURCES.md` notes) wants to tidy it, the smallest fix is a `.` after "body". G1 should not do this.

## Limitations

- This is a text and diff read plus the read-only commands above. I ran no evaluation runner and make no claim about one. The E1 runner, isolation, probe and records checks are not in G1's scope.
- I ran no third-party scanner, because no third-party content changed.
- The K7 heading-slug rules are approximated in my script; GitHub's renderer is the final authority.
- Anchors that later items create are not checked here; per the body, they are checked at G15.
- I edited no repo file and committed, pushed or wrote to the tracker nothing. My only writes are this report and `<scratch>/scratch/G1-sec/` (`a0check.sh`, `a0check.out`, `anchors.py`).
