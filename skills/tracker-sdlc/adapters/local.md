# Adapter — local (git `tickets` branch)

Verified: no — vendor docs as of 2026-09-24

Not loaded at runtime. Facts and recipes for onboarding and repair; onboarding copies the recipes into `.agents/tracker/SKILL.md`.

## Hierarchy

- Branch `tickets` on the repo's own `origin`: orphan, never PR'd, no
  merges, no force-push. Anyone with push can write; no per-ticket permissions.
- One file per ticket, `tickets/<id>.md`; `type` is `track`, `epic`,
  `task`, or `bug`; `parent` holds the parent id. Sub-items stay off.
- Recipes stage only `tickets/` and `comments/`; readers ignore other paths.

## Blockers

- The blocked ticket lists blockers in `blocked_by`; set-blocker appends one (an
  existing ticket, not itself); agents never remove one. `blocks` is computed.
- Open blocker = its file is missing, or its `state` is not `done` / `canceled`.

## Text format

- YAML front matter between `---` lines, then a markdown body. Keys in this order:
  `id`, `type`, `title`, `state` (canonical), `parent`, `blocked_by`, `labels`,
  `assignee`, `created`, `updated` (ISO-8601 UTC, microseconds), `links`
  (reserved: recipes never write it; PR and SHA go in comment text).
- Lists: one `  - <item>` line each, or `[]`. Empty scalar: nothing after
  the colon. A malformed `blocked_by` line is rejected, not skipped.
- Comments: `comments/<id>/<TS>-<agent>.md` (`date -u +%Y%m%dT%H%M%SZ`);
  created once, never edited. The comment id is that file name.

## States and transitions

`state` holds the canonical state, set directly; nothing auto-transitions. Each
ticket edit rewrites `updated:` (microseconds), so concurrent edits conflict and re-decide.

## Safety rules

- **Patterns**, checked before a value reaches a path, refspec, or command; a mismatch
  stops and is reported. Prefix `^[a-z][a-z0-9]{0,5}$` (fixed at onboarding); id
  `^<prefix>-[a-z0-9]{4}$` for `id`, `parent`, each `blocked_by` entry, any requested id;
  agent `^[a-z0-9][a-z0-9-]{0,31}$` (own label, never ticket text); six canonical states.
- **Paths**: only `tickets/$ID.md`, `comments/$ID/$TS-$AGENT.md`. After every
  checkout (`worktree add`, `rebase`, `reset`) stop unless each `git ls-tree
  -r HEAD -- tickets comments` entry is mode `100644` and both are real
  directories: a planted symlink redirects writes. Temp files live outside `$W`.
- **Ticket text** goes into a draft file `D` (file-write tool); recipes copy it, never
  on a command line or `eval`. Commit messages: `[<id>] <verb>` in a `mktemp` file, `-F`.
- **Hooks off for every git command** (`GIT_CONFIG_COUNT` exports
  `core.hooksPath=/dev/null`; covers `reference-transaction` and husky-style
  relative paths): no secret scan runs, so ticket writes must never hold
  secrets. **Signing** follows git config; `SIGN=off` only if Gaps say so.
- **Retry** only when the ref moved, matched under `LC_ALL=C`: `[rejected]` (`fetch
  first`, `non-fast-forward`) or, pushes racing at the server, `[remote rejected]`
  (`incorrect old value provided`, `reference already exists`). Others stop, reported,
  URLs redacted. `fetch` retries 5 times (one clone's runs share a ref lock).

## Reads

`git fetch origin tickets`; `git show "origin/tickets:tickets/$ID.md"`. Use
only `git ls-tree origin/tickets tickets/` entries of mode `100644` named by
the id pattern; validate every id read from a file before use.

- **read**: front matter, body, and each `blocked_by` id with its file's
  `state` (`missing` if absent). URL: n/a; report `tickets/<id>.md`.
- **list-ready**: `state: ready`, `assignee` empty or `$AGENT`, every
  `blocked_by` file present in `done` / `canceled`. Scope epic: `parent` is
  the epic; track: walk `parent` (≤5 hops, stop on a repeat) to the track.

## Write recipe

One operation = one commit, in a temp worktree: the checkout you run from
is never touched or pushed. Set `PFX`, `AGENT`, `VERB`, `ID` (empty for
create), `D` (comment text, or a full create draft with every key line;
create overwrites `id`, `state`, `created`, `updated`), `TO`, `BY`,
`SIGN`, and `BOOT=approved` only if onboarding approved the bootstrap.
Define the verb's `change` from the first block (step 3: read `$W`, decide,
write; return 1 to stop), then run the write block; it prints `ok <id>`.

```sh
# change: create
change() { chk "$D"; while [[ -e $W/tickets/$ID.md ]]; do mint; done; local t; t=$(now) &&   # collision: new id
  put "$W/tickets/$ID.md" sed "1,/^---\$/{s/^id:.*/id: $ID/;s/^state:.*/state: backlog/;s/^created:.*/created: $t/
    s/^updated:.*/updated: $t/;}" "$D"; }
# change: claim
change() { local f=$W/tickets/$ID.md a; have "$f" && chk "$f" && ! open "$f" || return 1
  a=$(fm assignee "$f"); [[ -z $a || $a == "$AGENT" ]] ||
    { printf 'assigned to another agent: ask the orchestrator\n' >&2; return 1; }
  put "$f" sed "1,/^---\$/{s/^state:.*/state: in_progress/;s/^assignee:.*/assignee: $AGENT/
    s/^updated:.*/updated: $(now)/;}" "$f"; }
# change: transition
change() { local f=$W/tickets/$ID.md; have "$f" && chk "$f" &&
  put "$f" sed "1,/^---\$/{s/^state:.*/state: $TO/;s/^updated:.*/updated: $(now)/;}" "$f"; }
# change: set-blocker
change() { local f=$W/tickets/$ID.md; have "$f" && chk "$f" && have "$W/tickets/$BY.md" || return 1
  [[ $'\n'$(bl "$f")$'\n' != *$'\n'"$BY"$'\n'* ]] || return 0                    # already set
  put "$f" awk -v b="$BY" -v t="$(now)" 'NR>1&&/^---$/{e=1} !e&&/^blocked_by:/{print "blocked_by:"
    print "  - " b; next} !e&&/^updated:/{print "updated: " t; next} {print}' "$f"; }
# change: comment
# the ticket file is untouched: no `updated` rewrite, no `links` append
change() { local c; have "$W/tickets/$ID.md" && mkdir -p -- "$W/comments/$ID" || return 1
  c=$W/comments/$ID/$(date -u +%Y%m%dT%H%M%SZ)-$AGENT.md
  [[ ! -e $c ]] || { printf 'comment exists: retry\n' >&2; return 1; }
  put "$c" cat -- "$D" && printf 'comment %s\n' "${c##*/}"; }
```

```sh
# write
set -euo pipefail; IFS=$'\n\t'; ((BASH_VERSINFO[0] >= 5)) || { printf 'needs bash >= 5\n' >&2; exit 1; }
export LC_ALL=C GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.hooksPath GIT_CONFIG_VALUE_0=/dev/null
[[ ${SIGN:-} != off ]] || export GIT_CONFIG_COUNT=2 GIT_CONFIG_KEY_1=commit.gpgsign GIT_CONFIG_VALUE_1=false
RJ='^ ! \[rejected\] +[^ ]+ -> tickets \((fetch first|non-fast-forward)\)$'
RR='^ ! \[remote rejected\] +[^ ]+ -> tickets \((incorrect old value provided|reference already exists)\)$'
ok() { [[ $2 =~ $1 ]] || { printf 'rejected: bad %s\n' "$3" >&2; exit 2; }; }
fm() { awk -v k="$1:" 'NR==1{next} /^---$/{exit} index($0,k)==1{sub(/^[^:]*:[ ]*/,"");print;exit}' "$2"; }
bl() { awk 'NR==1{next} /^---$/{exit} /^[a-z_]+:/{k=$1;next} k=="blocked_by:"{print (/^  - /?substr($0,5):$0)}' "$1"; }
chk() { local k v; for k in id parent; do v=$(fm "$k" "$1"); [[ -z $v ]] || ok "$IDRE" "$v" "$k"; done
  v=$(fm blocked_by "$1"); [[ -z $v || $v == '[]' ]] || ok '^$' "$v" 'blocked_by (not a list)'
  while IFS= read -r v; do ok "$IDRE" "$v" blocked_by; done < <(bl "$1"); }
have() { [[ -f $1 ]] || { printf 'no such ticket\n' >&2; return 1; }; }
open() { local b; while IFS= read -r b; do [[ -f $W/tickets/$b.md && $(fm state "$W/tickets/$b.md") =~ \
  ^(done|canceled)$ ]] || { printf 'open blocker %s\n' "$b" >&2; return 0; }; done < <(bl "$1"); return 1; }
put() { local f=$1 n; shift; n=$(mktemp) || return 1; "$@" >"$n" && mv -- "$n" "$f" || { rm -f -- "$n"; return 1; }; }
now() { printf '%s.%sZ' "$(date -u +%Y-%m-%dT%H:%M:%S)" "${EPOCHREALTIME#*.}"; }       # bash >= 5
rnd() { head -c 512 /dev/urandom | tr -dc a-z0-9 | cut -c "1-$1"; }; mint() { ID=$PFX-$(rnd 4); ok "$IDRE" "$ID" id; }
root() { [[ $(git -C "$1" rev-parse --show-toplevel) == "$(cd -- "$1" && pwd -P)" ]] ||
  { printf 'not a worktree root\n' >&2; exit 2; }; }
safe() { local t b; t=$(git -C "$1" ls-tree -r HEAD -- tickets comments) || exit 2; b=$(grep -v '^100644 ' <<<"$t" || :)
  [[ -d $1/tickets && ! -L $1/tickets && -d $1/comments && ! -L $1/comments && -z $b ]] ||
    { printf 'refused: not a plain file or directory:\n%s\n' "$b" >&2; exit 2; }; }
red() { sed -E 's#(://)[^/ ]*@#\1REDACTED@#g' >&2; }
push() { local out; out=$(git -C "$1" push origin HEAD:refs/heads/tickets 2>&1) && return 0
  grep -qE "$RJ|$RR" <<<"$out" && return 1; red <<<"$out"; return 2; }
fetch() { local i; for i in 1 2 3 4 5; do git -C "$1" fetch -q origin tickets 2>/dev/null && return; sleep 1; done
  printf 'fetch failed\n' >&2; return 1; }
gone() { local n; n=$(git -C "$1" rev-list --count origin/tickets..HEAD 2>/dev/null) && [[ $n == 0 ]]; }
bye() { local d; [[ -z $M ]] || rm -f -- "${M:?}"; for d in "$B" "$W"; do [[ -z $d ]] ||
  { gone "$d" && git worktree remove "$d"; } || printf 'kept worktree %s\n' "$d" >&2; done; git worktree prune; }
W=; B=; M=; trap bye EXIT
ok '^[a-z][a-z0-9]{0,5}$' "$PFX" prefix; ok '^[a-z0-9][a-z0-9-]{0,31}$' "$AGENT" agent
ok '^(create|claim|transition|comment|set-blocker)$' "$VERB" verb; IDRE="^$PFX-[a-z0-9]{4}\$"
if [[ $VERB == create ]]; then mint; else ok "$IDRE" "$ID" id; fi
[[ $VERB != transition ]] || ok '^(backlog|ready|in_progress|in_review|done|canceled)$' "$TO" state
[[ $VERB != set-blocker ]] || { ok "$IDRE" "$BY" blocker; [[ $BY != "$ID" ]] || ok '^$' x self-block; }
M=$(mktemp) || exit 1
T=$(git ls-remote --heads origin refs/heads/tickets 2>"$M") || { red <"$M"; exit 1; }   # 0. bootstrap
if [[ -z $T ]]; then [[ ${BOOT:-} == approved ]] || { printf 'no tickets branch\n' >&2; exit 3; }
  B=$(mktemp -d) || exit 1; R=$(rnd 6); ok '^[a-z0-9]{6}$' "$R" suffix
  git worktree add -q --orphan -b "tickets-init-$R" "${B:?}"; root "$B"
  mkdir -- "$B/tickets" "$B/comments"; : >"$B/tickets/.keep"; : >"$B/comments/.keep"
  git -C "${B:?}" add tickets comments; printf 'Bootstrap tickets\n' >"$M"
  git -C "${B:?}" commit -q -F "$M"; r=0; push "$B" || r=$?; ((r != 2)) || exit 2   # 1: someone else won
  git worktree remove "${B:?}"; git branch -q -D "tickets-init-$R"; B=; fi
fetch .; W=$(mktemp -d) || exit 1                                                    # 1., 2.
git worktree add -q --detach "${W:?}" origin/tickets; root "$W"; safe "$W"; a=0
while :; do
  change || exit 3                                                                   # 3.
  git -C "${W:?}" add tickets comments                                               # 4.
  if git -C "$W" diff --cached --quiet; then printf 'ok %s\n' "$ID"; exit 0; fi
  printf '[%s] %s\n' "$ID" "$VERB" >"$M"; git -C "$W" commit -q -F "$M"
  while :; do a=$((a + 1)); r=0; push "$W" || r=$?                                   # 5.
    if ((r == 0)); then printf 'ok %s\n' "$ID"; exit 0; elif ((r == 2)); then exit 2; fi   # 9. via trap
    ((a < 10)) || { printf 'gave up: %s in %s\n' "$(git -C "$W" rev-parse HEAD)" "$W" >&2; exit 4; }
    fetch "$W"                                                                       # 6.
    git -C "${W:?}" rebase -q origin/tickets >/dev/null 2>&1 || break; safe "$W"
    sleep $((RANDOM % (2 * a) + 1)); done                                            # 8.
  git -C "${W:?}" rebase --abort; git -C "${W:?}" reset -q --hard origin/tickets; safe "$W"; done   # 7.
```

Exit: 0 done; 1 bash < 5, git, fetch, or `ls-remote` failure; 2 bad value, unsafe tree, or
other push rejection (bootstrap too); 3 chose not to write; 4 gave up (SHA and
worktree printed, kept). The trap removes a worktree only when `rev-list --count
origin/tickets..HEAD` succeeds and prints `0`. Never `-X ours`/`theirs`.

## Gotchas

- Needs git ≥ 2.42 (`worktree add --orphan`) and bash ≥ 5. Writes use detached temp
  worktrees: beads' long-lived sync worktree in `.git` bred most of its sync bugs.
- A symlink or non-`100644` entry under `tickets/` or `comments/` blocks every write;
  the refusal prints the `ls-tree` lines (git quotes odd paths). Agents stop and
  report; the operator removes the entry in a reviewed commit on `tickets`; agents
  never auto-delete.
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
- https://git-scm.com/docs/githooks#_reference_transaction
- https://github.com/steveyegge/beads
- https://github.com/gastownhall/beads/issues/1634
