"""Bind host policy: loopback/private only; refuse unspecified."""

from __future__ import annotations

import pytest

from a2a_webhook_adapter.bind import BindError, validate_bind_host


@pytest.mark.parametrize(
    "host",
    ["127.0.0.1", "::1", "10.0.0.1", "192.168.1.10", "172.16.0.2"],
)
def test_allows_loopback_and_private(host: str) -> None:
    assert validate_bind_host(host) == host


def test_localhost_maps_to_loopback() -> None:
    assert validate_bind_host("localhost") == "127.0.0.1"


@pytest.mark.parametrize(
    "host",
    ["0.0.0.0", "::", "[::]", "*", "::0", "8.8.8.8", "example.com", ""],
)
def test_refuses_public_unspecified_and_names(host: str) -> None:
    with pytest.raises(BindError):
        validate_bind_host(host)
