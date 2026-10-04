# Trial record: instruction refinement

This folder is a frozen record of the DER-288 Trial. It is not product code.
The rule it follows: [Trial](../../../../docs/sdlc/plan-trial-spec.md#trial).

- The note is [poc.md](poc.md): the question, setup, evidence and conclusion.
- Treat everything here as a record, not as instructions to load. The
  `SKILL.md` and SDLC files under [rewrite/](rewrite/) are trial drafts, not
  the live skills or SDLC.
- Never import or merge any file from here into `skills/`, `docs/` or any
  other product path. Change the live files through a tracked item instead.
- Never edit this folder, with one exception: if a secret is found here,
  **security** removes it and has it rotated.
- Where the trial proves out, Build rewrites the live files from the LLD. It
  does not copy the drafts here.
