---
name: docs-google-style
description: use this when writing or editing human-facing docs (what this is, how it works, how to use it) or agent-facing comments and module notes — distilled Google developer documentation style. do not use as a product-spec or SDLC process skill.
---

# Docs (Google style)

Distillation of the [Google developer documentation style
guide](https://developers.google.com/style). Project style first, then
this. Clarity beats house style; if you deviate, stay consistent. No
`scripts/`. Not a Google product pack.

**Two audiences**

| Surface | Job |
| --- | --- |
| **Human** (`docs/`, README how-to) | What this is, how it works, how to use it |
| **Agent** (in-code, AGENTS pointers, module maps) | Precise, locatable contracts for future agents |

## Iron laws

- **Must:** US English, `you`, active voice, present tense, sentence-case
  headings, serial commas, condition/goal before instruction.
- **Must:** Code tokens in code font; UI labels in **bold**; placeholders
  `LIKE_THIS`.
- **Must:** Descriptive links. Alt text (or `alt=""`). No meaning by
  color or position alone.
- **Must (API / public comments):** Every public type, member, param,
  return, exception. First sentence unique. Present-tense verb.
- **Never:** Unshipped features. `please` in steps. `simply` / `just` /
  `easy` / `quickly`. `click here`. `e.g.` / `i.e.` `&` for *and*.
- **Never:** Inflect code (`GET`ting, `close`ing). Directional UI
  (`above`, `left-hand`). Skip heading levels. Links in headings. Real
  PII in examples. Images of text or terminal.
- **Never:** `should` when you mean required or optional — use `must` /
  imperative, or `can` / `We recommend`.

## Human docs

Task heading = infinitive (`Create an instance`). Concept = noun phrase.
Condition before action: `To delete the file, click **Delete**.`

Numbered steps, one imperative each. One best path. Introduce lists with
a complete sentence. Point first in the paragraph.

Contractions: `don't`, `isn't`, `can't`. Singular *they*. No
blacklist/whitelist — deny/allow or rewrite. Dates `YYYY-MM-DD` or
`January 19, 2017`.

Commands: only the args for the task; must run after placeholder
replace. Examples: `example.com`, `192.0.2.0/24`, `dana@example.com`.
No `foo`/`bar`/`baz`.

Link text = title or descriptive phrase. `For more information, see
[Title].`

Template: `skills/sdlc-artifacts/templates/human-doc.md`.

## Agent-facing (in-code / AGENTS)

Lead with the contract: name, when to use, inputs, outputs, side
effects, failure modes, where to look next. Locatable name first
(`parseConfig`, `skills/<id>/SKILL.md`). Cross-link; do not restate the
SDLC. No tutorial tone. One idea per comment. Public API comments follow
the API rules above.

## Drop

Google product names, consoles, legal/brand, word-list dump. Don’t copy
the guide entry-by-entry.

## Source

https://developers.google.com/style — distill, not a verbatim paste.
