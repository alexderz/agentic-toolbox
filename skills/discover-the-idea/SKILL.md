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
In the SDLC, **the user** is the operator.

## Iron law

**Do not write the thing. Surface the thing.** The user owns every
Always-theirs and "theirs" question
([Asking the operator](../sdlc/SKILL.md#asking-the-human)).
Settle a minor point yourself: write it in the brief marked `your call`.
`your call` means you settled it without asking; the user may still
change it. In an SDLC chunk, also log it as a ruling in `rulings.md`.
You own facts. The session ends in a brief.

## Loop

### 0. Dump (always first)

1. If the thread already holds a **dump**, the user's unsorted text
   about the idea, for example in the invoking message, use that text
   as the dump and go to step 1.
2. Otherwise, in an SDLC chunk: end your turn and report to the
   **manager** that you need the dump; send the user nothing. Outside the
   SDLC, send this and nothing else:

   > Dump whatever is in your head about this. Messy is the point. Goals,
   > fears, constraints, half-ideas, things you already rejected, what
   > "done" might look like. I will not interrogate until you send it.

3. Wait for the dump. Send no questions in that message.

### 1. Reflect

1. Restate the dump in one short paragraph, in the user's words,
   tightened, and name what is still vague.
2. In an SDLC chunk, put the restatement under Intent in the brief; the
   operator corrects it at touchpoint 1. Outside the SDLC, put it at the
   top of the first question round, or in the brief when no question is
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

Resumed with a refiner's delta → each delta item is a frontier question.

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
live system. Put those questions under Not yet specified; never invent
an answer.

### 5. Brief, then stop

1. Emit the brief in this outline:

   ```
   Intent               — the restatement of the dump
   Decided              — chose A over B because …; minor calls marked `your call`
   Not yet specified    — in scope, still open; Spec or a Trial settles it
   Out of scope         — rejected, with a lasting reason; or `no source`, `your call`
   Later                — wanted, deferred to a named later phase
   Constraints
   Assumptions          — now explicit
   Riskiest assumptions — most uncertain first; the top ones are the Trial slice
   Standing permissions — SDLC chunk: budget, disposable environments, may create, may delete
   Release permission   — SDLC chunk: its own ask; recommend: ship without asking
   HLD review           — SDLC chunk: yes or no, with the recommendation
   Guardrails we added  — `Guardrail:` lines, or none
   Options map          — only if step 3 ran
   Open                 — "theirs" questions still unanswered, each with its ask id
   Verify later         — how we would know a later build matched this
   ```

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
