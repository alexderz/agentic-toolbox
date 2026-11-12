# Rule map — trunk-changelog-monthly

Item: DER-739 (G8, source item A7 of DER-712).

Old: `docs/sdlc/trunk-changelog-monthly.md` at main c26f424, lines 1–34. New: `skills/sdlc/references/trunk-changelog-monthly.md`.

The A0 move left this file byte-identical ([A0 path map](a0-path-map.md)).
Edit: the new Trunk step of [overlay G8](../opus-rebuild.md#g8--design-gate-hld-touchpoint-delivery-route-a7) (R159).

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1 | Title | **kept** | L1 |
| 3–6 | Trunk: an incoming item with no project-main → `n/a` | **kept** | L3–6 |
| 8 | Otherwise, start after the chunk's items are on project-main | **kept** | L8 |
| — (after 8) | New Trunk step 1: release permission not given → the liaison sends touchpoint 4, the ask to merge, and the merge waits; given → go on, and touchpoint 4 is the report after step 4 | **changed** (R159; HLD touchpoint 4) | L10–13 |
| 10–11 | Step 1: merge project-main into trunk, the coherent integrate | **kept**, renumbered 2 | L14–15 |
| 12 | Step 2: the manager transitions the Epic to `done` | **kept**, renumbered 3 | L16 |
| 13 | Step 3: delete project-main | **kept**, renumbered 4 | L17 |
| 15–16 | The changelog may wait; a cancelled chunk deletes project-main | **kept** | L19–20 |
| 18–23 | Changelog table | **kept** | L22–27 |
| 25–34 | Monthly: not the security gate; cadence review; no watcher or cron | **kept** | L29–38 |

## Meaning questions

None. The new step adds a route that the HLD names (touchpoint 4: "A report under auto-ship; at
Trunk"); no old line changes meaning.
