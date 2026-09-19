---
name: lang-js-ts
description: use this when writing, reviewing, or testing JavaScript or TypeScript — *.ts, *.tsx, *.js, *.mjs, *.cjs, tsconfig, package.json. TypeScript-strict wins when tsconfig exists. do not use for HTML/CSS-only (lang-web-markup) or Python.
---

# JavaScript / TypeScript

One skill for both. TS-strict is the default when `tsconfig.json` exists;
JS is the same rules minus the type checker. Compatible with `tdd`,
`verify-before-done`, `pr-review`, `security-hardening`. No
`scripts/`. Not a React/Next/Vue skill.

## Iron law

**`any` is a bug. Untrusted data is parsed at the boundary. Promises are
not fire-and-forget.**

## Tooling / verify

Use the lockfile's package manager (`pnpm` / `npm` / `yarn`). Typical:

```bash
# names vary — run what package.json scripts already define
npm test
npx tsc --noEmit   # when tsconfig exists
npx eslint .       # when eslint is already in the tree
```

Do not add a second test runner or a second linter. Read the full output.

## Idioms a linter misses

- `const` default, `let` when reassigned. No `var`. No implicit globals.
- `===`. `??` for nullish; do not use `||` when `0` or `''` is valid.
- Named exports. Default exports only if the file already does.
- ESM if the package is ESM. Do not mix `require` and `import` without
  an existing pattern.
- Functions that return a Promise are `async` or clearly chained. Callers
  `await` or return the promise. No floating promises.
- Narrow with predicates / discriminated unions, not `as T`.
- `unknown` at untrusted boundaries, then narrow. Never `as any`.

## Errors

- Do not empty-`catch`. Log or wrap with context, then rethrow or return
  a typed error the caller expects.
- Node: do not `process.exit` from a library.
- Map HTTP / network failures to a small error union, not a raw `any`.

## Concurrency

- No shared mutable state across requests without a documented store.
- `AbortSignal` for cancellable I/O when the caller can cancel.
- Avoid `Promise.all` on untrusted-length lists without a bound.
- Worker threads / child processes: structured messages, no string `eval`.

## Testing

- Test through the public API. Mock only at process boundaries (network,
  clock, RNG, fs).
- One behavior per test. Names say the expected outcome.
- Use the runner already in the repo (node:test, vitest, jest). Do not
  add another.

## PR review

- New `as` / `any` / `@ts-ignore`: reject unless the comment names the
  invariant and the escape is local.
- New dependency: why not std or an existing dep?
- Async path: every rejection handled.
- Bundle / Node surface: no secrets in client code.

## Security

- Validate untrusted input at the boundary. Use the schema library the
  repo already has; do not invent a second one.
- No string-built SQL, HTML, or shell. Parameterize / use APIs.
- Browser: no `innerHTML` / `dangerouslySetInnerHTML` / `postMessage` of
  untrusted data. Same sink class. `target=_blank` needs
  `rel="noopener noreferrer"`.
- Node: no `eval`, `new Function`, or `child_process` with a concatenated
  string. `path` joins stay inside an allowlisted root.
- Do not store tokens in `localStorage`.

## Always

- `strict` stays on. New files match existing `tsconfig`.
- Quote-free equality and nullish rules above.
- Tests for the new branch.

## Ask first

- Disabling a `strict` flag.
- Adding a runtime schema library the repo does not use.
- Introducing a new test runner or bundler.
- `any` in a public `.d.ts`.

## Never

- `any`, `as unknown as T`, empty `catch {}`.
- `eval` / `new Function` / `document.write`.
- String-building SQL, HTML, or shell.
- Pinning a future TS / Node version the repo is not on.
- Loading `lang-web-markup` instead of this skill for `.tsx` logic.

## Red flags

- "I'll type this as any and fix later"
- "The frontend already validated it"
- "JSON.parse is fine, we control the server"
- "It's just a quick child_process.exec"
