# Trunk, Changelog, and Monthly

## Trunk

If the item is an incoming item with no project-main, this step is
`n/a`. The item is already on trunk after Review.

Otherwise, start after the chunk's items are on project-main:

1. Merge project-main into **trunk**: the repo's protected default
   branch, usually `main`. This merge is the **coherent integrate**.
2. **manager** transitions the Epic to `done` with `tracker-sdlc`.
3. Delete project-main.

The `CHANGELOG.md` update may wait for the Changelog step. If
**manager** cancels the chunk, delete project-main.

## Changelog

| Condition | Action |
| --- | --- |
| The chunk is on trunk after the coherent integrate | Promote the `CHANGELOG.md` Unreleased section into a dated chunk heading. Use template `changelog.md` and the heading format in [Conventions](conventions.md#changelog-and-connection). |
| An incoming item is already on trunk | Keep its Unreleased line from Build. Promote that line with the next Changelog pass: a later chunk, or a dated heading that lists that ticket and the trunk SHA. Never write a chunk heading only to close a lone item; leave its line under Unreleased. |

## Monthly

Monthly is **not** the security gate. **security** has already gated
trust boundaries at Spec and Review. Monthly is not a substitute for
those gates. Never defer a Spec or Review security check to Monthly;
**security** runs it at that gate.

Monthly is a cadence review of vulns, updates and new solutions. Write
it from template `monthly.md`. Recurrence note only until **manager** /
**operator** cut a Task. Monthly needs no watcher and no cron.
