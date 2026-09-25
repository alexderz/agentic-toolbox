# Adapter — local (git `tickets` branch)

Verified: no — vendor docs as of 2026-09-24

Facts and recipes for `sdlc-onboarding` and for repair. Not loaded at
runtime: onboarding copies the recipes into `.agents/tracker/SKILL.md`.

## Hierarchy

- Branch `tickets` on the repo's own `origin`: orphan, never PR'd, no
  merges, no force-push. Anyone with push can write; no per-ticket permissions.
- One file per ticket, `tickets/<id>.md`; `type` is `track`, `epic`,
  `task`, or `bug`; `parent` holds the parent id. Sub-items stay off.
- Recipes stage only `tickets/` and `comments/`; readers ignore other paths.

## Blockers

- The blocked ticket lists blockers in `blocked_by`; set-blocker appends
  one, agents never remove one. `blocks` is never stored: compute it.
- Open blocker = its file is missing, or its `state` is not `done` / `canceled`.

## Text format

- YAML front matter between `---` lines, then a markdown body. Keys in
  this order: `id`, `type`, `title`, `state` (canonical), `parent`,
  `blocked_by`, `labels`, `assignee`, `created`, `updated` (ISO-8601
  UTC), `links` (`pr: <n>` / `sha: <sha>` items).
- Lists: one `  - <item>` line each, or `[]`. Empty scalar: nothing after the colon.
- Comments: `comments/<id>/<TS>-<agent>.md`, `<TS>` from
  `date -u +%Y%m%dT%H%M%SZ`; created once, never edited.

## States and transitions

`state` holds the canonical state, set directly; nothing auto-transitions. Every
write rewrites `updated:`, so concurrent edits of one ticket conflict and re-decide.

## Safety rules

- **Patterns**, checked before a value reaches a path, refspec, or command;
  a mismatch stops and is reported. Prefix `^[a-z][a-z0-9]{0,5}$` (fixed at
  onboarding); id `^<prefix>-[a-z0-9]{4}$` for `id`, `parent`, each `blocked_by`
  entry, and any requested id; agent `^[a-z0-9][a-z0-9-]{0,31}$` (own label,
  never ticket text). Paths: only `tickets/$ID.md`, `comments/$ID/$TS-$AGENT.md`.
- **Ticket text** goes into a draft file `D` written with the file-write
  tool; recipes copy it, never put it on a command line, never `eval` it.
  Commit messages are `[<id>] <verb>` in a `mktemp` file, passed with `-F`.
- **Hooks off** (`H`) on every `worktree add`, `commit`, `rebase`, and
  `push`: no pre-push secret scan runs, so ticket writes must never hold
  secrets. **Signing** follows the operator's git config; only if Gaps
  say "signing off", set `S=(-c commit.gpgsign=false)`.
- **Retry** only when the ref moved: `[rejected]` (`fetch first`,
  `non-fast-forward`) or, for two pushes racing at the server, `[remote
  rejected]` (`MOVED`). Any other rejection stops, reported, URLs redacted.

## Reads

No worktree: `git fetch origin tickets`; `git show "origin/tickets:tickets/$ID.md"`
(validated `ID`); list-ready walks `git ls-tree --name-only origin/tickets tickets/`,
skipping names that fail the id pattern.

## Write recipe

One operation = one commit, in a temp worktree: the checkout you run
from is never touched or pushed. Set `PFX`, `AGENT`, `VERB`, `ID` (empty
for create), `D`, and `BOOT=approved` only if onboarding approved the
bootstrap. Define `change` (step 3: read `$W`, decide, write; return 1 to
stop), then run the write block. transition, comment, and set-blocker
follow the claim shape.

```sh
# change: create
change() { chk "$D"; while [[ -e $W/tickets/$ID.md ]]; do mint; done   # collision: new id
  mkdir -p -- "$W/tickets"; sed "1,/^---\$/s/^id:.*/id: $ID/" "$D" >"$W/tickets/$ID.md"; }
```

```sh
# change: claim
change() { local f=$W/tickets/$ID.md b; [[ -f $f ]] || { printf 'no ticket\n' >&2; return 1; }
  chk "$f"; [[ -z $(fm assignee "$f") ]] || { printf 'assigned: ask the orchestrator\n' >&2; return 1; }
  while IFS= read -r b; do [[ -f $W/tickets/$b.md && $(fm state "$W/tickets/$b.md") =~ ^(done|canceled)$ ]] ||
    { printf 'open blocker %s\n' "$b" >&2; return 1; }; done < <(bl "$f")
  sed "1,/^---\$/{s/^state:.*/state: in_progress/;s/^assignee:.*/assignee: $AGENT/;s/^updated:.*/updated: $(
    date -u +%Y-%m-%dT%H:%M:%SZ)/;}" "$f" >"$f.new"; mv -- "$f.new" "$f"; }
```

```sh
# write
set -euo pipefail; IFS=$'\n\t'; export LC_ALL=C
H=(-c core.hooksPath=/dev/null); S=(); W=; B=; M=$(mktemp) || exit 1
MOVED='incorrect old value provided|reference already exists'    # ref moved mid-push
ok() { [[ $2 =~ $1 ]] || { printf 'rejected: bad %s\n' "$3" >&2; exit 2; }; }
ok '^[a-z][a-z0-9]{0,5}$' "$PFX" prefix; ok '^[a-z0-9][a-z0-9-]{0,31}$' "$AGENT" agent
ok '^(create|claim|transition|comment|set-blocker)$' "$VERB" verb; IDRE="^$PFX-[a-z0-9]{4}\$"
fm() { awk -v k="$1:" 'NR==1{next} /^---$/{exit} $1==k{sub(/^[^:]*:[ ]*/,"");print;exit}' "$2"; }
bl() { awk 'NR==1{next} /^---$/{exit} /^[a-z_]+:/{k=$1} k=="blocked_by:"&&/^  - /{print substr($0,5)}' "$1"; }
chk() { local k v; for k in id parent; do v=$(fm "$k" "$1"); [[ -z $v ]] || ok "$IDRE" "$v" "$k"; done
  v=$(fm blocked_by "$1"); [[ -z $v || $v == '[]' ]] || ok "$IDRE" "$v" blocked_by
  while IFS= read -r v; do ok "$IDRE" "$v" blocked_by; done < <(bl "$1"); }
rnd() { head -c 512 /dev/urandom | tr -dc a-z0-9 | cut -c "1-$1"; }; mint() { ID=$PFX-$(rnd 4); ok "$IDRE" "$ID" id; }
root() { [[ $(git -C "$1" rev-parse --show-toplevel) == "$(cd -- "$1" && pwd -P)" ]] ||
  { printf 'not a worktree root\n' >&2; exit 2; }; }
push() { local out; out=$(git -C "$1" "${H[@]}" push origin HEAD:refs/heads/tickets 2>&1) && return 0
  grep -qE "^ ! \[(remote )?rejected\] .*\((fetch first|non-fast-forward|$MOVED)\)" <<<"$out" && return 1
  printf '%s\n' "$out" | sed -E 's#(://)[^/ ]*@#\1REDACTED@#g' >&2; return 2; }
fetch() { local i; for i in 1 2 3 4 5; do git -C "$1" fetch -q origin tickets 2>/dev/null && return; sleep 1; done
  printf 'fetch failed\n' >&2; return 1; }        # retries: sibling runs share the tracking-ref lock
gone() { local n; n=$(git -C "$1" rev-list --count origin/tickets..HEAD 2>/dev/null) && [[ $n == 0 ]]; }
bye() { local d; rm -f -- "$M"; for d in "$B" "$W"; do [[ -z $d ]] || { gone "$d" && git worktree remove "$d"; } ||
  printf 'kept worktree %s\n' "$d" >&2; done; git worktree prune; }; trap bye EXIT
if [[ $VERB == create ]]; then mint; else ok "$IDRE" "$ID" id; fi
T=$(git ls-remote --heads origin refs/heads/tickets)                                 # 0. bootstrap
if [[ -z $T ]]; then [[ ${BOOT:-} == approved ]] || { printf 'no tickets branch\n' >&2; exit 3; }
  B=$(mktemp -d) || exit 1; R=$(rnd 6); ok '^[a-z0-9]{6}$' "$R" suffix
  git "${H[@]}" worktree add -q --orphan -b "tickets-init-$R" "${B:?}"; root "$B"
  mkdir -- "$B/tickets" "$B/comments"; : >"$B/tickets/.keep"; : >"$B/comments/.keep"
  git -C "${B:?}" add tickets comments; printf 'Bootstrap tickets\n' >"$M"
  git -C "${B:?}" "${H[@]}" "${S[@]}" commit -q -F "$M"
  push "$B" || [[ $? == 1 ]]                                         # 1: someone else won
  git worktree remove "${B:?}"; git branch -q -D "tickets-init-$R"; B=; fi
fetch .; W=$(mktemp -d) || exit 1                                                    # 1., 2.
git "${H[@]}" worktree add -q --detach "${W:?}" origin/tickets; root "$W"; a=0
while :; do
  change || exit 3                                                                   # 3.
  git -C "${W:?}" add tickets comments                                               # 4.
  if git -C "$W" diff --cached --quiet; then exit 0; fi
  printf '[%s] %s\n' "$ID" "$VERB" >"$M"; git -C "$W" "${H[@]}" "${S[@]}" commit -q -F "$M"
  while :; do a=$((a + 1)); r=0; push "$W" || r=$?                                   # 5.
    if ((r == 0)); then exit 0; elif ((r == 2)); then exit 2; fi                     # 9. via trap
    ((a < 10)) || { printf 'gave up: %s in %s\n' "$(git -C "$W" rev-parse HEAD)" "$W" >&2; exit 4; }
    fetch "$W"                                                                       # 6.
    git -C "${W:?}" "${H[@]}" "${S[@]}" rebase -q origin/tickets >/dev/null 2>&1 || break
    sleep $((RANDOM % (2 * a) + 1)); done                                            # 8.
  git -C "${W:?}" rebase --abort; git -C "${W:?}" reset -q --hard origin/tickets; done   # 7.
```

Exit: 0 done; 2 bad value or other rejection; 3 chose not to write; 4 gave
up (SHA and worktree printed, kept). The trap removes a worktree only when
`rev-list --count origin/tickets..HEAD` succeeds and prints `0`. Never `-X ours`/`theirs`.

## Gotchas

- Needs git ≥ 2.42 (`worktree add --orphan`). Writes use detached temp worktrees:
  beads' long-lived sync worktree in `.git` bred most of its sync bugs.
- Rulesets that block direct pushes or require signed commits reject
  writes: onboarding reports them as gaps. Keep CI off `tickets`.
- Claims are push-wins; contention grows with agents. History grows
  without bound; squashing would need a force-push (Never).

## Discovery hints

- `git ls-remote --heads origin refs/heads/tickets` is non-empty.
- The operator says "no hosted tracker", or no other adapter's hints match.

## Sources

- https://git-scm.com/docs/git-worktree
- https://git-scm.com/docs/git-push
- https://git-scm.com/docs/git-config#Documentation/git-config.txt-receivedenyNonFastForwards
- https://github.com/steveyegge/beads
- https://github.com/gastownhall/beads/issues/1634
