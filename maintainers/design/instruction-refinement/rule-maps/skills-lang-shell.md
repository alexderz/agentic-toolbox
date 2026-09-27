# Change map — `skills/lang-shell/SKILL.md`

Item: DER-335 (G, light pass).

Old: `skills/lang-shell/SKILL.md` at main 7a11696, lines 1–43.
New: [`skills/lang-shell/SKILL.md`](../../../../skills/lang-shell/SKILL.md).
Light pass: this map lists changed lines only; every other line is
unchanged. 43 lines old, 42 new.

Names: no banned name in old or new. Shell advice, Iron law, Load
(including old L19 "`shell-safety` only. Then stop."), Combined verify,
Combined PR checklist and Never: unchanged.
Frontmatter `description`: unchanged (see MQ2).

| Old L | Change | Kind | Reason |
| --- | --- | --- | --- |
| 8–10 | "Compatible with `security-hardening`, `tdd`, `verify-before-done`." → the route line "Process skills that **may** load with this one: [load-with list](…#load-with-list)." (new L9); the rest of old L8–10 rewrapped onto new L8, same words | dedupe | Repeats the load-with list; its owner is [`language-router#load-with-list`](../../../../skills/language-router/SKILL.md#load-with-list); the route adds no condition |

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
- **MQ3** — Old L8 "Load `shell-safety`", L14 Iron law and L19
  "`shell-safety` only. Then stop." restate the one-language-skill rule
  ([`language-router#iron-law`](../../../../skills/language-router/SKILL.md#iron-law))
  and the pointer row (`#map`). Resolved from the text: they are this
  pointer's own content, and the router says a pointer "routes to the
  language skill in its row"; kept.
- **MQ4** — Old L9–10 named three process skills; the owner's load-with
  list names nine. Resolved from the text: the owner holds the rule
  (standard 5, writing-standard `#rule-owners` "Language map, load-with
  list"), so the route follows the owner's list, and "**may**" keeps
  each one optional.
