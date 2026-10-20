schemaVersion: 1
id: security
job: security
scope: chunk
readOnly: true
model: strong
tools: [read, bash, grep, find, ls]
skills: []
tracker: true

## Role

You are the security for {{ticket}}.

## State template

## Next

(one line)

## Prompt: mint

Run {{node}} on {{ticket}}. Exits: {{exits}}.

## Prompt: resume

Run {{node}} on {{ticket}}. Exits: {{exits}}.
