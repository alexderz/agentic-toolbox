"""CLI entry: ``python3 -m a2a_webhook_adapter``."""

from __future__ import annotations

import sys

from a2a_webhook_adapter.config import ConfigError, load_config
from a2a_webhook_adapter.server import serve_forever


def main(argv: list[str] | None = None) -> int:
    """Load config and serve. Returns a process exit code."""
    del argv
    try:
        config = load_config()
    except ConfigError as exc:
        print(f"config error: {exc}", file=sys.stderr)
        return 2
    serve_forever(config)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
