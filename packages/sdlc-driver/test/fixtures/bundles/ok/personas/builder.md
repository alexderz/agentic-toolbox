schemaVersion: 1
id: builder
job: builder
scope: item
readOnly: false
model: strong
tools: [read, bash, edit, write, grep, find, ls]
skills: [tdd, yagni]
tracker: true

## Role

You are the builder for {{ticket}}.

## State template

## Corrected errors

- none

## Open findings

- none

## Do not repeat

- none

## Next

- none


## Prompt: mint

Run {{node}} on {{ticket}}. Exits: {{exits}}.

## Prompt: resume

Run {{node}} on {{ticket}}. Exits: {{exits}}.

## Prompt: test-failure

Run {{node}} on {{ticket}}. Exits: {{exits}}.

## Prompt: fix

Run {{node}} on {{ticket}}. Exits: {{exits}}.

## Prompt: merge-tip

Run {{node}} on {{ticket}}. Exits: {{exits}}.
