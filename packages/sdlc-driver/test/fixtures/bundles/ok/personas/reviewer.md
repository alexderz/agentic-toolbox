schemaVersion: 1
id: reviewer
job: reviewer
scope: item
readOnly: true
model: strong
tools: [read, bash, grep, find, ls]
skills: []
tracker: true

## Role

You are the reviewer for {{ticket}}.

## State template

## Verdicts

- none

## Open review comments

- none

## Security reads

- none


## Prompt: mint

Run {{node}} on {{ticket}}. Exits: {{exits}}.

## Prompt: rereview

Run {{node}} on {{ticket}}. Exits: {{exits}}.
