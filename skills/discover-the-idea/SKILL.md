---
name: discover-the-idea
description: use this when the user wants to think through a fuzzy idea, gather requirements, pressure-test a plan before building, or says "discover the idea", "grill me", or "interview me"; also as the SDLC refiner, which runs its Refine section. architect gatherer and refiner. do not use to implement, scaffold, or critique a finished design.
---

# Discover the idea

This skill turns a messy thought into a **brief**: a written summary
that a different agent, the **refiner**, critiques. The subject does
not have to be code. The skill has no `scripts/`.

Role: **architect**. In the SDLC Brief step this agent is the
**gatherer**; gatherer and refiner ids, mint and resume:
[Step agents](../sdlc/references/subagents.md#step-agents). Load no
language skill on a gather-only turn:
[No-language turns](../language-router/SKILL.md#no-language-turns).

## Iron law

**Do not write the thing. Surface the thing.** The user owns every
"theirs" question ([Asking the operator](../sdlc/SKILL.md#asking-the-human)).
Settle a minor point yourself and mark it `your call` in the brief.
You own facts. The session ends in a brief.

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
2. In an SDLC chunk, put the restatement in the brief; the operator
   corrects it at touchpoint 1. Outside the SDLC, put it at the top of
   the first question round, or in the brief when no question is
   left. Never send it alone.

### 2. Environment (only if it exists)

The environment may not be a code repo. Run this step after the dump.

1. Skip this step only when there is nothing to read. Otherwise inspect
   only what is actually there: working tree, notes, prior briefs, open
   tickets, linked docs, public pages the user named.
2. Look up every fact you can. Never ask the user what a file, ticket,
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

1. Sort each frontier question into the three piles of
   [Asking the operator](../sdlc/SKILL.md#asking-the-human). Write the
   answered ones into the brief. Settle the minor ones and mark them
   `your call`. Keep only "theirs".
2. In an SDLC chunk, you are not the liaison: write each remaining
   question as an ask section
   ([Raising an ask](../sdlc/references/liaison.md#raising-an-ask)) and
   send no message. Then write the brief, with those questions under
   Open; do not wait and run no further round. Outside the SDLC, ask
   the remaining frontier in one round. Number the questions and give
   a recommended answer on each, in this format:

   ```
   ❓ **Q1** — **<title>**: <body, choices if any>
   ➡️ <recommended answer, grounded in the dump or research>

   ---

   ❓ **Q2** — **<title>**: …
   ➡️ …
   ```

3. Outside the SDLC: while you wait, do the research and look-ups
   every answer needs. None left → end the turn.
4. Recompute the frontier. A question that depends on another question
   still open this round goes in the next round.

Push back on vague words ("probably", "later", "something like").
Propose a strawman they can reject.

Cap the session at four rounds. If round 4 still widens scope, split
the idea and gather one slice. When the frontier holds no "theirs"
question, stop. Also stop when the next question cannot be answered by
talking, for example because it needs a prototype, a screenshot, or a
live system. Mark those questions open; never invent an answer.

### 5. Brief, then stop

1. Emit the brief in this outline:

   ```
   Intent
   Decided              — chose A over B because …; minor calls marked `your call`
   Not yet specified    — in scope, still open; Spec or a Trial settles it
   Out of scope         — rejected, with a lasting reason
   Later                — wanted, deferred to a named later phase
   Constraints
   Assumptions          — now explicit
   Riskiest assumptions — most uncertain first; the top ones are the Trial slice
   Standing permissions — budget, disposable environments, may create, may delete
   Release permission   — its own item; recommend: ship without asking
   HLD review           — yes or no, with the recommendation
   Guardrails we added  — `Guardrail:` lines, or none
   Options map          — only if step 3 ran
   Open                 — "theirs" questions still unanswered
   Verify later         — how we would know a later build matched this
   ```

2. In an SDLC chunk, write the brief to `brief.md` in the chunk's
   design folder ([layout](../sdlc/references/conventions.md#product-repo-layout))
   and hand it to the refiner. Otherwise keep the brief in chat; write
   a file only when the user asks.
3. Outside the SDLC, ask the user to confirm the brief. In the SDLC,
   the manager sends it at touchpoint 1 after Refine:
   [Chunk brief](../sdlc/references/entry-brief-repo.md#chunk-brief).
4. Stop.

## Refine

The **refiner** runs this section on a brief it did not gather. It
makes the brief buildable. It loads no `yagni` and no language skill.
It gets no say on settled answers or on SDLC shape.

1. Sort every requirement into Decided, Not yet specified or Out of
   scope. A requirement the operator asked for that cannot be built now
   → Later; never delete it. Dropping one the operator asked for → a
   "theirs" question.
2. Name each contradiction: the two lines and why both cannot hold. A
   wording satisfies both → propose it. None does → a "theirs" question.
3. Name the riskiest assumptions, most uncertain first. The top ones are
   the Trial slice.
4. Flag each invented requirement: a line no dump sentence, operator
   answer or looked-up fact supports. Propose removing it.
5. Run the three-pile sort of
   [Asking the operator](../sdlc/SKILL.md#asking-the-human) on every open
   question. Write in the answered ones; settle the minor ones as
   `your call`.
6. Return `back to Gather`, with those items as the delta, only when a
   contradiction has no wording that meets both sides, or a drop of a
   requirement the operator asked for has no answer yet. Otherwise
   return `buildable`: Later stays in the brief, and each other
   "theirs" question goes in the touchpoint 1 batch (R91).

## Ask first

- Writing `CONTEXT.md`, an ADR, a ticket, or any file other than the brief, `rulings.md` and `asks.md`.
- Expanding "this idea" into "rebuild the product."
- Calling a builder before the operator confirms the brief.

## Never

- Never implement, scaffold, or "just sketch the API"; emit the brief.
- Never critique the brief in the same turn; the refiner does that.
- Never recommend a tool you have not looked at this session; look first.
- Never name pantheon personas; use only [Roles](../sdlc/SKILL.md#roles).

## Red flags

- "I'll start the questions while you think"
- "Industry standard is X" with no source
- "Let me just write a stub so we can discuss"
- Forty questions with no recommended answers
- Loading language skills "in case we code next"
