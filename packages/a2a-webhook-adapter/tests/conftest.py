"""Shared test helpers. No live webhook calls."""

from __future__ import annotations

import threading
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

from a2a_webhook_adapter.config import Config
from a2a_webhook_adapter.server import AdapterHTTPServer, make_server

EXAMPLE_WEBHOOK = "https://api2.cursor.sh/automations/webhook/exampleRoutine1"
EXAMPLE_KEY = "crsr_test_placeholder_not_a_secret"


def make_config(**overrides: object) -> Config:
    data = {
        "webhook_url": EXAMPLE_WEBHOOK,
        "webhook_key": EXAMPLE_KEY,
        "peer_token": EXAMPLE_KEY,
        "bind_host": "127.0.0.1",
        "bind_port": 0,
        "max_body_bytes": 262_144,
        "rate_limit_per_minute": 30,
        "env_file": None,
    }
    data.update(overrides)
    return Config(**data)  # type: ignore[arg-type]


@contextmanager
def running_server(
    config: Config | None = None,
    *,
    forward=None,
    rate_limit: int | None = None,
) -> Iterator[tuple[AdapterHTTPServer, str]]:
    cfg = config or make_config()
    if rate_limit is not None:
        cfg = make_config(rate_limit_per_minute=rate_limit)
    server = make_server(cfg, forward=forward, bind_host="127.0.0.1", bind_port=0)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        host, port = server.server_address[:2]
        yield server, f"http://{host}:{port}"
    finally:
        server.shutdown()
        server.server_close()


FIXTURES = Path(__file__).parent / "fixtures"
