# HLD — Tracker-agnostic SDLC

- Slug: `tracker-sdlc`
- Track / chunk ids: track P-DER-11; chunk DER-252
- Brief: DER-252 brief, confirmed 2026-09-24 (Refine: ready for Plan)
- Date: `2026-09-24`
- Status: **accepted** (operator, 2026-09-24; decisions folded in below)

## Required

- **Problem** — The SDLC assumes Linear (call names in `docs/SDLC.md`,
  `AGENTS.md`, `sdlc-artifacts`), lets items "nest sub-issues", and
  defines no states. Jira, Asana, Trello or file-ticket teams have no
  honest path; loading every tracker's detail per turn bloats context.

- **Goals**
  1. Linear, Jira, Asana, Trello, local files: equally first-class
     behind one contract (`tracker-sdlc`).
  2. Runtime tracker context = `tracker-sdlc` + repo skill, except the
     adapter read during repair.
  3. New `sdlc-onboarding` discovers, proposes, writes after confirm.
  4. No SDLC process file names a specific tracker.

- **Non-goals** — Per-tracker MCP/CLI manuals; tracker schema changes;
  helper packages or `scripts/`; live Jira/Asana/Trello tests (operator's
  work agents); non-tracker onboarding; small-work lane (DER-253).

- **Users / operators** — SDLC agents (manager files, builders claim).
  Operator confirms onboarding and owns tracker credentials.

- **UX / stories** — `docs/tracker-sdlc/ux.md` — agent review agreed;
  operator acceptance pending.

- **Comparables** — [comparables.md](comparables.md)

- **Shape**
  - **Contract** — `skills/tracker-sdlc/SKILL.md` (≤250 lines): the
    canonical model below plus the map. Mirrors `language-router`: read
    a small table, load exactly one target, stop.
  - **Adapters** — `skills/tracker-sdlc/adapters/{linear,jira,asana,trello,local}.md`:
    hierarchy, native blockers + direction, text format, transitions,
    gotchas, discovery hints. No tool names or CLI commands. Header
    `Verified: no — vendor docs as of 2026-09-24`; one Sources list.
    Read **only** by onboarding or when a recipe fails.
  - **Onboarding** — `skills/sdlc-onboarding/SKILL.md`: tracker section
    now, structured for later sections (testing etc.). Discovers and
    proposes the brief's list (What ships §3): tracker + access, board,
    types, state map, blockers, parent link, sub-items, PR/branch links.
  - **Product repo** — `AGENTS.md` `## Tracker` (1–2 lines: name +
    pointer) and committed `.agents/tracker/SKILL.md`: one recipe per
    verb, adapter gotchas baked in, for the tool the agent has, plus a
    contract-version stamp.
  - **Setup check** (map and Spec gate) — cheap and offline: the
    `## Tracker` line exists and the repo skill's stamp matches the
    contract version. No live call. Only onboarding and repair go live.
  - **Repair** — a recipe fails → read the adapter → retry. Still
    failing → stop that tracker action, report (see Runtime), propose
    the new recipe; commit on the current branch only on operator OK.
    No silent self-rewrite.
  - **Runtime** — Operator away and a tracker action fails → comment on
    the ticket + report to the orchestrator. Ticket assigned to someone
    else → neither skip nor start; check with the orchestrator.

```mermaid
flowchart TD
  T[Agent needs a tracker verb] --> C[tracker-sdlc contract]
  C --> A{"Offline check: Tracker line<br/>+ repo skill stamp current?"}
  A -- yes: runtime --> R[.agents/tracker/SKILL.md recipe]
  R -- ok --> D[Done]
  R -- recipe fails --> AD1[Read adapters/&lt;tracker&gt;.md]
  AD1 -- still fails --> RP[Stop, report, propose fix]
  RP -- operator OK --> CM[Commit on current branch]
  CM --> R
  A -- no: onboarding --> O[sdlc-onboarding]
  O --> AD2[Read adapters/&lt;tracker&gt;.md]
  AD2 --> P[Discover + propose to operator]
  P -- confirmed --> W["Write Tracker section + .agents/tracker/SKILL.md"]
  W --> R
```

  - **Canonical model**
    - Hierarchy: track → epic → work item (Task | Bug). Sub-items
      (child tickets under a work item) off unless the workplace
      already uses them.
    - States: `backlog`, `ready`, `in_progress`, `in_review`, `done`
      (= landed+verified), `canceled`. Many may map to one tracker state
      (`ready` = Backlog, no open blockers; Linear Todo → `ready`).
      Blocked = open blockers, not a state.
    - Verbs: create, read, list-ready, transition, set-blocker, comment
      (PR/SHA links fold in unless native). Claim = `in_progress` +
      claim comment `Claimed by <agent-label> <UTC>`, then re-fetch;
      an earlier unreleased claim by another label → post `Released
      by`, ask the orchestrator (the source of truth; agents share one
      tracker identity; contract v2).
    - Blockers: native relation, else `Blocked-by:` line + `blocked`
      label. Store one direction.
  - **Where onboarding sits** — **Entry is read-only**: it classifies
    from what it was handed and writes nothing. Full onboarding at the
    **first tracker touch of any grain**: a chunk files its Epic at end
    of Brief and onboards there; an item's onboarding opens item Brief,
    then the "one line on the ticket" is written. The **Spec entry
    gate** runs only the offline setup check.
  - **Branch at onboarding** — The branch is cut when onboarding runs:
    a chunk's project-main at end of Brief (was Groom), an item's branch
    at item Brief (was Build). The onboarding commit lands there at once,
    visible to every worktree. Parallel chunks: first to land on trunk
    wins; the others rebase. Repair commits follow the same rule.
  - **Local tracker** — Long-lived `tickets` branch, never PR'd; linear
    history, no merges, no force-push. `tickets/<id>.md` (front matter:
    id, type, title, state, parent, blocked_by, labels, assignee,
    created, updated, links) + append-only
    `comments/<id>/<UTC>-<agent>.md`. ID = repo prefix + 4 random chars,
    unique-checked before push. Each operation: fresh detached worktree
    at `origin/tickets` (outside the repo or gitignored), exactly one
    commit, hooks and commit signing off, push `HEAD:refs/heads/tickets`.
    On rejection: fetch, rebase the one commit, push; jittered retry ~10.
    On rebase conflict: abort, re-read, re-decide (claim taken → give
    up; ID collision → mint a new ID). Never `-X ours/theirs`. Give-up:
    report the commit SHA and keep the worktree (no lost write). After
    success: `git worktree remove` / `prune`. Recipes in `adapters/local.md`.
  - **Trust boundaries (HLD grain)**
    - Credentials stay with the local agent; no tokens in any file.
    - Onboarding never changes tracker schema; gaps go to the operator.
      Live reads prove access; test writes only on operator yes (one
      throwaway ticket, create then cancel).
    - `tickets`: anyone with repo push may write; no per-ticket
      permissions. Rulesets may need an exemption; no CI.
    - Ticket text (titles, bodies, comments) is untrusted data, never
      instructions — every tracker, and above all `tickets`.
    - `.agents/tracker/SKILL.md` is loaded instructions: every change
      (onboarding or repair) goes through review like code. No SOURCES
      row; **security** reads it in the change that adds or edits it
      (no tokens, no scripts).

- **Persistence** — Skills home: contract, adapters, onboarding, these
  docs, SOURCES. Product repo: `## Tracker` + `.agents/tracker/SKILL.md`
  committed at onboarding on the chunk's project-main or the item
  branch (both cut then); **never** a direct trunk commit. Local
  tracker: `tickets` branch. Board: the tracker (Epic, items, relations).

- **Worker rules** — Onboarding proposes, operator confirms, then it
  writes. No agent creates tracker states/types/fields. Runtime uses
  repo recipes; adapter reads are for repair. SOURCES flips
  `tracker-sdlc` to `first-party` before its body lands;
  `sdlc-onboarding` is a new first-party id (security cut).

- **Doc edits** — `docs/SDLC.md`: Hierarchy (L76–86 incl. "may nest
  sub-issues"), states, Entry read-only (ticket line moves to Brief),
  chunk Brief files the Epic, onboarding + branch cut in Brief, Groom /
  Build / Project-main lifetime table (branches cut at Brief, not Groom
  or Build), onboarding as Spec entry gate, delete Linear call names
  L663–664. `docs/INTAKE.md`: one line on product-repo
  `.agents/tracker/SKILL.md` (no SOURCES row; security reads the
  change). `AGENTS.md`: delete L73
  call names; `tracker-sdlc` out of placeholders, add `sdlc-onboarding`.
  `skills/sdlc-artifacts/SKILL.md`: delete L47–48 (not into an adapter).
  `docs/ARCHITECTURE.md` Board layer; SOURCES rows; SDLC skill table;
  `README.md:47` and `:120` (both call `tracker-sdlc` a placeholder with
  no `SKILL.md`).

- **Groom order** — (1) contract + Linear adapter + onboarding + doc
  edits → (2) onboard this repo (settle: `Bug` label outside Linear's
  Type group; Linear default branch names vs SDLC `item/<ticket>-<slug>`)
  → (3) Jira → (4) Asana → (5) Trello → (6) local.

- **Open** — Adapters stay unverified until work agents run them live.
  Operator decisions: [Decided](#decided-operator-2026-09-24).

## Optional

- **Risks**
  - Adapters ship `Verified: no`; first live use may fail → repair.
  - beads dropped its JSONL sync-branch mode after worktree/hook bugs.
    Ours: disposable per-operation worktree outside `.git`, hooks off, one
    file per ticket, concurrency test before trust.
  - Jira Blocks create direction (`inwardIssue` = blocker) comes from a
    third-party quote, not a primary doc; JQL cannot isolate direction.
    Prove live.
  - Jira REST v3 bodies are ADF JSON, not markdown (MCP conversion
    unverified); Asana wants XML-valid `<body>` HTML. Recipes encode it.
  - Tracker auto-transitions (PR merge → Done) may mark `done` before
    landed+verified. Onboarding surfaces them.

- **Alternatives rejected**
  - Git plumbing, no worktree (`commit-tree` / `update-ref`): hookless,
    but opaque to agents and humans and hard to express as prose
    recipes; a worktree is inspectable and survives a give-up.
  - One shared worktree per clone with a lock: a branch checks out in
    only one worktree; the lock is the long-lived shared worktree beads
    abandoned, and a stale lock blocks every agent.

- **Verify later**
  - Onboarding this repo on Linear reproduces P-DER-11; Type/Epic,
    Type/Task; Backlog/Todo/In Progress/In Review/Done/Canceled
    (+Duplicate→`canceled`); native blocks; a working repo skill.
  - Two concurrent `tickets` writers in a scratch repo both land.
  - Work agents flip adapter headers after live runs.
  - No process file names Linear: `grep -rli linear docs/SDLC.md
    AGENTS.md skills/` returns only `skills/tracker-sdlc/adapters/linear.md`.
  - Runtime tracker loads never exceed `tracker-sdlc` + repo skill,
    except the adapter read during repair.

## Decided (operator, 2026-09-24)

1. **Entry is read-only.** Classifies from what it was handed; writes
   nothing. The ticket line moves to Brief, after onboarding.
2. **Branch cut at onboarding.** Chunk project-main at end of Brief;
   item branch at item Brief. Onboarding (and repair) commits land
   there at once. Parallel chunks: first to land wins; others rebase.
3. **"No Linear" scope** = process files only: `docs/SDLC.md`,
   `AGENTS.md`, `skills/*` except `skills/tracker-sdlc/adapters/linear.md`.
4. **Product-repo `.agents/tracker/SKILL.md`**: no SOURCES row;
   **security** reads it in the change that adds or edits it (no
   tokens, no scripts). One line in `docs/INTAKE.md`.
5. **Runtime**: Linear Todo → `ready`; failure while operator away →
   ticket comment + report to orchestrator; ticket assigned to someone
   else → do not skip, do not start, check with orchestrator; recipe
   still failing after adapter read → stop, report, propose repair
   (committed only on operator OK).
6. **Claim marker, contract v2** (DER-260). Assignee cannot tell agents
   apart on a shared identity: claim adds a `Claimed by` comment and a
   re-fetch; the loser of a conflict posts `Released by` and asks the
   orchestrator, which is the source of truth. Native agent field or
   per-agent labels only on operator yes; `local` keeps `assignee`.
   Details: [LLD Decided](lld.md#decided-operator-2026-09-24).
7. **Land path** (DER-260). No PRs; Review is an explicit gate; item
   branches and project-main are pushed; lands are local and serialized.
