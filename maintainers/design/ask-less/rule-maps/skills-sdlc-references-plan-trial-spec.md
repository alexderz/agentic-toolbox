# Rule map — plan-trial-spec

Item: DER-739 (G8, source item A7 of DER-712).

Old: `docs/sdlc/plan-trial-spec.md` at main c26f424, lines 1–148. New: `skills/sdlc/references/plan-trial-spec.md`.

The A0 move kept every old line number; A0 changed only link paths ([A0 path map](a0-path-map.md)).
Edits: [overlay G8](../opus-rebuild.md#g8--design-gate-hld-touchpoint-delivery-route-a7) and
[LLD A7](../lld.md#a7--design-gate-and-hld-touchpoint).

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1 | Title | **kept** | L1 |
| 3–13 | Plan steps 1–7: architect writes, stages, scans, commits and pushes the HLD; manager posts its path | **kept** | L3–13 |
| — (after 13) | New Plan step 8: the brief's `HLD review` line says yes → the liaison sends touchpoint 2; Spec starts only after the operator accepts the HLD; requested changes → the architect revises and the step repeats | **changed** (R154; overlay G8 edit 1) | L14–15 |
| 15–23 | Item: no new HLD; the manager posts one verdict; the verdict table, including the "no HLD to align to" ask | **kept** | L17–25 |
| 25–26 | In this skills home the SDLC counts as the plan | **kept** | L27–28 |
| 28–45 | Comparables: 2–4 real examples, the page, the waiver in writing, its Never | **kept** | L30–47 |
| 47–51 | UX: designer writes UX and stories in Plan; mockups are part of Spec | **kept** | L49–53 |
| 53–60 | Review loop steps 1–3: designer produces, a different agent reviews against written requirements, fix until agreed | **kept** | L55–62 |
| 61–62 | Review loop step 4: the operator accepts, or writes `UX verification not required`; for mockups, before Groom | **changed** (LLD A7 edit 2; HLD touchpoint 3): the acceptance or waiver happens at the design gate. MQ1 | L63–64 |
| 64–69 | UX Never: no self-OK as the gate; no skipped mockups without the written waiver | **kept** | L66–71 |
| 71–87 | Trial: optional, frozen `poc/`, its steps, the secret-removal exception, the item skip | **kept** | L73–89 |
| 89–98 | Spec entry gate and steps 1–3 | **kept** | L91–100 |
| 100–103 | Item Spec: align to the LLD as in Plan; clarify in place; escalate a shape change; security reads the trust-boundary note; `n/a` and why | **changed** (R156; overlay G8 edit 4): an in-place clarification's acceptance goes as an ask in the next batch and Build waits for it; an unchanged LLD needs no ask; the shape change links Escalation. The security read and the `n/a` rule are kept | L102–105 |
| 105–114 | Mockups: 2–3 structurally different variants; acceptance by the UX review loop; no screen → `n/a` and why | **kept** | L107–116 |
| 116–121 | Security gate steps 1–2: security reviews the LLD and `poc/`; architect and security accept | **kept** | L118–123 |
| 122 | Security gate step 3: the operator accepts the LLD after them | **changed** (R155; LLD A7 edit 3): the operator accepts the LLD, and the UX and mockups when there are any, at the design gate. MQ2 | L124 |
| 123 | Start Groom or Build only after step 3 | **kept** | L125 |
| 125–129 | Monthly is not the security gate; no skip to Build without this review | **kept** | L127–131 |
| 131–148 | Documentation: two surfaces, same land, engineering words | **kept** | L133–150 |

## Meaning questions

- MQ1. Old L62 "For mockups, this happens before Groom" is gone. Does mockup acceptance still come
  before Groom? Resolved: yes. Step 4 now happens at the design gate, and Security gate step 4
  (old L123, kept) starts Groom or Build only after the design gate. Cited:
  [hld.md](../hld.md) Touchpoints table, row 3 ("Design gate, hard | LLD, UX and mockup acceptance").
- MQ2. Old L122 "after them" (after the architect and security accept) is gone. Does the operator
  still accept after them? Resolved: yes. The step order is unchanged (steps 1–2, then 3), and
  touchpoint 3 carries the security gate result. Cited: [hld.md](../hld.md) Touchpoints table,
  row 3 ("the security gate result"); R155 in [opus-rebuild.md](../opus-rebuild.md#8-rulings-opus-rebuild).
