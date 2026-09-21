# A2A webhook adapter

Stdlib Python HTTP server that speaks **A2A JSON-RPC** to a peer and
forwards each accepted `SendMessage` as a **plain HTTPS POST** to a
webhook (a Cursor Grok Bot webhook routine).

This package is MIT, same as the repository
[LICENSE](../../LICENSE). No extra runtime dependencies.

**Origin:** first-party sanitized extract inspired by a private court
adapter. Public history: `alexderz/grok-bot-perm` pull requests
[#6](https://github.com/alexderz/grok-bot-perm/pull/6) and
[#7](https://github.com/alexderz/grok-bot-perm/pull/7). This copy does
not include house names as required identifiers, mesh addresses, or
secrets.

## What this is

An A2A client (for example OpenClaw) POSTs JSON-RPC to this process.
The adapter authenticates the peer, extracts user text, and POSTs
`{"text": "…"}` to `WEBHOOK_URL` with `Authorization: Bearer WEBHOOK_KEY`.
The JSON-RPC result is `result.task` (echo the request `id`). A body of
`{"ok": true}` is not a valid SendMessage result.

## How it works

```
A2A peer  --Bearer-->  POST /a2a/v1 (this process, loopback or private)
                       GET  /.well-known/agent-card.json
                  \--> HTTPS POST WEBHOOK_URL (allowlisted host, no redirects)
```

1. `GET /.well-known/agent-card.json` (also `/.well-known/agent.json`)
   returns A2A 1.0 `supportedInterfaces[]`.
2. `POST /a2a/v1` requires `Authorization: Bearer`.
3. Methods: `SendMessage` / `message/send` (forward), `GetTask` (stub),
   `CancelTask` (JSON-RPC `-32004` unsupported).
4. Outbound wire: `ROLE_USER` (or `user`), text parts as bare `{text}`
   (no `kind` required), `returnImmediately` accepted.

## How to use it

1. Copy `.env.example` to `~/.config/a2a-webhook-adapter/adapter.env`.
2. Replace `YOUR_ROUTINE_ID` and `WEBHOOK_KEY` with values from the
   webhook routine panel. `chmod 600` the file.
3. Leave `A2A_PEER_TOKEN` unset unless you want a Bearer distinct from
   `WEBHOOK_KEY`. A commented `# A2A_PEER_TOKEN=` does not count.
4. Bind loopback (`127.0.0.1`) or a private address. Do not bind
   `0.0.0.0` or `::`.
5. From this directory: `./start.sh` (or
   `PYTHONPATH=src python3 -m a2a_webhook_adapter`).
6. Point the A2A peer URL at `http://127.0.0.1:8780/a2a/v1` and set its
   outbound token to the same value the adapter uses for Bearer.

Prove the suite:

```bash
cd packages/a2a-webhook-adapter
python3 -m pytest
```

### Environment variables

| Name | Required | Meaning |
| --- | --- | --- |
| `WEBHOOK_URL` | yes | HTTPS allowlisted webhook |
| `WEBHOOK_KEY` | yes | Bearer secret for the webhook POST |
| `A2A_PEER_TOKEN` | no | Bearer for the A2A peer; defaults to `WEBHOOK_KEY` |
| `BIND_HOST` | no | Listen IP; default `127.0.0.1` |
| `BIND_PORT` | no | Listen port; default `8780` |
| `A2A_ADAPTER_ENV` | no | Path to the env file |

`start.sh` unsets a stale process `A2A_PEER_TOKEN` when the env file
exists and does not assign that key, then sources the file (`umask 077`).
Secrets stay out of argv.

An optional unit file lives in
`systemd/a2a-webhook-adapter.service`. Replace user and paths before
install. This repository does not deploy it.

## Security notes (Always / Ask / Never)

**Always**

- Validate at the boundary: JSON-RPC schema, Bearer, body size, rate
  limit.
- HTTPS webhook only. Host and path allowlist. No redirect follow.
- Timing-safe Bearer compare (SHA-256 then `hmac.compare_digest`).
- Bind loopback or RFC1918 private unicast only.
- Redact tokens in logs. `chmod 600` on the env file.

**Ask first**

- New webhook hosts or path shapes (allowlist change).
- Public or mesh-wide listen addresses.
- A second secret class beyond webhook key / optional peer token.

**Never**

- Secrets in git, chat, or command lines that will be logged.
- Bind `0.0.0.0` / `::`.
- Trust the A2A client without Bearer.
- House Soft LLD / operator allow-never lists (out of scope here).

## License

MIT. See the repository [LICENSE](../../LICENSE).
