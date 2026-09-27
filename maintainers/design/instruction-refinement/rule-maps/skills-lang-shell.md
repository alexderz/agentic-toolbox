# Change map — `skills/lang-shell/SKILL.md`

Item: DER-335 (G, light pass).

Old: `skills/lang-shell/SKILL.md` at main 7a11696, lines 1–43.
New: [`skills/lang-shell/SKILL.md`](../../../../skills/lang-shell/SKILL.md).
Light pass: this map lists changed lines only; every other line is
unchanged. 43 lines old, 42 new.

Names: no banned name in old or new. Shell advice, Iron law, Combined
verify, Combined PR checklist and Never: unchanged.
Frontmatter `description`: unchanged (see MQ2).

| Old L | Change | Kind | Reason |
| --- | --- | --- | --- |
| 9–10 | "Compatible with `security-hardening`, `tdd`, `verify-before-done`." removed; "No `scripts/`." kept on L9 | dedupe | Repeats the load-with list; its owner is [`language-router#load-with-list`](../../../../skills/language-router/SKILL.md#load-with-list); the route is new L18 |
| 19 | "`shell-safety` only. Then stop." → one route line (new L18): "`shell-safety` only, then stop, and the skills that load with it:" + links to `language-router#map` and `#load-with-list` | dedupe | One language skill per turn and the `lang-shell` → `shell-safety` pointer row are owned by [`language-router#map`](../../../../skills/language-router/SKILL.md#map); the line names the rule, links the owner and adds no condition |

## Meaning questions

- **MQ1** — Old L21–23 ("Dockerfile `RUN` snippets stay `lang-docker`
  first. Load `shell-safety` only when …") partly restates the
  `language-router` map row for `*.sh` / shebang / agent shell, but the
  Docker `RUN` clause is not in the router. Open: kept as old wording;
  the operator decides whether it becomes part of the route.
- **MQ2** — The frontmatter `description` repeats routing hints (pointer
  to `shell-safety`, `lang-docker` first). It is trigger text and holds
  no link. Open: kept as old wording; the operator decides whether
  descriptions count as copies under standard 5.
- **MQ3** — Old L8 "Load `shell-safety`" and L14 Iron law restate the
  pointer row. Resolved from the text: they are this pointer's whole
  content, and the router says a pointer "routes to the language skill
  in its row" (`language-router#map`); kept.
