# Opus rebuild: exact texts

Exact replacement texts for DER-712 items G2–G12, owned by
[opus-rebuild.md](../opus-rebuild.md). They are design data: never load
them as skills.

Each file holds the text of one target file or block. Its links are
written relative to that target path, not to this folder, so a link
check here reports them as broken; check them at the target instead.
Builders and verifiers read these files from the `integrate/ask-less`
branch with `git show`, never from an item worktree.

| File | Target | Item |
| --- | --- | --- |
| `index-asking.md` | `skills/sdlc/SKILL.md`, from `<a id="asking-the-human">` to the line before `## Steps` | G2 |
| `liaison.md` | `skills/sdlc/references/liaison.md` | G3 |
| `asks-template.md` | `skills/sdlc-artifacts/templates/asks.md` | G3 |
| `ask-human-template.md` | `skills/sdlc-artifacts/templates/ask-human.md` | G3 |
| `yagni.md` | `skills/yagni/SKILL.md` | G5 |
| `judging.md` | `maintainers/evals/procedure.md`, the `### Judging an ask (C6)` block | G11 |
| `runner-needs.md` | `maintainers/evals/procedure.md`, the Runner needs paragraph | G11 |
| `t4-card.md` | `maintainers/evals/t4-card.md` | G12 |
| `t4-key.md` | `maintainers/evals/t4-key.md` | G12 |
