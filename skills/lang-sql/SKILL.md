---
name: lang-sql
description: use this when writing, reviewing, or migrating SQL — *.sql, schema files, embedded queries in host code. postgres-shaped defaults; name the dialect if it is not postgres. load with the host language skill when the query lives in application code.
---

# SQL

Parameterize or do not ship. Compatible with `tdd`,
`verify-before-done`, `pr-review`, `security-hardening`,
and the host language skill. No `scripts/`.

## Iron law

**Parameters, never string concatenation. Migrations are forward-only
and reversible, or explicitly one-way.**

## Tooling / verify

- Host-language tests cover the bind path (this is the real test).
- `EXPLAIN` the new query before adding an index "for speed."
- Run the migration against a disposable database when one exists.

Name the dialect in the PR if it is not Postgres.

## Idioms a linter misses

- Bound parameters (`$1`, `?`, named) from the host. Always.
- Name columns. No `SELECT *` in application queries.
- Transactions around multi-statement writes.
- `timestamptz` for instants (Postgres). Money: integer cents or
  `numeric`, not float.
- Indexes for predicates you actually use, not every column.
- `NOT NULL` when absence has no meaning.

## Errors

- Constraint failures are data errors, not "retry until it works"
  unless the operation is documented idempotent.
- Check `rowcount` when a write must touch exactly N rows.

## Concurrency

- Know the isolation level the app already uses.
- `SELECT … FOR UPDATE` only with a transaction and a short critical
  section.
- Avoid long transactions that hold row locks across user think-time.

## Testing

- Fixture data in the test DB or transaction-per-test as the project
  already does.
- Assert on the rows, not only "no exception."
- Migration tests: apply on empty and on a snapshot of prod-shaped
  data when the project has that harness.

## PR review

- Every user-influenced value is a bind parameter.
- Destructive DDL has an expand-contract plan.
- New index: `EXPLAIN` evidence, or do not add it.
- Do not edit a migration that has already run.

## Security

- Least-privilege role for the app (no owner role at runtime).
- No `SECURITY DEFINER` functions unless the project already uses
  them and the body is reviewed.
- Views / RLS: do not assume the app layer is the only client.

## Always

- Binds. Named columns. Transactions on multi-writes.

## Ask first

- DROP COLUMN / DROP TABLE / type change of a shipped column.
- Dialect switch (MySQL / SQLite / SQL Server).
- New extension or `SECURITY DEFINER`.

## Never

- String-built SQL with user input (including "it's an int").
- Interpolating identifiers (table/column names) from user input.
- `LIKE` patterns from user text without escaping `%` and `_`.
- Float for money.
- Re-editing applied migrations.
- `SELECT *` in app code.

## Red flags

- "I'll just interpolate, it's an int"
- "SELECT * is fine"
- "We'll add the index if it's slow"
- "The ORM will escape it" without checking the generated SQL
