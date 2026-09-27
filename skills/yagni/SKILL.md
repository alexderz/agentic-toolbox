---
name: yagni
description: use this when scoping a change, adding a helper, or expanding a skill or AGENTS.md — ship the smallest thing that satisfies the current ask; defer speculative generality.
---

# YAGNI

**The ask** is what the current task asks for. **Speculative generality** is anything built for a need the ask does not state. Use restraint. Prefer the smallest change that meets **this** ask. Do not build for a future need the ask does not state. This skill is compatible with `tdd` and `verify-before-done`. This skill has no `scripts/`.

## Iron law

**Do not ship speculative generality.** If the ask does not need it, leave it out.

## Always

- Prefer one focused PR: one idea, ~≤300–400 lines.
- Delete or skip each dead code path you replace. Never leave dual routers; keep one path.
- Reuse an existing skill id before you write a parallel procedure.
- Keep `AGENTS.md` thin: ids and repo rules only. Put procedures in skills.

## Ask first

Before you do any of these, ask the operator per [Asking the operator](../../docs/SDLC.md#asking-the-human):
- New abstraction “for later reuse” with no second caller yet.
- New config flag or feature toggle with no current consumer.
- Expanding a skill past ~250 lines or adding `scripts/` to a skill dir.
- Second toolkit that overlaps an installed skill id: a dual-router risk.

## Never

- Never remint a MERGED skill body without a new **security** cut; get the cut first.
- Never add marketplace installers or auto-update upstream into skills; take third-party content through [INTAKE.md](../../docs/INTAKE.md).
- Never add “just in case” helpers for personal finance, mail, password stores, or extra hosts; leave them out.

## Red flags

If your plan says one of these, stop. Shrink the change. Ship the ask.
- “We will need this eventually”
- “Keep both routers until we migrate”
- “Add a flag so we can turn it on later”
- “Copy the full vendor skill and trim later”
