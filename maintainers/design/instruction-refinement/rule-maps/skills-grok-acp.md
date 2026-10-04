# Rule map — `skills/grok-acp/SKILL.md`

Item: DER-315 (E4).

Old: `skills/grok-acp/SKILL.md` at main 7a11696, lines 1–177.
New: [`skills/grok-acp/SKILL.md`](../../../../skills/grok-acp/SKILL.md).
Disposition: **kept** (same rule, this file), **route** (the rule lives in
its owner; this file links it), **dropped** (duplicate, owner named),
**DER-265**, **DER-271**. "Old L" = line in the old file; "L" = line in
the new file. Old and new are 177 lines (K2).

Protected row touched: `grok-acp` permission posture, labels, own-item
limits. Every row for them is **kept**; rows marked (P) below.
**security** reads it at Review. Operator clarifications (2026-09-27):
none of their subjects occur in this file.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–4 | Frontmatter: name; description (operator opt-in, builder by default, not for inline work) | kept verbatim | L1–4 |
| 6 | Title "Grok over ACP" | kept | L6 |
| 8–13 | Grok is a worker: minted clean, resumed by id, never trusted without verification; ACP over `grok agent stdio`; `grok-acp` from `packages/grok-acp`; stdlib Python, Linux only | kept; parenthesis "(JSON-RPC over …)" → apposition, no condition | L8–13 |
| 13–15 | No `grok-acp` on `PATH`: run `grok_acp.py` from the checkout at the skill's real path, or install per the package README | kept, as if/then; "(it is usually a symlink)" → own sentence (MQ7) | L13–15 |
| 17–20 | Iron law: the operator picks Grok; summary is a claim; verify before you report | kept verbatim, still first | L17–20 |
| 22 | Heading "Permissions (operator order, 2026-09-21)" (P) | kept verbatim; anchor unchanged (MQ4) | L22 |
| 24–27 | Maximum permissions: `--always-approve`, `_meta.yoloMode`, sandbox `off`, auto-approve; same user, same reach as the operator (P) | kept verbatim | L24–27 |
| 29–33 | What still binds it: `deny` rules and hooks in the two config files; project-level rules only in a trusted folder; nothing else; scope is set by your prompt, write it down (P) | kept verbatim | L29–33 |
| 35–45 | Heading "Run it"; mint and resume commands with `--label` / `--resume <item-id>:builder` (P) | kept verbatim | L35–45 |
| 47–49 | One invocation = one turn; stdout JSON, progress on stderr; start `run` in the background | kept; "Builds outlast …: start" → imperative first, reason after | L47–49 |
| 49–54 | `--timeout` 3600; timeout/SIGTERM → `session/cancel`, 20 s, exit 5, resumable; early SIGTERM spends no turn; one turn at a time per label and session, else `busy` (P) | kept verbatim, reflowed | L49–53 |
| 56–57 | Flag table header | kept | L55–56 |
| 58 | `--cwd` required; resumed label uses its minting cwd (P) | kept verbatim | L57 |
| 59 | `--label` = `<item-id>:<role>` = `builder_id` stored on the item (P) | kept verbatim | L58 |
| 60 | `--resume` takes a label or raw session id; `grok sessions list`; adopt with an unused `--label` (P) | kept; parenthesis → two sentences, same instructions | L59 |
| 61 | `--replace`: `--label` only, new session under an existing label, fallback / overflow (P) | kept; "(fallback / overflow)" → "For fallback or overflow" (MQ2) | L60 |
| 62–65 | `--prompt*`, `--model`/`--effort`, `--rules-file` (new sessions only), `--out` default | kept verbatim | L61–64 |
| 67–71 | `sessions` prints the registry at `sessions.json`; state and run dirs `0700`; `GROK_ACP_STATE` moves the state dir; `forget` drops a label, Grok keeps the session (P) | kept; parenthesis → sentences; "moves with `GROK_ACP_STATE`" → "If `GROK_ACP_STATE` is set, the state directory is that path" (the package's override, `grok_acp.py` L12, L34) | L66–69 |
| 73–84 | Result heading and field table | kept; `leftoverProcessesKilled` parenthesis → sentence; rest verbatim | L71–82 |
| 86–89 | Exit table header, exit 0 verify, exit 2 usage errors; `unknown_label` is not a reason to `--replace` (P) | kept verbatim | L84–87 |
| 90 | Exit 3: mint `--replace` with a short handoff, SDLC fallback (P) | kept; "(SDLC fallback)", a forward reference to L118, → link `docs/sdlc/subagents.md#fallback` (standard 4) | L88 |
| 91 | Exit 4: read `grok.stderr`; operator runs `grok login` | kept verbatim | L89 |
| 92 | Exit 5: resume or raise `--timeout`; `sessionId: null` → mint again | kept, as if/then | L90 |
| 93 | Exit 6: read `stopReason`; usually overflow → `--replace` (P) | kept verbatim (MQ1) | L91 |
| 95 | Heading "SDLC fit" | kept | L93 |
| 97–100 | Grok is a builder unless the operator says otherwise; verifier and reviewer are different agents, never see Grok's transcript; do not read `response.md` / `events.ndjson` into their prompts (P) | kept verbatim; allowed action added beside "Do not", per role: the verifier gets the ticket and the proving commands (old L145–146); the reviewer gets the inputs `skills/pr-review/SKILL.md` names (route, not restated) (MQ6) | L95–99 |
| 101–102 | One label per role per item; `DER-12:builder` never reused on another item, never resumed to verify or review its own work (P) | kept verbatim; the bold rule is the allowed action | L100–101 |
| 103–106 | Mint = pack: whole handoff; tell it to read `AGENTS.md` first; Grok cannot see this skills home unless packed or pathed | kept; parenthesis "(tell it to read …)" → own sentence; last clause → imperative "so pack the text or give the path" | L102–105 |
| 107–108 | Resume = delta; do not re-send the spec | kept verbatim | L106–107 |
| 109–111 | Create the item branch and worktree yourself from project-main (or trunk); pass it as `--cwd` | kept "yourself" and `--cwd`; branch source → route to `docs/sdlc/branches-and-lands.md#branches` (MQ3) | L108–110 |
| 111–112 | Tell Grok to commit on the branch, never push, never merge the item branch into anything | kept verbatim; "commit on that branch" is the allowed action | L110–111 |
| 112–115 | De-conflicting is the builder's job: resume the label with a merge/rebase delta; lands stay serialized and with the orchestrator (P, label) | kept; "orchestrator" → "manager" (K3, MQ5); link to `branches-and-lands.md#land-path` added, no condition | L111–114 |
| 116–117 | Check blockers before minting; offloading skips no gate; Review and security still run | kept verbatim | L115–116 |
| 118–119 | Fallback and overflow: exit 3 or a session too long to be useful → `--replace` with a short handoff (paths, decisions, open failures) (P) | kept (MQ1); the handoff list → route to `subagents.md#fallback`, which holds it verbatim | L117–118 |
| 121–136 | Handoff shape heading and template block | kept verbatim | L120–135 |
| 138 | Heading "After it returns" | kept; anchor used by L165 | L137 |
| 140 | Load `verify-before-done`; you are the orchestrator, not the verifier | kept; "orchestrator" → "manager" (K3, MQ5) | L139 |
| 142–144 | Step 1: smoke-check `git status`, `git diff <base>...`, branch and git rule; `filesEdited` misses shell-made changes; not the gate | kept, one step; parenthesis → sentence | L141–143 |
| 145–147 | Step 2: verifier runs the proving commands; first pass mint clean with ticket and commands; later passes resume `verifier_id` with the delta; never give it Grok's output (P) | kept, split for standard 1: manager's mint/resume step (L144–146), then the verifier's step with **verifier** first (L147) | L144–147 |
| 148 | Step 3: verifier failures go back to the same Grok label as a delta (P) | kept, imperative | L148 |
| 149 | Step 4: do not take "tests pass" from `text` at any step (P) | kept as step 5; "from the verifier" names the allowed action | L149 |
| 151–155 | Always: scope, do-not-touch paths, git rule in every mint; secrets out of prompts; report what, label, evidence | kept verbatim | L151–155 |
| 157–161 | Ask first: offloading without an operator ask; `--cwd` at a live host's config, `$HOME`, `/`; credentials in the prompt | kept verbatim | L157–161 |
| 163 | Heading "Never" | kept | L163 |
| 165 | Never treat `ok: true` as landed+verified (P) | kept verbatim; allowed action "Run After it returns" (MQ6) | L165 |
| 166 | Never let one Grok session build and verify the same item (P) | kept verbatim; allowed action "Mint a separate verifier" (MQ6) | L166 |
| 167 | Never feed Grok's transcript to a verifier or reviewer (P) | kept verbatim; allowed action "Give each its Role inputs": the per-role inputs at L98–99, no new input named (MQ6) | L167 |
| 168 | Never run two turns against the same session at once (P) | kept verbatim; allowed action "Wait, then resume" (MQ6) | L168 |
| 169–170 | Never tighten or loosen the permission posture without a new operator order; recorded above with its date (P) | kept verbatim; allowed action "Ask the operator for one" (MQ4, MQ6) | L169–170 |
| 172–177 | Red flags: four rationalizations | kept verbatim | L172–177 |

## Meaning questions

- **MQ1** — Old L93 "usually overflow" and old L118 "a session too long
  to be useful" are not checkable conditions (standard 2). A checkable
  rewrite (for example, `stopReason: max_tokens` only) would change when
  a label is replaced, a protected row. Resolved from the text: the old
  wording stays; the owner `docs/sdlc/subagents.md#fallback` uses the
  same condition ("too large to be useful"), so no reading is chosen.
- **MQ2** — Old L61 "(fallback / overflow)" reads as either the only uses
  of `--replace` or examples. Resolved from the text: the same two words
  stay, outside the parenthesis ("For fallback or overflow"); no reading
  is chosen. The exit 2 row still says `unknown_label` is not a reason to
  `--replace`.
- **MQ3** — Old L110 "from project-main (or trunk)" hides the condition
  for trunk in a parenthesis (standard 8). Resolved from the text: branch
  source is owned by `docs/sdlc/branches-and-lands.md#branches` ("from
  current project-main (or from trunk if none)"); the route adds no
  condition. "Yourself" and `--cwd` stay here.
- **MQ4** — Old L22 and L169–170 carry a date, and standard 8 bans dated
  conditions. Resolved from the text: the date records when the operator
  gave the order; nothing expires on it. The protected rows stay
  verbatim, heading and anchor unchanged.
- **MQ5** — Old L115 and L140 say "orchestrator". Resolved from the text:
  the SDLC index `#names` bans it for `manager`, the same actor (K3).
- **MQ6** — Standard 7 asks every "never" to name the allowed action.
  The added actions come from this file's own text: old L145–147 (mint a
  clean verifier with the ticket and commands), old L54 (one turn at a
  time), old L169 (a new operator order), old L138–149 (After it
  returns). The old text names no reviewer inputs, so for the reviewer
  the Role bullet routes to `skills/pr-review/SKILL.md` (clean reviewer,
  crafted inputs) and restates nothing; Never L167 points back to Role.
  Resolved from the text: each protected sentence stays verbatim; no
  condition or input is added.
- **MQ7** — Old L13–15 "resolve this skill directory's real path (it is
  usually a symlink), run `packages/grok-acp/grok_acp.py` from that
  checkout". Resolved from the text: "from the checkout that holds this
  skill directory's real path", with the symlink note as its own
  sentence; same action, same order (run first, or install).

All MQs resolved; none open.

## PR #9: credit fallback exception

Old: `skills/grok-acp/SKILL.md` at `pr-9-cursor-worker` 1946868, lines
1–177. New: lines 1–178 (K1 cap 250). One line added after the Iron law's
first rule; every other line is unchanged. K2: 178 > 177 at 7a11696; the
added line routes to a rule the operator decided on 2026-10-04 (MQ4).
K2 guards wording passes, and this is a new rule, so the manager
accepted the one line of growth on 2026-10-04.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 19 | Iron law: the operator picks Grok; offloading is opt-in per ask | kept verbatim | L19 |
| — | Exception: the credit-failure fallback in `cursor-cloud-agents-when#credit-degrade` is pre-approved; it covers only a failed Cloud Agent run (usage, credits, quota, billing) | new route; the owner is `cursor-cloud-agents-when` Credit degrade; adds no other condition | L20 |

PR #9 meaning questions: MQ4 in
[skills-cursor-cloud-agents-when.md](skills-cursor-cloud-agents-when.md),
resolved by operator 2026-10-04. The protected rows (permission posture,
labels, own-item limits) are untouched.
