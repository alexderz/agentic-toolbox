# User stories — solo-dlc

Shape: `skills/sdlc-artifacts/templates/user-story.md`, one job each.
UX: [ux.md](ux.md). HLD: `maintainers/design/solo-dlc/hld.md`.
Brief: DER-421 brief v3, confirmed 2026-10-18.

`RUN_ROOT` is the run root; `ABC-12` is an example ticket id. Each
story's **Done when** is checkable from console output, run-root files,
git, or tracker state.

## Operator: start

### SD-1 Ready the repo before Gather

- **As** the operator **I want** the kickoff skill to ready the repo and
  the plumbing first **so that** the run starts on a ready repo, with
  the tracker chosen now or after Gather.
- **Done when:**
  - The kickoff skill runs in a normal interactive session; no driver
    and no plugin are required.
  - It shows a checklist covering the tracker, each branch the run uses
    (trunk, project-main, and the `tickets` branch when the `local`
    adapter is chosen), and the run root's parent folder. Each line is
    marked `done`, `to do`, or `deferred`.
  - The `local` adapter is an allowed tracker choice.
  - The tracker line can be `deferred` until after Gather. A deferred
    choice is asked again before the first tracker write (SD-2).
  - It writes nothing before the operator replies to the checklist.
- **Out of scope:** installing the harness or the plugin.

### SD-2 Choose a tracker, warned about public tickets

- **As** the operator **I want** to be told when tickets would be public
  **so that** I do not publish private notes by accident.
- **Done when:**
  - The choice comes as one `ask-human.md` message.
  - With no tracker connected, the message offers the `local` adapter.
  - If the repo is public, the message states that the `tickets` branch
    and every title, body, and comment on it are public, before any
    ticket is written.
  - The choices include: use `local`, name another tracker or repo, or
    decide after Gather. A public repo has no default; silence writes
    nothing.
  - A choice of "after Gather" asks again before the first tracker
    write.
- **Out of scope:** creating tracker types or states.

### SD-3 Turn a brain dump into a confirmed brief

- **As** the operator **I want** Gather to run on my brain dump in the
  same session **so that** I do not restate it elsewhere.
- **Done when:**
  - Gather follows `discover-the-idea` and ends with a brief the
    operator confirms in words.
  - The Gather session is saved where the manager can read it later.
  - No run root exists before the confirmation.
- **Out of scope:** changing the Gather interview itself.

### SD-4 Get the run root and the start line

- **As** the operator **I want** the run root and the exact command
  printed **so that** I can start the run without searching.
- **Done when:**
  - After confirmation, the run root exists outside the checkout with
    one folder per persona and the first run folders.
  - The last lines of the session are the absolute run root and the
    line `/sdlc RUN_ROOT` with the real path.
- **Out of scope:** the plugin finding the run root by itself.

### SD-5 Start the driver myself

- **As** the operator **I want** only me to start a run **so that** no
  model starts work I did not ask for.
- **Done when:**
  - `/sdlc` is not in any model's tool list.
  - Asked to start the run, the model answers that only the operator
    can type `/sdlc`, and repeats the line from SD-4.
- **Out of scope:** headless start; `pi -p "/sdlc …"` is not confirmed.

## Operator: run

### SD-6 See which persona runs where

- **As** the operator **I want** one line per stage start and end
  **so that** I know what runs and where its files are.
- **Done when:**
  - The first line names the bundle, the mode (`enforced` or
    `followed, not enforced`), and the run root.
  - Each start line names the item, the step, the persona, `new` or
    `resumed`, and the run folder.
  - Each end line names the status, the `choice`, and the `artifact`
    path.
  - No new start line appears until the previous stage has printed its
    end line or a `STOP` line.
  - A failed proving command line names the command, the log path, and
    the repair count as `repair N/3`.
  - An invalid `result.json` line names the stage and the run folder,
    and its repair attempt prints `repair 1/1`.
  - Status is in words; no meaning by color alone.
  - Worker transcripts are not printed to the console.
- **Out of scope:** a dashboard; live transcript streaming.

### SD-7 See a stop and the manager answer first

- **As** the operator **I want** stops to go to the manager before me
  **so that** I only see questions the project cannot answer.
- **Done when:**
  - Each of the four stop kinds prints a `STOP` line naming the kind in
    words (`blocked`, `needs input`, `repair budget exhausted`,
    `invalid result after repair`), the stage, and its run folder.
  - The next line says the manager is being resumed and names the
    manager's run folder.
  - If the manager answers, one line names the source it used (brief,
    plan, spec, tracker, or a Gather session) and the run continues.
  - An operator gate always escalates, as SD-26 sets out.
- **Out of scope:** the manager's reasoning in the console.

### SD-8 Answer an escalated question

- **As** the operator **I want** an escalation as a full question with a
  recommendation **so that** I can answer without opening files.
- **Done when:**
  - The console shows a complete `ask-human.md` message, and the same
    text is saved in the manager's run folder.
  - The escalated item waits. Other unblocked items continue, one
    large-model session at a time.
  - When the operator runs `/sdlc RUN_ROOT`, the same ask appears before
    any stage starts, and the next line the operator types is the
    reply. The reply is saved verbatim with the ask.
- **Out of scope:** replies from a chat channel; a reply typed in the
  console while the run is going, which is a Trial candidate (UX Q1).

### SD-9 Decide on a Trial at the end of HLD

- **As** the operator **I want** to be asked whether to run a Trial
  **so that** uncertain parts get proof only when I choose.
- **Done when:**
  - The HLD stage ends with an `ask-human.md` message that names the
    unconfirmed facts and recommends yes or no.
  - On yes, the Trial kickoff prompt is written to a file and the
    console prints its path.
  - On no, the run continues to Spec.
  - The run does not continue past HLD without an answer.
- **Out of scope:** running the Trial inside the driver.

### SD-10 Find a run's outputs and state

- **As** the operator **I want** to find any stage's files from its
  console line **so that** I can audit what happened.
- **Done when:**
  - Every run folder named on the console exists.
  - The run folder of each finished invocation holds `result.json`,
    prose, logs, and `state.md`. Its `result.json` passes the reader in
    `docs/sdlc/stage-result.md`, including `schemaVersion`, `choice`,
    `ticket`, and `artifact`.
  - An interrupted run folder stays, is marked interrupted, and is
    exempt from the reader rule.
  - `state.md` is at most one page.
  - Old run folders are still present after later runs.
- **Out of scope:** search across run roots.

### SD-11 Resume after a crash or reboot

- **As** the operator **I want** to resume with the same line I started
  with **so that** a crash costs me nothing but time.
- **Done when:**
  - Typing `/sdlc RUN_ROOT` again prints, before any stage starts: the
    last finished stage, any interrupted run folder, the sessions it
    will resume, and the next run folder.
  - The interrupted run folder is kept, marked interrupted, and never
    reused; the next invocation gets a new `run-N`.
  - If a session file to resume is missing, the driver stops and names
    the file; it never starts a blank session in its place.
- **Out of scope:** resuming a run root on another machine.

### SD-12 Stop a run on purpose

- **As** the operator **I want** to interrupt the driver safely **so
  that** I can stop for the day.
- **Done when:**
  - Interrupting the console marks the in-flight run folder interrupted
    and leaves the run root ready for SD-11.
  - No merge is left half done: the merge has either not started, or
    has finished and is checked out.
  - No push uses force, and stopping needs no push.
- **Out of scope:** pausing a single item while others continue.

### SD-13 See items land without waking the manager

- **As** the operator **I want** land paperwork done by the driver and
  the verifier **so that** a pass needs no manager turn.
- **Done when:**
  - After a reviewer pass, the console shows fetch, merge, proving
    commands on `integrate/solo-dlc`, and the verifier's confirmation,
    then `done`.
  - The ticket has a comment with the land SHA, the result, and the
    reviewer verdict.
  - No manager run folder is created for a land with no stop.
  - A dependent item's first line appears only after its blocker shows
    `done`.
- **Out of scope:** landing project-main on trunk.

### SD-26 Hold every operator gate myself

- **As** the operator **I want** every operator gate to come to me
  **so that** no agent makes a decision the SDLC keeps for me.
- **Done when:**
  - Each of these gates stops its stage and comes to the operator:
    accepting the Plan, accepting the Spec, a waiver, a security
    severity, three failed fixes, a destructive action, and spending.
  - The manager may not answer a gate. Its result for a gate is always
    an escalation, even when the project holds an answer.
  - The console shows the full `ask-human.md` message, and the same
    text is saved in the manager's run folder.
  - In followed mode, the ask carries the words `followed, not
    enforced`.
  - The stage does not continue until the operator's reply is recorded
    (SD-8).
- **Out of scope:** the Trial question, which is SD-9.

### SD-27 See every Build exit pass Verify and Review

- **As** the operator **I want** the driver to send every exit from
  Build through Verify and then Review **so that** no change lands
  without the separate checks, including the security reads.
- **Done when:**
  - In enforced mode, the console shows every exit from Build as
    Build → Verify → Review: a Build pass is followed by Verify for the
    same item, and a Verify pass by Review.
  - No Land line appears for an item unless Review passed after the
    item's last Build pass.
  - Each Review end line names its security reads.
  - At run time, a `choice` that would skip a step, or any `choice` not
    in the step's exits, is rejected. One line names the step, the
    value, and the allowed exits, and the run does not take that exit.
- **Out of scope:** followed mode, which is SD-18.

### SD-28 Land on a moved tip without force

- **As** the operator **I want** lands to stay safe on branches other
  people share **so that** no one's work is overwritten.
- **Done when:**
  - The console shows a fetch line before each merge.
  - Merges run one item at a time: no item's merge line appears while
    another item's merge is unfinished.
  - No push uses force: each pushed tip of a shared branch contains the
    tip it replaced.
  - When the fetched tip has moved, the console shows a line that says
    so, then a builder line merging the tip into the item branch. The
    builder's end line says either `tip merged clean` or `tip merged,
    conflicts resolved`.
  - After `tip merged clean`, a verifier re-run line follows. While the
    item branch's tree is still exactly the tree of that clean merge
    commit, no reviewer line appears before the item's merge line.
  - After `tip merged, conflicts resolved`, the console shows builder,
    then verifier re-run, then reviewer re-run lines, and the item's
    merge line appears only after both re-runs pass.
  - If the builder changes the item branch after `tip merged clean`,
    for example to fix a failed verifier re-run, the console shows
    builder, then verifier re-run, then reviewer re-run lines before the
    item's merge line. The merge line appears only after both re-runs
    pass, and the reviewer's re-review range starts at the clean merge
    commit.
  - When the builder cannot resolve a conflict, the console shows a
    `STOP` line of kind `blocked` (SD-7), and no merge line appears for
    that item.
- **Out of scope:** how the builder resolves a conflict.

## Bundle author

### SD-14 Write a new bundle

- **As** a bundle author **I want** a skill that teaches the bundle
  format **so that** I can define a workflow without reading the driver.
- **Done when:**
  - Following the bundle-authoring skill yields one folder with a flow
    file, personas, skills, and scripts.
  - The bundle passes the driver's bundle check.
  - The same bundle runs enforced and followed with no edits.
- **Out of scope:** porting existing bundles from other tools.

### SD-15 Get errors that name the step and exit

- **As** a bundle author **I want** each flow-file error to name its
  step and exit **so that** I fix it in one pass.
- **Done when:**
  - The bundle check reports one error per line, each naming the file,
    the step, and the exit or field at fault.
  - A flow file with an exit to an undefined step fails the check.
- **Out of scope:** auto-fixing the flow file; rejecting a `choice` at
  run time, which is SD-27.

## Followed mode

### SD-16 Know the run is followed, not enforced

- **As** the operator **I want** to be told when no driver keeps the
  gates **so that** I trust the run only as far as it deserves.
- **Done when:**
  - The followed-mode skill's first message says `followed, not
    enforced` and explains in one sentence that an agent, not a driver,
    keeps the gates on this harness.
  - Each stage's prose and each stop say the same words.
- **Out of scope:** writing a plugin for that harness.

### SD-17 Keep separate-agent gates in followed mode

- **As** the operator **I want** separate-agent steps to stay separate
  **so that** followed mode keeps the same gates.
- **Done when:**
  - At a step that needs a separate agent, the skill prints the
    persona, the run folder, and the prompt, then stops.
  - The skill never continues as the next separate-agent persona in
    the same session.
- **Out of scope:** starting processes on harnesses that cannot.

### SD-18 Apply the same exit rule in followed mode

- **As** the operator **I want** followed mode to reject the same bad
  exits **so that** the flow means the same in both modes.
- **Done when:**
  - Followed mode writes the same run folders and `result.json` fields
    as the driver.
  - A `choice` outside the step's exits is refused, and the skill names
    the allowed exits.
  - Every exit from Build goes through Verify and then Review.
- **Out of scope:** detecting an agent that ignores the skill.

## Workers

### SD-19 Builder resumed with a failing log

- **As** the builder **I want** a short prompt with the failing log
  path **so that** I fix the failure without re-reading the item.
- **Done when:**
  - The builder is resumed from the same session file as its earlier
    passes on the item, and its start line says `resumed`.
  - The resume prompt is the fixed text that loads
    `test-failure-handler`, plus the log path and `repair N/3`; it does
    not repeat the item, the spec, or earlier logs.
  - The builder opens the log, runs `debug` through root cause, fixes,
    and adds the lesson to `state.md`.
  - The proving commands in the plan entry are unchanged after the
    builder's run.
  - The builder never moves the ticket to `in_review` or `done`.
- **Out of scope:** the builder choosing which commands prove the item.

### SD-20 Builder keeps the driver's facts after compaction

- **As** the builder **I want** my compaction summary built from my
  `state.md` and the driver's facts **so that** I do not lose open
  issues.
- **Done when:**
  - After a compaction, the summary holds the builder's `state.md`,
    the open verifier issues, and the failing log paths.
  - Removing a driver fact from `state.md` does not remove it from the
    next summary.
- **Out of scope:** compaction for non-worker sessions.

### SD-21 Verifier re-checks against its ledger

- **As** the verifier **I want** my ledger of committed issues in
  `state.md` **so that** a re-check confirms fixes instead of starting
  over.
- **Done when:**
  - Each re-check resumes the same verifier session file as the item's
    earlier checks, and its start line says `resumed`.
  - The model verifier starts only after every proving command passes.
  - Each ledger entry has a criticality; a re-check marks each
    committed issue fixed or still open.
  - A re-check raises a new issue only if it is breaking or critical.
  - Nits are recorded in the ledger and not sent back to the builder.
  - The verifier never writes to the item worktree.
- **Out of scope:** the verifier fixing code.

### SD-22 Verifier confirms the land and closes the item

- **As** the verifier **I want** to confirm the land on project-main
  **so that** `done` means landed and verified.
- **Done when:**
  - The post-land verifier resumes the same session file as the item's
    earlier checks, and its start line says `resumed`.
  - The resumed verifier reads the proving-command results on
    `integrate/solo-dlc` and confirms them.
  - It moves the ticket to `done` and comments the land SHA, the
    result, and the reviewer verdict.
  - No other persona moves a ticket to `done`.
- **Out of scope:** the land merge itself; the driver merges.

### SD-23 Reviewer resumed for re-review

- **As** the reviewer **I want** to be resumed on the same item **so
  that** I check only what changed since my last verdict.
- **Done when:**
  - A re-review of the same item resumes the same reviewer session.
  - The prompt holds only the new range and the open review comments.
  - The reviewer never writes to the item worktree.
- **Out of scope:** reviewing a different item in the same session.

### SD-24 Claim and comment before exit

- **As** a worker **I want** to claim the ticket and comment on every
  outcome **so that** the tracker shows who ran and what happened.
- **Done when:**
  - Every worker run, whatever its status, leaves a claim and a comment
    on its ticket through `tracker-sdlc`, before the process exits.
  - Every tracker comment the run writes, from a worker or the manager,
    carries only the ticket id, the status, and the run folder relative
    to the run root.
  - A comment may also carry one more field: the repo-relative git path
    of a record this run has committed, such as the HLD or LLD path a
    step persona posts on the Epic. That path names a file that a commit
    made by this run added or changed.
  - A land comment may also carry the land SHA, the result, and the
    reviewer verdict.
  - No comment holds an absolute path, a log, a prompt, or Gather text.
- **Out of scope:** tracker writes by the console or the driver.

## Manager

### SD-25 Manager answers from the project

- **As** the manager **I want** the stop's context handed to me **so
  that** I answer without asking the operator what the project already
  says.
- **Done when:**
  - The resume prompt names the stop kind, the stage, its run folder,
    and the question or failure.
  - The manager's result cites the file or session it answered from,
    or escalates with a full `ask-human.md` message.
  - An operator gate is escalated, never answered by the manager
    (SD-26).
- **Out of scope:** the manager doing land paperwork.
