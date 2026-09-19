---
name: golang-safety
description: use this when writing or reviewing Go for nil panics, typed-nil interfaces, append backing-array aliasing, silent integer truncation, float ==, defer-in-loops, defensive copies, or zero-value design — not concurrency primitives, not attacker vulns, not debugging an already-failing program.
---

# Go safety

Rewrite of samber/cc-skills-golang `golang-safety` @ `22c58a55`. **Not** a vendor paste. **Not** an `npx` / marketplace pack. **SKILL.md only** — no `evals/`, no `scripts/`, no `references/`. Id: `golang-safety`.

**security CLEAR (conditional):** SKILL only. Safety is *our* bugs. Attackers belong in `golang-security` (separate PR) and `security-hardening`. Proof belongs in `golang-testing` (separate PR) and `tdd`.

## Iron law

**No untested assumption about nil, capacity, or numeric range ships.**

Did not initialize it, bound-check it, or copy it? Treat it as a latent panic or a silent wrap.

## Scope

| This skill | Not this skill |
| --- | --- |
| Panics and silent corruption in ordinary Go | Concurrent maps, channels, goroutine leaks |
| Nil, slices/maps, numbers, defer, zero values | Injection, crypto, secrets, path traversal → `golang-security` / `security-hardening` |
| Stopping the next crash | Debugging a crash already in hand |

Pair, do not merge the three Go skills into one body. Attackers stay in `golang-security`; proof stays in `golang-testing`.

## Always

| Rule | Why |
| --- | --- |
| Comma-ok assert: `v, ok := x.(T)` | Bare `x.(T)` panics on mismatch |
| Return untyped `nil` for a nil interface | A typed-nil pointer inside an interface is `!= nil` |
| `make` (or lazy-init) maps before write | Nil map read is fine; write panics |
| Full-slice or `slices.Clone` before `append` when the original must stay intact | `append` reuses leftover cap and aliases the array |
| Return copies of exported slices/maps | Callers otherwise mutate internals |
| Extract the loop body so `defer` runs per item | `defer` fires at function exit, not at the iteration |
| Bound-check before narrowing ints | `int64`→`int32` wraps with no error |
| Epsilon (or `math/big`) for floats | `0.1+0.2 == 0.3` is false |
| Guard integer division by zero | Integer `/ 0` panics; float `/ 0` is Inf/NaN |
| Usable zero value; `sync.Once` if lazy-init can race | `var x T` must not panic on first use |
| Prefer generics over `any` when the set is known | Compiler, not a runtime panic |
| `errcheck`, `forcetypeassert`, `nilerr`, `govet`, `staticcheck` | **tester** static catch |

Go 1.25+ reflection: `reflect.TypeAssert[T](v)` — not `v.Interface().(T)`.

## Ask first

| Topic | Why it is a stop |
| --- | --- |
| Skipping a bounds check because "the value is small" | Small today; wrap tomorrow |
| Returning an internal slice/map "just this once" | Alias is a contract leak |
| Concurrent map read/write | Wrong skill; needs sync, not a comment |
| `init()` order across files | Unspecified; use a constructor |
| Integer overflow an attacker can drive | `golang-security`, not a safety nit |
| "Linters will catch it" without a fresh run | **tester** evidence, not vibes |

Do not self-except. Record the decision.

## Never

| Never | Why |
| --- | --- |
| Bare `v := x.(T)` on a production path | Crash on mismatch |
| Write to a map you did not initialize | Panic |
| `defer f.Close()` inside a loop in the same function | FDs pile up until return |
| `==` on computed floats | Silent wrong branch |
| `npx skills add` / marketplace install of the samber pack | INTAKE: clone, do not install |
| Copy `evals/`, `scripts/`, or `references/` into this skill dir | Conditional CLEAR is SKILL only |
| Treat this skill as a vuln audit | Attackers are `golang-security` + **security** |

## Traps (compressed)

### Typed nil

An interface is nil only when **type and value** are both nil.

```go
func handler(ok bool) http.Handler {
    var h *MyHandler
    if !ok {
        return nil // not h — *MyHandler(nil) boxed is != nil
    }
    return &MyHandler{}
}
```

### Nil containers

| | Index | Write | Len/cap | Range |
| --- | --- | --- | --- | --- |
| Map | zero | **panic** | 0 | 0 |
| Slice | **panic** | **panic** | 0 | 0 |
| Chan | block | block | 0 | block |

```go
func (r *Reg) Put(k string, v int) {
    if r.items == nil {
        r.items = make(map[string]int)
    }
    r.items[k] = v
}
```

### Append alias

```go
// may share a's array — writes to out can mutate a
out := append(a, x)

// keep a stable: cap==len forces a new array
out := append(a[:len(a):len(a)], x)
```

### Narrowing

```go
if n < math.MinInt32 || n > math.MaxInt32 {
    return 0, fmt.Errorf("int32 overflow: %d", n)
}
```

### Defer per item

```go
for _, path := range paths {
    if err := one(path); err != nil {
        return err
    }
}

func one(path string) error {
    f, err := os.Open(path)
    if err != nil {
        return err
    }
    defer f.Close()
    return use(f)
}
```

### Zero value

`sync.Mutex` and `bytes.Buffer` work at zero. A struct whose first write is `m[k]=v` on a nil map field does not. Lazy-init the map. If two goroutines can hit that init, `sync.Once` — do not invent a concurrency protocol in this skill.

Exported accessors that hand back `[]T` or `map[K]V` return `slices.Clone` / `maps.Clone`, not the live field.

## Roles

| Role | Owns | Does not own |
| --- | --- | --- |
| **builder** | Applying this gate when writing or reviewing Go | Installing the samber pack beside these ids |
| **security** | Intake CLEAR; overflow-as-vuln → security skills | Day-to-day nil coaching |
| **tester** | gofmt / staticcheck / errcheck hooks | Claiming DoD from fmt-only green |
| **manager** | After-act | Blessing a panic class that skipped the gate |

Workers do not bypass intake. A green `gofmt` is not a **security** clear.

## Red flags

- "It's never nil in practice"
- "append always copies"
- "I'll close everything at function exit"
- "int conversion is fine, the number is small"
- "npx the samber golang pack"
- "Safety and security are the same skill"
- "Copy the evals so we can score it"

Stop. Initialize, bound-check, or copy. Or ask.

## Upstream pin

Intent: [samber/cc-skills-golang](https://github.com/samber/cc-skills-golang) `golang-safety` @ `22c58a55a0a799b901aa251172923180bad9e010`. Body is a rewrite. See [SOURCES.md](../../SOURCES.md).
