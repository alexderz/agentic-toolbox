#!/usr/bin/env python3
"""Render a story test round 3 script to audio with ElevenLabs Eleven v4, then check it.

  ELEVENLABS_API_KEY=... python3 render_narration.py script.md OUTDIR [--voice ID] [--limit N] [--check]

- Converts the script with studio_text.convert(), so every paragraph opens with its tag.
- Splits it into requests at the part breaks and wherever a silence belongs, each under 10,000 characters.
- Renders each request once with the same voice, settings and seed, passing previous_request_ids for continuity, as
  pcm_24000. Requests already on disk are skipped, so a failed run resumes; it stops if the text of a request on disk
  has changed. --limit N renders only the first N.
- Joins the requests with silence into OUTDIR/narration.wav, and OUTDIR/narration.mp3 when lameenc is installed.
- --check transcribes each request with Speech to text (scribe_v1) and reports how its words match the script and any
  tag words or audio events heard, where a spoken tag or a sound effect would show up. A request that already has a
  transcript on disk is not transcribed again.
OUTDIR/render-log.jsonl records each request's characters, request ID, character-cost header and length.
"""
import argparse
import difflib
import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.request
import uuid
import wave

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from studio_text import convert  # noqa: E402

API = "https://api.elevenlabs.io"
RATE = 24000
LIMIT = 10000
SILENCE = {"part": 1.2, "[short pause]": 1.0, "[pause]": 1.6, "[pauses]": 1.6, "[long pause]": 2.0}
TAG = re.compile(r"\[[^\]\n]+\]")


def chunks(paras):
    """Group paragraphs into requests; return [(texts, seconds of silence after)]."""
    out, cur = [], []
    for i, p in enumerate(paras):
        brk = 0.0
        if cur and p["part"]:
            brk = SILENCE["part"]
        if cur and p["gap_before"]:
            brk = max(brk, max(SILENCE[t] for t in p["gap_before"]))
        if cur and len("\n\n".join(cur + [p["text"]])) > LIMIT:
            brk = max(brk, 0.4)
        if brk:
            out.append((cur, brk))
            cur = []
        cur.append(p["text"])
        if p["gap_after"]:
            out.append((cur, max(SILENCE[t] for t in p["gap_after"])))
            cur = []
    if cur:
        out.append((cur, 0.0))
    return out


def post(path, body=None, files=None):
    key = os.environ["ELEVENLABS_API_KEY"]
    headers = {"xi-api-key": key}
    if files is not None:
        boundary = uuid.uuid4().hex
        parts = []
        for name, value in body.items():
            parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="{name}"\r\n\r\n{value}\r\n'.encode())
        for name, (fname, data) in files.items():
            parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="{name}"; filename="{fname}"\r\n'
                         f"Content-Type: application/octet-stream\r\n\r\n".encode() + data + b"\r\n")
        data = b"".join(parts) + f"--{boundary}--\r\n".encode()
        headers["Content-Type"] = f"multipart/form-data; boundary={boundary}"
    else:
        data = json.dumps(body).encode()
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(API + path, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=600) as r:
            return r.read(), r.headers
    except urllib.error.HTTPError as e:
        sys.exit(f"{path.split('?')[0]}: HTTP {e.code} {e.read()[:500]!r}")


def words(s):
    return re.findall(r"[a-z']+", s.lower().replace("’", "'"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("script")
    ap.add_argument("outdir")
    ap.add_argument("--voice", default="nPczCjzI2devNBz1zQrb", help="default: Brian, a stock narrator voice")
    ap.add_argument("--stability", type=float, default=0.35)
    ap.add_argument("--similarity", type=float, default=0.75)
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--limit", type=int)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()

    os.makedirs(a.outdir, exist_ok=True)
    plan = chunks(convert(open(a.script, encoding="utf-8").read()))
    log_path = os.path.join(a.outdir, "render-log.jsonl")
    done = {}
    if os.path.exists(log_path):
        for line in open(log_path):
            r = json.loads(line)
            done[r["request"]] = r
    print(f"{len(plan)} requests, {sum(len(t) for texts, _ in plan for t in texts)} characters")

    prev = []
    for n, (texts, _) in enumerate(plan, 1):
        pcm_path = os.path.join(a.outdir, f"part{n:02d}.pcm")
        text = "\n\n".join(texts)
        digest = hashlib.sha256(text.encode()).hexdigest()[:16]
        if n in done and os.path.exists(pcm_path):
            if done[n].get("sha") != digest:
                sys.exit(f"request {n} on disk was rendered from different text; use a new OUTDIR")
            if done[n].get("request_id"):
                prev.append(done[n]["request_id"])
            continue
        if a.limit is not None and n > a.limit:
            break
        body = {"text": text, "model_id": "eleven_v4", "language_code": "en", "seed": a.seed,
                "voice_settings": {"stability": a.stability, "similarity_boost": a.similarity}}
        if prev:
            body["previous_request_ids"] = prev[-3:]
        audio, h = post(f"/v1/text-to-speech/{a.voice}?output_format=pcm_{RATE}", body)
        open(pcm_path, "wb").write(audio)
        rec = {"request": n, "sha": digest, "chars": len(text), "request_id": h.get("request-id"),
               "character_cost": h.get("character-cost"), "seconds": round(len(audio) / 2 / RATE, 1)}
        open(log_path, "a").write(json.dumps(rec) + "\n")
        print(json.dumps(rec), flush=True)
        if rec["request_id"]:
            prev.append(rec["request_id"])

    have = [n for n in range(1, len(plan) + 1) if os.path.exists(os.path.join(a.outdir, f"part{n:02d}.pcm"))]
    if a.check:
        for n in have:
            tr_path = os.path.join(a.outdir, f"part{n:02d}.transcript.txt")
            if os.path.exists(tr_path):
                heard = open(tr_path).read()
            else:
                pcm = open(os.path.join(a.outdir, f"part{n:02d}.pcm"), "rb").read()
                wav_path = os.path.join(a.outdir, f"part{n:02d}.wav")
                with wave.open(wav_path, "wb") as w:
                    w.setnchannels(1); w.setsampwidth(2); w.setframerate(RATE); w.writeframes(pcm)
                raw, _ = post("/v1/speech-to-text", {"model_id": "scribe_v1", "language_code": "en",
                                                     "tag_audio_events": "true"},
                              files={"file": (os.path.basename(wav_path), open(wav_path, "rb").read())})
                heard = json.loads(raw).get("text", "")
                open(tr_path, "w").write(heard)
            texts = plan[n - 1][0]
            exp = words(TAG.sub(" ", " ".join(texts)))
            tag_words = set(words(" ".join(TAG.findall(" ".join(texts))))) - set(exp)
            got = words(heard)
            ratio = difflib.SequenceMatcher(None, exp, got, autojunk=False).ratio()
            print(f"request {n}: {len(exp)} words in the script, {len(got)} heard, match {ratio:.3f}; "
                  f"tag words heard: {sorted(set(got) & tag_words)}; "
                  f"audio events: {re.findall(r'[(][^)]*[)]', heard)[:10]}")

    if len(have) < len(plan):
        print(f"rendered {len(have)} of {len(plan)} requests; rerun without --limit to finish")
        return
    pcm = bytearray(b"\0\0" * int(RATE * 0.5))
    for n, (_, gap) in enumerate(plan, 1):
        pcm += open(os.path.join(a.outdir, f"part{n:02d}.pcm"), "rb").read()
        pcm += b"\0\0" * int(RATE * gap)
    with wave.open(os.path.join(a.outdir, "narration.wav"), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(RATE); w.writeframes(bytes(pcm))
    print(f"narration.wav: {len(pcm) / 2 / RATE / 60:.1f} minutes")
    try:
        import lameenc
    except ImportError:
        print("lameenc not installed (pip install lameenc); skipped the MP3")
        return
    enc = lameenc.Encoder()
    enc.set_bit_rate(128); enc.set_in_sample_rate(RATE); enc.set_channels(1); enc.set_quality(2)
    open(os.path.join(a.outdir, "narration.mp3"), "wb").write(enc.encode(bytes(pcm)) + enc.flush())
    print("narration.mp3 written")


if __name__ == "__main__":
    main()
