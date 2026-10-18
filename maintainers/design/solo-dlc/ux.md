# UX — solo-dlc: the SDLC on a harness without sub-agents

High-level. How it feels and who does what — not pixels. **designer.**
Human gate: operator accepts, or writes `UX verification not required`.

- Slug: `solo-dlc`
- Brief: DER-421 brief v3, confirmed 2026-10-18 (tracker copy: a comment on DER-421)
- HLD: `maintainers/design/solo-dlc/hld.md` (Plan, same step)
- Stories: [user-stories.md](user-stories.md)
- Date: `2026-10-18`
- Agent review (requirements only): round 1 failed; fix round 1 done;
  re-check raised one major; fix round 2 done; round 3 review raised
  two majors; fix round 3 done, re-check pending
- Operator: pending

## People

- **Operator.** Owns the repo and the tracker. Runs the kickoff skill
  and Gather in an interactive session, runs the start command, answers
  escalated questions, and holds every operator gate (SD-26).
- **Manager session.** The agent session the driver resumes when a stage
  stops. Answers from what the project holds, or escalates.
- **Workers.** One harness process per persona invocation: builder,
  verifier, reviewer, and the step personas (architect, designer, and
  so on). The builder, verifier, and reviewer of an item are resumed
  across passes, never replaced.
- **Bundle author.** Any person or agent writing a second bundle with
  the bundle-authoring skill.
- **Followed-mode agent.** An agent on a harness with no plugin that
  follows a bundle through the followed-mode skill.

## Terms used here

- **Run root**: the durable folder, outside the checkout, that holds
  one bundle instance.
- **Run folder**: `<persona>/run-N/` under the run root. One per
  invocation. Holds `result.json`, prose, logs, and `state.md`.
- **Stop**: a stage that is `blocked`, returns `needs_input`, exhausts
  its repair budget, or gives an invalid result after its one repair.
- **Console**: the operator's terminal session where `/sdlc` runs.
- **Start command**: how the operator starts or resumes the driver. In
  OpenCode, start and resume use a dialog: pick `/sdlc`, then enter
  RUN_ROOT. In Pi, type `/sdlc RUN_ROOT`.

## Journeys

- **J1 Kickoff to first command (happy path).** Interactive session →
  operator loads the kickoff skill → readiness checklist (tracker,
  branches, plumbing) → Gather interviews the operator on a brain dump →
  operator confirms the brief → kickoff initializes the run root →
  console prints the run root and the exact start command for
  the harness → operator runs it.
- **J2 Public tickets warning.** No tracker connected → kickoff offers
  the `local` adapter (a `tickets` branch) → the repo is public → kickoff
  says, before anything is written, that ticket titles, bodies, and
  comments on that branch are public → operator picks: use it, name
  another tracker or repo, or decide after Gather. No default on a
  public repo.
- **J3 Driver runs workers.** Start command → the console shows one
  start line and one end line per stage: item, step, persona, new or
  resumed, run folder; then status, choice, and artifact path. No stage
  starts before the previous one has ended or stopped → every exit from
  Build goes Build → Verify → Review → items land and close without
  waking the manager.
- **J4 Failing proving command.** Proving command fails → console shows
  the failure, the log path, and `repair 1/3` → builder resumed with the
  log → commands re-run → pass, then the model verifier runs. Third
  failed fix → stop (J5). An invalid `result.json` gets one repair,
  shown as `repair 1/1`; still invalid → stop (J5).
- **J5 Stop, manager first.** A stage stops → console names the stop
  kind, the stage, and its run folder → driver resumes the manager →
  manager answers from the project and the driver continues, or the
  manager escalates and the console shows a full `ask-human.md` message
  → the escalated item waits; other unblocked items continue, one
  large-model session at a time → the next start command shows
  the ask before any stage starts, and the operator's next line is the
  reply.
- **J6 Trial question.** HLD stage ends → operator gets an
  `ask-human.md` message: run a Trial or not, with the architect's
  recommendation → yes writes the Trial kickoff prompt and prints its
  path → no continues to Spec.
- **J7 Find outputs.** Operator opens the run root → finds the run
  folder for an item and step from the console line, or from the run
  root's chronological index (open question Q3) → reads prose,
  `result.json`, logs, and `state.md`.
- **J8 Crash or reboot.** Harness dies mid-stage → operator runs
  the start command again → console reports what it found: last finished
  stage, the interrupted run folder (kept), sessions it will resume, and
  the next run folder → continues. A missing session file stops the
  resume with a clear message; the driver never resumes into a blank
  session.
- **J9 Second bundle.** Bundle author loads the bundle-authoring skill
  → writes the flow file, personas, skills, and scripts in one folder →
  runs the driver's bundle check → fixes errors that name the step and
  exit → runs the bundle in either mode.
- **J10 Followed mode.** Harness without a plugin → agent loads the
  followed-mode skill with a bundle and run root → first line it writes
  says the run is followed, not enforced → agent follows the same flow,
  writes the same run folders, and applies the same exit rule → at each
  separate-agent step it prints the persona, the run folder, and the
  prompt, then stops; the operator opens a new session for that step
  (open question Q2).
- **J11 Moved tip at land.** Reviewer passes → driver fetches → the tip
  moved → console says so → builder resumed to merge the tip into the
  item branch → builder's end line says the merge was clean or needed
  conflict resolution → verifier re-runs → if the builder resolved
  conflicts, reviewer re-runs too → after a clean merge, Review is
  skipped only while the item's tree is exactly that merge; if the
  builder changes anything after it, for example to fix a failed
  re-run, the console shows builder → verifier → reviewer again before
  the merge line → driver fetches again → tip unchanged
  → driver merges this one item and pushes without force → post-land
  verifier → `done`. A conflict the builder cannot resolve is a stop
  (J5), and the item does not merge.
- **J12 Operator gate.** A stage reaches an operator gate: accepting
  the Plan or the Spec, a waiver, a security severity, three failed
  fixes, a destructive action, or spending → driver resumes the manager,
  which may only escalate → console and the manager's run folder hold
  the full `ask-human.md` message; in followed mode it says `followed,
  not enforced` → operator replies as in J5. The Trial question is J6.

## Stories

In [user-stories.md](user-stories.md):

| Person | Stories |
| --- | --- |
| Operator, start | SD-1 ready the repo, SD-2 tracker and public tickets, SD-3 Gather, SD-4 run root and start line, SD-5 only the operator starts |
| Operator, run | SD-6 progress lines, SD-7 stop and manager first, SD-8 escalation, SD-9 Trial question, SD-10 find outputs, SD-11 resume, SD-12 stop on purpose, SD-13 land without the manager, SD-26 operator gates, SD-27 Build → Verify → Review, SD-28 land on a moved tip |
| Bundle author | SD-14 write a bundle, SD-15 errors by step and exit |
| Followed mode | SD-16 followed, not enforced, SD-17 separate-agent steps, SD-18 same exit rule |
| Workers | SD-19 builder with failing log, SD-20 builder after compaction, SD-21 verifier ledger, SD-22 post-land verifier, SD-23 reviewer re-review, SD-24 claim and comment |
| Manager | SD-25 answer from the project |

## High-level UX

**Kickoff (interactive).** A normal conversation. The kickoff skill
shows a short readiness checklist and marks each line done, to do, or
deferred. Tracker choice is one `ask-human.md` message. Gather is the
existing `discover-the-idea` interview. The session ends with two lines
the operator can copy: the run root and the start command, in OpenCode
"pick `/sdlc`, then enter RUN_ROOT", in Pi `/sdlc RUN_ROOT`. If the
operator asks the model to start the run, the model says `/sdlc` is a
command only the operator can run, and repeats the line.

**Driver console.** Terse and line-based; worker transcripts go to log
files, not the console. Rough sketch, exact text belongs to Spec:

```text
solo-dlc  bundle sdlc  mode enforced  root RUN_ROOT
ABC-12 Build   builder  resumed  builder/run-4  started
ABC-12 Build   fail     proving command 2 of 3 failed  log builder/run-4/logs/prove-2.log  repair 1/3
ABC-12 Build   builder  resumed  builder/run-5  started
ABC-12 Build   pass     choice verify  artifact builder/run-5/result.md
ABC-12 Verify  verifier resumed  verifier/run-3  started
ABC-12 Verify  pass     choice review  ledger 2 fixed, 0 open, 1 nit
ABC-12 Review  reviewer resumed  reviewer/run-2  started
ABC-12 Review  pass     choice land  reads pr-review, security-hardening
ABC-12 Land    fetched  tip moved  builder merges the tip
ABC-12 Land    builder  resumed  builder/run-6  started  merge tip
ABC-12 Land    pass     tip merged clean  artifact builder/run-6/result.md
ABC-12 Land    verifier resumed  verifier/run-4  started  re-run
ABC-12 Land    pass     ledger 0 open
ABC-12 Land    fetched  tip unchanged  merged  integrate/solo-dlc  pushed
ABC-12 Land    verifier resumed  verifier/run-5  verified  done
ABC-14 Land    fetched  tip moved  builder merges the tip
ABC-14 Land    builder  resumed  builder/run-7  started  merge tip
ABC-14 Land    pass     tip merged, conflicts resolved  artifact builder/run-7/result.md
ABC-14 Land    verifier resumed  verifier/run-6  started  re-run
ABC-14 Land    pass     ledger 0 open
ABC-14 Land    reviewer resumed  reviewer/run-3  started  re-review
ABC-14 Land    pass     reads pr-review, security-hardening
ABC-14 Land    fetched  tip unchanged  merged  integrate/solo-dlc  pushed
ABC-14 Land    verifier resumed  verifier/run-7  verified  done
ABC-15 Land    fetched  tip moved  builder merges the tip
ABC-15 Land    builder  resumed  builder/run-8  started  merge tip
ABC-15 Land    pass     tip merged clean  artifact builder/run-8/result.md
ABC-15 Land    verifier resumed  verifier/run-8  started  re-run
ABC-15 Land    fail     ledger 1 open  builder fixes after the clean merge
ABC-15 Land    builder  resumed  builder/run-9  started  fix
ABC-15 Land    pass     choice verify  artifact builder/run-9/result.md
ABC-15 Land    verifier resumed  verifier/run-9  started  re-run
ABC-15 Land    pass     ledger 0 open
ABC-15 Land    reviewer resumed  reviewer/run-4  started  re-review
ABC-15 Land    pass     reads pr-review, security-hardening
ABC-15 Land    fetched  tip unchanged  merged  integrate/solo-dlc  pushed
ABC-15 Land    verifier resumed  verifier/run-10  verified  done
ABC-13 Build   invalid result  builder/run-10  repair 1/1
STOP   ABC-13 Build  repair budget exhausted (3 failed fixes)  builder/run-11
       resuming manager  manager/run-2
```

Each line names the item, the step, the persona, whether the session is
new or resumed, and the run folder relative to the run root. A stop
line starts with `STOP` and a reason in words, not color alone. One
large-model session runs at a time, so no start line appears before the
previous stage's end line or `STOP` line. A `choice` that would skip
Verify or Review is rejected with one line naming the step, the value,
and the allowed exits.

**Stops.** The manager is always resumed first. If it answers, the
console prints one line naming where the answer came from (brief, plan,
spec, tracker, or a Gather session) and the run continues. If it
escalates, the console prints the full `ask-human.md` message and the
ask is also saved in the manager's run folder. The escalated item waits
while other unblocked items continue. The next start command shows
the ask before any stage starts, and the operator's next line is the
reply (open question Q1).

**Operator gates.** Accepting the Plan, accepting the Spec, waivers,
security severity, three failed fixes, destructive actions, and spending
always reach the operator. The manager may only escalate them. In
followed mode the ask also says `followed, not enforced`. The Trial
question at the end of HLD is its own ask (SD-9).

**Tracker comments.** Public comments carry only the ticket id, the
status, and the run folder relative to the run root. Any comment may add
one more field: the repo-relative git path of a record this run has
committed, such as the HLD or LLD path posted on the Epic. A land
comment may add the land SHA, the result, and the reviewer verdict. No
absolute paths, logs, prompts, or Gather text.

**Run root.** One folder per persona, `run-N` folders inside, old runs
kept. `state.md` is at most one page. The operator never has to read a
worker transcript to know what happened: the console line, `result.json`,
and the prose are enough.

**Resume.** The start command again is the only resume action: in
OpenCode, pick `/sdlc`, then enter RUN_ROOT in its dialog; in Pi, type
`/sdlc RUN_ROOT`.
No flags to remember. The first lines report what the driver found
before it starts anything.

**Followed mode.** Same run root, same files, same exit rule. The
difference is stated, not hidden: the first line, each stage's prose,
and each stop say `followed, not enforced`, meaning an agent, not a
driver, keeps the gates on this harness. At a separate-agent step the
skill prints the persona, the run folder, and the prompt, then stops.

**Bundle authoring.** The skill walks the author through the folder
and the flow file. The driver's bundle check reports errors by step and
exit, one per line.

**Mockups:** `n/a` — no graphical screen; console lines, chat messages,
and run-root files only. The sketch here stands in; exact console text
is fixed at Spec.

## Comparables

The HLD's page, `maintainers/design/solo-dlc/comparables.md`, covers
shape. For look and flow:

| Example | Steal | Will not copy |
| --- | --- | --- |
| [`git rebase`](https://git-scm.com/docs/git-rebase) stop and continue | A stop says why, where its state is, and the one command that continues. State lives on disk, so a crash loses nothing. | Separate `--continue`, `--skip`, and `--abort` verbs. Here, the start command is the only resume. |
| [GitHub Actions run logs](https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs) | One status line per step, full log one hop away. | A web page, live log streaming in the main view, and color as the only status signal. |
| [`terraform apply`](https://developer.hashicorp.com/terraform/cli/commands/apply) confirmation | Nothing irreversible happens until the person answers in words. | `-auto-approve`: no flag skips an operator gate. |

## Not this

- A graphical or web dashboard; a TUI panel beyond console lines.
- An orchestrator agent, or a tool the model can call to start `/sdlc`.
- Live streaming of worker transcripts into the console.
- Automatic discovery of the run root from the previous transcript
  (later, per the brief).
- The OpenCode plugin console; it follows the Pi console once item 7
  starts.
- Exact console wording, file names inside run folders, and the bundle
  check's command name; those belong to the HLD and Spec.

## Open questions for the operator

Q1–Q3 stay open until the operator accepts this page.

- **Q1 Replying to an escalation. Open.** Recommend: the escalated item
  waits and other unblocked items continue, one large-model session at
  a time. When the operator next runs the start command, the ask appears
  before any stage starts, and the next line the operator types is the
  reply (SD-8). A reply typed in the console while the run is going
  depends on whether the TUI stays usable during a long command
  handler, which the brief lists as not confirmed: a Trial candidate,
  not a done-when.
- **Q2 Separate-agent steps in followed mode. Open.** Recommend: the
  skill prints the persona, the run folder, and the prompt, then stops;
  the operator opens a new session for that step (SD-17).
- **Q3 Chronological index. Open.** Recommend: the driver appends one
  line per stage to one index file at the run root (time, item, step,
  persona, run folder, status). It answers "what ran, in what order"
  without opening persona folders, and is the same data resume reports.
