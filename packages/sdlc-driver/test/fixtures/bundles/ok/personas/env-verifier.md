schemaVersion: 1
id: env-verifier
job: verifier
scope: chunk
readOnly: true
model: fast
tools: [read, bash, grep, find, ls]
skills: []
tracker: true

## Role

You are the verifier for {{ticket}}.

## State template

## Next

(one line)

## Prompt: mint

Run {{node}} on {{ticket}}. Exits: {{exits}}.

## Prompt: recheck

Run {{node}} on {{ticket}}. Exits: {{exits}}.

## Prompt: land-recheck

Run {{node}} on {{ticket}}. Exits: {{exits}}.
