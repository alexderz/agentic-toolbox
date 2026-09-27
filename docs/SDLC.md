# SDLC

Shared process for work that uses this skills home. Software is the
common case; the same steps apply to docs, process changes, and other
tickets. Git holds durable artifacts. The issue tracker is the board.
Branches and land commits cite a ticket ID when the project uses
tickets.

## How to read

1. Find your step in [Steps](#steps).
2. Read the file in that row's Read column.
3. You are the **manager** → also read
   [branches-and-lands.md](sdlc/branches-and-lands.md) and
   [subagents.md](sdlc/subagents.md).

## Roles

Skills are **tools**, keyed by role. Improvise when the work needs it.
Do not remint a skill that already has an id here.

| Role | Job |
| --- | --- |
| **architect** | Design, HLD/LLD, adversarial review of approach |
| **designer** | User stories, high-level UX, Spec mockups when there is a screen |
| **builder** | Implement and ship |
| **tester** | Mechanical CI, hooks, cleanup, verification evidence |
| **security** | Gates at Spec (trust boundaries) and Review, plus skill intake — not only a monthly vuln pass |
| **manager** | Process, board after-act, and land order (local, serialized merges; no PRs). Sole tracker writer. Does not bless ships |
| **operator** | Human in the loop: exceptions, vuln severity, extra hosts, personal accounts |

Workers (agents, CI bots) act as **builder** or **tester**. They do not
bypass **security**.

## Names

Name formats: [Conventions](sdlc/conventions.md#name-formats).

## Tracker

| Layer | Typical object | Meaning |
| --- | --- | --- |
| Track | Project (or the tracker's equivalent) | One product or process track |
| Chunk | Epic | Discrete, parallel slice |
| Work item | Task or Bug under its Epic | Implementable unit. Sub-items only if the repo's tracker skill enables them |

**Every tracker read and write goes through
[`tracker-sdlc`](../skills/tracker-sdlc/SKILL.md)** and the product
repo's `.agents/tracker/SKILL.md`. Canonical states (six): `backlog`,
`ready`, `in_progress`, `in_review`, `done` (= landed+verified; an Epic
when on trunk), `canceled`. Blocked is not a state: an item is blocked
while it has open blockers.

**Only the orchestrator (manager) writes to the tracker:** create,
claim, release, set-blocker, comment, and every transition. Builders,
verifiers, and reviewers never write to it; they report, and the
orchestrator writes.

After-act **manager** with the operator's timezone. The board is the
tracker; git holds the files. Designs live in git from onset — do not
keep HLD/LLD only on a local mirror.

## Grain

The board layer **is** the grain. Do not add a fourth issue type.

| Arrives as | Needs a person for taste / design talk? | Enter at |
| --- | --- | --- |
| New product or process track | Yes | **Chunk** that also writes `track.md`. Full ladder; write Plan and Spec |
| Feature, redesign, fuzzy idea | Yes | **Chunk** — interview; write or extend Plan and Spec |
| Broken build, failing test, mechanical bug | No | **Item** — problem + fix; align existing Plan and Spec |

**Entry** (first step) classifies, or asks. It does not fix.

A UI defect stays an item until analysis shows the question is “what
should this screen be?” Then it is a chunk (or promote).

Work split from an **accepted Spec** is already an item in **Build**.
Do not re-run item-Brief on those Tasks. If Build finds a shape change,
escalate (ask, block that issue, siblings proceed).

<a id="asking-the-human"></a>

## Asking the operator

When a person must decide, **stop and say so.** Do not hide the ask in a
status dump. Do not keep going as if they said yes. Do not use project
words (`HLD`, `LLD`, `project-main`, `DoD`, ticket codes) unless you
immediately say what they mean in everyday language.

Use this shape (template `ask-human.md`):

```
Need a decision from you before I continue.

What I need
<the choice, in plain language>

Why it matters
<what happens if we wait, guess, or pick each way>

Choices
1. <option> — <what you get>
2. <option> — <what you get>
3. <option, if any>

What I recommend
Choice N, because <one or two reasons>.

What to reply
Reply with 1, 2, or 3 (or “wait” / “don’t need my OK on this”).
I will not continue this part until you answer.
```

Show the recommendation **and** why. If there is no good default, say
that. One question per message when you can; if several must be
together, number them and say which you recommend as a set.

**When this is required:** accepting the write-up, the look-and-feel,
or the detailed design; waiving a check; an open blocker you cannot
finish; three failed fixes; anything in an Ask-first row; spending
money; destructive actions.

**Never:** “Please advise.” “LGTM?” “UX verification not required?”
with no explanation. Proceeding after silence.

Waiting on a person is a **blocker on that issue**. Other unblocked
items keep moving. Do not freeze the chunk. If the operator wrote that
they are AFK / headless / autonomous, the parent may pick between two
**item** fixes that both honor the existing plan. It must **not** change
Plan or Spec shape — those stay blocked until a person answers.

## Steps

Same names at every grain. Grain changes **what you write** and how many
agents, not which steps exist. Headings and tickets use the **name**.

| Step | What it is | Read |
| --- | --- | --- |
| [Entry](sdlc/entry-brief-repo.md#entry) | Classify chunk vs item, or ask. Do not fix. | [entry-brief-repo.md](sdlc/entry-brief-repo.md) |
| [Brief](sdlc/entry-brief-repo.md#brief) | Chunk: Gather ↔ Refine. Item: problem+fix vs removal, then pick. | [entry-brief-repo.md](sdlc/entry-brief-repo.md) |
| [Repo](sdlc/entry-brief-repo.md#repo) | Git ready, agents aware. Item: confirm, do not reinvent. | [entry-brief-repo.md](sdlc/entry-brief-repo.md) |
| [Plan](sdlc/plan-trial-spec.md#plan) | Write or **align** HLD. Shape change → escalate. | [plan-trial-spec.md](sdlc/plan-trial-spec.md) |
| [Trial](sdlc/plan-trial-spec.md#trial) | Optional proof. Item: usually skip. | [plan-trial-spec.md](sdlc/plan-trial-spec.md) |
| [Spec](sdlc/plan-trial-spec.md#spec) | Write or **align** LLD. Shape change → escalate. | [plan-trial-spec.md](sdlc/plan-trial-spec.md) |
| [Groom](sdlc/groom-step.md) | Tickets, blockers, land path. Incoming item: this ticket. | [groom-step.md](sdlc/groom-step.md) |
| [Build](sdlc/build-review.md#build) | Implement ↔ test until DoD. | [build-review.md](sdlc/build-review.md) |
| [Review](sdlc/build-review.md#review) | Reviewer ≠ builder. Required for every land (no PRs). | [build-review.md](sdlc/build-review.md) |
| [Trunk](sdlc/trunk-changelog-monthly.md#trunk) | Land project-main on the official copy (when a chunk used one). | [trunk-changelog-monthly.md](sdlc/trunk-changelog-monthly.md) |
| [Changelog](sdlc/trunk-changelog-monthly.md#changelog) | Promote Unreleased. | [trunk-changelog-monthly.md](sdlc/trunk-changelog-monthly.md) |
| [Monthly](sdlc/trunk-changelog-monthly.md#monthly) | Cadence, not a ship gate. | [trunk-changelog-monthly.md](sdlc/trunk-changelog-monthly.md) |
| Manager: branches and lands | Project-main, land path, Never | [branches-and-lands.md](sdlc/branches-and-lands.md) |
| Manager: subagents | Step and item agents, spawn prompts, workers | [subagents.md](sdlc/subagents.md) |
| Conventions | Names, commits, layout, changelog, designs in git, old Stage numbers | [conventions.md](sdlc/conventions.md) |

HLD and LLD are **artifact** names (`docs/hld.md`, `docs/lld.md`). The
steps are Plan and Spec.

## Skill table

Ids and ownership: [SOURCES.md](../SOURCES.md). Empty SHA = no body yet.
No marketplace install. No auto-update. See [INTAKE.md](INTAKE.md).

| Skill | Role | Notes |
| --- | --- | --- |
| `tracker-sdlc` | manager (writes) / architect (reads) | Contract for all tracker reads/writes; loads the repo's `.agents/tracker/SKILL.md` |
| `sdlc-onboarding` | manager / architect | First tracker touch and Spec gate failure; proposes, writes `## Tracker` and `## Execution` on confirm |
| `cursor-cloud-agents-when` | architect | Empty dir until a first-party body |
| `discover-the-idea` | architect | Brief Gather on a **chunk**. Load the skill; do not paste it here. Do not load on an incoming item |
| `ux-design` | designer | Stories + high-level UX at Plan; mockups at Spec if there is a screen. Human gate |
| `sdlc-artifacts` | architect / manager / designer | Templates for HLD/LLD/UX/tickets/changelog. Do not paste the SDLC into them |
| `tdd` | builder | Fail-first |
| `debug` | builder | Default systematic debug. Load on failure and on incoming-item Brief. Alternatives: `debug-pocock`, `debug-anthropic` |
| `docs-google-style` | builder / architect | Human how-tos + agent-facing contracts after Spec |
| `pr-review` | architect / security / builder | Reviewer ≠ builder; receive-review on the builder; Standards vs Spec |
| `security-hardening` | security | Always / Ask first / Never |
| `shell-safety` | security / tester | Classify before a command runs |
| `verify-before-done` | builder / tester | Build / notify landed+verified; resume verifier |
| `grok-acp` | manager / builder | Operator opt-in worker: Grok Build over ACP as the item's builder. Label = `builder_id`; mint packs, resume is delta-only. Never the verifier or reviewer of its own item |
| `pr-lens` | builder / manager | Operator opt-in: PR Lens diagrams for the PR into `main`. Local render + `gh --attach` only; no canvas, no `analyze`; CLI pinned `@coldtea/pr-lens-cli@0.8.1` |
| `yagni` | architect / builder | Smallest change that meets this Task; Brief Refine (chunk) and removal alternative (item) |
| `modern-python` | builder | uv / ruff / ty / pytest |
| `golang-testing` | builder / tester | Go test shape |
| `golang-safety` | builder | Nil / slice / numeric traps |
| `golang-security` | security / builder | Exploitable Go issues |
| `language-router` | builder | Pick at most one language-family skill |
| `lang-*` | builder | Pointers or language guides |

Pin SHAs in [SOURCES.md](../SOURCES.md). **security** intake before any
vendor content. See [INTAKE.md](INTAKE.md).
