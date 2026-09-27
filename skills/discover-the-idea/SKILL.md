---
name: discover-the-idea
description: use this when the user wants to think through a fuzzy idea, gather requirements, pressure-test a plan before building, or says "discover the idea", "grill me", or "interview me". architect gatherer. do not use to implement, scaffold, or critique a finished design.
---

# Discover the idea

This skill turns a messy thought into a **brief**: a written summary
that a different agent, the **refiner**, critiques. The subject does
not have to be code. The skill has no `scripts/`.

Role: **architect**. In the SDLC Brief step this agent is the
**gatherer**; gatherer and refiner ids, mint and resume:
[Step agents](../../docs/sdlc/subagents.md#step-agents). Load no
language skill on a gather-only turn:
[No-language turns](../language-router/SKILL.md#no-language-turns).

## Iron law

**Do not write the thing. Do not decide the thing. Surface the thing.**
The user owns decisions. You own facts. The session ends in a brief.

## Loop

### 0. Dump (always first)

1. If the thread already holds a **dump**, the user's unsorted text
   about the idea, for example in the invoking message, use that text
   as the dump and go to step 1.
2. Otherwise, send this and nothing else:

   > Dump whatever is in your head about this. Messy is the point. Goals,
   > fears, constraints, half-ideas, things you already rejected, what
   > "done" might look like. I will not interrogate until you send it.

3. Wait for the dump. Send no questions in that message.

### 1. Reflect

1. Restate the dump in one short paragraph, in the user's words,
   tightened, and name what is still vague.
2. Ask the user to confirm or correct it. Send no question list until
   they do.

### 2. Environment (only if it exists)

The environment may not be a code repo. Run this step after the dump.

1. Skip this step when there is no environment worth reading.
2. Inspect only what is actually there: working tree, notes, prior
   briefs, open tickets, linked docs, public pages the user named.
3. Look up every fact you can. Never ask the user what a file, ticket,
   or public page already says; read it instead.

### 3. Options map (when alternatives exist)

1. If the dump is a personal decision with no market, skip this step.
2. If the idea has real options, such as tools, patterns, or prior art,
   research 3–5 of them before the first question round that depends
   on that choice.
3. For each option, write who uses it, the ugly part, how it fits this
   dump, and a source. Never claim an "industry standard" without a
   source; cite one or leave the claim out.

### 4. Question the frontier

The idea is a **design tree**: each decision raises more decisions. The
**frontier** is every question whose prerequisites are already settled.

1. Ask the whole frontier in one round. Number the questions and give a
   recommended answer on each, in this format:

   ```
   ❓ **Q1** — **<title>**: <body, choices if any>
   ➡️ <recommended answer, grounded in the dump or research>

   ---

   ❓ **Q2** — **<title>**: …
   ➡️ …
   ```

2. Wait for the answers.
3. Recompute the frontier. A question that depends on another question
   still open this round goes in the next round.

Push back on vague words ("probably", "later", "something like").
Propose a strawman they can reject. When you feel ready to stop, ask one
more round on out-of-scope and failure modes, then stop.

The session is done when the frontier is empty, or when the next
question cannot be answered by talking, for example because it needs a
prototype, a screenshot, or a live system. Mark those questions open;
never invent an answer. Cap the session at four rounds. If round 4
still widens scope, split the idea and gather one slice.

### 5. Brief, then stop

1. Emit the brief in this outline:

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

2. Keep the brief in chat. Write a file only when the user asks.
3. Ask the user to confirm the brief.
4. Stop. Hand the brief to the refiner only when the user says so.

## Ask first

- Writing `CONTEXT.md`, an ADR, a ticket, or any file.
- Expanding "this idea" into "rebuild the product."
- Calling the refiner or a builder before the user confirms the brief.

## Never

- Never implement, scaffold, or "just sketch the API"; emit the brief.
- Never critique the brief in the same turn; the refiner does that.
- Never recommend a tool you have not looked at this session; look first.
- Never name pantheon personas; use only [Roles](../../docs/SDLC.md#roles).

## Red flags

- "I'll start the questions while you think"
- "Industry standard is X" with no source
- "Let me just write a stub so we can discuss"
- Forty questions with no recommended answers
- Loading language skills "in case we code next"
