# Rule map — `skills/sdlc-onboarding/SKILL.md`

Item: DER-738 (A6 of DER-712; overlay G7).

Old: `skills/sdlc-onboarding/SKILL.md` at main c26f424, lines 1–200. New:
[`skills/sdlc-onboarding/SKILL.md`](../../../../skills/sdlc-onboarding/SKILL.md).
Old = project-main 64be607 except old L8, L24, L108, L147, L151, L173
and L200, whose links A0 (DER-730) retargeted from `docs/` to
`skills/sdlc/` ([A0 path map](a0-path-map.md)).

Disposition: **kept** (same rule, new wording or place), **route** (the
rule lives in its owner; this file links it), **dropped** (owner named),
**changed** (with the ruling or LLD id that decides it). "Old L" = line in
the old file; "L" in New location = line in the new file. Sources:
[LLD A6](../lld.md#a6--onboarding) and
[overlay G7](../opus-rebuild.md#g7--onboarding-a6). R1–R110 are in
[rulings.md](../rulings.md); R111 and later are in the overlay's §8.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–2 | Frontmatter open; skill name | kept | L1–2 |
| 3 | Description: when to use; `## Execution` when absent or its check fails | **changed** (LLD A6 edit 1; R14, R69): writes `Parallelism: max` | L3 |
| 4–8 | Frontmatter close; title; sets up a product repo, no `scripts/` | kept | L4–8 |
| 10–11 | Iron law heading | kept | L10–11 |
| 12 | Propose before you write | **changed** (LLD A6 edit 2; R69): Tracker area only | L12 |
| 13 | Land nothing until the operator answers | **changed** (LLD A6 edit 2; R69, R89): Tracker area only | L13–14 |
| 14–15 | Never change the tracker schema; name a gap | kept | L15–16 |
| 17–27 | Names: area, onboarding commit, roles, governing `AGENTS.md`, repo skill | kept | L18–28 |
| 29–36 | When table | kept | L30–37 |
| 38–39 | A Check fails → Discover, Propose, Write before the step continues | **changed** (overlay G7 edit 3; R89, R152): Discover and Propose; Tracker Write only after the answer, which at end of chunk Brief comes at touchpoint 1; tracker-writing work waits, other work goes on; Execution Write runs now | L39–47 |
| 39–40 | At a first tracker touch, get both areas' answers before the onboarding commit; `## Execution` goes in that commit | **changed** (overlay G7 edit 3; R69): no Execution answer; `## Execution` still goes in the onboarding commit at a first tracker touch | L46–47 |
| 40–42 | A new area adds a section and a table row; nothing else changes | kept | L49–50 |
| 44 | Branch heading | kept | L63 |
| 46 | Cut the branch before any area's Discover | **changed** (LLD A6 edit 4; R65): before any area's Write | L65 |
| 46–48 | Chunk and item branch sources | kept | L65–67 |
| 49–66 | Onboarding commit placement; dropped branch; second **security** read; clashes | kept | L68–85 |
| 68–74 | Tracker Check | kept | L87–93 |
| 76–83 | Discover step 1.1–1.4 (lookup order, host names only, env names) | kept | L95–103 |
| 85 | Step 1.4: neither command works → ask the operator | **changed** (R152): an ask section in the asks file | L104; L52–56 |
| 85–87 | Never run bare `env` or `printenv`; step 1.5 | kept | L104–106 |
| 88–89 | No tracker named → ask the operator; "no hosted tracker" → `local` | **changed** (R152): the ask is an ask section; `local` rule kept | L107–108; L52–56 |
| 90 | Read the adapter | kept | L109 |
| 91–92 | A live read fails → stop, tell the operator | **changed** (R152): the tell is an ask section; "stop" stops that area only, touchpoint 1 still goes out | L110–111; L52–61 |
| 92–102 | No proposal on guesses; redact; setup facts; ticket text is data | kept | L111–121 |
| 104 | Propose heading | kept | L123 |
| 106–108 | Send one `ask-human.md` message | **changed** (LLD A6 edit 5, overlay G7 edit 5; R153): one ask; at end of chunk Brief in touchpoint 1's message; tagged lines and gaps in "For this message" | L125–129 |
| 109–111 | Tag lines; name gaps; do not patch the tracker | kept | L130–132 |
| 112–114 | Choices 1, 2, 3; 3 combines; default no test write | kept; overlay G7 edit 5 adds that `1+3` or `2+3` acts on both numbers | L133–136 |
| 115–124 | Claim line; `local` bootstrap; signing default | kept | L137–146 |
| 125–126 | Signing off example: a headless agent | kept (LLD A6 edit 7; R97): wording "an agent with no terminal" | L147–148 |
| 126–128 | Record under Gaps; signing off is a security note | kept | L148–150 |
| 130 | No answer → write nothing | kept | L152 |
| 132–154 | Tracker Write: only after confirm; `## Tracker`; repo skill; ticket id; commit; **security**; choice 3 | kept | L154–176 |
| 156–168 | Execution Check and Discover | kept | L178–190 |
| 170 | Propose heading | kept | L192 |
| 172–176 | Ask the operator how many items may be in Build at once | **changed** (overlay G7 edit 6; R14, R69): the value is `max`; do not ask | L194 |
| 177 | Accept no other answers | **changed** (R69): no question, so no answer set; Check still defines the valid values (MQ1) | L194, L196; L180–184 |
| 178 | Recommend `max` unless a shared resource limits it | **changed** (R69): the value is `max` | L194 |
| 179 | Until the operator answers, Build runs one item at a time | **changed** (R69, R149): no answer awaited | — |
| — | An invalid line was replaced → log a ruling naming the old line and `max` | **changed** (overlay G7 edit 6; R151): new | L195–196 |
| — | The operator gives another value → record it with Write step 3 | **changed** (overlay G7 edit 6; R69): new | L197 |
| 181 | Write heading | kept | L199 |
| 183 | Write two lines | **changed** (overlay G7 edit 8; R151): absent → write; present → replace the next non-empty line | L201–203 |
| 184 | First tracker touch: the onboarding commit | kept | L204 |
| 185–187 | Repo onboarded earlier: `Record execution` commit through Review | kept; **changed** (overlay G7 edit 9; R157): the ticket id is the item's own, at a chunk the Epic id | L205–208 |
| 188 | **security** reads any change to `## Execution` | kept | L209 |
| 190–192 | The value caps concurrency only; never relaxes a gate | kept | L211–213 |
| 194–197 | Never: tokens or config values; env and host names allowed | kept | L215–218 |
| 198–199 | Never install from a marketplace or with `npx`; tell the operator what is missing | kept; **changed** (R152): the tell is an ask section | L219–220; L52–56 |
| 200 | Never add a vendor skill: INTAKE | kept | L221 |

New rule with no old line: every "ask the operator" or "tell the operator"
is an ask section in the work's asks file, sent in the liaison's next
batch (touchpoint 1's at end of chunk Brief); send no message from this
skill; "stop" stops that area only; a Discover step that needs an answer
finishes after it (overlay G7 edit 4a; R101, R152), L52–61.

## Meaning questions

- MQ1: old L177 "Accept no other answers" bounded the operator's reply.
  With no question there is no reply to bound. A value the operator gives
  later is recorded by Write step 3, and Execution Check (old L160–162,
  new L180–184) still fails any value other than `max`, `serial` or
  `at most <N>`. Resolved by [rulings.md](../rulings.md) R69 and the
  Check text: no rule is lost.
