# Writing standard for agent text

Write, rewrite and review agent text to these rules. Source: DER-288
[HLD](design/instruction-refinement/hld.md) and [LLD](design/instruction-refinement/lld.md).

## Names

- **Agent text** (`$AT`) — `AGENTS.md`, `skills/` (the SDLC is `skills/sdlc/`), `maintainers/AGENTS.md`, `maintainers/evals/`.
- **Old** — the chunk's base commit: `main` 7a11696 for DER-288, `main` c26f424 for DER-712; **Old L**, a line in it. **SDLC index** — `skills/sdlc/SKILL.md`.
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
9. Caps in lines: `SKILL.md` ≤250, the SDLC index included; files in
   `skills/sdlc/references/` ≤150, except `trunk-changelog-monthly.md` ≤80,
   `branches-and-lands.md` ≤120, `conventions.md` ≤100, `intake.md` ≤55; root
   `AGENTS.md` ≤100; this file ≤150. `tracker-sdlc` has a 150-line target: a goal,
   not a blocker; only its `SKILL.md` cap blocks (Q10). Caps and K1 apply to rewrites,
   not to a move. A rewrite may grow to its cap. Never drop a rule to fit a cap: move
   whole rules to a new file its entry links (standard 6) and log a ruling. Dropping a rule the operator asked for → raise it per `skills/sdlc/SKILL.md#asking-the-human`.
10. Each item carries a rule map for every agent file it edits. The
    reviewer checks the map, not only the prose.

## Rule owners

| Rule | Owner | Others route |
| --- | --- | --- |
| Roles; names `manager`, `trunk`, `project-main` | `skills/sdlc/SKILL.md#roles`, `#names` | all |
| Only the manager writes the tracker | `skills/sdlc/SKILL.md#tracker` | `tracker-sdlc`, `sdlc-artifacts`, `AGENTS.md`, subagents |
| Workers do not bypass security | `skills/sdlc/SKILL.md#roles` | Build, subagents |
| When to ask the operator; rulings; guardrails; auto mode; escalation; touchpoints | `skills/sdlc/SKILL.md#asking-the-human`, `skills/sdlc/SKILL.md#escalation`, `skills/sdlc/SKILL.md#touchpoints` | skills; Brief; Plan; Spec; Build |
| Ask, batch and touchpoint message shape | `skills/sdlc-artifacts/templates/ask-human.md` | SDLC, no inline copy |
| Liaison; asks file; `needs_input` pointer | `skills/sdlc/references/liaison.md`; shape `skills/sdlc-artifacts/templates/asks.md`; pointer `skills/sdlc/references/stage-result.md#schema` | SDLC index, subagents |
| Refiner job; three buckets; defer, don't delete | `skills/discover-the-idea/SKILL.md#refine` | `AGENTS.md`, Brief |
| Branch source; incoming-item branch; project-main | `skills/sdlc/references/branches-and-lands.md#branches`, `#project-main` | `AGENTS.md`, Build, item Brief, Groom |
| Serialized lands; land order; `done` after land and verify | `skills/sdlc/references/branches-and-lands.md#land-path` | `AGENTS.md`, Build, Groom, conventions |
| Gatherer, refiner, designer, contrarian: ids, mint, resume | `skills/sdlc/references/subagents.md#step-agents` | Brief |
| Builder, verifier, reviewer distinct; mint, resume | `skills/sdlc/references/subagents.md#item-agents` | Build, Review, `pr-review`, `verify-before-done` |
| Pack vs point; workers | `skills/sdlc/references/subagents.md#spawn-prompts`, `#workers` | `AGENTS.md` |
| Groom reviewer id | `skills/sdlc/references/groom-step.md#names` | copy dropped |
| Notify only when landed and verified | `skills/sdlc/references/build-review.md#definition-of-done` | none; the old L1088 copy moves into the owner |
| Designs in git from onset | `skills/sdlc/references/conventions.md#designs-in-git` | SDLC index, Repo |
| UX review loop; operator acceptance | `skills/sdlc/references/plan-trial-spec.md#ux` | Plan, Spec |
| Monthly is not the security gate | `skills/sdlc/references/trunk-changelog-monthly.md#monthly` | Spec, Review |
| Which skill loads when | root `AGENTS.md` load table | SDLC skill table dropped |
| Language map, load-with list, no-language turns | `skills/language-router/SKILL.md` | `AGENTS.md`, one row |
| Skill inventory | `SOURCES.md` | `AGENTS.md`; SDLC skill table dropped |
| Third-party intake | `skills/sdlc/references/intake.md` | `AGENTS.md`, `SOURCES.md` |
| Public-repo voice | root `AGENTS.md#public-repo` | `maintainers/AGENTS.md` |
| `researcher` is not an SDLC role; "no ninth role" → "use only the roles in the table" | `skills/sdlc/SKILL.md#roles` | root `AGENTS.md` Research row |

## Protected rules

Map each row's old text `kept`, or `route` to an owner that keeps it;
any other change is an MQ. The item names its rows; **security** reads it at Review.

| Rule | LLD item | Mechanical check, old vs new |
| --- | --- | --- |
| `security-hardening` Never, Ask first | E5 | `sed -n '/^## Never/,/^## [^N]/p' f \| grep -c '^\| '` equal; same for `## Ask first` |
| `skills/sdlc/references/intake.md` checklist | H | six numbered steps under `## Checklist` |
| `tracker-sdlc` claim protocol, Never, Ask first; adapters | D1 | Claim steps 1–5 kept; Never and Ask-first bullet counts equal |
| `skills/tracker-sdlc/adapters/local.md` recipe | D1 | K5 |
| `grok-acp` permission posture, labels, own-item limits | E4 | every map row `kept` |
| Public-repo rule, root `AGENTS.md` | C11 | every map row `kept` |
| SDLC index `#roles`, `#tracker` | C2 | every map row `kept` or `route` to its owner |
| `branches-and-lands.md#never` | C8 | each old L945–961 bullet `kept` here or at its owner |
| `subagents.md#tracker-writes` | C9 | every map row `kept` |

## Rule maps

1. Write one rule map per edited agent file at
   `maintainers/design/<chunk-slug>/rule-maps/<slug>.md`. The
   slug is the path lowercased, `/SKILL.md` and `.md` dropped, `/` → `-`.
2. Header: `Old: <path> at <chunk base commit>, lines a–b. New: <path>.`
3. Key: **kept**, **route**, **dropped** with the owner named, **changed** with the brief, ruling or LLD id that decides it. A Protected rule is never **changed**. DER-288 maps also use **DER-265**, **DER-271**.
4. Table `Old L | Rule | Disposition | New location`, in old-line order;
   ranges cover every non-blank old line.
5. End with `## Meaning questions`: each `MQ<n>` resolved by a cited line of the brief,
   HLD, LLD or a ruling, or by the operator with the date. An open MQ blocks the item.
6. A light pass writes a change map of changed lines only. Light passes cover
   `lang-*`; vendor-derived skills, whose `SOURCES.md` Upstream names a third
   party; and people docs: `README.md`, `CONTRIBUTING.md`, `docs/ARCHITECTURE.md`.

If a rewording could change a role, gate, step, tracker verb, state, template shape, operator
approval or protected rule, or an old rule has two readings: open an MQ. A protected rule → stop the item, keep the
old text, and raise an Always-theirs ask per `skills/sdlc/SKILL.md#asking-the-human`. Otherwise resolve the MQ by step 5, or raise it per the same rules.

Operator clarifications (2026-09-27), everywhere: the architect fixes groom-review
findings and the groom reviewer re-checks; gate reasons in parentheses are examples;
a review item's verdict says whether a whole re-check is needed, and the manager
files it; the "Improvise" and "a person" replacements in Names; frontmatter
`description` fields are metadata, not copies under standard 5 (Q16).

## Checks

- **K1 caps** (`wc -l`) on each file the item rewrote or added; the integrated check uses every file the chunk rewrote or added: the caps in standard 9 block; the target there does not.
- **K2**: retired by DER-712; a rewrite may grow to its standard 9 cap (K1).
- **K3 names**: `grep -rniE 'orchestrator|official copy|improvise|parent (agent|session)|parent-pick|the \*{0,2}parent\*{0,2} (may|picks|is)' $AT`
  → empty, except the `tracker-sdlc` comment shape `(per orchestrator …)`,
  which is contract text (Q9); other `-w parent` hits: tracker fields, Go tests.
- **K4 maps**: every edited file mapped; no open MQ; protected checks.
- **K5 recipe**: `awk '/^```sh$/{f=1} f{print} f&&/^```$/{f=0}'` on
  `adapters/local.md`, old (`git show 7a11696:…`) vs new → no diff.
- **K6 shapes**: `git diff --quiet 7a11696 -- skills/sdlc-artifacts/templates/tracker-skill.md`;
  per template `grep -oE '^#+ .*|^- \*\*[^*]+\*\*'` unchanged, except `ask-human.md` and `asks.md` (DER-712);
  `grep -c '^Contract version: 2$' skills/tracker-sdlc/SKILL.md` = 1.
- **K7 links**: every relative link in changed files resolves; every
  `#anchor` matches a heading slug or `<a id>`; the anchors of the LLD
  [file map](design/ask-less/lld.md#a0-file-map) exist.
- **K8 people doc**: `diff <(git show 7a11696:docs/SDLC.md | sed -n '119,383p' | sed -E 's/^#(#+ )/\1/') <(git show 88455d8:docs/how-software-gets-built.md)` → empty (DER-288 items, through project-main 88455d8);
  each later commit in `git log 88455d8.. -- docs/how-software-gets-built.md` has a change map naming its `docs-google-style` read at Review (operator, 2026-09-27). **K9**: `grep -c 'id="asking-the-human"' skills/sdlc/SKILL.md` = 1.
- **K10 public text**, before each push and the PR: `git diff main...
  | grep -nE '^\+.*(([0-9]{1,3}\.){3}[0-9]{1,3}|/home/|:[0-9]{4,5}\b|\bsk-[A-Za-z0-9_-]{20,}|\bxai-[A-Za-z0-9_-]{20,}|\.(lan|local|internal|ts\.net)\b|https?://)'`
  → each hit is an allowed reference (upstream or comparables URL) or is
  removed; same check on PR and tracker text before posting.

Every item: rule maps, the clarifications, one `CHANGELOG.md` line under
`## Unreleased`, K1–K4 and K7. The integrated check runs K1–K10 on the tree.
