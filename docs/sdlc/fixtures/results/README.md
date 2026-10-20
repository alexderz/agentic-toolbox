# Result fixtures

Each fixture is three files, read together by the stage-result reader:

- `NAME.json`: the submitted result.
- `NAME.context.json`: the invocation context, `{"ticket": …, "runFolder": …, "files": […]}`. `ticket` is the invocation ticket, `runFolder` is the stage's run folder under the run root, and `files` lists the run-root-relative paths that exist (a folder ends in `/`).
- `NAME.expect.json`: `{"valid": …, "codes": […]}`.

Each invalid fixture yields exactly its one code. The artifact checks run in order: syntax (`result.artifact-path`), run folder (`result.artifact-outside-run`), existence (`result.artifact-missing`). A parse failure stops all later checks.
