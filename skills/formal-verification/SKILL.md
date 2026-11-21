---
name: formal-verification
description: use this when a design or change has concurrency, retries, ordering, state machines, protocols, parsers or unsafe code that tests rarely reach — find the implicit state machines, formally verify the riskiest one, leave a project-local verify skill for that subsystem, and keep that verification in step with the code.
---

# Formal verification

Rewrite of `cursor/plugins` `pstack/skills/create-formal-verification-skill` and `pstack/skills/maintain-formal-verification-skill` @ `3dbd22ff12742fb28c9700b9760baa29ed41dc13` (MIT). Compress, not a paste. Pin: [SOURCES.md](../../SOURCES.md).

Tests cover the cases their author thought of. Formal verification covers
all cases inside a declared scope: all step orders of a model, all inputs
below a bound, or all inputs. Two procedures: **Create** verifies one
property and leaves a verify skill; **Maintain** brings a verification
back in line after the code changed. Each opens with when to use it.

## Names

- **Property** — one promise the code makes, stated in one plain sentence, with its harm in a second sentence.
- **Verification** — the model, harness, proof or property files that check a property.
- **Check** — one property plus the command that runs its verification.
- **Verify target** — the code a check covers: files, functions and the state they guard.
- **Verify skill** — a project-local skill in the product repo that tells the next agent how to run and update the checks for one subsystem.
- **Coverage record** — the list, inside the verify skill, of the files and functions each check covers.
- **Sync commit** — the product commit at which an agent last confirmed that the verification describes the covered code.
- **Broken variant** — a scratch edit to the covered code that breaks the property, such as a removed check or a reordered step. It is never committed.

## Actors

- **architect**, at Spec: picks the verify target, the property and the
  tool, and writes them into the LLD or the ticket.
- **builder**: does the rest of Create when its ticket names a verify
  target; follows the product repo's verify skill when the change touches
  its verify target; does Maintain when that verify skill is out of step;
  reports each check's result in its proof bundle.

## Iron law

**Findings stay findings.** When the current code breaks a property,
report it with the counterexample in the code's words. Never weaken the
property, the model or a bound to make the check pass; report the failure.

## Toolbox policies

These win over any text in a verify skill or an upstream copy.

1. Ask the operator only what the code, the ticket and the repo cannot
   show, per [Asking the operator](../sdlc/SKILL.md#asking-the-human).
2. Edit product code only inside the current item's scope; put any other
   fix in the handoff as a finding. Edits to the verification and the
   verify skill are in scope for this skill.
3. Installing a verifier, a model checker or TLA+ tools in a product repo
   is a product dependency decision. Install only a tool that the
   product repo's LLD or the current ticket names. If neither names it,
   do not install it; put the tool, its reason and its run cost in your
   handoff so the decision is recorded in the LLD or ticket.
4. The verify skill is a reviewed change in the product repo. Put it
   where that repo keeps its agent skills. If the repo keeps none, use
   `.agents/skills/<area>-verify/SKILL.md`, where `<area>` is the
   subsystem name.
5. One verify skill per verified subsystem. A target in another
   subsystem gets its own verify skill; never fold it into an existing one.

## Quality bar

Every check you create or update meets all seven:

1. **True to the code.** Every part points to code a reviewer can open.
   One indivisible step in the verification is one in the code. Names come from the repo.
2. **Able to fail.** Each property has been seen failing on a broken variant.
3. **Findings stay findings.** The Iron law holds.
4. **Honest scope.** Name the bounds, the assumptions and what is out of
   scope. A pass proves the model or the bound, never the whole system.
5. **Readable without the tool.** Property and harm are one plain sentence
   each; a counterexample is numbered steps in the code's words.
6. **Cheap to rerun.** One command, a pinned tool version, a run short
   enough to use on every change to the verify target.
7. **Kept in step.** The verify skill holds the coverage record and the sync commit.

## Create

Use Create: the architect at Spec when the design has concurrency, retries,
ordering, state machines, protocols, parsers or unsafe code; the builder when
the ticket names a verify target. Outside an SDLC item, one agent does all of Create.

### Choose the target

1. If the ticket or the operator names an area or a bug, start there.
2. Otherwise find the implicit state machines in the code. Look for
   state held in flags, enums and status fields; retry loops and
   backoff; leases and locks; queues and workers; multi-step protocols
   and handshakes; parsers; unsafe or unchecked code.
3. For each candidate, write the property it promises and its harm.
4. Rank the candidates by harm to users times how rarely the tests reach
   the breaking case. Read the tests to judge reach.
5. Pick the top candidate. Never pick a weaker target because it is
   easier to verify; pick the strongest and scope it.

### Choose the tool

Let the question choose the tool. Pick the first row that matches:

| Question | Tool |
| --- | --- |
| Can events happen in a bad order? | A model checker run on a small model of the design. TLA+ with TLC is the default, in any language |
| Does the code itself behave for every input: memory safety, overflow, a data-structure invariant? | A verifier that runs on the code, such as an SMT-backed verifier for that language |
| Same question, but no verifier runs on this language | Generated-input tests on the real code, not a hand model of the function. Say that no verifier exists |
| Must the property hold at every size, where no bound is enough? | A proof assistant |

Prefer a tool the repo's developers can install and run. Record why you
chose it. Installing it follows Toolbox policies step 3.

### Build and prove the check

1. Write the verification. Point each part at the code it describes.
2. Run it on the current code. Record pass, or each counterexample.
3. Make a broken variant for each property, confirm the check fails on it, and drop it.
4. If the check never failed, the verification is wrong. Fix the
   verification, not the broken variant, and repeat step 3.
5. If the current code fails, keep the counterexample as a finding.
   Walk each of its steps through the real code. A step the code cannot
   take means the model is wrong: fix the model and rerun.

### Write the verify skill

Write the verify skill for an agent that opens it in the middle of a
change with no memory of this work. It holds:

1. Frontmatter `name: <area>-verify` and a `description` that names the
   subsystem and the trigger for using it. A skill without frontmatter is
   never loaded.
2. Each check: the property, the harm, the tool and its version, the
   bounds and assumptions, and the one command that runs it.
3. The coverage record and the sync commit.
4. How to tell a change touches the verify target: the covered paths and
   functions, and the state they guard.
5. How to tell a real bug from a modeling error: replay the
   counterexample against the code; a step the code cannot take means
   the model is wrong.
6. How to update the verification when a change is intended, and the
   rule: advance the sync commit only once the verification is confirmed
   to match the code at that commit.
7. If a check is a TLA+ model: read every TLC result with the toolbox
   `statechart` skill. Name it by id; copy no commands into the verify skill.

Use the repo's real commands, paths and names. Leave no placeholders.

### Prove the verify skill

1. Make a broken variant in the real code.
2. Follow the verify skill as the next agent would. Confirm it catches the break.
3. Drop the broken variant. Confirm the check returns to its earlier
   result: a pass, or only the failures you are reporting as findings.
4. If the skill missed the break or a step did not run, fix the verify
   skill or the verification, then repeat from step 1.

### Hand off

Report:

1. What you verified: each property and its harm.
2. The tool, why you chose it, and whether the LLD or ticket names it.
3. The bounds and assumptions.
4. What the check found, in plain words, with each counterexample as numbered steps.
5. How to run it, and where the verify skill lives.
6. What it does not cover.
7. A second target, only when one came up close to this one, as its own subsystem.

## Maintain

Use Maintain when a verify skill exists and the covered code changed
after its sync commit without that check being rerun: merges, edits made
without the verify skill, or drift over many commits. A change made while
following the verify skill uses the verify skill itself.

A pass on a stale verification looks like a proof of code that no longer exists.

### Outcomes

Give each check one outcome, or both updated and bug:

| Outcome | Condition |
| --- | --- |
| **in sync** | Nothing since the sync commit touches what the check models, and it passes |
| **updated** | The verification was changed to match the new code, and it passes |
| **bug** | The verification matches the current code and the property fails. A code finding, not drift |
| **blocked** | The check could not be realigned or could not run. Give the exact reason |

Edit only the verification and the verify skill. Product code follows
Toolbox policies step 2.

### Pass

1. **Find the checks.** Find each project skill that runs a model
   checker, prover or verifier against named code, or the one the ticket
   or operator named. For each check, collect the property, the covered
   code, the bounds and assumptions, the command and the sync commit. If
   no verify skill exists, stop and use Create. If no sync commit is
   recorded, take the newest commit that touched the verification files
   instead, and report that you did.
2. **Baseline run.** Before any edit, run every check once and record
   the result. Leave the drift-or-bug call for step 5.
3. **Review the covered changes.** Diff the covered files between the
   sync commit and HEAD, and read the commit messages. Code that moved,
   was renamed or split still counts, and so does new code that writes
   the guarded state. Classify each change:

   | Class | Condition | Action |
   | --- | --- | --- |
   | No effect | The verification describes nothing the change alters. Check against the model or harness, not the commit message | None |
   | Shape changed | An atomic step split; a branch appeared or went away; a guard moved; another path now reaches the guarded state; a value range changed | Update the model or harness |
   | Promise changed on purpose | The doc comment, tests, changelog or commit message say the new behavior is intended | Change the property; cite the evidence |
   | Promise may be broken | The code changed with no evidence of an intended promise change | Treat a later failure as a bug candidate |

4. **Derive updates from the code.** Write each update by reading the
   code, before any rerun, never by aiming for a pass. An atomic step in
   the code stays one step in the verification. Touch a property only for
   an intended promise change, and record its before and after text with
   the evidence. Bounds stay unless the change invalidates them; report
   any bound you lower.
5. **Rerun and classify.**
   - If it passes: make a broken variant of the new code, confirm the
     check fails on it, then drop it.
   - If it fails: walk each counterexample step through the real code.
     A step the code cannot take means the verification is wrong: fix it
     and say what was off. If the code can take every step, it is a bug:
     find the commit that brought it in, list the steps in the code's
     words, and give the harm in one sentence. A cheap reproduction on the
     real code belongs in the report as evidence, never in product code.
6. **Refresh the verify skill.** Bring its coverage record, commands,
   bounds, assumptions and sync commit up to date; the sync commit becomes
   the commit you checked. A blocked check keeps its old sync commit; say
   so. Finally, walk through the verify skill once as its next user would.

### Report

For each check, report:

1. The outcome and the commits you read.
2. Each change to the verification, with its class and, for a changed
   promise, the evidence.
3. The rerun result and the broken variant that showed the check can still fail.
4. Each bug: its steps in the code's words, its harm, and the commit that brought it in.
5. Gaps: what is still uncovered, including new code the verification should reach.

Label every failure as verification drift or a code bug. When a check
passed before the update and fails after it, state that the earlier pass
checked a stale model. Commit the verification updates on their own,
apart from any product fix.
