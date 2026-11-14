---
name: statechart
description: use this when charting how a system or a user flow moves between states, in the reader's words — draw a Mermaid stateDiagram-v2 from a TLC-checked TLA+ model and report each broken rule as its shortest path, or chart a user flow from approved stories, labelled "not model-checked" when no checked model backs it.
---

# Statechart

Rewrite of `cursor/plugins` `pstack/skills/statechart` @ `3dbd22ff12742fb28c9700b9760baa29ed41dc13` (MIT), method only. Compress, not a paste. Pin: [SOURCES.md](../../SOURCES.md).

A statechart draws the states a system passes through and the steps
between them, labelled for the reader, who judges whether the behavior is right. The deliverable is
plain Mermaid `stateDiagram-v2` text, written by hand. Rendering it is optional.

## Names

- **Reader** — whoever decides whether the charted behavior is right: the operator, or someone the operator names in writing.
- **Reader rule** — one rule the reader agrees to, in the reader's words, such as "you are never charged twice". It may concern what a screen shows, an outcome, saved data or a sent message.
- **Model state** — one state TLC reports: one value for every variable.
- **Chart state** — one box in the chart, labelled in the reader's words. Several model states can share one chart state.
- **Step label** — the words on an arrow: the event as the reader would describe it, such as "you tap pay" or "the card is declined".
- **Bug path** — TLC's shortest trace from a start state to a state that breaks one reader rule.
- **Mark** — the class `breaks` on a chart state where every model state behind it breaks a rule, or `mayBreak` where only some do.

## Iron law

**Never weaken a reader rule to make it hold.** When no variable can
express a rule, add one to the model. If a rule breaks, report its bug
path instead. A chart drawn without a checked model is labelled "not
model-checked" in its title and in the handoff.

## Actors

- **architect** or **verifier**: charts a TLA+ model and reads TLC's results.
- **designer**: charts a user flow from approved stories.

## Toolbox policies

1. Run TLC from the TLA+ tools the product repo already uses. Adding TLA+
   tools to a product repo follows
   [formal-verification Toolbox policies](../formal-verification/SKILL.md#toolbox-policies) step 3.
2. Work in a scratch folder outside the repo. When a verify skill keeps
   the spec in the repo, read the spec there and write every TLC output
   and chart to the scratch folder.
3. Ask the operator only per [Asking the operator](../sdlc/SKILL.md#asking-the-human).
4. The upstream pstack `statechart` command is an operator opt-in, used
   only when the operator says so in writing, at the operator's own risk.
   It is TypeScript at [cursor/plugins `pstack` at `3dbd22f`](https://github.com/cursor/plugins/tree/3dbd22ff12742fb28c9700b9760baa29ed41dc13/pstack).
   Its first run installs TLC and Java through `mise` and needs the
   network. This toolbox does not vendor it, run it or give an install
   command for it. Without that opt-in, follow this file.

## Chart a checked model

The **architect** or **verifier** uses this section.

### Write the spec

1. Write each reader rule as an `INVARIANT` in the config. Name it after the rule.
2. Write `Next` as a disjunction of named actions, such as
   `YouPressPlay \/ YouPressStop`. Without names, every step is `Next`.
3. For each correct end state, add one action to `Next` that is true only
   in end states and leaves every variable as it is, for example
   `Finished == stage \in {"shipped", "cancelled"} /\ UNCHANGED vars`. TLC reports
   any state with no step out as a deadlock, a correct end state included;
   once those actions exist, every deadlock TLC reports is a bug.
4. Keep the constants small, or add a `CONSTRAINT`, so the state space is finite.

### Run TLC

1. Run TLC once on the unmodified config, single-worker, with its
   `-dump dot` option set to label actions (`-dump dot,actionlabels <file>`).
   Keep the output as `tlc.out`.
2. If TLC reports a broken invariant, a broken `PROPERTY` or a deadlock,
   save its trace as that rule's bug path, in `tlc-<rule>.out`. TLC
   stops at the first break; for an invariant or a deadlock its trace is
   the shortest path to it.
3. Remove that rule from a copy of the config; for a deadlock, set
   `CHECK_DEADLOCK FALSE`. Run TLC again on the copy.
4. Repeat steps 2 and 3 until no rule breaks.
5. Keep the `.dot` graph and the distinct state count from the last run:
   it explored the whole state space, past every broken rule.
6. If a run stops on an error or does not finish, list each rule it did
   not check under "Rules not checked". Do not mark those rules. A rule
   not checked can hold or break.

Read these limits before you trust a result:

- A state beyond a `CONSTRAINT` or `ACTION_CONSTRAINT` still has its
  reader rules checked, but TLC neither expands it nor tests it for
  deadlock, so a deadlock there stays hidden.
- A `VIEW` or `SYMMETRY` makes TLC fold equivalent states into one. An arrow can lead to that one state rather than to the state
  the step reaches. Say so in the report.

### Map states and steps

1. Write a table: each model state, or each group of variable values, to
   one chart state label. Use what the reader sees or cares about, such
   as "Checking out" or "Lock taken, save not yet written", never a
   variable name. The label is a function of the model state alone.
2. Choose the form. Flat: one label per state. Nested: a parent state
   holds child states, written as `state "Parent" as p { ... }`. Parallel:
   one region per independent part, separated by `--` inside a parent state.
3. Write a table: each TLC action to one step label, in the reader's
   words. Never name the code or the TLA+ action. Actions that land the
   same way in the chart get one shared label, and so one arrow.
4. If a step is possible only in some situations, append that situation
   in square brackets, phrased for the reader, as in
   `you tap pay [while the cart is saving]`. In a parallel chart, never
   bracket a condition on another region; write that region's label,
   such as `[when Offline]`.
5. When a hidden value picks the step's destination, put the outcome in
   the label, as in "the stock lookup fails".
6. A step that stays inside one chart state draws no arrow. If the reader
   must see that step, split the label.

### Draw the chart

1. If TLC counted more than 500 states, draw only the bug paths; if no
   rule broke, draw no chart, report the state count, and say that a
   smaller model is needed to see the graph. Otherwise draw every chart
   state reachable from a start state, and every arrow.
2. Count the arrows. Above about 20, coarsen first: merge values that
   behave alike under one label, and drop detail the reader can skip,
   such as a pending call whose answer changes nothing.
3. While coarsening, keep every state of every bug path and every mark.
   Never merge two states that break different rules. A merge that turns
   `breaks` into `mayBreak` hides where a rule breaks; undo it.
4. If it is still too busy, hide steps the reader can skip, such as a
   reset available everywhere or an arrow that duplicates others. Hide
   every step behind an arrow, or none. Every chart state must stay
   reachable from a start state. A chart state that can move in the model
   keeps at least one outgoing arrow.
5. Evaluate each broken rule on the variable values in the graph's state
   labels. Mark each chart state: `breaks` if every model state behind it
   breaks a rule, `mayBreak` if only some do. The graph explored past each
   broken rule, so states after a bug appear too.
6. Add the class lines and a Legend. One Legend state per mark names the
   rules it marks; if two rules break in one state, name both:

   ```mermaid
   stateDiagram-v2
     classDef breaks fill:#ffecee,stroke:#e72e3b,color:#cd2834
     classDef mayBreak fill:#fff3e6,stroke:#e8730c,color:#b85a06
     state "Breaks rule: never charged twice" as legend_breaks
     class legend_breaks breaks
   ```

7. To color phases, give each phase a `classDef` and a `class` line. A
   chart state whose model states are in different phases gets no phase color.
8. Put a title on the chart with Mermaid front matter `title:`.

### Report and replay

1. For each broken rule, write: the rule's name, the reader's sentence for
   it, and its bug path as numbered steps in step labels.
2. Say which chart state breaks which rule.
3. List "Rules not checked", if any, and the steps the chart hides.
4. Say what the model leaves out.
5. When the model describes code, re-run each bug path on the real code,
   as a test or a live reproduction, one code step per model action. If a bug
   does not occur, treat the model as wrong until you show it is not.
6. Hand off the Mermaid text in a `mermaid` code block, the report, and
   the TLC commands that make the files again into a new scratch folder.

## Chart a user flow

The **designer** uses this section for the product's most important user flows.

1. Take the flow from stories the operator approved in `ux-design`.
2. Name the reader rules the stories promise, in the reader's words.
3. Map each screen or state the user sees to a chart state, and each user
   action or system event to a step label, per Map states and steps steps 1–6.
4. Draw it per Draw the chart steps 2, 4, 7 and 8. Without a checked model,
   draw no mark.
5. If no TLC run backs the chart, put "not model-checked" in its title and
   in the handoff.
6. To check the flow, write it as a spec with the reader rules as
   invariants and follow Chart a checked model.
7. Hand off the Mermaid text in a `mermaid` code block, the stories it
   came from, and whether it is model-checked.
