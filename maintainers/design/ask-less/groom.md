# Groom — Ask less

DRAFT (pre-review)

<!-- At freeze, replace the draft marker above with this sentence and
delete this comment: Frozen record of the plan as reviewed at Groom on
<YYYY-MM-DD>. Not live: the tracker is the source of truth for tickets,
blockers and state. -->

- Chunk: `DER-712` · LLD: `maintainers/design/ask-less/lld.md` · Date: `2026-11-11`
- Review: `<groom reviewer label>` — pass on `<date>` at `<SHA of the
  reviewed draft commit>`; `pending` until filled at freeze
- Tickets: `G1` = `<id>`, … (filled at freeze)

Fifteen items, one per HLD item: A0–A9 are G1–G10, E1–E5 are G11–G15.
Every item honors the accepted Spec; none adds a gate. Builders: Grok 4.7
for text items, Opus for the move and the runner work. The operator
also allowed Sol 6.1 through Codex for work; the manager may assign it
in place of either. Every item runs inside the existing capped agent
units (GR12). Each A item and E1 carries rule maps per the writing
standard (A0: a path map) and one `CHANGELOG.md` Unreleased line from
[Changelog lines](lld.md#changelog-lines); E2 adds new files and its
one Added line. E3–E5 land no agent text and add no changelog line.

## Helpers

Proving commands that compare a file with its exact text in the LLD use
this function. Define it in the shell first, from the repo root. It
prints the first column-0 fenced block after the line that starts with
the marker, without its fences, from the LLD in the working tree, which
is frozen once this plan passes review. No commit is pinned.

```bash
lldblock() { awk -v m="$1" 'f==0 && index($0,m)==1 {f=1; next} f==1 && /^```/ {fence=$0; sub(/[a-z]+$/,"",fence); f=2; next} f==2 && $0==fence {exit} f==2 {print}' maintainers/design/ask-less/lld.md; }
```

## Items

### G1: Move the SDLC to skills/sdlc (paths only)

- Type: Task
- Parent: `DER-712`
- LLD: `maintainers/design/ask-less/lld.md#a0-file-map`
- Branch: `item/<ticket-id>-sdlc-move`
- Source item: A0 · Builder: Opus

- **Outcome** — The SDLC index is `skills/sdlc/SKILL.md`; its step files and intake are in `skills/sdlc/references/`; `docs/SDLC.md` is the 7-line pointer; every other changed file differs from `c26f424` only by the LLD link rules.
- **Acceptance**
  - LLD A0 steps 0–11 done exactly: file map, frontmatter, link rule sets per file class, pointer text, the `SOURCES.md` `sdlc` row and path-edit notes, writing-standard L141, one Unreleased line.
  - A path map with the protected-rows table, every row `kept`, in `maintainers/design/ask-less/rule-maps/` (R47).
  - **security** reads the item at Review: skill id `sdlc`, the protected rows, the `SOURCES.md` notes and blobs.
- **Verify** — from the repo root on this item's branch; each command prints what its comment says:

```bash
# run every command of the A0 check block (lld.md#a0-check), parts 1-6: each prints nothing or the value its comment names
wc -l < skills/sdlc/SKILL.md   # 178
```

  K1–K4 and K7 per the writing standard, leaving out `maintainers/design/`, whose records predate A0. K7's anchors that later items create (`liaison.md`, `#refine`, `#escalation`, `#touchpoints`, `#while-a-question-is-open`) are checked at G15, once those files exist.
- **Blocked by** — none
- **Blocks** — G2–G10: each edits a moved path or A0's post-move text
- **Out of scope** — any wording change; the A1–A9 rewrites
- **Proposed fix** — `n/a — split from accepted Spec`
- **Removal alternative** — `n/a — split from accepted Spec`
- **Pick** — `n/a — split from accepted Spec`
- **Plan / Spec** — honors

### G2: Index: asking the operator, escalation, touchpoints

- Type: Task
- Parent: `DER-712`
- LLD: `maintainers/design/ask-less/lld.md#a1--sdlc-index-asking-escalation-touchpoints`
- Branch: `item/<ticket-id>-index-asking`
- Source item: A1 · Builder: Grok 4.7

- **Outcome** — `skills/sdlc/SKILL.md` carries the LLD A1 asking block and the three other A1 edits, at 249 lines.
- **Acceptance**
  - A1 edits 1–4 done exactly; the asking block is byte-identical to the LLD block.
  - Rule map with the A1 dispositions.
  - **security** reads the item at Review.
- **Verify** — from the repo root on this item's branch, after defining `lldblock` (groom.md, Helpers); each command prints what its comment says:

```bash
diff <(lldblock '4. **Steps table.**') <(sed -n '/^<a id=.asking-the-human.><.a>$/,/Guardrails we added. section.$/p' skills/sdlc/SKILL.md)   # nothing
wc -l < skills/sdlc/SKILL.md                                    # 249
grep -c 'id=.asking-the-human.' skills/sdlc/SKILL.md            # 1
grep -c 'id=.while-a-question-is-open.' skills/sdlc/SKILL.md    # 1
grep -cE '^### (Escalation|Touchpoints)$' skills/sdlc/SKILL.md  # 2
grep -c 'references/liaison.md' skills/sdlc/SKILL.md            # 3
grep -ciE 'AFK|headless|autonomous' skills/sdlc/SKILL.md        # 0
```

- **Blocked by** — G1: edits the moved index
- **Blocks** — G15
- **Caps** — judged by writing standard 9 and K1 as G9 leaves them: a rewrite may grow to its cap (SD-Q22, R45, R64), and K2 is not applied. That growth is already approved; do not wait for an approval.
- **Out of scope** — `liaison.md` (G3); step-file edits (G4–G8)
- **Proposed fix** — `n/a — split from accepted Spec`
- **Removal alternative** — `n/a — split from accepted Spec`
- **Pick** — `n/a — split from accepted Spec`
- **Plan / Spec** — honors

### G3: Liaison, asks file and message templates

- Type: Task
- Parent: `DER-712`
- LLD: `maintainers/design/ask-less/lld.md#a2--liaison-asks-file-messages-pointer`
- Branch: `item/<ticket-id>-liaison-asks`
- Source item: A2 · Builder: Grok 4.7

- **Outcome** — The liaison procedure, the asks-file template and the batch and touchpoint message shape exist as the LLD writes them, and the stage-result pointer, layout line and subagents route point at them.
- **Acceptance**
  - New `skills/sdlc/references/liaison.md` and `skills/sdlc-artifacts/templates/asks.md`, and the replaced `ask-human.md`, are byte-identical to the LLD blocks.
  - `sdlc-artifacts` map: the three row edits; `stage-result.md` L54 and L141 in place; `conventions.md` L39 in place; the `subagents.md` line at the end of Step agents.
  - Rule maps, with MQ1 for the `ask-human.md` shape change resolved by the brief.
  - **security** reads the item at Review.
- **Verify** — from the repo root on this item's branch, after defining `lldblock` (groom.md, Helpers); each command prints what its comment says:

```bash
diff <(lldblock '**New file `skills/sdlc/references/liaison.md`**') skills/sdlc/references/liaison.md                 # nothing
diff <(lldblock '**New file `skills/sdlc-artifacts/templates/asks.md`**') skills/sdlc-artifacts/templates/asks.md     # nothing
diff <(lldblock '**`skills/sdlc-artifacts/templates/ask-human.md`**: replace') skills/sdlc-artifacts/templates/ask-human.md   # nothing
wc -l < skills/sdlc/references/stage-result.md                                                 # 150
grep -c 'question.: .asks: ' skills/sdlc/references/stage-result.md                            # 1
wc -l < skills/sdlc/references/conventions.md                                                  # 100
grep -c 'groom.md (frozen once tickets exist), rulings.md, asks.md' skills/sdlc/references/conventions.md   # 1
grep -c 'liaison.md#raising-an-ask' skills/sdlc/references/subagents.md                        # 1
grep -c 'templates/asks.md' skills/sdlc-artifacts/SKILL.md                                     # 1
```

- **Blocked by** — G1: edits moved step files
- **Blocks** — G15
- **Caps** — judged by writing standard 9 and K1 as G9 leaves them: a rewrite may grow to its cap (SD-Q22, R45, R64), and K2 is not applied. That growth is already approved; do not wait for an approval.
- **Out of scope** — the index asking text (G2)
- **Proposed fix** — `n/a — split from accepted Spec`
- **Removal alternative** — `n/a — split from accepted Spec`
- **Pick** — `n/a — split from accepted Spec`
- **Plan / Spec** — honors

### G4: Brief step: refiner without yagni, touchpoint 1

- Type: Task
- Parent: `DER-712`
- LLD: `maintainers/design/ask-less/lld.md#a3--brief-step-and-discover-the-idea`
- Branch: `item/<ticket-id>-brief-refine`
- Source item: A3 · Builder: Grok 4.7

- **Outcome** — The chunk Brief runs the refiner from `discover-the-idea` Refine without `yagni`, sends touchpoint 1 once per loop, and freezes the confirmed brief; the gatherer files its asks and writes the brief.
- **Acceptance**
  - `entry-brief-repo.md` edits 1–4 exact, 144 lines.
  - `AGENTS.md` Refine row exact.
  - `discover-the-idea` edits 1–10 exact, with the `## Refine` section.
  - Rule maps; **security** reads the `discover-the-idea` body at Review.
- **Verify** — from the repo root on this item's branch; each command prints what its comment says:

```bash
wc -l < skills/sdlc/references/entry-brief-repo.md                         # 144
grep -ci 'afk' skills/sdlc/references/entry-brief-repo.md                  # 0
grep -c 'discover-the-idea/SKILL.md#refine' skills/sdlc/references/entry-brief-repo.md AGENTS.md   # 1 each
grep -c 'skills/yagni' AGENTS.md                                           # 0
grep -c '^## Refine$' skills/discover-the-idea/SKILL.md                    # 1
grep -c 'Return .back to Gather.' skills/discover-the-idea/SKILL.md        # 1
grep -c 'one more round on out-of-scope' skills/discover-the-idea/SKILL.md # 0
```

- **Blocked by** — G1: edits a moved step file
- **Blocks** — G15
- **Caps** — judged by writing standard 9 and K1 as G9 leaves them: a rewrite may grow to its cap (SD-Q22, R45, R64), and K2 is not applied. That growth is already approved; do not wait for an approval.
- **Out of scope** — onboarding text (G7); Build text (G6)
- **Proposed fix** — `n/a — split from accepted Spec`
- **Removal alternative** — `n/a — split from accepted Spec`
- **Pick** — `n/a — split from accepted Spec`
- **Plan / Spec** — honors

### G5: yagni off the refiner, on the reviewer

- Type: Task
- Parent: `DER-712`
- LLD: `maintainers/design/ask-less/lld.md#a4--yagni-off-the-refiner-on-the-reviewer`
- Branch: `item/<ticket-id>-yagni-reviewer`
- Source item: A4 · Builder: Grok 4.7

- **Outcome** — `yagni` is the LLD's 40-line body; the refiner no longer packs it; the reviewer loads it and Review step 5 fails diffs that change authority files.
- **Acceptance**
  - `skills/yagni/SKILL.md` byte-identical to the LLD block.
  - `subagents.md` pack-list phrase edits; `build-review.md` Review steps 4–5 exact.
  - A4 rule map for `yagni`; **security** reads the `yagni` body at Review.
- **Verify** — from the repo root on this item's branch, after defining `lldblock` (groom.md, Helpers); each command prints what its comment says:

```bash
diff <(lldblock '**`skills/yagni/SKILL.md`**: replace') skills/yagni/SKILL.md          # nothing
wc -l < skills/yagni/SKILL.md                                                          # 40
grep -c 'refiner with .yagni.' skills/sdlc/references/subagents.md                     # 0
grep -c 'refiner with .discover-the-idea.' skills/sdlc/references/subagents.md         # 1
grep -c 'and .yagni. plus the range' skills/sdlc/references/subagents.md               # 1
grep -c 'and .yagni. loaded' skills/sdlc/references/build-review.md                    # 1
grep -c 'citing the operator.s instruction' skills/sdlc/references/build-review.md     # 1
```

- **Blocked by** — G1: edits moved step files
- **Blocks** — G15
- **Caps** — judged by writing standard 9 and K1 as G9 leaves them: a rewrite may grow to its cap (SD-Q22, R45, R64), and K2 is not applied. That growth is already approved; do not wait for an approval.
- **Out of scope** — Open blockers, Dispatch and Debug in Build (G6)
- **Proposed fix** — `n/a — split from accepted Spec`
- **Removal alternative** — `n/a — split from accepted Spec`
- **Pick** — `n/a — split from accepted Spec`
- **Plan / Spec** — honors

### G6: Build: defer and escalate, dispatch defaults to max

- Type: Task
- Parent: `DER-712`
- LLD: `maintainers/design/ask-less/lld.md#a5--build-returns`
- Branch: `item/<ticket-id>-build-returns`
- Source item: A5 · Builder: Grok 4.7

- **Outcome** — Build defers an out-of-chunk blocker and escalates instead of asking, dispatch writes `Parallelism: max`, and a wrong-kind failure escalates one rung.
- **Acceptance**
  - The three A5 edits to `build-review.md` exact.
  - Rule map; **security** reads the item at Review.
- **Verify** — from the repo root on this item's branch; each command prints what its comment says:

```bash
grep -ci 'ask the operator' skills/sdlc/references/build-review.md                 # 0
grep -c 'which writes .Parallelism: max.' skills/sdlc/references/build-review.md   # 1
grep -c 'SKILL.md#escalation' skills/sdlc/references/build-review.md               # 2
```

- **Blocked by** — G1: edits a moved step file
- **Blocks** — G15
- **Caps** — judged by writing standard 9 and K1 as G9 leaves them: a rewrite may grow to its cap (SD-Q22, R45, R64), and K2 is not applied. That growth is already approved; do not wait for an approval.
- **Out of scope** — Review steps 4–5 (G5)
- **Proposed fix** — `n/a — split from accepted Spec`
- **Removal alternative** — `n/a — split from accepted Spec`
- **Pick** — `n/a — split from accepted Spec`
- **Plan / Spec** — honors

### G7: Onboarding: Parallelism max, Discover asks in touchpoint 1

- Type: Task
- Parent: `DER-712`
- LLD: `maintainers/design/ask-less/lld.md#a6--onboarding`
- Branch: `item/<ticket-id>-onboarding-max`
- Source item: A6 · Builder: Grok 4.7

- **Outcome** — Onboarding writes `Parallelism: max` with no question, runs the Tracker Write only after the operator's answer, and routes its Discover and Propose asks into touchpoint 1.
- **Acceptance**
  - A6 edits 1–7, with 4a, exact in `skills/sdlc-onboarding/SKILL.md`.
  - Rule map; **security** reads the body at Review.
- **Verify** — from the repo root on this item's branch; each command prints what its comment says:

```bash
grep -c 'Until the operator answers, Build runs one item' skills/sdlc-onboarding/SKILL.md   # 0
grep -c 'The value is .max.. Do not ask the operator.' skills/sdlc-onboarding/SKILL.md     # 1
grep -c 'Before any area.s Write' skills/sdlc-onboarding/SKILL.md                         # 1
grep -c 'touchpoint 1.s batch' skills/sdlc-onboarding/SKILL.md                            # 1
grep -c 'get both areas' skills/sdlc-onboarding/SKILL.md                                  # 0
grep -ci 'headless' skills/sdlc-onboarding/SKILL.md                                       # 0
wc -l < skills/sdlc-onboarding/SKILL.md                                                   # 250 or less
```

- **Blocked by** — G1: its old text is A0's post-move text
- **Blocks** — G15
- **Caps** — judged by writing standard 9 and K1 as G9 leaves them: a rewrite may grow to its cap (SD-Q22, R45, R64), and K2 is not applied. That growth is already approved; do not wait for an approval.
- **Out of scope** — tracker schema; the Tracker Propose choices 1/2/3 stay
- **Proposed fix** — `n/a — split from accepted Spec`
- **Removal alternative** — `n/a — split from accepted Spec`
- **Pick** — `n/a — split from accepted Spec`
- **Plan / Spec** — honors

### G8: Design gate gathers acceptances; optional HLD touchpoint

- Type: Task
- Parent: `DER-712`
- LLD: `maintainers/design/ask-less/lld.md#a7--design-gate-and-hld-touchpoint`
- Branch: `item/<ticket-id>-design-gate`
- Source item: A7 · Builder: Grok 4.7

- **Outcome** — UX, mockup and LLD acceptance happen at the design gate, an HLD review touchpoint runs only when chosen, and `ux-design` routes its acceptance there.
- **Acceptance**
  - The three `plan-trial-spec.md` edits exact, 150 lines.
  - The `ux-design` step 3 edit exact; its L79–80 stays.
  - Rule maps; **security** reads the `ux-design` body at Review.
- **Verify** — from the repo root on this item's branch; each command prints what its comment says:

```bash
wc -l < skills/sdlc/references/plan-trial-spec.md                                       # 150
grep -c 'SKILL.md#touchpoints' skills/sdlc/references/plan-trial-spec.md                # 3
grep -c 'For mockups, this happens before Groom' skills/sdlc/references/plan-trial-spec.md   # 0
grep -c 'go to the operator at the design' skills/ux-design/SKILL.md                    # 1
```

- **Blocked by** — G1: edits a moved step file
- **Blocks** — G15
- **Caps** — judged by writing standard 9 and K1 as G9 leaves them: a rewrite may grow to its cap (SD-Q22, R45, R64), and K2 is not applied. That growth is already approved; do not wait for an approval.
- **Out of scope** — Chunk B's design-gate review and lenses
- **Proposed fix** — `n/a — split from accepted Spec`
- **Removal alternative** — `n/a — split from accepted Spec`
- **Pick** — `n/a — split from accepted Spec`
- **Plan / Spec** — honors

### G9: Writing standard and maintainer rules

- Type: Task
- Parent: `DER-712`
- LLD: `maintainers/design/ask-less/lld.md#a8--writing-standard-and-maintainer-rules`
- Branch: `item/<ticket-id>-writing-standard`
- Source item: A8 · Builder: Grok 4.7

- **Outcome** — The writing standard names the new owners, retires the AFK row and K2, lets rewrites grow to their caps, generalises rule maps per chunk, exempts the two templates from K6 and catches `xai-` keys; `maintainers/AGENTS.md` lists the new agent-text paths.
- **Acceptance**
  - A8 edits 1–10 exact; `maintainers/writing-standard.md` stays 150 lines.
  - The `maintainers/AGENTS.md` § Evals line exact; rules 1–5 unchanged.
  - Rule maps.
- **Verify** — from the repo root on this item's branch; each command prints what its comment says:

```bash
wc -l < maintainers/writing-standard.md                                      # 150
grep -ci 'afk' maintainers/writing-standard.md                               # 0
grep -c 'retired by DER-712' maintainers/writing-standard.md                 # 1
grep -c 'xai-' maintainers/writing-standard.md                               # 1
grep -c 'except .ask-human.md. and .asks.md.' maintainers/writing-standard.md   # 1
grep -c 'design/<chunk-slug>/rule-maps' maintainers/writing-standard.md      # 1
grep -c 'discover-the-idea/SKILL.md#refine' maintainers/writing-standard.md  # 1
grep -c 'the SDLC is .skills/sdlc/.' maintainers/AGENTS.md                   # 1
```

- **Blocked by** — G1: its old text is A0's post-move text
- **Blocks** — G15
- **Out of scope** — `## Evals` rules 1–5 (T1–T3 stay the merge rule, R59)
- **Proposed fix** — `n/a — split from accepted Spec`
- **Removal alternative** — `n/a — split from accepted Spec`
- **Pick** — `n/a — split from accepted Spec`
- **Plan / Spec** — honors

### G10: SOURCES.md intent credits and row notes

- Type: Task
- Parent: `DER-712`
- LLD: `maintainers/design/ask-less/lld.md#a9--sourcesmd-credits-and-row-notes`
- Branch: `item/<ticket-id>-sources-credits`
- Source item: A9 · Builder: Grok 4.7

- **Outcome** — `SOURCES.md` credits the upstream ideas the chunk used, at their pins, and its rows describe the changed skills.
- **Acceptance**
  - Before the builder writes a credit, a **security** agent, not the builder, re-reads each source at its pin (clone, no install; intake steps 1–2). The **manager** records each source, pin and verdict on this ticket with `comment`.
  - The A9 table appends and replacements exact, minus any credit the read does not support.
  - A dropped credit is also removed from `comparables.md` and logged as a ruling in `rulings.md`.
  - Every `YYYY-MM-DD` this item writes is the date of this item's own **security** read; it waits on no other item's read.
- **Verify** — from the repo root on this item's branch; each command prints what its comment says:

```bash
grep -c 'Intent credits (DER-712)' SOURCES.md   # 2, unless the read dropped every credit of a row
grep -c 'Decide and log' SOURCES.md             # 1
grep -c 'no question; DER-712' SOURCES.md       # 1
grep -c 'Template asks.md' SOURCES.md           # 1
grep -c 'design gate route' SOURCES.md          # 1
```

- **Blocked by** — G1: appends to the `sdlc` row G1 creates
- **Blocks** — G15
- **Caps** — judged by writing standard 9 and K1 as G9 leaves them: a rewrite may grow to its cap (SD-Q22, R45, R64), and K2 is not applied. That growth is already approved; do not wait for an approval.
- **Out of scope** — any third-party body; pin bumps
- **Proposed fix** — `n/a — split from accepted Spec`
- **Removal alternative** — `n/a — split from accepted Spec`
- **Pick** — `n/a — split from accepted Spec`
- **Plan / Spec** — honors

### G11: Eval text: C6, T1–T3 keys, procedure

- Type: Task
- Parent: `DER-712`
- LLD: `maintainers/design/ask-less/lld.md#e1--eval-text`
- Branch: `item/<ticket-id>-eval-c6`
- Source item: E1 · Builder: Grok 4.7

- **Outcome** — Every task scores C6 by the judging table; the T1 key has no Execution ask; T3's triggers follow the escalation ladder; the procedure names the two confirmed models and runners and the extra runner, probe and record rules.
- **Acceptance**
  - Every E1 edit exact: `procedure.md` 1–13 with 6a–6c, `run-template.md` 1–6, the reply-table C6 marks, `t1-card.md`, `t1-key.md`, `t2-card.md`, `t3-card.md`, `t3-key.md`.
  - Models stay Grok 4.7 through the grok CLI and DeepSeek V4.1 Flash 1017 through OpenRouter with OpenCode under T3 Code.
  - Rule maps; **security** reads the Runner needs, Isolation, Pre-run probe and Records changes at Review.
- **Verify** — from the repo root on this item's branch; each command prints what its comment says:

```bash
grep -c '^### Judging an ask (C6)$' maintainers/evals/procedure.md      # 1
grep -c 'deepseek-v4.1-flash-1017' maintainers/evals/procedure.md       # 1
grep -c '^6. A search of the runner home' maintainers/evals/procedure.md   # 1
grep -c 'Never write a credential' maintainers/evals/procedure.md       # 1
grep -c '^## T4 counts$' maintainers/evals/run-template.md              # 1
grep -c 'Reply | C6 |' maintainers/evals/t1-card.md maintainers/evals/t2-card.md maintainers/evals/t3-card.md   # 1 each
grep -c 'No Execution question goes out' maintainers/evals/t1-key.md    # 1
grep -c 'fails C6' maintainers/evals/t3-key.md                          # 1
```

- **Blocked by** — none
- **Blocks** — G13: the runner read and probe use these Runner needs, Isolation and Pre-run probe rules
- **Caps** — judged by writing standard 9 and K1 as G9 leaves them: a rewrite may grow to its cap (SD-Q22, R45, R64), and K2 is not applied. That growth is already approved; do not wait for an approval.
- **Out of scope** — T4 files (G12); runs (G13–G15); any change to provider-side guardrails or spend limits
- **Proposed fix** — `n/a — split from accepted Spec`
- **Removal alternative** — `n/a — split from accepted Spec`
- **Pick** — `n/a — split from accepted Spec`
- **Plan / Spec** — honors

### G12: T4 eval task: a browser Breakout-style game through the SDLC

- Type: Task
- Parent: `DER-712`
- LLD: `maintainers/design/ask-less/lld.md#e2--t4-build-a-browser-breakout-style-game`
- Branch: `item/<ticket-id>-eval-t4`
- Source item: E2 · Builder: Grok 4.7

- **Outcome** — `maintainers/evals/` holds the T4 card, key and dump fixture exactly as the LLD writes them.
- **Acceptance**
  - The three files byte-identical to the LLD blocks.
  - T4 stays an eval job: the game is built only by the agent under test, in scratch repos inside the run directory.
  - One `CHANGELOG.md` line under `## Unreleased`, `### Added`: the E2 line of [Changelog lines](lld.md#changelog-lines).
- **Verify** — from the repo root on this item's branch, after defining `lldblock` (groom.md, Helpers); each command prints what its comment says:

```bash
diff <(lldblock '**`maintainers/evals/t4-dump.md`**') maintainers/evals/t4-dump.md   # nothing
diff <(lldblock '**`maintainers/evals/t4-card.md`**') maintainers/evals/t4-card.md   # nothing
diff <(lldblock '**`maintainers/evals/t4-key.md`**') maintainers/evals/t4-key.md     # nothing
```

- **Blocked by** — none; its links into `procedure.md` and `run-template.md` resolve once G11 lands (land order: after G11, and after G3)
- **Blocks** — G14
- **Out of scope** — any game code in this repo; running T4 (G14, G15)
- **Proposed fix** — `n/a — split from accepted Spec`
- **Removal alternative** — `n/a — split from accepted Spec`
- **Pick** — `n/a — split from accepted Spec`
- **Plan / Spec** — honors

### G13: Runner security reads and smoke tests

- Type: Task
- Parent: `DER-712`
- LLD: `maintainers/design/ask-less/lld.md#e3--runner-reads-and-smoke-tests`
- Branch: `n/a — records only; no repo change`
- Source item: E3 · Builder: Opus
- Related legacy work: DER-294 (runner smoke test), DER-295 (runner security read). Link as related; leave their state as it is.

- **Outcome** — Each runner in the procedure's Models table has a recorded security read and smoke result on this ticket, or a recorded failed need and a return to the operator.
- **Acceptance**
  - A **security** agent, distinct from the builder and the verifier, reads each runner against the procedure's Runner needs and the LLD E3 table, including the revoke line (R102).
  - grok CLI uses the operator's existing subscription login: no new login, no revocation after E5. OpenCode with `openrouter` under T3 Code uses the existing key. Provider-side guardrails and limits stay as they are.
  - Per runner: pre-run probe steps 1–6 recorded as `pass` or `fail` only; the tool-call gate; one T1 repeat on a skills home exported from `main` `c26f424`; tokens in and out over every subagent, wall time, reply mode and the installed runner version as the runner reports them. No version is pinned and host updates stay on (R107).
  - Evidence is only what the runner and the probe actually output. A value the runner cannot give is recorded as `not available` and counts as a failed need; nothing is estimated or filled in.
  - A failed need stops E3 for that runner; the **manager** raises it as an ask for the operator (W3).
  - The **manager** records every result on this ticket with `comment`: no transcript, host name, path outside the repo or credential.
- **Verify** — a verifier agent, not the builder or the security agent, checks each recorded value against the runner's own output, and runs from the repo root:

```bash
git status --porcelain   # nothing: E3 commits no repo file
```

- **Blocked by** — G11: the read and the probe use E1's Runner needs, Isolation and Pre-run probe text
- **Blocks** — G14
- **Out of scope** — the baseline (G14); a dedicated runner login; any provider guardrail or spend change
- **Proposed fix** — `n/a — split from accepted Spec`
- **Removal alternative** — `n/a — split from accepted Spec`
- **Pick** — `n/a — split from accepted Spec`
- **Plan / Spec** — honors

### G14: Baseline on main: T1–T4 on both models

- Type: Task
- Parent: `DER-712`
- LLD: `maintainers/design/ask-less/lld.md#e4--baseline-on-main`
- Branch: `item/<ticket-id>-eval-baseline`
- Source item: E4 · Builder: Opus
- Related legacy work: DER-296 (baseline). Link as related; leave its state as it is.

- **Outcome** — One baseline run file per model on `main` `c26f424`, scored with the integrate head's keys, and both rows in `baseline.md`.
- **Acceptance**
  - Skills home: the export of `main` `c26f424` per the procedure. Keys: the integrate head after G11 and G12 land; each run file's `## Run` names `Keys: integrate/ask-less <sha7>`.
  - T1, T2, T3 and T4, three repeats each, on Grok 4.7 and on DeepSeek V4.1 Flash 1017, through the runners G13 cleared.
  - A clean scorer agent that did not run the task scores C1–C6, Completed and the T4 counts from transcripts and `origin.git`; evidence is short phrases, never quotes.
  - Run files `maintainers/evals/runs/<date>-c26f424-grok-4.7.md` and `maintainers/evals/runs/<date>-c26f424-deepseek-v4.1-flash-1017.md`; two `baseline.md` rows.
  - K10 on this item's diff; **security** reads the first run file at Review.
- **Verify** — from the repo root on this item's branch; each command prints what its comment says:

```bash
ls maintainers/evals/runs/*-c26f424-grok-4.7.md maintainers/evals/runs/*-c26f424-deepseek-v4.1-flash-1017.md   # both files
grep -c 'Keys: integrate/ask-less' maintainers/evals/runs/*-c26f424-*.md   # 1 each
grep -c 'c26f424' maintainers/evals/baseline.md                             # 2
```

- **Blocked by** — G12: T4 must exist to run; G13: the runners must be cleared (G13 already waits on G11's scoring text)
- **Blocks** — G15
- **Out of scope** — the PR-head run (G15); any game code in this repo
- **Proposed fix** — `n/a — split from accepted Spec`
- **Removal alternative** — `n/a — split from accepted Spec`
- **Pick** — `n/a — split from accepted Spec`
- **Plan / Spec** — honors

### G15: PR-head eval run, report and release guard

- Type: Task
- Parent: `DER-712`
- LLD: `maintainers/design/ask-less/lld.md#e5--pr-head-run-and-report`
- Branch: `item/<ticket-id>-eval-head`
- Source item: E5 · Builder: Opus

- **Outcome** — The integrate head is measured against the baseline, the PR into `main` reports regressions first, and the release guard decides merge or report.
- **Acceptance**
  - Skills home: the integrate head after G1–G12 and G14 land; that head's sha7 is the measured head, recorded in the run files and on this ticket. Same task set, repeats, models, runners and scorer rules as G14. Each run file records each runner's installed version.
  - One run file per model at the head's sha7.
  - The PR description lists regressions first, then the T4 counts, baseline → head, per model.
  - Release guard (GR6): a regression per procedure Scoring 4 → no merge, and the liaison reports to the operator; none → the verdict is merge, on the auto-ship permission. G15 records the verdict and its evidence on this ticket; the **manager** performs the merge at the Trunk step. After that merge, the head's run files become the `baseline.md` rows.
  - LLD Verify 1–8 pass on the head. K1–K10 on the tree, including K7's anchors for the files G2–G4 created.
- **Verify** — from the repo root on the measured integrate head; each command prints what its comment says:

```bash
wc -l < skills/sdlc/SKILL.md                         # 249
wc -l < skills/sdlc/references/build-review.md       # 150 or less
wc -l < skills/sdlc/references/entry-brief-repo.md   # 150 or less
wc -l < skills/sdlc/references/liaison.md            # 150 or less
wc -l < skills/sdlc/references/subagents.md          # 150 or less
wc -l < skills/yagni/SKILL.md                        # 40
grep -rniE 'AFK|headless|autonomous' skills/sdlc skills/sdlc-onboarding AGENTS.md maintainers/writing-standard.md   # nothing
ls maintainers/evals/runs/ | grep -c '<measured sha7>'   # 2; the measured head's sha7, as the run files' ## Run section and this ticket record it
```

- **Blocked by** — G2–G10: the head must hold every agent-text change; G14: the baseline to compare with
- **Blocks** — none
- **Out of scope** — the Trunk merge itself, which is the SDLC Trunk step
- **Proposed fix** — `n/a — split from accepted Spec`
- **Removal alternative** — `n/a — split from accepted Spec`
- **Pick** — `n/a — split from accepted Spec`
- **Plan / Spec** — honors

## Graph

- Wave 1: G1, G11, G12
- Wave 2: G2 ← G1; G3 ← G1; G4 ← G1; G5 ← G1; G6 ← G1; G7 ← G1; G8 ← G1; G9 ← G1; G10 ← G1; G13 ← G11
- Wave 3: G14 ← G12, G13
- Wave 4: G15 ← G2, G3, G4, G5, G6, G7, G8, G9, G10, G14

Edges are minimal: G14 needs G11's scoring text, but that need is
already met through G13; G15 needs G1, G11, G12 and G13, already met
through G2 and G14.

Gates: `none`. G15 waits on every item but has no wave after it.

Land order: G1; then G2; then G3; then G4–G10 in any order, and G11
then G12, both after G3; G13 lands nothing; G14; G15. G1 → G2 → G3 and
G11 → G12 are land order only, not blockers: G1's check needs
`CHANGELOG.md` and `maintainers/evals/` unchanged when it lands.

```json
{"items":[
{"g":"G1","source":"A0","title":"Move the SDLC to skills/sdlc (paths only)","slug":"sdlc-move","builder":"Opus","blocked_by":[],"body":"- Type: Task\n- Parent: `DER-712`\n- LLD: `maintainers/design/ask-less/lld.md#a0-file-map`\n- Branch: `item/<ticket-id>-sdlc-move`\n- Source item: A0 · Builder: Opus\n\n- **Outcome** — The SDLC index is `skills/sdlc/SKILL.md`; its step files and intake are in `skills/sdlc/references/`; `docs/SDLC.md` is the 7-line pointer; every other changed file differs from `c26f424` only by the LLD link rules.\n- **Acceptance**\n  - LLD A0 steps 0–11 done exactly: file map, frontmatter, link rule sets per file class, pointer text, the `SOURCES.md` `sdlc` row and path-edit notes, writing-standard L141, one Unreleased line.\n  - A path map with the protected-rows table, every row `kept`, in `maintainers/design/ask-less/rule-maps/` (R47).\n  - **security** reads the item at Review: skill id `sdlc`, the protected rows, the `SOURCES.md` notes and blobs.\n- **Verify** — from the repo root on this item's branch; each command prints what its comment says:\n\n```bash\n# run every command of the A0 check block (lld.md#a0-check), parts 1-6: each prints nothing or the value its comment names\nwc -l < skills/sdlc/SKILL.md   # 178\n```\n\n  K1–K4 and K7 per the writing standard, leaving out `maintainers/design/`, whose records predate A0. K7's anchors that later items create (`liaison.md`, `#refine`, `#escalation`, `#touchpoints`, `#while-a-question-is-open`) are checked at G15, once those files exist.\n- **Blocked by** — none\n- **Blocks** — G2–G10: each edits a moved path or A0's post-move text\n- **Out of scope** — any wording change; the A1–A9 rewrites\n- **Proposed fix** — `n/a — split from accepted Spec`\n- **Removal alternative** — `n/a — split from accepted Spec`\n- **Pick** — `n/a — split from accepted Spec`\n- **Plan / Spec** — honors"},
{"g":"G2","source":"A1","title":"Index: asking the operator, escalation, touchpoints","slug":"index-asking","builder":"Grok 4.7","blocked_by":["G1"],"body":"- Type: Task\n- Parent: `DER-712`\n- LLD: `maintainers/design/ask-less/lld.md#a1--sdlc-index-asking-escalation-touchpoints`\n- Branch: `item/<ticket-id>-index-asking`\n- Source item: A1 · Builder: Grok 4.7\n\n- **Outcome** — `skills/sdlc/SKILL.md` carries the LLD A1 asking block and the three other A1 edits, at 249 lines.\n- **Acceptance**\n  - A1 edits 1–4 done exactly; the asking block is byte-identical to the LLD block.\n  - Rule map with the A1 dispositions.\n  - **security** reads the item at Review.\n- **Verify** — from the repo root on this item's branch, after defining `lldblock` (groom.md, Helpers); each command prints what its comment says:\n\n```bash\ndiff <(lldblock '4. **Steps table.**') <(sed -n '/^<a id=.asking-the-human.><.a>$/,/Guardrails we added. section.$/p' skills/sdlc/SKILL.md)   # nothing\nwc -l < skills/sdlc/SKILL.md                                    # 249\ngrep -c 'id=.asking-the-human.' skills/sdlc/SKILL.md            # 1\ngrep -c 'id=.while-a-question-is-open.' skills/sdlc/SKILL.md    # 1\ngrep -cE '^### (Escalation|Touchpoints)$' skills/sdlc/SKILL.md  # 2\ngrep -c 'references/liaison.md' skills/sdlc/SKILL.md            # 3\ngrep -ciE 'AFK|headless|autonomous' skills/sdlc/SKILL.md        # 0\n```\n\n- **Blocked by** — G1: edits the moved index\n- **Blocks** — G15\n- **Caps** — judged by writing standard 9 and K1 as G9 leaves them: a rewrite may grow to its cap (SD-Q22, R45, R64), and K2 is not applied. That growth is already approved; do not wait for an approval.\n- **Out of scope** — `liaison.md` (G3); step-file edits (G4–G8)\n- **Proposed fix** — `n/a — split from accepted Spec`\n- **Removal alternative** — `n/a — split from accepted Spec`\n- **Pick** — `n/a — split from accepted Spec`\n- **Plan / Spec** — honors"},
{"g":"G3","source":"A2","title":"Liaison, asks file and message templates","slug":"liaison-asks","builder":"Grok 4.7","blocked_by":["G1"],"body":"- Type: Task\n- Parent: `DER-712`\n- LLD: `maintainers/design/ask-less/lld.md#a2--liaison-asks-file-messages-pointer`\n- Branch: `item/<ticket-id>-liaison-asks`\n- Source item: A2 · Builder: Grok 4.7\n\n- **Outcome** — The liaison procedure, the asks-file template and the batch and touchpoint message shape exist as the LLD writes them, and the stage-result pointer, layout line and subagents route point at them.\n- **Acceptance**\n  - New `skills/sdlc/references/liaison.md` and `skills/sdlc-artifacts/templates/asks.md`, and the replaced `ask-human.md`, are byte-identical to the LLD blocks.\n  - `sdlc-artifacts` map: the three row edits; `stage-result.md` L54 and L141 in place; `conventions.md` L39 in place; the `subagents.md` line at the end of Step agents.\n  - Rule maps, with MQ1 for the `ask-human.md` shape change resolved by the brief.\n  - **security** reads the item at Review.\n- **Verify** — from the repo root on this item's branch, after defining `lldblock` (groom.md, Helpers); each command prints what its comment says:\n\n```bash\ndiff <(lldblock '**New file `skills/sdlc/references/liaison.md`**') skills/sdlc/references/liaison.md                 # nothing\ndiff <(lldblock '**New file `skills/sdlc-artifacts/templates/asks.md`**') skills/sdlc-artifacts/templates/asks.md     # nothing\ndiff <(lldblock '**`skills/sdlc-artifacts/templates/ask-human.md`**: replace') skills/sdlc-artifacts/templates/ask-human.md   # nothing\nwc -l < skills/sdlc/references/stage-result.md                                                 # 150\ngrep -c 'question.: .asks: ' skills/sdlc/references/stage-result.md                            # 1\nwc -l < skills/sdlc/references/conventions.md                                                  # 100\ngrep -c 'groom.md (frozen once tickets exist), rulings.md, asks.md' skills/sdlc/references/conventions.md   # 1\ngrep -c 'liaison.md#raising-an-ask' skills/sdlc/references/subagents.md                        # 1\ngrep -c 'templates/asks.md' skills/sdlc-artifacts/SKILL.md                                     # 1\n```\n\n- **Blocked by** — G1: edits moved step files\n- **Blocks** — G15\n- **Caps** — judged by writing standard 9 and K1 as G9 leaves them: a rewrite may grow to its cap (SD-Q22, R45, R64), and K2 is not applied. That growth is already approved; do not wait for an approval.\n- **Out of scope** — the index asking text (G2)\n- **Proposed fix** — `n/a — split from accepted Spec`\n- **Removal alternative** — `n/a — split from accepted Spec`\n- **Pick** — `n/a — split from accepted Spec`\n- **Plan / Spec** — honors"},
{"g":"G4","source":"A3","title":"Brief step: refiner without yagni, touchpoint 1","slug":"brief-refine","builder":"Grok 4.7","blocked_by":["G1"],"body":"- Type: Task\n- Parent: `DER-712`\n- LLD: `maintainers/design/ask-less/lld.md#a3--brief-step-and-discover-the-idea`\n- Branch: `item/<ticket-id>-brief-refine`\n- Source item: A3 · Builder: Grok 4.7\n\n- **Outcome** — The chunk Brief runs the refiner from `discover-the-idea` Refine without `yagni`, sends touchpoint 1 once per loop, and freezes the confirmed brief; the gatherer files its asks and writes the brief.\n- **Acceptance**\n  - `entry-brief-repo.md` edits 1–4 exact, 144 lines.\n  - `AGENTS.md` Refine row exact.\n  - `discover-the-idea` edits 1–10 exact, with the `## Refine` section.\n  - Rule maps; **security** reads the `discover-the-idea` body at Review.\n- **Verify** — from the repo root on this item's branch; each command prints what its comment says:\n\n```bash\nwc -l < skills/sdlc/references/entry-brief-repo.md                         # 144\ngrep -ci 'afk' skills/sdlc/references/entry-brief-repo.md                  # 0\ngrep -c 'discover-the-idea/SKILL.md#refine' skills/sdlc/references/entry-brief-repo.md AGENTS.md   # 1 each\ngrep -c 'skills/yagni' AGENTS.md                                           # 0\ngrep -c '^## Refine$' skills/discover-the-idea/SKILL.md                    # 1\ngrep -c 'Return .back to Gather.' skills/discover-the-idea/SKILL.md        # 1\ngrep -c 'one more round on out-of-scope' skills/discover-the-idea/SKILL.md # 0\n```\n\n- **Blocked by** — G1: edits a moved step file\n- **Blocks** — G15\n- **Caps** — judged by writing standard 9 and K1 as G9 leaves them: a rewrite may grow to its cap (SD-Q22, R45, R64), and K2 is not applied. That growth is already approved; do not wait for an approval.\n- **Out of scope** — onboarding text (G7); Build text (G6)\n- **Proposed fix** — `n/a — split from accepted Spec`\n- **Removal alternative** — `n/a — split from accepted Spec`\n- **Pick** — `n/a — split from accepted Spec`\n- **Plan / Spec** — honors"},
{"g":"G5","source":"A4","title":"yagni off the refiner, on the reviewer","slug":"yagni-reviewer","builder":"Grok 4.7","blocked_by":["G1"],"body":"- Type: Task\n- Parent: `DER-712`\n- LLD: `maintainers/design/ask-less/lld.md#a4--yagni-off-the-refiner-on-the-reviewer`\n- Branch: `item/<ticket-id>-yagni-reviewer`\n- Source item: A4 · Builder: Grok 4.7\n\n- **Outcome** — `yagni` is the LLD's 40-line body; the refiner no longer packs it; the reviewer loads it and Review step 5 fails diffs that change authority files.\n- **Acceptance**\n  - `skills/yagni/SKILL.md` byte-identical to the LLD block.\n  - `subagents.md` pack-list phrase edits; `build-review.md` Review steps 4–5 exact.\n  - A4 rule map for `yagni`; **security** reads the `yagni` body at Review.\n- **Verify** — from the repo root on this item's branch, after defining `lldblock` (groom.md, Helpers); each command prints what its comment says:\n\n```bash\ndiff <(lldblock '**`skills/yagni/SKILL.md`**: replace') skills/yagni/SKILL.md          # nothing\nwc -l < skills/yagni/SKILL.md                                                          # 40\ngrep -c 'refiner with .yagni.' skills/sdlc/references/subagents.md                     # 0\ngrep -c 'refiner with .discover-the-idea.' skills/sdlc/references/subagents.md         # 1\ngrep -c 'and .yagni. plus the range' skills/sdlc/references/subagents.md               # 1\ngrep -c 'and .yagni. loaded' skills/sdlc/references/build-review.md                    # 1\ngrep -c 'citing the operator.s instruction' skills/sdlc/references/build-review.md     # 1\n```\n\n- **Blocked by** — G1: edits moved step files\n- **Blocks** — G15\n- **Caps** — judged by writing standard 9 and K1 as G9 leaves them: a rewrite may grow to its cap (SD-Q22, R45, R64), and K2 is not applied. That growth is already approved; do not wait for an approval.\n- **Out of scope** — Open blockers, Dispatch and Debug in Build (G6)\n- **Proposed fix** — `n/a — split from accepted Spec`\n- **Removal alternative** — `n/a — split from accepted Spec`\n- **Pick** — `n/a — split from accepted Spec`\n- **Plan / Spec** — honors"},
{"g":"G6","source":"A5","title":"Build: defer and escalate, dispatch defaults to max","slug":"build-returns","builder":"Grok 4.7","blocked_by":["G1"],"body":"- Type: Task\n- Parent: `DER-712`\n- LLD: `maintainers/design/ask-less/lld.md#a5--build-returns`\n- Branch: `item/<ticket-id>-build-returns`\n- Source item: A5 · Builder: Grok 4.7\n\n- **Outcome** — Build defers an out-of-chunk blocker and escalates instead of asking, dispatch writes `Parallelism: max`, and a wrong-kind failure escalates one rung.\n- **Acceptance**\n  - The three A5 edits to `build-review.md` exact.\n  - Rule map; **security** reads the item at Review.\n- **Verify** — from the repo root on this item's branch; each command prints what its comment says:\n\n```bash\ngrep -ci 'ask the operator' skills/sdlc/references/build-review.md                 # 0\ngrep -c 'which writes .Parallelism: max.' skills/sdlc/references/build-review.md   # 1\ngrep -c 'SKILL.md#escalation' skills/sdlc/references/build-review.md               # 2\n```\n\n- **Blocked by** — G1: edits a moved step file\n- **Blocks** — G15\n- **Caps** — judged by writing standard 9 and K1 as G9 leaves them: a rewrite may grow to its cap (SD-Q22, R45, R64), and K2 is not applied. That growth is already approved; do not wait for an approval.\n- **Out of scope** — Review steps 4–5 (G5)\n- **Proposed fix** — `n/a — split from accepted Spec`\n- **Removal alternative** — `n/a — split from accepted Spec`\n- **Pick** — `n/a — split from accepted Spec`\n- **Plan / Spec** — honors"},
{"g":"G7","source":"A6","title":"Onboarding: Parallelism max, Discover asks in touchpoint 1","slug":"onboarding-max","builder":"Grok 4.7","blocked_by":["G1"],"body":"- Type: Task\n- Parent: `DER-712`\n- LLD: `maintainers/design/ask-less/lld.md#a6--onboarding`\n- Branch: `item/<ticket-id>-onboarding-max`\n- Source item: A6 · Builder: Grok 4.7\n\n- **Outcome** — Onboarding writes `Parallelism: max` with no question, runs the Tracker Write only after the operator's answer, and routes its Discover and Propose asks into touchpoint 1.\n- **Acceptance**\n  - A6 edits 1–7, with 4a, exact in `skills/sdlc-onboarding/SKILL.md`.\n  - Rule map; **security** reads the body at Review.\n- **Verify** — from the repo root on this item's branch; each command prints what its comment says:\n\n```bash\ngrep -c 'Until the operator answers, Build runs one item' skills/sdlc-onboarding/SKILL.md   # 0\ngrep -c 'The value is .max.. Do not ask the operator.' skills/sdlc-onboarding/SKILL.md     # 1\ngrep -c 'Before any area.s Write' skills/sdlc-onboarding/SKILL.md                         # 1\ngrep -c 'touchpoint 1.s batch' skills/sdlc-onboarding/SKILL.md                            # 1\ngrep -c 'get both areas' skills/sdlc-onboarding/SKILL.md                                  # 0\ngrep -ci 'headless' skills/sdlc-onboarding/SKILL.md                                       # 0\nwc -l < skills/sdlc-onboarding/SKILL.md                                                   # 250 or less\n```\n\n- **Blocked by** — G1: its old text is A0's post-move text\n- **Blocks** — G15\n- **Caps** — judged by writing standard 9 and K1 as G9 leaves them: a rewrite may grow to its cap (SD-Q22, R45, R64), and K2 is not applied. That growth is already approved; do not wait for an approval.\n- **Out of scope** — tracker schema; the Tracker Propose choices 1/2/3 stay\n- **Proposed fix** — `n/a — split from accepted Spec`\n- **Removal alternative** — `n/a — split from accepted Spec`\n- **Pick** — `n/a — split from accepted Spec`\n- **Plan / Spec** — honors"},
{"g":"G8","source":"A7","title":"Design gate gathers acceptances; optional HLD touchpoint","slug":"design-gate","builder":"Grok 4.7","blocked_by":["G1"],"body":"- Type: Task\n- Parent: `DER-712`\n- LLD: `maintainers/design/ask-less/lld.md#a7--design-gate-and-hld-touchpoint`\n- Branch: `item/<ticket-id>-design-gate`\n- Source item: A7 · Builder: Grok 4.7\n\n- **Outcome** — UX, mockup and LLD acceptance happen at the design gate, an HLD review touchpoint runs only when chosen, and `ux-design` routes its acceptance there.\n- **Acceptance**\n  - The three `plan-trial-spec.md` edits exact, 150 lines.\n  - The `ux-design` step 3 edit exact; its L79–80 stays.\n  - Rule maps; **security** reads the `ux-design` body at Review.\n- **Verify** — from the repo root on this item's branch; each command prints what its comment says:\n\n```bash\nwc -l < skills/sdlc/references/plan-trial-spec.md                                       # 150\ngrep -c 'SKILL.md#touchpoints' skills/sdlc/references/plan-trial-spec.md                # 3\ngrep -c 'For mockups, this happens before Groom' skills/sdlc/references/plan-trial-spec.md   # 0\ngrep -c 'go to the operator at the design' skills/ux-design/SKILL.md                    # 1\n```\n\n- **Blocked by** — G1: edits a moved step file\n- **Blocks** — G15\n- **Caps** — judged by writing standard 9 and K1 as G9 leaves them: a rewrite may grow to its cap (SD-Q22, R45, R64), and K2 is not applied. That growth is already approved; do not wait for an approval.\n- **Out of scope** — Chunk B's design-gate review and lenses\n- **Proposed fix** — `n/a — split from accepted Spec`\n- **Removal alternative** — `n/a — split from accepted Spec`\n- **Pick** — `n/a — split from accepted Spec`\n- **Plan / Spec** — honors"},
{"g":"G9","source":"A8","title":"Writing standard and maintainer rules","slug":"writing-standard","builder":"Grok 4.7","blocked_by":["G1"],"body":"- Type: Task\n- Parent: `DER-712`\n- LLD: `maintainers/design/ask-less/lld.md#a8--writing-standard-and-maintainer-rules`\n- Branch: `item/<ticket-id>-writing-standard`\n- Source item: A8 · Builder: Grok 4.7\n\n- **Outcome** — The writing standard names the new owners, retires the AFK row and K2, lets rewrites grow to their caps, generalises rule maps per chunk, exempts the two templates from K6 and catches `xai-` keys; `maintainers/AGENTS.md` lists the new agent-text paths.\n- **Acceptance**\n  - A8 edits 1–10 exact; `maintainers/writing-standard.md` stays 150 lines.\n  - The `maintainers/AGENTS.md` § Evals line exact; rules 1–5 unchanged.\n  - Rule maps.\n- **Verify** — from the repo root on this item's branch; each command prints what its comment says:\n\n```bash\nwc -l < maintainers/writing-standard.md                                      # 150\ngrep -ci 'afk' maintainers/writing-standard.md                               # 0\ngrep -c 'retired by DER-712' maintainers/writing-standard.md                 # 1\ngrep -c 'xai-' maintainers/writing-standard.md                               # 1\ngrep -c 'except .ask-human.md. and .asks.md.' maintainers/writing-standard.md   # 1\ngrep -c 'design/<chunk-slug>/rule-maps' maintainers/writing-standard.md      # 1\ngrep -c 'discover-the-idea/SKILL.md#refine' maintainers/writing-standard.md  # 1\ngrep -c 'the SDLC is .skills/sdlc/.' maintainers/AGENTS.md                   # 1\n```\n\n- **Blocked by** — G1: its old text is A0's post-move text\n- **Blocks** — G15\n- **Out of scope** — `## Evals` rules 1–5 (T1–T3 stay the merge rule, R59)\n- **Proposed fix** — `n/a — split from accepted Spec`\n- **Removal alternative** — `n/a — split from accepted Spec`\n- **Pick** — `n/a — split from accepted Spec`\n- **Plan / Spec** — honors"},
{"g":"G10","source":"A9","title":"SOURCES.md intent credits and row notes","slug":"sources-credits","builder":"Grok 4.7","blocked_by":["G1"],"body":"- Type: Task\n- Parent: `DER-712`\n- LLD: `maintainers/design/ask-less/lld.md#a9--sourcesmd-credits-and-row-notes`\n- Branch: `item/<ticket-id>-sources-credits`\n- Source item: A9 · Builder: Grok 4.7\n\n- **Outcome** — `SOURCES.md` credits the upstream ideas the chunk used, at their pins, and its rows describe the changed skills.\n- **Acceptance**\n  - Before the builder writes a credit, a **security** agent, not the builder, re-reads each source at its pin (clone, no install; intake steps 1–2). The **manager** records each source, pin and verdict on this ticket with `comment`.\n  - The A9 table appends and replacements exact, minus any credit the read does not support.\n  - A dropped credit is also removed from `comparables.md` and logged as a ruling in `rulings.md`.\n  - Every `YYYY-MM-DD` this item writes is the date of this item's own **security** read; it waits on no other item's read.\n- **Verify** — from the repo root on this item's branch; each command prints what its comment says:\n\n```bash\ngrep -c 'Intent credits (DER-712)' SOURCES.md   # 2, unless the read dropped every credit of a row\ngrep -c 'Decide and log' SOURCES.md             # 1\ngrep -c 'no question; DER-712' SOURCES.md       # 1\ngrep -c 'Template asks.md' SOURCES.md           # 1\ngrep -c 'design gate route' SOURCES.md          # 1\n```\n\n- **Blocked by** — G1: appends to the `sdlc` row G1 creates\n- **Blocks** — G15\n- **Caps** — judged by writing standard 9 and K1 as G9 leaves them: a rewrite may grow to its cap (SD-Q22, R45, R64), and K2 is not applied. That growth is already approved; do not wait for an approval.\n- **Out of scope** — any third-party body; pin bumps\n- **Proposed fix** — `n/a — split from accepted Spec`\n- **Removal alternative** — `n/a — split from accepted Spec`\n- **Pick** — `n/a — split from accepted Spec`\n- **Plan / Spec** — honors"},
{"g":"G11","source":"E1","title":"Eval text: C6, T1–T3 keys, procedure","slug":"eval-c6","builder":"Grok 4.7","blocked_by":[],"body":"- Type: Task\n- Parent: `DER-712`\n- LLD: `maintainers/design/ask-less/lld.md#e1--eval-text`\n- Branch: `item/<ticket-id>-eval-c6`\n- Source item: E1 · Builder: Grok 4.7\n\n- **Outcome** — Every task scores C6 by the judging table; the T1 key has no Execution ask; T3's triggers follow the escalation ladder; the procedure names the two confirmed models and runners and the extra runner, probe and record rules.\n- **Acceptance**\n  - Every E1 edit exact: `procedure.md` 1–13 with 6a–6c, `run-template.md` 1–6, the reply-table C6 marks, `t1-card.md`, `t1-key.md`, `t2-card.md`, `t3-card.md`, `t3-key.md`.\n  - Models stay Grok 4.7 through the grok CLI and DeepSeek V4.1 Flash 1017 through OpenRouter with OpenCode under T3 Code.\n  - Rule maps; **security** reads the Runner needs, Isolation, Pre-run probe and Records changes at Review.\n- **Verify** — from the repo root on this item's branch; each command prints what its comment says:\n\n```bash\ngrep -c '^### Judging an ask (C6)$' maintainers/evals/procedure.md      # 1\ngrep -c 'deepseek-v4.1-flash-1017' maintainers/evals/procedure.md       # 1\ngrep -c '^6. A search of the runner home' maintainers/evals/procedure.md   # 1\ngrep -c 'Never write a credential' maintainers/evals/procedure.md       # 1\ngrep -c '^## T4 counts$' maintainers/evals/run-template.md              # 1\ngrep -c 'Reply | C6 |' maintainers/evals/t1-card.md maintainers/evals/t2-card.md maintainers/evals/t3-card.md   # 1 each\ngrep -c 'No Execution question goes out' maintainers/evals/t1-key.md    # 1\ngrep -c 'fails C6' maintainers/evals/t3-key.md                          # 1\n```\n\n- **Blocked by** — none\n- **Blocks** — G13: the runner read and probe use these Runner needs, Isolation and Pre-run probe rules\n- **Caps** — judged by writing standard 9 and K1 as G9 leaves them: a rewrite may grow to its cap (SD-Q22, R45, R64), and K2 is not applied. That growth is already approved; do not wait for an approval.\n- **Out of scope** — T4 files (G12); runs (G13–G15); any change to provider-side guardrails or spend limits\n- **Proposed fix** — `n/a — split from accepted Spec`\n- **Removal alternative** — `n/a — split from accepted Spec`\n- **Pick** — `n/a — split from accepted Spec`\n- **Plan / Spec** — honors"},
{"g":"G12","source":"E2","title":"T4 eval task: a browser Breakout-style game through the SDLC","slug":"eval-t4","builder":"Grok 4.7","blocked_by":[],"body":"- Type: Task\n- Parent: `DER-712`\n- LLD: `maintainers/design/ask-less/lld.md#e2--t4-build-a-browser-breakout-style-game`\n- Branch: `item/<ticket-id>-eval-t4`\n- Source item: E2 · Builder: Grok 4.7\n\n- **Outcome** — `maintainers/evals/` holds the T4 card, key and dump fixture exactly as the LLD writes them.\n- **Acceptance**\n  - The three files byte-identical to the LLD blocks.\n  - T4 stays an eval job: the game is built only by the agent under test, in scratch repos inside the run directory.\n  - One `CHANGELOG.md` line under `## Unreleased`, `### Added`: the E2 line of [Changelog lines](lld.md#changelog-lines).\n- **Verify** — from the repo root on this item's branch, after defining `lldblock` (groom.md, Helpers); each command prints what its comment says:\n\n```bash\ndiff <(lldblock '**`maintainers/evals/t4-dump.md`**') maintainers/evals/t4-dump.md   # nothing\ndiff <(lldblock '**`maintainers/evals/t4-card.md`**') maintainers/evals/t4-card.md   # nothing\ndiff <(lldblock '**`maintainers/evals/t4-key.md`**') maintainers/evals/t4-key.md     # nothing\n```\n\n- **Blocked by** — none; its links into `procedure.md` and `run-template.md` resolve once G11 lands (land order: after G11, and after G3)\n- **Blocks** — G14\n- **Out of scope** — any game code in this repo; running T4 (G14, G15)\n- **Proposed fix** — `n/a — split from accepted Spec`\n- **Removal alternative** — `n/a — split from accepted Spec`\n- **Pick** — `n/a — split from accepted Spec`\n- **Plan / Spec** — honors"},
{"g":"G13","source":"E3","title":"Runner security reads and smoke tests","slug":"runner-reads","builder":"Opus","blocked_by":["G11"],"body":"- Type: Task\n- Parent: `DER-712`\n- LLD: `maintainers/design/ask-less/lld.md#e3--runner-reads-and-smoke-tests`\n- Branch: `n/a — records only; no repo change`\n- Source item: E3 · Builder: Opus\n- Related legacy work: DER-294 (runner smoke test), DER-295 (runner security read). Link as related; leave their state as it is.\n\n- **Outcome** — Each runner in the procedure's Models table has a recorded security read and smoke result on this ticket, or a recorded failed need and a return to the operator.\n- **Acceptance**\n  - A **security** agent, distinct from the builder and the verifier, reads each runner against the procedure's Runner needs and the LLD E3 table, including the revoke line (R102).\n  - grok CLI uses the operator's existing subscription login: no new login, no revocation after E5. OpenCode with `openrouter` under T3 Code uses the existing key. Provider-side guardrails and limits stay as they are.\n  - Per runner: pre-run probe steps 1–6 recorded as `pass` or `fail` only; the tool-call gate; one T1 repeat on a skills home exported from `main` `c26f424`; tokens in and out over every subagent, wall time, reply mode and the installed runner version as the runner reports them. No version is pinned and host updates stay on (R107).\n  - Evidence is only what the runner and the probe actually output. A value the runner cannot give is recorded as `not available` and counts as a failed need; nothing is estimated or filled in.\n  - A failed need stops E3 for that runner; the **manager** raises it as an ask for the operator (W3).\n  - The **manager** records every result on this ticket with `comment`: no transcript, host name, path outside the repo or credential.\n- **Verify** — a verifier agent, not the builder or the security agent, checks each recorded value against the runner's own output, and runs from the repo root:\n\n```bash\ngit status --porcelain   # nothing: E3 commits no repo file\n```\n\n- **Blocked by** — G11: the read and the probe use E1's Runner needs, Isolation and Pre-run probe text\n- **Blocks** — G14\n- **Out of scope** — the baseline (G14); a dedicated runner login; any provider guardrail or spend change\n- **Proposed fix** — `n/a — split from accepted Spec`\n- **Removal alternative** — `n/a — split from accepted Spec`\n- **Pick** — `n/a — split from accepted Spec`\n- **Plan / Spec** — honors"},
{"g":"G14","source":"E4","title":"Baseline on main: T1–T4 on both models","slug":"eval-baseline","builder":"Opus","blocked_by":["G12","G13"],"body":"- Type: Task\n- Parent: `DER-712`\n- LLD: `maintainers/design/ask-less/lld.md#e4--baseline-on-main`\n- Branch: `item/<ticket-id>-eval-baseline`\n- Source item: E4 · Builder: Opus\n- Related legacy work: DER-296 (baseline). Link as related; leave its state as it is.\n\n- **Outcome** — One baseline run file per model on `main` `c26f424`, scored with the integrate head's keys, and both rows in `baseline.md`.\n- **Acceptance**\n  - Skills home: the export of `main` `c26f424` per the procedure. Keys: the integrate head after G11 and G12 land; each run file's `## Run` names `Keys: integrate/ask-less <sha7>`.\n  - T1, T2, T3 and T4, three repeats each, on Grok 4.7 and on DeepSeek V4.1 Flash 1017, through the runners G13 cleared.\n  - A clean scorer agent that did not run the task scores C1–C6, Completed and the T4 counts from transcripts and `origin.git`; evidence is short phrases, never quotes.\n  - Run files `maintainers/evals/runs/<date>-c26f424-grok-4.7.md` and `maintainers/evals/runs/<date>-c26f424-deepseek-v4.1-flash-1017.md`; two `baseline.md` rows.\n  - K10 on this item's diff; **security** reads the first run file at Review.\n- **Verify** — from the repo root on this item's branch; each command prints what its comment says:\n\n```bash\nls maintainers/evals/runs/*-c26f424-grok-4.7.md maintainers/evals/runs/*-c26f424-deepseek-v4.1-flash-1017.md   # both files\ngrep -c 'Keys: integrate/ask-less' maintainers/evals/runs/*-c26f424-*.md   # 1 each\ngrep -c 'c26f424' maintainers/evals/baseline.md                             # 2\n```\n\n- **Blocked by** — G12: T4 must exist to run; G13: the runners must be cleared (G13 already waits on G11's scoring text)\n- **Blocks** — G15\n- **Out of scope** — the PR-head run (G15); any game code in this repo\n- **Proposed fix** — `n/a — split from accepted Spec`\n- **Removal alternative** — `n/a — split from accepted Spec`\n- **Pick** — `n/a — split from accepted Spec`\n- **Plan / Spec** — honors"},
{"g":"G15","source":"E5","title":"PR-head eval run, report and release guard","slug":"eval-head","builder":"Opus","blocked_by":["G2","G3","G4","G5","G6","G7","G8","G9","G10","G14"],"body":"- Type: Task\n- Parent: `DER-712`\n- LLD: `maintainers/design/ask-less/lld.md#e5--pr-head-run-and-report`\n- Branch: `item/<ticket-id>-eval-head`\n- Source item: E5 · Builder: Opus\n\n- **Outcome** — The integrate head is measured against the baseline, the PR into `main` reports regressions first, and the release guard decides merge or report.\n- **Acceptance**\n  - Skills home: the integrate head after G1–G12 and G14 land; that head's sha7 is the measured head, recorded in the run files and on this ticket. Same task set, repeats, models, runners and scorer rules as G14. Each run file records each runner's installed version.\n  - One run file per model at the head's sha7.\n  - The PR description lists regressions first, then the T4 counts, baseline → head, per model.\n  - Release guard (GR6): a regression per procedure Scoring 4 → no merge, and the liaison reports to the operator; none → the verdict is merge, on the auto-ship permission. G15 records the verdict and its evidence on this ticket; the **manager** performs the merge at the Trunk step. After that merge, the head's run files become the `baseline.md` rows.\n  - LLD Verify 1–8 pass on the head. K1–K10 on the tree, including K7's anchors for the files G2–G4 created.\n- **Verify** — from the repo root on the measured integrate head; each command prints what its comment says:\n\n```bash\nwc -l < skills/sdlc/SKILL.md                         # 249\nwc -l < skills/sdlc/references/build-review.md       # 150 or less\nwc -l < skills/sdlc/references/entry-brief-repo.md   # 150 or less\nwc -l < skills/sdlc/references/liaison.md            # 150 or less\nwc -l < skills/sdlc/references/subagents.md          # 150 or less\nwc -l < skills/yagni/SKILL.md                        # 40\ngrep -rniE 'AFK|headless|autonomous' skills/sdlc skills/sdlc-onboarding AGENTS.md maintainers/writing-standard.md   # nothing\nls maintainers/evals/runs/ | grep -c '<measured sha7>'   # 2; the measured head's sha7, as the run files' ## Run section and this ticket record it\n```\n\n- **Blocked by** — G2–G10: the head must hold every agent-text change; G14: the baseline to compare with\n- **Blocks** — none\n- **Out of scope** — the Trunk merge itself, which is the SDLC Trunk step\n- **Proposed fix** — `n/a — split from accepted Spec`\n- **Removal alternative** — `n/a — split from accepted Spec`\n- **Pick** — `n/a — split from accepted Spec`\n- **Plan / Spec** — honors"}
]}
```
