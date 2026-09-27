# Plan, Trial, and Spec

## Plan

1. **architect** writes the HLD with `sdlc-artifacts` templates `hld.md`
   and `track.md` / `chunk.md`.
2. **architect** locks hierarchy, persistence, and worker rules in the
   HLD.
3. **architect** commits the HLD to git.
4. **manager** posts the HLD path on the Epic with `tracker-sdlc`
   `comment`.

**Item:** do not write a new HLD. Read the existing one. **manager**
posts one verdict on the ticket with `tracker-sdlc` `comment`:

| The item | Verdict |
| --- | --- |
| Honors the existing HLD | `honors` |
| Needs a small clarification, made in place | `clarification` |
| Changes shape: for example new parts, a new trust boundary, a new screen, several tickets | `escalate` to a chunk. Never edit the HLD quietly for a shape change. |
| Has no HLD to align to | Ask the operator ([Asking the operator](../SDLC.md#asking-the-human)): stub or promote. |

In this skills home, when the change is the process itself,
`docs/ARCHITECTURE.md` and the SDLC ([`docs/SDLC.md`](../SDLC.md) and
its step files) count as the plan.

### Comparables

Before locking shape, **architect** looks at how others have done it.
If there are screens, **designer** looks too.

1. Find 2–4 real examples.
2. Write the comparables page with template `comparables.md`.
3. For each example, write: who, what they did, what we steal, what we
   will not copy, a link.
4. If the confirmed brief has an options map, reuse it. Still write this page.
5. Cite only the real examples. Never invent an "industry standard".

Skip this page only if the operator waives look-around in writing
([Asking the operator](../SDLC.md#asking-the-human)).

**Never**

- Lock Plan shape without 2–4 real comparables, unless the operator
  waived look-around in writing. Write the comparables page first.

### UX

**designer** writes high-level UX and user stories in this same step
(`ux-design`, templates `ux.md` / `user-story.md`). This is not the
Spec. Do not make mockups here. If there is a screen, mockups are part
of Spec.

**Review loop.** UX work and mockups both pass this loop:

1. **designer** produces the work.
2. A **different** agent reviews it against the written requirements:
   function, and any stated taste or shape. The reviewer's own taste is
   not a requirement.
3. **designer** fixes the findings. Repeat steps 2–3 until the designer
   and the reviewing agent agree the work meets the requirements.
4. **operator** accepts the work, or writes `UX verification not
   required`. For mockups, this happens before Groom.

**Never**

- Treat designer or architect self-OK as the UX gate. Architect and
  designer do not self-approve. The gate is step 4, after a different
  agent's review.
- Skip mockups for a screen without a written `UX verification not
  required`. Make the mockups, or get that line from the operator.

## Trial

The Trial is optional proof. Run it only if needed. Keep its evidence in
git. Use template `poc.md`.

**Item:** skip the Trial unless the chosen fix is itself uncertain.

## Spec

Entry gate: run the offline `tracker-sdlc` setup check. If it fails, run
`sdlc-onboarding` first.

1. **architect** writes the LLD with template `lld.md`. The
   trust-boundary section is required. If there is no trust boundary,
   write `n/a` and why.
2. **architect** commits the LLD to git.
3. **manager** posts the LLD path on the Epic with `tracker-sdlc`
   `comment`.

**Item:** align to the existing LLD the same way as in [Plan](#plan).
Make a clarification in place. Escalate a shape change. **security**
still reads the trust-boundary note. If the item does not touch a
boundary, the note is `n/a` and why.

### Mockups

If people see a screen, mockups are part of Spec. **designer** produces
**2–3 structurally different** mockups (`ux-design`, template
`mockup.md`) in whatever medium this agent has (markdown, HTML, canvas,
image, or an attached design tool — plus a git snapshot).

Review and operator acceptance: the [UX](#ux) review loop.

No screen: write `n/a` and why. Do not invent pictures.

### Security gate

1. Before Groom or Build, **security** reviews the LLD for trust
   boundaries: authn/z, secrets, egress, data class, who may write what.
2. **Accept the LLD** (architect + **security** on trust boundaries)
   before Groom/Build.

This review is a gate at Spec. Monthly is not the security gate:
[Monthly](trunk-changelog-monthly.md#monthly).

If the change touches a boundary, do not skip to Build without this
review. Run the review first.

## Documentation

Once the LLD is accepted, builders keep docs current through land. Two
surfaces; do not mix their jobs:

| Surface | Where | Skill | Job |
| --- | --- | --- | --- |
| **Human** | `docs/` how-tos, README usage | `docs-google-style` + template `human-doc.md` | What this is, how it works, how to use it |
| **Agent** | In-code comments, AGENTS pointers, module maps | `docs-google-style` (agent extras) | Locatable contracts for future agents: name, when, inputs, outputs, side effects, where to look next |

Human docs are for people. Agent notes enable future agents; they are
not tutorials. Do not paste the SDLC into product docs. Update both
surfaces in the same land as the change. The Build
[definition of done](build-review.md#definition-of-done) includes docs
current with the item.

Skills, templates, and other technical docs use engineering words. Do
not reuse the layperson analogies outside
[How software gets built](../how-software-gets-built.md).
