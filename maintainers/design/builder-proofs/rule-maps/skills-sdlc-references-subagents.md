# Rule map — `skills/sdlc/references/subagents.md`

Item: DER-809. Brief: [brief](../brief.md).

Old: `skills/sdlc/references/subagents.md` at chunk base commit 80bfbd5, lines 1–142. New: `skills/sdlc/references/subagents.md` (145 lines).

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–18 | Unchanged rules in this range | kept | 1–18 |
| 19–20 | Two ids per item: builder_id and verifier_id; Review adds reviewer_id; three different agents | changed (R1, R3): two ids, builder_id and reviewer_id; two different agents; route to `proofs.md#builder-checks` | 19–21 |
| 21–24 | Unchanged rules in this range | kept | 22–25 |
| 25 | Item agents table: verifier row (mint clean, never the builder, re-run proving commands) | dropped (R3): re-runs are redundant; the builder runs and re-runs checks at `proofs.md#builder-checks` | — (after new 25) |
| 26–28 | Unchanged rules in this range | kept | 26–28 |
| 29 | One pair per item | kept, and "the pair" is defined as builder and reviewer | 29–30 |
| 30–32 | Unchanged rules in this range | kept | 31–33 |
| 33–42 | Never bullets: builder never the only verifier/reviewer; no transcript to verifier/reviewer; no reuse across items; no new builder/verifier per loop; manager never contrarian/builder/verifier | changed (R3, R2): verifier dropped from each; builder never reviews its own work; reviewer gets the proof bundle, never the transcript | 34–43 |
| 43–68 | Unchanged rules in this range | kept | 44–69 |
| 69–70 | Troubleshooter and contrarian are neither builder, verifier nor reviewer | changed (R3): verifier dropped | 70–71 |
| 71–73 | Unchanged rules in this range | kept | 72–74 |
| 74 | Item grain: mint builder, verifier and reviewer | changed (R3): builder and reviewer | 75 |
| 75–82 | Unchanged rules in this range | kept | 76–83 |
| 83–84 | Tracker writes: builder, verifier and reviewer prompts carry no tracker-writing instructions | changed (R3): verifier dropped; rule kept | 84–85 |
| 85–110 | Unchanged rules in this range | kept | 86–111 |
| 111–114 | Pack list: first builder pack; verifier pack; reviewer pack | changed (R1, R2, R4): builder pack adds `verify-before-done`, the proving commands and a scratch folder; verifier pack dropped; reviewer pack uses the land target and adds the private proof bundle and `docs-google-style` when human docs ship and no style guide is named | 112–117 |
| 115–142 | Unchanged rules in this range | kept | 118–145 |

Protected rows touched: `#tracker-writes` (C9): L83–84 changed under R1/R3 (MQ2).

## Meaning questions

- MQ1 — Resolved: R1/R3: use one builder and a separate reviewer for each item.
- MQ2 — Resolved: R3: retiring a role does not give workers tracker access.
- MQ3 — Resolved: R2: the reviewer receives the bundle, not the builder transcript.
