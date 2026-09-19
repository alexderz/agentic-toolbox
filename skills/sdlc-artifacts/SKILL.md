---
name: sdlc-artifacts
description: use this when writing or updating an HLD, LLD, ticket, epic, track/roadmap, PoC note, decision, changelog, PR, monthly note, human how-to, or AGENTS stub that the SDLC calls for — copy the matching template and fill required fields. do not use to invent a second process or to skip a gate.
---

# SDLC artifacts

Fill-in shapes for artifacts the SDLC already requires. Process lives in
[docs/SDLC.md](../../docs/SDLC.md). **Copy a template; do not paste the
SDLC into the artifact.** No `scripts/`.

## Iron law

**One template per artifact. Fill every required field or write `n/a`
and why.** Do not invent a parallel outline.

## Map

| Artifact | Step | Template | Lands in |
| --- | --- | --- | --- |
| Brief (chunk) | Brief | `discover-the-idea` (not here) | Chat unless asked to file |
| Incoming item | Brief | `templates/bug.md` / `task.md` | Same files as Groom; fill Proposed fix / Removal / Pick **at Brief**, not later |
| Track / roadmap | Plan | `templates/track.md` | Board project; git copy optional |
| Chunk / epic | Plan–Groom | `templates/chunk.md` | Board parent issue |
| HLD | Plan | `templates/hld.md` | `docs/hld.md` or `docs/<slug>/hld.md` |
| Comparables | Plan | `templates/comparables.md` | `docs/comparables.md` or `docs/<slug>/comparables.md` |
| UX / journeys | Plan | `templates/ux.md` | `docs/ux.md` or `docs/<slug>/ux.md` |
| User story | Plan | `templates/user-story.md` | `docs/stories/` or the board |
| PoC | Trial | `templates/poc.md` | `docs/` next to the HLD |
| LLD | Spec | `templates/lld.md` | `docs/lld.md` or `docs/<slug>/lld.md` |
| Mockups | Spec | `templates/mockup.md` | `docs/mockups/` (or `n/a`) |
| Decision | any | `templates/decision.md` | `docs/decisions/<slug>.md` |
| Task | Groom | `templates/task.md` | Board issue, label Task |
| Bug | Groom | `templates/bug.md` | Board issue, label Bug |
| Changelog | Build / Changelog | `templates/changelog.md` | repo-root `CHANGELOG.md` |
| PR / land | Review | `templates/pr.md` | PR body or merge message |
| Monthly | Monthly | `templates/monthly.md` | Ticket or `docs/monthly/` |
| Human doc | Spec+ | `templates/human-doc.md` | `docs/` how-to (Google style) |
| Ask the human | any gate | `templates/ask-human.md` | The message to the person — not a git file |
| AGENTS stub | Repo | `templates/agents-stub.md` | product-repo `AGENTS.md` |

## Always

- Copy the file. Delete unused *optional* sections. Keep required ones.
- Link the layer above and below (track → chunk → item; HLD → LLD →
  ticket). Changelog line cites ticket + land SHA or PR.
- Linear: paste the ticket/chunk/track body into the issue or project
  description. Set `blockedBy` / `blocks` as fields, not only as text.
- Dates ISO-8601. Slugs lowercase hyphen.

## Ask first

- A new artifact type that is not in the map.
- Skipping a required field other than with `n/a` + why.

## Never

- A second HLD/LLD/ticket outline “just this repo.”
- Cloning the `discover-the-idea` brief into `templates/`.
- Empty acceptance or empty trust-boundary section on an LLD that
  touches a boundary.
- Language skills on a templates-only turn.

## Red flags

- “I’ll freehand the HLD”
- “Acceptance is ‘it works’”
- “No blockers, we’ll sequence in chat”
