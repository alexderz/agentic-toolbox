# Entry, Brief, and Repo

## Entry

Classify: **chunk** (needs a person for taste, opinions, or a design
talk) or **item** (mechanical, tactical, immediate). Examples of item:
broken build, unit failure, a UI bug report until analysis shows it
needs taste.

Unclear: a short look — can we reproduce it, and does the fix need a
design choice? If still unclear, **ask**. Do not implement here.

Read-only: classify from what you were handed. No template, no
subagent, no tracker write. The classification line goes on the ticket
at Brief.

## Brief

Before Plan.

### Chunk brief

**Chunk — Gather ↔ Refine.** Skip only when a confirmed brief already
exists for this chunk. Loop until the operator confirms a brief that
Refine did not send back. Do not implement in this step.

**Gather** — load
[`discover-the-idea`](../../skills/discover-the-idea/SKILL.md). That skill
owns the interview, environment facts, options map, and the brief.
**Read it** (or pack it into the gatherer prompt). Do not copy or
paraphrase its loop here; the skill will change.

**Refine** — a **different** subagent from the gatherer. Load `yagni`.
Question necessity. Make the brief less stupid and simpler. First
principles: from the dump and looked-up facts, not from a product
template. If a requirement dies or new fog appears, return to Gather
with the delta (resume the gatherer).

Mint a clean **gatherer** and a clean **refiner** on the first pass of
this chunk; resume those ids on later rounds. Never the same agent for
both. No language skill on a gather- or refine-only turn.

Plan is written from the confirmed brief, not from a raw dump.

**End of chunk Brief.** Cut project-main `integrate/<chunk-slug>` from
trunk. Run the `tracker-sdlc` setup check (fail → load
[`sdlc-onboarding`](../../skills/sdlc-onboarding/SKILL.md), which writes
the tracker files first). Get the Epic (`backlog`): if the chunk
arrived as a tracker ticket, use that ticket as the Epic (ask the
operator to relabel it if its type differs; never duplicate it);
otherwise **manager** files it with `tracker-sdlc` `create`. If
onboarding ran, commit it as `[<epic-id>] Onboard tracker: <Tracker>`
on an item branch cut from project-main and land it on project-main
as its own item through Review **before Plan**: a short item with its
own **verifier**, **reviewer**, and **security** read of the repo skill
(never a bare commit).
**manager** posts the Entry classification on the Epic with
`tracker-sdlc` `comment`.

### Item brief

**Item (arrives as Task or Bug).** Always run this path unless the
ticket is `n/a — split from accepted Spec` (those start at Build). A
confirmed brief on the parent chunk does **not** skip item-Brief.

0. Cut `item/<ticket-id>-<slug>` (from the live project-main, else
   trunk). Run the `tracker-sdlc` setup check (fail →
   `sdlc-onboarding`). **manager** posts the Entry classification on
   the ticket with `tracker-sdlc` `comment`.
1. **Troubleshooter** (architect hat) writes **problem + proposed fix**
   and out of scope. May load `debug` (one of `debug` / `debug-pocock` /
   `debug-anthropic`) through root cause / hypothesis only — do **not**
   run the fix phase, `tdd`, or land. The parent session may do this
   when it is already that item and not too dirty to reason; otherwise
   mint a clean troubleshooter.
2. A **different** agent loads `yagni` only. Competing fix that
   **removes** something (revert, delete a path, drop a part of the
   plan). Honor the existing HLD, or propose removing a **part** of it
   (that is an escalation). Never “delete the product.” If there is no
   honest removal path: `none — already smallest`.
3. The **parent** (not the troubleshooter, not the yagni agent) picks
   and records why.
4. **Ask the human** if the two options would look different to a user
   or if either is a plan change. If the parent *is* the troubleshooter
   or the yagni agent, mint a clean parent-pick (or ask) — do not let
   one of those two choose. That wait is a blocker on **this** issue
   unless the operator already wrote AFK / headless / autonomous, in
   which case the parent may pick **between** two item fixes that both
   honor the plan (see [Asking the human](../SDLC.md#asking-the-human)). Other
   items proceed.

Store `contrarian_id` (the yagni agent) on the item; resume it if the
debate has another round. Do not add a ninth role.

## Repo

Before Plan:

- Repo or subdir exists (private as needed).
- README / AGENTS stub so agents who need access are aware (layout:
  [Conventions](conventions.md#name-formats); stub template
  `agents-stub.md`).
- **tester** watch if applicable.
- **Designs live in git from onset.**

**Item:** confirm the workspace exists. Do not reinvent it.
