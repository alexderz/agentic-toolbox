# First cherry-pick candidates (security intake)

**architect** list for **security**. **Names, upstream repos, and why
only.** No skill bodies in this file. No vendor `SKILL.md`. No
marketplace pack.

Owner: **architect** (this list + SHA pin after clear) + **security**
(intake).

## Gates before any body lands

1. **security** intake per [INTAKE.md](../docs/INTAKE.md). Workers do not bypass.
2. **SkillSpector** (and/or cisco skill-scanner / verified obielin
   skillguard — verify the GitHub org) **before a body lands**.
   Layout-only `.gitkeep` dirs do not need a scan.
3. Pin the cherry-pick **SHA** in [SOURCES.md](../SOURCES.md) **after
   security clear**, before the body. Empty SHA = no body. First-party
   rows use `first-party` in the SHA cell.
4. Rewrite ≤250 lines. No verbatim vendor paste. No `scripts/`. No
   secrets. No auto-update.

**architect** names the SHA set after the first security clear. This file
is not a pin list.

## Candidates

| Candidate id | Upstream | Why | Notes |
| --- | --- | --- | --- |
| `tdd` | [obra/superpowers](https://github.com/obra/superpowers) (`test-driven-development`) | Iron law fail-first | **security** decides |
| `verify-before-done` | [obra/superpowers](https://github.com/obra/superpowers) (`verification-before-completion`) | No done without fresh evidence | **security** decides |
| `pr-review` | [mattpocock/skills](https://github.com/mattpocock/skills) (`code-review` dual-axis) | Standards vs Spec unmerged | **Rename** off `/code-review` collision. Id stays `pr-review` |
| `security-hardening` | first-party (Always/Ask/Never compress) | Not a vendor cherry-pick | Body already on `main`. Do not remint |
| `shell-safety` | first-party ≤80 lines preferred | Safe shell defaults for tester/security | konstruktoid bash-secure as **reference only** — not a vendor install |
| `golang-testing` | [samber/cc-skills-golang](https://github.com/samber/cc-skills-golang) (`golang-testing`) | Go test idioms | SKILL only |

Placeholders already exist under `skills/<id>/`. This list does not
authorize copying those upstream files.

## Not in this cut

- A second process pack beside this repo’s ids — do not install.
- `yagni` — first-party restraint; not a vendor intake item unless
  **security** pulls it.
- Still-empty first-party ids (`tracker-sdlc`,
  `cursor-cloud-agents-when`) — written here later; not vendor
  cherry-picks.

## Landed vs remaining (historical list)

This file is not the live pin list — see [SOURCES.md](../SOURCES.md).
Bodies already on `main` (do not remint without a new **security** cut):
`security-hardening`, `tdd`, `verify-before-done`, `pr-review`,
`shell-safety`, `modern-python`, `golang-testing`, plus later fills
(`yagni`, `golang-safety`, `golang-security`, language pack).

Still empty first-party ids: `tracker-sdlc`, `cursor-cloud-agents-when`.
