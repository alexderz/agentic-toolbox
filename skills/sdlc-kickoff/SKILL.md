---
name: sdlc-kickoff
description: use this to prepare a driven or followed SDLC run before its first stage (prep), to interview the operator into a confirmed brief (gather), or to rebuild a pushed or local run root (restore). do not use to start the driver or a worker, or mid-run.
---

# SDLC kickoff

Three modes, each run by the operator in a normal interactive session
(OpenCode or Claude Code): `prep`, `gather`, `restore`. **No mode starts
the driver or a worker.** Formats and rules for every file named here:
[run-state.md](../../docs/sdlc/run-state.md). Design:
`maintainers/design/solo-dlc/lld.md` (Item 0). No `scripts/`.

Question ids in operator prompts are stable and never reused. Print the
id on the question. Retire an id when its question is dropped; do not
give it to another question. A paid slot's spending ask is `prep-1`.

## Iron law

1. Ask setup questions only, never a product question.
2. Write, cut, or push nothing until the operator replies to the
   checklist preview.
3. Never propose, default, or prefill the toolbox remote. The operator
   types it in full.
4. Run every shell command through [shell-safety](../shell-safety/SKILL.md):
   quote variables, arrays for argv, no `eval`, no operator text in a
   command string.
5. A check you cannot run says `to do` or `unknown`, never `done`.

## Driver commands

`sdlc-driver` and its subcommands (`readiness`, `toolbox`, `state-init`,
`drill`, `persist`, `status`, `restore`) do not exist yet; item 5 builds
them. Until item 5, and for every followed run, durability is `plain`
only. Skip `state-init`, drill, and the genesis note. Do not imitate them.

| Need | Today |
| --- | --- |
| R1-R4 | This skill, below. Walkable now |
| R5-R7, R9, `readiness`, `toolbox` | `to do`, reason `driver not built yet` |
| R8 | Hand check sets the parent-folder word. `0700` is after the reply |
| R10, `state-init`, `drill`, genesis note | `n/a` at `plain`. Do not imitate |
| `persist`, `status`, `restore` | Not available until item 5. Say so; do not imitate |
| Run files | Write by hand per [run-state.md](../../docs/sdlc/run-state.md) |

When a step needs a missing command, print `driver command not available
yet: <name> (item 5)` and carry on with what the skill can do.

## Mode: prep

1. **Setup questions.** One at a time. Print the id. Each has the default
   below except `prep-remote`. Ask `prep-mode` before `prep-level`.
   1. **`prep-remote`.** Ask the operator to type the full toolbox URL.
      No default, no prefill, no suggestion from the repo's remotes.
      Refuse, and ask again, before any fetch, when it breaks the
      [remote rule](../../docs/sdlc/run-state.md#toolbox-copy).
   2. **`prep-trunk`.** Toolbox trunk, default `main`. Refuse a value
      that starts with `-`. Run `fmt=(git check-ref-format --branch "$trunk")`
      then `"${fmt[@]}"`. A non-zero exit asks again.
   3. **`prep-pin`.** After that rule and the trunk check pass, resolve
      the pin from a clean temporary directory. Do not clone. Do not
      fetch into the product repo. Do not read that repo's `.git/config`.
      `"$remote"` is the typed URL. `"$trunk"` already passed
      `prep-trunk`. Set `pin_dir` with `mktemp -d`. `git -C "$pin_dir"
      rev-parse --is-inside-work-tree` must not print `true`. The loop
      copies only `credential.*` and `core.sshCommand` into
      `"$pin_dir/gitconfig"`. Do not copy `url.*.insteadOf` or any
      other key. `GIT_CONFIG_GLOBAL` is that file only. The `env` line
      unsets `GIT_DIR` and `GIT_WORK_TREE` and sets `GIT_CONFIG_COUNT=0`.
      Tags, then the trunk tip. Show the 40-hex. The answer is yes or
      ask again.

      ```sh
      : > "$pin_dir/gitconfig"
      while IFS= read -r -d '' rec; do
        git -C "$pin_dir" config --file "$pin_dir/gitconfig" --add "${rec%%$'\n'*}" "${rec#*$'\n'}"
      done < <(GIT_CONFIG_NOSYSTEM=1 git -C "$pin_dir" config --global --null --get-regexp '^(credential\..*|core\.sshCommand)$' || true)
      pin=(git -C "$pin_dir" -c protocol.file.allow=never -c protocol.ext.allow=never ls-remote --tags -- "$remote")
      env -u GIT_DIR -u GIT_WORK_TREE GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_GLOBAL="$pin_dir/gitconfig" GIT_CONFIG_COUNT=0 GIT_ALLOW_PROTOCOL=https:ssh "${pin[@]}"
      tip=(git -C "$pin_dir" -c protocol.file.allow=never -c protocol.ext.allow=never ls-remote -- "$remote" "refs/heads/$trunk")
      env -u GIT_DIR -u GIT_WORK_TREE GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_GLOBAL="$pin_dir/gitconfig" GIT_CONFIG_COUNT=0 GIT_ALLOW_PROTOCOL=https:ssh "${tip[@]}"
      ```

      A release tag matches `^v[0-9]+(\.[0-9]+)*$`. Pass only matching
      names as argv to `printf '%s\n'`, and pipe that stdout to `sort -V`.
      Do not pass the names to `sort` as file operands. The pin is the
      peeled 40-hex of the last line, the `^{}` line when it exists. No such tag: the trunk command's 40-hex is the pin.
   4. **`prep-repo`.** Origin name, repo trunk, project-main, design
      folder, test command or `null`. Run `git check-ref-format --branch`
      on `"$origin"` the same way as `prep-trunk`. Refuse a non-zero
      exit. Do not put a refused origin in a refspec.
   5. **`prep-slug`.** Chunk slug and Epic title. Accept the slug only
      when it matches `^[a-z0-9]+(-[a-z0-9]+)*$`. Then set
      `project_main=integrate/$slug`. Run `git check-ref-format --branch`
      on `"$trunk"` and on `"$project_main"` the same way as `prep-trunk`.
      Refuse a non-zero exit.
   6. **`prep-tracker`.** Required; the Epic is filed here, so it cannot
      be `deferred`. Driven runs support `local` only. For any other
      answer say `tracker backend <name> is not supported for driven
      runs yet; use local` and ask again. With no tracker connected,
      offer `local` (a `tickets` branch). If the repo is public, say
      before anything is written: the `tickets` branch and every ticket
      title, body, and comment on it are public. A public repo has no
      default; the choices are use `local`, or name another repo.
      Silence writes nothing.
   7. **`prep-harness`.** Harness name, pinned version, each model slot.
      A paid slot asks the operator's spending words as `prep-1`.
   8. **`prep-root`.** Run root, default
      `$XDG_STATE_HOME/sdlc/<chunk-slug>/`
      (`~/.local/state/sdlc/<chunk-slug>/` when unset).
   9. **`prep-mode`.** Ask driven or followed. Record driven as `mode`
      `enforced`. Record followed as `followed`.
   10. **`prep-level`.** When the answer is followed, or item 5 has not
       landed, do not ask. Set `plain` and say why. When the answer is
       driven, item 5 has landed, and the repo is public, say first that
       the state branch (brief, prose, `state.md`, verbatim answers)
       would be public, and offer `pushed`, `local`, and `plain` with no
       default. When it is driven, item 5 has landed, and the repo is
       not public, the default is `pushed`.
   11. **`prep-backup`.** Backup folder, default none.
2. **Readiness preview.** Print one line per check, each `done`,
   `to do`, `deferred`, or `n/a`, then stop. The preview writes nothing.

   | # | Check | Today |
   | --- | --- | --- |
   | R1 | Tracker | [R1](#r1-r4-checks) |
   | R2 | Branches | [R2](#r1-r4-checks) |
   | R3 | Push permission | [R3](#r1-r4-checks) |
   | R4 | Branch protection and CI | [R4](#r1-r4-checks) |
   | R5 | Harness and plugin | `to do`: driver not built yet (`readiness`) |
   | R6 | Models | `to do`: driver not built yet (`readiness`) |
   | R7 | Toolbox | `to do`: driver not built yet (`toolbox`) |
   | R8 | Run root | Parent-folder word from the hand check. `0700` after the reply |
   | R9 | Labels | `to do`: driver not built yet; say `short` when the key pattern allows ids over 23 characters |
   | R10 | State | `plain`: `n/a` |

   R8 hand check, read only. The parent exists, `test ! -L "$parent"`
   passes, and `git -C "$parent" rev-parse --is-inside-work-tree` is not
   `true`. When all of that holds, the word is `done`. Else `to do`.
   Do not mark `0700` here.
3. **After the operator replies**, in this order. Still no Gather.
   1. R2's cut and push, if the reply approved them, using the R2 argv.
      Never `--force`.
   2. File the Epic through
      [tracker-sdlc](../tracker-sdlc/SKILL.md) (`create`, type `epic`,
      under the repo's own skill). Record the id.
   3. Create the run root `0700`. Write `run.json`, `machine.json`
      (`0600`), `checklist.md` (the preview as answered), and empty
      `refiner/run-1/` and `gatherer/run-1/`, per
      [run-state.md](../../docs/sdlc/run-state.md). `mode` is `enforced`
      or `followed`. `state.level` is the `prep-level` result. `run.json`
      holds no absolute path, host name, address, or credential. Stop
      and revise on a
      [scan pattern](../../docs/sdlc/run-state.md#scan-patterns) hit.
      Write each file as that doc says: a temporary file in the same
      folder, `fsync`, then `rename`.
   4. While the level is `plain`, skip `state-init`, drill, and the
      genesis note. Do not imitate them.
4. **Print** `next: Gather; open a new session and load sdlc-kickoff in
   gather mode for RUN_ROOT` only after `run.json` is on disk. Discard
   this session. Do not start Gather here.

### R1-R4 checks

Run in the repo checkout. `"$origin"` is the remote name from
`prep-repo`, and only after `git check-ref-format --branch` on it
exits 0. Use `"$trunk"` and `"$project_main"` only after `prep-trunk`
and `prep-slug` pass. Read only, until the reply. Each git call is one
argv array. Never paste an unquoted refspec into a command string.

- **R1 Tracker.** The repo's `.agents/tracker/SKILL.md` exists, names
  the `local` backend, and carries a `read` recipe. Run
  `r1=(git ls-remote --heads -- "$origin" tickets)` then `"${r1[@]}"`.
  No `tickets` ref: `to do` (bootstrap needs the operator's approval in
  [local adapter](../tracker-sdlc/adapters/local.md)). Missing repo
  skill: `to do`, run
  [sdlc-onboarding](../sdlc-onboarding/SKILL.md) first.
- **R2 Branches.** `r2=(git ls-remote --heads -- "$origin" "$trunk")`
  then `"${r2[@]}"` must show the trunk, else `to do` and stop.
  Project-main is `done` when
  `r2b=(git ls-remote --heads -- "$origin" "$project_main")` shows it.
  Else `to do`, and after the reply
  `push=(git push -- "$origin" "${trunk}:refs/heads/${project_main}")`
  then `"${push[@]}"`, never `--force`.
- **R3 Push permission.** `fetch=(git fetch -- "$origin")` then
  `"${fetch[@]}"`. When project-main exists,
  `dry=(git push --dry-run -- "$origin" "refs/remotes/${origin}/${project_main}:refs/heads/${project_main}")`.
  When it does not,
  `dry=(git push --dry-run -- "$origin" "refs/remotes/${origin}/${trunk}:refs/heads/${project_main}")`.
  Then `"${dry[@]}"`. Exit `0` is `done`. It authenticates without
  moving a ref. When the branch is not cut yet, say the first real push
  also proves branch creation.
- **R4 Protection and CI.** CI at the project-main tip
  (`.github/workflows/`, `.gitlab-ci.yml`, or the repo's own) is
  `present` or `absent`. When `gh auth status` is ok, run
  `view=(gh repo view --json nameWithOwner --jq .nameWithOwner)` then
  `"${view[@]}"`. A non-zero exit, or a value that is not one non-empty
  owner, one `/`, and one non-empty name, is `unknown` for both
  branches. Do not call `repos/OWNER/REPO/...`. Split a good value into
  `"$owner"` and `"$repo"`. For `"$b"` of `"$project_main"` and of
  `"$trunk"`, run `api=(gh api --include -- "repos/${owner}/${repo}/branches/${b}/protection")`
  then `"${api[@]}"`. The first line is the HTTP status. 403 is
  `unknown`. 404 is `unknown`. Do not record `none` for 403 or 404.
  Any other status than 200 is `unknown`, which the operator confirms.
  A 200 rule that blocks a direct, non-force push to project-main is `to do`.

## Mode: gather

Run in a **new** session, and only after `RUN_ROOT/run.json` exists.
Until item 5, stop when `state.level` is not `plain`.

1. Read `run.json` and `checklist.md`. If either is missing, stop and
   say to run `prep`.
2. Load [discover-the-idea](../discover-the-idea/SKILL.md) and interview
   the operator on their brain dump.
3. End with a brief; read it back in words, and wait for the operator to
   confirm in words. No confirmation, no write.
4. Write `RUN_ROOT/gatherer/run-1/brief.md` with a temporary file,
   `fsync`, then `rename`. Copy this session's file next to it, and
   list the copy in `machine.json` `gather.sessions` (run-root-relative).
   If no session file can be found, say so and list nothing.
5. At `plain`, there is nothing to persist. For `pushed` or `local`,
   print `driver command not available yet: persist (item 5)`. Do not
   imitate it.
6. Print the run root and the start line. OpenCode: `pick /sdlc, then
   enter RUN_ROOT`. Pi: `/sdlc RUN_ROOT`. Item 8 is not landed. Stop
   after the brief and this note.

## Mode: restore

For a machine without the run root. A `plain` run has nothing to
restore. Question ids: `restore-bin`, `restore-root`, `restore-backup`.

1. Ask only those machine-local questions: harness executable and Node
   paths, run-root location, backup folder. Never ask the toolbox remote
   or trunk here. The first `/sdlc` asks them from the genesis note.
2. Run R5, R6, and R8. R5 and R6 are `to do` until item 5. R8 uses the
   prep hand check. Write a new `machine.json` with a new `hostId`
   (32 random hex digits) by temporary file, `fsync`, then `rename`.
3. Print `driver command not available yet: restore (item 5)`. Do not
   imitate it.
4. Print the start line as in Gather, including the item 8 stop note.

## Standing rules

- Public repo: no people's names, internal hostnames, IPs, or
  credentials in anything this skill writes.
- Never write a credential to `run.json`, `machine.json`, or
  `checklist.md`. Refuse `apiKey` or header values from provider config.
- Report outcomes as they are. A check you skipped is `to do`.
