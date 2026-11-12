# Rule map — `maintainers/evals/procedure.md`

Item: DER-731 (E1 of DER-712). Old: `maintainers/evals/procedure.md` at main c26f424, lines 1–216.
New: `maintainers/evals/procedure.md`. Edits: [LLD E1](../lld.md#e1--eval-text) as overridden by
[overlay G11](../opus-rebuild.md#g11--eval-text-e1).

Key: **kept**; **route**; **dropped** with the owner named; **changed** with its deciding id.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–2 | Title; page purpose | kept | L1–2 |
| 3 | Runs cover T1–T3 | changed (R59, R60): T1–T4 | L3 |
| 4–7 | When a run is needed routes to `## Evals`; no runner commands | kept | L4–7 |
| 9–26 | Names: commit under test, runner, run directory, skills home, scratch product repo, fixture directory, repeat | kept | L9–26 |
| 27 | Names C1–C5 | changed (R26): C1–C6 | L27 |
| 29–34 | Tasks table header, T1, T2 rows | kept | L29–34 |
| 35 | T3 row "pending (G3)" | changed (R60): links to card, key, fixture; T4 row and the "T1–T3 run on every eval run" line added (R59) | L35–39 |
| 37–52 | Runner needs 1–7; one missing need disqualifies | kept | L41–56 |
| 54–59 | **security** reads a runner before its first run; runner change needs a new read; proxy or bind is Ask first | kept | L58–63 |
| — | The read also records items 1–9 and the version-change recheck | changed (R83, R107; overlay G11 item 1): new paragraph | L65–84 |
| 61–63 | Isolation intro | kept | L86–88 |
| 65–66 | Step 1: separate user or container; T3 in a container | changed (R181; overlay G11 item 2): T3 and T4 in a container; T4's has Node.js 20 or later | L90–91 |
| 67–68 | Step 2: empty runner home | changed (R83): the one model credential the read names is the only exception | L92–94 |
| 69 | Step 3: no SSH agent | kept | L95 |
| 70 | Step 4: egress only to the model endpoint | changed (R83): egress only to the endpoints the read lists | L96 |
| 71–72 | Step 5: unset tracker and git-host tokens | kept | L97–98 |
| 74–83 | Pre-run probe intro, checks 1–5 | kept | L100–109 |
| — | Probe check 6: no credential other than the named one | changed (R83): added | L110–112 |
| 85–86 | A failed check → no run; record pass or fail only | kept | L114–115 |
| 88–93 | Tool-call gate | kept | L117–122 |
| 95–107 | Skills home steps 1–5 | kept | L124–136 |
| 109–137 | Scratch product repo, T1 start state | kept | L138–166 |
| — | T4 starts from its own `main` | changed (R59): added | L168 |
| 139–155 | T2 start state | kept | L170–186 |
| 157–162 | Scripted replies: one mode per model; record the mode | kept | L188–193 |
| 163–164 | Re-baseline runs T1–T3 in the new mode | changed (R177; overlay G11 item 5): every task the comparison run will run | L194–195 |
| 166–168 | Mode (a) | kept | L197–199 |
| 169 | Mode (b): instruction text, then the reply table | changed (R177; overlay G11 item 4): the reply table without its `C6` column | L200–201 |
| 170–174 | Mode (b) `Continue.` rule, one follow-up, C1 scoring | kept | L201–206 |
| 176 | Models heading | kept | L208 |
| 178–182 | Candidate list; confirmed set = rows of `baseline.md` | changed (HLD Evals 7, R31; overlay G11 item 3): the confirmed set is the Grok 4.7 and DeepSeek V4.1 Flash 1017 table; `baseline.md` holds a row per model after its first baseline run; a new model or runner needs the operator's written confirmation, then a **security** read | L210–219 |
| 184–190 | Run hygiene 1–3 | kept | L221–227 |
| 191 | Hygiene 4: three repeats, nine per model | changed (R59): "nine repeats per model" dropped, as T4 makes it twelve | L228 |
| 192 | Hygiene 5 | kept | L229 |
| 193–194 | Hygiene 6: 2-hour stop | changed (R41): the card's wall-time cap, else 2 hours | L230–231 |
| 196–202 | Scoring 1–2 | kept | L233–239 |
| 203 | Scoring 3: C1–C5 | changed (R26): C1–C6; T4 counts | L240 |
| 204–205 | Tokens and wall time never a pass bar | kept | L241–242 |
| 206–207 | Scoring 4: regression | changed (R51): C1–C6; T4 needed asks kept | L243–245 |
| — | Judging an ask (C6) | changed (R26, R171, R172, R176, R177; overlay G11 item 6): added at the end of `## Scoring` | L247–282 |
| 209–216 | Records 1–4 | kept | L284–291 |
| — | Records 5: never write a credential into a run file | changed (R83): added | L292 |

## Meaning questions

None. Every change is decided by a cited ruling or the overlay; the T1–T3 merge rule is kept (R59).
