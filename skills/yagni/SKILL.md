---
name: yagni
description: use this when scoping a change, adding a helper, or expanding a skill or AGENTS.md, as the builder, the item contrarian or the reviewer — ship the smallest thing that satisfies the current ask; defer speculative generality. do not use on a chunk brief.
---

# YAGNI

**The ask** is what the current task asks for. **Speculative generality** is anything built for a need the ask does not have (a future need). Use restraint. Prefer the smallest change that meets **this** ask. Do not build for a need the ask does not have. This skill is compatible with `tdd` and `verify-before-done`. This skill has no `scripts/`.

## Iron law

**Do not ship speculative generality.** If the ask does not need it, leave it out.

## Always

- Prefer one focused PR: one idea, ~≤300–400 lines.
- Delete or skip each dead code path you replace. Never leave dual routers; keep one path.
- Reuse an existing skill id before you write a parallel procedure.
- Keep `AGENTS.md` thin: ids and repo rules only. Put procedures in skills.
- `yagni` for safety: add no guardrail that no rule and no operator asked for, unless it protects a one-way door; then log its `Guardrail:` line. A control that `security-hardening`, the LLD's trust boundaries or a **security** finding requires is a rule, not a guardrail; keep it ([Asking the operator](../sdlc/SKILL.md#asking-the-human)).

## Decide and log

Each of these is a two-way door. Act as the line says, without asking, and log a ruling per [Asking the operator](../sdlc/SKILL.md#asking-the-human):
- An abstraction “for later reuse” with no second caller, a config flag with no consumer, or a second toolkit overlapping an installed skill id → leave it out. For the toolkit, use the installed id.
- A skill past its line cap → split it into a second file.

## Never

- Never remint a MERGED skill body without a new **security** cut; get the cut first.
- Never add `scripts/` to a first-party skill; a vendor helper comes in only through [intake](../sdlc/references/intake.md) step 2.
- Never add marketplace installers or auto-update upstream into skills; take third-party content through [intake](../sdlc/references/intake.md).
- Never add “just in case” helpers for personal finance, mail, password stores, or extra hosts; leave them out.

**Red flags.** If your plan says one of these, stop. Shrink the change. Ship the ask.

- “We will need this eventually”
- “Keep both routers until we migrate”
- “Add a flag so we can turn it on later”
- “Copy the full vendor skill and trim later”
