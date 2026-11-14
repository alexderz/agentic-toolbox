# Spec review: design

Reviewer: design reviewer (Grok 4.7, cross-model, fresh session, resumed per round).

## Round 1

Commit: `a0fcc5e`

### Verdict

**Changes needed.** The Decided rows, the gate answers (SD-Q17 through SD-Q22, Breakout, auto-ship, the move), and the later list are placed: A0–A9 and E1–E5 build the first set, and Chunks B–D stay in the HLD later table. Old quotes checked against the repo match, including `docs/SDLC.md`, `docs/sdlc/entry-brief-repo.md`, `build-review.md`, `stage-result.md`, `plan-trial-spec.md` (148 lines), `skills/sdlc-onboarding/SKILL.md`, `skills/ux-design/SKILL.md`, `maintainers/evals/t1-key.md`, `t3-key.md`, and `procedure.md`. The A0 path rules cover the links that are actually in the tree. The holes are contradictions in the new text, one check that fails as written, and a few rules a builder cannot apply as a condition.

### Findings

1. **Blocking.** A minted gatherer still messages the operator. Brief L1 (`brief.md:50`) says child sessions never ask the operator. `docs/sdlc/subagents.md:101-102` mints the gatherer. `lld.md:667-683` still says "Ask the remaining frontier in one round" and shows a question script. Confirmation was split (`lld.md:740-742`); question rounds were not. **Fix:** in an SDLC chunk, the gatherer writes only "theirs" questions into the asks file (or its stage result) and sends no operator message. Outside the SDLC, that session is the liaison and sends `ask-human.md`.

2. **Blocking.** Tracker Write still runs before the operator answers. `skills/sdlc-onboarding/SKILL.md:38-39` says a failed Check runs Discover, Propose, and Write before the calling step continues. A6 (`lld.md:936-940`) changes only the phrase "get both areas' answers" and says "No other change." Chunk Brief (`lld.md:570-571` and `596-598`) runs Propose at step 4 and Write only after touchpoint 1. **Fix:** change that When sentence so Tracker Write runs after the touchpoint 1 answer, and so step 4 stops at Propose.

3. **Blocking.** A blanket yes settles two different sets. Brief contradiction 13 (`brief.md:202-208`) and the index (`lld.md:286-288`) settle only two-way items, each logged as a ruling. `lld.md:493` settles "the other items," which on a "theirs" list are what-questions (goal, scope, taste). Writing standard 5 (`maintainers/writing-standard.md:37-39`) allows one owner. **Fix:** delete the settlement sentence from `ask-human.md` and point at the index. A what-question stays open until its own answer.

4. **Blocking.** The refiner's verdict is not a condition. `lld.md:770-771` says return `buildable` or `back to Gather` with contradictions, deferrals, drops, and "theirs" questions, and does not say when. Chunk Brief branches on that word (`lld.md:568-571`). S1 (`brief.md:43`) keeps Later in the brief. Sending every deferral back to Gather never reaches `buildable`. Standard 2 is `maintainers/writing-standard.md:31-33`. **Fix:** `back to Gather` only when a contradiction has no wording that meets both sides, or a drop of an operator-asked requirement has no answer yet. Later stays in the brief. "Theirs" questions go in the touchpoint 1 batch.

5. **Blocking.** K6 fails on the required template edit, and the LLD still requires it. `maintainers/writing-standard.md:136-138` says every template's heading and bold-field outline is unchanged. A2 replaces `ask-human.md` (`lld.md:479-514`) and adds `asks.md`. Verify runs K1–K10 (`lld.md:1509-1511`; `maintainers/writing-standard.md:150`). The brief answers the meaning question; it does not change K6. **Fix:** exempt `ask-human.md` and `asks.md` from that outline check, and record the shape change as a resolved MQ in the rule map.

6. **Should fix.** The ladder starts when a level "cannot meet" a need (`lld.md:319-320`). The change map (`brief.md:66`) replaces "three failed fixes" and "open blocker" with checkable conditions (`maintainers/writing-standard.md:31-33`). **Fix:** name the triggers: the third failed fix of the same item; an out-of-chunk blocker with no unblocked item left (A5 already says this); a shape change the current rung's text does not allow.

7. **Should fix.** Brief L3 (`brief.md:52`) says the child writes the asks file, then notifies. `rulings.md:50` (R36) and `lld.md:397-401` say role agents never write it and the manager writes every field except the answer. **Fix:** the child writes its own ask section (id already unique). The liaison stays the only writer of `Status` and `Answer`.

8. **Should fix.** SD-Q22 granted growth up to the caps (`brief.md:385-386`, `brief.md:400-401`). R45 and `lld.md:1035-1036` also drop the ask when a rewrite needs a new file past the cap. **Fix:** growth up to the cap stands. A file that does not fit the cap is still an operator ask.

9. **Should fix.** GR13 (`rulings.md:104`) adds a 4-hour hold. G3 (`brief.md:57`) allows an unrequested guardrail only for an A2 one-way door (`brief.md:36`: lost data, money, publish or send, credentials, delete what others use, production deploy). A wall-clock limit is a limit value, which the door table already tells the agent to decide and log as a ruling (R41). **Fix:** delete GR13. Keep the 4-hour number as R41, a ruling on a limit, inside the procedure's existing stop rule.

10. **Should fix.** The HLD leaves "interrupting or restarting something in use" for Spec to decide and log (`hld.md:415-419`). The held-out note says the how-list is too broad there (`brief.md:224-225`). The door table makes "order and timing of runs and steps" two-way (`lld.md:256`) and logs no ruling. **Fix:** add the ruling and the row. Put "interrupt or restart something others are using" on the one-way row.

11. **Should fix.** The new message shape uses letters (`lld.md:489`, `lld.md:513`). Onboarding still offers 1, 2, and 3 (`skills/sdlc-onboarding/SKILL.md:112-114`). The T1 key still requires choices 1/2/3 (`maintainers/evals/t1-key.md:15`). T4's N3 reply is `1 — use as listed` (`lld.md:1302`). **Fix:** keep 1/2/3 in `ask-human.md`. The current template, the tracker proposal, and the T1 key already use them.

12. **Should fix.** G1 (`brief.md:55`) says a read-only restriction is written as a `Guardrail:` line. R49 (`rulings.md:63`) says agents read only the `Auto mode:` and `Production:` lines, and the trust-boundary table repeats it (`lld.md:1492`), with no Guardrail line. It protects a one-way door (text in that section steering an auto decision), so G3 allows it once it is logged in that form. **Fix:** add the Guardrail line beside GR14, including how to remove it (read the whole section).

13. **Note.** `git mv` does not create missing directories. A0 steps 1–3 (`lld.md:52-54`) need `mkdir -p skills/sdlc/references` first.

14. **Note.** `lld.md:621` says entry-brief-repo ends at 140 lines (134+4+1+1). The new Refine block is 13 lines against 8 (`lld.md:564-576`), so the sum is 141. The cap is 150.

15. **Note.** The operator kept GR12 (`brief.md:410`). The design rulings do not mention it. Add one line that the chunk's own runtime limits stay, or that they ended with the crawl.

16. **Note.** Brief verify-later (`brief.md:337`) says no "headless" wording left. `skills/sdlc-onboarding/SKILL.md:126` still says a headless agent can hang on pinentry. The verify grep (`lld.md:1517`) does not scan that file.

### Simpler shape

Keep every condition in the index. `liaison.md` stays the procedure, because the index is already 249 of 250 (`lld.md:345-348`). `ask-human.md`, `discover-the-idea`, and onboarding keep a route line and no second settlement, ask, or Write rule. That removes findings 1–3 and the duplicated blanket-yes sentence, and it leaves the move, the evals, and the door table as they are.

## Round 2

Commit: `da9e613`

### Verdict

changes needed

### Round-1 findings

| ID | Status | Evidence |
| --- | --- | --- |
| D1 | resolved | In an SDLC chunk the gatherer writes each "theirs" question as an ask section and sends no message (`lld.md:721-724`, R88). |
| D2 | resolved | A failed Check runs Discover and Propose; the Tracker Write waits for the touchpoint 1 answer (`lld.md:1013-1017`, `1032-1035`, R89). |
| D3 | resolved | `ask-human.md` has no blanket-yes sentence. Settlement stays in the index Answers rule (`lld.md:307-309`, `544-545`, R90). |
| D4 | resolved | `back to Gather` only when a contradiction has no wording that meets both sides, or a drop of an operator-asked requirement has no answer yet (`lld.md:820-824`, R91). |
| D5 | resolved | K6 exempts `ask-human.md` and `asks.md`; the shape change is MQ1 (`lld.md:548-550`, `1143`, R92). |
| D6 | resolved | Escalation triggers are the third failed fix, an out-of-chunk blocker with nothing left unblocked, and a shape change the rung's text does not allow (`lld.md:337-338`, R93). |
| D7 | resolved | The raising agent writes every field except `Answer`, with `Status: open`. Only the liaison writes `Status` and `Answer` (`lld.md:417-419`, `496-498`, R36, R95). |
| D8 | rejected by the manager | R45 stands: grow to the cap, and add a file where the cap would force dropping a rule (`lld.md:1119-1120`, `rulings.md:119`). |
| D9 | resolved | GR13 is deleted. The 4-hour T4 cap stays ruling R41 (`lld.md:1673-1674`, `rulings.md:55`, `133`). |
| D10 | resolved | "Deletes, interrupts or restarts what others use" is on the one-way row. HLD Open is none (`lld.md:273`, `hld.md:439-441`, R94). |
| D11 | resolved | Choices stay **1 / 2 / 3** (`lld.md:522`, `545`). |
| D12 | resolved | GR19: agents read only the `Auto mode:` and `Production:` lines (`lld.md:324-326`, `1681`, `rulings.md:139`). |
| D13 | resolved | A0 step 0 is `mkdir -p skills/sdlc/references` (`lld.md:52`). |
| D14 | resolved | Entry-brief arithmetic is 134 + 5 + 4 + 1 = 144 of 150 (`lld.md:661-662`). The asking block is 109 lines (`lld.md:253-361`) and the index check is 246 (`lld.md:364-367`). `yagni` is 40 (`lld.md:838-877`). |
| D15 | resolved | GR12 stays; limits live in the job settings (`rulings.md:118`, `132`, R98). |
| D16 | resolved | "Headless agent" becomes "an agent with no terminal", and the verify grep includes `skills/sdlc-onboarding` (`lld.md:1050-1052`, `1635`, R97). |

### New findings

1. **Blocking.** In an SDLC chunk the gatherer files its asks and then ends the turn, so the brief is never written. Frontier step 2 sends no message, and step 3 is unconditional: "None left → end the turn" (`lld.md:721-731`). The brief file is still loop step 5, after that wait (`skills/discover-the-idea/SKILL.md:97-114`, `lld.md:786-792`). The new cap stops only when the frontier holds no "theirs" question (`lld.md:749-750`), and those questions stay open until touchpoint 1. Nothing resumes the gatherer. **Fix:** in an SDLC chunk, once the ask sections are written, go straight to the brief. Keep the wait and the next round for outside the SDLC only.

2. **Should fix.** An Always-theirs item can still be closed from earlier words. Batch step 2 writes `Answer: record — <where>` when the record or earlier words answer the ask (`lld.md:441-442`). Raising step 1 says the same and then applies it (`lld.md:471-473`). Always-theirs says only the operator's own answer to that item settles it (`lld.md:293-297`, R75). Batch step 3 already skips those items for auto mode (`lld.md:443-446`, R76). **Fix:** the same skip on Batch step 2 and Raising step 1.

3. **Should fix.** Onboarding Discover still messages the operator in the middle of chunk Brief. Steps 2 and 4 still say "ask the operator" and "tell the operator" (`skills/sdlc-onboarding/SKILL.md:88-92`). Round 2 routes only Tracker Propose into touchpoint 1 (`lld.md:1032-1035`) and leaves Discover as it is. A missing tracker or a failed access read sends a message before the one touchpoint 1 batch. **Fix:** those two Discover lines write an ask section and go out in that same batch.

4. **Note.** The `build-review.md` result line adds 3 lines for the Review edit and lands on 105 (`lld.md:915-916`). The quoted replacement is 3 lines to 7 (`lld.md:897-912`), which is +4, so the file is 106. The cap is 150, and there is no `wc -l` check. **Fix:** state +4 and 106.

## Round 3

Commit: `c3f2328`

### Verdict

changes needed

### Round-2 findings

| ID | Status | Evidence |
| --- | --- | --- |
| N1 | resolved | In an SDLC chunk the gatherer writes the asks, then the brief, and does not wait or run another round (`lld.md:730-745`, R100). |
| N2 | resolved | Batch step 2 and Raising step 1 skip the record for an Always-theirs item (`lld.md:445-447`, `478-481`). A ruling settles only a two-way question (`lld.md:297-298`, R99). |
| N3 | resolved | At end of chunk Brief, Discover's "ask the operator" and "tell the operator" lines (steps 1.4, 2, and 4) become ask sections in the touchpoint 1 batch (`lld.md:1040-1048`, R101). |
| N4 | resolved | Review steps 4–5 are 3 lines replaced by 9. The file check is 108 (`lld.md:919-932`). |

### New finding

1. **Should fix.** A one-way door the brief already allows is sent to the operator anyway. Standing permissions need no ask (`lld.md:282-285`), and the Theirs row asks only for a one-way door with no standing permission (`lld.md:306`). Batch step 2 and Raising step 1 skip the record for every one-way door, and the next numbered step writes or sends the ask (`lld.md:445-447`, `478-482`, `452-454`). **Fix:** keep the skip for Always-theirs items. For a one-way door, apply a standing permission and stop. The index sentence that keeps `rulings.md` off one-way doors stays (`lld.md:297-298`).

## Round 4

Commit: `88e51eb`

### Verdict

meets requirements

The finding is resolved. Batch step 2 settles a permitted one-way door as `Answer: record — standing permission <where>` and does not send it (`lld.md:445-448`). Raising step 1 applies that permission and stops (`lld.md:480-482`). Always-theirs items still skip the record. `rulings.md` still never settles a one-way door, and the index standing-permission and Always-theirs lines are unchanged. No new problem.
