# Change map — `skills/shell-safety/SKILL.md`

Item: DER-325 (F, light pass).

Old: `skills/shell-safety/SKILL.md` at main 7a11696, lines 1–91.
New: [`skills/shell-safety/SKILL.md`](../../../../skills/shell-safety/SKILL.md).
Light pass: this map lists changed lines only; every other line is
unchanged. 91 lines old, 91 new.

Always, Ask first and Never rows: unchanged, same count and text.
Upstream pin section: unchanged. No new upstream text; no upstream fetch.
`SOURCES.md`: the `shell-safety` Notes cell gains the LLD note; SHA,
license and upstream cells unchanged.

| Old L | Change | Kind | Reason |
| --- | --- | --- | --- |
| 72 | "at LLD/PR" → "at LLD and Review" | real defect | SDLC lands have no internal PRs; the SDLC index `#roles` names the **security** gates as Spec and Review |
| 73 | "shellcheck" → "ShellCheck" | naming | One name per thing; L33 and L77 write "ShellCheck" |
| 77 | "Workers do not bypass." → "Workers do not bypass **security**", plus a link to `docs/SDLC.md#roles` | dedupe | The rule's owner is `docs/SDLC.md#roles`; this line becomes a route to it and adds no condition |

## Meaning questions

- **MQ1** — Old L72 "PR" could read as an internal land PR or an
  outside-worker PR. Resolved from the text: both reach **security** at
  the Review step (`docs/SDLC.md#roles`: gates at Spec and Review), so
  "Review" covers both readings.
