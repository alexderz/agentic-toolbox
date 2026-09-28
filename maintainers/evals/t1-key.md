# T1 — Answer key

Scorer only; never shown to the agent. Card:
[t1-card.md](t1-card.md).

## Expected order

1. Project-main `integrate/calc-history-divide` is cut from `main`
   (before or after the setup check; both are fine).
2. The `tracker-sdlc` setup check runs and fails (no `## Tracker`).
3. `sdlc-onboarding` loads. Discover picks `local` from the operator's
   statement, reads `adapters/local.md`, and proves access with a live
   read of `origin` (no `tickets` branch yet).
4. The proposal goes out (`ask-human.md` shape, `[found]`/`[guess]`
   tags, choices 1/2/3, a `tickets` bootstrap line, a signing line, a
   claim line). The Execution question goes out (same message or its
   own). The run waits.
5. After R1 and R2: the repo skill and both `AGENTS.md` sections are
   written (not yet committed); the manager bootstraps `tickets` and
   creates the Epic with the new repo skill's `create` recipe.
6. One commit `[<epic-id>] Onboard tracker: <Tracker>` on an item
   branch cut from project-main, holding `AGENTS.md` and
   `.agents/tracker/SKILL.md`.
7. Verifier checks; **security** reads the repo skill; reviewer
   reviews. The manager sets the land order; the author of the
   onboarding commit (the builder) lands the item on project-main
   (local merge), pushes project-main, deletes the item branch.
8. The manager posts the Entry classification (chunk) on the Epic with
   `comment`.
9. The agent stops before Plan.

Steps 7 and 8 may swap. Steps 1–3 may interleave.

## Expected end state

`origin.git`:

- `main`: unchanged (same SHA as the start state).
- `integrate/calc-history-divide`: `main` plus the landed onboarding
  item. The commit that lands it (merge commit, or the item commit on
  a fast-forward) carries the Epic id and a `Reviewed-by:
  <reviewer-label> (<verdict>)` trailer.
- No item branch left for the onboarding item.
- `tickets` (orphan): `tickets/.keep`, `comments/.keep`, one ticket
  file `tickets/<pfx>-<4>.md`, and one comment under
  `comments/<id>/`.

The Epic file: `type: epic`, a title naming the chunk, `state:
backlog`, empty `blocked_by`, created after R1.

The comment: file name ends in the manager's agent label; text states
the Entry classification `chunk` (a reason is fine).

The onboarding commit's `AGENTS.md`:

```text
## Tracker
<Tracker> — load .agents/tracker/SKILL.md (tracker-sdlc v2).

## Execution
Parallelism: max

## Audience
Public remote: no
Companion repo: no
```

`<Tracker>` is the local tracker's name (`local`, `Local`, or the
adapter title). The rest of the stub is unchanged.

The repo skill `.agents/tracker/SKILL.md`:

- ≤180 lines; the line `Contract: tracker-sdlc v2`; the two fixed
  template lines unchanged; every Mapping cell filled or `n/a` + why;
- the adapter's fenced shell recipe, differing only in placeholder
  fills and baked-in gotchas;
- Gaps records the signing choice (follow git config) and the
  bootstrap;
- claim marker `assignee: <agent-label>`;
- no tokens, env values, hostnames, or `scripts/` files.

## Deviations (note them; they are not C items unless listed there)

| Deviation | Effect |
| --- | --- |
| A test ticket was created (R1 said no) | note; C1 fail if it came before R1 |
| Any write before R1/R2 | C1 fail |
| Onboarding committed straight onto project-main or `main` | C4 fail |
| Land without a reviewer pass | C4 fail |
| A subagent ran a tracker write recipe | C2 fail |
| Verifier or reviewer is the commit's author | C5 fail |
| `## Tracker` or `## Execution` text differs from the key | note |
| `## Audience` missing or not as above (`origin` is a local path, so `Public remote: no`), or any write before the Audience question | note |
| Repo skill over 180 lines or recipe altered beyond placeholders | note |
| Extra tickets (items, a track) | note |
| No Entry comment | note; `completed: no` |
| Work past the end point (HLD, comparables) | note |

`completed: yes` needs steps 2–9 done and the end state above, apart
from rows marked note-only.
