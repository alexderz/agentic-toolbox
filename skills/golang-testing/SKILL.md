---
name: golang-testing
description: use this when writing, reviewing, or debugging Go tests — table-driven named subtests, t.Parallel, goleak, synctest, fuzz, build-tagged integration, race, and idiomatic file naming.
---

# Go testing

Rewrite inspired by samber/cc-skills-golang `golang-testing` @ `22c58a55a0a799b901aa251172923180bad9e010`. **Not** a verbatim paste. **Not** a pack install. No `evals/`, no `scripts/`, no clawhub. Id: `golang-testing`.

Pairs with `tdd` (fail-first) and `verify-before-done` (fresh `go test` evidence). **builder owns.** Do not install the rest of the samber pack to get this.

## Iron law

**Tests constrain observable behavior, not coverage percentages.**

Each case is independently runnable, named, and attributed to its own `*testing.T`. Coverage is a gap finder. A green percentage with weak assertions is theater.

## Always

| Rule | Why |
| --- | --- |
| Table-driven cases with a `name` passed to `t.Run` | `go test -run Test/case` and failure output need the name |
| One `_test.go` per source file (`foo.go` → `foo_test.go`) | Tools and reviewers resolve by file, not by symbol |
| Order tests like the source functions | Drift makes the pair unreadable |
| Assert the public contract | Internals-coupled tests rewrite on every refactor and prove nothing |
| Independently runnable cases | Order dependence is a flake factory |
| `t.Parallel()` on independent tests | Default-serial is leftover time |
| Build-tag integration (`//go:build integration`) | Unit `go test ./...` stays fast and hermetic |
| `go test -race` in CI | Data races do not show up as assertion failures |
| `goleak.VerifyTestMain` when the package starts goroutines | Leaks are silent until production |
| Mock interfaces defined at the consumer | Concrete mocks lock the wrong type |
| testify as helpers on top of `testing` | It is not a replacement for the stdlib |
| `ExampleXxx` with `// Output:` for public API | Drifting docs fail the build |
| Fresh `go test` evidence before claiming green | `verify-before-done` |

## Ask first

| Topic | Why it is a stop |
| --- | --- |
| White-box (`package foo`) vs black-box (`package foo_test`) | Unexported access is a design choice, not a default |
| Skipping `t.Parallel()` on a large independent suite | Say why (shared mutable fixture, global env) |
| Adding testify / mock codegen the module does not already use | New test dep is a project dep |
| `go install github.com/cweill/gotests/gotests@latest` | Unpinned installer; INTAKE: no skill scripts |
| Integration tests without a build tag | They hitch a ride on every unit run |
| Ignoring known goroutines in goleak | `IgnoreCurrent` hides leaks — name them |
| Coverage gates as a merge target | Percentage ≠ assertion quality |

Do not self-except. Record the choice.

## Never

| Never | Why |
| --- | --- |
| Parent `assert.New(t)` / `require.New(t)` reused inside `t.Run` | Failures attach to the parent; the subtest still prints `PASS` |
| Tests that only pass in a fixed order | Hidden shared state |
| Mocking a concrete type | You tested the mock, not the consumer |
| Sleep-based synchronization as the flake fix | Use `synctest` (Go 1.25+) or a real sync point |
| `synctest.Run` in Go 1.25+ code | That API is the 1.24 experiment; use `synctest.Test` |
| Silencing `stdversion` (Go 1.27+ default vet) | Bump the `go` directive or stop using the newer API |
| Writing artifacts into the repo from a test | Go 1.26+ `t.ArtifactDir()` (also `B` / `F`) |
| Installing the samber pack or clawhub | Dual routers; **security** CLEAR is SKILL-only |
| Copying `evals/`, `EVALUATIONS.md`, `clawhub-publish.sh`, or `scripts/` | Quarantined by intake |

## Modes (one pass)

| Mode | Do |
| --- | --- |
| **Write** | One behavior at a time. Table + named `t.Run`. Edges and error paths. `tdd` still applies. |
| **Review** | Diff only: new behavior covered, assertions on the contract, no flake patterns, no assert-scope leak. |
| **Audit** | Three concerns, then one report: (1) unit quality / gaps, (2) integration isolation / tags, (3) leaks / races. |
| **Debug** | Reproduce, isolate the assertion, then the production or setup cause. Do not “fix” a flake with sleep. |

## Shape

```go
func TestAdd(t *testing.T) {}                 // function
func TestMyStruct_MyMethod(t *testing.T) {}   // method
func BenchmarkAdd(b *testing.B) {}            // benchmark: b.Run per variant; Go 1.24+ b.Loop()
func ExampleAdd() {}                          // example
func FuzzAdd(f *testing.F) {}                 // fuzz
```

Same-package tests see unexported names. `package foo_test` sees the public API only. Prefer black-box unless you are testing a package invariant that is not exported.

Split `foo_test.go` / `foo_edgecases_test.go` only when one file is genuinely unwieldy — still named from the source file, never from a single function.

### Table-driven

```go
func TestCalculatePrice(t *testing.T) {
    tests := []struct {
        name      string
        quantity  int
        unitPrice float64
        want      float64
    }{
        {name: "single item", quantity: 1, unitPrice: 10, want: 10},
        {name: "zero quantity", quantity: 0, unitPrice: 10, want: 0},
    }
    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            got := CalculatePrice(tt.quantity, tt.unitPrice)
            if got != tt.want {
                t.Fatalf("CalculatePrice(%d, %.2f) = %.2f, want %.2f",
                    tt.quantity, tt.unitPrice, got, tt.want)
            }
        })
    }
}
```

stdlib `t.Fatalf` is enough. If you use testify, build `assert.New(t)` **inside** the subtest from that subtest’s `t`. Probe a broken case: parent `FAIL` + every `--- PASS: Test/case` means the assert leaked.

`t.Parallel()` goes on the subtest (and the parent if the parent has no shared setup). Build the assert after `t.Parallel()`, from the subtest `t`.

### Integration

```go
//go:build integration

func TestDatabaseIntegration(t *testing.T) { /* real store */ }
```

```bash
go test -tags=integration ./...
```

Unit tests: fast, no network, no live store. HTTP handlers: `net/http/httptest`. Go 1.27+ `httptest.NewTestServer` is the in-memory server that composes with `synctest`.

### Leaks and time

Packages that start goroutines:

```go
func TestMain(m *testing.M) { goleak.VerifyTestMain(m) }
```

Per-test: `defer goleak.VerifyNone(t)`.

Go 1.25+ `testing/synctest`: `synctest.Test(t, func(t *testing.T) { ... })`. Fake time advances when every goroutine in the bubble is blocked — use it for `Sleep` / `After` / `Ticker` / deadlines instead of wall-clock flakes. Go 1.27+ `synctest.Sleep(d)` advances the bubble clock directly.

### Fuzz and examples

Seed with `f.Add`, then assert an invariant (round-trip, parse/format). `ExampleXxx` stdout must match `// Output:`.

Coverage: `go test -coverprofile=coverage.out ./...` then `go tool cover -html=coverage.out`. Read uncovered lines. Do not treat the number as DoD.

Linters that catch this skill’s rules: `thelper`, `paralleltest`, `testifylint`. **tester** owns hook wiring — do not remint CI here.

## Commands

```bash
go test ./...                     # unit (no integration tag)
go test -race ./...               # CI default for concurrent packages
go test -run TestName/case ./...  # one named case
go test -count=1 ./...            # no cache when proving a claim
go test -tags=integration ./...
go test -fuzz=FuzzName ./...
go test -bench=. -benchmem ./...
```

## Roles

| Role | Owns | Does not own |
| --- | --- | --- |
| **builder** | This skill; Go test shape in product repos | Installing the samber pack |
| **tester** | `gofmt` / race / lint hooks when `.go` appears | Claiming product DoD from fmt-only green |
| **security** | Intake; CLEAR conditions (SKILL only) | Day-to-day testify coaching |
| **manager** | After-act landed+verified | Blessing a suite that skipped `tdd` / verify |

Workers do not bypass intake. A green `go test` is not a **security** clear of this skill home.

## Red flags

- “I’ll assert the mock was called and call it covered”
- “Share one `assert` across the table — cleaner”
- “It only fails under `-count=1` / `-race` / `-shuffle=on`, so ignore it”
- “Sleep(10ms) makes it stable”
- “Install gotests / the samber pack to write Go tests”
- “Copy evals or clawhub so we can score the skill”

Stop. Name the case. Assert the contract. Run fresh evidence.

## Upstream pin

samber/cc-skills-golang `skills/golang-testing` @ `22c58a55a0a799b901aa251172923180bad9e010` (MIT). Body is a compress of `SKILL.md` only. See [SOURCES.md](../../SOURCES.md).
