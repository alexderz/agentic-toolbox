schemaVersion: 1
id: env-builder
job: builder
scope: chunk
readOnly: false
model: local
tools: [read, bash, edit, write, grep, find, ls]
skills: []
tracker: true
## Role
Do the job.

## State template
## Corrected errors
- none
## Open findings
- none
## Do not repeat
- none
## Next
- none

## Prompt: node-env-prep
Do node-env-prep.

## Prompt: resume
Do resume.

## Prompt: test-failure
Do test-failure.

## Prompt: fix
Do fix.

## Prompt: merge-tip
Do merge-tip.
