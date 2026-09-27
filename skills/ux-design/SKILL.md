---
name: ux-design
description: use this when writing user stories, high-level UX, or UI mockups — designer persona; variants in any attached tool or markdown/HTML/canvas; agent review vs requirements then operator. do not use to implement, apply reviewer taste, or skip the operator gate.
---

# UX design

**designer** skill. Stories and how it feels, not the Spec (LLD).
Templates (`sdlc-artifacts`): `user-story.md`, `ux.md`, `mockup.md`,
`comparables.md`. No `scripts/`. No language skill on a UX-only turn.

Inspired by Pocock UI variants (structurally different options), Addy
anti-“AI default” UI, hueyexe composition (hierarchy, states, explain
as function not taste). Not those packs.

## Iron law

**Agents agree the design meets the written requirements. Then the
operator accepts — unless they waive in writing.** Designer, architect,
and builder do not self-approve. Agent reviewers do **not** apply their
own taste.

## Medium (mockups)

The job is a **deliverable in git** the operator can look at. Pick
**one** medium this agent can actually produce. Do not stall for a
plugin.

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
set in git until the operator has picked; then keep the winner, drop the
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

Designer and UX reviewer ids, and resume across rounds:
[Step agents](../../docs/sdlc/subagents.md#step-agents).

## Review loop (agents, then operator)

Loop and operator acceptance: [UX](../../docs/sdlc/plan-trial-spec.md#ux).

1. **UX reviewer** reads the brief, the stories, and written taste/shape
   **if those are requirements**. Checks:
   - Can the user finish the job in the stories?
   - Empty/error/loading covered?
   - Matches stated constraints (brand, density, platform)?
   - Variants are actually different?
   Does **not** add “I would use more whitespace” unless the write-up
   asked for that shape.
2. Designer fixes; the UX reviewer re-checks until those agents agree.
   If they disagree on the requirements, ask the operator ([Asking the
   operator](../../docs/SDLC.md#asking-the-human)).
3. When the agents agree, ask the operator the same way: show the
   variants and say which the agents recommend and why (requirements,
   not taste).

## Always

- Copy templates. Link brief, HLD, stories, mockups.
- One job per story. Checkable “done when.”
- Agent review before the operator, except a written waiver.
- If UI changes in Build, update stories/mockups in the same land.

## Ask first

- Skipping mockups or comparables when there is a screen, without a written waiver.
- Fighting an existing product UI with a new visual system.

## Never

- Implement the product as the mockup.
- Reviewer taste, or “the architect liked it.”
- Fake screenshots. One medium with nothing in git.
- Load a language skill “so we can code the screen next.”
- Show the operator before agents agree, unless they asked to see drafts.

## Red flags

- “We’ll show the operator after it works”
- Three variants that are the same card grid
- Reviewer rewriting the palette with no requirement
