# DER-421 G0: `run-state.md` rule map

Old: `docs/sdlc/run-state.md` absent at main 7a11696.
New: `docs/sdlc/run-state.md`. New file: empty old side. Every rule
below is **kept** in this path. No route, no drop.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| — | This file owns run-root formats. Rules only. Examples stay in the LLD. Procedure is `sdlc-kickoff` | kept | Opening |
| — | Run root is outside every worktree, not a link, mode `0700`. Default `$XDG_STATE_HOME/sdlc/<chunk-slug>/` | kept | Run root |
| — | Every file is written with a temporary file in the same folder, `fsync`, then `rename` | kept | Run root |
| — | **D** files mirror at `pushed` and `local`. Unmarked files are local | kept | Run root |
| — | `run.json` keys, fixed remote and trunk, pin, `local` tracker backend for driven runs, levels, and `mode` `enforced` or `followed` (`followed` allows only `plain`) | kept | `run.json` |
| — | A paid slot needs `spending`. Provider config holds no `apiKey` or header value. No run without the operator's yes | kept | `run.json` |
| — | `machine.json` is mode `0600`, never mirrored. `hostId` is 32 random hex digits. Backup folder rules | kept | `machine.json` |
| — | `driver.json` is the driver's alone. `index.jsonl` is history. `plan/items.json` supplies no command. Asks record the answer only while no driver holds the lock | kept | Driver files and `asks/` |
| — | Run-folder **D** set, mirror condition, interrupted folder never reused | kept | Run folder |
| — | Label pattern and `plain` / `short` | kept | Labels |
| — | Durability table. A followed run is `plain` only, including on a public repo. A driven public repo offers all three levels with no default | kept | Durability levels |
| — | State branch shape, `sdlc-state.json`, local tip record. `state-init`, `persist`, and `restore` refuse while `SDLC_RUN_DIR` is set or a driver holds the lock | kept | State branch |
| — | Persist copies changed **D** files, never deletes, skips oversized or non-UTF-8 files. A scan hit commits nothing until the scan answer | kept | Persist |
| — | Lease: tip equal to `pushedTip` with this holder continues; a local tip ahead is pushed first; anything else is `state lease lost`; a failed fetch is `state lease unknown` and asks `state-push`. Only a restore moves the lease | kept | Lease |
| — | Restore checks, genesis confirmation, local files absent after restore | kept | Restore |
| — | Drill compare ignores the lease, the tip record's `restore` and `pushedTip`, the run-root path, `bundle.trunkTip`, `checkedAt`, `excluded`, and `skipped` | kept | Drill |
| — | Toolbox remote rule, typed remote, trunk check, and git limits: `GIT_CONFIG_NOSYSTEM=1`, `GIT_NO_REPLACE_OBJECTS=1`, `GIT_CONFIG_GLOBAL` limited to `driver/gitconfig` (`credential.*` and `core.sshCommand` only), `GIT_ALLOW_PROTOCOL=https:ssh`, no other operator `GIT_*`. Allowed commands exclude `show` | kept | Toolbox copy |
| — | Compiled file: recompile when missing or when `pin` or `sources` differ from the toolbox copy now. New bytes must equal the `driver.json` hash. Any other difference, or a file with no entry, is `check failed: compiled` | kept | Compiled files |
| — | Rehydrate and session backup | kept | Rehydrate and session backup |
| — | Scan patterns apply to persist copies, committed design records, and added or modified ticket and comment files. A credential hit is revise-only (`state-secret`: `exclude` or `defer`), never `allow`, and never `exclude` on `run.json`, `driver.json`, or `plan/items.json` | kept | Scan patterns |

## Meaning questions

None. No open MQ.
