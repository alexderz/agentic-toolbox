# Writing standard for agent text

Write, rewrite and review agent text to these rules. Source: DER-288
[HLD](design/instruction-refinement/hld.md) and [LLD](design/instruction-refinement/lld.md).

## Names

- **Agent text** (`$AT`) — `AGENTS.md`, `docs/SDLC.md`, `docs/sdlc/`,
  `docs/INTAKE.md`, `skills/`, `maintainers/AGENTS.md`,
  `maintainers/evals/`.
- **Old** — `main` at 7a11696; **Old L**, a line in it. **SDLC index** — `docs/SDLC.md`.
- **Owner** — the one file that holds a rule. **Route** — one line
  elsewhere that names the rule and links the owner by path and anchor.
- **Rule map** — per edited agent file: each old rule, its disposition,
  its new location. **MQ** — meaning question: an old rule with two
  readings, or a rewording that could change a rule's meaning.

The SDLC index `#names` defines `manager`, `trunk`, `project-main`,
roles and step names. Write the Use name, never the banned one:

| Banned in agent text | Use |
| --- | --- |
| orchestrator; parent agent; parent session; parent-pick; "the parent may / picks / is" | `manager` |
| official copy | `trunk` |
| "Improvise when the work needs it" | "If no listed skill fits the task, do the work without one. Never create a new skill id mid-task." |
| "a person" | "the operator, or someone the operator names in writing" |

## Standard

1. Procedures are numbered steps, one action each. A step for another
   actor starts with that role in bold.
2. Decisions are if/then or a condition → action table. Each condition
   is checkable from files, tracker state, or the operator's written
   words. No "use judgment", "when appropriate", "not too X".
3. One name per thing, defined in one line at first use in its owner
   file. Agent text uses no banned name from Names.
4. No forward references inside a file.
5. One owner per rule. Outside the owner, write at most a route; a route
   adds no condition. Never assemble a rule from several sections; put
   the whole rule in its owner.
6. Routing is one hop. Every agent file is linked from its entry:
   `AGENTS.md`, the SDLC index, or its `SKILL.md`. A routed file needs
   no second hop to finish a rule.
7. Put the most-violated rule first; the Iron law stays first. Every
   "never" names the allowed action beside it.
8. Write imperative sentences, one instruction each. Hide no condition
   in a parenthesis. No metaphor. No self-deleting or dated conditions.
9. Caps in lines: `SKILL.md` ≤250; `tracker-sdlc` ≤150; SDLC index ≤200;
   `docs/sdlc/` files ≤150, except `trunk-changelog-monthly.md` ≤80,
   `branches-and-lands.md` ≤120, `conventions.md` ≤100; root `AGENTS.md`
   ≤100; `docs/INTAKE.md` ≤55; this file ≤150. Caps and K1 apply to
   rewrites, not to the C1 move. Rewrites never grow, except
   `language-router`, `maintainers/AGENTS.md` and new files. If a cap
   needs a dropped rule or a new file, ask the operator.
10. Each item carries a rule map for every agent file it edits. The
    reviewer checks the map, not only the prose.

## Rule owners

| Rule | Owner | Others route |
| --- | --- | --- |
| Roles; names `manager`, `trunk`, `project-main` | `docs/SDLC.md#roles`, `#names` | all |
| Only the manager writes the tracker | `docs/SDLC.md#tracker` | `tracker-sdlc`, `sdlc-artifacts`, `AGENTS.md`, subagents |
| Workers do not bypass security | `docs/SDLC.md#roles` | Build, subagents |
| When to ask the operator; AFK pick between two item fixes | `docs/SDLC.md#asking-the-human` | skills; item Brief |
| Ask message shape | `skills/sdlc-artifacts/templates/ask-human.md` | SDLC, no inline copy |
| Branch source; incoming-item branch; project-main | `docs/sdlc/branches-and-lands.md#branches`, `#project-main` | `AGENTS.md`, Build, item Brief, Groom |
| Serialized lands; land order; `done` after land and verify | `docs/sdlc/branches-and-lands.md#land-path` | `AGENTS.md`, Build, Groom, conventions |
| Gatherer, refiner, designer, contrarian: ids, mint, resume | `docs/sdlc/subagents.md#step-agents` | Brief |
| Builder, verifier, reviewer distinct; mint, resume | `docs/sdlc/subagents.md#item-agents` | Build, Review, `pr-review`, `verify-before-done` |
| Pack vs point; workers | `docs/sdlc/subagents.md#spawn-prompts`, `#workers` | `AGENTS.md` |
| Groom reviewer id | `docs/sdlc/groom-step.md#names` | copy dropped |
| Notify only when landed and verified | `docs/sdlc/build-review.md#definition-of-done` | none; the old L1088 copy moves into the owner |
| Designs in git from onset | `docs/sdlc/conventions.md#designs-in-git` | SDLC index, Repo |
| UX review loop; operator acceptance | `docs/sdlc/plan-trial-spec.md#ux` | Plan, Spec |
| Monthly is not the security gate | `docs/sdlc/trunk-changelog-monthly.md#monthly` | Spec, Review |
| Which skill loads when | root `AGENTS.md` load table | SDLC skill table dropped |
| Language map, load-with list, no-language turns | `skills/language-router/SKILL.md` | `AGENTS.md`, one row |
| Skill inventory | `SOURCES.md` | `AGENTS.md`; SDLC skill table dropped |
| Third-party intake | `docs/INTAKE.md` | `AGENTS.md`, `SOURCES.md` |
| Public-repo voice | root `AGENTS.md#public-repo` | `maintainers/AGENTS.md` |
| `researcher` is not an SDLC role; "no ninth role" → "use only the roles in the table" | root `AGENTS.md` Research row | — |

## Protected rules

Map each row's old text `kept`, or `route` to an owner that keeps it;
any other change is an MQ. The item names its rows; **security** reads it at Review.

| Rule | LLD item | Mechanical check, old vs new |
| --- | --- | --- |
| `security-hardening` Never, Ask first | E5 | `sed -n '/^## Never/,/^## [^N]/p' f \| grep -c '^\| '` equal; same for `## Ask first` |
| `docs/INTAKE.md` checklist | H | six numbered steps under `## Checklist` |
| `tracker-sdlc` claim protocol, Never, Ask first; adapters | D1 | Claim steps 1–5 kept; Never and Ask-first bullet counts equal |
| `skills/tracker-sdlc/adapters/local.md` recipe | D1 | K5 |
| `grok-acp` permission posture, labels, own-item limits | E4 | every map row `kept` |
| Public-repo rule, root `AGENTS.md` | C11 | every map row `kept` |
| SDLC index `#roles`, `#tracker` | C2 | every map row `kept` or `route` to its owner |
| `branches-and-lands.md#never` | C8 | each old L945–961 bullet `kept` here or at its owner |
| `subagents.md#tracker-writes` | C9 | every map row `kept` |

## Rule maps

1. Write one rule map per edited agent file at
   `maintainers/design/instruction-refinement/rule-maps/<slug>.md`. The
   slug is the path lowercased, `/SKILL.md` and `.md` dropped, `/` → `-`.
2. Header: `Old: <path> at main 7a11696, lines a–b. New: <path>.`
3. Key: **kept**, **route**, **dropped** with the owner named, **DER-265**, **DER-271**.
4. Table `Old L | Rule | Disposition | New location`, in old-line order;
   ranges cover every non-blank old line.
5. End with `## Meaning questions`: each `MQ<n>` resolved from the text,
   or by the operator with the date. An open MQ blocks the item.
6. A light pass writes a change map of changed lines only. Light passes cover
   `lang-*`; vendor-derived skills, whose `SOURCES.md` Upstream names a third
   party; and people docs: `README.md`, `CONTRIBUTING.md`, `docs/ARCHITECTURE.md`.

If a rewording could change a role, gate, step, tracker verb, state,
template shape, operator approval or protected rule, or an old rule has
two readings: stop, open an MQ, block the item, ask with `ask-human.md`.

Operator clarifications (2026-09-27), everywhere: the architect fixes
groom-review findings and the groom reviewer re-checks; gate reasons in
parentheses are examples; a review item's verdict says whether a whole
re-check is needed, and the manager files it; the "Improvise" and
"a person" replacements in Names.

## Checks

- **K1 caps** (`wc -l`): the caps in standard 9.
- **K2 never grow**: each edited file ≤ `git show 7a11696:<f> | wc -l`;
  exempt `language-router`, `maintainers/AGENTS.md`, new files.
- **K3 names**: `grep -rniE 'orchestrator|official copy|improvise|parent (agent|session)|parent-pick|the \*{0,2}parent\*{0,2} (may|picks|is)' $AT`
  → empty; other `-w parent` hits: tracker fields, Go tests.
- **K4 maps**: every edited file mapped; no open MQ; protected checks.
- **K5 recipe**: `awk '/^```sh$/{f=1} f{print} f&&/^```$/{f=0}'` on
  `adapters/local.md`, old (`git show 7a11696:…`) vs new → no diff.
- **K6 shapes**: `git diff --quiet 7a11696 -- skills/sdlc-artifacts/templates/tracker-skill.md`;
  per template `grep -oE '^#+ .*|^- \*\*[^*]+\*\*'` unchanged;
  `grep -c '^Contract version: 2$' skills/tracker-sdlc/SKILL.md` = 1.
- **K7 links**: every relative link in changed files resolves; every
  `#anchor` matches a heading slug or `<a id>`; the anchors of the LLD
  [file map](design/instruction-refinement/lld.md#paths--modules-file-and-anchor-map) exist.
- **K8 people doc**: `diff <(git show 7a11696:docs/SDLC.md | sed -n '119,383p' | sed -E 's/^#(#+ )/\1/') docs/how-software-gets-built.md`
  → empty. **K9**: `grep -c 'id="asking-the-human"' docs/SDLC.md` = 1.
- **K10 public text**, before each push and the PR: `git diff main...
  | grep -nE '^\+.*(([0-9]{1,3}\.){3}[0-9]{1,3}|/home/|:[0-9]{4,5}\b|\bsk-[A-Za-z0-9_-]{20,}|\.(lan|local|internal|ts\.net)\b|https?://)'`
  → each hit is an allowed reference (upstream or comparables URL) or is
  removed; same check on PR and tracker text before posting.

Every item: rule maps, the clarifications, one `CHANGELOG.md` line under
`## Unreleased`, K1–K4 and K7. The integrated check runs K1–K10 on the tree.
