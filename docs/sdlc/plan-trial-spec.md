# Plan, Trial, and Spec

## Plan

**architect** commits the HLD to git; **manager** posts its path on the
Epic with `tracker-sdlc` `comment`. Lock hierarchy,
persistence, and worker rules. Use `sdlc-artifacts` templates `hld.md`
and `track.md` / `chunk.md`.

**Item:** do not write a new HLD. Read the existing one. **manager**
posts `honors` / `clarification` (small, in place) / `escalate` on the
ticket with `tracker-sdlc` `comment`. A real shape
change (new parts, new trust boundary, new screen, several tickets) is
an escalation to a chunk, not a quiet HLD edit. Nothing to align to:
ask (stub vs promote). This skills home: `docs/ARCHITECTURE.md` + this
file count as the plan when the change is the process itself.

### Comparables

**Comparables.** Before locking shape, **architect** (and **designer**
if there are screens) look at **how others have done it**: 2–4 real
examples (`comparables.md`). For each: who, what they did, what we
steal, what we will not copy, a link. Reuse the brief’s options map if
it exists — still write this page. Skip only if the operator waives
look-around in writing ([Asking the human](../SDLC.md#asking-the-human)). No
invented “industry standard.”

**Never**

- Lock Plan shape without 2–4 real comparables, unless the operator
  waived look-around in writing.

### UX

**UX (designer).** Same step: high-level UX and user stories
(`ux-design`, templates `ux.md` / `user-story.md`). Not the Spec.
**Loop:** designer produces → a **different** agent reviews against the
written requirements (function and any stated taste/shape — not the
reviewer’s taste) → designer fixes until those agents agree → **then**
the **operator** accepts (or writes `UX verification not required`).
Architect and designer do not self-approve. Skip mockups here — those
are Spec if there is a screen.

**Never**

- Treat designer or architect self-OK as the UX gate, or skip mockups
  for a screen without a written `UX verification not required`.

## Trial

Only if needed. Evidence in git. Template: `poc.md`.

**Item:** skip unless the chosen fix is itself uncertain.

## Spec

Entry gate: `tracker-sdlc` setup check (offline). Fail →
`sdlc-onboarding` first.

**architect** commits the LLD to git; **manager** posts its path on the
Epic with `tracker-sdlc` `comment`. Use template `lld.md` (trust-boundary section is
required; `n/a` + why if none).

**Accept the LLD** (architect + **security** on trust boundaries) before
Groom/Build. If people see a screen, **designer** mockups (`mockup.md`)
are part of Spec. The **operator** accepts those mockups (or writes
`UX verification not required`) before Groom. Then
[Documentation](#documentation) is in force.

**Item:** align to the existing LLD the same way as Plan. Clarification
in place; shape change → escalate. Security still reads the
trust-boundary note (`n/a` + why if the item does not touch a boundary).

### Mockups

**Mockups (designer).** If people see a screen, produce **2–3
structurally different** mockups (`ux-design`, `mockup.md`) in whatever
medium this agent has (markdown, HTML, canvas, image, or an attached
design tool — plus a git snapshot). Same review loop as Plan: agents
agree it meets requirements, **then** the **operator** accepts (or
writes `UX verification not required`). No screen: `n/a` and why — do
not invent pictures.

### Security gate

**security gate (trust boundaries):** before Groom/Build, **security**
reviews the LLD for trust boundaries (authn/z, secrets, egress, data
class, who may write what). This is a gate, not a later monthly note. Do
not skip to Build without it when the change touches a boundary.

## Documentation

Once the LLD is accepted, builders keep docs current through land. Two
surfaces — do not mix their jobs:

| Surface | Where | Skill | Job |
| --- | --- | --- | --- |
| **Human** | `docs/` how-tos, README usage | `docs-google-style` + template `human-doc.md` | What this is, how it works, how to use it |
| **Agent** | In-code comments, AGENTS pointers, module maps | `docs-google-style` (agent extras) | Locatable contracts for future agents: name, when, inputs, outputs, side effects, where to look next |

Human docs are for people. Agent notes are enablement, not tutorials.
Do not paste the SDLC into product docs. Update both in the same land as
the change. Build DoD includes docs current with the item.

Skills, templates, and other technical docs use engineering words. Do
not reuse the layperson analogies outside
[How software gets built](../how-software-gets-built.md).
