"""Black-box tests: run grok_acp.py against a fake ACP agent named `grok`."""

import json
import os
import signal
import subprocess
import sys
import time
from pathlib import Path

import pytest

HERE = Path(__file__).parent
CLIENT = HERE.parent / "grok_acp.py"


@pytest.fixture
def box(tmp_path):
    """A sandbox: fake `grok` first on PATH, private state dir, two worktrees."""
    bindir = tmp_path / "bin"
    bindir.mkdir()
    fake = bindir / "grok"
    fake.write_text(f"#!/bin/sh\nexec {sys.executable} {HERE / 'fake_grok.py'}\n")
    fake.chmod(0o755)
    for name in ("wt1", "wt2"):
        (tmp_path / name).mkdir()
    env = dict(
        os.environ,
        PATH=f"{bindir}:{os.environ['PATH']}",
        GROK_ACP_STATE=str(tmp_path / "state"),
        GROK_ACP_CANCEL_GRACE="1",
        FAKE_LOG=str(tmp_path / "fake.log"),
    )
    return tmp_path, env


def start(box, *args, **extra_env):
    tmp, env = box
    cmd = [sys.executable, str(CLIENT), "run", "--prompt", "hi", *args]
    return subprocess.Popen(
        cmd,
        env=dict(env, **extra_env),
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True,
    )


def run(box, *args, **extra_env):
    proc = start(box, *args, **extra_env)
    stdout, _ = proc.communicate(timeout=60)
    return proc.returncode, json.loads(stdout)


def registry(box):
    return json.loads((box[0] / "state" / "sessions.json").read_text())


def fake_log(box):
    path = box[0] / "fake.log"
    return path.read_text().split() if path.exists() else []


def wait_for(predicate, seconds=10):
    end = time.monotonic() + seconds
    while time.monotonic() < end:
        if predicate():
            return
        time.sleep(0.05)
    raise AssertionError("condition not reached")


def test_mint_then_resume_keeps_one_session(box):
    wt = str(box[0] / "wt1")
    rc, first = run(box, "--cwd", wt, "--label", "T-1:builder")
    assert (rc, first["ok"], first["text"]) == (0, True, "done")
    rc, second = run(box, "--cwd", wt, "--resume", "T-1:builder")
    assert rc == 0 and second["resumed"] is True
    assert second["sessionId"] == first["sessionId"]
    assert registry(box)["T-1:builder"]["turns"] == 2
    assert fake_log(box).count("session/new") == 1


def test_state_and_run_dirs_are_private(box):
    out_dir = box[0] / "out"
    run(box, "--cwd", str(box[0] / "wt1"), "--out", str(out_dir))
    assert (box[0] / "state").stat().st_mode & 0o777 == 0o700
    assert out_dir.stat().st_mode & 0o777 == 0o700
    assert {p.name for p in out_dir.iterdir()} >= {
        "prompt.md",
        "response.md",
        "result.json",
        "events.ndjson",
    }


def test_existing_label_needs_resume_or_replace(box):
    wt = str(box[0] / "wt1")
    _, first = run(box, "--cwd", wt, "--label", "T-1:builder")
    rc, clash = run(box, "--cwd", wt, "--label", "T-1:builder")
    assert (rc, clash["error"]) == (2, "label_exists")
    rc, new = run(box, "--cwd", wt, "--label", "T-1:builder", "--replace")
    assert rc == 0 and new["sessionId"] != first["sessionId"]


def test_resume_cannot_clobber_another_items_label(box):
    run(box, "--cwd", str(box[0] / "wt1"), "--label", "A:builder")
    _, b = run(box, "--cwd", str(box[0] / "wt2"), "--label", "B:builder")
    rc, res = run(
        box,
        "--cwd",
        str(box[0] / "wt1"),
        "--resume",
        "A:builder",
        "--label",
        "B:builder",
    )
    assert (rc, res["error"]) == (2, "label_exists")
    assert registry(box)["B:builder"]["sessionId"] == b["sessionId"]


def test_usage_errors_are_json_with_exit_2(box):
    wt = str(box[0] / "wt1")
    run(box, "--cwd", wt, "--label", "A:builder")
    cases = {
        "unknown_label": ["--cwd", wt, "--resume", "A:bulder"],
        "cwd_mismatch": ["--cwd", str(box[0] / "wt2"), "--resume", "A:builder"],
        "bad_cwd": ["--cwd", str(box[0] / "nope")],
        "bad_out": ["--cwd", wt, "--out", "/proc/nope"],
    }
    for error, args in cases.items():
        rc, res = run(box, *args)
        assert (rc, res["ok"], res["error"]) == (2, False, error)
    tmp, env = box
    for error, args in {
        "unreadable_file": ["--prompt-file", "/nope"],
        "empty_prompt": ["--prompt", ""],
        "bad_args": ["--prompt", "x", "--replace"],
    }.items():
        cmd = [sys.executable, str(CLIENT), "run", "--cwd", wt, *args]
        proc = subprocess.run(cmd, env=env, capture_output=True, text=True, timeout=60)
        assert (proc.returncode, json.loads(proc.stdout)["error"]) == (2, error)


def test_failed_resume_is_exit_3(box):
    wt = str(box[0] / "wt1")
    run(box, "--cwd", wt, "--label", "A:builder")
    rc, res = run(box, "--cwd", wt, "--resume", "A:builder", FAKE_FAIL_RESUME="1")
    assert rc == 3 and res["error"].startswith("resume failed")


def test_missing_grok_is_exit_4(box):
    tmp, env = box
    lonely = dict(env, PATH="/usr/bin:/bin", HOME=str(tmp / "nohome"))
    cmd = [
        sys.executable,
        str(CLIENT),
        "run",
        "--cwd",
        str(tmp / "wt1"),
        "--prompt",
        "x",
    ]
    proc = subprocess.run(cmd, env=lonely, capture_output=True, text=True, timeout=60)
    assert proc.returncode == 4
    assert json.loads(proc.stdout)["error"] == "agent_error"


def test_permission_requests_get_the_widest_allow(box):
    rc, res = run(box, "--cwd", str(box[0] / "wt1"), FAKE_ASK="1")
    assert rc == 0 and res["permissionRequestsAutoApproved"] == 1
    assert "picked=always" in fake_log(box)


def test_timeout_sends_cancel_and_exits_5(box):
    rc, res = run(box, "--cwd", str(box[0] / "wt1"), "--timeout", "1", FAKE_HANG="1")
    assert (rc, res["stopReason"]) == (5, "cancelled")
    assert res["error"] == "cancelled by timeout"
    assert fake_log(box).count("session/cancel") == 1


def test_signal_before_session_sends_no_prompt(box):
    proc = start(box, "--cwd", str(box[0] / "wt1"), "--label", "C:b", FAKE_SLOW_NEW="2")
    wait_for(lambda: "session/new" in fake_log(box))
    proc.send_signal(signal.SIGTERM)
    stdout, _ = proc.communicate(timeout=30)
    res = json.loads(stdout)
    assert proc.returncode == 5 and res["sessionId"] is None
    assert "session/prompt" not in fake_log(box)
    assert not (box[0] / "state" / "sessions.json").exists()


def test_signal_mid_prompt_with_deaf_agent_exits_after_grace(box):
    proc = start(
        box,
        "--cwd",
        str(box[0] / "wt1"),
        "--timeout",
        "600",
        FAKE_HANG="1",
        FAKE_IGNORE_CANCEL="1",
    )
    wait_for(lambda: "session/prompt" in fake_log(box))
    began = time.monotonic()
    proc.send_signal(signal.SIGTERM)
    proc.send_signal(signal.SIGINT)
    stdout, _ = proc.communicate(timeout=30)
    assert proc.returncode == 5 and time.monotonic() - began < 10
    assert "not acknowledged" in json.loads(stdout)["error"]
    assert fake_log(box).count("session/cancel") == 1


def test_second_turn_on_a_busy_session_is_refused(box):
    wt = str(box[0] / "wt1")
    run(box, "--cwd", wt, "--label", "A:builder")
    turns_before = fake_log(box).count("session/prompt")
    hog = start(
        box, "--cwd", wt, "--resume", "A:builder", "--timeout", "5", FAKE_HANG="1"
    )
    wait_for(lambda: fake_log(box).count("session/prompt") > turns_before)
    rc, res = run(box, "--cwd", wt, "--resume", "A:builder")
    assert (rc, res["error"]) == (2, "busy")
    hog.communicate(timeout=30)


def test_leftover_children_are_killed(box):
    pid_file = box[0] / "child.pid"
    rc, res = run(box, "--cwd", str(box[0] / "wt1"), FAKE_CHILD_PID=str(pid_file))
    assert rc == 0 and res["leftoverProcessesKilled"] >= 1
    pid = int(pid_file.read_text())

    def gone():
        try:
            state = Path(f"/proc/{pid}/stat").read_text().rsplit(")", 1)[1].split()[0]
        except OSError:
            return True
        return state == "Z"

    wait_for(gone)


def test_forget_and_sessions(box):
    tmp, env = box
    run(box, "--cwd", str(tmp / "wt1"), "--label", "A:builder")
    base = [sys.executable, str(CLIENT)]
    listed = subprocess.run(
        [*base, "sessions"], env=env, capture_output=True, text=True
    )
    assert "A:builder" in json.loads(listed.stdout)
    assert subprocess.run([*base, "forget", "A:builder"], env=env).returncode == 0
    assert registry(box) == {}
    assert subprocess.run([*base, "forget", "A:builder"], env=env).returncode == 2
