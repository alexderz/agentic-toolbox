# Change map (light pass) — `skills/statechart/SKILL.md`

Item: DER-774. Vendor-derived skill: SOURCES Upstream names cursor/plugins pstack, so this is a
light-pass change map per `maintainers/writing-standard.md` Rule maps step 6. The file is
**added** (new skill id).

Old: upstream `pstack/skills/statechart/SKILL.md` (82 lines) and `references/render.md`
(93 lines) at 3dbd22ff12742fb28c9700b9760baa29ed41dc13. New:
[`skills/statechart/SKILL.md`](../../../../skills/statechart/SKILL.md).

Key: **kept** (same behavior, new words), **adapted** (changed by a manager ruling, named),
**dropped** (reason), **added** (source).

| Upstream L | Content | Disposition | New location |
| --- | --- | --- | --- |
| 1–5 | Frontmatter; `/statechart` trigger; `disable-model-invocation` | adapted: toolbox `description`; routing is the `AGENTS.md` row (ruling 3) | frontmatter |
| 9 | The reader decides | kept | intro; Names |
| — | Attribution; Names; Iron law (never weaken a rule; "not model-checked" label) | added (ruling 2, ruling 5, writing standard 3 and 7) | L8; Names; Iron law |
| 13 | Scratch folder outside the repo | kept; plus reading a spec a verify skill keeps in the repo | Toolbox policies 2 |
| 14–21 | Run `scripts/statechart` (TypeScript); first run installs TLC and Java with mise, needs the network | adapted (ruling 2, intake step 2): not vendored, not run; named only as an operator opt-in with a link at the pin and those facts; no install command | Toolbox policies 4 |
| — | Run TLC from the repo's own TLA+ tools; adding them follows formal-verification policy 3 | added (ruling 2, ruling 4) | Toolbox policies 1 |
| 25 | Reader rules as INVARIANTs; add a variable; never weaken | kept | Iron law; Write the spec 1 |
| 26 | `Next` as a disjunction of named actions | kept | Write the spec 2 |
| 27 | Deadlock on correct end states; `Done` action | kept; the CLI's `NoDeadlock`/`CHECK_DEADLOCK` naming dropped (CLI-specific) | Write the spec 3 |
| 64 (part) | Small constants or a CONSTRAINT | kept | Write the spec 4 |
| 66 | CLI removes each broken rule and reruns; one worker; 100,000-state bound after the first break; "Rules not checked" | adapted: the same loop done by hand with TLC (remove the rule, rerun); the state bound dropped (CLI-specific), replaced by "a run that does not finish lists its rules as not checked" | Run TLC 1–6 |
| — | Use TLC traces and the `-dump dot` state graph as input | added (ruling 2) | Run TLC 1, 5 |
| 65, 67 | VIEW/SYMMETRY merges; CONSTRAINT and ACTION_CONSTRAINT limits | kept, compressed; the ACTION_CONSTRAINT step-drawing detail dropped (CLI output behavior) | Run TLC limits |
| 68 | `tlc.out` / `tlc-RULE.out`; the UseParallelGC warning detail | kept the file names; warning detail dropped (CLI output behavior) | Run TLC 1–2 |
| 31–41 | View module `state()`: flat, parents, regions; reader labels; no variable names | adapted: a hand-written mapping table; same three forms as Mermaid flat, composite and `--` regions | Map states and steps 1–2 |
| 43 | `step()` labels in the reader's words; shared labels share an arrow | kept as a table | Map states and steps 3 |
| 45 | Bracketed conditions; regions rule; name a hidden deciding value | kept | Map states and steps 4–5 |
| 47–51 | `group`, `colors`, `title` exports | adapted: phase `classDef`s and a Mermaid front-matter title | Draw the chart 7–8 |
| 53 | Functions depend only on their arguments | kept: a label depends only on the model state | Map states and steps 1 |
| 55 | A step inside one label draws no arrow; split the label | kept | Map states and steps 6 |
| 57–60 | ~20 arrows; coarsen before hiding; keep bug-path states and marks; breaks→mayBreak; never merge different rules; four hiding rules; say what is hidden | kept | Draw the chart 2–4; Report 3 |
| 64 | `breaks`/`mayBreak` classes; Legend; two rules on one mark | kept; Legend example with `classDef` lines (colors from render.md) | Draw the chart 5–6; Report 2 |
| 64 (regions) | Region-combination marking rule | dropped: it describes the CLI's computation; by hand, each chart state is marked from its own model states | — |
| 74 | Show `chart.mmd` as a `mermaid` block; 500-state budget; bug paths only above it; no chart when none break | kept | Draw the chart 1; Report 6 |
| 76 | Render with Pele; follow render.md | dropped (ruling 2): plain Mermaid text is the deliverable; rendering optional | intro |
| render.md 1–93 | Pele install, API options, CSS theme | dropped (ruling 2; intake: no install); only the two mark colors kept in the `classDef` example | Draw the chart 6 |
| 80 | Hand-off: chart, one line per bug, what the model leaves out, regenerate command | kept; regenerate with TLC commands | Report 1–6 |
| 82 | Replay each bug path against the real code; model wrong until shown otherwise | kept | Report 5 |
| — | Designer use: user flow from approved stories; "not model-checked" without a TLC run | added (ruling 2, from the post) | Chart a user flow 1–7 |

Guardrails added beyond ruling 4: none.

## Meaning questions

None open. The opt-in line ("only when the operator says so in writing") restates ruling 2's
"operator opt-in"; it adds no ask: agents do not raise it, the operator may.
