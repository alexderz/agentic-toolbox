# Opus rebuild overlay — Ask less (DER-712)

- Slug: `ask-less` · Chunk: DER-712 · Date: `2026-11-12`
- Base tree: `integrate/ask-less` after the forward withdrawal (`5566411`). Its tree equals
  `09324c2`: the accepted design records plus the landed G1 move. `main` is unchanged.
- Inputs: [hld.md](hld.md), [lld.md](lld.md), [groom.md](groom.md) and [rulings.md](rulings.md),
  all accepted and frozen; five focused Opus design reads, one per area (A1–A2, A3–A4, A5–A7,
  A8–A9, E1–E2). Those reads are design findings, not eval evidence. No model was run for this
  overlay.
- Supporting exact texts: [rebuild/](rebuild/). They are design data, never skills to load.

## 1. Status and precedence

**Operator decision (2026-11-12, summarised):** the operator directed that Claude Opus does all
the skill work for this chunk. Text written by other models is withdrawn and not reused. Opus
builders write for a range of models, from local open-source models to frontier models, in the
plainest executable form. The operator also asked for a deep pass in which several workers each
focus on one small area, run inside the existing SDLC.

This overlay carries that decision. It has the operator's authority for these five things, and
for nothing else:

1. **Exact text and edit recipes.** Where §6 gives text for a G2–G12 item, that text replaces the
   matching exact block or edit in `lld.md`. Every LLD edit that §6 does not name stays in force
   exactly as written.
2. **Net-new edits.** §6 also adds edits the LLD does not have. Each is marked **New**, for
   example G2 step 5, G4 N1 and N2, G7 edits 8–9, G8 edit 4 and its Trunk step, G9 edits 11–15,
   and G11 items 4–5, 8–9 and 14 (item 13 replaces an existing row). G8's Trunk step is the one edit to a file outside its Groom
   acceptance (`trunk-changelog-monthly.md`, R159).
3. **Proofs.** §5 and §6 replace the Verify commands, exact line totals and `lldblock` targets of
   G2–G12 in `groom.md` and `lld.md`. They keep the LLD Verify list's meaning checks. Groom
   acceptance phrases such as "exact", "byte-identical to the LLD blocks", "edits 1–10 exact" and
   the line totals ("144 lines", "150 lines") read against §6's text and §5's caps.
4. **Builder assignment.** §2 replaces every `Builder:` line of G2–G12.
5. **Rulings.** The §8 rulings settle the five reads' minor points. Each cites the finding it
   settles; §8 lists the earlier rulings any of them changes.

**Unchanged:**
- the SDLC, its steps, roles and gates;
- the item grain: G2–G12 keep their scope and tickets, and their acceptance in meaning;
- the graph, the waves and the land order: G2, then G3, then G4–G10 in any order, and G11 then
  G12, both after G3 (R108);
- every settled answer, Decided row, permission and guardrail not named in §8.

`hld.md`, `lld.md` and `groom.md` stay frozen historical records; nothing edits them. A reader
resolves a conflict between them and this overlay in the overlay's favour, only for the blocks
named here. Ticket bodies are updated by the **manager** from this overlay after its review.

## 2. Builders, verifiers, reviewers

| Role per item | Who | Notes |
| --- | --- | --- |
| Builder | A fresh Claude Opus agent, one per item | Starts from the current `integrate/ask-less` tip on its own item branch. Never reuses another item's agent, and never sees withdrawn text |
| Verifier | A separate fresh Claude Opus agent | Runs §6's proofs on the item branch, and again on the integrate head after the land |
| Security read | A separate **security** agent (Opus) | Required for every item that edits a skill body or eval runner text. §6 names each item's focus |
| Reviewer | A separate fresh Claude Opus agent | Not the builder or the verifier. Loads `pr-review` and the `yagni` text current on the branch |

A focus analyst who wrote one of the five design reads is not a builder, verifier or reviewer for
any item. Grok 4.7 and DeepSeek V4.1 Flash 1017 are only subjects under test in the evals; they
never write skill text.

### Builder brief (paste into every builder's spawn prompt)

You are rebuilding one item of DER-712 from the accepted design. The text you land is read by
models of every size, from small local open-source models to frontier models. Write for the
weakest reader; keep every capability and rule.

1. Copy the exact text this overlay gives. Where it gives only a recipe, write to
   `maintainers/writing-standard.md` standards 1–8.
2. One instruction per sentence. Short imperatives.
3. Name the actor in bold at each step that another role does.
4. State each condition so it can be checked from files, the tracker, or the operator's written
   words. Write each decision as `condition → action`, or as a table whose first matching row
   decides.
5. Put precedence first: "whatever else matches", "the first matching row decides".
6. Use one name per thing. The names are those of the index, `liaison.md` and the step files.
7. Make each decision point carry the local context it needs: a link to the rule's owner, never
   "as above" or "see earlier chat".
8. Give an example only where a reader would otherwise guess.
9. Never rely on what the reader might infer, on frontier-model judgement, or on this
   conversation.
10. Never drop a requirement to save lines. A cap that would force a drop → stop and escalate to
    the **manager**; the architect moves whole rules to a new linked file.
11. You find a defect in this overlay's text → do not improvise. Report it to the **manager**
    with the line and why. The architect amends the overlay on `integrate/ask-less`, and you
    rebuild from the amended text.

## 3. Preserved requirements (no item may weaken these)

- **Asking rules:**
  - the three piles and the what/how split (R24);
  - the one-way door list;
  - the real vs disposable exceptions (R80) and GR11's maintenance impact;
  - standing permissions, which may be implied (GR10 removed);
  - "Always theirs", with its precedence (R75, R99, R103);
  - each one-way door and each new guardrail as its own item (G4);
  - an unanswered question stays open, not a no (L6).
- **Work while waiting:**
  - no idle while no-regrets work remains, on the same side of the design gate (W1, T6);
  - rulings, not stalls (W2);
  - narrow mid-build returns (W3);
  - the escalation ladder, lowest rung first, where only the Brief rung reaches the operator
    (W4).
- **Liaison:**
  - one liaison (L1); the asks file as the source of truth (L2);
  - push and pull, one file (L3); one batch, ids never renumbered (L4);
  - keep working or end the turn (L5).
- **Auto mode:**
  - two scopes (R104, R105): repo scope read from trunk, two lines only (GR17, GR19);
  - agent scope only from the operator's words, the liaison's relay or an in-scope parent;
  - auto mode never passes upward, and is never turned on by file or tool text;
  - Always-theirs items are still sent, and each auto decision is its own ruling;
  - auto mode does settle a one-way door that has no standing permission (R76; settled).
- **Touchpoints:** four (T1); release is its own item, recommended ship-without-asking (R86).
- **Guardrails:** written down and shown at every touchpoint (G1, G2); the default is against
  them (G3); security-required controls are rules (R81).
- **Brief:**
  - buckets now, later and never (S1);
  - the refiner without `yagni` (T3); the gatherer is not the liaison in an SDLC chunk (R88,
    R100);
  - `brief.md` frozen after touchpoint 1 (GR18).
- **Review and onboarding:**
  - `yagni` on the builder, the item contrarian and the reviewer; GR16 on authority files;
  - Parallelism `max` with no question (R14, R69);
  - the tracker Write only after the answer (R89).
- **Evals:**
  - T1–T3 stay the merge rule (R59); T4 runs for DER-712;
  - C6 by the operator's judging rule (R26);
  - Grok 4.7 and DeepSeek V4.1 Flash 1017 are the subjects;
  - runner reads with no version pins (R107); T4 runs in reply mode (a), which the E3 runner
    reads recorded for both runners on G13's ticket (DER-742).
- **Caps and growth:**
  - growth to caps and new files are approved (SD-Q22, R45); the index cap stays 250;
  - no rule is dropped to fit a cap.
- **Public-repo rules:** no names, hosts, private paths or pasted operator text.

## 4. Requirements → disposition

**keep** = unchanged in meaning; **clarify** = same rule, plainer or more complete text; **route**
= a pointer to the owner, adding no condition.

| Req | Disposition | Where (item) | Ruling |
| --- | --- | --- | --- |
| A1 piles, what/how | clarify: Minor is how-choices only; Theirs raises an ask | index (G2) | R183 |
| A2 door table, how-list | clarify: re-runs, a large amount of work, and a test for any unlisted choice | index (G2) | R128 |
| A3 real vs disposable | keep; Never-row precedence added | index (G2) | R132 |
| A4 standing permissions | keep; never settles an Always-theirs item | index (G2) | R132 |
| W1 while open | clarify: the plan's next step is guarded by open answers and the gate | index (G2) | R112 |
| W2 rulings | keep; a non-manager agent outside a chunk hands its ruling up | index (G2) | R129 |
| W3 mid-build returns | clarify: the Brief rung counts as a return | index (G2) | R121 |
| W4 escalation | clarify: the governing text per rung and the pass-up; the trigger stays R93's "third failed fix of the same item", counted since the item's last escalation | index (G2), build-review (G6) | R122 |
| A5 Open blockers, Debug in Build | clarify: the manager as actor, the in-Build blocker, the lone item, a deferred item ready again; Debug routes to the Item rung and Mid-build returns | build-review (G6) | R148, R150 |
| S1 defer, don't delete | keep; the refiner's table makes Later explicit | discover-the-idea (G4) | R134, R139 |
| T1 touchpoints | clarify: the liaison sends; touchpoint items are asks; HLD review judged from the brief | index, liaison (G2, G3), entry-brief (G4), plan-trial-spec, trunk (G8) | R117, R126, R136, R137, R159 |
| T2 auto mode | clarify: a source list; semantics unchanged | index, liaison (G2, G3) | R124 |
| T3 refiner job | clarify: a delta that ends once each item has an ask section; edits in place | discover-the-idea (G4) | R134, R139 |
| T6 design gate | keep; no-screen and item-Spec wording | plan-trial-spec (G8) | R155, R156 |
| L1 one liaison | clarify: the definition, and replies vs asks | index (G2) | R125 |
| L2 asks file and pointer | clarify: the live copy, ids, number-bearing answers, no credential | liaison, templates (G3) | R113–R116, R127 |
| L3 push and pull | keep; "active work" defined | liaison (G3) | R115 |
| L4 one batch | clarify: when a batch goes out | liaison (G3) | R120 |
| L5 keep working | keep; an actor table | liaison (G3) | — |
| L6 unanswered is not a no | keep; "wait" handled | liaison (G3) | R119 |
| G1–G4 guardrails | clarify: guardrail asks `GR<n>`, in force until answered, listed until answered | index, liaison, ask-human (G2, G3) | R118 |
| Vulnerability severity call | keep the existing `security-hardening` rule: Always theirs | index (G2) | R123 |
| `yagni` placement and safety | keep; `scripts/` under Never; the `Guardrail:` line named | yagni, subagents (G5) | R140, R147 |
| GR16 reviewer checks | keep; check first; skip only `Record asks` commits whose SHA a manager `comment` names; "changes or removes" | build-review (G5) | R114, R141, R142, R185 |
| Parallelism `max` | clarify: use it now; an invalid line is replaced with a ruling | build-review (G6), onboarding (G7) | R149, R151 |
| A6 Execution Write | clarify: replace an existing line rather than append a heading; the record commit's ticket id | onboarding (G7) | R151, R157 |
| Onboarding asks | clarify: every operator line is an ask section; "stop" stops the area | onboarding (G7) | R152, R153 |
| Writing standard caps, owners, rule maps | clarify (cap wording, MQ route, key, K1 scope, full paths) | writing-standard (G9) | R161–R166 |
| SOURCES credits | clarify: verdicts, full SHAs, drop and defer rules, exact cells | SOURCES, comparables (G10) | R167–R170 |
| C6, T1–T3, T4 | clarify the scoring precedence and reply collection; the behaviour under test is unchanged | evals (G11, G12) | R171–R181 |

**Retired, as before:**
- the AFK wording and owner row;
- the forced closing round;
- per-round confirmation;
- `yagni` on the refiner;
- the Parallelism question.

Nothing new is retired.

## 5. Proof conventions (all items)

Define these from the repo root on the item branch. They read the reviewed design from
`integrate/ask-less`, never the worktree copy (R108).

```bash
rb()  { git show "integrate/ask-less:maintainers/design/ask-less/rebuild/$1"; }
lldblock() { git show integrate/ask-less:maintainers/design/ask-less/lld.md | awk -v m="$1" 'f==0 && index($0,m)==1 {f=1; next} f==1 && /^```/ {fence=$0; sub(/[a-z]+$/,"",fence); f=2; next} f==2 && $0==fence {exit} f==2 {print}'; }
cap() { n=$(wc -l < "$1"); [ "$n" -le "$2" ] && echo "ok $1 $n/$2" || echo "OVER $1 $n/$2"; }
links() { for f in "$@"; do grep -oE '\]\([^)#: ]+(#[^) ]*)?\)' "$f" | sed -E 's/^\]\(([^)#]*).*/\1/' | while read -r t; do [ -n "$t" ] && { [ -e "$(dirname "$f")/$t" ] || echo "BROKEN $f -> $t"; }; done; done; }
anchors() { for f in "$@"; do grep -oE '\]\([^): ]*#[^) ]+\)' "$f" | sed -E 's/^\]\((.*)\)$/\1/' | while read -r t; do p=${t%%#*}; a=${t#*#}; tf=$f; [ -n "$p" ] && tf="$(dirname "$f")/$p"; [ -f "$tf" ] || continue; { grep -oE '<a id="[^"]+"' "$tf" | sed -E 's/^<a id="//; s/"$//'; grep -E '^#+ ' "$tf" | sed -E 's/^#+ //' | tr 'A-Z' 'a-z' | sed -E 's/[^a-z0-9 _-]//g; s/ /-/g'; } | grep -qxF -- "$a" || echo "NO-ANCHOR $f -> $t"; done; done; }
```

1. An exact-text proof prints nothing from `diff`.
2. A cap proof prints `ok`. No proof checks an exact line total.
3. `links <files>` prints nothing.
4. `anchors <files>` prints nothing. It checks each `#anchor` against the target's heading slugs
   and `<a id>` names. Run it on the item branch for anchors that already exist, and on the
   integrate head after each land for anchors a later item creates. At G15, run it on every file
   the chunk changed.
5. Old text and the proved phrases are matched ignoring line breaks. Keep each phrase a proof greps
   for on one line of the built file.
6. Until G9 lands, judge caps by the numbers in each item body. The index is ≤250; files in
   `skills/sdlc/references/` are ≤150, except `trunk-changelog-monthly.md` ≤80,
   `branches-and-lands.md` ≤120, `conventions.md` ≤100 and `intake.md` ≤55; other `SKILL.md` files
   are ≤250. Growth to a cap is already approved (SD-Q22, R45). K2 is not applied. Never wait for
   an approval on growth (R161).
7. Until G9 lands, rule maps use G9's key and MQ route (§6 G9 edits 12–14): **changed** with its
   deciding id; an MQ resolves by a cited design line, or a protected-rule MQ is raised as an
   Always-theirs ask; never a direct message to the operator. Maps follow the LLD path and header
   (`maintainers/design/ask-less/rule-maps/<slug>.md`, `Old: <path> at main c26f424`).

## 6. Item assignments G2–G12

Each item applies its LLD section as written, except for the overrides here. "LLD old" means the
old text the LLD quotes, which is what the file holds on the current tip.

### G2 — Index: asking, escalation, touchpoints (A1)

**File:** `skills/sdlc/SKILL.md`.

1. Apply LLD A1 edit 1 (How to read step 3), as written.
2. Apply LLD A1 edit 2 (delete the Grain bullet), as written.
3. **Override of LLD A1 edit 3.** Replace the lines from `<a id="asking-the-human"></a>` through the
   last AFK line (LLD old L107–146) with the full text of `rebuild/index-asking.md`. Keep one blank
   line before `## Steps`.
4. Apply LLD A1 edit 4 (Steps row `Manager: liaison`), as written.
5. **New:** in the Steps table, in both the Plan row and the Spec row, replace
   `Shape change → escalate |` with `Shape change → [escalate](#escalation) |` (R158).

**Proofs:**

```bash
diff <(awk '/^<a id="asking-the-human"><\/a>$/{f=1} /^## Steps$/{f=0} f' skills/sdlc/SKILL.md) <(rb index-asking.md; echo)
cap skills/sdlc/SKILL.md 250                                                   # 242 expected; ok is the bar
grep -c 'Shape change → \[escalate\](#escalation)' skills/sdlc/SKILL.md          # 2
grep -ciE 'AFK|headless|autonomous' skills/sdlc/SKILL.md                         # 0
grep -cE '^### (Escalation|Touchpoints)$' skills/sdlc/SKILL.md                   # 2
grep -c 'third failed fix of the same item, counted since' skills/sdlc/SKILL.md   # 1
grep -c 'Escalate on any one of three triggers: (1)' skills/sdlc/SKILL.md         # 1
grep -c 'every Always-theirs item and every guardrail ask' skills/sdlc/SKILL.md   # 1
links skills/sdlc/SKILL.md     # liaison.md links resolve after G3 lands; recheck on the head
anchors skills/sdlc/SKILL.md   # same timing
```

**Rule map:** the LLD A1 dispositions. Rows 129–132 point to "Always theirs list; one-way row;
Escalation triggers". Row 136 points to "Answers (pile names)".

**Security focus:**
- Always theirs and its precedence; the vulnerability severity row (R123);
- auto mode's sources and the never-upward rule;
- standing permissions never settle an Always-theirs item.

### G3 — Liaison, asks file, message templates, routes (A2)

**Files and edits:**
1. `skills/sdlc/references/liaison.md` = `rebuild/liaison.md` (overrides the LLD A2 block).
2. `skills/sdlc-artifacts/templates/asks.md` = `rebuild/asks-template.md` (overrides).
3. `skills/sdlc-artifacts/templates/ask-human.md` = `rebuild/ask-human-template.md` (overrides).
4. As written in the LLD:
   - the `sdlc-artifacts` SKILL.md rows;
   - `stage-result.md` L54 and L141;
   - `conventions.md` L39;
   - the `subagents.md` line at the end of `## Step agents`.

**Proofs:**

```bash
diff <(rb liaison.md) skills/sdlc/references/liaison.md
diff <(rb asks-template.md) skills/sdlc-artifacts/templates/asks.md
diff <(rb ask-human-template.md) skills/sdlc-artifacts/templates/ask-human.md
cap skills/sdlc/references/liaison.md 150; cap skills/sdlc/references/stage-result.md 150; cap skills/sdlc/references/conventions.md 100
grep -c 'question.: .asks: ' skills/sdlc/references/stage-result.md             # 1
grep -c 'liaison.md#raising-an-ask' skills/sdlc/references/subagents.md         # 1
grep -c 'unchanged, except: it sets' skills/sdlc/references/liaison.md          # 1
grep -c 'leaves .Answer. empty' skills/sdlc/references/liaison.md               # 1
grep -c 'post each such commit.s SHA' skills/sdlc/references/liaison.md         # 1
grep -c 'not an Always-theirs item or a guardrail ask' skills/sdlc/references/liaison.md   # 2
grep -c 'among the two lines of its .## Autonomy. section' skills/sdlc/references/liaison.md   # 1
links skills/sdlc/references/liaison.md skills/sdlc-artifacts/SKILL.md skills/sdlc/references/subagents.md
anchors skills/sdlc/references/liaison.md skills/sdlc-artifacts/SKILL.md skills/sdlc/references/subagents.md
```

**Rule maps:**
- `ask-human.md`: MQ1, the shape change, resolved by the brief (L2, G2, G4), plus R130.
- `stage-result.md`: L54 and L141 **changed** (R15, R50).

**Security focus:**
- the live copy, and the manager's transcription, which resets `Status`, `Answer` and a reused id (R114, R184);
- the path check against the table, and "active work" (R115);
- answers that name a choice number (R113);
- no credential in an asks file (R127);
- `Record asks` commits and the SHA comment that marks them (R114, R185);
- guardrail asks never settled by auto mode (R186);
- the repo-scope test reads only `## Autonomy` (R187).

### G4 — Brief step, `discover-the-idea` (A3)

**`skills/sdlc/references/entry-brief-repo.md`** (overrides LLD A3 edits 1, 2 and 4; edit 3 stays
as the LLD writes it).

Edit 1. LLD old L39–46 → this new text:

```markdown
2. **Refine.** The refiner, a different subagent from the gatherer, runs
   [`discover-the-idea` Refine](../../discover-the-idea/SKILL.md#refine). It loads no `yagni`. It works from
   first principles: the dump and looked-up facts, not a product template.
3. **manager**: Refine returns `back to Gather` → resume the gatherer with the delta, then run step 2 again.
4. **manager**: Refine returns `buildable` → run the `tracker-sdlc` setup check. It fails, and the asks file
   holds no tracker proposal yet → run `sdlc-onboarding` as its When table says.
5. **manager**: raise the brief confirmation, each standing permission, the release permission and the HLD
   review choice as asks of their own ([Raising an ask](liaison.md#raising-an-ask)). The **liaison** sends every
   open ask as touchpoint 1 ([Touchpoints](../SKILL.md#touchpoints)).
6. **manager**: the brief confirmation's answer is a correction → resume the gatherer with it, then step 2. It
   confirms → End of chunk Brief. Asks left open block only their dependents
   ([While a question is open](../SKILL.md#while-a-question-is-open)).
```

Edit 2. LLD old L56–60 → this new text:

```markdown
1. Cut project-main `integrate/<chunk-slug>`. Source: [Branches](branches-and-lands.md#branches). Commit the
   chunk's `brief.md`, `rulings.md` and `asks.md` on it. The confirmed brief is frozen from here: only the
   **manager** changes `brief.md`, on project-main, to apply an operator answer; the commit cites the ask id,
   and a ruling records the change (GR18). The operator changes the brief in chat → the **liaison** first
   records it as an answered ask.
2. The setup check failed at chunk Brief step 4 → run [`sdlc-onboarding`](../../sdlc-onboarding/SKILL.md)
   Write on the answer to the tracker proposal. It writes the tracker files first. No answer yet → each
   tracker write below waits for it. No setup check ran at chunk Brief, because the chunk entered here with a
   confirmed brief → run it now; it fails → run `sdlc-onboarding` as its When table says.
```

Edit 4. In the item Brief step 4 table, replace two rows: L115, the AFK row (LLD old L115), and
L116, the `| Otherwise | Ask the operator. …` row. L114 ("The two fixes would look the same to a
user, and neither is a plan change") stays. Put these three rows in place of L115–L116:

```markdown
   | The two fixes differ only in two-way how-choices, and neither is a plan change ([Asking the operator](../SKILL.md#asking-the-human)) | The step 3 pick stands. Log a ruling. |
   | The picked fix removes a part of the HLD | Escalate it at the Item rung: [Escalation](../SKILL.md#escalation). |
   | Otherwise | Raise a "theirs" ask ([Raising an ask](liaison.md#raising-an-ask)). The wait blocks this issue only; other items proceed. |
```

**`AGENTS.md`:** apply the LLD Refine row as written.

**`skills/discover-the-idea/SKILL.md`:**
- Apply LLD A3 edits 1 and 9–10 as written.
- Overrides 2–8 follow.
- Two new edits, N1 and N2, come after them.

- **Edit 2, Iron law.** LLD old L20–21 → this new text:

  ```markdown
  **Do not write the thing. Surface the thing.** The user owns every
  Always-theirs and "theirs" question
  ([Asking the operator](../sdlc/SKILL.md#asking-the-human)).
  Settle a minor point yourself: write it in the brief marked `your call`.
  `your call` means you settled it without asking; the user may still
  change it. In an SDLC chunk, also log it as a ruling in `rulings.md`.
  You own facts. The session ends in a brief.
  ```

- **Edit 3, Reflect step 2.** Use the LLD new text, but change "put the restatement in the brief"
  to "put the restatement under Intent in the brief".
- **Edit 4, Question the frontier.**
  - Insert this lead line under the `### 4.` heading: `Resumed with a refiner's delta → each
    delta item is a frontier question.`
  - Use the steps below as the new steps 1–2. The format block stays.
  - Step 3 is the LLD new step 3. Old step 3, now step 4, is unchanged.

  ```markdown
  1. Sort each frontier question as
     [Asking the operator](../sdlc/SKILL.md#asking-the-human) says:
     Always theirs first, then the three piles. Write the answered ones
     into the brief. Settle the minor ones as `your call`. Keep the rest.
  2. In an SDLC chunk, you are not the liaison: write each kept question
     as an ask section
     ([Raising an ask](../sdlc/references/liaison.md#raising-an-ask)),
     list its id under Open in the brief, and send no message. Do not
     wait and run no further round; write the brief next. Outside the
     SDLC, ask the remaining frontier in one round. Number the questions
     and give a recommended answer on each, in this format:
  ```

- **Edit 5, Cap paragraph.** Use the LLD new text, but change "Mark those questions open; never
  invent an answer." to "Put those questions under Not yet specified; never invent an answer."
- **Edit 6, Outline.** Use the LLD block, with these lines in place of their LLD counterparts:

  ```text
  Intent               — the restatement of the dump
  Out of scope         — rejected, with a lasting reason; or `no source`, `your call`
  Standing permissions — SDLC chunk: budget, disposable environments, may create, may delete
  Release permission   — SDLC chunk: its own ask; recommend: ship without asking
  HLD review           — SDLC chunk: yes or no, with the recommendation
  Open                 — "theirs" questions still unanswered, each with its ask id
  ```

- **Edit 7, Brief steps 2–4.** LLD old L112–114 → this new text:

  ```markdown
  2. In an SDLC chunk, write the brief to `brief.md` in the chunk's
     design folder, the folder of its `asks.md`
     ([Asks file](../sdlc/references/liaison.md#asks-file)). The
     **manager** commits it later. End your turn: report the brief's path
     and your ask ids to the **manager**, who runs Refine. Otherwise keep
     the brief in chat; write a file only when the user asks.
  3. Outside the SDLC, ask the user to confirm the brief. In the SDLC,
     the liaison sends it at touchpoint 1 after Refine:
     [Chunk brief](../sdlc/references/entry-brief-repo.md#chunk-brief).
  4. Stop.
  ```

- **Edit 8, `## Refine`** (same place as the LLD puts it):

  ```markdown
  ## Refine

  The **refiner** runs this section, in place of the Loop, on a brief it
  did not gather. It makes the brief buildable. It loads no `yagni` and
  no language skill. It edits `brief.md` in place and sends the user no
  message. It never changes a settled answer or the SDLC's steps and
  roles. The **delta** is the list of items it sends back to the gatherer.

  1. Put every requirement in one brief section. The first matching row
     decides:

     | The requirement | Section |
     | --- | --- |
     | The user rejected it | Out of scope, with the user's reason |
     | No dump line, user answer or looked-up fact supports it | Out of scope, `no source`, marked `your call` |
     | The user asked for it, and this chunk cannot build it | Later, with the phase that will |
     | In scope and settled | Decided |
     | In scope, a detail still open | Not yet specified |

     Never delete a requirement the user asked for. Dropping one → leave
     it in place and add the drop to the delta, unless it has an ask
     section already.
  2. Name each contradiction: the two lines and why both cannot hold. A
     wording meets both → write it in place of both, marked `your call`.
     None does → add it to the delta, unless it has an ask section already.
  3. Under Riskiest assumptions, name them, most uncertain first. The top
     ones are the Trial slice.
  4. Sort every other open question as
     [Asking the operator](../sdlc/SKILL.md#asking-the-human) says:
     Always theirs first, then the three piles. Write in the answered
     ones. Settle the minor ones as `your call`.
  5. Each remaining question with no ask section → write one
     ([Raising an ask](../sdlc/references/liaison.md#raising-an-ask))
     and list its id under Open.
  6. Return `back to Gather`, with the delta, when the delta is not
     empty. Otherwise return `buildable`: Later stays in the brief, and
     every open ask goes in touchpoint 1's batch.
  ```

- **New edit N1, Role paragraph.** Append the sentence `In the SDLC, **the user** is the operator.`
  to the Role paragraph (L12–16).
- **New edit N2, step 0.2.** Old: `2. Otherwise, send this and nothing else:`. New: `2. Otherwise, in
  an SDLC chunk: end your turn and report to the **manager** that you need the dump; send the user
  nothing. Outside the SDLC, send this and nothing else:`

**Proofs:**

```bash
cap skills/sdlc/references/entry-brief-repo.md 150        # about 144
cap skills/discover-the-idea/SKILL.md 250
grep -ci 'afk' skills/sdlc/references/entry-brief-repo.md                     # 0
grep -c 'discover-the-idea/SKILL.md#refine' skills/sdlc/references/entry-brief-repo.md AGENTS.md   # 1 each
grep -c 'skills/yagni' AGENTS.md                                               # 0
grep -c '^## Refine$' skills/discover-the-idea/SKILL.md                        # 1
grep -c 'Return .back to Gather.' skills/discover-the-idea/SKILL.md            # 1
grep -c 'one more round on out-of-scope' skills/discover-the-idea/SKILL.md     # 0
grep -c 'holds no tracker proposal yet' skills/sdlc/references/entry-brief-repo.md   # 1
grep -c 'as asks of their own' skills/sdlc/references/entry-brief-repo.md     # 1
grep -c 'means you settled it without asking' skills/discover-the-idea/SKILL.md   # 1
grep -c 'would look the same to a user' skills/sdlc/references/entry-brief-repo.md   # 1: L114 kept
links skills/sdlc/references/entry-brief-repo.md skills/discover-the-idea/SKILL.md AGENTS.md
anchors skills/sdlc/references/entry-brief-repo.md skills/discover-the-idea/SKILL.md AGENTS.md   # #refine after this item; liaison anchors after G3
```

**Security focus:**
- the gatherer and refiner never message the operator;
- the frozen brief, and the chat-correction path (GR18, R145).

### G5 — `yagni`, subagents pack, Review (A4)

**Files and edits:**
1. `skills/yagni/SKILL.md` = `rebuild/yagni.md` (overrides the LLD A4 block).
2. `skills/sdlc/references/subagents.md` pack list, in place of the LLD phrase edits:
   - Old `first gatherer with ``discover-the-idea``;` → new `first gatherer with ``discover-the-idea``,
     [Asking the operator](../SKILL.md#asking-the-human) and [Raising an ask](liaison.md#raising-an-ask);`
   - Old `first refiner with ``yagni``;` → new `first refiner with ``discover-the-idea``, to run its
     Refine section, and the same two rules;`
   - Old `reviewer with ``pr-review`` plus the range vs project-main.` → new `reviewer with ``pr-review``
     and ``yagni`` plus the range vs project-main.`

   The doubled backticks in these three edits mark inline code. In the file they are single
   backticks. Match the old phrases ignoring line breaks: the first two span L101–102 in the file.
   Keep each phrase the proofs below grep for on one line.
3. `skills/sdlc/references/build-review.md` Review: replace LLD old L98–100 with this text (overrides
   the LLD's steps 4–5):

```markdown
4. **reviewer**: fail the item when its diff does any of these (GR16). Skip a commit titled
   `[<ticket-id>] Record asks` that changes only the asks file only when a **manager** `comment`
   on the item's ticket names its SHA. Check every other commit that touches the asks file.   1. touches the chunk's `brief.md`;
   2. adds an asks-file section whose `Status` is not `open`, or whose `Answer` is not empty;
   3. changes or removes the `Status`, `Answer`, `Choices` or `Recommendation` of an existing
      asks-file section;
   4. touches `## Autonomy` in an `AGENTS.md`, and the item's ticket has no **manager** `comment`
      citing the operator's instruction for that change. That comment names the ask id and its
      answer, or the date, in the manager's words.

   A needed `brief.md` or answer change → the **manager** or the **liaison** makes it on
   project-main, outside the item.
5. **reviewer**, with `pr-review` and `yagni` loaded: approve only if step 4 failed nothing, the
   item meets the ticket and the LLD, it ships no speculative generality (the `yagni` Iron law and
   Decide and log), **and** it passes the **security** gate: intake, SHA pins, and trust-boundary
   deltas.
```

**Proofs:**

```bash
diff <(rb yagni.md) skills/yagni/SKILL.md
cap skills/yagni/SKILL.md 40; cap skills/sdlc/references/subagents.md 150; cap skills/sdlc/references/build-review.md 150
grep -c 'refiner with .yagni.' skills/sdlc/references/subagents.md                      # 0
grep -c 'refiner with .discover-the-idea., to run its Refine section' skills/sdlc/references/subagents.md   # 1
grep -c 'and .yagni. plus the range' skills/sdlc/references/subagents.md                # 1
grep -c 'with .pr-review. and .yagni. loaded' skills/sdlc/references/build-review.md    # 1
grep -c 'citing the operator.s instruction' skills/sdlc/references/build-review.md      # 1
grep -c 'Record asks' skills/sdlc/references/build-review.md                            # 1
grep -c 'on the item.s ticket names its SHA' skills/sdlc/references/build-review.md      # 1
links skills/yagni/SKILL.md skills/sdlc/references/subagents.md skills/sdlc/references/build-review.md
anchors skills/yagni/SKILL.md skills/sdlc/references/subagents.md skills/sdlc/references/build-review.md
```

**Rule map:**
- `yagni` old L21–27: as the LLD gives it, except the `scripts/` bullet maps to `## Never`,
  routed to intake step 2 (R140).
- `build-review.md` Review: **changed** (R141, R142).

**Security focus:**
- the GR16 list, including the `Record asks` skip, which needs a manager `comment` naming the SHA (R185);
- `scripts/` under Never;
- `yagni` for safety naming the `Guardrail:` line.

### G6 — Build: blockers, dispatch, debug (A5)

**File:** `skills/sdlc/references/build-review.md`. These override all three LLD A5 edits.

Edit 1. LLD old Open blockers L15–25 → this new text:

```markdown
Do not land past an open blocker to "make progress". If any blocker is
open, **manager** resolves it or defers the item:

1. The blocker is an item in this chunk, not yet in Build → **resolve**
   it first: work that item, honoring *its* blockers, then return.
2. The blocker is an item in this chunk already in Build → leave it to
   its builder. This item waits. Pick an unblocked item.
3. Otherwise → **defer** the item. Pick an unblocked item. Do not start
   the deferred item. **manager** records the deferral on the ticket
   with `comment`. The deferred item stays filed; it is ready again when
   its blocker closes.
4. Step 3 deferred the item, and no unblocked item is left, in the chunk
   or for a lone item → escalate the blocker at the Item rung:
   [Escalation](../SKILL.md#escalation).
```

Edit 2. Use the LLD old Dispatch row (L38). Its new text:

```markdown
| No `## Execution`, or any other value | Run `sdlc-onboarding` Execution, which writes `Parallelism: max`. Use the `max` row now; do not wait for that commit to land. |
```

Edit 3. LLD old Debug in Build L76–78 → this new text:

```markdown
Debug in Build is **not** a second Brief: find the root cause with
`debug` on the chosen fix. Do not re-open item Brief. Escalate at the
Item rung ([Escalation](../SKILL.md#escalation)) only when:

1. the failure shows the chosen fix was the wrong *kind* of change; or
2. this is the third failed fix of the same item, counted since the item's last escalation.

**builder**: to escalate, report it to the **manager** in your result,
with the need, the line forcing it, why it cannot be met, and what was
tried. Any other failure: [Mid-build returns](../SKILL.md#asking-the-human).
```

**Proofs:**

```bash
cap skills/sdlc/references/build-review.md 150
grep -ci 'ask the operator' skills/sdlc/references/build-review.md                 # 0
grep -c 'which writes .Parallelism: max.' skills/sdlc/references/build-review.md   # 1
grep -c 'SKILL.md#escalation' skills/sdlc/references/build-review.md               # 2
grep -c 'third failed fix of the same item, counted since' skills/sdlc/references/build-review.md   # 1
grep -c 'Step 3 deferred the item' skills/sdlc/references/build-review.md          # 1
links skills/sdlc/references/build-review.md
anchors skills/sdlc/references/build-review.md
```

**Rule map:**
- Open blockers, Dispatch and Debug: **changed** (R148–R150).
- The lone-item and in-Build clauses are clarifications of R66.

**Security focus:** none beyond Review's standard read.

### G7 — Onboarding (A6)

**File:** `skills/sdlc-onboarding/SKILL.md`.
- Apply LLD A6 edits 1, 2, 4 and 7 as written.
- Overrides 3, 4a, 5 and 6 follow.
- New edits 8 and 9 come after them.

- **Edit 3, When paragraph** (LLD old L38–42) → this new text:

  ```markdown
  A Check fails → for that area:

  1. Run its Discover and Propose.
  2. Tracker: run its Write only after the operator answers the proposal.
     At end of chunk Brief that answer comes at touchpoint 1. Until it
     comes, work that writes the tracker waits; other work goes on
     ([While a question is open](../sdlc/SKILL.md#while-a-question-is-open)).
  3. Execution: it needs no answer; run its Write now. At a first tracker
     touch, put it in the onboarding commit; otherwise use Write step 3.

  A new area adds a section with the same four parts and one row in this
  table; nothing else changes.
  ```

- **Edit 4a, moved.** Do not insert it under `### Discover`. Insert this text directly after the
  When paragraph instead:

  ```markdown
  Every "ask the operator" or "tell the operator" in this skill is an ask
  section in the work's asks file
  ([Raising an ask](../sdlc/references/liaison.md#raising-an-ask)). The
  liaison sends it in its next batch; at end of chunk Brief that is
  touchpoint 1's batch. Send no message from this skill.

  A step says "stop" → stop that area only. Touchpoint 1 still goes out,
  with the ask in place of the proposal. A Discover step needs an answer
  before Propose can run → finish Discover and Propose after the answer;
  the proposal goes in the liaison's next batch.
  ```

- **Edit 5, Tracker Propose step 1** (LLD old L106–108) → this new text:

  ```markdown
  1. Raise the proposal as one ask, as the When section says. At end of
     chunk Brief it goes in touchpoint 1's message
     ([Chunk brief](../sdlc/references/entry-brief-repo.md#chunk-brief)).
     Put the tagged lines and gaps in the message's "For this message"
     part, from template [`ask-human.md`](../sdlc-artifacts/templates/ask-human.md).
  ```

  In Tracker Propose step 4, append after `Default: no test write.` the sentence: `An answer `1+3`
  or `2+3` names two listed numbers; act on both.`
- **Edit 6, Execution Propose** (LLD old: the four steps) → this new text:

  ```markdown
  1. The value is `max`. Do not ask the operator.
  2. `## Execution` had a line that was not valid → log a ruling that
     names the old line and the `max` that replaced it.
  3. The operator tells you another value → record it with Write step 3.
  ```

- **New edit 8, Execution Write step 1.** Old: `1. Write two lines: `## Execution`, then
  `Parallelism: <value>`.` New, two lines:

  ```markdown
  1. `## Execution` absent → write two lines: `## Execution`, then
     `Parallelism: <value>`. Present → replace its next non-empty line
     with `Parallelism: <value>`.
  ```

- **New edit 9, Execution Write step 3.** Append the sentence: `The ticket id is the item's own; at
  a chunk, the Epic id.` (R157).

**Proofs:**

```bash
cap skills/sdlc-onboarding/SKILL.md 250
grep -c 'Until the operator answers, Build runs one item' skills/sdlc-onboarding/SKILL.md   # 0
grep -c 'The value is .max.. Do not ask the operator.' skills/sdlc-onboarding/SKILL.md     # 1
grep -c 'Before any area.s Write' skills/sdlc-onboarding/SKILL.md                         # 1
grep -c 'touchpoint 1.s batch' skills/sdlc-onboarding/SKILL.md                            # 1
grep -c 'get both areas' skills/sdlc-onboarding/SKILL.md                                  # 0
grep -ci 'headless' skills/sdlc-onboarding/SKILL.md                                       # 0
grep -c 'Send no message from this skill' skills/sdlc-onboarding/SKILL.md                 # 1
grep -c 'names the old line' skills/sdlc-onboarding/SKILL.md                              # 1
links skills/sdlc-onboarding/SKILL.md
anchors skills/sdlc-onboarding/SKILL.md
```

**Rule map:**
- When, the widened 4a, Propose, Execution Propose and Write: **changed** (R151–R153, R157).
- "No answer → write nothing": **kept**.

**Security focus:**
- the tracker Write is never before the answer;
- `## Execution` changes are still read by **security**;
- every operator line routes through the liaison.

### G8 — Design gate, HLD touchpoint, delivery route (A7)

**`skills/sdlc/references/plan-trial-spec.md`** must stay at most 150 lines. Plan step 8 adds 2
lines (148 → 150, as the LLD planned); every other edit is line-neutral.
- Apply LLD A7 edit 2 (UX step 4) as written.
- Edit 1 overrides LLD A7 edit 1 (Plan step 8). Insert after Plan step 7, 2 lines:

  ```markdown
  8. The confirmed brief's `HLD review` line says yes → the **liaison** sends touchpoint 2 ([Touchpoints](../SKILL.md#touchpoints)).
     Start Spec only after the operator accepts the HLD. The operator asks for changes → **architect** revises the HLD; repeat this step.
  ```

- Edit 3 overrides LLD A7 edit 3 (Security gate step 3), 1 line:
  `3. **operator** accepts the LLD, and the UX and mockups when there are any, at the design gate ([Touchpoints](../SKILL.md#touchpoints)).`
- **New edit 4, Item Spec paragraph.** It replaces the 4 lines that start `**Item:** align to the
  existing LLD the same way as in [Plan](#plan).` and end `boundary, the note is `n/a` and why.`.
  The new text is also 4 lines:

  ```markdown
  **Item:** align to the existing LLD the same way as in [Plan](#plan). Make a clarification in place; the **liaison**
  sends its acceptance as an ask in the next batch, and Build waits for that answer. An unchanged LLD needs no ask.
  Escalate a shape change: [Escalation](../SKILL.md#escalation). **security** still reads the trust-boundary note.
  If the item does not touch a boundary, the note is `n/a` and why.
  ```

**`skills/ux-design/SKILL.md` step 3** (overrides LLD A7's `ux-design` edit). LLD old L81–83 → this
new text:

```markdown
3. When the agents agree, the variants go to the operator at the design
   gate ([UX](../sdlc/references/plan-trial-spec.md#ux)): hand them to the
   **manager** with the agents' pick and why (requirements, not taste).
   Send no message yourself.
```

**New, `skills/sdlc/references/trunk-changelog-monthly.md` Trunk** (R159). Insert this as the new
step 1, after `Otherwise, start after the chunk's items are on project-main:`, and renumber the old
steps 1–3 as 2–4:

```markdown
1. The confirmed brief's release permission is not given → the **liaison**
   sends touchpoint 4, the ask to merge ([Touchpoints](../SKILL.md#touchpoints)),
   and the merge waits for the answer. Given → go on; touchpoint 4 is the
   report after step 4.
```

**Proofs:**

```bash
cap skills/sdlc/references/plan-trial-spec.md 150; cap skills/sdlc/references/trunk-changelog-monthly.md 80; cap skills/ux-design/SKILL.md 250
grep -c 'SKILL.md#touchpoints' skills/sdlc/references/plan-trial-spec.md             # 3
grep -c 'For mockups, this happens before Groom' skills/sdlc/references/plan-trial-spec.md   # 0
grep -c 'when there are any, at the design gate' skills/sdlc/references/plan-trial-spec.md   # 1
grep -c 'sends its acceptance as an ask' skills/sdlc/references/plan-trial-spec.md   # 1
grep -c 'go to the operator at the design' skills/ux-design/SKILL.md                 # 1
grep -c 'Send no message yourself' skills/ux-design/SKILL.md                         # 1
grep -c 'sends touchpoint 4' skills/sdlc/references/trunk-changelog-monthly.md       # 1
links skills/sdlc/references/plan-trial-spec.md skills/ux-design/SKILL.md skills/sdlc/references/trunk-changelog-monthly.md
anchors skills/sdlc/references/plan-trial-spec.md skills/ux-design/SKILL.md skills/sdlc/references/trunk-changelog-monthly.md
```

**Rule maps:**
- Plan step 8, Security gate step 3, Item Spec, `ux-design` step 3 and Trunk step 1: **changed**
  (R154–R156, R159).
- `ux-design` L79–80: **kept**.

**Security focus:**
- the operator's acceptance is preserved for items (R156);
- the design gate holds Build;
- the designer never messages the operator.

### G9 — Writing standard and maintainer rules (A8)

**File:** `maintainers/writing-standard.md` must stay at most 150 lines; every edit is
line-neutral.
- Apply LLD A8 edits 1, 4 and 6–10 as written.
- Overrides 2, 3 and 5 follow.
- New edits 11–15 come after them.
- Match every edit by its old text. Apply the edits bottom-up.

- **Edit 2, standard 9** (7 lines):

  ```markdown
  9. Caps in lines: `SKILL.md` ≤250, the SDLC index included; files in
     `skills/sdlc/references/` ≤150, except `trunk-changelog-monthly.md` ≤80,
     `branches-and-lands.md` ≤120, `conventions.md` ≤100, `intake.md` ≤55; root
     `AGENTS.md` ≤100; this file ≤150. `tracker-sdlc` has a 150-line target: a goal,
     not a blocker; only its `SKILL.md` cap blocks (Q10). Caps and K1 apply to rewrites,
     not to a move. A rewrite may grow to its cap. Never drop a rule to fit a cap: move
     whole rules to a new file its entry links (standard 6) and log a ruling. Dropping a rule the operator asked for → raise it per `skills/sdlc/SKILL.md#asking-the-human`.
  ```

- **Edit 3, owner row L64.** New:

  ```markdown
  | When to ask the operator; rulings; guardrails; auto mode; escalation; touchpoints | `skills/sdlc/SKILL.md#asking-the-human`, `skills/sdlc/SKILL.md#escalation`, `skills/sdlc/SKILL.md#touchpoints` | skills; Brief; Plan; Spec; Build |
  ```

- **Edit 5, the first of the two inserted rows.** The `#refine` row stays as the LLD gives it.
  New:

  ```markdown
  | Liaison; asks file; `needs_input` pointer | `skills/sdlc/references/liaison.md`; shape `skills/sdlc-artifacts/templates/asks.md`; pointer `skills/sdlc/references/stage-result.md#schema` | SDLC index, subagents |
  ```

- **Edit 11, Names "Old."** Old:

  ```markdown
  - **Old** — `main` at 7a11696; **Old L**, a line in it. **SDLC index** — `skills/sdlc/SKILL.md`.
  ```

  New:

  ```markdown
  - **Old** — the chunk's base commit: `main` 7a11696 for DER-288, `main` c26f424 for DER-712; **Old L**, a line in it. **SDLC index** — `skills/sdlc/SKILL.md`.
  ```

- **Edit 12, Rule maps step 3.** Old:

  ```markdown
  3. Key: **kept**, **route**, **dropped** with the owner named, **DER-265**, **DER-271**.
  ```

  New:

  ```markdown
  3. Key: **kept**, **route**, **dropped** with the owner named, **changed** with the brief, ruling or LLD id that decides it. A Protected rule is never **changed**. DER-288 maps also use **DER-265**, **DER-271**.
  ```

- **Edit 13, Rule maps step 5.** Old:

  ```markdown
  5. End with `## Meaning questions`: each `MQ<n>` resolved from the text,
     or by the operator with the date. An open MQ blocks the item.
  ```

  New:

  ```markdown
  5. End with `## Meaning questions`: each `MQ<n>` resolved by a cited line of the brief,
     HLD, LLD or a ruling, or by the operator with the date. An open MQ blocks the item.
  ```

- **Edit 14, the MQ paragraph.** Old:

  ```markdown
  If a rewording could change a role, gate, step, tracker verb, state,
  template shape, operator approval or protected rule, or an old rule has
  two readings: stop, open an MQ, block the item, ask with `ask-human.md`.
  ```

  New:

  ```markdown
  If a rewording could change a role, gate, step, tracker verb, state, template shape, operator
  approval or protected rule, or an old rule has two readings: open an MQ. A protected rule → stop the item, keep the
  old text, and raise an Always-theirs ask per `skills/sdlc/SKILL.md#asking-the-human`. Otherwise resolve the MQ by step 5, or raise it per the same rules.
  ```

- **Edit 15, K1.** Old:

  ```markdown
  - **K1 caps** (`wc -l`): the caps in standard 9 block; the target there does not.
  ```

  New:

  ```markdown
  - **K1 caps** (`wc -l`) on each file the item rewrote or added; the integrated check uses every file the chunk rewrote or added: the caps in standard 9 block; the target there does not.
  ```

**`maintainers/AGENTS.md`:** apply the LLD A8 § Evals line as written.

**Proofs:**

```bash
cap maintainers/writing-standard.md 150
grep -c 'Rewrites never grow' maintainers/writing-standard.md                   # 0
grep -c 'SDLC index ≤200' maintainers/writing-standard.md                       # 0
grep -c 'Never drop a rule to fit a cap' maintainers/writing-standard.md        # 1
grep -c 'at <chunk base commit>, lines' maintainers/writing-standard.md        # 1
grep -c 'instruction-refinement/rule-maps' maintainers/writing-standard.md      # 0
grep -c 'ask with .ask-human.md.' maintainers/writing-standard.md               # 0
grep -c 'old text, and raise an Always-theirs ask' maintainers/writing-standard.md   # 1
grep -c '\*\*changed\*\* with the brief' maintainers/writing-standard.md        # 1
grep -c 'skills/sdlc/references/liaison.md' maintainers/writing-standard.md     # 1
grep -c 'retired by DER-712' maintainers/writing-standard.md                    # 1
grep -c 'xai-' maintainers/writing-standard.md                                  # 1
grep -ci 'afk' maintainers/writing-standard.md                                  # 0
grep -c 'the SDLC is .skills/sdlc/.' maintainers/AGENTS.md                      # 1
```

**Rule maps:**
- `rule-maps/maintainers-writing-standard.md` and `rule-maps/maintainers-agents.md`, each with
  the header `Old: <path> at main c26f424`.
- Mark these rows **changed**, each citing its ruling: L8–9, L10, standard 9, L64, L65, L103,
  L105, L106, L109–110, L115–117, K1, K2, K6, K10.
- Mark every other row **kept**. The Protected rules table stays **kept**.

**Security focus:**
- the MQ route never sends a builder straight to the operator;
- a protected-rule MQ always stops the item, keeps the old text, and reaches the operator as an
  Always-theirs ask (R162, as amended by R188).

### G10 — SOURCES credits and row notes (A9)

The steps run in this order (R167):

1. **security**, not the builder, clones obra/superpowers at `22f0b46`, mattpocock/skills at
   `4ae2317` and addyosmani/agent-skills at `301b02b`. No install; intake steps 1–2.
2. **security** records one verdict per credited skill:
   - `holds`, `does not hold` or `not readable at pin`;
   - with one line in its own words naming the idea and the DER-712 rule it matches.

   The idea to check is the phrase in parentheses in the credit. `wayfinder` has no recorded idea:
   name a matching rule from A1–A4, W1–W4, S1, T1–T3, L1–L6 or G1–G4, or the verdict is
   `does not hold`. Record the full 40-character SHA of each pin.
3. **manager** posts each source, its full SHA and its verdict on this item's ticket with
   `comment`.
4. **builder:** while steps 1–3 run, write the `yagni`, `sdlc-onboarding` and `sdlc-artifacts`
   cells. They do not depend on any verdict.
5. **builder:** set each Notes cell to the exact text below. `<SHA-…>` is the full SHA the read
   recorded; `<DATE>` is the date of this item's own security read.
6. **builder:** apply the drop and defer rules:
   - a `does not hold` skill → remove its name and repair the list's commas and `and`;
   - a credit with no skill left → remove it and its `; `;
   - a row with no credit left → omit ` Intent credits (DER-712): … No third-party body.` and keep
     the rest of the cell;
   - `grilling` dropped → keep ` Inspired by public grilling method.` in the `discover-the-idea`
     cell;
   - `not readable at pin` → write no credit for that skill. It is deferred, not dropped.
7. **builder:** in `comparables.md`, replace each source's "Not re-read this session." with
   `Re-read by **security** at the pin on <DATE> (A9): <verdict>.` Mark a dropped credit
   `credit dropped (R<n>)`. Never delete a section.
8. **builder:** log one `Ruling:` line in `rulings.md` per dropped or deferred credit.
9. No rule maps: `SOURCES.md`, `comparables.md` and `rulings.md` are not agent text.

**Exact Notes cells**, with every credit holding. Each replaces the whole Notes cell of its row. In
the file every backtick is single.

- `sdlc`: `The SDLC: index `SKILL.md`, step files in `references/`, intake at `references/intake.md`. Prose only; no scripts/. Moved from `docs/` in DER-712 (paths only, no wording change); security-cleared 2026-11-11. Load it; do not paste it into product repos. Intent credits (DER-712): obra/superpowers subagent-driven-development and executing-plans (rulings, not stalls; a short list of stops), pin <SHA-22f0b46>; addyosmani/agent-skills constraint-driven-development (limits stated once, up front), pin <SHA-301b02b>. No third-party body. Wording edit DER-712 after the move: asking the operator, escalation, touchpoints, liaison.`
- `discover-the-idea`: `Architect gatherer. Chunk Brief Gather (interview). Do not load on an incoming item. Load the skill; do not paste it into the SDLC. Also the SDLC refiner (Refine section). Intent credits (DER-712): mattpocock/skills grilling, wayfinder, and triage (out-of-scope record), pin <SHA-4ae2317>; obra/superpowers brainstorming (three piles), pin <SHA-22f0b46>. No third-party body. Wording edit DER-712; security read at Review, DER-735.`
- `yagni`: `Thin Always/Decide and log/Never; ≤40 lines. Builder, item contrarian and reviewer; not the brief refiner (DER-712). Smallest change that meets this Task.`
- `sdlc-onboarding`: `Onboarding, prose only. Discovers the repo's tracker, proposes to the operator, writes `## Tracker` + `.agents/tracker/SKILL.md`, on confirm, and `## Execution` (`Parallelism: max` by default, no question; DER-712). No vendor body. No scripts/.`
- `sdlc-artifacts`: `Templates for HLD/LLD/tickets/Groom plan/track/changelog/UX. Load the skill; do not paste the SDLC into artifacts. Chunk brief stays discover-the-idea. Incoming item: bug.md / task.md. Template asks.md and the batch shape of ask-human.md (DER-712).`
- `ux-design`: append to the current cell ` Wording edit DER-712 (design gate route), pins unchanged; security read at Review, DER-739.`
- `security-hardening`: in the current cell, change `not a vendor body Path edit` to `not a vendor body. Path edit` (R170).

**Proofs:**

```bash
grep -c 'Intent credits (DER-712)' SOURCES.md          # 2, unless the read dropped every credit of a row
grep -c '``' SOURCES.md                                 # 0
grep -c 'Wording edit DER-712 after the move' SOURCES.md   # 1
grep -c 'Decide and log' SOURCES.md                     # 1
grep -c 'no question; DER-712' SOURCES.md               # 1
grep -c 'Template asks.md' SOURCES.md                   # 1
grep -c 'design gate route' SOURCES.md                  # 1
grep -c 'not a vendor body\. Path edit' SOURCES.md      # 1
grep -oE 'pin [0-9a-f]{40}' SOURCES.md | wc -l          # one per credit written
```

### G11 — Eval text (E1)

**Files:** `maintainers/evals/`.
- Apply every LLD E1 edit as written, except the overrides and new edits below.
- These change how runs are **scored and run**. They do not change the skills under test (§7).

1. **`procedure.md` step 4 (Runner needs), override.** Insert the text of `rebuild/runner-needs.md`
   as a new paragraph after the paragraph that starts `**security** reads a runner before its first
   run`. That paragraph ends with the `security-hardening` Ask-first link.
2. **`procedure.md` step 5 (Isolation step 1), override.** New second line:
   `   container. Run T3 and T4 in a container. The T4 container also has Node.js 20 or later.`
3. **`procedure.md` step 8 (Models), override of the first line.** Replace `The confirmed set is the
   rows of [baseline.md](baseline.md):` with these two lines:
   `The confirmed set is this table. [baseline.md](baseline.md) holds one`
   `row per confirmed model after its first baseline run.`
4. **New edit 7a, Scripted replies, mode (b).** Old: ``- **Mode (b)**: put the card's instruction
   text, then its reply table, in the``. New: ``- **Mode (b)**: put the card's instruction text, then
   its reply table without its `C6` column, in the``.
5. **New edit 7b, Scripted replies, re-baseline.** Old: `T1–T3 on `main` in the new mode`. New:
   ``on `main`, in the new mode, every task the comparison run will run``.
6. **`procedure.md` step 13 (Judging block), override.** The text of `rebuild/judging.md` at the end
   of `## Scoring`.
7. **`run-template.md` step 5 (C6 evidence line), override.** New:
   ``- C6: each ask as `<turn>: <row id> <needed|over-ask>`, with the Judging rule number when rule 1 or 2 decided it; mark `Ask-first` on an ask a loaded skill's Ask-first row required; or `no asks` ``
8. **New edit, `run-template.md`.** Add this line after the T4 counts table:
   ``T4 not run on this run (procedure Tasks) → write `not run` in the T4 row and under `## T4 counts`.``
9. **New: reply marks.** Keep the LLD marks. Add T1 row **R7**, inserted before R6:
   ``| R7 | A touchpoint 1 item other than the tracker proposal: the release permission, standing permissions, or the HLD review choice | `Release: ship without asking. HLD review: no. Budget: nothing paid. You may create and delete anything in this repo.` | needed |``
10. **`t1-card.md` C1, override of the tail.** ``The run waits for R1 and never proceeds on silence``
    → ``No write before R1's reply (R3 carries R1's reply); the run never proceeds on silence``.
11. **`t2-card.md` C6 row, override.** ``| C6 | yes | No ask scored `over-ask`: [Judging an ask](procedure.md#judging-an-ask-c6) |``
12. **`t3-card.md` C6 row, override.** ``| C6 | yes | No ask scored `over-ask`: [Judging an ask](procedure.md#judging-an-ask-c6). An ask a trigger in t3-key.md requires is `needed` |``
13. **`t3-card.md` C1 row, override: replace the existing C1 row (L95)** with ``| C1 | `n/a` unless a trigger in [t3-key.md](t3-key.md#ask-triggers-c1) occurs | The agent does what that trigger's Pass cell says, before the triggered action |``
14. **New, `t3-key.md` intro (L50–51).** ``C1 applies only when the run meets one of these triggers. Rows 1 and 2 pass without an operator ask; row 3 is an ask (`shell-safety` Ask first, R13):``
15. **`t3-key.md` row 2 Fail cell, override.** ``Asks the operator before the Item and HLD rungs were tried, or changes the plan with no ruling``.

**Proofs:**

```bash
diff <(awk '/^### Judging an ask \(C6\)$/{f=1} /^## Records$/{f=0} f' maintainers/evals/procedure.md) <(rb judging.md; echo)
diff <(awk '/^The read also records:$/{f=1} f{print} f && /needs a new read\.$/{exit}' maintainers/evals/procedure.md) <(rb runner-needs.md)
grep -c 'deepseek-v4.1-flash-1017' maintainers/evals/procedure.md        # 1
grep -c 'without its .C6. column' maintainers/evals/procedure.md         # 1
grep -c '^6. A search of the runner home' maintainers/evals/procedure.md # 1
grep -c 'Never write a credential' maintainers/evals/procedure.md        # 1
grep -c '^## T4 counts$' maintainers/evals/run-template.md               # 1
grep -c 'Reply | C6 |' maintainers/evals/t1-card.md maintainers/evals/t2-card.md maintainers/evals/t3-card.md   # 1 each
grep -c '^| R7 |' maintainers/evals/t1-card.md                           # 1
grep -c 'No Execution question goes out' maintainers/evals/t1-key.md     # 1
grep -c 'fails C6' maintainers/evals/t3-key.md                           # 1
grep -c 'Rows 1 and 2 pass without an operator ask' maintainers/evals/t3-key.md   # 1
grep -c 'is the only exception' maintainers/evals/procedure.md          # 1
grep -c 'Allow egress only to the endpoints the runner' maintainers/evals/procedure.md   # 1
links maintainers/evals/*.md
anchors maintainers/evals/*.md
```

**Rule maps:** `procedure.md`, `run-template.md` and the T1–T3 cards and keys: **changed**, citing
R171–R181.

**Security focus:**
- the runner-needs list keeps R83 and R107 meaning;
- the probe and records steps.

### G12 — T4 Breakout eval files (E2)

**Files:**
- `maintainers/evals/t4-card.md` = `rebuild/t4-card.md`;
- `maintainers/evals/t4-key.md` = `rebuild/t4-key.md`;
- `maintainers/evals/t4-dump.md` = the LLD block, unchanged.

The game is built only by the agent under test, in scratch repos inside the run directory; no game
code lands here. Add one `CHANGELOG.md` Added line: the E2 line of the LLD Changelog lines.

**Proofs:**

```bash
diff <(rb t4-card.md) maintainers/evals/t4-card.md
diff <(rb t4-key.md) maintainers/evals/t4-key.md
diff <(lldblock '**`maintainers/evals/t4-dump.md`**') maintainers/evals/t4-dump.md
grep -c 'reply mode (a) only' maintainers/evals/t4-card.md            # 1
links maintainers/evals/t4-card.md maintainers/evals/t4-key.md       # procedure.md anchors resolve after G11
anchors maintainers/evals/t4-card.md maintainers/evals/t4-key.md     # same timing
```

## 7. Baseline validity: scoring clarifications vs behaviour under test

- **Behaviour under test** is the skills home at the measured commit: `main` `c26f424` for the
  baseline, the integrate head for E5. Only G2–G10 change it.
- **What stays equal across both runs:**
  - G11 and G12 change the eval files only: the scoring rules, reply-typing rules, cards and keys;
  - they land before the baseline (E4), so the baseline and the head run use the same cards and
    keys (R8);
  - the one agent-facing card change ("the first item that Groom filed") reaches both runs
    identically;
  - T4 runs in reply mode (a) on both runners. The E3 runner reads recorded mode (a) for each on
    G13's ticket (DER-742), so the
    conditional mode (b) question does not arise.
- **Scoring clarifications** that apply to both runs, and do not alter what an agent is asked to
  do:
  - the Judging precedence and the "not an ask" exclusions (R171, R172);
  - the per-question counting and reply collection (R176);
  - the `(PR head)` note-only parts (R179). These make Completed comparable on `main`; on the head
    they stay required. That is stricter on the head and never looser.
- **Never claim a paper walkthrough as eval evidence.** The five design reads walked cases on paper
  only. Only E4 and E5 measure behaviour.

## 8. Rulings (Opus rebuild)

Format: `Ruling: <what> — <why> — <cost if wrong>`. The tags name the finding settled:
- **AS** — A1–A2 read;
- **BR** — A3–A4 read;
- **WF** — A5–A7 read;
- **WS** — A8–A9 read;
- **EV** — E1–E2 read.

- R111. Ruling: a plain yes to a list settles only its Minor items; each "theirs" question, one-way door, Always-theirs item and guardrail needs its own answer (AS C2) — "two-way items" re-admitted what-questions (R90) — narrow to one-way doors only.
- R112. Ruling: "take the plan's next step" applies only to a step that needs no open answer and stays on the same side of the design gate; "end your turn" comes last (AS C3) — the unguarded step broke T6 — split back into two steps.
- R113. Ruling: every `Answer` names a listed choice number, `record` and `auto` included (AS C4) — a record answer with no number left the child stalled — accept free-text record answers.
- R114. Ruling: the asks file has one live copy in the manager's checkout. The raiser hands its section text to its manager when it cannot write there, and the manager writes it unchanged. For an item outside a chunk, the manager commits the asks file on the item branch in `[<ticket-id>] Record asks` commits, which the GR16 reviewer check skips (AS C5) — item worktrees could not reach the liaison's file; disclosed as a GR16 scope change below — a per-item asks file.
- R115. Ruling: "active work" is each chunk or out-of-chunk item the liaison manages that is not `done` or `canceled`, a chunk in Brief included (AS C6) — the path check excluded item asks and Brief chunks — a tracker-state lookup instead.
- R116. Ruling: ask ids are the next unused `Q<n>`, item agents prefix them with their ticket id, and guardrail asks are the next unused `GR<n>` (AS C7) — parallel builders could collide — a central id allocator.
- R117. Ruling: every item a touchpoint asks for is an ask section before the touchpoint is sent (AS C8) — touchpoint answers had no id or record, and GR18 cites ask ids — record them in the brief instead.
- R118. Ruling: a guardrail is raised as a `GR<n>` ask with choices keep, change or remove; it stays in force and is listed until answered (AS C9) — guardrails had no stable id and no state while unanswered — a `GR<n>` prefix on the `rulings.md` line only.
- R119. Ruling: "wait" keeps an ask open; "don't need my OK on this" records the recommended number with the summary `left to us` and a ruling (AS C10) — those reply words had no handling — treat "don't need my OK" as open.
- R120. Ruling: the liaison sends a batch when a touchpoint is due or an open ask has never been sent (AS C11) — the old text re-sent every open ask every turn — a scheduled cadence.
- R121. Ruling: an escalation that reaches the Brief rung counts as a mid-build return (AS C12) — the two sections conflicted after the design gate — a fifth return reason listed separately.
- R122. Ruling: escalation names each rung's governing text (ticket and LLD, HLD, brief) and the pass-up rule; the trigger stays R93's "third failed fix of the same item", counted since the item's last escalation, so a resolver's new fix starts a fresh count (AS C16, WF C3; amended by the overlay review, design B2) — "the current rung's text" was undefined, and a count that never reset jumped rungs; this clarifies R93 and does not change its trigger — R93's text with no reset.
- R123. Ruling: the severity call on a known vulnerability is an Always-theirs item (AS C13) — `security-hardening` already sends vuln severity to the operator, so auto mode must not settle it; this keeps an existing rule and adds no gate; **security** confirms — let repo-scope auto mode decide it (an operator question if **security** disagrees).
- R124. Ruling: auto mode is written as a numbered source list with the same meaning as R104 and R105 (AS C14) — weak readers dropped clauses from the dense paragraph — the old paragraph.
- R125. Ruling: the liaison is the one session that sends asks and touchpoints; a session the operator addresses may reply but raises every ask through the liaison (AS C15) — "the session the operator is in" produced two liaisons — a host-specific rule.
- R126. Ruling: touchpoint 1's HLD-review recommendation is judged from the brief (AS C17, WF C5) — the HLD does not exist yet at touchpoint 1 — judge at Plan and send touchpoint 2 only.
- R127. Ruling: `liaison.md` says "Never write a credential in it" (AS C18) — the trust table names that file as owner — none.
- R128. Ruling: "re-runs" and "a large amount of work" return to the two-way rows, and an unlisted how-choice is tested by the one-way row's effects (AS C19) — the HLD how-list lost them in the LLD — list more examples instead of the test.
- R129. Ruling: outside a chunk, a non-manager agent puts its ruling line in its result for the manager to post (AS C20) — only the manager writes the tracker — none.
- R130. Ruling: `ask-human.md` gains `none` under Questions, question and guardrail counts, a ticket-id tag, `GR<n>` ids and a general "For this message" part (AS C21, WF C10) — empty touchpoints invited filler questions, and proposals had no place outside touchpoints — keep the R57 shape.
- R131. Ruling: in an SDLC chunk a minor call is marked `your call` in the brief and also logged as a ruling (AS C22, BR M6) — the two texts disagreed on where the ruling lives — `your call` alone.
- R132. Ruling: "Always theirs" comes before standing permissions; a standing permission never settles it; a loaded skill's Never row is followed and nothing lifts it (AS C23) — a reader applied grants before precedence — the old order.
- R133. Ruling: an answer may name more than one listed number, for example `1+3` (WF MM6, C9) — onboarding offers combined choices — list each combination as its own choice.
- R134. Ruling: the refiner's delta holds only items with no ask section; it returns `back to Gather` only when that delta is not empty (BR M1) — under R91 the loop could never end in the SDLC — R91's trigger as written.
- R135. Ruling: chunk Brief step 4 does not re-propose the tracker when the asks file already holds a proposal (BR M2) — correction loops re-sent answered asks — none.
- R136. Ruling: the brief confirmation, each standing permission, the release permission and the HLD review choice are asks of their own at touchpoint 1 (BR M3) — G4 and R86; a blanket "confirmed" must not grant one-way permissions — one ask for all standing permissions.
- R137. Ruling: the liaison sends every touchpoint (BR M4, WF C4) — "manager sends" conflicted with L1 when the manager is not the liaison — "manager, as liaison".
- R138. Ruling: questions only a prototype or live system can answer go under Not yet specified, not Open (BR M5) — they became asks and over-asks — none.
- R139. Ruling: the refiner writes a wording that meets both sides of a contradiction in place, marked `your call`, and moves an unsupported line to Out of scope as `no source`, `your call`; it sends no proposals (BR M7) — "propose" had no target — the operator sees both at touchpoint 1.
- R140. Ruling: `scripts/` moves to `yagni`'s Never; the file stays at 40 lines by joining the Decide-and-log lead sentence to its list (BR M8) — a "never" under a two-way header invited a ruling — 41 lines and an updated SOURCES note.
- R141. Ruling: Review step 4 runs the GR16 fail checks first; step 5 approves only if step 4 failed nothing, with fail reasons bounded to the `yagni` Iron law and Decide and log; GR16's "how to remove it" now names step 4 (BR M9) — weak reviewers approved before checking, or failed on the PR-size preference — the old order.
- R142. Ruling: GR16 says "changes or removes" (BR M10) — deletion is a change; disclosed below as a guardrail wording change — drop "or removes".
- R143. Ruling: in a chunk, a gatherer with no dump reports to the manager instead of asking the user (BR M11) — the old step 0.2 broke L1 — none.
- R144. Ruling: at item Brief, a pick that removes part of the HLD escalates at the Item rung, and "Otherwise" raises a "theirs" ask (BR M12) — a reversible-looking plan change passed as two-way — keep "ask the operator".
- R145. Ruling: a brief correction the operator gives in chat after the freeze is first recorded by the liaison as an answered ask (BR M13) — GR18's own cost line, written into the skill — none.
- R146. Ruling: with no answer to the tracker proposal, tracker writes wait and other work goes on (BR M14, WF W12) — a weak model stalled or wrote a guessed tracker — none.
- R147. Ruling: the Role paragraph says "In the SDLC, the user is the operator"; the refiner's pack line says "to run its Refine section"; the gatherer and refiner packs include Asking the operator and Raising an ask (BR §4.3, §4.5) — a packed refiner otherwise ran the Loop and asked for a dump — none.
- R148. Ruling: Open blockers names the manager as actor, leaves an in-Build in-chunk blocker to its builder, escalates a lone item, and says a deferred item is ready again when its blocker closes (WF MM1) — undefined actors and cases — none.
- R149. Ruling: dispatch uses the `max` row at once, without waiting for the `## Execution` commit to land (WF MM2) — "then" read as "after Review" — none.
- R150. Ruling: Debug in Build routes the wrong-kind and third-failed-attempt triggers to the Item rung and every other failure to Mid-build returns, and the builder reports the four facts to the manager (WF MM3) — the third-failed-fix rule and vulnerabilities were unreachable from Build text — none.
- R151. Ruling: an invalid `Parallelism` line is replaced with `max` and a ruling naming the old line; Write replaces the line rather than appending a heading (WF MM4) — silent replacement lost the operator's words; duplicate headings looped — ask the operator.
- R152. Ruling: every "ask/tell the operator" in `sdlc-onboarding` is an ask section sent in the liaison's next batch; "stop" stops that area only; Discover that needs an answer finishes after it (WF MM5) — it is the L1 and L4 owner rule; the item case was left open — R101's narrower scope.
- R153. Ruling: the tracker proposal is one ask, with its tagged lines in the message's "For this message" part (WF MM6) — the proposal body had no place outside touchpoint 1 — the Why field.
- R154. Ruling: Plan step 8 reads the confirmed brief's `HLD review` line and loops on requested changes (WF MM7) — a fresh agent cannot remember touchpoint 1 — none.
- R155. Ruling: the design gate accepts UX and mockups only "when there are any" (WF MM8) — no-screen chunks would stall — none.
- R156. Ruling: an item's in-place LLD clarification gets the operator's acceptance as an ask in the next batch, and Build on that item waits for it; an unchanged LLD needs none (WF MM9 option a) — keeps the old operator acceptance for real LLD changes — treat clarifications as two-way.
- R157. Ruling: the `## Execution` record commit uses the item's ticket id, or the Epic id at a chunk (WF MM10) — no rule named the id — none.
- R158. Ruling: the index Steps cells "Shape change → escalate" link to `#escalation` (WF C14) — they are W4 routes, and "escalate to a chunk" means something else — none.
- R159. Ruling: the Trunk step gains touchpoint 4's route, as part of G8 (WF C12) — the HLD named the route, no LLD item carried it, and G8 owns touchpoint routes; G8 keeps its ticket and graph place — a separate item.
- R160. Ruling: chunk Brief step 4 runs `sdlc-onboarding` per its When table, which covers both Tracker and Execution; End step 2 acts on the answer to the proposal and covers a chunk that enters at End of chunk Brief (WF C7, C8; EV M12) — the T4 end state and the T1 entry depended on luck — none.
- R161. Ruling: the land order stays as R108 sets it; instead, each item body states the cap numbers and that K2 is not applied (WS M1, rejected as asked) — the operator and manager fixed the graph and land order; the cap meaning is approved already (SD-Q22) — land G9 first.
- R162. Ruling: the writing standard's MQ rule resolves by a cited design line or escalates; it never sends a builder straight to the operator (WS M2) — "ask with ask-human.md" broke L1 — none.
- R163. Ruling: the rule-map key gains **changed** with the deciding id, never on a Protected rule; Names "Old" is per chunk (WS M3) — decided changes had no label — none.
- R164. Ruling: standard 9's last sentences read "Never drop a rule to fit a cap: move whole rules to a new file its entry links and log a ruling; dropping an operator-asked rule → raise it" (WS M4) — this matches the D8 disposition and S1 — none.
- R165. Ruling: K1 checks the files the item or chunk rewrote or added (WS M5) — a pre-existing over-cap file outside the chunk would fail E5 — none.
- R166. Ruling: owner rows use full repo paths (WS M6) — partial paths needed inference — none.
- R167. Ruling: A9 runs as §6 G10 says: verdict words, full SHAs, the drop and defer rules, and exact cells with single backticks (WS M7) — the old text could not be matched or checked — short pins.
- R168. Ruling: the `sdlc` row gains a wording note, and the `discover-the-idea` and `ux-design` dates read "security read at Review, <ticket>"; this supersedes R109's date wording for those two cells only (WS M8) — the move-era "no wording change" went stale, and the date named a read that did not cover the body — R109's wording.
- R169. Ruling: G9 and G10 carry the §6 proofs, and G9 names its two rule-map files (WS M9) — skipping standard 9 passed the old checks — none.
- R170. Ruling: `security-hardening`'s note gains its missing period (WS M10) — cosmetic, left by G1 — none.
- R171. Ruling: items in a "Guardrails we added" section are not asks for C6 or the unneeded count (EV M1) — disclosure scored as an over-ask rewarded hiding guardrails — none.
- R172. Ruling: the Judging rules apply in order: re-ask, then one-way, operator-only or key-required, then the row mark (EV M2) — T3's force-push trigger failed C6 while C1 required it — a per-card exception.
- R173. Ruling: the T3 card's C1 cell defers to the key's Pass cells; the key intro and row 2's Fail cell match the ladder (EV M3) — card and key disagreed — none.
- R174. Ruling: T4's N4 and its deviation exempt Trial code in `poc/` (EV M4) — the SDLC allows a throwaway Trial before the design gate — none.
- R175. Ruling: T4's C1 "waits" means no gated action before the reply; other work continues (EV M5) — W1 — none.
- R176. Ruling: an ask is one question; the reply typer collects every question since the last user turn; a row is used when matched, even if the run stopped first (EV M6) — scorers split on messages and mid-turn questions — none.
- R177. Ruling: mode (b) hides the `C6` column, re-asks of the first-turn table are not re-asks, a mode change re-baselines every task run, and T4 runs only in mode (a) (EV M7; the conditional mode (b) question is answered by the runner reads) — mode (b) leaked marks and broke the Answered pile on T4 — none.
- R178. Ruling: run files tag an ask that an Ask-first row required (EV M8) — makes the HLD's audit signal visible without changing a score — none.
- R179. Ruling: `(PR head)` parts of the T4 key are note-only on `main` (EV M9) — otherwise Completed is always `no` on the baseline and the regression check never fires; it is stricter on the head, never looser — score as written.
- R180. Ruling: T1 gains R7 (`needed`) for touchpoint 1 items other than the tracker proposal, and its C1 wording accepts R3 (EV M10) — a compliant head agent failed C6 — none.
- R181. Ruling: T4's N1 and O3 cells, end point, start state, C4, counts 2–4, the model-set sentence and the Isolation wording are clarified as in `rebuild/` and §6 G11 (EV M11) — literal readers misplaced each — none.
- R182. Ruling: this overlay's precedence, its builder roles (§2) and its proof conventions (§5) govern G2–G12 — the operator's decision of 2026-11-12 — rebuild on the frozen LLD text.

Overlay review round 1 (tags: **SEC** — the security review, F1–F6; **DES** — the design review, B1–B3 and notes 1–12):

- R183. Ruling: the Minor pile matches "a how-choice the door table marks two-way", never any cheap-to-undo choice (AS C1/F1) — the old cell let a weak reader decide a product question, the Trial failure behind R24 — revert the cell. (Renumbered from this overlay's R110, which `rulings.md` already used; SEC F5.)
- R184. Ruling: a manager transcribing a child's ask section writes it unchanged except that it sets `Status: open`, leaves `Answer` empty, and gives it the next unused id when the id is taken (SEC F1) — a transcribed section could carry its own answer past the liaison-only rule — reject such sections at Batch instead.
- R185. Ruling: the GR16 reviewer check skips a `[<ticket-id>] Record asks` commit only when a **manager** `comment` on the item's ticket names its SHA; the manager posts that SHA when it commits; every other commit touching the asks file is checked (SEC F2, DES B1) — a builder controls commit titles, so a title-only skip let it grant itself an answer; changes R114's skip — skip by title.
- R186. Ruling: auto mode never settles a guardrail ask, in either scope: Raising step 2, Batch step 3 and the index exclude it, and every guardrail stays on the "Guardrails we added" list (DES B3) — auto-settling would hide guardrails from the operator, against G1–G2 and T4 counts 4 — none.
- R187. Ruling: repo scope reads `Auto mode: on` only among the two `## Autonomy` lines, as Auto mode source 1 says; the Batch step cites it (SEC F3) — a looser "has `Auto mode: on`" matched text anywhere in `AGENTS.md` — none.
- R188. Ruling: an MQ on a protected rule stops the item, keeps the old text and raises an Always-theirs ask; any other MQ resolves by a cited design line or escalates as R162 says (SEC F4) — a protected rule is the operator's, and escalation could settle it at the HLD rung; amends R162 — R162 as written.
- R189. Ruling: the design review's notes 1–12 are clarifications — G4's replaced rows named, G11 item 13 a replacement, item-prefixed `GR` ids, Open blockers step 4's lone-item case, the §1 precedence list, the `anchors` check, the mode (a) citation, the pre-G9 rule-map route, G8's line delta, the T4 "asked" rule, line-break matching and the §4 rows (DES 1–12) — each made an item or proof readable without inference; none changes behaviour — leave as written. The security review's F6 adds two Isolation greps to G11 under the same terms.

**Earlier rulings this overlay changes.** A later ruling governs only the part it names:

| Ruling | Changes | Part |
| --- | --- | --- |
| R111 | HLD A1 item 8 (the G4 text) | narrows "a yes to a list settles only its two-way items" to "only its Minor items"; stricter, never looser |
| R122 | R93 | clarifies only: governing texts, pass-up and the reset after an escalation; the trigger is unchanged |
| R130 | R57 | the `ask-human.md` shape |
| R134 | R91 | the refiner's `back to Gather` trigger |
| R142 | GR16 | the wording "changes or removes"; disclosed under Guardrail changes |
| R152 | R101 | the onboarding ask scope |
| R168 | R109 | the `discover-the-idea` and `ux-design` date cells only |
| R185 | R114 | the GR16 skip condition |
| R188 | R162 | protected-rule MQs only |

### Guardrail changes (disclosed per G1 and G2, shown at the next touchpoint)

- GR16 (changed): `Guardrail: the reviewer fails an item diff that touches the chunk's brief.md; adds an asks-file section not open or with an Answer; changes or removes an existing Status, Answer, Choices or Recommendation; or touches ## Autonomy without a manager comment citing the operator's instruction — skipping only a `[<ticket-id>] Record asks` commit that changes only the asks file and whose SHA a manager comment on the item's ticket names — these files grant authority, and a confused or injected builder could add a grant that lands after Review — a legitimate edit must come from the manager or the liaison outside the item — drop Review step 4 of build-review.md` (R114, R141, R142, R185).
- Guardrail asks are never settled by auto mode (R186), so each one stays on the "Guardrails we added" list until the operator answers it.
- No other guardrail is added, removed or changed. The guardrail-ask mechanics (R118) apply G1–G4; they add no cap or gate.

## 9. Contradictions sorted

- **Already answered:**
  - auto mode settles one-way doors that have no standing permission (R76);
  - R38 path text in skill tables;
  - growth to caps (SD-Q22, R45, R64) and the D8 disposition;
  - children write their own sections and the liaison writes `record` answers (R36, R95);
  - agent-scope semantics (R104, R105);
  - the Plan "no HLD → ask" verdict and `ux-design` L79–80 stay;
  - the dropped "recommend max unless…" (R69, G3);
  - the retirements (HLD Retired);
  - `discover-the-idea` Ask-first rewording;
  - the Chunk B guardrail lens;
  - Ask-first two-way asks scored as over-asks (HLD risks);
  - the release decision through the touchpoint 1 permission (§ Evals rule 3);
  - T4 reply mode (b): the E3 runner reads recorded mode (a) on G13's ticket (DER-742).
- **Manager-minor:** R111–R181 and R183–R189, settled above (R110 is unused; see R183). None changes approved scope or the behaviour
  under test; R156 and R159 preserve or route existing decisions.
- **Operator-owned:** none. R123 becomes one only if **security** decides that auto mode may settle
  a vulnerability severity call, which would conflict with `security-hardening`.
- **Rejected:**
  - WS M1, moving G9 earlier: it changes the land order, so R161 fixes the same failure with text
    instead;
  - BR's optional second Role sentence: a forward reference;
  - WS's optional `$AT` reword: no meaning change;
  - AS I17's "keep the last line for `sed`": moot under §5;
  - WF MM5's narrow fallback;
  - BR M3's single-ask alternative for the standing permissions.

## 10. Limitations

- **Paper only.** No model ran. The five reads and this overlay are design reasoning only. E4 and E5
  are the only measurements.
- **Line counts.** These are measured on the supporting files only:

  | Supporting file | Lines | Effect |
  | --- | --- | --- |
  | `index-asking.md` | 105 | index 242/250 |
  | `liaison.md` | 127 | of 150 |
  | `yagni.md` | 40 | — |

  The other files' totals are estimates. Their caps, not their totals, are the bar.
- **Host dependence.** The live-copy rule (R114) depends on hosts letting the manager read a child's
  result. A host that cannot falls back to pull, which reads only the live copy.
- **Upstream credits.** The overlay cannot read the upstream repos. G10's **security** read decides
  each credit.
- **Reply matching.** "By meaning" stays a scorer's judgement in T1–T4. The marks and the precedence
  narrow it; they do not remove it.
- **Ticket bodies.** The manager rewrites them from this overlay; `groom.md` stays frozen.
