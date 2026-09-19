---
name: discover-the-idea
description: use this when the user wants to think through a fuzzy idea, gather requirements, pressure-test a plan before building, or says "discover the idea", "grill me", or "interview me". architect gatherer. do not use to implement, scaffold, or critique a finished design.
---

# Discover the idea

Architect gatherer. Turns a messy thought into a brief another agent can
attack. No `scripts/`. The subject does not have to be code.

## Iron law

**Do not write the thing. Do not decide the thing. Surface the thing.**
The user owns decisions. You own facts. The session ends in a brief.

## Loop

### 0. Stream of consciousness (always first)

Ask for a dump. Wait. Do not start the grill in the same message.

Say this, then stop:

> Dump whatever is in your head about this. Messy is the point. Goals,
> fears, constraints, half-ideas, things you already rejected, what
> "done" might look like. I will not interrogate until you send it.

If they already dumped in the invoking message, do not ask again. Use
that text as the dump.

### 1. Reflect

One short paragraph in their words, tightened. Confirm or correct
before any question list. Name what is still fog.

### 2. Environment (only if it exists)

Look around **after** the dump. This may not be a code repo.

Inspect only what is actually there: working tree, notes, prior briefs,
open tickets, linked docs, public pages they named. Skip this step when
there is no environment worth reading.

Facts you can look up are your job. Do not ask the user what a file,
ticket, or public page already says.

### 3. Options map (when alternatives exist)

If the idea has real options (tools, patterns, prior art), research
**3–5** of them before the first grill round that depends on that
choice. Each option: who uses it, the ugly part, how it fits *this*
dump. Cite a source. No invented "industry standard."

Skip the map when the dump is a personal decision with no market.

### 4. Frontier grill

Treat the idea as a **design tree**. Each decision hangs more decisions
off it.

A **frontier** is every question whose prerequisites are already
settled. Ask the whole frontier in one round. Number the questions.
Give a recommended answer on each. Wait.

Format:

```
❓ **Q1** — **<title>**: <body, choices if any>
➡️ <recommended answer, grounded in the dump or research>

---

❓ **Q2** — **<title>**: …
➡️ …
```

After answers, recompute the frontier. A question that depends on
another still open this round belongs to the *next* round.

Push back on fog ("probably", "later", "something like"). Propose a
strawman they can reject. When you feel ready to stop, ask one more
round on out-of-scope and failure modes, then stop.

The session is done when the frontier is empty, or the next question
cannot be answered by talking (needs a prototype, a screenshot, a live
system). Mark those open. Do not invent.

### 5. Brief, then stop

Emit the brief. Ask the user to confirm it. Do not implement. Do not
hand the brief to a critiquer until they say so.

```
Intent
Out of scope
Constraints
Decisions          — chose A over B because …
Assumptions        — now explicit
Options map        — only if step 3 ran
Open               — ungrillable or deferred
Verify later       — how we would know a later build matched this
```

Default: the brief stays in chat. Do not write a file unless asked.

## Always

- Start at step 0 unless a dump is already in the thread.
- Recommended answer on every grill question.
- Look up facts before asking.
- Cap at four rounds. If round 4 still widens scope, split the idea and
  gather one slice.
- Load no language skill on a gather-only turn.

## Ask first

- Writing `CONTEXT.md`, an ADR, a ticket, or any file.
- Expanding "this idea" into "rebuild the product."
- Calling a critiquer or builder before the user confirms the brief.

## Never

- Implement, scaffold, or "just sketch the API."
- Critique the brief in the same turn (different agent).
- Ask the user for something the environment already answers.
- Recommend a tool you have not looked at this session.
- Name pantheon personas. Roles here are architect / designer / builder /
  tester / security / manager / operator.

## Red flags

- "I'll start the questions while you think"
- "Industry standard is X" with no source
- "Let me just write a stub so we can discuss"
- Forty questions with no recommended answers
- Loading language skills "in case we code next"
