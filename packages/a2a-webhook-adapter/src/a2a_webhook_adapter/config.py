"""Load operator config from an env file and/or process environment.

When an env file is in use, ``A2A_PEER_TOKEN`` is taken only from a
real assignment in that file. A commented ``# A2A_PEER_TOKEN=`` does
not count. Process env is honored only when there is no env file
(foreground ``python -m`` and tests).
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass
from pathlib import Path

from a2a_webhook_adapter.bind import validate_bind_host
from a2a_webhook_adapter.webhook import validate_webhook_url

_ASSIGN = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*)=(.*)$")
_DEFAULT_ENV = Path.home() / ".config" / "a2a-webhook-adapter" / "adapter.env"
DEFAULT_BIND_HOST = "127.0.0.1"
DEFAULT_BIND_PORT = 8780
MAX_BODY_BYTES = 262_144
RATE_LIMIT_PER_MINUTE = 30


class ConfigError(ValueError):
    """Raised when required configuration is missing or invalid."""


def parse_env_file(path: Path) -> dict[str, str]:
    """Parse ``KEY=value`` lines. Comments and blank lines are ignored."""
    values: dict[str, str] = {}
    text = path.read_text(encoding="utf-8")
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        match = _ASSIGN.match(line)
        if match is None:
            continue
        key, value = match.group(1), match.group(2)
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        values[key] = value
    return values


def env_file_assigns(path: Path, key: str) -> bool:
    """Return True if *path* contains a non-comment assignment of *key*."""
    if not path.is_file():
        return False
    return key in parse_env_file(path)


def resolve_peer_token(
    *,
    webhook_key: str,
    process_env: dict[str, str],
    file_values: dict[str, str] | None,
) -> str:
    """Return the A2A Bearer secret.

    File present: only a file assignment of ``A2A_PEER_TOKEN`` counts;
    otherwise ``WEBHOOK_KEY``. No file: process ``A2A_PEER_TOKEN`` or
    ``WEBHOOK_KEY``. Empty values fall back to ``WEBHOOK_KEY``.
    """
    if file_values is not None:
        assigned = file_values.get("A2A_PEER_TOKEN", "")
        if assigned.strip():
            return assigned
        return webhook_key
    assigned = process_env.get("A2A_PEER_TOKEN", "")
    if assigned.strip():
        return assigned
    return webhook_key


@dataclass(frozen=True)
class Config:
    webhook_url: str
    webhook_key: str
    peer_token: str
    bind_host: str
    bind_port: int
    max_body_bytes: int
    rate_limit_per_minute: int
    env_file: Path | None


def _merged(
    process_env: dict[str, str],
    file_values: dict[str, str] | None,
) -> dict[str, str]:
    merged = dict(process_env)
    if file_values:
        merged.update(file_values)
    return merged


def load_config(
    *,
    process_env: dict[str, str] | None = None,
    env_file: Path | None = None,
    env_file_required: bool = False,
) -> Config:
    """Load and validate config. Raises ``ConfigError`` if fail-closed."""
    env = dict(os.environ if process_env is None else process_env)
    path = env_file
    if path is None:
        override = env.get("A2A_ADAPTER_ENV", "").strip()
        path = Path(override) if override else _DEFAULT_ENV

    file_values: dict[str, str] | None = None
    if path.is_file():
        file_values = parse_env_file(path)
    elif env_file_required:
        raise ConfigError(f"env file not found: {path}")

    merged = _merged(env, file_values)
    webhook_url = merged.get("WEBHOOK_URL", "").strip()
    webhook_key = merged.get("WEBHOOK_KEY", "").strip()
    if not webhook_url:
        raise ConfigError("WEBHOOK_URL is required")
    if not webhook_key:
        raise ConfigError("WEBHOOK_KEY is required")
    try:
        validate_webhook_url(webhook_url)
    except ValueError as exc:
        raise ConfigError(str(exc)) from exc

    peer = resolve_peer_token(
        webhook_key=webhook_key,
        process_env=env,
        file_values=file_values,
    )
    if not peer.strip():
        raise ConfigError("peer token resolved empty")

    bind_host = merged.get("BIND_HOST", DEFAULT_BIND_HOST).strip() or DEFAULT_BIND_HOST
    try:
        bind_host = validate_bind_host(bind_host)
    except ValueError as exc:
        raise ConfigError(str(exc)) from exc

    port_raw = merged.get("BIND_PORT", str(DEFAULT_BIND_PORT)).strip()
    try:
        bind_port = int(port_raw)
    except ValueError as exc:
        raise ConfigError("BIND_PORT must be an integer") from exc
    if not (1 <= bind_port <= 65535):
        raise ConfigError("BIND_PORT out of range")

    return Config(
        webhook_url=webhook_url,
        webhook_key=webhook_key,
        peer_token=peer,
        bind_host=bind_host,
        bind_port=bind_port,
        max_body_bytes=MAX_BODY_BYTES,
        rate_limit_per_minute=RATE_LIMIT_PER_MINUTE,
        env_file=path if path.is_file() else None,
    )
