# Trunk, Changelog, and Monthly

## Trunk

After the chunk’s items are on project-main, merge project-main to the
repo’s protected default (**trunk**, usually `main`). That is the
coherent integrate. CHANGELOG may wait for the Changelog step.
**manager** transitions the Epic to `done` with `tracker-sdlc`. Delete
project-main after it is on trunk (or if **manager** cancels the chunk).

**Incoming item with no project-main:** already on trunk after Review.
This step is `n/a`.

## Changelog

Coherent chunk on trunk. Promote `CHANGELOG.md` Unreleased into a dated
chunk heading (template `changelog.md`; see
[Conventions](conventions.md#name-formats)).

**Incoming item already on trunk:** keep the Unreleased line from Build.
Promote it with the next Changelog pass (a later chunk, or a dated
heading that lists that ticket and the trunk SHA). Do not invent a
chunk heading just to close a lone item.

## Monthly

Vuln / updates / new solutions review. Template `monthly.md`. Recurrence
note only until **manager** / **operator** cut a Task. No watcher, no
cron required.

Monthly is **not** the security gate. **security** already gated trust
boundaries at Spec and Review. Monthly is cadence review of
vulns/updates/new solutions, not a substitute for those gates.
