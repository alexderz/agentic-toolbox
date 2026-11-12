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
A9). This session had no web access: each description below comes from
the brief and `SOURCES.md`, and is marked **not re-read this session**.
A9's **security** read re-reads each source at its pin before the
credits land and corrects this page if a description is wrong.

## Required

### obra/superpowers: `subagent-driven-development`, `executing-plans`

- **Who / what** — [obra/superpowers](https://github.com/obra/superpowers),
  skills `subagent-driven-development` and `executing-plans`.
  Re-read by **security** at the pin on 2026-11-12 (A9): holds.
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

- **Who / what** — [obra/superpowers](https://github.com/obra/superpowers),
  skill `brainstorming`. Re-read by **security** at the pin on 2026-11-12 (A9): holds.
- **What they did** — The brief credits it with a builder check that
  sorts open points into three piles before asking.
- **Steal** — A1's three piles (already answered, minor, theirs), run
  before each question round in `discover-the-idea` and by the refiner
  in its new `## Refine` section.
- **Won't copy** — A sort that stops at "minor": ours splits **what**
  from **how** first, because the Trial showed that a model given only
  cost to undo files product questions as reversible minor points.

### mattpocock/skills: `grilling`, `wayfinder`, `triage`

- **Who / what** — [mattpocock/skills](https://github.com/mattpocock/skills),
  skills `grilling`, `wayfinder` and `triage`.
  Re-read by **security** at the pin on 2026-11-12 (A9): holds.
- **What they did** — `grilling`: an interview method that drives a
  fuzzy idea to decisions; `discover-the-idea` already credits "public
  grilling method" in `SOURCES.md`. `triage`: the brief credits its
  out-of-scope record, a list of what was rejected and why, kept rather
  than deleted. `wayfinder`: named by the brief as an intent source;
  what it contributes was not recorded in the brief, so this page
  claims nothing for it until A9's read.
- **Steal** — From `triage`: S1's "defer, don't delete" and the brief's
  Out of scope (with a lasting reason) and Later buckets. From
  `grilling`: front-loading the operator's questions at the brief, so
  Build does not need to come back.
- **Won't copy** — Open-ended grilling rounds and a forced closing
  round: ours sends only "theirs" questions, in one batch, and drops the
  closing round.

### addyosmani/agent-skills: `constraint-driven-development`

- **Who / what** — [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills),
  skill `constraint-driven-development`.
  Re-read by **security** at the pin on 2026-11-12 (A9): holds.
- **What they did** — Named by the brief as an intent credit. The brief
  does not record which part it uses. The same author's Always / Ask
  first / Never boundary pattern already shapes `security-hardening`
  (`SOURCES.md`).
- **Steal** — Stating the limits of the work once, up front, so the
  agent does not ask about them later: A4's standing permissions
  collected at the brief. This reading is an inference from the skill's
  name and the brief's use; A9 confirms or drops it.
- **Won't copy** — Fixed constraint lists as auto-mode stops: auto mode
  here is judgement written as conditions, not a list of stops (T2).

## Optional

- Looked at, not used: no other pack was searched this session (no web
  access). The brief's survey of further packs belongs to Chunk B.
