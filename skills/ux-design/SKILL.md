---
name: ux-design
description: use this when writing user stories, high-level UX, or UI mockups — designer persona; variants in any attached tool or markdown/HTML/canvas; agent review vs requirements then human. do not use to implement, apply reviewer taste, or skip the human gate.
---

# UX design

**designer** skill. Stories and how it feels, not the Spec (LLD).
Templates: `user-story.md`, `ux.md`, `mockup.md`, `comparables.md`. No
`scripts/`. No language skill on a UX-only turn.

Inspired by Pocock UI variants (structurally different options), Addy
anti-“AI default” UI, hueyexe composition (hierarchy, states, explain
as function not taste). Not those packs.

## Iron law

**Agents agree the design meets the written requirements. Then the
human accepts — unless they waive in writing.** Designer, architect, and
builder do not self-approve. Agent reviewers do **not** apply their own
taste.

## Medium (mockups)

The job is a **deliverable in git** the human can look at. Pick **one**
medium this agent can actually produce. Do not stall for a plugin.

| Medium | When |
| --- | --- |
| Markdown wireframe | Always works. Default if nothing else is attached |
| HTML/CSS in `docs/mockups/` | Best “click around” without a design tool |
| Canvas / JSON canvas | Spatial flows |
| Image | Mood/layout when HTML is overkill |
| Attached design tool (Figma, Stitch, Penpot, …) | Only if that tool is on **this** agent. Store the link **and** a git snapshot (PNG or HTML) |

If HTML lives in an existing app, variants on one route (`?variant=`)
are fine. Prototype code is not production — fold the winner later via
`tdd`.

## Variants

For a screen, default **3** structurally different options (cap 5).
Different layout, hierarchy, or primary action — not three color tweaks.
If two look the same, redo one. Label A/B/C. After a winner, keep the
set in git until the human has picked; then keep the winner, drop the
rest from the live path.

## Produce (designer)

0. **Comparables** — 2–4 real products/screens (`comparables.md`): steal
   / won’t copy. Same page as the architect, plus look-and-flow.
1. Feature and stories first, chrome last.
2. Hierarchy in structure (and grayscale if visual) before color.
3. Empty / error / loading named or pictured.
4. Avoid AI-default look unless the brief asked for it: purple/indigo
   everything, heavy gradients, max rounding, generic hero, cookie
   Inter-on-white. Use the product palette if one exists.
5. Color is not the only signal. Familiar controls unless the brief
   wants novelty.
6. Explain choices as task fit, not “I like it.”

Resume the same **designer** on later rounds.

## Review loop (agents, then human)

1. **Designer** produces (stories, comparables for look/flow if there
   are screens, then mockup variants).
2. **UX reviewer** — a **different** subagent, not the designer. Resume
   `ux_reviewer_id`. Reads brief, stories, and written taste/shape
   **if those are requirements**. Checks:
   - Can the person finish the job in the stories?
   - Empty/error/loading covered?
   - Matches stated constraints (brand, density, platform)?
   - Variants are actually different?
   Does **not** add “I would use more whitespace” unless the write-up
   asked for that shape.
3. Designer fixes. Loop until the reviewer agrees it meets the
   **requirements** (or they disagree and need the human).
4. **Then** ask the human ([Asking the
   human](../../docs/SDLC.md#asking-the-human)): show variants, say
   which the agents recommend and why (requirements, not taste), what
   to reply. Do not continue UX until they answer — unless they already
   wrote `UX verification not required`.

## Always

- Copy templates. Link brief, HLD, stories, mockups.
- One job per story. Checkable “done when.”
- Agent review before human, except a written waiver.
- If UI changes in Build, update stories/mockups in the same land.

## Ask first

- Skipping mockups or comparables when there is a screen, without a written waiver.
- Fighting an existing product UI with a new visual system.

## Never

- Implement the product as the mockup.
- Reviewer taste, or “the architect liked it.”
- Fake screenshots. One medium with nothing in git.
- Load a language skill “so we can code the screen next.”
- Show the human before agents agree, unless they asked to see drafts.

## Red flags

- “We’ll show the human after it works”
- Three variants that are the same card grid
- Reviewer rewriting the palette with no requirement
