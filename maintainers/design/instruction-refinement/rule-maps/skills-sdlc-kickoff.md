# DER-421 G0: `sdlc-kickoff` rule map

Old: `skills/sdlc-kickoff/SKILL.md` absent at main 7a11696.
New: `skills/sdlc-kickoff/SKILL.md`. New file: empty old side. Every
rule below is **kept** in this path. No route, no drop.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| — | Three modes (`prep`, `gather`, `restore`). None starts the driver or a worker | kept | Opening |
| — | Question ids in operator prompts are stable and never reused. `prep-1` is only the paid-slot spending ask | kept | Opening |
| — | Iron law: setup questions only; no write, cut, or push before the checklist reply; no proposed toolbox remote; quoted argv, no `eval`, no operator text in a command string; an unrun check is `to do` or `unknown` | kept | Iron law |
| — | `sdlc-driver` subcommands are not available until item 5. Until then, and for every followed run, the level is `plain`. Skip `state-init`, drill, and the genesis note. Do not imitate them | kept | Driver commands |
| — | R1-R4 are walkable from this skill. R5-R7 and R9 are `to do`. R8's parent-folder word comes from the hand check. `0700` is after the reply. R10 is `n/a` at `plain` | kept | Driver commands |
| — | Ask `prep-mode` before `prep-level`. Ids: `prep-remote`, `prep-trunk`, `prep-pin`, `prep-repo`, `prep-slug`, `prep-tracker`, `prep-harness`, `prep-root`, `prep-mode`, `prep-level`, `prep-backup` | kept | Mode: prep |
| — | Refuse a toolbox URL that breaks the remote rule before any fetch. Trunk passes `git check-ref-format --branch` and does not start with `-` | kept | `prep-remote`, `prep-trunk` |
| — | After those checks, the pin is a quoted `git ls-remote` argv (tags, then trunk tip), not a clone into the product repo. Show the 40-hex commit | kept | `prep-pin` |
| — | Slug matches `^[a-z0-9]+(-[a-z0-9]+)*$`. `project_main` is `integrate/$slug` only after that match and `git check-ref-format --branch` | kept | `prep-slug` |
| — | Tracker is required and `local` only for a driven run. A public repo has no default and is warned before any ticket write | kept | `prep-tracker` |
| — | Followed, and any prep before item 5, sets `plain` without asking. A driven run after item 5 offers three levels with no default on a public repo, else default `pushed` | kept | `prep-level` |
| — | Readiness preview writes nothing. R1-R4 use quoted argv arrays. No unquoted refspec. No `--force` | kept | Readiness preview, R1-R4 checks |
| — | R8: parent exists, is not a symbolic link, and is not inside a worktree. That word can be `done`. Creating mode `0700` is after the reply | kept | R8 hand check |
| — | After the reply: approved R2 push, file the Epic, write the run files with a temporary file, `fsync`, and `rename`. While `plain`, skip `state-init`, drill, and the genesis note | kept | After the operator replies |
| — | Gather starts only in a new session, and only after `run.json` exists. Until item 5, a level other than `plain` stops | kept | Mode: gather |
| — | Gather confirms the brief in words before writing it. Item 8 is not landed. Stop after the brief and the start-line note. Do not name a skill that is not in the tree | kept | Mode: gather |
| — | Restore asks only `restore-bin`, `restore-root`, and `restore-backup`. It does not imitate `sdlc-driver restore`. A `plain` run has nothing to restore | kept | Mode: restore |
| — | No names, internal hostnames, IPs, or credentials in files this skill writes. No `apiKey` or header values | kept | Standing rules |

## Meaning questions

None. No open MQ.
