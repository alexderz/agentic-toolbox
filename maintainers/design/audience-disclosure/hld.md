# HLD — Audience and disclosure for public repos

- Slug: `audience-disclosure`
- Track / chunk ids: skills-home process track; chunk DER-286
- Brief: confirmed by the operator 2026-09-27. Record:
  [gather.md](gather.md) (Brief, final), simplified by
  [refine.md](refine.md) S1–S6 and P1–P3. The six decisions after
  Refine are D2 (with D1 and D11), D3 (with D10), D4 (with D5), D6, D7
  and D8. D9 was cut.
- Date: `2026-09-27`

## Required

- **Problem** — The ban on internal hostnames and IPs covers only
  deliverables (root `AGENTS.md` `## Public repo`). Agent notes, commit
  text, tickets, PoC code and onboarding's tracker host names sit in
  the same public git, under "civil and credential-free" or no rule at
  all. Every **security** read runs after the push (Spec, Review), but
  item branches, Plan and Trial drafts and `tickets` are pushed before
  it. A pushed leak cannot be recalled: forks, `refs/pull/`, caches and
  clones keep it ([comparables](comparables.md) §1). This repo shows
  the pattern: landed item branches are still on `origin` (gather E9).
  No repo records whether its remote is public.

- **Goals**
  1. Each repo records one fact, `Public remote: yes|no`, in
     `## Audience`. `sdlc-onboarding` fills it from the host and
     re-checks it at each chunk Brief (D2).
  2. When it is `yes`, the ban covers everything sent to the public
     host, not only deliverables (D3).
  3. Private context has a private home: a private tracker, plus an
     optional companion repo that `AGENTS.md` only mentions (D4).
  4. The pushing agent reads what it is about to push, before every
     push to a public remote, with two fixed outcomes (D6, D7).
  5. The local tracker runs on a public repo only after an explicit
     yes (D8).
  6. A `no` → `yes` flip warns the operator that the whole history is
     now public (D2).
  7. Each rule has one owner file ([Rule owners](#rule-owners)).

- **Non-goals** (brief, Out of scope) — Tone and style levels
  (DER-269). Workplace rules (DER-287). A private working remote,
  mirror or fork (DER-266). A separate private remote for `tickets`
  (later ticket). A concrete deny-list of names or IPs. gitleaks or any
  other mechanical hook (separate **tester** ticket). Auditing
  already-published history and stale pushed branches (DER-350).
  Encrypted files as a default (D10: on request only). `Public remote:
  no` changes nothing from today.

- **Users / operators** — Every agent that pushes: **builder** (item
  branches, project-main after a land), **architect** (Plan and Trial
  drafts), **manager** (`tickets` writes, PR text). Agents running
  `sdlc-onboarding`. The operator, who answers onboarding, gets the
  flip warning, and decides on already-public leaks. Product repos that
  use this toolbox, and this repo itself.

- **UX / stories** — `n/a`: no screen. The operator-facing messages
  (onboarding proposal, flip warning, already-public stop) use
  template `ask-human.md`. The **manager** asks for `UX verification
  not required` with the HLD acceptance.

- **Comparables** — [comparables.md](comparables.md): GitHub
  repository networks, pre-push secret scanners, GitLab's public and
  internal handbooks, agent instruction files.

### Shape

**1. `## Audience` in the governing `AGENTS.md` (D2).** This is a new
`sdlc-onboarding` area with Check, Discover, Propose and Write, plus
one row in its When table. Its lines:

```
## Audience

Public remote: yes
Companion repo: yes — location in the tracker
```

- `Public remote` is `yes` when any remote the SDLC pushes to is
  publicly readable. Discover reads the host's visibility for each
  push URL, for example `gh repo view --json visibility`. If no host
  read works, it asks the operator. The LLD picks the host reads and
  whether an anonymous `git ls-remote` probe is a fallback.
- `Companion repo` is `yes` or `no`. The line never holds a location
  (D4).
- When: at the first tracker touch, with Tracker and Execution, in the
  onboarding commit. At every chunk Brief the area re-checks: it reads
  the host again and compares the answer with the file (Q1: item Brief
  too).
- A re-check that flips `no` → `yes` sends the flip warning before any
  push. The warning says that all history, branches, tags and
  `tickets` are now public, and that cleanup is an audit ticket
  (DER-350 here). There is no automatic rewrite. It may point at a
  history scan (comparables §2).
- In this repo the governing file is `maintainers/AGENTS.md`, so
  `## Audience` goes there.

**2. The ban (D3).** It covers everything sent to a public host, not
only deliverables:

- In scope: file content and paths, commit and tag messages, branch
  and tag names, PR titles, bodies and comments, `tickets` and
  `comments/` files, PoC code, and the host names onboarding writes.
- Banned: internal hostnames and IPs; private workspace URLs and names;
  people's names beyond credits and git authorship; credentials; the
  companion's location.
- Public hosts stay allowed, for example `mcp.linear.app` or an
  upstream URL. A self-hosted tracker on an internal host is recorded
  by env var name, never by host name (refine P1).
- Tone does not change. Deliverables stay professional. Agent context
  may stay informal, but it follows the same ban.
- Encryption (sops, git-crypt) happens only on the user's request. The
  agent then explains the limits: file names and commit messages stay
  readable, and access cannot be revoked (D10).

**3. Private context (D4).** Private context goes to the tracker when
the tracker is private (hosted). The optional private companion repo
holds notes that do not fit in tickets. It is not a mirror or fork and
never syncs code. Its location lives in the tracker. When the tracker
is itself public (local, D8), see Q2.

**4. Pre-push read (D6, D7).** Before every push to a public remote,
the agent that pushes reads the outgoing range: file diffs, commit and
tag messages, ref names. Before posting to a public host, it reads the
PR text too. This covers every push path: item branches, project-main
after a land, Plan and Trial drafts (DER-278), the onboarding commit,
tags, and `tickets` writes. The read has two outcomes:

| Hit | Outcome |
| --- | --- |
| Only in commits not yet on any public ref | 1. Remove the text. If it is needed, move it to the private tracker or the companion. If neither exists, drop it or ask (refine P3). 2. Rewrite the unpushed commits; no force-push is involved. 3. Read again, then push. |
| Already on a public ref: in an earlier push, another branch, or a `-` line of this diff | 1. Stop. Push nothing that repeats it. 2. Ask the operator (`ask-human.md`). No automatic history rewrite, no force-push. 3. A credential is rotated first, per security-hardening. 4. The **manager** links or files the audit ticket. |

This read is a floor, not a control. Prompts are not a boundary, and
the mechanical hook is the **tester** ticket.

**5. Local tracker on a public repo (D8).** Onboarding's `tickets`
bootstrap line (Propose step 6) adds a clause: "The remote is public:
every ticket and comment is published forever, and private context
goes only to the companion." Only an explicit yes sets
`BOOT=approved`. Every later ticket write is a push, so the
**manager** reads the draft `D` against the ban before it runs the
recipe. The adapter's shell recipe does not change (writing standard
K5).

### Trust boundaries (HLD grain)

- **Local clone → public host.** This is the new boundary. Anything
  that crosses it is permanent. It is guarded by the pre-push read
  (floor) and later by the **tester** hook (control).
- **Private tracker / companion ↔ public git.** Private context may
  point into public git. Public git never points at the companion's
  location.
- **Visibility read.** Egress goes only to the repo's own host. Host
  names only; the no-token and no-config-value rules stay as in
  onboarding's Never.

### Rule owners

| File | Owns after the change | Routes to |
| --- | --- | --- |
| Root `AGENTS.md` `## Public repo` | This repo is public. The voice split: deliverables are professional, agent context may be informal. One line: everything pushed follows the ban. | `security-hardening` for the ban |
| `skills/security-hardening/SKILL.md` | The ban: its scope (everything sent to a public host), its categories, where private context goes, that the companion location is never pushed, encryption on request with its limits, rotation of a leaked credential. The read is a floor and the hook is **tester**'s. | `branches-and-lands` for when the read runs |
| `skills/sdlc-onboarding/SKILL.md` `## Audience` | The `## Audience` lines; Check, Discover, Propose, Write; the When row and the chunk Brief re-check; the flip warning; the public clause on the `tickets` bootstrap line. The Never row narrows host names to public ones. | `security-hardening` for the categories |
| `docs/sdlc/branches-and-lands.md`, new `## Before a push` | The pre-push read: who, when (every push path to a public remote), what is read, the two outcomes. The Land path Durability row links here. | `security-hardening` for the categories |
| `skills/tracker-sdlc/adapters/local.md` | A public-remote note: every write publishes; allowed only with onboarding's yes; the manager reads `D` before the recipe; no private context in tickets. Recipe unchanged. | `branches-and-lands`, `security-hardening` |
| Route-only edits | `maintainers/AGENTS.md` (this repo's `## Audience`; the Where-notes-go bullet); `docs/sdlc/entry-brief-repo.md` (end of chunk Brief step 2, item Brief step 0.2); template `agents-stub.md` (one Audience line); `docs/sdlc/conventions.md` (the `.agents/` ban line); `docs/sdlc/plan-trial-spec.md` (DER-278 steps, Q3); `maintainers/writing-standard.md` (Rule-owners rows; K10 stays this repo's helper grep for the read). | the owners above |

**Overlap with DER-278** (`item/der-278-poc-code`, not landed). DER-278
adds Plan step 4: "Before each commit, **architect** scans every staged
file … for credentials, hostnames or IPs, personal data, local paths,
`.env` files, logs, and data dumps." Steps 5–6 commit and push. The
Trial adds: "If a pushed Plan or Trial file holds a secret,
**security** removes it and has it rotated." That is a second category
list and a second leak outcome, so two owners. The one-owner proposal
(Q3):

- `security-hardening` holds both lists. List A, never committed in
  any repo: credentials, `.env` files, logs, data dumps. List B, never
  sent to a public host: DER-278's hostnames or IPs, personal data and
  local paths, plus this chunk's categories.
- `branches-and-lands` `## Before a push` holds when and what. Every
  push reads list A; a push to a public remote also reads list B.
- DER-278's steps 4–6 become one route to `## Before a push`. Its
  Trial secret line becomes outcome 2: stop, ask, rotate, with no
  silent rewrite.

- **Persistence**
  - Git: `## Audience` in the governing `AGENTS.md`, the skill and SDLC
    text above, and this folder.
  - Tracker (private): private context and the companion's location.
  - Companion repo (private, optional): notes that do not fit in
    tickets.
  - Nothing new in the tracker schema, and no new files in product
    repos beyond two lines in `AGENTS.md`.

- **Worker rules**
  - The agent that pushes runs the read. No worker, remote or local,
    pushes to a public remote without it.
  - Outcome 2 is the operator's call. No agent rewrites public history
    or force-pushes on its own.
  - Only the **manager** writes the tracker. **security** reads the
    `## Audience` Write like any onboarding change.
  - Build follows the writing standard. Each edited agent file gets a
    rule map. Line caps: root `AGENTS.md` ≤100 (76 now),
    `branches-and-lands.md` ≤120 (70), `conventions.md` ≤100,
    `SKILL.md` ≤250 (`sdlc-onboarding` is at 201, so the new area gets
    about 45 lines).
  - Before merging into `main`: the eval run T1–T3
    (`maintainers/AGENTS.md` `## Evals`), plus a seeded diff with a
    fake internal hostname that must stop before the push (brief,
    Verify later).

- **Open**
  - Q1–Q4 below.
  - LLD: the host reads per remote type and the anonymous probe; the
    exact rewrite commands for unpushed commits (interactive git is
    unavailable to agents); where in the tracker the companion's
    location lives, per adapter.

## Operator questions

❓ **Q1** — **Re-check at item Brief too?** The brief re-checks
`## Audience` at each chunk Brief. A repo that only gets items would
never re-check, so a flip goes unwarned.
1. Chunk Brief only. 2. Chunk Brief and item Brief (one host read).
➡️ 2: it costs one read and closes the item-only gap.

❓ **Q2** — **Where does the companion's location live when the tracker
is public** (local tracker, D8)? There, the tracker would publish it.
1. The clone's local git config (`git config --local`). It is never
pushed; the operator gives it once per clone. 2. Always ask the
operator in the session. 3. Forbid a companion with a public tracker.
➡️ 1: it is private and survives sessions. `## Audience` then says
"location: local git config".

❓ **Q3** — **One owner for the DER-278 scan?**
1. As in [Overlap with DER-278](#rule-owners): lists in
`security-hardening`, when and outcomes in `branches-and-lands`,
DER-278's steps become a route. DER-278 lands first as it is, and
DER-286 Build does the move. 2. The same split, but DER-278 is changed
before it lands.
➡️ 1: DER-278 is further along, and the move is one Build item here.

❓ **Q4** — **Warn before an agent makes a repo public?** The brief
warns only at the re-check, after the flip.
1. No. 2. Yes: one line in the Repo step, with the same warning, before
any visibility change the operator asks for.
➡️ 2: the warning is worth more before the flip, and it is one line.

## Optional

- **Alternatives rejected** (gather §2, Round 1–2):
  - Four audience levels: tone goes to DER-269.
  - Detecting on every push with nothing recorded: there would be no
    one place to read.
  - A ban on deliverables only: that is today's gap.
  - A private working mirror: sync work; DER-266.
  - A check at Review only: it runs after the push.
  - A deny-list now: deferred with the hook.
  - Encryption by default: metadata leaks and access cannot be
    revoked.
- **PoC questions** — none. No Trial: the shape is text rules, and the
  seeded-diff eval proves them at Build.
- **Risks**
  - The author reads its own diff, and small models miss paraphrase.
    The tester hook is the real control.
  - `sdlc-onboarding` nears its 250-line cap.
  - A host read without auth may fall back to asking the operator too
    often.
  - Stale pushed branches keep leaking until DER-350.
