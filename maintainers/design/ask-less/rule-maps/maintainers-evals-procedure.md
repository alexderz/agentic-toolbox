# Rule map — `maintainers/evals/procedure.md`

Item: DER-731 (E1).

Old: `maintainers/evals/procedure.md` at main c26f424, lines 1–216.
New: [`maintainers/evals/procedure.md`](../../../evals/procedure.md).
Key: **kept** (same rule), **replaced** (the old line's rule is the new
text), **new** (added from [E1](../lld.md#e1--eval-text)), **dropped**
(the old text is gone and the new text is named). "Old L" is a line in
the file at main c26f424.

Operator clarifications (2026-09-27): none of their subjects are in this file.

Protected rows touched: none.

**security** reads the Runner needs, Isolation, Pre-run probe and Records
changes at Review. This build does not read a runner.

Links to `t4-card.md`, `t4-key.md` and `t4-dump.md` resolve when E2 lands.
That is scheduled, not a missing file in this item.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1 | Title | kept | H1 |
| 3 | How to run T1–T3 on one commit and one model | replaced: T1–T4 (E1 step 1) | intro |
| 4–7 | When a run is due; the page states requirements and names no runner commands | kept | intro |
| 9 | Names | kept | ## Names |
| 11–26 | Commit under test, runner, run directory, skills home, scratch product repo, fixture directory, repeat | kept | ## Names |
| 27 | C1–C5 are the checklist items in the run template | replaced: C1–C6 (E1 step 2) | ## Names |
| 29 | Tasks | kept | ## Tasks |
| 31–34 | Tasks table header, T1 and T2 rows | kept | ## Tasks |
| 35 | T3 row names the card, key and fixture as pending | replaced: links to `t3-card.md`, `t3-key.md` and `t3-groom.md`; T4 row and the line that says when T4 runs added (E1 step 3, R60) | ## Tasks |
| 37–59 | A runner qualifies only with needs 1–7; **security** reads it before the first run; a change needs a new read; a local-model proxy or a network bind is Ask first | kept | ## Runner needs |
| — | The read records the one model credential, its scope and revocation, the endpoints, session sharing off, no language-server or plugin download, the installed version with no pin, any bind and session state, no second login, and the provider-side credit limit; a version that differs rechecks those settings | new (E1 step 4, R83, R107) | ## Runner needs, the paragraph after the Ask-first sentence |
| 61–64 | Set up every repeat as listed | kept | ## Isolation |
| 65–66 | Run the runner as a separate user or in a container; run T3 in a container | replaced: run T3 and T4 in a container; T4's also has Node.js 20 or later (E1 step 5) | ## Isolation step 1 |
| 67–68 | Empty home: no `gh` or git credential helpers, no SSH keys, no runner MCP config | kept, and the one model credential the read names is the only exception (E1 step 6) | ## Isolation step 2 |
| 69 | Run no SSH agent | kept | ## Isolation step 3 |
| 70 | Allow egress only to the model endpoint | replaced: only to the endpoints the read lists (E1 step 6a) | ## Isolation step 4 |
| 71–72 | Unset every tracker or git-host token variable | kept | ## Isolation step 5 |
| 74–83 | Pre-run probe: five checks that must fail | kept | ## Pre-run probe steps 1–5 |
| — | A search of the runner home and environment finds no credential other than the one the read names | new (E1 step 6b) | ## Pre-run probe step 6 |
| 85–86 | A check that does not fail as listed means no run; record `pass` or `fail` only, never a host name | kept | ## Pre-run probe |
| 88–93 | Tool-call gate | kept | ## Tool-call gate |
| 95–107 | Skills home: export, delete `maintainers/`, read-only, discovery off, first turn names the path | kept | ## Skills home |
| 109–137 | Scratch product repo, including no `tickets` branch at T1 start | kept | ## Scratch product repo |
| — | T4 starts from its own `main`, named by the T4 card | new (E1 step 7). The card link resolves when E2 lands | ## Scratch product repo |
| 139–155 | T2 start state | kept | ## T2 start state |
| 157–174 | Scripted replies, including mode (a), mode (b), and a T1–T3 re-baseline before a comparison in a new mode | kept. The re-baseline stays T1–T3 (R59) | ## Scripted replies |
| 176 | Models | kept | ## Models |
| 178–182 | Candidate model list, confirmed at B1; the confirmed set is the baseline rows | dropped. Replaced by the confirmed-set table (next row) | ## Models |
| — | Confirmed set: `grok-4.7` is Grok 4.7 on the grok CLI; `deepseek-v4.1-flash-1017` is DeepSeek V4.1 Flash 1017 through OpenRouter, on OpenCode with its `openrouter` provider, run under T3 Code. A new model or runner needs the operator's written confirmation, then a **security** read | new (E1 step 8) | ## Models |
| 184–190 | Run hygiene steps 1–3: fresh session, no MCP server, same sampling settings | kept | ## Run hygiene |
| 191 | Three repeats per task per model, and nine repeats per model | replaced: three repeats per task per model; the nine-repeat count is dropped (E1 step 9) | ## Run hygiene step 4 |
| 192 | Repeats strictly one at a time; warm the model before timing | kept | ## Run hygiene step 5 |
| 193–194 | Stop at the card's end point or at 2 hours | replaced: stop at the card's wall-time cap, or at 2 hours when the card names none (E1 step 10, R41) | ## Run hygiene step 6 |
| 196–202 | Score from the transcript and `origin.git`; the scorer is `person` or `agent` | kept | ## Scoring steps 1–2 |
| 203 | Per task, C1–C5 and Completed as passes out of 3 | replaced: C1–C6, and for T4 also its counts (E1 step 11) | ## Scoring step 3 |
| 204–205 | Tokens and wall time are a median and range, never a pass bar | kept | ## Scoring step 3 |
| 206–207 | Regression: fewer C1–C5 or Completed passes than the baseline | replaced: C1–C6 or Completed, or T4's needed asks kept summed over repeats, is lower; fewer unneeded asks is reported, not a bar (E1 step 12, R51) | ## Scoring step 4 |
| — | An ask is a message that waits or a turn that ends on a question; the reply table marks each row `needed` or `over-ask`; C6 passes when no `over-ask` row was used; a repeated ask is `over-ask`; a catch-all is `over-ask` unless the ask is a one-way door or an action only the operator can do | new (E1 step 13) | ### Judging an ask (C6) |
| 209–216 | One run file per model; regressions first; **security** reads the first run file; update the baseline per ## Evals rules 4 and 5 | kept | ## Records steps 1–4 |
| — | Never write a credential, token, key or login-file content into a run file | new (E1 step 6c) | ## Records step 5 |

## Meaning questions

None open.

- The new Runner-needs paragraph follows the whole security paragraph, after the Ask-first sentence. The locator sentence is inside that paragraph, and the instruction says to add a paragraph after it. The Ask-first sentence stays with the read it belongs to.
- The intro sentence "It names no runner and no runner commands" stays. E1 step 1 changes only T1–T3 to T1–T4. The Models table names the two runners and names no runner commands.
