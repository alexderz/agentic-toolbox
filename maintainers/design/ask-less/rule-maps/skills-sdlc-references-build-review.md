# Rule map — `build-review.md` (Review)

Old: `docs/sdlc/build-review.md` at main c26f424, lines 98–100. New: `skills/sdlc/references/build-review.md`.
Item: DER-736 (G5, A4 of DER-712). Changed lines only: Review step 4. G6 maps its own Build edits.
Text: [opus-rebuild.md G5](../opus-rebuild.md#g5--yagni-subagents-pack-review-a4).

Key: **kept**, **route**, **dropped** with the owner named, **changed** with the brief, ruling or
LLD id that decides it.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| — | GR16: the reviewer fails a diff that touches `brief.md`, adds a non-open or answered asks-file section, changes or removes an existing `Status`, `Answer`, `Choices` or `Recommendation`, or touches `## Autonomy` without a manager `comment`; skips only a `Record asks` commit whose SHA a manager `comment` names | **changed** (GR16, R114, R141, R142, R185): new step 4, run first | Review step 4 |
| 98–100 | Reviewer approves only if the item meets the ticket and the LLD and passes the security gate | **changed** (R67, R141): step 5; loads `pr-review` and `yagni`; also needs step 4 to fail nothing and no speculative generality (the `yagni` Iron law and Decide and log) | Review step 5 |

## Meaning questions

None.
