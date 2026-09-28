# DER-286 gather, round 1

Chunk Brief (Gather). Repo: `instruction-refinement` worktree at
project-main `88455d8`. Skill: `skills/discover-the-idea/SKILL.md`.
Language skills: none loaded.

## Reflect (dump restated)

Each repo gets a declared audience and a disclosure policy, learned at
onboarding and confirmed at Brief. The audience sets tone and what may
be revealed. Private context (home-lab names, IPs, and similar) must
never enter a public repo's git. Deleting it before a squash does not
help: pushed branches, `refs/pull/N/head`, tags, forks, caches, and the
local tracker's `tickets` branch all publish it. Private context lives
in a private channel (the tracker, or a private working remote).
**security** reads every diff, and every push to a public remote,
against the policy. Encrypted-in-repo is probably rejected.

Still vague: how many audience levels really matter; which private
channel; when the check runs, given that pushes happen before Review;
where a concrete deny-list lives; what happens to the local tracker on
a public repo. Round 1 targets these. The operator confirms or corrects
this restatement with the Round 1 answers.

## 1. Environment facts

Paths are relative to the worktree root.

- **E1. Public-repo rule.** `AGENTS.md:16-32`. Deliverables: no
  names beyond credits, no private tracker workspace URLs or names, no
  internal hostnames or IPs, no credentials, no session leftovers
  (`:20-27`). Agent context (`maintainers/design/`, `maintainers/.agents/`,
  other `maintainers/` notes) "can be informal: civil and
  credential-free" (`:28-30`). Commit messages, PR descriptions and tags
  are public and permanent (`:31-32`). Repeated in
  `maintainers/AGENTS.md:45-47`.
  **Gap:** the hostname/IP ban names only deliverables. Agent context
  sits in the same public git, but its rule says only "civil and
  credential-free". The dump's constraint (everything pushed is
  published) is not stated.
- **E2. security-hardening has no disclosure rule.** Gate = LLD and PR
  (`skills/security-hardening/SKILL.md:10`). The nearest rows are Never
  "Secrets in git" (`:55`) and Ask first "New sensitive data classes"
  (`:38`). The "Extra hosts" Never row (`:62`) is about *using* a
  machine, not naming it. "Prompts are not a boundary" (`:12-16`): a
  text-only rule is not a control by the skill's own standard.
- **E3. INTAKE covers only third-party intake.** `docs/INTAKE.md:3-32`.
  Workers (`:40-49`): **security** reads a repo tracker skill for tokens,
  `scripts/` and executable blocks, not for disclosure.
- **E4. SDLC security gates run after the push.** **security** gates at
  Spec and Review (`docs/SDLC.md:31`). Spec gate: LLD trust boundaries
  "authn/z, secrets, egress, data class, who may write what"
  (`docs/sdlc/plan-trial-spec.md:108-116`). Review: "intake, SHA pins,
  and trust-boundary deltas" (`docs/sdlc/build-review.md:97-100`). But
  the item branch is pushed "while it is built and reviewed"
  (`docs/sdlc/branches-and-lands.md:51`). On a public remote, the text
  is published before any **security** read.
- **E5. No mechanical scan.** CI is fmt/lint only, "No ... secret
  scan" (`.github/workflows/fmt-lint.yml:1-4`). Secret scan parked for
  **tester** (`maintainers/CI-HOOKS-PLAN.md:34,44,49`).
- **E6. sdlc-onboarding asks about two areas.** `## Tracker` and
  `## Execution` (`skills/sdlc-onboarding/SKILL.md:19-20`). Each area has
  Check / Discover / Propose / Write. "A new area adds a section with the
  same four parts and one row in this table; nothing else changes"
  (`:40-42`), a natural slot for `## Audience`. Tracker Discover reads
  MCP/CLI **host names** (`:81-82`), and Never allows "Env var names and
  host names" in files (`:196-197`). A self-hosted tracker's internal
  host name could land in a public repo's `.agents/tracker/SKILL.md`,
  which may conflict with a disclosure policy. The local `tickets`
  bootstrap gets its own proposal line (`:122-128`), but visibility is
  not mentioned.
- **E7. Local tracker lives on the public remote.** Branch `tickets` on
  the repo's own `origin`, orphan, no force-push
  (`skills/tracker-sdlc/adapters/local.md:9-10`). Hooks are off for every
  git command, so no secret scan runs (`:49-52`). History grows without
  bound, and a squash would need a force-push (Never) (`:185-186`). On a
  public repo every ticket and comment is published and cannot be
  removed.
- **E8. Designs live in git.** HLD, LLD, PoC notes, decisions and
  changelogs live in git from Repo on (`docs/sdlc/conventions.md:71-75`).
  Product layout puts the Groom plan under `.agents/design/` (`:39`).
  `.agents/` rule: "No credentials, internal hostnames, or private
  workspace URLs" (`:43-44`). Repo step: "Make it private only when the
  operator says so" (`docs/sdlc/entry-brief-repo.md:125-126`).
- **E9. Observed on this repo.** `git branch -r` shows many pushed item
  branches still on `origin` after landing (for example
  `origin/item/der-272-maintainers`), although the land path says
  "Delete the item branch" (`docs/sdlc/branches-and-lands.md:52`). This
  is live evidence for the dump's constraint.
- **E10. Neighbours.** This repo's tracker is Linear
  (`maintainers/AGENTS.md:14-16`). Its repo skill names only the MCP
  host `mcp.linear.app` (`maintainers/.agents/tracker/SKILL.md:9`).
  Instruction-refinement lists DER-286, DER-266 and DER-287 as
  non-goals (`maintainers/design/instruction-refinement/hld.md:26`).

## 2. Options map

| Option | Who uses it | Ugly part | Fit to dump | Source |
| --- | --- | --- | --- | --- |
| **A. Text rule + agent read** (`## Audience`, **security** reads the diff) | This repo today (E1) | Not a control by security-hardening's own rule (E2). Runs after the push (E4). | Cheapest. The minimum floor. | E1, E2, E4 |
| **B. Private tracker holds private context** | This repo (Linear, E10) | Only works with a hosted private tracker. The local tracker on a public repo is public (E7). | Direct fit. Already in place here. | E7, E10 |
| **C. Private working remote, sanitized PRs upstream** | Common for private work on public projects | GitHub forks of public repos are always public, and "You cannot change the visibility of a fork by itself". It must be a mirror/duplicate, synced by hand (`git fetch -p origin`, `git push --mirror`). Two remotes to reason about. | Fits DER-266. Heavy. | https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-permissions-and-visibility-of-forks ; https://docs.github.com/en/repositories/creating-and-managing-repositories/duplicating-a-repository |
| **D. Mechanical deny-list scan, list kept outside the repo** | git-secrets: patterns in repo or **global** git config, or from a "provider" executable. pre-commit and commit-msg hooks, global template install. gitleaks: `--config`, `GITLEAKS_CONFIG` path, or `GITLEAKS_CONFIG_TOML`. Can scan a log range. | Regex misses paraphrase. Per-machine setup. The local tracker recipe forces hooks off (E7). | Fits "deny-list lives in the private channel". | https://github.com/awslabs/git-secrets ; https://github.com/gitleaks/gitleaks |
| **E. Encrypted in repo** (git-crypt, sops) | git-crypt: repos that are mostly public with a few secret files | git-crypt "does not encrypt file names, commit messages ... or other metadata". It "does not support revoking access". It is "not the best tool for encrypting most or all of the files". | Poor. Metadata leaks and key handling (as the dump expects). | https://github.com/AGWA/git-crypt |

Background for the constraint: GitHub marks `refs/pull/` read-only.
Data in forks "will continue to be accessible there". Removing cached
views and PR references needs GitHub Support. Other users' clones
cannot be cleaned.
https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository

## 3. Round 1 questions

❓ **Q1** — **How many audience levels?**
1. Four levels, as in the dump. 2. One yes/no: does the repo push to a public remote? Tone goes to the style guide (DER-269); workplace rules go to DER-287. 3. Keep this repo's rule; no per-repo setting.
➡️ 2: the public remote drives the leak risk; the other levels are tone.

---

❓ **Q2** — **Where does private context live for a public repo?**
1. The private tracker only. 2. A private copy repo as the working remote. GitHub forks of public repos are always public, so it must be a hand-synced mirror, not a fork. 3. The tracker by default; the private copy later, with DER-266.
➡️ 3: the tracker is already private; a mirror adds sync work.

---

❓ **Q3** — **Local-file tracker on a public repo.** Its `tickets` branch sits on the public remote, can never be force-pushed, and runs no hooks, so every ticket is public forever.
1. Refuse it. 2. Allow it only after an explicit yes at onboarding. 3. Put `tickets` on a separate private remote.
➡️ 2: onboarding already asks about the bootstrap on its own line; 3 is a later ticket.

---

❓ **Q4** — **When does the disclosure check run?** Item branches are pushed before Review, so a Review-time check is too late.
1. At Review only. 2. The pushing agent reads the outgoing diff before every push to a public remote. 3. 2, plus a mechanical hook (gitleaks or git-secrets).
➡️ 2 now; 3 as a separate tester ticket (CI has no secret scan today).

---

❓ **Q5** — **A deny-list of concrete names and IPs?**
1. None; category rules, as today. 2. In a private tracker document. 3. In machine-level config outside any repo (global git config, a gitleaks config path).
➡️ 1 now; 3 lands with Q4's hook.

---

❓ **Q6** — **Encrypted files in the repo (sops, git-crypt)?**
1. Never. 2. Ask first, per repo.
➡️ 1: git-crypt leaves file names and commit messages readable and cannot revoke access.

Reply per question, for example "Q1: 2". I will not continue until you answer.

## Round 1 answers (operator, 2026-09-27, relayed by the manager)

- **Q1: 2.** A single yes/no: does the repo push to a public remote?
  Tone goes to DER-269, workplace rules to DER-287.
- **Q2: tracker by default, plus an optional private companion repo**
  (the operator's idea). It sits next to the public repo and holds
  notes that do not fit in tickets. It is not a mirror or fork and
  never syncs code. This replaces option C.
- **Q3: 2.** The local tracker is allowed on a public repo only after
  an explicit yes at onboarding. A separate private remote comes later.
- **Q4: 2.** The pushing agent reads the outgoing diff before every
  push to a public remote. A gitleaks hook is a separate **tester**
  ticket (option D deferred).
- **Q5: 1.** No deny-list for now; keep the category rules.
- **Q6: the user's choice, never by default.** When the user asks for
  it, explain the limits (metadata stays readable, access cannot be
  revoked). Quote: "We never say never. We don't tell the user what
  to do." Option E is allowed on request, not a default.
- **Related (DER-278, 2026-09-27):** PoC code is pushed as it is
  written, after the same pre-push diff scan. This confirms that the
  scan covers every push, not only item branches.

## Frontier after Round 1

Settled: the audience setting is one bit; the private channel is the
tracker plus an optional companion repo; the check runs before every
push; no deny-list; encryption only on request.

Open (Round 2):
- Where the bit is recorded, and how it is detected (E6 slot).
- Coverage: does the published-text rule cover everything pushed?
  E1 covers only deliverables; E6 allows host names in the tracker
  skill; E7 covers tickets.
- How agents find the companion repo without publishing its location
  (AGENTS.md:24 bans private workspace URLs and names).
- What the agent does when the scan finds something, before and after
  the push.
- Text already published (E9), and a repo that goes from private to
  public.

## Round 2 questions

❓ **Q1** — **Where is the public/private answer kept?**
1. A new onboarding section `## Audience` in AGENTS.md with `Public remote: yes|no`. Agents detect it from the host (for example `gh repo view`) and ask only when that fails. 2. Detect on every push; record nothing.
➡️ 1: one place to read. Re-checked at each chunk Brief, like `## Tracker`.

---

❓ **Q2** — **What counts as published?** Today the hostname/IP ban covers only deliverables. Agent notes, commit text, tickets, PoC code and onboarding's tracker host names are exempt.
1. Everything pushed to a public remote follows the ban. 2. Deliverables only, as today.
➡️ 1: it is your constraint, and the pushed item branches still on the remote prove it.

---

❓ **Q3** — **How do agents find the companion repo?**
1. AGENTS.md names it by URL. 2. AGENTS.md says only that one exists; its location lives in the tracker. 3. Each machine's local config.
➡️ 2: AGENTS.md already bans private workspace URLs; the tracker is shared by all agents.

---

❓ **Q4** — **The pre-push read finds private text. Then what?**
1. Stop, move the text to the tracker or companion, rewrite the unpushed commits, then push. If it is already public: stop and ask you, with no automatic history rewrite. 2. Always stop and ask you.
➡️ 1: an unpushed fix is safe and local; a public leak needs your call.

---

❓ **Q5** — **Already-public text, and a repo that goes public.**
1. Out of scope: a separate ticket audits current history and stale branches. When a repo goes public, warn that its history is now public. 2. In this epic.
➡️ 1: this epic stops new leaks; cleanup is separate work.

Reply per question, for example "Q1: 1". I will not continue until you answer.

## Round 2 answers (operator, 2026-09-27, relayed by the manager)

- **Q1: 1.** `## Audience` in AGENTS.md with `Public remote: yes|no`.
  Detected from the host; asked only if detection fails; re-checked at
  each chunk Brief.
- **Q2: 1.** Everything pushed to a public remote follows the ban.
- **Q3: 2.** AGENTS.md says only that a companion exists; its location
  lives in the tracker.
- **Q4: 1.** An unpushed leak is fixed locally, then pushed. An
  already-public leak stops and asks the operator; no automatic history
  rewrite.
- **Q5: 1** (answered later, 2026-09-27). Already-public text goes to
  the separate audit ticket DER-350. When a repo goes public, warn that
  its history is now public.

Frontier: empty. Q5 was the out-of-scope and failure-mode round; the
session stops (3 rounds used of 4).

## Brief (final, ready to stop)

**Intent.** Each repo records one fact: does it push to a public
remote? When the answer is yes, nothing private is ever pushed, because
everything pushed counts as published. Private context lives in the
tracker, or in an optional private companion repo.

**Out of scope.** Tone and style levels (DER-269). Workplace rules
(DER-287). A private working remote, mirror or fork (DER-266). A
separate private remote for `tickets` (later). A concrete deny-list. A
gitleaks or other mechanical hook (separate **tester** ticket).
Auditing already-published history and stale pushed branches (DER-350).

**Constraints.**
- Pushed branches, `refs/pull/N/head`, tags, forks and caches cannot
  be cleaned, so a pushed leak cannot be recalled (GitHub docs; E9).
- The local `tickets` branch cannot be force-pushed and runs no hooks
  (E7).
- Item branches and PoC code are pushed before Review (E4, DER-278).
- Prompts are not a boundary (E2), so the text rule is a floor, not a
  control.
- sdlc-onboarding areas are Check/Discover/Propose/Write (E6).

**Decisions.**
- D1. The audience is one yes/no, not four levels. The public remote
  drives the risk; the other levels are tone.
- D2. A new onboarding area records it: `## Audience`, next line
  `Public remote: yes|no`. Detected from the host; asked only if
  detection fails; re-checked at each chunk Brief. Chosen over
  detecting on every push, so there is one place to read.
- D3. The ban (internal hostnames, IPs, private workspace URLs and
  names, people's names, credentials) covers everything pushed to a
  public remote. That includes agent notes under `maintainers/` and
  `.agents/`, commit and PR text, tags, `tickets`, PoC code, and the
  tracker host names onboarding writes. Chosen over "deliverables
  only" (today's E1), which leaves the gap.
- D4. Private context goes to the tracker by default. An optional
  private companion repo holds notes that do not fit in tickets. It is
  not a mirror or fork and never syncs code. Chosen over a private
  working mirror, which adds sync work.
- D5. AGENTS.md says only that a companion exists; its location lives
  in the tracker. Chosen over a URL in AGENTS.md, which AGENTS.md:24
  already bans.
- D6. The pushing agent reads the outgoing diff before every push to a
  public remote. Chosen over a check at Review only, which runs after
  the push.
- D7. On a hit before the push: move the text to the tracker or
  companion, rewrite the unpushed commits, then push. On a hit that is
  already public: stop and ask the operator, with no automatic history
  rewrite.
- D8. The local tracker is allowed on a public repo only after an
  explicit yes at onboarding, on the bootstrap line.
- D9. No deny-list; category rules only.
- D11. When a repo goes from private to public (the `## Audience`
  re-check flips to `yes`), warn the operator that its whole history is
  now public. No automatic rewrite. The cleanup goes to DER-350. Chosen
  over auditing inside this epic.
- D10. Encrypted files in the repo (sops, git-crypt) are the user's
  choice and never a default. On request, the agent explains the
  limits: file names and commit messages stay readable, and access
  cannot be revoked. Operator: "We never say never. We don't tell the
  user what to do."

**Assumptions.**
- The host exposes repo visibility (for example `gh repo view`).
  Elsewhere, the agent asks.
- The pushing agent is the one that can stop the push. Every push path
  (item branches, project-main, `tickets`, PoC) goes through an agent.
- The tracker is private whenever it is hosted.
- `Public remote: no` changes nothing from today.

**Options map.** A: text rule plus agent read (taken, as the floor).
B: private tracker (taken). C: private mirror (replaced by the
companion, D4). D: mechanical scan (deferred to a **tester** ticket).
E: encryption (on request only, D10). Sources: §2.

**Open.**
- None. Deferred to other tickets: DER-350 (audit), the **tester**
  gitleaks ticket, a private `tickets` remote, DER-266, DER-269,
  DER-287.

**Verify later.**
- A public-remote repo's AGENTS.md has `## Audience` /
  `Public remote: yes`. Onboarding writes it from the host read and
  re-checks it at chunk Brief.
- The root public-repo rule and security-hardening state the ban for
  all pushed text, not only deliverables.
- The branch, land and PoC push steps carry the pre-push read, and its
  two outcomes (fix before the push; stop and ask after it).
- sdlc-onboarding's local bootstrap line needs an explicit yes when
  the remote is public. Tracker host names are not written into a
  public repo.
- AGENTS.md names no companion location.
- When the re-check flips from `no` to `yes`, the operator gets the
  history-is-public warning.
- An eval or seeded diff with a fake internal hostname is stopped
  before the push.
