# DER-290 intake note: `ui-craft` from Impeccable

Design record for the intake of `skills/ui-craft/`. The **security** read
is [security-intake.md](security-intake.md), copied as written.

- **Upstream:** pbakaus/impeccable, `skill/` at
  `9d715cc4f5564a990ca8345abfdd5df6dc9b41c8`, Apache-2.0. Skill v4.4.0,
  engine v0.1.6.
- **Where this note lives:** pr-lens (DER-274) has no intake note in the
  repo; its record is the `SOURCES.md` row and its rule map. This
  directory follows `maintainers/design/<topic>/`.
- **Order (INTAKE step 4):** the `SOURCES.md` row was written first,
  with the full SHA, before the body.
- **Scanner (INTAKE step 3):** waived by the operator, 2026-09-27, for
  option 1. Scanner work is DER-273, pending. The manual **security**
  read above stands in for it.

## Operator decisions, 2026-09-27

1. Skill id `ui-craft`, crediting Impeccable (Apache-2.0).
2. Two options, asked once per product repo in the `ask-human.md` shape,
   option 1 recommended; the answer goes in that repo's `AGENTS.md`
   under `## UI craft`.
3. Option 1, the default: the topic-only rewrite in this repo.
4. Option 2: upstream at the user's own risk. A link at the pin and the
   `security-intake.md` §5 disclosure; no install command we endorse. The
   agent checks out upstream only after the operator's explicit yes,
   outside any path an agent harness loads, and records it in the
   product repo's `AGENTS.md`.

## How the body was written

1. Upstream was cloned into a scratch directory. Only `skill/SKILL.src.md`,
   `skill/reference/`, `skill/agents/` and `NOTICE.md` were extracted with
   `git archive` and read as plain text. Nothing ran; the clone was never
   opened as an agent workspace (condition 6) and was deleted afterwards.
2. Topics only, from the §4 allowed list: anti-patterns (`craft-floor`,
   `quieter`), typography (`typeset`), color (`colorize`, `new-work`
   color strategy), layout (`layout`), motion (`animate`), UI states
   (`harden`, `polish`, `onboard`, `clarify`), "the brief wins" and
   refinement versus redesign (`SKILL.src.md`), one verification pass.
3. Left out: everything on the §4 leave-out list. No `ios.md` or
   `android.md` content, so no ehmo MIT attribution is needed.
4. **Shared-run check:** longest run of consecutive words shared with the
   upstream Markdown at the pin, words as lowercase `[a-z0-9]+` tokens.
   Threshold: 12. Result: 10, in `SKILL.md`, the list of hook file names
   in the option 2 disclosure (taken from `security-intake.md` §5).

## Choices the builder made

- **Load rule:** the skill loads on UI build turns; only the upstream
  option is operator opt-in (brief risk 1).
- **Who asks:** the builder puts the ask in its handoff and keeps building
  with option 1, the default, which runs nothing (brief risk 2). Only
  after the operator answers does the manager write the product repo's
  UI craft note (Review round 1). The options are a numbered list, so a
  third answer ("neither") can be added as one more item.
- **Neither (DER-352):** option 3 added as that item. The note records it
  like the other answers; a stop line after the Iron law ends reading when
  the note records option 2 or 3, and carries the never-open-upstream rule
  for option 2 repos. `AGENTS.md` and `README.md` route to the
  ask and no longer list the options. `language-router` is unchanged.
- **`language-router`:** `ui-craft` joins load-with item 1. That list
  names the process skills that may load beside the one language skill;
  a UI build is a code turn with `lang-web-markup` or `lang-js-ts`, so
  without the entry the skill could not load there.
- **License:** `skills/ui-craft/LICENSE` and a `NOTICE` entry, following
  `debug-anthropic`. Upstream `NOTICE.md` covers only `ios.md` and
  `android.md`, which are not used, so nothing carries over.
