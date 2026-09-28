# Change map — `skills/ui-craft/SKILL.md`

## DER-352: option 3, neither

Item: DER-352 (vendor-derived light pass: `SOURCES.md` Upstream names
Impeccable). Old: `skills/ui-craft/SKILL.md` at project-main 63f6b72,
lines 1–249. New: [`skills/ui-craft/SKILL.md`](../../../../skills/ui-craft/SKILL.md),
lines 1–250 (cap 250). Changed lines only; every other line is unchanged.
Disposition: **kept** (same rule, new wording or place), **new**,
**dropped** (duplicate, owner named).

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 3 | Description: when to load, when not to | **kept**; **new** clause: do not load it when the product repo's `## UI craft` records option 3, neither. Frontmatter is metadata (Q16) | L3 |
| — | Stop line: read the product repo's root `AGENTS.md`; if the UI craft note records option 2 or 3, stop reading unless the operator reopens the choice in writing | **new** for option 3; for option 2 it is old L93–95, moved up so it is read before the rules. It opens Which version, directly after the Iron law (standard 7: the Iron law stays first) | L25–31 |
| 25–27 | UI craft note: the `## UI craft` section of the product repo's root `AGENTS.md`, recording the option and the date; one pick per product repo | **kept**; the definition moves to its first use, the stop line (standard 3, 4). The heading keeps "once per product repo" | L25–26, L33 |
| — | Option 3, neither: no UI craft in this repo, not this file and not upstream; `ux-design` and the SDLC gates still apply | **new**; source: DER-352. The intake note planned it as one more list item | L39–40 |
| 36–37 | Ask step 1: a note exists → follow it, do not ask again | **kept**; adds "unless the operator reopens the choice in writing". Reading `AGENTS.md` is now the stop line's step | L44–45 |
| 38–42 | Ask step 2: the ask shape, one choice per option, option 1 recommended | **kept**; reflowed from 5 lines to 4, same words | L46–49 |
| 92–93 | Never do any option 2 step on your own initiative; without an explicit yes, use option 1 | **dropped**; owner: Never "Any option 2 step without the operator's explicit yes. Use option 1." | L241 |
| 93–95 | Note records option 2 → this file's rules do not apply; SDLC gates still apply whatever upstream says | **kept**, moved into the stop line | L27–30 |
| 234 | Ask first: option 2, through the ask, once per product repo | **dropped**; owner: The ask (L42–51) and Never L241 | — |
| 241 | Never: run, install or open upstream in an agent harness; read it as text | **kept** at L242; also stated in the stop line, "With upstream in use, never run, install or open its clone in an agent harness; read it as text", because an option 2 reader stops before Never (Review: security, reviewer) | L30–31, L242 |

## Meaning questions

Resolved from the text:

- **MQ1** (old L92–95, L234): the option 2 guard loses two copies. Never
  L241 keeps "no option 2 step without the operator's explicit yes; use
  option 1", and The ask step 3 keeps "only after the operator answers";
  same meaning. **security** reads this diff at Review.
- **MQ2** (stop line vs ask step 1): a note of option 2 or 3 stops the
  reader before The ask; the reopen clause sits in both places, so an
  operator's written reopen still reaches the ask.
- **MQ3** (option 3 scope): "no UI craft" covers this file and upstream
  only; the option text keeps `ux-design` and the SDLC gates.
- **MQ4** (Review fix): in an option 2 repo the stop line ends reading
  before Never, so the stop line carries the harness rule itself. Same
  rule as Never L242; the stop line adds no condition.

K1: 250 lines. K3: no hits. K7: links unchanged; the new anchor
`#which-version-ask-once-per-product-repo` used by `AGENTS.md` and
`README.md` matches the heading. K10: no added hits.
