# Third-party skill intake

Checklist before any third-party skill **body** lands in this repo.
**security** owns this gate. Workers (remote agents, local CLIs, mirrors)
do not bypass it.

First-party files written in this repo (this checklist,
`skills/security-hardening/SKILL.md`, language guides) are not vendor
intake. They still must not ship secrets or `scripts/`.

## Checklist

1. **Clone, do not `npx`.** Fetch the upstream git repo (clone or fetch +
   checkout). Do not marketplace-install a pack. Do not `npx` an
   installer, skill runner, or “add this skill” command. Do not install
   a second process pack beside this repo’s ids.
2. **Quarantine scripts.** Do not copy `scripts/`. Do not run upstream
   install, postinstall, or bootstrap scripts. Treat executable skill
   helpers as untrusted until **security** says otherwise — default is
   drop them.
3. **Scan the candidate.** Run SkillSpector, cisco skill-scanner, and/or
   a **verified** obielin skillguard. **Verify the GitHub org** on the
   tool before you trust the binary or action (name collisions are not a
   clear).
4. **Pin SHA in [SOURCES.md](../SOURCES.md) before the body.** The table
   row must name upstream, SHA, license, and notes. Empty SHA means no
   body may land. First-party rows use `first-party` in the SHA cell.
5. **Rewrite ≤250 lines + least privilege.** Do not paste a vendor
   `SKILL.md` verbatim. Compress. Review skills must not write. No
   secrets. No extra skill bodies in the same PR unless **security**
   asked for them.
6. **No auto-update.** Pin stays until a later **security**-cleared bump.
   No marketplace sync, no “latest”, no unattended vendor pull.

## Workers

Remote-agent PRs into this repo **still need a security clear**. Remote
authoring is not an exemption. Build DoD still requires the diff to
match the pinned SHA (or `first-party` for first-party prose).

Product-repo `.agents/tracker/SKILL.md`: no SOURCES row; **security**
reads the change that adds or edits it. It holds no tokens, no
`scripts/` files, and no executable blocks except the fenced shell
recipe from `skills/tracker-sdlc/adapters/local.md`. **security**
compares that recipe with the adapter's current text; only placeholder
fills and baked-in adapter gotchas may differ. Any other executable
content fails the read.

## Layout-only exception

Empty skill directories that only hold `.gitkeep` (layout, no `SKILL.md`,
no scripts) are **OK without scan**. Intake and scanners start when a
body, script, or third-party file would land.
