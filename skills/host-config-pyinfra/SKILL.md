---
name: host-config-pyinfra
description: use this when an agent running on a Linux host must capture, codify, or change that host's configuration in a shared pyinfra and just repository - one agent per host, local apply only, zero drift first, sops secrets. Do not use for cloud resources, network appliances, or any host other than your own.
---

# Host config with pyinfra

Each host has **one owning agent that runs on that host**. The agent
changes its host only by editing its own folder in a shared repository
and applying it locally. Configuration as code is the agent's toolbox,
so every change can be reproduced. Change the host by hand only in an
emergency, and codify that change in the same session.

Site facts (host names, addresses, buckets, which repo) live in the
repository's own `AGENTS.md`, `NOTICES.md` and `hosts/<host>/NOTES.md`.
This skill holds the method. Where they disagree, the repository wins.

## Iron law

**Reproduce first, then improve.** A host's first deliverable is code
that matches the live host exactly, proven by `just check <host>`
reporting zero changes. Cleanups come after, one change at a time.

## The repository contract

```
justfile              verbs; refuses any host that is not `hostname -s`
scripts/              helpers the verbs use (dry-run parser)
.sops.yaml            one creation_rules entry per host
keys/                 operator's public age key
NOTICES.md            cross-host notices, newest first
hosts/<host>/
  deploy.py           includes the parts below
  base.py             what any of the operator's boxes gets
  <role>.py           what this host is for (nas.py, ai.py, daemons.py, ...)
  <host>_secrets.py   host-local helper for sops secrets (never `secrets.py`,
                      which shadows the standard library module)
  files/              files the deploy puts in place
  secrets.sops.json   encrypted secrets
  age-host.pub        this host's public age key
  status              read-only live health script
  NOTES.md            decisions, facts that look wrong but are not, rebuild runbook
  TODO.md             work not yet done
  repos.txt           cloned repos (owner/name), never their contents
```

| Verb | Does | Changes the host |
| --- | --- | --- |
| `just diff <host>` | Pending changes, with file diffs | No |
| `just check <host>` | Exit 1 on any unconditional change | No |
| `just apply <host>` | Make the host match the repo | Yes |
| `just status <host>` | Live health (`hosts/<host>/status`) | No |

Rules that bind every host agent:

1. **Write only in your own `hosts/<host>/`.** Root files are shared.
   Changes to them must be backwards compatible; otherwise add a
   `NOTICES.md` entry and tell the other hosts' agents.
2. **No shared code yet.** Copy from another host's folder; do not
   import from it. A later pass across all hosts extracts what is
   common. Do not design abstractions before every host is captured.
3. **Never configure another host.** Ask its agent. Moving *data* to
   another host over SSH (backups, model files) is fine; installing or
   reconfiguring it is not.
4. **Commit and push every applied change** to `main`
   (`git pull --rebase` first). No PRs.
5. **No third-party services.** Services of the site's cloud provider
   are acceptable when the operator agrees. Alerting to a human waits for the
   operator's chosen channel; record it as a TODO, do not invent one.

## Procedure

### 1. Read before writing

Read the repository's `AGENTS.md`, `NOTICES.md`, and the most complete
existing `hosts/<host>/` folder. That folder is the reference
implementation: copy its patterns (secret handling, reload gating,
status script) rather than re-deriving them.

### 2. Capture the live host (read-only)

Look up facts; do not ask the operator for anything the host can tell
you. Record findings in `NOTES.md`. Checklist:

- OS, edition, kernel, package manager (`dnf` or `rpm-ostree`).
- Packages the operator added: `dnf history list` and
  `dnf history info <id>`; on rpm-ostree, `rpm-ostree status` (layered
  packages) and `flatpak list`.
- Users, groups, uid, sudo (`/etc/sudoers` and `/etc/sudoers.d/`),
  linger (`/var/lib/systemd/linger/`).
- SSH: `authorized_keys`, `sshd -T`, `/etc/ssh/sshd_config.d/`.
- Firewall zones and rich rules; listening ports (`ss -tlnp`).
- Storage: `/etc/fstab`, mounts, pools, exports.
- Enabled system units and timers; user units in
  `~/.config/systemd/user/`; crontabs.
- Dotfiles. The reference host manages them as whole files; if other
  tools own marked blocks inside them, note the exact markers.
- User toolchains in `~/.local/bin`, `~/.cargo`, `~/.nvm`, pipx, `uv tool`.
- Cloned repos under `~/src`.
- Secret file locations (never their contents).
- History: other agents' notes and session logs about this host.

### 3. Scaffold and reproduce

Create `hosts/<host>/` from the reference folder. Codify what you
captured, section by section, running `just diff <host>` after each.
Hand edits are codified as they are, even when ugly; cleanups go in
`TODO.md`.

Done when `just check <host>` prints `in sync`, and a real
`just apply <host>` reports zero changes.

### 4. Secrets

- sops, pinned by version and sha256 in `base.py`; reinstall when the
  hash differs. `/usr/local` is writable on rpm-ostree hosts too.
- Post-quantum age keys (`age-keygen -pq`, ML-KEM-768 + X25519; needs
  age 1.3 or later, and a sops release built against it). On rpm-ostree,
  install age the same way as sops (pinned binary) rather than layering.
  Recipients: the operator's key in `keys/` and this host's own key,
  kept root-only (600) at the path the repository names, for example
  `/etc/<repo>/age/host.key`. Do **not** use the SSH host key as a recipient:
  it is classical crypto and undoes the post-quantum choice.
- Publish the host's public key as `hosts/<host>/age-host.pub` and add
  a `creation_rules` entry to `.sops.yaml`.
- Encrypt live secrets from memory; never write plaintext to disk or
  print it. Creation rules match on the file name, so encrypting from
  stdin needs `--filename-override hosts/<host>/secrets.sops.json`. To add
  one secret: `sudo cat FILE | sops set --value-stdin
  hosts/<host>/secrets.sops.json '["key"]'`.
- Deploy: decrypt at deploy time, compare **sha256 only** with the live
  file, and when they differ run a shell command that decrypts straight
  into place (`sops decrypt --extract '["key"]'`). Secret contents must
  never reach `files.put`, a diff, a log, or your own context.
- Verify: both keys decrypt; each value matches the live file by hash;
  a deleted secret file is restored identically; a scan of `-vvv`
  output and the staged diff finds no secret tokens.
- If the host key is missing (fresh host), warn and skip dependent
  services. Never create an empty secret file.
- The operator's private age key never stays on a host. If you generate
  it, leave it in a clearly named file for the operator to move off the
  host, and track that in `TODO.md`.

### 5. Verify, then hand over

- `just check <host>` is zero; a real apply changes nothing.
- Simulate drift (edit an installed file), confirm `check` fails and
  `apply` restores it.
- Run a **clean verifier agent** (not you) over the folder: lockout
  safety, data safety, fresh-host behaviour, secret leakage, docs vs
  code. Fix what it finds.
- Commit, push, and summarize for the operator what changed on the live
  host. Expect almost nothing during the baseline.

## Safety

Never lock the operator out, never damage data.

- **sshd:** put the drop-in, then
  `sshd -t || { rm -f <drop-in>; exit 1; }` before `systemctl reload sshd`.
- **Firewall:** put the zone file, then
  `firewall-cmd --check-config || { rm -f <zone>; exit 1; }` before
  reload. Any firewall change needs the operator's yes in that session.
- **sudo:** passwordless sudo for the operator comes from a drop-in.
  Stage it outside `/etc/sudoers.d/`, `visudo -cf` it, then
  `install -m 440` it into place. A broken sudoers file blocks the sudo
  needed to fix it. Until the first apply, sudo asks for a password, and
  deploy-time decryption (`sudo -n`) fails, so run that apply
  interactively.
- **SSH port** stays 22.
- Keep every key in `authorized_keys` unless the operator says
  otherwise. A key that looks stale may belong to another OS on a
  dual-boot machine.
- A normal apply never restarts networking.
- Storage is **checked, never created**: no `mkfs`, partitioning,
  subvolume or dataset deletion, or `chown -R` over data. Codify mounts
  and exports; put pool health in `status`.
- Disable a service rather than delete its unit when the operator says
  "stop it for now".

## pyinfra gotchas

- **Zero drift needs idempotent operations.** No unguarded
  `server.shell`. Gate reloads and restarts with
  `_if=any_changed(op, ...)` from `pyinfra.operations.util`.
  `systemd.service(daemon_reload=True)` reports a change on every run:
  use a separate `systemd.daemon_reload(_if=...)`.
- **Deploy-time conditionals** (`if not host.get_fact(File, ...)`) add
  an operation only when needed, so they report nothing when satisfied.
  Check `Link` as well as `File` for tools installed as symlinks.
- **Facts on root-only files need `_sudo=True`** on `get_fact`.
- **Package names are rpm names**, not provides (`nodejs22`, not
  `nodejs`). `dnf.packages` also reports a change forever when the
  installed build has left the repositories: upgrade that package.
- **`files.line` patterns are grep basic regex.** `\s` is whitespace,
  but `\s+` means "whitespace then a literal +". Use `[[:space:]]` or `extended_regex=True`. A
  pattern that never matches looks like "no change" in a dry run.
- **`files.file` creates missing files.** Never use it as a presence
  check for secrets.
- **Run pyinfra as the operator's user** with `_sudo=True` only on
  system operations, so files under the home stay user-owned.
- **Self-updating tools** (agent CLIs, nvm, rustup): manage presence
  only (install if missing), never the version.
- **Helpers across files:** `local.include()` for the parts;
  `sys.path.insert(0, HERE)` in `deploy.py` so parts can import a
  host-local helper module named `<host>_secrets.py` or similar.
- **Operation names** read `"<part>: <what>"` (`"base: authorized_keys"`),
  so `just check` output says where drift is.
- **User units** need linger to run without a login; scheduled jobs do
  not read `.bashrc`, so pass things like `--profile` explicitly.
- `just check` parses the `--> Detected changes` table and counts only
  the unconditional column; conditional changes cannot fire without an
  unconditional one.

## Host kinds

- **Fedora (dnf):** the reference implementation applies as is.
- **rpm-ostree (Fedora Atomic, Bazzite, and similar):** pyinfra has no
  rpm-ostree operation. Prefer, in order: flatpak (`flatpak`
  operations); user-level installs (`pipx`, `uv tool`, `npm --prefix`,
  and Homebrew where the image ships it, via `brew` operations); a
  toolbox or distrobox container; then layered packages via a guarded
  `server.shell` (`rpm-ostree install --idempotent`, guard on
  `rpm-ostree status --json`). Layering needs a reboot: never reboot in
  an apply, record it for the operator.
  - `/usr` is read-only; `/etc`, `/var` and `/usr/local` are writable.
    Home is `/var/home/<user>` behind the `/home` symlink.
  - Groups such as `wheel`, `docker` or `libvirt` may exist only in
    `/usr/lib/group`. Copy the entry into `/etc/group` before
    `server.user(groups=...)`, or the operation fails.
  - Record in `NOTES.md` how `just` and `uv` were bootstrapped.
- **Dual-boot hosts:** the other OS is out of scope. Its SSH keys stay
  authorized.

## Cross-host conventions

The repository's `AGENTS.md` is authoritative for these; the defaults
below apply when it is silent.

- **DNS:** each host publishes its own records with its own cloud
  identity. Taking over from another publisher is ordered: dry-run
  publish, the old publisher drops the host, then write.
- **Backups (if the site has a NAS host):** writers put `<host>/<service>/<YYYY>/<MM>/<entry>` on the
  NAS with a **relative** `LATEST` link and publish their own
  success/failure metrics. The NAS host copies onward to object storage
  add-only, and checks freshness, size, readability and the remote copy.
- **Other hosts' agents** are reached through whatever messaging the
  operator provides. Confirm facts they report before acting on them.
- **Operator user IDs match across hosts**; NFS `sec=sys` relies on it.
- **Cloned repos** (`repos.txt`): clone if missing, never touch
  contents, and skip with a warning until `gh auth login` is done.
- **Drift** is the operator's responsibility. Do not add a scheduled
  drift check unless asked.

## Always

- Look up facts on the host before asking the operator.
- Record "looks wrong but is not" facts in `NOTES.md` so the next agent
  does not "fix" them. Date each decision and say who made it.
- Keep `TODO.md` current: baseline, secrets, then cleanups.

## Ask first

- Firewall changes, SSH authentication changes, removing any
  authorized key.
- Anything that restarts networking, reboots, or touches storage
  layout.
- Changing a shared root file in a way that is not backwards
  compatible.

## Never

- Apply to a host other than the one you run on.
- Put plaintext secrets in git, a diff, a log, or your context.
- Create, format, or delete storage.
- Add a third-party service.
