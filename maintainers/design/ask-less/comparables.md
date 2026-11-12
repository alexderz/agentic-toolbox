# Comparables — ask less

How other agent skill packs decide when an agent stops to ask, and what
it does instead of stopping. **Before** locking HLD shape.

- Slug: `ask-less`
- Brief / options map: the confirmed brief's options map, "Upstream
  prior art" row (DER-712, 2026-11-11)
- Date: `2026-11-11`

These are the upstream sources the brief names, at the pins it read
them: obra/superpowers `22f0b46` (v7.0.2, MIT), mattpocock/skills
`4ae2317` (MIT), addyosmani/agent-skills `301b02b` (MIT). They enter as
intent credits in `SOURCES.md` only; no third-party body lands (item
A9). A9's **security** read on 2026-11-11 re-read each source at its
pin (clone, no install). The descriptions below are what that read
found. Citations are `path:line` in the upstream repo at the pin. The
read corrected `wayfinder` and `constraint-driven-development`.

## Required

### obra/superpowers: `subagent-driven-development`, `executing-plans`

- **Who / what** — [obra/superpowers](https://github.com/obra/superpowers)
  at pin `22f0b46`, skills `subagent-driven-development`
  (`skills/subagent-driven-development/SKILL.md:17-31`) and
  `executing-plans` (`skills/executing-plans/SKILL.md:27-43`). Read
  2026-11-11. Both files match the description below: rulings, not
  stalls, and four stops.
- **What they did** — The brief credits them with "rulings, not
  stalls": while executing a plan, the agent settles a point itself,
  records the call, and keeps going, and it stops only at a short fixed
  list of stops (the brief counts four).
- **Steal** — W2's `Ruling:` line in place of a stall; W3's short,
  closed list of mid-build returns; W1's rule that the next step the
  plan names is taken, not asked about.
- **Won't copy** — Their stop list as written: ours is derived from
  cost to undo and the what/how test (A1, A2), so it stays the same
  across steps and models. Any wording: credit only.

### obra/superpowers: `brainstorming`

- **Who / what** — [obra/superpowers](https://github.com/obra/superpowers)
  at pin `22f0b46`, skill `brainstorming`
  (`skills/brainstorming/SKILL.md:250-266`). Read 2026-11-11. That
  file matches the description below: a check that sorts open points
  into three piles.
- **What they did** — The brief credits it with a builder check that
  sorts open points into three piles before asking.
- **Steal** — A1's three piles (already answered, minor, theirs), run
  before each question round in `discover-the-idea` and by the refiner
  in its new `## Refine` section.
- **Won't copy** — A sort that stops at "minor": ours splits **what**
  from **how** first, because the Trial showed that a model given only
  cost to undo files product questions as reversible minor points.

### mattpocock/skills: `grilling`, `wayfinder`, `triage`

- **Who / what** — [mattpocock/skills](https://github.com/mattpocock/skills)
  at pin `4ae2317`, skills `grilling`
  (`skills/productivity/grilling/SKILL.md:6-30`), `wayfinder`
  (`skills/engineering/wayfinder/SKILL.md:82-101`) and `triage`
  (`skills/engineering/triage/SKILL.md:70,83-85`;
  `skills/engineering/triage/OUT-OF-SCOPE.md:3-6,62-68`). Read
  2026-11-11.
- **What they did** — `grilling`: an interview method that drives a
  fuzzy idea to decisions; `discover-the-idea` already credits "public
  grilling method" in `SOURCES.md`. The read matches
  `skills/productivity/grilling/SKILL.md:6-30`. `triage`: an
  out-of-scope record, a list of what was rejected and why, kept rather
  than deleted. The read matches
  `skills/engineering/triage/OUT-OF-SCOPE.md:3-6,62-68` and
  `skills/engineering/triage/SKILL.md:70,83-85`. `wayfinder`
  contributes the map's Out of scope section (one line with the reason,
  never graduates) and the Not yet specified / Later bucket
  (`skills/engineering/wayfinder/SKILL.md:82-101`).
- **Steal** — From `wayfinder`: the map's Out of scope section (one
  line with the reason, never graduates) and the Not yet specified /
  Later bucket. That is S1's "defer, don't delete". From `triage`: the
  lasting record of what was rejected and why, kept rather than
  deleted. From `grilling`: front-loading the operator's questions at
  the brief, so Build does not need to come back.
- **Won't copy** — Open-ended grilling rounds and a forced closing
  round: ours sends only "theirs" questions, in one batch, and drops the
  closing round.

### addyosmani/agent-skills: `constraint-driven-development`

- **Who / what** — [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)
  at pin `301b02b`, skill `constraint-driven-development`
  (`skills/constraint-driven-development/SKILL.md:12-16,26,38,44,59`).
  Read 2026-11-11.
- **What they did** — The up-front limits are a written quality bar
  (thresholds and a floor), stated once so later work does not re-argue
  them. They are not permissions
  (`skills/constraint-driven-development/SKILL.md:12-16,26`). The same
  author's Always / Ask first / Never boundary pattern already shapes
  `security-hardening` (`SOURCES.md`).
- **Steal** — Stating the limits of the work once, up front, so the
  agent does not ask about them later. A4 adapts that idea to standing
  permissions collected at the brief. The source's limits stay a
  written quality bar.
- **Won't copy** — Fixed constraint lists as auto-mode stops: auto mode
  here is judgement written as conditions, not a list of stops (T2).

## Optional

- Looked at, not used: no other pack was searched this session (no web
  access). The brief's survey of further packs belongs to Chunk B.
