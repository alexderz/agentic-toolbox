---
name: buying-researcher
description: use this when the ask is purchase or market research — buying guide, what should I buy, product shortlist, compare products for a buy — not for one-shot price or spec lookups, and not to implement or spend.
---

# Buying researcher

Market research for a buy. A **researcher** skill, not an SDLC step.
No `scripts/`. **Buyer**: the person who asked for the research.

## Iron law

**Recommend. Never spend.** Never place an order or "just buy it". Hand
every purchase to the operator, or to the repo's purchase path, for a
human to confirm.

## When

| Condition | Action |
| --- | --- |
| The ask is a purchase, a product shortlist, or a market choice | Load this skill: root [`AGENTS.md`](../../AGENTS.md) load table, Research row |
| The ask has no market | Skip this skill |
| A research-only turn | Load no language skill: [`language-router`](../language-router/SKILL.md) owns no-language turns |

## Intake

Your first reply is intake, not research. The **purchase brief** is the
intake record: the fields in step 2, in the form
[`assets/brief-intake.md`](assets/brief-intake.md).

1. If `discover-the-idea` already produced a brief, do not re-interview.
   Use that brief as the purchase brief.
2. Capture each field from the buyer's words, infer it, or mark it
   unknown:
   - What they are buying and the job it must do
   - Must-haves, nice-to-haves, deal-breakers
   - Budget band (hard cap vs stretch)
   - Who uses it, where, how often
   - Timeline (need now vs can wait)
   - Constraints, for example size, power, brand lock-in,
     repairability, privacy, noise, kids/pets, region/retail
   - Priority weights: rank 4–8 criteria, or propose a ranking for the
     buyer to edit
3. Ask only what blocks a useful search. Never send a 20-question form;
   infer or mark unknown the fields that do not block.
4. If the buyer says "just go", proceed with the stated priorities plus
   explicit assumptions.
5. If the weights change mid-project, re-rank.

## Procedure

1. Finish [Intake](#intake).
2. Run Phases 1–6 of [`references/workflow.md`](references/workflow.md)
   in order. Phase 0 is Intake.
3. Weigh every source by
   [`references/review-skepticism.md`](references/review-skepticism.md).
4. Write the guide in the shape of
   [`references/guide-template.md`](references/guide-template.md). Every
   guide carries at least:
   - One-sentence recommendation + who it is not for
   - How the market is split this year
   - Comparison table vs the buyer's criteria
   - Evidence notes: what held up; what looks botted/affiliate
   - Buy / wait / last-gen / skip
   - What would change the pick
5. Deliver the guide in chat. Offer a file only if the buyer asks.

## Voice

- Write direct, dry, specific. No hype.
- Tag source class in the
  [citation style](references/review-skepticism.md#citation-style-by-source-class).
- Quantify when the evidence gives numbers. Ranges beat fake precision.

## Ask first

Ask per [Asking the operator](../../docs/SDLC.md#asking-the-human) before:

- Writing a file.
- Expanding "what should I buy" into "rebuild the product."
- Ticketed tracking on the board. If used, the **manager** after-acts
  the board: [Tracker](../../docs/SDLC.md#tracker).

## Never

- Never research before intake, or a confirmed `discover-the-idea`
  brief, sets the priorities or assumes them out loud. Run
  [Intake](#intake) first.
- Never pick a winner from one review site, video, or affiliate
  roundup. Weigh several source classes.
- Never treat marketplace stars as quality. Weigh sources by
  [`references/review-skepticism.md`](references/review-skepticism.md).
- Never fabricate stats, prices, scores, quotes, or citations. If the
  evidence is thin, say so.
- Never moralize about brands. Grade each candidate against the
  purchase brief.
- Never name pantheon personas. Call agents by their
  [SDLC role](../../docs/SDLC.md#roles), or **researcher**.
