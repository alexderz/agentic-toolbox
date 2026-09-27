# Rule map — `skills/modern-python/SKILL.md`

Item: DER-317 (E6).

Old: `skills/modern-python/SKILL.md` at main 7a11696, lines 1–182.
New: [`skills/modern-python/SKILL.md`](../../../../skills/modern-python/SKILL.md).
Disposition: **kept** (same rule, this file), **route** (the rule lives in
its owner; this file links it), **dropped** (duplicate, owner named),
**DER-265**, **DER-271**. "Old L" = line in the old file; "L" = line in
the new file.

Protected rows touched: none. Operator clarifications (2026-09-27): none
of their subjects occur in this file.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–4 | Frontmatter: name, description | kept verbatim | L1–4 |
| 6 | Title | kept | L6 |
| 8–10 | First-party, MIT, id, SKILL.md only, no `scripts/`, not a vendor paste, tool-fact sources | kept, rewrapped to two lines | L8–9 |
| 12–13 | Compatible with `tdd`, `verify-before-done`, `pr-review`, `security-hardening`; optional pointer `lang-python` | route (owner: `skills/language-router/SKILL.md#family-rules` load-with list; `#map` Python row `lang-python` → `modern-python`); one route line, no condition added | L11 |
| 15 | Heading "Iron law" | kept, still first | L13 |
| 17–18 | `uv add` / `uv remove` change deps; `uv run` runs tools; do not activate a venv or hand-edit dependency lists | kept verbatim | L15–16 |
| 20 | New work: Python 3.12+, uv, ruff, ty, pytest | kept; fragment → imperative "On new work, use …" | L18 |
| 21 | Keep pip / Poetry / mypy / black only when the operator says so | kept verbatim | L19 |
| 23–34 | Always table (8 rows) | kept verbatim | L21–32 |
| 36–45 | Ask first table (6 rows) | kept verbatim | L34–43 |
| 47 | Heading "Never" | kept | L45 |
| 49–50 | Never table header | kept; column "Instead" added so each never names the allowed action (standard 7) | L47–48 |
| 51 | Never marketplace `npx skills add` / plugin install; link INTAKE.md | kept; Instead "Follow INTAKE.md" (link moved there); Why "Intake owns third-party skills" (MQ1) | L49 |
| 52 | Never `scripts/` in this skill dir; intake quarantine | kept; Instead "Keep this skill `SKILL.md` only", from old L8 | L50 |
| 53 | Never hand-edit `pyproject.toml` deps; `uv add` / `uv remove` | kept; the old Why cell was the allowed action, now under Instead; Why "`uv.lock` is the install truth", from old L27 | L51 |
| 54 | Never secrets in `pyproject.toml`, scripts, lockfiles; history is forever | kept; Instead "Leave them out; see `security-hardening` `#never`" (MQ2) | L52 |
| 55 | Never live network in tests unless marked; tests stay offline | kept; Instead "Mark each test that needs the network", from "unless marked" | L53 |
| 57–63 | Decision table, first three rows | kept; "PEP 723 (below)" → "PEP 723 script", no forward reference (standard 4) | L55–61 |
| 64 | Existing tree → Migration, Ask first if it already ships | kept; → "Migrate; if it already ships, Ask first": a verb, not a forward section reference (standard 4); same condition | L62 |
| 66–75 | Tools table; scanners and CI hooks are tester / security | kept verbatim | L64–73 |
| 77–98 | New project and package command blocks | kept verbatim | L75–96 |
| 100–101 | `uv add` owns dependencies and dev group; do not type packages into `pyproject.toml` by hand | kept; "Do not" → "Never", allowed action "run `uv add`" beside it (standard 7) | L98–99 |
| 103–123 | PEP 723 script example and commands | kept verbatim | L101–121 |
| 125 | No lockfile; multi-file → `pyproject.toml` | kept; "Multi-file? Use" → if/then "If the code spans more than one file, use" | L123 |
| 125–126 | `uv run --with pkg` is a one-off probe, not a project dep | kept; → "Use … only as a one-off probe; add project deps with `uv add`" (allowed action from old L27, L53) | L124 |
| 128 | Heading "Migration (only when asked)" | kept; the condition leaves the parenthesis (standard 8) as "Migrate only when asked." (MQ3) | L126, L128 |
| 130–135 | Migration table | kept verbatim | L130–135 |
| 137 | Odd markers or VCS deps: stop and do them by hand | kept; → if/then, "odd" kept (MQ4) | L137 |
| 137–138 | Do not import a lock you have not read | kept; "Do not" → "Never", allowed action "read it first" | L138 |
| 140–159 | uv (short) table; Verify block | kept verbatim | L140–159 |
| 161–168 | Roles table | kept verbatim | L161–168 |
| 170–178 | Red flags; stop, use uv, or Ask first | kept verbatim | L170–178 |
| 180–182 | License | kept verbatim | L180–182 |

## Meaning questions

- **MQ1** — Old L51 had only a link in the Why cell. Resolved from the
  text: the link moves to Instead ("Follow INTAKE.md"); the Why states
  what the link says (intake owns third-party skills). No new condition.
- **MQ2** — Old L54 names no allowed action for secrets. Resolved from
  the text: "Leave them out" restates the never; the route names the
  owner of the secrets rule (`security-hardening` `## Never`, "Secrets in
  git"). No new condition, no new gate.
- **MQ3** — Old L128 "only when asked" does not name who asks. Resolved
  from the text: the sentence keeps "asked" verbatim, so no reading is
  chosen.
- **MQ4** — Old L137 "Odd markers" is not a checkable condition
  (standard 2); "odd" could mean any environment marker or only unusual
  ones. Resolved from the text: the word stays verbatim, so no reading is
  chosen; only the sentence shape changed to if/then.
