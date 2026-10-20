// flow.json types and the field tables (docs/sdlc/flow-spec.md). readFlow
// returns no flow when the strict reader or a field rule fails (B1), so
// the graph rules in check.ts run only on a well-typed flow.

import type { Issue } from "./issue.ts";
import { isInteger, isObject, readStrictJson, type JsonObject, type JsonValue } from "./json.ts";
import { NAME_RE, STATUSES, STEPS, type Status } from "./result.ts";

export type Kind = "model" | "command" | "gate" | "land";
export type Scope = "chunk" | "item";

export interface Extract {
  from: string;
  heading: string;
  to: string;
}

export interface FlowExit {
  name: string;
  statuses: Status[];
  to: string;
  say?: string;
  checks?: string[];
  extract?: Extract;
}

export interface FlowNode {
  id: string;
  label: string;
  step: string;
  kind: Kind;
  scope: Scope;
  persona?: string;
  envSpec?: true;
  skills?: string[];
  outputs?: string[];
  outputDirs?: string[];
  checks?: string[];
  commands?: string | string[];
  gate?: string;
  ask?: string;
  builder?: string;
  prove?: string;
  verify?: string;
  review?: string;
  exits: FlowExit[];
}

export interface Flow {
  schemaVersion: 1;
  id: string;
  entry: string;
  itemEntry?: string;
  defaults: { prove: string[]; commandTimeoutSec: number; workerTimeoutSec: number };
  nodes: FlowNode[];
}

const COMMON = ["id", "label", "step", "kind", "scope", "exits"];
const BY_KIND: Record<Kind, string[]> = {
  model: ["persona", "envSpec", "skills", "outputs", "outputDirs", "checks"],
  command: ["commands"],
  gate: ["gate", "ask"],
  land: ["builder", "prove", "verify", "review"],
};
const REQUIRED: Record<Kind, string[]> = {
  model: ["persona"],
  command: ["commands"],
  gate: ["gate", "ask"],
  land: ["builder", "prove", "verify", "review"],
};
const CHUNK_ONLY = ["envSpec", "outputs", "outputDirs"];
const GATE_TAG = /^[a-z][a-z0-9-]{0,15}$/;
const LABEL = /^[A-Z][A-Za-z]{0,11}$/;
const EXTRACT_TO = /^[a-z0-9-]{1,40}\.md$/;

/** A normalized repo-relative path; `{design}` may be the first segment. */
export function repoPath(p: string, dir: boolean): boolean {
  if (p === "" || p.startsWith("/") || p.includes("\\") || p.endsWith("/") !== dir) return false;
  const segs = (dir ? p.slice(0, -1) : p).split("/");
  return segs.every((s, n) => (s === "{design}" && n === 0 && segs.length > 1) || (/^[A-Za-z0-9._-]+$/.test(s) && s !== "." && s !== ".."));
}

export function readFlow(input: string | Uint8Array, file: string): { flow?: Flow; issues: Issue[] } {
  const issues: Issue[] = [];
  const parsed = readStrictJson(input);
  if (!parsed.ok) return { issues: [{ file, field: "-", code: "flow.json", message: parsed.error.message }] };
  const o = parsed.value;
  let fatal = false;
  const field = (f: string, message: string, code = "flow.field") => {
    issues.push({ file, field: f, code, message });
    if (code === "flow.field") fatal = true;
  };
  const at = (node: string, exit: string | undefined, message: string, code = "flow.field") => {
    issues.push(exit === undefined ? { file, node, code, message } : { file, node, exit, code, message });
    if (code === "flow.field") fatal = true;
  };
  if (!isObject(o)) return { issues: [{ file, field: "-", code: "flow.json", message: "not one JSON object" }] };
  unknown(o, ["schemaVersion", "id", "entry", "itemEntry", "defaults", "nodes"], (k) => field(k, "unknown key"));
  if (o.schemaVersion !== 1) field("schemaVersion", "must be the integer 1");
  if (!isName(o.id)) field("id", "must match ^[a-z][a-z0-9-]{0,31}$");
  if (typeof o.entry !== "string") field("entry", "must be a node id");
  if (o.itemEntry !== undefined && typeof o.itemEntry !== "string") field("itemEntry", "must be a node id");
  const defaults = { prove: [] as string[], commandTimeoutSec: 1800, workerTimeoutSec: 7200 };
  if (o.defaults !== undefined) {
    const d = o.defaults;
    if (!isObject(d)) field("defaults", "must be an object");
    else {
      unknown(d, ["prove", "commandTimeoutSec", "workerTimeoutSec"], (k) => field(`defaults.${k}`, "unknown key"));
      if (d.prove !== undefined) {
        if (!strings(d.prove, true)) field("defaults.prove", "must be an array of command lines");
        else defaults.prove = d.prove as string[];
      }
      for (const k of ["commandTimeoutSec", "workerTimeoutSec"] as const) {
        if (d[k] === undefined) continue;
        if (!isInteger(d[k]) || (d[k] as number) <= 0) field(`defaults.${k}`, "must be a positive integer");
        else defaults[k] = d[k] as number;
      }
    }
  }
  if (!Array.isArray(o.nodes) || o.nodes.length === 0) {
    field("nodes", "must be a non-empty array of nodes");
    return { issues };
  }
  for (const [n, raw] of o.nodes.entries()) {
    if (!isObject(raw)) {
      field(`nodes[${n}]`, "must be an object");
      continue;
    }
    const id = isName(raw.id) ? (raw.id as string) : `nodes[${n}]`;
    const bad = (k: string, message: string) => at(id, undefined, `${k}: ${message}`);
    if (!isName(raw.id)) bad("id", "must match ^[a-z][a-z0-9-]{0,31}$");
    if (typeof raw.label !== "string" || !LABEL.test(raw.label)) bad("label", "must match ^[A-Z][A-Za-z]{0,11}$");
    if (typeof raw.step !== "string" || !(STEPS as readonly string[]).includes(raw.step)) bad("step", "not a step name");
    if (raw.scope !== "chunk" && raw.scope !== "item") bad("scope", "must be chunk or item");
    const kind = raw.kind;
    if (kind !== "model" && kind !== "command" && kind !== "gate" && kind !== "land") {
      bad("kind", "must be model, command, gate, or land");
      continue;
    }
    unknown(raw, [...COMMON, ...BY_KIND[kind]], (k) => bad(k, `not a field of a ${kind} node`));
    for (const k of REQUIRED[kind]) if (raw[k] === undefined) bad(k, `required on a ${kind} node`);
    if (raw.scope === "item") for (const k of CHUNK_ONLY) if (raw[k] !== undefined) bad(k, "only on chunk nodes");
    if (raw.persona !== undefined && !isName(raw.persona)) bad("persona", "must be a persona id");
    if (raw.envSpec !== undefined && raw.envSpec !== true) bad("envSpec", "must be true when present");
    if (raw.skills !== undefined && !strings(raw.skills, true)) bad("skills", "must be an array of skill ids");
    if (raw.checks !== undefined && !names(raw.checks)) bad("checks", "must be an array of check names");
    for (const [k, dir] of [["outputs", false], ["outputDirs", true]] as const) {
      const v = raw[k];
      if (v === undefined) continue;
      if (!strings(v, true)) bad(k, "must be an array of paths");
      else for (const p of v as string[]) if (!repoPath(p, dir)) at(id, undefined, `${k}: ${JSON.stringify(p)} is not a normalized repo-relative ${dir ? "folder ending /" : "file path"}`, "flow.output-path");
    }
    if (kind === "command" && raw.commands !== undefined) {
      const c = raw.commands;
      const ok = c === "groom" || c === "env" || c === "env-test" || (strings(c, false) && (c as string[]).every((s) => /^scripts\/[A-Za-z0-9._-]+$/.test(s)));
      if (!ok) bad("commands", 'must be "groom", "env", "env-test", or an array of scripts/<file> paths');
      else if ((c === "env" || c === "env-test") && raw.scope !== "chunk") bad("commands", `${c} only on chunk nodes`);
    }
    if (kind === "gate" && raw.gate !== undefined && (typeof raw.gate !== "string" || !GATE_TAG.test(raw.gate))) bad("gate", "must match ^[a-z][a-z0-9-]{0,15}$");
    if (kind === "gate" && raw.ask !== undefined && (typeof raw.ask !== "string" || raw.ask.trim() === "")) bad("ask", "must be non-empty text");
    if (kind === "land") for (const k of BY_KIND.land) if (raw[k] !== undefined && !isName(raw[k])) bad(k, "must be a node id");
    if (!Array.isArray(raw.exits)) {
      bad("exits", "must be an array of exits");
      continue;
    }
    const seen = new Set<string>();
    for (const [e, ex] of raw.exits.entries()) {
      if (!isObject(ex)) {
        bad(`exits[${e}]`, "must be an object");
        continue;
      }
      const name = typeof ex.name === "string" ? ex.name : `exits[${e}]`;
      const ebad = (message: string, code = "flow.field") => at(id, name, message, code);
      unknown(ex, ["name", "statuses", "to", "say", "checks", "extract"], (k) => ebad(`${k}: unknown key`));
      if (ex.name === "stop" || ex.name === "operator") ebad(`${ex.name} is reserved and never listed`, "flow.reserved-listed");
      else if (!isName(ex.name)) ebad("name: must match ^[a-z][a-z0-9-]{0,31}$");
      else if (seen.has(name)) ebad("name: duplicate exit name on this node");
      seen.add(name);
      const st = ex.statuses;
      if (!Array.isArray(st) || st.length === 0 || new Set(st).size !== st.length || !st.every((s) => (STATUSES as readonly JsonValue[]).includes(s))) {
        ebad("statuses: must be a non-empty set of pass, fail, blocked, needs_input");
      }
      if (typeof ex.to !== "string") ebad("to: must be a node id, @items, or @done");
      if (ex.say !== undefined && (typeof ex.say !== "string" || ex.say.includes("\n"))) ebad("say: must be one line");
      if (ex.checks !== undefined && !names(ex.checks)) ebad("checks: must be an array of check names");
      if (ex.extract !== undefined) extractRules(ex.extract, kind, (m) => ebad(m, "flow.extract"));
    }
  }
  return fatal ? { issues } : { flow: o as unknown as Flow, issues };
}

function extractRules(x: JsonValue, kind: Kind, bad: (m: string) => void): void {
  if (kind !== "gate") bad("extract only on gate exits");
  if (!isObject(x)) return bad("extract must be an object with from, heading, to");
  unknown(x, ["from", "heading", "to"], (k) => bad(`extract.${k}: unknown key`));
  if (typeof x.from !== "string" || !repoPath(x.from, false)) bad("extract.from: not a normalized repo-relative path");
  if (typeof x.heading !== "string" || x.heading.trim() === "" || x.heading.includes("\n")) bad("extract.heading: must be one line of heading text");
  if (typeof x.to !== "string" || !EXTRACT_TO.test(x.to)) bad("extract.to: must match ^[a-z0-9-]{1,40}\\.md$");
}

function unknown(o: JsonObject, allowed: string[], report: (k: string) => void): void {
  for (const k of Object.keys(o)) if (!allowed.includes(k)) report(k);
}

function isName(v: JsonValue | undefined): boolean {
  return typeof v === "string" && NAME_RE.test(v);
}

function strings(v: JsonValue | undefined, emptyOk: boolean): boolean {
  return Array.isArray(v) && (emptyOk || v.length > 0) && v.every((s) => typeof s === "string" && s !== "");
}

function names(v: JsonValue | undefined): boolean {
  return Array.isArray(v) && v.every(isName);
}
