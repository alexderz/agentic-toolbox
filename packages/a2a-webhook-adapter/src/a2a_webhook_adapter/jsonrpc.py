"""JSON-RPC 2.0 helpers and A2A SendMessage extraction."""

from __future__ import annotations

from typing import Any

PARSE_ERROR = -32700
INVALID_REQUEST = -32600
METHOD_NOT_FOUND = -32601
INVALID_PARAMS = -32602
INTERNAL_ERROR = -32603
TASK_NOT_FOUND = -32001
UNSUPPORTED_OPERATION = -32004

SEND_METHODS = frozenset({"SendMessage", "message/send"})
GET_TASK_METHODS = frozenset({"GetTask", "tasks/get"})
CANCEL_METHODS = frozenset({"CancelTask", "tasks/cancel"})


def rpc_error(req_id: object, code: int, message: str) -> dict[str, Any]:
    """Return a JSON-RPC error object. Do not put secrets in *message*."""
    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "error": {"code": code, "message": message},
    }


def rpc_result(req_id: object, result: dict[str, Any]) -> dict[str, Any]:
    """Return a JSON-RPC success object."""
    return {"jsonrpc": "2.0", "id": req_id, "result": result}


def _as_dict(value: object) -> dict[str, Any] | None:
    return value if isinstance(value, dict) else None


def extract_user_text(params: dict[str, Any]) -> str | None:
    """Return concatenated text parts from an A2A message.

    Accepts A2A 1.0 bare ``{text}`` parts (no ``kind``) and the older
    ``{kind: text, text}`` shape. Roles ``ROLE_USER`` and ``user`` are
    both accepted so an example A2A client can speak either dialect.
    """
    message = _as_dict(params.get("message")) or _as_dict(params.get("params"))
    if message is None:
        # Some clients nest SendMessageRequest at the top of params.
        message = params if "parts" in params else None
    if message is None:
        return None
    role = str(message.get("role", "")).strip()
    if role and role not in {"ROLE_USER", "user"}:
        return None
    parts = message.get("parts")
    if not isinstance(parts, list) or not parts:
        return None
    chunks: list[str] = []
    for part in parts:
        if not isinstance(part, dict):
            continue
        kind = str(part.get("kind", "")).lower()
        if kind and kind not in {"text", "text/plain"}:
            continue
        text = part.get("text")
        if isinstance(text, str) and text.strip():
            chunks.append(text)
    if not chunks:
        return None
    return "\n".join(chunks)


def message_ids(params: dict[str, Any]) -> tuple[str | None, str | None]:
    """Return ``(messageId, contextId)`` from params when present."""
    message = _as_dict(params.get("message")) or params
    mid = message.get("messageId") or message.get("message_id")
    cid = message.get("contextId") or message.get("context_id")
    return (
        str(mid) if isinstance(mid, str) else None,
        str(cid) if isinstance(cid, str) else None,
    )
