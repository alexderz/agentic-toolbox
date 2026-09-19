# LLD — Item grain, named steps, language pass

- Slug: `item-grain`
- HLD: `docs/item-grain/hld.md`
- Tickets this LLD covers: this chunk (no board ticket)
- Date: `2026-09-18`

## Required

- **Paths / modules**
  - `docs/SDLC.md` — grain, named steps, in-flight map, lay extension
  - `docs/item-grain/` — this Plan / Spec / comparables
  - `docs/ARCHITECTURE.md`, `docs/INTAKE.md`,
    `docs/CHERRY-PICK-CANDIDATES.md` (historical heading only)
  - `AGENTS.md`, `README.md`, `SOURCES.md`
  - `skills/sdlc-artifacts/SKILL.md` and templates `bug.md`, `task.md`,
    `hld.md`, `lld.md`, `chunk.md`, `changelog.md`, `track.md`
  - Process skills that cited old numbers or called LLD a “recipe”:
    `ux-design`, `pr-review`, `verify-before-done`, `security-hardening`
  - Do **not** edit `lang-*`, Makefile “recipe,” or session-cookie
    rules except if a file cites `Stage N` (none do).

- **Behavior**
  - Step headings are names (`### Build`). One order table. In-flight
    map is the only place old numbers are taught.
  - Incoming item: Entry → item Brief (two agents + pick) → align Plan
    and Spec → Build / Review / land. Groomed Tasks skip item-Brief.
  - Human wait is a blocker on that issue.
  - Meal words only under `## How software gets built`.
  - Process intro: not software-only.

- **Trust boundaries** — `n/a`. Documentation in this skills home. No
  authn/z, secrets, egress, or new writers. **security** still reads
  this. Skill-home SHA/intake rules unchanged.

- **Mockups** — `n/a` — no screen. Operator does not wait on UX.

- **Verify**
  - `rg -n 'Stage [−0-9]|Stage −' --glob '*.md'` — hits only in the
    in-flight map in `docs/SDLC.md`, plus this chunk’s HLD/LLD
    describing that map. No skill, template, AGENTS, README, SOURCES,
    or ARCHITECTURE file teaches old numbers as current ids.
  - `rg -n '\\b(recipe|platter|dish|cook|dinner|kitchen|taster)\\b' --glob '*.md'`
    — process-metaphor sense only in `docs/SDLC.md` lay section;
    Makefile `recipe` and HTTP cookies unchanged.
  - Templates `bug.md` / `task.md` contain Out of scope, Proposed fix,
    Removal alternative, Pick, Plan / Spec.
  - `ux-design` does not call the Spec a recipe.

- **Land** — branch `sdlc/item-grain`; merge-and-delete after Review
  unless more items are in flight on a project-main. No ticket ID.
