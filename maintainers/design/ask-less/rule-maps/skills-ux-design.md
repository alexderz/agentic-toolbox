# Rule map — `skills/ux-design/SKILL.md`

Item: DER-739 (A7 of DER-712). Procedure:
[A7](../lld.md#a7--design-gate-and-hld-touchpoint).

Old: `skills/ux-design/SKILL.md` at main c26f424, lines 1–109.
New: `skills/ux-design/SKILL.md`, 109 lines.

A0 rewrote three links and did not change line numbers. A7 replaces
step 3 of the review loop (old L81–83). Old L79–80 stays. Rows below
cover every non-blank old line.

**security** reads this body at Review.

Key: **kept**, **route**, **dropped** (owner named), **DER-265**,
**DER-271**. No row uses DER-265 or DER-271.

Clarifications (operator, 2026-09-27): the frontmatter `description`
is metadata (Q16), not a second copy of a rule. This file has no
groom-review round.

This item edits no protected-rules row. Ask first and Never in this
file stay as they are.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–4 | Frontmatter. `description` is metadata (Q16) | kept | L1–4 |
| 6 | Title | kept | L6 |
| 8–10 | **designer** skill. Stories and how it feels, not the Spec. Template names. No `scripts/`. No language skill on a UX-only turn | kept | L8–10 |
| 12–14 | Inspiration note. Not those packs | kept | L12–14 |
| 16 | Heading Iron law | kept | L16 |
| 18–21 | Agents agree the design meets the written requirements. Then the operator accepts, unless they waive in writing. No self-approve. Reviewers do not apply their own taste | kept | L18–21 |
| 23 | Heading Medium | kept | L23 |
| 25–27 | The job is a deliverable in git. Pick one medium this agent can produce. Do not stall for a plugin | kept | L25–27 |
| 29–35 | Medium table | kept | L29–35 |
| 37–39 | If HTML lives in an existing app, a variant query is fine. Prototype code is not production | kept | L37–39 |
| 41 | Heading Variants | kept | L41 |
| 43–47 | Default 3 structurally different options, cap 5. Label A/B/C. Keep the set until the operator has picked; then keep the winner | kept | L43–47 |
| 49 | Heading Produce | kept | L49 |
| 51–61 | Produce steps 0–6: comparables, stories before chrome, hierarchy before color, empty / error / loading, avoid an unrequested AI-default look, color is not the only signal, explain choices as task fit | kept | L51–61 |
| 63–64 | Designer and UX reviewer ids, and resume across rounds | kept. A0 rewrote the link to `../sdlc/references/subagents.md#step-agents` | L63–64 |
| 66 | Heading Review loop | kept | L66 |
| 68 | Loop and operator acceptance | route to `skills/sdlc/references/plan-trial-spec.md#ux`. A0 rewrote the link | L68 |
| 70–77 | **UX reviewer** reads the brief, the stories, and written taste or shape when those are requirements. Checks the job, empty / error / loading, stated constraints, and that variants differ. Does not add taste | kept | L70–77 |
| 78 | Designer fixes; the UX reviewer re-checks until those agents agree | kept | L78 |
| 79–80 | If they disagree on the requirements, ask the operator | kept (A7). A0 rewrote the link on L80 | L79–80 |
| 81–83 | When the agents agree, ask the operator: show the variants and say which the agents recommend and why | route (A7) to `skills/sdlc/references/plan-trial-spec.md#ux`. The variants go to the operator at the design gate, with the agents' pick and why | L81–83 |
| 85 | Heading Always | kept | L85 |
| 87–90 | Copy templates. One job per story. Agent review before the operator, except a written waiver. If UI changes in Build, update stories and mockups in the same land | kept | L87–90 |
| 92 | Heading Ask first | kept | L92 |
| 94–95 | Skipping mockups or comparables when there is a screen, without a written waiver. Fighting an existing product UI with a new visual system | kept | L94–95 |
| 97 | Heading Never | kept | L97 |
| 99–103 | Do not implement the product as the mockup. No reviewer taste. No fake screenshots. Do not load a language skill to code the screen. Do not show the operator before agents agree, unless they asked to see drafts | kept | L99–103 |
| 105 | Heading Red flags | kept | L105 |
| 107–109 | Red flags: showing the operator only after it works; three variants that are the same card grid; a reviewer rewriting the palette with no requirement | kept | L107–109 |

## Meaning questions

No open question.

- **MQ1** — Old L81–83 told the designer to ask the operator once the
  agents agree. The new step sends the variants to the design gate and
  links the UX owner. Resolved from the accepted A7 text. Old L79–80
  stays: a disagreement on the requirements is a question for the
  operator, and A7 calls that a "theirs" question.
