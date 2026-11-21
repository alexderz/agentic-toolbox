# Rule map — `AGENTS.md`

Item: DER-809. Brief: [brief](../brief.md). Rulings: [rulings](../rulings.md).

Old: `AGENTS.md` at chunk base commit 80bfbd5, lines 1–80. New: `AGENTS.md` (80 lines).

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–60 | Unchanged rules in this range | kept | 1–60 |
| 61–62 | Formal verification and Statecharts rows: the verifier actor and its "run the product repo's verify skill" How cell | changed (R3): verifier clauses dropped; the How cell reads one instruction for architect and builder; the builder runs verify skills per `proofs.md#builder-checks` | 61–62 |
| 63–80 | Unchanged rules in this range | kept | 63–80 |

Protected rows touched: Public-repo rule: not touched (lines 17–33 kept).

## Meaning questions

- MQ1 — Does dropping the verifier actor remove a check that ran the product verify skill? Resolved: no; the builder runs it (`formal-verification` Actors, `proofs.md` Builder checks table row 4). Requirements: R1, R3.
