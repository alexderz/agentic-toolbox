#!/usr/bin/env bash
# Stop a background adapter started from this directory (PID file).
set -euo pipefail
IFS=$'\n\t'

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PID_FILE="${A2A_ADAPTER_PID:-${ROOT}/adapter.pid}"

if [[ ! -f "$PID_FILE" ]]; then
  printf 'no pid file\n' >&2
  exit 0
fi

pid="$(tr -d '[:space:]' <"$PID_FILE")"
if [[ ! "$pid" =~ ^[0-9]+$ ]]; then
  printf 'invalid pid file\n' >&2
  exit 1
fi

if kill -0 "$pid" 2>/dev/null; then
  kill "$pid"
fi
rm -f -- "$PID_FILE"
