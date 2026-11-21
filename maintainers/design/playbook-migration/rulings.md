# Instruction migration scope

DER-816 adds a first-party migration skill, not a new process step.
It adapts pending instructions to the existing owners without replaying
accepted work. No product migration, deployment or broad test run occurs.

Ruling: reuse current rule owners and infer project-local edits from the
actual consumer — avoids a parallel versioned process — cost if wrong:
revise the affected instruction rather than rebuild migration tooling.

Ruling: retain the specialized stage-result migration unchanged — a
harness-contract adoption is separate from retiring duplicate verification
— cost if wrong: clarify its routing.
