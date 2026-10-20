// Test toolbox: the `ok` fixture bundle copied into a temporary root with
// its own skills home and SOURCES.md, so each test can break one rule.

import { cpSync, mkdirSync, mkdtempSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { tmpdir } from "node:os";
import { spawnSync } from "node:child_process";
import { checkBundle } from "../src/check.ts";

export const OK = join(import.meta.dirname, "fixtures/bundles/ok");
export const CLI = join(import.meta.dirname, "../src/cli.ts");

export function toolbox(): { root: string; dir: string } {
  const root = mkdtempSync(join(tmpdir(), "sdlc-toolbox-"));
  const dir = join(root, "bundles/ok");
  cpSync(OK, dir, { recursive: true });
  for (const id of ["tdd", "yagni", "unlisted"]) {
    mkdirSync(join(root, "skills", id), { recursive: true });
    writeFileSync(join(root, "skills", id, "SKILL.md"), `---\nname: ${id}\n---\n`);
  }
  writeFileSync(join(root, "SOURCES.md"), "| Skill | Upstream |\n| --- | --- |\n| tdd | x |\n| yagni | x |\n");
  return { root, dir };
}

type Json = Record<string, any>;

export function editFlow(dir: string, f: (flow: Json) => void): void {
  const flow = JSON.parse(readFileSync(join(dir, "flow.json"), "utf8"));
  f(flow);
  writeFileSync(join(dir, "flow.json"), JSON.stringify(flow, null, 2));
}

export function node(flow: Json, id: string): Json {
  return flow.nodes.find((n: Json) => n.id === id);
}

export function exit(flow: Json, id: string, name: string): Json {
  return node(flow, id).exits.find((e: Json) => e.name === name);
}

export function editFile(dir: string, rel: string, f: (text: string) => string): void {
  writeFileSync(join(dir, rel), f(readFileSync(join(dir, rel), "utf8")));
}

export function codes(dir: string, opts = {}): string[] {
  return [...new Set(checkBundle(dir, opts).map((i) => i.code))].sort();
}

export function run(args: string[], cwd?: string): { status: number | null; out: string; err: string } {
  const r = spawnSync(process.execPath, [CLI, ...args], { cwd });
  return { status: r.status, out: r.stdout.toString("utf8"), err: r.stderr.toString("utf8") };
}
