# Chunk — <title>

- Slug: `<chunk-slug>`
- Type: Epic (or tracker equivalent)
- Track: `<track id>`
- HLD: `docs/<path>`
- LLD: `docs/<path>` or n/a until Spec
- Groom: `.agents/design/<chunk-slug>/groom.md` (frozen)
- project-main: `integrate/<chunk-slug>`
- Land path: merge-and-delete after explicit Review (local, serialized);
  push item branches and project-main; no internal PRs

## Required

- **Why this slice, why now**
- **Done** — Trunk: project-main on trunk; tickets landed+verified
- **Children** — Task/Bug ids (may start empty)
- **Wave view** — not kept here; manager posts one Epic comment only
  when the graph reshapes
- **Blocked by** — issue ids, or `none`
- **Blocks** — issue ids, or `none`

## Optional

- Risks that only this chunk carries
- Operator timezone for after-act
