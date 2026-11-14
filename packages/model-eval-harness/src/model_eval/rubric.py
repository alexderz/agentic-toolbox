#!/usr/bin/env python3
"""Grade one generated CLI by RUNNING it. Executes inside the container.

LOC measures verbosity, not quality. This executes each tool against the live
read-only Home Assistant proxy and records what actually works:

  help        --help exits 0 and prints usable help
  reads       a states-like command returns real entity data
  bad_input   a nonexistent entity fails cleanly, non-zero exit, no traceback
  bad_auth    a wrong token is handled, no traceback
  tests       the model's own tests run and pass
  no_crash    nothing raises an unhandled exception

Writes JSON to stdout.
"""
import json, os, re, subprocess, sys, glob

APP = "/app"
HA_URL = os.environ["HA_URL"]
HA_TOKEN = os.environ["HA_TOKEN"]
TIMEOUT = 60

SKIP = ("venv", ".venv", "site-packages", "__pycache__", ".pytest_cache",
        "node_modules", "build", "dist", ".git")


def files():
    out = []
    for p in glob.glob(f"{APP}/**/*", recursive=True):
        if not os.path.isfile(p):
            continue
        if any(s in p.split(os.sep) for s in SKIP):
            continue
        out.append(p)
    return out


def entrypoint():
    """Best guess at the CLI: prefers argparse+main, HA-ish names, bigger files."""
    best, best_score = None, -1
    for p in files():
        if not (p.endswith(".py") or _shebang_py(p)):
            continue
        base = os.path.basename(p).lower()
        if base.startswith(("test_", "conftest", "setup", "mock")) or base.endswith("_test.py"):
            continue
        try:
            src = open(p, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        score = 0
        if "argparse" in src or "click" in src: score += 3
        if re.search(r"def main\b", src): score += 3
        if '__main__' in src: score += 2
        if any(k in base for k in ("ha", "hass", "home")): score += 2
        score += min(len(src) // 2000, 3)
        if score > best_score:
            best, best_score = p, score
    return best


def _shebang_py(p):
    try:
        first = open(p, "rb").readline(200).decode("utf-8", "replace")
        return first.startswith("#!") and "python" in first
    except OSError:
        return False


def run(args, env=None, timeout=TIMEOUT):
    e = dict(os.environ)
    e.update(env or {})
    try:
        r = subprocess.run(args, capture_output=True, text=True, timeout=timeout,
                           env=e, cwd=APP)
        return r.returncode, r.stdout or "", r.stderr or ""
    except subprocess.TimeoutExpired:
        return -9, "", "TIMEOUT"
    except Exception as ex:
        return -1, "", f"{type(ex).__name__}: {ex}"


def traceback_in(s):
    return "Traceback (most recent call last)" in s


def main():
    ep = entrypoint()
    res = {"entrypoint": os.path.relpath(ep, APP) if ep else None,
           "help": False, "reads": False, "bad_input": False,
           "bad_auth": False, "tests": None, "no_crash": True,
           "subcommands": [], "notes": []}
    if not ep:
        res["notes"].append("no runnable entrypoint found")
        print(json.dumps(res)); return

    base = [sys.executable, ep]
    def mkenv(url):
        return {"HA_URL": url, "HA_TOKEN": HA_TOKEN,
                "HOMEASSISTANT_URL": url, "HASS_URL": url,
                "HA_BASE_URL": url, "HASS_TOKEN": HA_TOKEN,
                "HOMEASSISTANT_TOKEN": HA_TOKEN, "HA_SERVER": url}
    # some tools expect the base to already include /api, some append it
    ENVS = [mkenv(HA_URL), mkenv(HA_URL.rstrip("/") + "/api")]
    env = ENVS[0]

    # 1. help
    rc, out, err = run(base + ["--help"], env)
    res["help"] = rc == 0 and len(out) > 80
    if traceback_in(out + err):
        res["no_crash"] = False
    # scrape subcommand names out of the help text
    for m in re.finditer(r"^\s{2,}([a-z][a-z0-9_-]{2,20})\s{2,}\S", out, re.M):
        w = m.group(1)
        if w not in ("options", "usage", "positional", "optional", "commands", "help"):
            res["subcommands"].append(w)
    res["subcommands"] = sorted(set(res["subcommands"]))[:25]

    # 2. reads -- try the model's own subcommand names first, then common ones
    cands = [c for c in res["subcommands"]
             if any(k in c for k in ("state", "entit", "list", "get", "status"))]
    cands += ["states", "state", "list", "entities", "get-states", "list-states", "status"]
    url_flags = [[], ["--url", HA_URL], ["--url", HA_URL, "--token", HA_TOKEN],
                 ["--host", HA_URL], ["--base-url", HA_URL]]
    done = False
    for ev in ENVS:
        for c in dict.fromkeys(cands):
            for uf in url_flags:
                rc, out, err = run(base + [c] + uf, ev, timeout=45)
                if traceback_in(out + err):
                    res["no_crash"] = False
                blob = out + err
                if re.search(r"(light\.|sensor\.|switch\.|binary_sensor\.|scene\.|entity_id)", blob):
                    res["reads"] = True
                    res["read_cmd"] = " ".join([c] + uf)
                    res["read_env"] = ev["HA_URL"]
                    # exiting 0 while printing an error is its own defect
                    res["exit_code_ok"] = rc == 0
                    env = ev
                    done = True
                    break
            if done: break
        if done: break

    # 3. bad input -- nonexistent entity should fail cleanly
    if res.get("read_cmd"):
        c = res["read_cmd"].split()[0]
        rc, out, err = run(base + [c, "light.definitely_not_real_xyz"], env, timeout=45)
        res["bad_input"] = (rc != 0 or "not found" in (out + err).lower()) \
            and not traceback_in(out + err)
        if traceback_in(out + err):
            res["no_crash"] = False

        # 4. bad auth -- wrong token must not produce a traceback
        bad = dict(env)
        for k in list(bad):
            if "TOKEN" in k:
                bad[k] = "totally-wrong-token"
        rc, out, err = run(base + [c], bad, timeout=45)
        res["bad_auth"] = not traceback_in(out + err) and rc != 0
        if traceback_in(out + err):
            res["no_crash"] = False

    # 5. the model's own tests
    testfiles = [p for p in files()
                 if os.path.basename(p).startswith("test_")
                 or os.path.basename(p).endswith("_test.py")
                 or f"{os.sep}tests{os.sep}" in p]
    testfiles = [p for p in testfiles if p.endswith(".py")]
    if testfiles:
        rc, out, err = run([sys.executable, "-m", "pytest", "-q", "--no-header", "-x"] + testfiles, env, timeout=180)
        blob = out + err
        m = re.search(r"(\d+) passed", blob)
        f = re.search(r"(\d+) failed", blob)
        e = re.search(r"(\d+) error", blob)
        res["tests"] = {"files": len(testfiles), "rc": rc,
                        "passed": int(m.group(1)) if m else 0,
                        "failed": int(f.group(1)) if f else 0,
                        "errors": int(e.group(1)) if e else 0}
    print(json.dumps(res))


if __name__ == "__main__":
    main()
