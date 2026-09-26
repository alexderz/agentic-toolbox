---
name: pr-lens
description: use this when the operator asks for a diagram of a change or a system — "diagram this PR", "add a pr-lens diagram", "draw the architecture of this change", "put a diagram in the PR into main" — to write a PR Lens graph document, validate and render it locally with the pinned CLI, and attach the SVG to a pull request body. do not use on your own initiative, do not use for canvases or model-driven analysis, and do not use for a diagram the operator did not ask for.
---

# PR Lens

PR Lens turns a JSON description of a change (lanes, nodes, edges, and
ordered flows) into architecture and data-flow diagrams as SVG files.
This skill covers two things only: rendering those SVGs on this machine,
and attaching them to a pull request with the GitHub CLI.

This is a first-party rewrite of the upstream skill. For what we left
out and why, see [Upstream](#upstream).

## Iron law

**The operator asks for a diagram; you do not add one.** It is opt-in
per ask. A typical ask is a diagram in the PR into `main`.
**Run only the `validate` and `render` subcommands.** Every other
subcommand (`canvas`, `analyze`, `comment`, `auth`, `skill`, `export`,
and any other) is Never. The only thing that leaves the machine is the
PR attachment.

## Before you start

- Check the GitHub CLI version: `gh --version`. Attaching needs 2.99 or
  later. If it is older, render anyway and ask the operator how to
  publish the SVG.
- Every CLI call in this skill uses `npx @coldtea/pr-lens-cli@0.8.1`, an
  exact pin. Every new release is a one-line bump in
  [SOURCES.md](../../SOURCES.md) with a **security** read; there are no
  automatic patch releases. Never use `@latest`.
- The full document format lives upstream, at the pinned commit:
  - [graph-document.md](https://github.com/coldteadotai/pr-lens/blob/09f6378c082ff8ddb17e211f36bfc71c2f2b8d86/skills/pr-lens/references/graph-document.md):
    every field, enum, and limit.
  - [example.graph.json](https://github.com/coldteadotai/pr-lens/blob/09f6378c082ff8ddb17e211f36bfc71c2f2b8d86/skills/pr-lens/references/example.graph.json):
    a complete document that validates. Read it before your first one.
  - [config.md](https://github.com/coldteadotai/pr-lens/blob/09f6378c082ff8ddb17e211f36bfc71c2f2b8d86/skills/pr-lens/references/config.md):
    the correction overlay.

  Where those pages differ from this skill (commands, `@latest`,
  canvases, payloads), this skill wins.

## Steps

1. **Read the change.** Diff against the merge base, not the tip of the
   base branch:

   ```bash
   git diff --find-renames main...HEAD
   ```

   Replace `main` with the PR's base branch. For a diagram of existing
   code rather than a change, read that code instead.

2. **Write the document** to `.pr-lens/graph.json`. Follow the pinned
   `graph-document.md` and model it on `example.graph.json`. See
   [A good document](#a-good-document).

3. **Validate and fix.**

   ```bash
   npx @coldtea/pr-lens-cli@0.8.1 validate .pr-lens/graph.json
   ```

   Fix every failure, then run it again until it passes. Don't render an
   invalid document. Never delete the element a failure names just to
   make the failure go away; fix the reference or the field instead.

   | Code | Meaning |
   | --- | --- |
   | `BROKEN_REFERENCE` | An edge, flow step, view, or walkthrough step names an undeclared id |
   | `INVALID_DOCUMENT` | A field the strict schema doesn't know, or a bad value |
   | `DUPLICATE_ID` | Two nodes, edges, or views share an id |
   | `UNSUPPORTED_SCHEMA_VERSION` | `schemaVersion` doesn't match the CLI's contract |

4. **Render, light theme.**

   ```bash
   npx @coldtea/pr-lens-cli@0.8.1 render .pr-lens/graph.json --theme light
   ```

   Ask first before any theme other than light. The command prints the
   output directory under `.pr-lens/`, named after the document title,
   with one SVG per view and a `manifest.json` that lists them.

   The CLI adds `.pr-lens/` to `.gitignore`. Never commit anything under
   `.pr-lens/`; the files are rebuilt from the diff on demand.

5. **Attach to the PR**, when the operator asked for a PR or for a
   diagram on an existing one. See [Attach to a pull
   request](#attach-to-a-pull-request).

## Attach to a pull request

The diagram belongs in the PR description, where a reviewer looks
first, not in a trailing comment. Write the body to a file:

1. One sentence on why the change exists.
2. The top architecture view.
3. A data-flow view, only if the change has a sequence worth following.
4. Optional: a short list of what changed, using
   [change headings](#change-headings).

```markdown
Moves report exports off the request thread and onto a job queue.

![Architecture after this change: the export route, the new queue, and the export worker](.pr-lens/export-queue/overview-light-1a2b3c4d.svg)
```

Then pass the body file and every image it references:

```bash
gh pr create --title "Queue report exports" --body-file .pr-lens/body.md \
  --attach .pr-lens/export-queue/overview-light-1a2b3c4d.svg
```

For an existing PR, use `gh pr edit PR_NUMBER` with the same two flags.
Repeat `--attach` once per image.

- Use a Markdown image, `![alt](path)`. `gh` replaces the local path with
  the uploaded asset. An HTML `<img>` or `<picture>` is not rewritten.
- Write one line of alt text that says what the diagram shows. It is the
  caption for a reader without images.
- Two diagrams usually read better than four. If a diagram needs a
  paragraph to explain it, go back to step 2.

## A good document

- **Show unchanged neighbours.** Only-changed nodes hide the blast
  radius. Include the direct neighbours the change touches and mark them
  `delta: "unchanged"`.
- **Lanes are the reader's mental model**: a runtime, a tier, or a trust
  boundary. Not the folder tree.
- **One hero edge**, two at most: the connection the change is about.
- **Flows only for real sequences.** One clear flow beats three thin
  ones. Flows need the `data-flow` lens; an architecture view draws
  none.
- **File refs anchor nodes to code.** Add them to nodes. Links inside
  an SVG embedded in a PR aren't clickable, so name files in the body
  if a reviewer needs them.
- **No findings.** The document explains the change; it doesn't review
  it. Don't put bugs, risks, or security notes in it. The schema has no
  field for them and rejects a document that invents one. Report
  findings through `pr-review`, not the diagram.
- **Views, top down.** One view is enough for a small change. Go one
  level narrower (system context, then containers, then components)
  only when that level adds something. Don't draw code-level views, and
  don't infer architecture from folder names alone. Set
  `defaultOpen: true` on the highest useful architecture view. Keep
  data-flow views as separate roots.

## Change headings

The SVG renderer doesn't draw a walkthrough; only a canvas plays one.
So a `walkthrough` in the document is optional here: skip it, or write
its headings as the PR body's list of changes. When you write either,
use these rules:

- **One change each**: something added, removed, replaced, or moved,
  headline change first. Never a description of the diagram.
- **Heading**: up to 48 characters, sentence case, built from change
  words (added, removed, now, moved, split). If it was already true
  before the PR, rewrite it.
- **Body** (walkthrough steps only, required there): one line, up to
  140 characters, on what now happens that didn't before.
- **Walkthrough steps**: 2 to 12. Each names a view or flow as its
  stage and focuses the two or three elements it changes.
- **Plain words.** Short common words, active voice, digits for
  numbers, names as the diagram shows them.

| Write this | Not this |
| --- | --- |
| Export route now queues the job | Export orchestration moves to an asynchronous pipeline |
| Worker retries 3 times, then gives up | Resilient retry semantics leveraged for robustness |

## Payload samples

A flow step can carry a `payload`, a sample request and response. Only
canvases draw payloads, and this skill doesn't use canvases, so usually
leave them out. If the operator asks for one anyway, use placeholder
data only: `user@example.com`, `order_0001`, `192.0.2.1`. Never copy a
value from a fixture, a log, or a database.

## Correct the map

When the operator says the diagram is wrong (a node misnamed, a file
that shouldn't appear, a node in the wrong lane), put the correction in
`.github/pr-lens.yml`. That overlay is applied on every run.

```yaml
schemaVersion: 0.2.0
map:
  rename:
    - match: src/export/worker.ts
      to: Export worker
  exclude:
    - "**/*.test.ts"
```

Prefer a path glob in `match` over `id:NODE_ID`; paths survive
re-inference. Validate the overlay the same way:

```bash
npx @coldtea/pr-lens-cli@0.8.1 validate .github/pr-lens.yml
```

The overlay is a repo file, so ask before you commit it. `render`
reports a correction that matched nothing.

## Upstream

- Official skill, pinned:
  [coldteadotai/pr-lens `skills/pr-lens/SKILL.md` at `09f6378`](https://github.com/coldteadotai/pr-lens/blob/09f6378c082ff8ddb17e211f36bfc71c2f2b8d86/skills/pr-lens/SKILL.md)
  (MIT). Pin and notes: [SOURCES.md](../../SOURCES.md).
- **Excluded: `canvas push`, `open`, `look`, `answer`, `show`, and
  `fork`.** They publish the code's structure to prlens.dev, and a view
  link opens without a login.
- **Excluded: `analyze`.** It sends the diff to a third-party model
  provider.
- **Excluded: `comment`.** It needs the SVGs published publicly first.
- The pin, the CLI version, and this rewrite are compared with upstream
  at [Monthly](../../docs/SDLC.md#monthly) review.

## Always

- Use `npx @coldtea/pr-lens-cli@0.8.1 validate` or `render`, nothing else.
- Validate, fix every failure, and validate again before you render.
- Lead the PR body with why, then the top architecture view.

## Ask first

- Any theme other than light, or more than two diagrams in one PR body.
- Publishing an SVG any way other than `gh --attach`.
- Committing `.github/pr-lens.yml`.
- Payload samples.

## Never

- Any subcommand other than `validate` and `render`.
- `@latest` or an unpinned CLI.
- Commit anything under `.pr-lens/`.
- Labels, summaries, or titles built from anything but this
  repository's diff or code: no internal hostnames, URLs, credentials,
  personal data, or other repositories' names. On a public repository
  an attached diagram is public.
- Findings, bugs, or risks in the document.
- Delete an element to silence a validation failure.
- Install the upstream skill with an installer or marketplace command.
