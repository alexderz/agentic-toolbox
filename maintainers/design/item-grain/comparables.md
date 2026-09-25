# Comparables — item grain and named steps

How others have done “small change vs full design” without a second
process. **Before** locking Plan shape.

- Slug: `item-grain`
- Brief / options map: confirmed brief in the gather session
- Date: `2026-09-18`

## Required

### Google design docs (small vs large)

- **Who / what** — [Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/)
- **What they did** — Same design steps for small work, kept terse. Skip
  a doc only when the design is unambiguous (not “because it is a bug”).
- **Steal** — Same steps at every grain; fill-in gets shorter. Alignment
  with an existing design beats a skip-to-code path.
- **Won’t copy** — Optional skip of design when “the solution is
  obvious.” Our item path still **aligns** Plan and Spec.

### Rust RFC vs implementation PR

- **Who / what** — [Rust RFCs](https://github.com/rust-lang/rfcs/blob/master/README.md);
  [lang team: small PR until it isn’t](https://lang-team.rust-lang.org/how_to/propose.html)
- **What they did** — Bugfix and docs go as a PR. Substantial change
  needs an RFC. If a “small” PR grows, they stop it and demand an RFC.
- **Steal** — Start at item grain; **promote** when it is actually a
  plan change. Write the problem and the proposed change on the PR.
- **Won’t copy** — Skipping design review for every bugfix. We still
  check the existing Plan/Spec.

### ITIL incident / problem / change

- **Who / what** — [Incident vs problem vs change](https://www.alvao.com/en/blog/what-difference-between-incident-management-and-problem-management-and-change-management)
- **What they did** — Restore now, find why, planned change as three
  practices. Escalation when the incident is really a change.
- **Steal** — Waiting on a person blocks **that** record; other work
  continues. Promote when the work is larger than a tactical fix.
- **Won’t copy** — Three separate processes and the jargon. We have one
  process and two Entry outcomes (chunk vs item).

### Hotfix / fast path

- **Who / what** — Typical [hotfix](https://devopsschool.jp/hotfix/)
  write-ups: minimal scope, still tested, merge back to mainline.
- **What they did** — Emergency patch with a short pipeline. Not a
  substitute for root cause or for skipping tests.
- **Steal** — Tiny scope; still prove the fix; do not leave the official
  copy diverged.
- **Won’t copy** — A second “emergency SDLC” that skips Review or
  security. Not all bugs are production incidents.
