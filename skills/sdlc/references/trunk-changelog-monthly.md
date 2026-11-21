# Trunk, Changelog, and Monthly

## Trunk

If the item is an incoming item with no project-main, this step is
`n/a`. The item is already on trunk after Review.

Otherwise, start after the chunk's items are on project-main:

1. The confirmed brief's release permission is not given → the **liaison**
   sends touchpoint 4, the ask to merge ([Touchpoints](../SKILL.md#touchpoints)),
   and the merge waits for the answer. Given → go on; touchpoint 4 is the
   report after step 5.
2. Run the chunk's full journey set on project-main first:
   [After integration](proofs.md#after-integration) steps 3–4.
3. Merge project-main into **trunk**: the repo's protected default
   branch, usually `main`. This merge is the **coherent integrate**.
4. **manager** transitions the Epic to `done` with `tracker-sdlc`. In the `comment`,
   report the revision and result from step 3; cite only shareable artifacts per [After integration](proofs.md#after-integration).
5. Delete project-main.

The `CHANGELOG.md` update may wait for the Changelog step. If
**manager** cancels the chunk, delete project-main.

## Changelog

| Condition | Action |
| --- | --- |
| The chunk is on trunk after the coherent integrate | Promote the `CHANGELOG.md` Unreleased section into a dated chunk heading. Use template `changelog.md` and the heading format in [Conventions](conventions.md#changelog-and-connection). |
| An incoming item is already on trunk | Keep its Unreleased line from Build. Promote that line with the next Changelog pass: a later chunk, or a dated heading that lists that ticket and the trunk SHA. Never write a chunk heading only to close a lone item; leave its line under Unreleased. |

## Monthly

Monthly is **not** the security gate. **security** has already gated
trust boundaries at Spec and Review. Never defer a Spec or Review
security check to Monthly; **security** runs it at that gate.

Monthly is a cadence review of vulns, updates and new solutions. Write
it from template `monthly.md`. Keep it a recurring note, not a ticket,
until the **manager** or the **operator** files a Task. Monthly needs no
watcher and no cron.
