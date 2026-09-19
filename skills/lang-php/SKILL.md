---
name: lang-php
description: use this when writing, reviewing, or testing PHP — *.php, composer.json. PHP 8+ types. do not use for JavaScript. not a Laravel architecture skill.
---

# PHP

PHP 8+ types. Compatible with `tdd`, `verify-before-done`,
`pr-review`, `security-hardening`. No `scripts/`.

## Iron law

**Declare types. Parameterize queries. No eval.**

## Tooling / verify

```bash
composer test
# or vendor/bin/phpunit
```

`php -l` on touched files is not DoD.

## Idioms a linter misses

- `declare(strict_types=1);` when the project uses it.
- Typed properties, parameters, returns. No untyped public API.
- Constructor promotion when the class is already that style.
- Return empty array, not `null`, for lists.

## Errors

- Exceptions or the project's result type. No `@` error suppression.
- Do not display raw exceptions to clients.

## Concurrency

- PHP request lifecycle is the default. Shared mutable statics are a
  bug in FPM.
- Queues / workers: treat each job as a new process. No leftover
  state.

## Testing

- PHPUnit as the repo uses it. Test through public types.

## PR review

- New untyped public method: reject.
- New query: binds visible.
- Composer deps: lockfile in the diff.

## Security

- PDO or the project's DB layer with bound parameters.
- `password_hash` / `password_verify`. No home-rolled hashing.
- Escape output at the template boundary (the engine the project uses).
- No `unserialize` of untrusted data. No `eval`. No `extract` on user
  input.
- Uploads: allowlisted extensions and a storage path outside the docroot
  if the project already does that.

## Always

- Types on new public APIs. Binds. Tests.

## Ask first

- Raising the language level in `composer.json`.
- Adding a framework the module is not already on.

## Never

- `eval`, `extract` on user input, `unserialize` of untrusted data.
- `md5` / `sha1` for passwords.
- `mysql_*` APIs. String-built queries.
- Error suppression `@`.
- Displaying raw exceptions to clients.

## Red flags

- "PHP will coerce it"
- "addslashes is enough"
- "unserialize is just the session format"
