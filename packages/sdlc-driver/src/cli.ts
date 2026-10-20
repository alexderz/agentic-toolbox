#!/usr/bin/env node
// sdlc-driver check BUNDLE_DIR [--at COMMIT]
// sdlc-driver validate RESULT --flow F --node N
// Errors go to stdout, one per line; exit 0 when clean, 1 on any error,
// 2 on a usage error.

import { readFileSync } from "node:fs";
import { dirname, relative, resolve } from "node:path";
import { checkBundle } from "./check.ts";
import { readFlow } from "./flow.ts";
import { formatIssue, type Issue } from "./issue.ts";
import { validateResult } from "./result.ts";

const USAGE = "usage: sdlc-driver check BUNDLE_DIR [--at COMMIT]\n       sdlc-driver validate RESULT --flow F --node N\n";

class Usage extends Error {}

function options(args: string[], names: string[]): { positional: string[]; opts: Record<string, string> } {
  const positional: string[] = [];
  const opts: Record<string, string> = {};
  for (let i = 0; i < args.length; i++) {
    const a = args[i]!;
    if (!a.startsWith("--")) {
      positional.push(a);
      continue;
    }
    const v = args[++i];
    if (!names.includes(a.slice(2)) || v === undefined) throw new Usage(`bad option ${a}`);
    opts[a.slice(2)] = v;
  }
  return { positional, opts };
}

function check(args: string[]): Issue[] {
  const { positional, opts } = options(args, ["at"]);
  if (positional.length !== 1) throw new Usage("check takes one BUNDLE_DIR");
  try {
    return checkBundle(positional[0]!, opts.at === undefined ? {} : { at: opts.at });
  } catch (e) {
    throw new Usage((e as Error).message);
  }
}

function validate(args: string[]): Issue[] {
  const { positional, opts } = options(args, ["flow", "node"]);
  if (positional.length !== 1 || opts.flow === undefined || opts.node === undefined) throw new Usage("validate takes RESULT --flow F --node N");
  const flowFile = opts.flow;
  const read = readFlow(readFileSync(flowFile), flowFile);
  if (!read.flow) return read.issues;
  const node = read.flow.nodes.find((n) => n.id === opts.node);
  if (!node) throw new Usage(`${flowFile} has no node ${opts.node}`);
  // RUN_ROOT/<label>/run-N/result.json
  const file = positional[0]!;
  const folder = dirname(resolve(file));
  const runRoot = dirname(dirname(folder));
  const kind = node.kind === "command" ? "command" : node.kind === "land" ? undefined : "model";
  return validateResult(readFileSync(file), {
    step: node.step,
    ...(kind ? { kind } : {}),
    runRoot,
    runFolder: `${relative(runRoot, folder)}/`,
    exits: node.exits,
    checks: node.checks ?? [],
    driverAuthored: true,
  }, file).issues;
}

function main(argv: string[]): number {
  const [cmd, ...rest] = argv;
  try {
    const issues = cmd === "check" ? check(rest) : cmd === "validate" ? validate(rest) : undefined;
    if (!issues) throw new Usage(cmd === undefined ? "no command" : `unknown command ${cmd}`);
    for (const i of issues) process.stdout.write(`${formatIssue(i)}\n`);
    return issues.length === 0 ? 0 : 1;
  } catch (e) {
    if (!(e instanceof Usage) && !((e as { code?: string }).code === "ENOENT")) throw e;
    process.stderr.write(`sdlc-driver: ${(e as Error).message}\n${USAGE}`);
    return 2;
  }
}

process.exitCode = main(process.argv.slice(2));
