# UX — Tracker-agnostic SDLC and onboarding

High-level. How it feels and who does what — not pixels. **designer.**
Human gate: operator accepts, or writes `UX verification not required`.

- Slug: `tracker-sdlc`
- Brief: DER-252 brief, confirmed 2026-09-24 (Refine: ready for Plan)
- HLD: `docs/tracker-sdlc/hld.md` (Plan, same step)
- Date: `2026-09-24`
- Agent review (requirements only): round 1 fixes applied 2026-09-24
- Operator: accepted 2026-09-24 (with the decisions below folded in)

## People

- **Operator** — owns repo and tracker; confirms proposals, decides gaps.
- **Runtime agent** — any role touching tickets; loads `tracker-sdlc` +
  the repo's `.agents/tracker/SKILL.md` only.
- **Local-ticket agents** — several agents writing `tickets` at once.
- **Work agent** — on the operator's work setup; checks an unverified
  adapter (e.g. Jira) against a live instance.

## Stories (shape: `user-story.md`, one job each)

**TS-1 Onboard with confirmation.** *As* operator *I want* the agent to
find my tracker setup and propose it *so that* I only confirm, not type
it out. **Done when:** proposal covers tracker + access (live read),
project, types, states, blockers, parent, sub-items, PR/branch linking,
each marked found or guessed; asks only what it could not find; nothing
written before the reply. **Out:** non-tracker onboarding.

**TS-2 Gap reported, not patched.** *As* operator *I want* to hear what
my tracker lacks *so that* I decide. **Done when:** a missing concept
(e.g. no native blockers) is named with its fallback (`Blocked-by:` +
`blocked` label); nothing in the tracker schema is created or changed.

**TS-3 Optional test write.** *As* operator *I want* to choose whether a
throwaway ticket is written *so that* recipes are proven only if I allow
it. **Done when:** default is off; on "yes" exactly one ticket is created
then canceled (link reported: design choice); no answer, nothing written.

**TS-4 Setup lands in the repo.** *As* runtime agent *I want* the
confirmed setup in git *so that* later sessions skip discovery. **Done
when:** `AGENTS.md` `## Tracker` (1–2 lines) and `.agents/tracker/SKILL.md`
(recipe per verb, gotchas baked in) are committed at once on the branch
onboarding cuts (chunk: project-main at end of Brief; item: its branch
at item Brief); never trunk; no tokens in either file.

**TS-5 Small runtime load, self-repair.** *As* runtime agent *I want* to
load just the contract and the repo skill *so that* context stays small.
**Done when:** a normal verb reads no adapter; failing recipe → read the
adapter, retry with the fix; still failing → stop that tracker action,
comment on the ticket + report to the orchestrator, propose a repaired
recipe (committed only on operator OK); `## Tracker` missing or check
failing → `sdlc-onboarding`, not guessing.

**TS-6 Claim without collision.** *As* runtime agent *I want* claim =
transition to `in_progress` + a `Claimed by <agent-label> <UTC>` comment
*so that* two agents do not work one ticket, even on one shared tracker
account. **Done when:** claim sets state and the marker, then re-reads
the comments; on an earlier unreleased claim by another label it posts
`Released by <agent-label> <UTC>`. That ticket, or one assigned to
someone else, is neither skipped nor started — the agent checks with
the orchestrator, the source of truth.

**TS-7 Concurrent local writes.** *As* local-ticket agent *I want*
rejected pushes retried safely *so that* all agents' edits land. **Done
when:** rejected → fetch, rebase own unpushed commit only, push; jittered
retry ~10 then comment on the ticket + report to the orchestrator;
linear history, no merge or
force-push; ids checked unique before push.

**TS-8 Verify an adapter live.** *As* work agent *I want* to run the
adapter's facts against a real instance *so that* the header can say
verified. **Done when:** each fact is confirmed or corrected; the
`Verified: no` header flips only after the live run; corrections cite
what was observed (design choice).

## Journeys

- **J1 Chunk onboarding.** Brief ends → agent files the Epic → first
  tracker touch → `sdlc-onboarding` reads adapter + live reads → proposal
  (below) → operator replies → optional test write → cuts project-main →
  commits `## Tracker` + repo skill there (never trunk) → Spec entry gate
  only checks "present and current".
- **J2 Item onboarding.** Entry (no writes) → item Brief opens with J1,
  cutting and committing on the item branch instead.
- **J3 Gap.** Proposal names what is missing + fallback; operator picks.
- **J4 No access.** Live read fails → stop, tell the operator what access
  is missing; no proposal built on guesses.
- **J5 Recipe fails.** Read adapter → retry with the fix → still failing
  → stop that action, comment on the ticket + report to the orchestrator,
  propose a repaired recipe (committed only on operator OK).
  `## Tracker` check fails → onboarding.
- **J6 Local push race.** Rejected → rebase own commit → jittered retry →
  lands; ~10 fails → comment + report to the orchestrator; no force-push.
- **J7 Live verification.** Work agent exercises each Jira adapter fact →
  edits adapter + flips header.

## Example onboarding proposal (Linear, this repo)

```
Need a decision from you before I continue.

What I need
I looked at your Linear workspace to set up how agents file and move
tickets here. Please confirm what I found, or tell me what to change.

What I saw in Linear (nothing written). [found] = read it; [guess] = my pick:
- [found] Where tickets go: team DER, project P-DER-11.
- [found] Kinds: the "Type" label group has Epic and Task; a "Bug"
  label exists outside that group.
- [found] States: Backlog, Todo, In Progress, In Review, Done,
  Canceled, Duplicate.
- [guess] Mapping: Backlog → backlog; Todo → ready (picked up
  next); In Progress →
  in progress; In Review → in review; Done → done; Canceled and
  Duplicate → canceled.
- [found] "Waits on another ticket" is built in (blocks / blocked by).
- [found] Parent: tasks sit under their Epic. [guess] Sub-tasks: off.
- [found] Ticket ids look like DER-123. [guess] PR links: added as a
  comment unless Linear links them itself.
- [found] Branches: Linear suggests alexderz/der-123-…; our process
  uses item/der-123-<slug>. Both contain the ticket id.

Why it matters
Every agent after me follows this. A wrong state mapping means tickets
look finished too early, or never get picked up.

Choices
1. Use it as listed — saved with the rest of this project's changes.
2. Use it with changes — tell me which lines to change.
3. Also let me make one throwaway test ticket (created, then
   canceled) to prove the steps work. Can be added to 1 or 2.

What I recommend
Choice 1. The [found] lines came from live reads; a test ticket adds
noise to the board and the first real ticket proves the same steps.

What to reply
Reply 1, 2 (plus your changes), "1+3" or "2+3" (or "wait").
I will not save anything until you answer.
```

## High-level UX

Conversation only. Operator sees one proposal per onboarding, then only
gap asks and failure reports (J4–J6). Agents see a 1–2 line `## Tracker`
pointer and one repo skill.
**Mockups:** `n/a` — no screen; chat messages and repo files only. The
example message stands in for the one human touchpoint.
**Comparables:** same page as the HLD, `docs/tracker-sdlc/comparables.md`.
**Not this:** per-tracker MCP/CLI manuals; creating tracker types,
states, or labels; live Jira/Asana/Trello tests from this repo;
non-tracker onboarding; the small-work lane (DER-253).

## Decided (operator, 2026-09-24)

1. **Todo** → `ready`; Backlog stays `backlog`.
2. **Failures, operator away** (TS-7, J5, J6) → ticket comment + report
   to the orchestrator.
3. **Assigned to someone else** (TS-6) → check with the orchestrator.
4. **Recipe still failing** (TS-5, J5) → stop, report as in 2, propose a
   repaired recipe; commit only on operator OK.
5. **Branch timing** (TS-4, J1, J2) → onboarding cuts the branch and
   commits the setup at once.

**Deferred** to "onboard this repo": Bug label outside the Linear Type
group; branch names (`alexderz/der-…` vs `item/<ticket>-<slug>`).
