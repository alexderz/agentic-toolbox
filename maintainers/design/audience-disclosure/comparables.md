# Comparables — audience and disclosure for public repos

How others keep private context out of a public repo, and when they
check. Written before locking the [HLD](hld.md) shape.

- Slug: `audience-disclosure`
- Brief / options map: [gather.md](gather.md) §2 (options A–E), as
  simplified by [refine.md](refine.md)
- Date: `2026-09-27`

## Required

### 1. GitHub repository networks: a push cannot be recalled

- **Who / what** — GitHub docs on
  [removing sensitive data](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository),
  [fork permissions and visibility](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-permissions-and-visibility-of-forks),
  and [forks when a repo changes visibility](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/what-happens-to-forks-when-a-repository-is-deleted-or-changes-visibility);
  Truffle Security's 2024
  [Cross Fork Object Reference](https://trufflesecurity.com/blog/anyone-can-access-deleted-and-private-repo-data-github)
  research.
- **What they did** — GitHub documents that a pushed commit outlives
  its branch:
  - "GitHub marks those [`refs/pull/`] as read-only."
  - "If the commit that introduced the sensitive data exists in any
    forks, it will continue to be accessible there."
  - Cached views and pull request references go only through GitHub
    Support. "You cannot remove sensitive data from other users'
    clones."
  - "Public repository forks are public … You cannot change the
    visibility of a fork by itself." Git data in a network "may be
    accessed from any repository in the same network … even after a
    fork is deleted."
  - For a secret, "as a first step you need to revoke and/or rotate
    that secret."

  Truffle Security showed deleted-fork and pre-open-sourcing commits
  still readable, and GitHub calls this intended design.
- **Steal** — Everything pushed to a public remote counts as published
  (D3). The only cheap fix is before the push (D6, D7 outcome 1). For
  a leaked credential, rotate first. A repo that goes public publishes
  its whole history: warn at the flip (D2).
- **Won't copy** — History rewrite plus a Support ticket as a routine
  fix. It does not reach forks or clones. Already-public text is an
  operator call (D7 outcome 2), and cleanup is DER-350.

### 2. Secret scanners before the push: gitleaks, git-secrets, GitHub push protection

- **Who / what** — [gitleaks](https://github.com/gitleaks/gitleaks),
  [git-secrets](https://github.com/awslabs/git-secrets),
  [GitHub push protection](https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection).
- **What they did**
  - Push protection "blocks pushes that contain secrets *before* they
    reach your repository". A bypass needs a reason and raises an
    alert.
  - git-secrets installs `pre-commit`, `commit-msg` and
    `prepare-commit-msg` hooks, so commit messages are scanned too.
    Patterns live in local or `--global` git config, or come from a
    provider executable. `--scan-history` scans "all revisions before
    making a repository public". It warns that its patterns are "not
    guaranteed to catch them all".
  - gitleaks runs as a pre-commit hook and loads its config from
    `--config`, `GITLEAKS_CONFIG`, `GITLEAKS_CONFIG_TOML`, then the
    repo's `.gitleaks.toml`. `SKIP=gitleaks` bypasses it.
- **Steal**
  - Check at the last local moment before publication: the push (D6).
  - Read commit messages, not only file diffs.
  - A deny-list, when it comes, lives outside the repo (global config
    or an env path). That is the deferred **tester** ticket.
  - `--scan-history` is the tool DER-350 and the flip warning can
    point at.
- **Won't copy** — A hook now: it is the separate **tester** ticket
  (brief, Out of scope). Regex scanners match secret shapes. They miss
  internal hostnames, people's names and paraphrase, which is most of
  our ban, so the agent read stays. The bypass is also out: the pushing
  agent does not push past a hit. Push protection covers only secrets
  and only GitHub.

### 3. GitLab: public handbook first, internal handbook for the rest

- **Who / what** — GitLab
  [handbook usage](https://gitlab.com/gitlab-com/content-sites/handbook/-/raw/main/content/handbook/about/handbook-usage.md)
  and the [SAFE framework](https://handbook.gitlab.com/handbook/legal/safe-framework/).
- **What they did** — GitLab keeps its company handbook public.
  "We default to the public handbook for anything that can be made
  public." "Only add items to the internal handbook that fall into the
  not public category." A narrower "limited access" class goes in
  neither. SAFE names the categories that must not be published
  (team-member data, customer names, non-public financials) and who
  approves exceptions.
- **Steal** — A public repo plus a private companion that holds only
  what cannot be public (D4). Everything else stays in the public repo.
  Named categories decide, not case-by-case taste (D3's category ban).
- **Won't copy** — Three confidentiality levels and a legal approval
  flow. Our audience is one bit (D2), and the companion is optional
  per repo. GitLab's internal handbook is company-wide behind SSO. Ours
  is whatever private repo the operator names.

### 4. Agent instruction files: AGENTS.md and Claude Code memory

- **Who / what** — The [AGENTS.md](https://agents.md/) convention;
  Claude Code [memory](https://code.claude.com/docs/en/memory)
  (`CLAUDE.md`, `CLAUDE.local.md`, user memory).
- **What they did**
  - AGENTS.md has no required fields ("Use any headings you like") and
    suggests a "Security considerations" section. It has no audience
    or visibility field.
  - Claude Code shares `CLAUDE.md` through version control. It keeps
    private per-project notes ("sandbox URLs") in a gitignored
    `CLAUDE.local.md`, and personal notes in the home directory. A
    gitignored local file "only exists in the worktree where you
    created it". A `CLAUDE.local.md` also counts as an instruction
    file, so by default AGENTS.md is no longer read.
  - Memory is "context, not enforced configuration". To block an
    action, the docs point at a hook.
- **Steal**
  - A named section in the instruction file that every agent reads
    first: `## Audience` (D2).
  - Private context sits beside the repo, never in tracked files (D4).
  - Instruction text is context, not a control. That matches
    security-hardening's "Prompts are not a boundary", and the
    mechanical control is the **tester** hook.
- **Won't copy** — A gitignored local file as the home for shared
  private context. It is per clone and per worktree, so other agents
  never see it. In a repo that relies on AGENTS.md, it also stops
  AGENTS.md from loading. No convention records audience, so
  `## Audience` is our own.
