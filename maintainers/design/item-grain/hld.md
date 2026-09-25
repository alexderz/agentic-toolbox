# HLD — Item grain, named steps, language pass

- Slug: `item-grain`
- Track / chunk ids: skills-home process track; chunk `item-grain`
- Brief: confirmed after Refine (gather session 2026-09-18)
- Date: `2026-09-18`

## Required

- **Problem** — The SDLC is written as if every ask is a new chunk
  (interview → new HLD → new LLD → tickets). Incoming bugs, red builds,
  and unit failures have no honest path. Stage numbers (−3, −2, 0, 4)
  collide when a step is inserted and confuse in-flight work. Meal
  metaphor leaked into agent-facing steps. Process prose reads as
  software-only.

- **Goals**
  1. One process. Board layers stay Track / Chunk / Item. Entry
     classifies **chunk vs item** (a new track is a chunk that also
     writes `track.md`).
  2. Chunk: interview, **write** Plan and Spec. Item: problem + fix vs
     removal, **align** Plan and Spec, then the same implement loop.
  3. Promote when the item is a plan change, user-visible taste, or
     surprisingly large. Block **that** issue; siblings proceed.
  4. Step ids are **names**. In-flight map for old numbers. No
     gap-numbers.
  5. Meal metaphor only in “How software gets built.” Technical docs and
     skills: engineering / problem-solving language. Process applies to
     software, docs, process, and other tickets using this home.
  6. Whole-repo language pass: grep the tree; edit process surfaces and
     real leaks; do not rewrite language packs, Makefile recipes, or
     session cookies.

- **Non-goals** — New skill ids; hotfix process; new Linear types or a
  required workflow state; changing `discover-the-idea`; skipping tests,
  security, or Review; renaming `hld.md` / `lld.md`; a ninth role;
  item-Brief on Tasks already split from an accepted Spec.

- **Users / operators** — Agents running this SDLC; the operator who
  accepts write-ups and waives gates.

- **UX / stories** — `n/a` — no screens. Designer loop not used on this
  chunk.

- **Comparables** — [comparables.md](comparables.md)

- **Shape**
  - **Entry** — classify chunk vs item, or ask. No template, no
    subagent.
  - **Brief (item)** — troubleshooter (architect + optional `debug`)
    writes problem + proposed fix. A **different** agent (`yagni`)
    proposes a removal. Parent picks. Ask the human when taste or size
    is in play (`blockedBy` + ask-human).
  - **Plan / Spec (item)** — honor / clarify / escalate. Clarification
    in place. Shape change → chunk.
  - **Groom (item)** — this ticket; do not split unless promoting. No
    chunk: branch from trunk, Review vs trunk, merge-and-delete.
  - **Build / Review / Trunk / Changelog / Monthly** — same gates,
    named.
  - Language: lay section keeps food and adds leftover vs from-scratch.
    Everywhere else: named steps, no meal words for the process.

- **Persistence** — Git: this dir, `docs/SDLC.md`, `AGENTS.md`,
  `README.md`, `docs/ARCHITECTURE.md`, templates, process-skill notes.
  Board optional (no tickets required in this skills home).

- **Worker rules** — Parent may be the troubleshooter if the session is
  this item and not dirty; never the yagni agent, builder, or verifier
  of that item. Builder ≠ verifier ≠ Reviewer. Workers do not bypass
  security. Autonomous/AFK may pick between two item fixes that honor
  the plan; must not change HLD/LLD shape.

- **Open** — In-flight map is deleted after tickets that still say
  “Stage 4” have landed. Land path vs `sdlc/ux-review-loop` is a manager
  call at land, not this Plan.

## Optional

- Alternatives rejected: skip-design-for-bugs; ITIL three-process split;
  hotfix SDLC; gap-numbers (10, 20, …); `Recipe` as a step id.
- Risks: agents still say “Stage 4”; item path used to avoid the human
  — Entry and Plan/Spec escalate those.
