"""The proxy's whole job is refusing writes. Prove it without a live target."""
import importlib.util
import pathlib
import sys

import pytest

SRC = pathlib.Path(__file__).resolve().parents[1] / "src" / "model_eval" / "readonly_proxy.py"


def load(monkeypatch, tmp_path):
    token = tmp_path / "token"
    token.write_text("upstream-secret")
    monkeypatch.setenv("HA_TOKEN_FILE", str(token))
    spec = importlib.util.spec_from_file_location("readonly_proxy", SRC)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["readonly_proxy"] = mod
    spec.loader.exec_module(mod)
    return mod


def test_only_safe_methods_allowed(monkeypatch, tmp_path):
    m = load(monkeypatch, tmp_path)
    assert m.ALLOWED_METHODS == {"GET", "HEAD"}
    for verb in ("POST", "PUT", "DELETE", "PATCH"):
        assert verb not in m.ALLOWED_METHODS


def test_write_shaped_paths_blocked(monkeypatch, tmp_path):
    m = load(monkeypatch, tmp_path)
    blocked = m.BLOCKED_PREFIXES
    # calling a service or firing an event is refused ...
    assert any("/api/services/".startswith(p) or p == "/api/services/" for p in blocked)
    assert any(p == "/api/events/" for p in blocked)
    # ... but the bare listings stay discoverable
    assert not any("/api/services".startswith(p) and len(p) <= len("/api/services")
                   for p in blocked if p != "/api/services/")


def test_rate_limit_bounds_burst(monkeypatch, tmp_path):
    m = load(monkeypatch, tmp_path)
    m._hits.clear()
    allowed = sum(1 for _ in range(m.BURST * 2) if m.allow("client-a"))
    assert allowed == m.BURST


def test_rate_limit_is_per_client(monkeypatch, tmp_path):
    m = load(monkeypatch, tmp_path)
    m._hits.clear()
    for _ in range(m.BURST):
        m.allow("client-a")
    assert m.allow("client-b") is True


def test_upstream_credential_never_defaults_to_client_token(monkeypatch, tmp_path):
    m = load(monkeypatch, tmp_path)
    assert m.HA_TOKEN == "upstream-secret"
    assert m.CLIENT_TOKEN != m.HA_TOKEN


def test_missing_token_file_is_fatal(monkeypatch, tmp_path):
    monkeypatch.setenv("HA_TOKEN_FILE", str(tmp_path / "nope"))
    spec = importlib.util.spec_from_file_location("readonly_proxy_missing", SRC)
    mod = importlib.util.module_from_spec(spec)
    with pytest.raises(SystemExit):
        spec.loader.exec_module(mod)
