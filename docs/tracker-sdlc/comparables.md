# Comparables — tracker-agnostic SDLC

How others gave agents a tracker-neutral or git-resident ticket system.
**Before** locking the HLD shape. Sources: Brief research, 2026-09-24.

- Slug: `tracker-sdlc`
- Brief / options map: confirmed DER-252 brief (track P-DER-11) and its
  research notes (local trackers; Jira/Linear; Asana/Trello)
- Date: `2026-09-24`

## Required

### beads (`bd`)

- **Who / what** — [steveyegge/beads](https://github.com/steveyegge/beads).
  The best-known agent-first tracker.
- **What they did** — Hash IDs (`bd-a1b2`), a `ready` query, and an
  atomic claim (`--claim` sets assignee + in-progress). It used to keep
  JSONL on a `beads-sync` branch checked out in a worktree under
  `.git/beads-worktrees/`. That mode was **removed in v0.53.0** in favor
  of a Dolt database synced to `refs/dolt/data`
  ([migration](https://github.com/gastownhall/beads/issues/2442)). The
  bug stream behind it: local JSONL drifted from the branch
  ([#1379](https://github.com/steveyegge/beads/issues/1379)); a
  post-checkout hook broke bare-repo + worktree pushes
  ([#1634](https://github.com/gastownhall/beads/issues/1634)); untracked
  JSONL risked landing on main
  ([#797](https://github.com/steveyegge/beads/issues/797)).
- **Adopt** — Random IDs, never a counter. `list-ready` and claim =
  in-progress + assignee as first-class verbs. Hooks off for ticket
  commits (the #1634 workaround).
- **Won't copy** — A long-lived worktree hidden inside `.git`; one
  monolithic JSONL file; a database dependency. We keep the branch
  design but make the worktree per agent, disposable, and outside
  `.git`, and we treat beads' retreat as the main risk to test.

### ticket (`tk`)

- **Who / what** — [wedow/ticket](https://github.com/wedow/ticket).
  Written as a beads replacement with no DB or daemon.
- **What they did** — One markdown + YAML front-matter file per ticket
  in `.tickets/`; short random IDs (`nw-5c46`); `dep`, `ready`,
  `blocked` commands; plain git for concurrency.
- **Adopt** — One file per ticket; front matter for fields, body for
  prose; short prefixed random IDs. Our choice on top: store blockers
  in one direction only (`blocked_by`).
- **Won't copy** — Tickets on the code branches (they then ride PRs and
  merge with code). Ours live on a separate `tickets` branch, never
  PR'd.

### Backlog.md

- **Who / what** — [MrLesk/Backlog.md](https://github.com/MrLesk/Backlog.md).
- **What they did** — Markdown + YAML tasks in `backlog/` on code
  branches, `dependencies:` field, agent instructions and MCP. State is
  read across branches active in the last 30 days
  ([ADVANCED-CONFIG](https://github.com/MrLesk/Backlog.md/blob/main/ADVANCED-CONFIG.md));
  which copy wins is not documented.
- **Adopt** — A front-matter shape agents and humans both read;
  shipping agent-facing instructions with the tracker.
- **Won't copy** — Sequential IDs (`TASK-12`, collide across agents);
  reading ticket state from many branches (no single source of truth).
  Ours has exactly one branch as truth.

### git-bug (bridges)

- **Who / what** — [git-bug/git-bug](https://github.com/git-bug/git-bug);
  [data model](https://github.com/git-bug/git-bug/blob/master/doc/design/data-model.md).
- **What they did** — Issues as commit chains under custom refs, edits
  as append-only operation packs ordered by Lamport clock. Bridges sync
  to GitHub, GitLab, Jira and Launchpad: one local model, adapters per
  remote tracker.
- **Adopt** — One canonical model with per-tracker adapters, not a
  per-tracker process. Append-only records for concurrent writers (our
  `comments/<id>/<UTC>-<agent>.md`).
- **Won't copy** — Custom refs (default fetch covers only `refs/heads/*`,
  [refspec](https://git-scm.com/book/en/v2/Git-Internals-The-Refspec));
  bridge code. Our adapters are prose facts onboarding turns into
  recipes for the tool the agent already has — no package, no scripts.
