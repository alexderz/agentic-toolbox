---
name: sdlc-kickoff
description: use this to set up a driven SDLC run before its first stage (prep), to interview the operator into a confirmed brief for that run (gather), or to rebuild a run root on a machine that lost it (restore). do not use to start the driver or a worker, or mid-run.
---

# SDLC kickoff

Three modes, each run by the operator in a normal interactive session
(OpenCode or Claude Code): `prep`, `gather`, `restore`. **No mode starts
the driver or a worker.** Formats and rules for every file named here:
[run-state.md](../../docs/sdlc/run-state.md). Design:
`maintainers/design/solo-dlc/lld.md` (Item 0). No `scripts/`.

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
them. Until then:

| Need | Today |
| --- | --- |
| R1–R4 | This skill, below. Walkable now |
| R5–R10, `readiness`, `toolbox`, `drill` | Driven only. List the line as `to do`, reason `driver not built yet` |
| `state-init`, `persist`, `status`, `restore` | Driven only. Say so; do not imitate them by hand |
| Run files (`run.json`, `machine.json`, `checklist.md`, folders) | Write by hand per [run-state.md](../../docs/sdlc/run-state.md). Followed-mode runs are `plain` and need no state branch |

When a step needs a missing command, print `driver command not available
yet: <name> (item 5)` and carry on with what the skill can do.

## Mode: prep

1. **Setup questions.** One at a time, each with its default except the
   first:
   1. **Toolbox remote.** Ask the operator to type the full URL. No
      default, no prefill, no suggestion from the repo's remotes.
      Refuse, and ask again, before any clone or fetch, when it breaks
      the [remote rule](../../docs/sdlc/run-state.md#toolbox-copy):
      not `https://host/path`, `ssh://host/path`, or `[user@]host:path`;
      host starting with `-`; whitespace or control character;
      a `<transport>::` prefix; `file://`; a local path; a password or
      token in user info; a query string.
   2. **Toolbox trunk**, default `main`. It must pass
      `git check-ref-format --branch` and not start with `-`.
   3. **Pin**: newest release tag on that trunk, else the trunk tip.
      Read it only with the remote rule passed; show the 40-hex commit.
   4. **Repo**: origin, trunk, project-main
      (`integrate/<chunk-slug>`), design folder, test command or `null`.
   5. **Chunk slug and Epic title.** Slug: lowercase, hyphens, ASCII.
   6. **Tracker.** Required; the Epic is filed here, so it cannot be
      `deferred`. Driven runs support `local` only. For any other
      answer say `tracker backend <name> is not supported for driven
      runs yet; use local` and ask again. With no tracker connected,
      offer `local` (a `tickets` branch). If the repo is public, say
      before anything is written: the `tickets` branch and every ticket
      title, body, and comment on it are public. A public repo has no
      default; the choices are use `local`, or name another repo.
      Silence writes nothing.
   7. **Harness and models**: harness name, pinned version, each model
      slot; a paid slot needs the operator's spending words.
   8. **Run root**, default `$XDG_STATE_HOME/sdlc/<chunk-slug>/`
      (`~/.local/state/sdlc/<chunk-slug>/` when unset).
   9. **Durability level**: `pushed`, `local`, or `plain`. Public repo:
      warn that the state branch (brief, prose, `state.md`, verbatim
      answers) would be public, and offer all three with no default;
      otherwise default `pushed`. A followed-mode run offers `plain`
      only.
   10. **Backup folder**, default none.
2. **Readiness preview.** Print one line per check, each `done`,
   `to do`, `deferred`, or `n/a`, then stop. The preview writes nothing.

   | # | Check | Today |
   | --- | --- | --- |
   | R1 | Tracker | [R1](#r1-r4-checks) |
   | R2 | Branches | [R2](#r1-r4-checks) |
   | R3 | Push permission | [R3](#r1-r4-checks) |
   | R4 | Branch protection and CI | [R4](#r1-r4-checks) |
   | R5 | Harness and plugin | `to do`: driven only (`readiness`) |
   | R6 | Models | `to do`: driven only (`readiness`) |
   | R7 | Toolbox | `to do`: driven only (`toolbox`) |
   | R8 | Run root | `to do`: driven only (`readiness`); check by hand below |
   | R9 | Labels | `to do`: driven only (`readiness`); say `short` when the key pattern allows ids over 23 characters |
   | R10 | State | `plain`: `n/a`. Else `to do`: driven only (`state-init`, `drill`) |

   R8 by hand: parent outside every git worktree, not a symbolic link.
3. **After the operator replies**, in this order:
   1. R2's cut and push, if the reply approved them.
   2. File the Epic through
      [tracker-sdlc](../tracker-sdlc/SKILL.md) (`create`, type `epic`,
      under the repo's own skill). Record the id.
   3. Create the run root `0700`. Write `run.json`, `machine.json`
      (`0600`), `checklist.md` (the preview as answered), and empty
      `refiner/run-1/` and `gatherer/run-1/`, per
      [run-state.md](../../docs/sdlc/run-state.md). `run.json` holds no
      absolute path, host name, address, or credential; stop and revise
      if a [scan pattern](../../docs/sdlc/run-state.md#scan-patterns)
      hits. Atomic writes: temp file in the folder, `mv`.
   4. Driven runs: `sdlc-driver toolbox`, `readiness`, `state-init`,
      then `drill` (not available yet; `to do`). In the `state-init`
      turn print the only genesis note:
      `keep off this machine: genesis <40-hex>  toolbox <remote>  trunk <trunk>; a restore asks for all three`,
      with the typed remote and the trunk. At `plain`, no note.
4. **Print** `next: Gather; open a new session and load sdlc-kickoff in
   gather mode for RUN_ROOT`, with the real path. Discard this session;
   the answers live in the files.

### R1–R4 checks

Run in the repo checkout, with the remote's name from the operator's
repo answer (`origin` below). Read only, until the operator's reply.

- **R1 Tracker.** The repo's `.agents/tracker/SKILL.md` exists, names
  the `local` backend, and carries a `read` recipe; `git ls-remote
  --heads origin tickets` shows the branch, or `to do` (bootstrap needs
  the operator's approval in
  [local adapter](../tracker-sdlc/adapters/local.md)). Missing repo
  skill: `to do`, run
  [sdlc-onboarding](../sdlc-onboarding/SKILL.md) first.
- **R2 Branches.** `git ls-remote --heads origin <trunk>` must show the
  trunk, else `to do` and stop. Project-main: `done` if it exists on
  `origin`; else `to do`, and after the reply
  `git push origin <trunk>:refs/heads/<project-main>`, never `--force`.
- **R3 Push permission.** `git push --dry-run origin
  <project-main>:refs/heads/<project-main>`: exit `0` is `done`; it
  authenticates without moving a ref. With project-main not yet cut,
  dry-run the push from trunk and say the first real push also proves
  branch creation.
- **R4 Protection and CI.** CI config at the project-main tip
  (`.github/workflows/`, `.gitlab-ci.yml`, or the repo's own): `present`
  or `absent`. Protection on project-main and trunk: with `gh auth
  status` ok for the host, `gh api repos/OWNER/REPO/branches/<b>/protection`
  (a 404 is `none`); else `unknown`, which the operator confirms. A rule
  that blocks a direct, non-force push to project-main is `to do`.

## Mode: gather

Run in a **new** session, after prep. Needs `RUN_ROOT` with `run.json`.

1. Read `run.json` and `checklist.md`. If either is missing, stop and
   say to run `prep`.
2. Load [discover-the-idea](../discover-the-idea/SKILL.md) and interview
   the operator on their brain dump.
3. End with a brief; read it back in words, and wait for the operator to
   confirm in words. No confirmation, no write.
4. Write `RUN_ROOT/gatherer/run-1/brief.md` (atomic). Copy this
   session's file next to it, and list the copy in `machine.json`
   `gather.sessions` (run-root-relative). If no session file can be
   found, say so and list nothing.
5. `sdlc-driver persist RUN_ROOT`: not available yet. At `plain` there
   is nothing to persist; for `pushed` or `local`, say it is driven only.
6. Print the run root and the start line. OpenCode: `pick /sdlc, then
   enter RUN_ROOT`. Pi: `/sdlc RUN_ROOT`. Until the driver and plugin
   exist, add: the start line does not work yet; continue in followed
   mode (item 8).

## Mode: restore

For a machine without the run root. Needs the state branch on `origin`,
`pushed` or `local` runs only; a `plain` run has nothing to restore.

1. Ask only machine-local questions: harness executable and Node paths,
   run-root location, backup folder. Never ask the toolbox remote or
   trunk here; the first `/sdlc` asks them from the genesis note.
2. Run R5, R6, and R8 (R5 and R6 are driven only until item 5; R8 by
   hand as in prep). Write a new `machine.json` with a new `hostId`
   (32 random hex digits).
3. `sdlc-driver restore RUN_ROOT [--from <url or path>]`: not available
   yet (item 5). Name it, do not imitate it.
4. Print the start line as in Gather. The first `/sdlc` takes the typed
   genesis prefix, toolbox remote and trunk, re-clones the toolbox at the
   pin (R7), and shows the restore summary.

## Standing rules

- Public repo: no people's names, internal hostnames, IPs, or
  credentials in anything this skill writes.
- Never write a credential to `run.json`, `machine.json`, or
  `checklist.md`; refuse `apiKey` or header values from provider config.
- Report outcomes as they are: a check you skipped is `to do`.
