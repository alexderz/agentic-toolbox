// Driver git calls: hooks, fsmonitor, and replace objects off; no system
// or global config; no GIT_* variable from the caller's environment.

import { spawnSync } from "node:child_process";

const FLAGS = [
  "--no-pager",
  "-c", "core.fsmonitor=",
  "-c", "core.hooksPath=/dev/null",
  "-c", "core.commitGraph=false",
  "-c", "core.multiPackIndex=false",
  "-c", "gc.auto=0",
  "-c", "maintenance.auto=false",
  "-c", "protocol.ext.allow=never",
  "-c", "protocol.file.allow=never",
];

export function gitEnv(): Record<string, string | undefined> {
  const env: Record<string, string | undefined> = {};
  for (const [k, v] of Object.entries(process.env)) if (!k.startsWith("GIT_")) env[k] = v;
  return { ...env, GIT_CONFIG_NOSYSTEM: "1", GIT_CONFIG_GLOBAL: "/dev/null", GIT_NO_REPLACE_OBJECTS: "1", GIT_ALLOW_PROTOCOL: "https:ssh" };
}

export interface GitResult {
  ok: boolean;
  stdout: Buffer;
  stderr: string;
}

export function git(cwd: string, args: string[], input?: string): GitResult {
  const r = spawnSync("git", [...FLAGS, ...args], { cwd, env: gitEnv(), input, maxBuffer: 256 * 1024 * 1024 });
  return { ok: r.status === 0, stdout: r.stdout ?? Buffer.from(""), stderr: (r.stderr ?? Buffer.from("")).toString("utf8") };
}
