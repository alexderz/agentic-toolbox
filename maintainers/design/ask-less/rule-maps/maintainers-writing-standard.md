# Rule map — `maintainers/writing-standard.md`

Item: DER-740 (A8 of DER-712).

Old: `maintainers/writing-standard.md` at main c26f424, lines 1–150.
New: [`maintainers/writing-standard.md`](../../../writing-standard.md).
Disposition: **kept** (same rule, same place or A0 path only), **route**
(the rule lives in its owner; this file links it), **dropped** (duplicate
or retired, owner named), **DER-265**, **DER-271**. "Old L" is a line at
main c26f424. A0 rewrote paths only; those rows stay **kept**.

`CHANGELOG.md` carries the one A8 line under `## Unreleased` and is not
agent text, so it has no map. Protected rows touched: none.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1 | Title | kept | L1 |
| 3–4 | Source: DER-288 HLD and LLD | kept | L3–4 |
| 6 | Names heading | kept | L6 |
| 8–9 | Agent text (`$AT`) paths | replaced (A8 edit 1): one line, `skills/` with the SDLC at `skills/sdlc/`. A0 had already moved the docs paths into `skills/`; those paths sit inside `skills/` | L8 |
| 10 | Old, Old L, and the SDLC index name | kept; path only (A0): `docs/SDLC.md` → `skills/sdlc/SKILL.md` | L9 |
| 11–12 | Owner and route | kept | L10–11 |
| 13–15 | Rule map and MQ | kept | L12–14 |
| 17–18 | Use the Names table; never a banned name | kept | L16–17 |
| 20–21 | Banned-name table header | kept | L19–20 |
| 22 | orchestrator and parent → `manager` | kept | L21 |
| 23 | official copy → `trunk` | kept | L22 |
| 24 | Improvise replacement | kept | L23 |
| 25 | "a person" replacement | kept | L24 |
| 27 | Standard heading | kept | L26 |
| 29–30 | Standard 1: numbered steps | kept | L28–29 |
| 31–33 | Standard 2: checkable decisions | kept | L30–32 |
| 34–35 | Standard 3: one name | kept | L33–34 |
| 36 | Standard 4: no forward references | kept | L35 |
| 37–39 | Standard 5: one owner | kept | L36–38 |
| 40–42 | Standard 6: one hop | kept | L39–41 |
| 43–44 | Standard 7: most-violated rule first | kept | L42–43 |
| 45–46 | Standard 8: imperative sentences | kept | L44–45 |
| 47–53 | Standard 9: caps and growth | replaced (A8 edit 2, R45, R48): the SDLC index uses the `SKILL.md` cap of 250; a rewrite may grow to its cap; a new file is added and a ruling logged; dropping an operator-asked rule asks them; "the C1 move" becomes "a move". A0 had rewritten directory paths only | L46–52 |
| 54–55 | Standard 10: one map per edited agent file | kept | L53–54 |
| 57 | Rule owners heading | kept | L56 |
| 59–60 | Owner table header | kept | L58–59 |
| 61 | Roles; names `manager`, `trunk`, `project-main` | kept; path only (A0) | L60 |
| 62 | Only the manager writes the tracker | kept; path only (A0) | L61 |
| 63 | Workers do not bypass security | kept; path only (A0) | L62 |
| 64 | When to ask the operator; AFK pick between two item fixes | replaced (A8 edit 3). The AFK pick is **dropped** (T2); its owner is `skills/sdlc/SKILL.md` Auto mode and item Brief step 4 (A1). The row now names rulings, guardrails, auto mode, escalation and touchpoints, at `#asking-the-human`, `#escalation`, `#touchpoints` | L63 |
| 65 | Ask message shape | replaced (A8 edit 4): ask, batch and touchpoint message shape; same owner | L64 |
| — | Liaison; asks file; `needs_input` pointer | new (A8 edit 5); owner `skills/sdlc/references/liaison.md`, shape `templates/asks.md`, pointer `references/stage-result.md#schema` | L65 |
| — | Refiner job; three buckets; defer, don't delete | new (A8 edit 5); owner `skills/discover-the-idea/SKILL.md#refine` | L66 |
| 66 | Branch source; incoming-item branch; project-main | kept; path only (A0) | L67 |
| 67 | Serialized lands; land order; `done` after land and verify | kept; path only (A0) | L68 |
| 68 | Gatherer, refiner, designer, contrarian | kept; path only (A0) | L69 |
| 69 | Builder, verifier, reviewer distinct | kept; path only (A0) | L70 |
| 70 | Pack vs point; workers | kept; path only (A0) | L71 |
| 71 | Groom reviewer id | kept; path only (A0) | L72 |
| 72 | Notify only when landed and verified | kept; path only (A0) | L73 |
| 73 | Designs in git from onset | kept; path only (A0) | L74 |
| 74 | UX review loop; operator acceptance | kept; path only (A0) | L75 |
| 75 | Monthly is not the security gate | kept; path only (A0) | L76 |
| 76 | Which skill loads when | kept | L77 |
| 77 | Language map, load-with list, no-language turns | kept | L78 |
| 78 | Skill inventory | kept | L79 |
| 79 | Third-party intake | kept; path only (A0) | L80 |
| 80 | Public-repo voice | kept | L81 |
| 81 | `researcher` is not an SDLC role | kept; path only (A0) | L82 |
| 83 | Protected rules heading | kept | L84 |
| 85–86 | Map each row `kept` or `route`; any other change is an MQ | kept | L86–87 |
| 88–89 | Protected-rules table header | kept | L89–90 |
| 90 | `security-hardening` Never, Ask first | kept | L91 |
| 91 | Intake checklist | kept; path only (A0) | L92 |
| 92 | `tracker-sdlc` claim protocol, Never, Ask first | kept | L93 |
| 93 | `adapters/local.md` recipe | kept | L94 |
| 94 | `grok-acp` permission posture | kept | L95 |
| 95 | Public-repo rule | kept | L96 |
| 96 | SDLC index `#roles`, `#tracker` | kept | L97 |
| 97 | `branches-and-lands.md#never` | kept | L98 |
| 98 | `subagents.md#tracker-writes` | kept | L99 |
| 100 | Rule maps heading | kept | L101 |
| 102 | One rule map per edited agent file | kept | L103 |
| 103 | Rule-map directory | replaced (A8 edit 6, R44): `maintainers/design/<chunk-slug>/rule-maps/<slug>.md` | L104 |
| 104 | Slug shape | kept | L105 |
| 105 | Header names the base commit | replaced (A8 edit 7, R44): `<chunk base commit>` in place of `main 7a11696` | L106 |
| 106 | Disposition key | kept | L107 |
| 107–108 | Table covers every non-blank old line | kept | L108–109 |
| 109–110 | Meaning questions; an open MQ blocks the item | kept | L110–111 |
| 111–113 | Light pass writes a change map of changed lines only | kept | L112–114 |
| 115–117 | Stop and open an MQ when a rewording could change a rule | kept | L116–118 |
| 119–123 | Operator clarifications (2026-09-27) | kept | L120–124 |
| 125 | Checks heading | kept | L126 |
| 127 | K1 caps | kept | L128 |
| 128–129 | K2 never grow | **dropped** as its own check (R64). A rewrite may grow to its standard 9 cap; K1 checks that cap | L129 |
| 130–132 | K3 names | kept | L130–132 |
| 133 | K4 maps | kept | L133 |
| 134–135 | K5 recipe | kept | L134–135 |
| 136 | K6: tracker-skill template quiet against 7a11696 | kept | L136 |
| 137 | K6: per-template heading and label grep | replaced (A8 edit 9, R92): unchanged, except `ask-human.md` and `asks.md` | L137 |
| 138 | K6: contract version 2 | kept | L138 |
| 139–140 | K7: links and anchors resolve | kept | L139–140 |
| 141 | K7: LLD file-map anchors exist | kept; path only (A0): the link target is `design/ask-less/lld.md#a0-file-map` | L141 |
| 142 | K8 people doc, through project-main 88455d8 | kept | L142 |
| 143 | K8 later commits, and K9 | kept; path only (A0): K9 reads `skills/sdlc/SKILL.md` | L143 |
| 144 | K10: when the public-text check runs | kept | L144 |
| 145 | K10 grep pattern | replaced (A8 edit 10, R87): the `xai-` alternative `\bxai-[A-Za-z0-9_-]{20,}` inserted directly after the `sk-` alternative. No other change | L145 |
| 146–147 | K10: each hit is an allowed reference or is removed | kept | L146–147 |
| 149–150 | Every item runs rule maps, one changelog line, K1–K4 and K7 | kept | L149–150 |

## Meaning questions

None open. A8 edits 1–10 are the accepted LLD's exact text. R44, R45,
R48, R64, R87 and R92 already settled the rule-map path, growth to the
caps, the 250-line index cap, K2's retirement, the `xai-` pattern and
the K6 exemption (2026-11-11). No old line in this item has two readings.
