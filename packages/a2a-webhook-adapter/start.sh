#!/usr/bin/env bash
# Start the A2A webhook adapter. Unsets a stale A2A_PEER_TOKEN when the
# env file is present but does not assign that key.
set -euo pipefail
IFS=$'\n\t'
umask 077

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENV_FILE="${A2A_ADAPTER_ENV:-${HOME}/.config/a2a-webhook-adapter/adapter.env}"

_file_assigns_peer_token() {
  local f="${1:?}"
  [[ -f "$f" ]] || return 1
  grep -Eq '^[[:space:]]*A2A_PEER_TOKEN=' "$f"
}

if [[ -f "$ENV_FILE" ]]; then
  if ! _file_assigns_peer_token "$ENV_FILE"; then
    unset A2A_PEER_TOKEN || true
  fi
  set -a
  # shellcheck disable=SC1090
  source "$ENV_FILE"
  set +a
fi

if [[ "${A2A_ADAPTER_DRY_RUN:-}" == "1" ]]; then
  if [[ -n "${A2A_PEER_TOKEN:-}" ]]; then
    printf 'peer_token=set\n'
  else
    printf 'peer_token=unset\n'
  fi
  exit 0
fi

export PYTHONPATH="${ROOT}/src${PYTHONPATH:+:${PYTHONPATH}}"
cd -- "$ROOT"
exec python3 -m a2a_webhook_adapter "$@"
