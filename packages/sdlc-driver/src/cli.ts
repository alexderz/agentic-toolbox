#!/usr/bin/env node
// sdlc-driver check BUNDLE_DIR [--at COMMIT]
// sdlc-driver validate RESULT --flow F --node N
// Errors go to stdout, one per line; exit 0 when clean, 1 on any error,
// 2 on a usage error.

import { readFileSync } from "node:fs";
import { dirname, relative, resolve } from "node:path";
import { checkBundle } from "./check.ts";
import { readFlow, type FlowNode } from "./flow.ts";
import { formatIssue, type Issue } from "./issue.ts";
import { validateResult } from "./result.ts";

const USAGE = "usage: sdlc-driver check BUNDLE_DIR [--at COMMIT]\n       sdlc-driver validate RESULT --flow F --node N [--ticket TICKET] [--authored worker|driver]\n";

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
  const { positional, opts } = options(args, ["flow", "node", "ticket", "authored", "for-node"]);
  if (positional.length !== 1 || opts.flow === undefined || opts.node === undefined) throw new Usage("validate takes RESULT --flow F --node N");
  if (opts.authored !== undefined && opts.authored !== "worker" && opts.authored !== "driver") throw new Usage("authored must be worker or driver");
  const flowFile = opts.flow;
  const read = readFlow(readFileSync(flowFile), flowFile);
  if (!read.flow) return read.issues;
  const isManager = opts.node === "manager" && !read.flow.nodes.some((n) => n.id === "manager");
  let node: FlowNode | undefined = read.flow.nodes.find((n) => n.id === opts.node);
  if (isManager) {
    const stopped = read.flow.nodes.find((n) => n.id === opts["for-node"]);
    if (!stopped) throw new Usage("manager validation requires --for-node with the stopped flow node");
    // The manager is a driver-fixed invocation, never a graph edge. A gate
    // permits escalation only; it cannot be accepted by a manager decision.
    node = { id: "manager", label: "Manager", step: stopped.step, kind: "model",
      scope: "chunk", persona: "manager", exits: [
        ...(stopped.kind === "gate" ? [] : [
          { name: "resume", statuses: ["pass"] as const, to: "@repeat", checks: ["source"] },
          { name: "defer", statuses: ["pass"] as const, to: "@stop", checks: ["source"] },
        ]).map((e) => ({ ...e, statuses: [...e.statuses] })),
        { name: "escalate", statuses: ["needs_input"], to: "@stop" },
      ] };
  } else if (opts["for-node"] !== undefined) throw new Usage("--for-node is only valid for the fixed manager invocation");
  if (!node) throw new Usage(`${flowFile} has no node ${opts.node}`);
  // RUN_ROOT/<label>/run-N/result.json
  const file = positional[0]!;
  const folder = dirname(resolve(file));
  const runRoot = dirname(dirname(folder));
  const kind = node.kind === "command" ? "command" : node.kind === "land" ? undefined : "model";
  const raw = readFileSync(file);
  const issues = validateResult(raw, {
    step: node.step,
    ...(kind ? { kind } : {}),
    ...(opts.ticket !== undefined ? { ticket: opts.ticket } : {}),
    runRoot,
    runFolder: `${relative(runRoot, folder)}/`,
    exits: node.exits,
    checks: node.checks ?? [],
    driverAuthored: opts.authored === "driver",
  }, file).issues;
  if (isManager && issues.length === 0) {
    const result = JSON.parse(raw.toString("utf8"));
    if (result.status === "pass" && !result.evidence.checks.some((s: string) => /^source: (brief|plan|spec|tracker|gather) \S/.test(s))) {
      issues.push({ file, code: "flow.check-missing", field: "evidence.checks", message: "manager pass requires source: <brief|plan|spec|tracker|gather> <path or run folder>" });
    }
  }
  return issues;
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
