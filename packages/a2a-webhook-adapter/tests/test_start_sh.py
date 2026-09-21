"""start.sh unsets stale A2A_PEER_TOKEN unless the env file assigns it."""

from __future__ import annotations

import os
import stat
import subprocess
from pathlib import Path

PACKAGE = Path(__file__).resolve().parents[1]
START = PACKAGE / "start.sh"


def _run(env_file: Path, extra_env: dict[str, str]) -> str:
    env = os.environ.copy()
    env.update(extra_env)
    env["A2A_ADAPTER_ENV"] = str(env_file)
    env["A2A_ADAPTER_DRY_RUN"] = "1"
    completed = subprocess.run(
        ["bash", str(START)],
        check=True,
        capture_output=True,
        text=True,
        env=env,
        timeout=5,
    )
    return completed.stdout.strip()


def test_start_sh_is_executable() -> None:
    mode = START.stat().st_mode
    assert mode & stat.S_IXUSR


def test_unsets_stale_process_token_when_file_omits_it(tmp_path: Path) -> None:
    env_file = tmp_path / "adapter.env"
    env_file.write_text("WEBHOOK_KEY=filekey\n", encoding="utf-8")
    out = _run(env_file, {"A2A_PEER_TOKEN": "stale-from-parent-shell"})
    assert out == "peer_token=unset"


def test_commented_assignment_does_not_keep_stale(tmp_path: Path) -> None:
    env_file = tmp_path / "adapter.env"
    env_file.write_text(
        "# A2A_PEER_TOKEN=commented\nWEBHOOK_KEY=filekey\n", encoding="utf-8"
    )
    out = _run(env_file, {"A2A_PEER_TOKEN": "stale-from-parent-shell"})
    assert out == "peer_token=unset"


def test_file_assignment_is_kept(tmp_path: Path) -> None:
    env_file = tmp_path / "adapter.env"
    env_file.write_text("A2A_PEER_TOKEN=distinct\n", encoding="utf-8")
    out = _run(env_file, {"A2A_PEER_TOKEN": "stale-from-parent-shell"})
    assert out == "peer_token=set"


def test_no_env_file_keeps_process_token(tmp_path: Path) -> None:
    missing = tmp_path / "missing.env"
    out = _run(missing, {"A2A_PEER_TOKEN": "from-process"})
    assert out == "peer_token=set"
