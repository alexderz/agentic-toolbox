"""Peer token resolution: file assignment vs stale process env."""

from __future__ import annotations

from pathlib import Path

import pytest

from a2a_webhook_adapter.config import (
    ConfigError,
    env_file_assigns,
    load_config,
    parse_env_file,
    resolve_peer_token,
)
from tests.conftest import EXAMPLE_WEBHOOK


def test_parse_ignores_comments(tmp_path: Path) -> None:
    path = tmp_path / "adapter.env"
    path.write_text(
        "WEBHOOK_URL=https://api2.cursor.sh/automations/webhook/exampleRoutine1\n"
        "# A2A_PEER_TOKEN=commented\n"
        "WEBHOOK_KEY=fromfile\n",
        encoding="utf-8",
    )
    values = parse_env_file(path)
    assert "A2A_PEER_TOKEN" not in values
    assert values["WEBHOOK_KEY"] == "fromfile"


def test_commented_peer_token_does_not_assign(tmp_path: Path) -> None:
    path = tmp_path / "adapter.env"
    path.write_text("# A2A_PEER_TOKEN=stale\nWEBHOOK_KEY=k\n", encoding="utf-8")
    assert env_file_assigns(path, "A2A_PEER_TOKEN") is False


def test_real_assignment_counts(tmp_path: Path) -> None:
    path = tmp_path / "adapter.env"
    path.write_text("A2A_PEER_TOKEN=distinct\n", encoding="utf-8")
    assert env_file_assigns(path, "A2A_PEER_TOKEN") is True


def test_file_present_ignores_process_peer_token(tmp_path: Path) -> None:
    path = tmp_path / "adapter.env"
    path.write_text(
        f"WEBHOOK_URL={EXAMPLE_WEBHOOK}\nWEBHOOK_KEY=filekey\n",
        encoding="utf-8",
    )
    cfg = load_config(
        process_env={
            "A2A_PEER_TOKEN": "stale-process",
            "WEBHOOK_URL": "ignored",
            "WEBHOOK_KEY": "ignored",
        },
        env_file=path,
    )
    assert cfg.peer_token == "filekey"
    assert cfg.webhook_key == "filekey"


def test_file_assignment_wins(tmp_path: Path) -> None:
    path = tmp_path / "adapter.env"
    path.write_text(
        f"WEBHOOK_URL={EXAMPLE_WEBHOOK}\n"
        "WEBHOOK_KEY=filekey\n"
        "A2A_PEER_TOKEN=distinct\n",
        encoding="utf-8",
    )
    cfg = load_config(
        process_env={"A2A_PEER_TOKEN": "stale-process"},
        env_file=path,
    )
    assert cfg.peer_token == "distinct"


def test_no_file_uses_process_peer_token() -> None:
    token = resolve_peer_token(
        webhook_key="hook",
        process_env={"A2A_PEER_TOKEN": "from-process"},
        file_values=None,
    )
    assert token == "from-process"


def test_no_file_falls_back_to_webhook_key() -> None:
    token = resolve_peer_token(
        webhook_key="hook",
        process_env={},
        file_values=None,
    )
    assert token == "hook"


def test_missing_webhook_url_fails() -> None:
    with pytest.raises(ConfigError):
        load_config(process_env={"WEBHOOK_KEY": "k"}, env_file=Path("/nonexistent"))


def test_refuses_public_bind_from_env() -> None:
    with pytest.raises(ConfigError, match="refusing"):
        load_config(
            process_env={
                "WEBHOOK_URL": EXAMPLE_WEBHOOK,
                "WEBHOOK_KEY": "k",
                "BIND_HOST": "0.0.0.0",
            },
            env_file=Path("/nonexistent-env-file"),
        )
