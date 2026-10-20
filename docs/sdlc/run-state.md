# Run state

Owner of the run-root formats that Run prep, the harness plugins, and
workers use. Rules only; examples live in
`maintainers/design/solo-dlc/lld.md` (Behavior 4). Procedure:
[sdlc-kickoff](../../skills/sdlc-kickoff/SKILL.md). Files are UTF-8.

## Run root

- The run root is outside every git worktree, not a symbolic link, mode
  `0700`; tools refuse group or other permission. Default:
  `$XDG_STATE_HOME/sdlc/<chunk-slug>/`.
- Every file is written atomically: temporary file in the same folder,
  `fsync`, `rename`.
- **D** marks the durable part, mirrored to the state branch at `pushed`
  and `local`. Unmarked entries are local and never committed.

```text
RUN_ROOT/
  run.json                 # D  Run prep; operator confirms at first /sdlc
  machine.json             #    Run prep; 0600; never mirrored
  driver.json              # D  driver only
  index.jsonl              # D  driver only; one event per line
  checklist.md             # D  Run prep
  plan/items.json          # D  driver, after ticket filing
  asks/ask-N.json, .md     # D  driver: ask and answer
  gatherer/run-1/          #    brief.md (D); Gather session copy (local)
  refiner/run-1/           #    created empty by Run prep
  <persona>/run-N/         #    run folder; D files listed below
  compiled/ toolbox.git/ repo.git/ worktrees/ env-data/ driver/   # local
```

## `run.json`

- `schemaVersion` is `1`. Keys: `chunk`, `bundle`, `repo`, `tracker`,
  `mode`, `state`, `harness`, `models`, `spending`, `labels`, `limits`,
  `env`, `createdAt`. No absolute path, host name, address, or
  credential; refuse to write a [scan pattern](#scan-patterns) hit.
- `bundle.remote` and `bundle.trunk` are what the operator typed; both
  are fixed for the run. `bundle.commit` is the pin; `bundle.tag` the
  chosen tag or `null`.
- `tracker.backend` is `local` for driven runs. Any other value is
  refused: `tracker backend <name> is not supported for driven runs yet;
  use local`.
- `state.level` is `pushed`, `local`, or `plain`; `state.branch` is
  `sdlc/run/<chunk-slug>`, absent at `plain`. `mode` is `enforced` or
  `followed`; `followed` allows only `plain`.
- A `paid: true` slot needs `spending` (`askId`, `approvedAt`, the
  operator's words). `harness.providers` holds no `options`, `apiKey`, or
  header value.
- The plugin summarizes both JSON files at the first `/sdlc` and on any
  change; the operator's yes is a hash in `driver.json`. No yes, no run.

## `machine.json`

- Mode `0600`, never mirrored. Keys: `schemaVersion`, `hostId`, `harness`
  (`bin`, `node`, `providerOptions`), `backup.dir`, `gather.sessions`,
  `createdAt`.
- `hostId` is 32 random hex digits, new per run root and machine; it
  names the lease holder without a host name.
- `backup.dir` is `null` or an absolute `0700` folder outside every
  worktree, not a symbolic link. `gather.sessions` lists run-root-relative
  Gather copies; a restored run has none.

## Driver files and `asks/`

- `driver.json` is the driver's alone: confirmed file hashes,
  `bundleRemote`, toolbox hashes, pin history, `compiled` hashes, item and
  session state, `unmirrored` folders. `index.jsonl` is history only;
  `plan/items.json` supplies no command.
- `ask-N.json` (tools) and `ask-N.md` (people) hold the same ask and
  answer, verbatim: `{"choice", "text", "at"}`, recorded only by the
  plugin's `/sdlc` handler while no driver holds the lock.

## Run folder

`<persona>/run-N/`; a finished run has `result.json` per
[stage-result.md](stage-result.md). **D** files: `result.json`,
`result.md`, `state.md`, `ledger.json`, `baseline.json`, `ask-human.md`,
`out/`, `commands.json`, `env-evidence.json`, `check.json`, gate
extracts, `interrupted.json`. Local: the rest (`meta.json`, `prompt.md`,
`candidate.json`, `logs/`).

- Worker-written files (`result.md`, `state.md`, `ledger.json`,
  `baseline.json`, `ask-human.md`, `out/`) mirror only once `result.json`
  exists and the folder is not in `unmirrored`.
- An interrupted folder is kept with `interrupted.json`, never gets a
  `result.json`, and is never reused. `result.md` uses no absolute path.

## Labels

- A label matches `^[a-z0-9][a-z0-9-]{0,31}$`. An item persona's label
  and folder are `<persona-id>-<suffix>`, suffix at most 23 characters,
  fixed once the persona exists.
- `labels.mode` `plain`: the lowercased ticket id, matching
  `^[a-z0-9][a-z0-9-]{0,22}$`. `short`: that id with characters outside
  `[a-z0-9-]` replaced by `-`, cut to 12, then `-` and 8 hex digits of
  its SHA-256. Run prep sets `short` when the key pattern allows ids over
  23 characters or outside `[A-Za-z0-9-]`; `local` ids fit `plain`.

## Durability levels

| Level | **D** files live | Survives | Drill source |
| --- | --- | --- | --- |
| `pushed` | State branch, pushed to `origin` at every persist | Loss of the machine | `origin` |
| `local` | State branch in `repo.git`, never pushed | A damaged run-root file | `repo.git` |
| `plain` | Run root only | Crashes on this machine | none (`n/a`) |

- A followed run is `plain` only, including on a public repo. A driven
  run on a public repo says first that the state branch is public
  (brief, prose, `state.md`, answers) and offers all three, no default.

## State branch

- `sdlc/run/<chunk-slug>`: orphan, never merged, never named by the land
  path, never deleted by the driver. At `@done` it is the operator's.
- Its tree is the **D** files plus `sdlc-state.json`: `schemaVersion`,
  `seq`, `prev`, `level`, `event`, `run`, `pin`, `lease` (`pushed` only),
  `files` (SHA-256 ledger), `excluded`, `skipped`. The tip record
  `driver/state.json` (`seq`, `tip`, `genesis`, `pushedTip`, `restore`)
  is local.
- `state-init` refuses a second run root for a slug whose state branch
  exists; it, `persist`, and `restore` refuse while `SDLC_RUN_DIR` is
  set or a driver holds the lock.

## Persist

- Persist runs at `state-init`, the end of Gather, each stage start and
  end, each driver push to project-main outside a stage, and each Start.
  It copies each **D** file whose hash differs, never deletes one, and
  sends a file over 256 KiB or not NUL-free UTF-8 to `skipped`.
- It scans every copied file ([scan patterns](#scan-patterns)); a hit
  commits nothing until that section's answer. Else it commits as
  `sdlc-driver <sdlc-driver@sdlc.invalid>` (`[<epic>] state <seq>:
  <event> <run>`) and pushes without force at `pushed`.

## Lease

- `lease.holder` is `hostId`. Every Start fetches the branch: tip equal
  to `pushedTip` with this holder goes on; a local tip ahead is pushed
  first; anything else is `state lease lost`; a failed fetch is `state
  lease unknown`: ask `state-push`, never skip the check. Only a restore
  moves it.

## Restore

- `sdlc-driver restore RUN_ROOT [--from <url or path>]` (default
  `origin`) creates the run root `0700`, rebuilds `repo.git`, fetches the
  branch, walks `prev` to the first commit, and refuses a commit whose
  `sdlc-state.json` fails the reader, whose ledger differs from its tree,
  or whose `seq` does not fall by one.
- It lists commits by another identity, checks each commit named in
  `driver.json` is an ancestor of fetched project-main, and writes the tip
  record with `restore.confirmed` false.
- The first `/sdlc` asks, from the genesis note, the first 12 hex digits
  of the genesis commit, the full toolbox remote, and the trunk. They
  must equal the restored `bundleRemote` and `bundle.trunk`.
- It then re-clones the toolbox at the pin and shows the restore summary.
  The operator types the first 12 hex digits of the state tip; a pin
  other than the genesis one needs its full SHA typed back.
- Local files (Gather copies, logs, `excluded`, `skipped`) are absent
  after a restore.

## Drill

- At `pushed` and `local`, `sdlc-driver drill RUN_ROOT` restores the
  branch from its drill source into a temporary `0700` folder with no
  lease and no push, and a `machine.json` copy with a new `hostId` and
  no backup folder. It writes nothing outside that folder.
- It rebuilds the toolbox with the remote typed at Run prep, fails when
  `config` or `HEAD` hashes differ from the source, and compares status,
  every ledger file, and every compiled hash. Status ignores the lease,
  the tip record's `restore` and `pushedTip`, the run-root path,
  `bundle.trunkTip`, `checkedAt`, `excluded`, and `skipped`.
- Pass prints `restore drill: done`; else it names the difference and Run
  prep prints no Gather line. The folder is removed either way.

## Toolbox copy

- `toolbox.git` is a bare copy of `bundle.remote` holding only its trunk
  and tags. The driver reads bundle, persona, skill, and script files and
  `docs/INTAKE.md` from its object store at the pin, never a working
  tree; none is copied into the product repo.
- **Remote rule.** An `https://host/path` or SSH URL (`ssh://host/path`
  or `[user@]host:path`), host not starting with `-`, no whitespace or
  control character. Refused: a `<transport>::` prefix, `file://`, a
  local path, a password or token in user info, a query string.
- The operator types the remote in full, no default or prefill, before
  any clone or fetch; no model proposes it.
- The trunk is `main` unless the operator names another at Run prep; it
  passes `git check-ref-format --branch` and does not start with `-`. The
  reviewed ref is `refs/heads/<trunk>`; the remote `HEAD` is never read.
- Git in the copy runs with hooks, fsmonitor, commit graphs, `ext::`, and
  `file://` off, on git 2.32 or newer, with `GIT_CONFIG_NOSYSTEM=1`,
  `GIT_NO_REPLACE_OBJECTS=1`, `GIT_CONFIG_GLOBAL` set to `driver/gitconfig`
  (only `credential.*` and `core.sshCommand`), `GIT_ALLOW_PROTOCOL=https:ssh`,
  and no other operator `GIT_*` variable. Only `init`, `config`, fetch,
  `rev-parse`, `merge-base --is-ancestor`, `ls-tree`, and `cat-file`;
  never `show`.
- The toolbox check, at every Start, requires: recorded `config` and
  `HEAD` hashes; `remote.origin.url` equal to `bundleRemote`;
  `bundle.commit` an ancestor of the fetched trunk (or a typed pin) and
  equal to the state pin; each file read at the pin hashing to its blob
  id; the bundle check passing on those bytes.
- `toolbox --rebuild` removes a damaged copy without running git in it.
- **Genesis note.** At `pushed` and `local`, Run prep prints once, in
  the `state-init` turn, `keep off this machine: genesis <40-hex>  toolbox <remote>  trunk <trunk>; a restore asks for all three`.

## Compiled files

- `compiled/<persona>.md`: local, a pure function of the pin and the
  `run.json` repo facts; regenerated at `state-init`, item planning, a
  repin, and the env land.
- First line `<!-- sdlc-compiled pin=<40-hex> sources=<sha256> -->`, then
  Role, Repo facts, each `Packed skill <id> — do not reload`; no absolute
  path.
- `driver.json` `compiled` holds each file's SHA-256. A missing file, or
  a `pin` or `sources` that differs from the toolbox copy now, is
  recompiled and the new bytes must equal that hash; any other
  difference, or a file with no entry, is `check failed: compiled`.
- Only a mint's `prompt.md` names the file, in its first line; changes
  reach a resumed session as a `# Compiled update` block.

## Rehydrate and session backup

- A resume with a missing session file restores the backup when its
  SHA-256 matches and the file passes the session check; else it mints a
  session from the compiled file, the latest mirrored `state.md`, the
  last three run folders, and the facts.
- `rehydratePending` holds until the next valid result; a failed or
  again-missing file meanwhile is `session lost: <file>`: operator decides.
- With `backup.dir` set, each stage end writes the persona's compressed
  session file to `<backup.dir>/<chunk-slug>/<persona>.gz` and records its
  SHA-256. A failure never stops the run.

## Scan patterns

Per line, over every file a persist copies, each committed design record,
and each added or modified ticket or comment file. A hit names file,
line, and class, never the text. A `credential` hit offers `revise` or
`defer` (`state-secret`: `exclude` or `defer`), never `allow`, and never
`exclude` for `run.json`, `driver.json`, or `plan/items.json`.

| Class | Matches | Operator may allow |
| --- | --- | --- |
| `credential` | private-key headers; `lin_api_`, `ghp_`, `github_pat_`, `AKIA`, `xox[abprs]-`, `sk-` with a long body; URLs with a password; each accepted `passEnv` value of 6+ characters | No |
| `ip` | IPv4 except documentation ranges and `127.0.0.1` | Yes |
| `path` | `/home/`, `/Users/`, `/root/`, `/var/lib/`, `C:\Users\`, the run root | Yes |
| `host` | `.lan`, `.local`, `.internal`, `.ts.net`, `.home.arpa` | Yes |
| `userinfo` | URLs with a user name and no password | Yes |
