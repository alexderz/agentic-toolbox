#!/usr/bin/env python3
"""Record a Home Assistant instance to a replayable JSON fixture.

A live target makes an eval unreproducible: entity counts drift, the house
changes, and nobody else can run the suite at all without their own instance.
Recording once and replaying forever fixes that, removes the rate limit as a
concern, and lets the fixture ship with the open-source harness.

Only GET is ever issued. Nothing here can change state.

Usage:
  python3 ha-record.py --url http://127.0.0.1:8124 --token <tok> --out fixture.json
"""
import argparse
import json
import pathlib
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

# Endpoints worth having in a fixture, in the order a curious agent tends to
# hit them. Per-entity state paths are expanded from /api/states.
BASE_PATHS = [
    "/api/",
    "/api/config",
    "/api/states",
    "/api/services",
    "/api/events",
    "/api/error_log",
    "/api/logbook",
    "/api/calendars",
    "/api/config/core/check_config",
]


def get(url, token, path, timeout=30, retries=6):
    """GET with backoff on 429. The proxy rate limits, and recording an error
    body as if it were data silently produces a useless fixture -- the first
    attempt captured the 429 JSON for /api/states and recorded 1 entity."""
    for attempt in range(retries):
        st, ct, body = _get_once(url, token, path, timeout)
        if st != 429:
            return st, ct, body
        time.sleep(1.5 * (attempt + 1))
    return st, ct, body


def _get_once(url, token, path, timeout=30):
    req = urllib.request.Request(
        url.rstrip("/") + path,
        headers={"Authorization": f"Bearer {token}",
                 "Content-Type": "application/json"},
        method="GET")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.headers.get("Content-Type", "application/json"), r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, "application/json", e.read().decode("utf-8", "replace")
    except Exception as e:
        return 0, "application/json", json.dumps({"error": f"{type(e).__name__}: {e}"})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True, help="base URL (the read-only proxy)")
    ap.add_argument("--token", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--delay", type=float, default=0.25,
                    help="pause between requests so recording stays gentle")
    ap.add_argument("--max-entities", type=int, default=0,
                    help="0 = every entity")
    args = ap.parse_args()

    rec, order = {}, []

    def capture(path):
        st, ct, body = get(args.url, args.token, path)
        rec[path] = {"status": st, "content_type": ct, "body": body}
        order.append(path)
        time.sleep(args.delay)
        return st, body

    print("recording base endpoints", file=sys.stderr)
    for p in BASE_PATHS:
        st, _ = capture(p)
        print(f"  {p:<34} {st}", file=sys.stderr)

    if rec["/api/states"]["status"] != 200:
        sys.exit(f"/api/states returned {rec['/api/states']['status']}; refusing "
                 f"to write a fixture built on an error response")

    # expand per-entity states so a model can look up any single entity
    states_raw = rec.get("/api/states", {}).get("body", "[]")
    try:
        states = json.loads(states_raw)
    except Exception:
        states = []
    if not isinstance(states, list):
        sys.exit(f"/api/states was not a list (got {type(states).__name__}: "
                 f"{states_raw[:120]}); refusing to write a bad fixture")
    ids = [e["entity_id"] for e in states if isinstance(e, dict) and "entity_id" in e]
    if len(ids) < 10:
        sys.exit(f"only {len(ids)} entities parsed; that is not a real recording")
    if args.max_entities:
        ids = ids[:args.max_entities]
    print(f"recording {len(ids)} per-entity states", file=sys.stderr)
    for i, eid in enumerate(ids, 1):
        capture(f"/api/states/{eid}")
        if i % 50 == 0:
            print(f"  {i}/{len(ids)}", file=sys.stderr)

    # a couple of history/logbook shapes so those endpoints are not dead ends
    if ids:
        sample = ids[0]
        for p in (f"/api/history/period?filter_entity_id={urllib.parse.quote(sample)}",
                  f"/api/logbook?entity={urllib.parse.quote(sample)}"):
            st, _ = capture(p)
            print(f"  {p[:50]:<50} {st}", file=sys.stderr)

    # fingerprint: lets a later run tell "the model changed" from "the house did"
    domains = {}
    for e in states:
        if isinstance(e, dict) and "entity_id" in e:
            d = e["entity_id"].split(".")[0]
            domains[d] = domains.get(d, 0) + 1

    fixture = {
        "recorded_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "fingerprint": {
            "entity_count": len(states),
            "domain_counts": dict(sorted(domains.items(), key=lambda kv: -kv[1])),
            "paths_recorded": len(rec),
        },
        "responses": rec,
        "order": order,
    }
    outp = pathlib.Path(args.out)
    outp.parent.mkdir(parents=True, exist_ok=True)
    with outp.open("w") as fh:
        json.dump(fixture, fh)
    print(f"\nwrote {args.out}: {len(rec)} paths, {len(states)} entities, "
          f"{len(domains)} domains", file=sys.stderr)


if __name__ == "__main__":
    main()
