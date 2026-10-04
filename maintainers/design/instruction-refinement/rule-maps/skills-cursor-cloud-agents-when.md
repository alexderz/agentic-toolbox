# Rule map — `skills/cursor-cloud-agents-when/SKILL.md`

Item: PR #9, outside work by a Cursor Cloud Agent, reworked to the
writing standard on the integration branch.

Old: `skills/cursor-cloud-agents-when/SKILL.md` at PR #9 commit ac3236b,
lines 1–67. The file is new, so the PR text stands in for main 7a11696.
New: [`skills/cursor-cloud-agents-when/SKILL.md`](../../../../skills/cursor-cloud-agents-when/SKILL.md),
94 lines (K1 cap 250; K2 exempt, new file).

Key: **kept** (same rule, this file), **route** (the rule lives in its
owner; this file links it), **dropped** (duplicate, owner named),
**DER-265**, **DER-271**. "Old L" = line in the PR file; "L" = line in
the new file. No protected row is touched. Operator clarifications
(2026-09-27): only the frontmatter one applies; the `description` stays
metadata.

Plain-word and public-repo edits, applied throughout (operator, PR #9
review): the private workspace's product name and its jargon term for
the code host → "the operator's private SDLC repository" (PR #9 review:
"workspace" stays only for the host-lock scope of `security-hardening#never`); the PR's hyphenated
"this machine" term → "on this machine"; the manager's tracker-moves
sentence → route to the tracker owner.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–4 | Frontmatter: name; description (pick Cloud Agent, grok CLI, or the private SDLC repository; credit degrade; no bot token) | kept; plain words per the edits above; still lowercase trigger text; adds "do not use on your own initiative", as `grok-acp` has (MQ3) | L1–4 |
| 6 | Title naming three choices | kept; the private SDLC repository is a destination in the table, not a third worker | L6 |
| 8 | Choose the worker for coding or heavy multi-step work | kept | L8–9 |
| 8–10 | grok CLI run steps live in `grok-acp`; load it when the operator opts in to Grok Build over ACP | route to `grok-acp`; moved under Launch so the Iron law is the first section; the load condition adds the pre-approved Credit degrade fallback (MQ4) | L86–88 |
| 12–15 | Iron law: builds go to the grok CLI, Cloud Agents, or both; never implement with a bot token | kept, still first; the never now names the allowed action | L11–14 |
| 17 | Hand off the whole ticket | kept, numbered step | L18 |
| 17 | The CLI owns the implementation loop | kept as "the worker" (MQ1) | L19 |
| 18 | **verifier** checks the final result | kept, numbered step | L20 |
| 18–19 | Prefer Grok 4.7 on launch and on reply unless the operator names another model | dropped here; duplicate of Old L57–58, kept once under Launch | L78–79 |
| 19–22 | How remote agents and local CLIs fit the process: "docs/SDLC.md (Workers)" | route; the old target has no Workers heading. Now `docs/sdlc/subagents.md#workers` (worker table) and `docs/INTAKE.md#workers` (worker pull request intake) | L22–25 |
| 24–27 | Default split heading and table header | kept | L27–30 |
| 28 | Work on this machine: design, review, scratch, build-quota research → grok CLI | kept; plain words | L31 |
| 29 | Change that must land as a remote branch or pull request → Cloud Agent | kept verbatim | L32 |
| 30 | Greenfield, no repository named → Cloud Agent `new_repo` | kept verbatim | L33 |
| 31 | SDLC artifacts in the private SDLC repository → that repository, often through a Cloud Agent pull request | kept; generic name | L34 |
| 32 | Files only on a host with no remote checkout → grok CLI or shell on that host | kept verbatim | L35 |
| 33 | Windows or any host outside the workspace: off limits unless the operator approved | kept; route added to the owner, `security-hardening#never` | L36 |
| 35 | Product GitHub repositories stay separate from the private SDLC repository | kept, imperative | L38–39 |
| 37–41 | Prefer Cloud Agent: branch, pull request, or a land in the private SDLC repository on a connected remote repository; Cursor source control or a cloud VM | kept; one condition per bullet | L41–49 |
| 43–45 | Usage, credits, quota, or billing failure: say so once, fall back to the grok CLI | kept; steps 1–2; the fallback is stated as pre-approved (MQ4) | L51–60 |
| 45–48 | Remote pull request required: patch on this machine, then open or hand off from an approved host with credentials, or a branch-ready diff | kept; steps 3–4, condition stated in each | L61–65 |
| 48–49 | grok CLI also unavailable: stop, report both blockers | kept; step 5 | L66 |
| 49–50 | Never retry in a tight loop | kept; allowed action named | L68 |
| 50–51 | Never implement with a bot token, including a large patch | kept; allowed action named | L69–70 |
| 51–52 | Never work around the block with cookies or a Windows host | kept; allowed action named | L71–72 |
| 54–55 | Confirm the repository with the operator when ambiguous | kept, if/then | L76 |
| 55–56 | Launch with goal, constraints, definition of done | kept | L77 |
| 56–57 | Prefer Grok 4.7 unless the operator names another model | kept once, with "on launch and on reply" from Old L18 | L78–79 |
| 57–58 | Do not poll; resume when the run completes; follow up with a reply | kept; allowed action named | L80–81 |
| 58 | Interrupt only when asked | kept | L82 |
| 58–60 | No bank, mail, password-store, VPN, or chat secrets in the prompt | kept, imperative | L83–84 |
| 63–64 | Builder ships settings and new functionality | route to `docs/SDLC.md#roles` | L92 |
| 64–65 | Manager handles ticketed tracker moves only | route to `docs/SDLC.md#tracker` (owner: only the manager writes the tracker) | L92–93 |
| 65–66 | Windows off limits unless the operator approved that host | kept in the Default split row; route to `security-hardening#never` | L36, L93–94 |
| 66–67 | See `security-hardening` | route, now to its `#never` anchor | L94 |

## Meaning questions

- **MQ1** Old L17 "The CLI owns the implementation loop": the grok CLI
  only, or whichever worker took the ticket? Resolved from the text: the
  Iron law (Old L14) sends builds to the grok CLI, Cloud Agents, or both,
  and Old L17 follows it as the hand-off for any build. New L19 says "the
  worker".
- **MQ2** Old L63–65 "the manager … moves only": a narrower manager role
  than `docs/SDLC.md#roles`? Resolved from the text: Rule owners name
  `#roles` and `#tracker` as owners and this file may only route; the
  route adds no condition (standard 5).
- **MQ3** The new `AGENTS.md` row makes the skill operator opt-in.
  Resolved from the text: README listed it as optional, the sibling
  `grok-acp` Iron law says the operator picks Grok, and the manager
  brief asked for a row in the `grok-acp` shape. The skill's rules are
  unchanged. The description adds "do not use on your own initiative"
  (PR #9 review), which states the same opt-in.
- **MQ4** Old L43–45 "fall back to the grok CLI": does the fallback need
  a new operator opt-in, given `grok-acp`'s "the operator picks Grok"?
  Resolved by operator 2026-10-04: the fallback is pre-approved. A
  request to run a Cursor Cloud Agent approves the grok CLI fallback for
  that same goal; the agent says once that credits ran out, then falls
  back. New L53–55 and L59–60 state it; `grok-acp` carries a one-line
  exception that routes here (its rule map, PR #9 section).
