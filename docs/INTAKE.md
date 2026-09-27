# Third-party skill intake

Checklist before any third-party skill **body** lands in this repo.
**security** owns this gate. Workers — remote agents, local CLIs,
mirrors — go through it and do not bypass it.

First-party files are written in this repo, for example this checklist,
`skills/security-hardening/SKILL.md` and language guides. They are not
vendor intake. Ship them without secrets and without `scripts/`.

## Checklist

1. **Clone, do not `npx`.** Fetch the upstream git repo: clone, or fetch
   and checkout. Never marketplace-install a pack. Never `npx` an
   installer, skill runner, or “add this skill” command. Never install a
   second process pack beside this repo’s ids.
2. **Quarantine scripts.** Never copy `scripts/`. Never run upstream
   install, postinstall, or bootstrap scripts. Drop executable skill
   helpers as untrusted; keep one only if **security** clears it.
3. **Scan the candidate.** Run one or more of: SkillSpector, cisco
   skill-scanner, a **verified** obielin skillguard. **Verify the GitHub
   org** of the tool before you trust its binary or action. A matching
   name is not a clear.
4. **Pin SHA in [SOURCES.md](../SOURCES.md) before the body.** Write the
   row first: upstream, SHA, license, notes. If the SHA cell is empty,
   land no body. For a first-party row, write `first-party` as the SHA.
5. **Rewrite ≤250 lines + least privilege.** Compress the vendor
   `SKILL.md`; never paste it verbatim. Review skills must not write.
   Ship no secrets. Add no extra skill bodies to the same PR unless
   **security** asked for them.
6. **No auto-update.** Keep the pin until a later **security**-cleared
   bump. No marketplace sync, no “latest”, no unattended vendor pull.

## Workers

A remote-agent PR into this repo **still needs a security clear**.
Remote authoring is not an exemption. Build DoD still requires the diff
to match the pinned SHA. For first-party prose, the pin is `first-party`.

A product-repo `.agents/tracker/SKILL.md` needs no SOURCES row. This
covers every one that a governing `## Tracker` names: at the root, or in
a subdirectory whose `AGENTS.md` the root `AGENTS.md` or `CLAUDE.md`
names. **security** reads the change that adds or edits one:
1. **security** checks it holds no tokens, no `scripts/` files, and no
   executable blocks except the fenced shell recipe from
   `skills/tracker-sdlc/adapters/local.md`.
2. **security** compares that recipe with the adapter's current text;
   only placeholder fills and baked-in adapter gotchas may differ.
3. **security** fails the read on any other executable content.

## Layout-only exception

An empty skill directory that holds only `.gitkeep` is layout: no
`SKILL.md`, no scripts. It is **OK without scan**. Start intake and the
scanners when a body, script, or third-party file would land.
