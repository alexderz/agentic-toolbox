# Proofs

The builder of an item runs every check for its item and returns a proof
bundle. Nobody re-runs the builder's checks: the **reviewer** reads the
bundle and its raw outputs, and does not execute them. The **tester**
keeps CI, hooks and cleanup; a CI run is evidence the bundle links.

## Names

- **Check** — one command that passes or fails: a formatter, linter,
  unit, integration or end-to-end test, a span test, or a project verify
  skill's command.
- **Raw output** — the full output of one check run, saved to a file.
- **Proof bundle** — the builder's evidence that its item meets the
  ticket, in fixed fields. It is part of the builder's result to the
  **manager**. It is not a transcript: it holds no reasoning and no chat.
- **Journey** — one end-to-end user or system path, from its real start
  to its real end.
- **Midpoint** — a named state partway along a journey that a test can
  assert and seed.
- **Span test** — a test of part of a journey. A **start-to-mid** test
  runs from the real start to a midpoint and asserts the state there. A
  **mid-to-end** test seeds the midpoint state and runs to the real end.
  A failing span test points at its half of the journey.

## Sharing evidence

Return the bundle through the private review channel to the manager for the
**authorized reviewer**. For public PRs, tickets, comments and commit messages,
report only the tested revision, public-safe results and shareable artifact links.
Keep workspace paths, raw logs, private CI links and the full bundle out of them.

## Proof bundle

The bundle has these fields. A field with nothing to record holds `n/a`
and why.

1. **Criteria**: per acceptance criterion, the proving command, its exit
   code, its counts (passed, failed, skipped) and its raw output path.
2. **Seen failing**: per new check, how it failed first (red before
   green, or the broken variant) and that run's raw output path.
3. **Visual**: per UI behavior, the screenshot or video path.
4. **Scope**: what is verified, under which bounds and assumptions; what
   is left out, and why.
5. **Sync commit**: the commit the checks ran on.
6. **Direct evidence**: the build workspace path on disk, and the CI run
   link when the repo has CI.
7. **Journeys**: per journey and span test run, the fields of field 1.

## Journeys

1. **architect**, at Spec: name the chunk's journeys and each journey's
   midpoints in the LLD's Verify. The chunk changes no user or system
   path → write `n/a` and why.
2. **architect**, at Groom: in each item's Verify, name the journeys and
   the spans the item touches.
3. **builder**: write and run the span tests for each span its item
   touches, and run each journey its item touches. If a touched journey lacks
   an end-to-end test, add and run the missing test even if Verify or the LLD
   omitted it. The item changes no user or system behavior → record `n/a`
   and why for journeys; do not invent one.

## Builder checks

**builder**, for its item:

1. Pick the checks from this table. The diff touches a path when it
   changes a file on that path.

   | The item's diff touches | Run |
   | --- | --- |
   | Files a formatter or linter in the repo covers | That formatter and that linter |
   | Code that has unit or integration tests | Those test suites |
   | Behavior on a journey | That journey's end-to-end test, and each span test of the spans the diff touches |
   | A verify target of a project verify skill | That verify skill, per `formal-verification` |
   | None of these for one kind of check | Nothing for that kind; write `n/a` and why in the bundle |

2. Compare the diff with Verify and apply [Journeys](#journeys) step 3
   to the journeys and spans the item touches.
3. See each new check fail before it passes: run it before the change it
   proves, or against a broken variant for a formal property. Save that
   raw output.
4. Save the raw output of every run to the scratch folder the
   **manager** named in the mint prompt.
5. Before claiming done, run every check from step 1 again, fresh, on
   the item head, per the `verify-before-done` Gate.
6. Return the proof bundle in your result.

Never weaken a test, a property or a bound so that a check passes;
report the failure as a finding.

## After integration

1. After each land, the landing **builder** runs each journey its item
   touched at the land SHA on its land target: project-main for a chunk
   item, or trunk for an item landed directly there. Return a proof
   bundle with that SHA as the sync commit. The item touched no journey
   → the result is `n/a` and why. This run is the verify of
   landed+verified.
2. A journey fails after a land → the item is not `done`. **manager**
   resumes that builder with the failure. Its fix goes through
   [Review](build-review.md#review) and lands like the item.
3. Before Trunk merges project-main, **manager** resumes the builder of
   the last item landed. **builder**: run the chunk's full journey set on
   the project-main tip and return it as a proof bundle. This chunk-level
   run is not a different item under [Item agents](subagents.md#item-agents).
4. A journey fails in step 3 → **manager** files a Bug under the Epic
   with the failing journey, tested revision, and public-safe result. Include
   only shareable artifact links; keep raw evidence in private review. Trunk waits until
   that Bug is `done`, then step 3 runs again.
5. **manager**: at Trunk, report the revision and public-safe result from step 3
   in the Epic's `done` `comment`; cite only shareable artifacts.
