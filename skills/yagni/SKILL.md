---
name: yagni
description: use this when scoping a change, adding a helper, or expanding a skill or AGENTS.md — ship the smallest thing that satisfies the current ask; defer speculative generality.
---

# YAGNI

Restraint. Prefer the smallest change that meets **this** Task. Compatible with `tdd` and `verify-before-done`: do not build for imagined tomorrow. No `scripts/`.

## Iron law

**Do not ship speculative generality.** If the ask does not need it, leave it out.

## Always

- Prefer one focused PR (~≤300–400 lines, one idea).
- Delete or skip dead code paths you are replacing — do not leave dual routers.
- Reuse an existing skill id before inventing a parallel procedure.
- Keep AGENTS.md thin (ids + repo rules); put procedures in skills.

## Ask first

- New abstraction “for later reuse” with no second caller yet.
- New config flag / feature toggle with no current consumer.
- Expanding a skill past ~250 lines or adding `scripts/` to a skill dir.
- Second toolkit that overlaps an installed skill id (dual router risk).

## Never

- Remint a MERGED skill body without a new **security** cut.
- Add marketplace installers or auto-update upstream into skills.
- Personal finance, mail, password stores, or extra hosts via “just in case” helpers.

## Red flags

- “We will need this eventually”
- “Keep both routers until we migrate”
- “Add a flag so we can turn it on later”
- “Copy the full vendor skill and trim later”

Stop. Shrink the change. Ship the ask.
