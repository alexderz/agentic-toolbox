// Stage result v1 (docs/sdlc/stage-result.md) and the candidate rules
// (docs/sdlc/flow-spec.md). validateResult reads a `result.json`;
// validateCandidate reads a worker's `candidate.json`, fills the fixed
// fields the worker omitted, and applies the run-folder rules.

import { lstatSync, readdirSync, readFileSync } from "node:fs";
import { join } from "node:path";
import { git } from "./git.ts";
import type { Issue } from "./issue.ts";
import { isInteger, isObject, readStrictJson, type JsonObject, type JsonValue } from "./json.ts";

export const STEPS = [
  "Entry", "Brief", "Repo", "Plan", "Trial", "Spec", "Groom", "Build",
  "Review", "Trunk", "Changelog", "Monthly",
] as const;
export const STATUSES = ["pass", "fail", "blocked", "needs_input"] as const;
export const NAME_RE = /^[a-z][a-z0-9-]{0,31}$/;
const TICKET_RE = /^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$/;
const SEGMENT_RE = /^[A-Za-z0-9._-]+$/;
const TOP_KEYS = ["schemaVersion", "step", "status", "choice", "ticket", "artifact", "evidence", "findings"];
const EVIDENCE_KEYS = ["kind", "command", "exit_code", "checks", "blocker", "question"];
const ENV_CAP = "env-capability: ";

export type Status = (typeof STATUSES)[number];
export type Reserved = "stop" | "operator";

export interface StageResult {
  schemaVersion: 1;
  step: string;
  status: Status;
  choice: string;
  ticket: string;
  artifact: string;
  evidence: JsonObject;
  findings: string;
}

export interface Exit {
  name: string;
  statuses: string[];
  checks?: string[];
}

export interface Invocation {
  step?: string;
  ticket?: string;
  kind?: "model" | "command";
  /** Absolute run root; enables the artifact existence check. */
  runRoot?: string;
  /** Run-root-relative run folder, ending `/`. */
  runFolder?: string;
  /** With a flow: the stage's exits. Reserved exits are added from `reserved`. */
  exits?: Exit[];
  /** Reserved exits offered; default both. */
  reserved?: Reserved[];
  /** Driver-authored results may also take a reserved exit with `fail`. */
  driverAuthored?: boolean;
  /** The node's required checks. */
  checks?: string[];
}

export interface CandidateInvocation extends Invocation {
  /** Absolute path of the stage's run folder. */
  runFolderAbs: string;
  /** The node's `outputs`, repo-relative; `{design}` expands to designDir. */
  outputs?: string[];
  designDir?: string;
  /** Builder pass or fail: this worktree must have no uncommitted change. */
  worktree?: string;
  /** This stage is a builder run (candidate rule 7). */
  builder?: boolean;
  /** This stage is a verifier run (candidate rule 8). */
  verifier?: boolean;
  /** This stage is the envSpec node (candidate rule 9). */
  envSpec?: boolean;
}

export interface Validation {
  result?: StageResult;
  issues: Issue[];
}

const RESERVED: Record<Reserved, { worker: Status[]; driver: Status[] }> = {
  stop: { worker: ["blocked", "needs_input"], driver: ["fail"] },
  operator: { worker: ["needs_input"], driver: ["fail"] },
};

export function validateResult(input: string | Uint8Array, inv: Invocation, file = "result.json"): Validation {
  return read(input, inv, file, false);
}

export function validateCandidate(input: string | Uint8Array, inv: CandidateInvocation, file = "candidate.json"): Validation {
  const v = read(input, inv, file, true);
  if (!v.result) return v;
  const issues = v.issues;
  const add = (code: string, field: string, message: string) => issues.push({ file, field, code, message });
  const r = v.result;
  const dir = inv.runFolderAbs;
  if (r.status === "pass") {
    for (const p of inv.outputs ?? []) {
      const rel = p.replace(/^\{design\}(?=\/)/, inv.designDir ?? "{design}");
      if (!lstatSync(join(dir, "out", rel), { throwIfNoEntry: false })?.isFile()) {
        add("flow.output-missing", "outputs", `out/${rel} is not a regular file`);
      }
    }
    const link = findSymlink(join(dir, "out"), "out");
    if (link) add("flow.output-symlink", "outputs", `${link} is a symbolic link`);
  }
  if (inv.builder === true && (r.status === "pass" || r.status === "fail")) {
    if (inv.worktree === undefined) add("flow.uncommitted", "worktree", "no worktree to check");
    else {
      const st = git(inv.worktree, ["status", "--porcelain", "--untracked-files=all", "-z"]);
      if (!st.ok || st.stdout.length > 0) add("flow.uncommitted", "worktree", "the worktree has an uncommitted change");
    }
  }
  if (inv.verifier === true) ledgerRules(dir, r.status, add);
  if (inv.envSpec === true && r.status === "pass") envRules(dir, inv, add);
  const state = lstatSync(join(dir, "state.md"), { throwIfNoEntry: false });
  if (!state?.isFile()) add("flow.state-size", "state.md", "state.md is missing");
  else {
    const s = readFileSync(join(dir, "state.md"), "utf8");
    const lines = s.split("\n").length - (s.endsWith("\n") ? 1 : 0);
    if (lines > 60 || s.length > 6000) add("flow.state-size", "state.md", `${lines} lines, ${s.length} characters; limit 60 and 6000`);
  }
  return v;
}

function findSymlink(abs: string, rel: string): string | undefined {
  const st = lstatSync(abs, { throwIfNoEntry: false });
  if (!st) return undefined;
  if (st.isSymbolicLink()) return rel;
  if (!st.isDirectory()) return undefined;
  for (const name of readdirSync(abs).sort()) {
    const hit = findSymlink(join(abs, name), `${rel}/${name}`);
    if (hit) return hit;
  }
  return undefined;
}

function read(input: string | Uint8Array, inv: Invocation, file: string, candidate: boolean): Validation {
  const issues: Issue[] = [];
  const add = (code: string, field: string, message: string) => issues.push({ file, field, code, message });
  const parsed = readStrictJson(input);
  if (!parsed.ok) {
    const code = parsed.error.kind === "syntax" ? "result.not-object" : `result.${parsed.error.kind}`;
    add(code, "-", parsed.error.message);
    return { issues };
  }
  const o = parsed.value;
  if (!isObject(o)) {
    add("result.not-object", "-", "not one JSON object");
    return { issues };
  }
  for (const k of Object.keys(o)) if (!TOP_KEYS.includes(k)) add("result.unknown-key", k, "unknown key");
  const ev = o.evidence;
  if (isObject(ev)) for (const k of Object.keys(ev)) if (!EVIDENCE_KEYS.includes(k)) add("result.unknown-key", `evidence.${k}`, "unknown key");

  // Fixed fields: a candidate may omit them; a present value must match.
  const fixed: [string, JsonValue | undefined, string][] = [
    ["schemaVersion", o.schemaVersion, "result.schema-version"],
    ["step", o.step, "result.step"],
    ["ticket", o.ticket, "result.ticket-mismatch"],
    ["evidence.kind", isObject(ev) ? ev.kind : undefined, "result.evidence-kind"],
  ];
  const want: Record<string, JsonValue | undefined> = { schemaVersion: 1, step: inv.step, ticket: inv.ticket, "evidence.kind": inv.kind };
  for (const [field, got, code] of fixed) {
    const w = want[field];
    if (got === undefined) {
      if (candidate && w !== undefined) {
        if (field === "evidence.kind") (ev as JsonObject).kind = w;
        else o[field] = w;
      }
      continue;
    }
    const wellFormed = field === "schemaVersion" ? isInteger(got) : field !== "ticket" || (typeof got === "string" && TICKET_RE.test(got));
    if (w !== undefined && got !== w && wellFormed) {
      add(candidate ? "flow.fixed-field" : code, field, `${JSON.stringify(got)} differs from the invocation's ${JSON.stringify(w)}`);
    }
  }

  if (o.schemaVersion !== 1) {
    if (!issues.some((i) => i.field === "schemaVersion")) add("result.schema-version", "schemaVersion", "must be the integer 1");
  }
  if (typeof o.step !== "string" || !(STEPS as readonly string[]).includes(o.step)) {
    if (!issues.some((i) => i.field === "step")) add("result.step", "step", "not a step name");
  }
  const status = o.status;
  const statusOk = typeof status === "string" && (STATUSES as readonly string[]).includes(status);
  if (!statusOk) add("result.status", "status", "not one of pass, fail, blocked, needs_input");
  if (typeof o.choice !== "string" || !NAME_RE.test(o.choice)) add("result.choice-pattern", "choice", "does not match ^[a-z][a-z0-9-]{0,31}$");
  if (typeof o.ticket !== "string" || !TICKET_RE.test(o.ticket)) add("result.ticket-pattern", "ticket", "not a tracker id");
  else if (inv.ticket !== undefined && o.ticket !== inv.ticket && !issues.some((i) => i.field === "ticket")) {
    add(candidate ? "flow.fixed-field" : "result.ticket-mismatch", "ticket", `differs from the invocation's ${inv.ticket}`);
  }
  artifactRules(o.artifact, inv, add);
  if (typeof o.findings !== "string") add("result.findings-empty", "findings", "must be a string");
  else if ((status === "fail" || status === "blocked") && o.findings === "") add("result.findings-empty", "findings", `required when status is ${status}`);

  if (!isObject(ev)) add("result.evidence-missing", "evidence", "must be an object");
  else if (ev.kind !== "model" && ev.kind !== "command") {
    if (!issues.some((i) => i.field === "evidence.kind")) add("result.evidence-kind", "evidence.kind", "must be command or model");
  } else if (statusOk) evidenceRules(ev, status as Status, o.choice, add);

  if (issues.length > 0) return { issues };
  const result = o as unknown as StageResult;
  flowRules(result, inv, candidate, add);
  return issues.length > 0 ? { issues } : { result, issues };
}

type Add = (code: string, field: string, message: string) => void;

function artifactRules(a: JsonValue | undefined, inv: Invocation, add: Add): void {
  if (typeof a !== "string" || a === "" || a.startsWith("/") || a.includes("\\")) {
    add("result.artifact-path", "artifact", "not a run-root-relative path");
    return;
  }
  const segs = (a.endsWith("/") ? a.slice(0, -1) : a).split("/");
  if (segs.some((s) => s === "." || s === ".." || !SEGMENT_RE.test(s))) {
    add("result.artifact-path", "artifact", "a segment is empty, `.`, `..`, or has a character outside [A-Za-z0-9._-]");
    return;
  }
  if (inv.runFolder !== undefined && !a.startsWith(inv.runFolder)) {
    add("result.artifact-outside-run", "artifact", `not in the stage's run folder ${inv.runFolder}`);
    return;
  }
  if (inv.runRoot === undefined) return;
  let path = inv.runRoot;
  for (const [n, s] of segs.entries()) {
    path = join(path, s);
    const st = lstatSync(path, { throwIfNoEntry: false });
    const last = n === segs.length - 1;
    const ok = st && !st.isSymbolicLink() && (!last ? st.isDirectory() : a.endsWith("/") ? st.isDirectory() : st.isFile());
    if (!ok) {
      add("result.artifact-missing", "artifact", `${a} does not exist as a ${a.endsWith("/") ? "folder" : "regular file"}`);
      return;
    }
  }
}

function evidenceRules(ev: JsonObject, status: Status, choice: JsonValue | undefined, add: Add): void {
  const kind = ev.kind as "model" | "command";
  const required = new Set<string>(["kind"]);
  if (kind === "command") required.add("command").add("exit_code");
  if (kind === "model" && status === "pass") required.add("checks");
  if (status === "blocked") required.add("blocker");
  if (status === "needs_input") required.add("question");
  const lines = (v: JsonValue | undefined) =>
    Array.isArray(v) && v.length > 0 && v.every((s) => typeof s === "string" && s !== "" && !s.includes("\n"));
  const capOnly = kind === "model" && lines(ev.checks) && (ev.checks as string[]).every((s) => s.startsWith(ENV_CAP));
  // Candidate rule 10 puts env-capability checks on needs_input.
  if (status === "needs_input" && capOnly) required.add("checks");
  for (const k of EVIDENCE_KEYS) {
    if (!required.has(k)) {
      if (ev[k] !== undefined) add("result.evidence-extra", `evidence.${k}`, `not allowed for kind ${kind} and status ${status}`);
      continue;
    }
    const v = ev[k];
    const valid = k === "kind" ? true : k === "exit_code" ? isInteger(v) : k === "checks" ? lines(v) : typeof v === "string" && v !== "";
    if (!valid) add("result.evidence-missing", `evidence.${k}`, "missing or invalid");
  }
  if (kind === "command" && isInteger(ev.exit_code)) {
    const want = ev.exit_code === 0 ? "pass" : "fail";
    if (status !== want) add("result.command-disagreement", "status", `exit_code ${ev.exit_code} needs status ${want}`);
  }
  if (Array.isArray(ev.checks) && ev.checks.some((s) => typeof s === "string" && s.startsWith(ENV_CAP))) {
    if (status !== "needs_input" || choice !== "operator") {
      add("flow.env-capability", "evidence.checks", "env-capability needs status needs_input and choice operator");
    }
  }
}

function flowRules(r: StageResult, inv: Invocation, candidate: boolean, add: Add): void {
  if (inv.exits !== undefined) {
    const reserved = inv.reserved ?? ["stop", "operator"];
    const exit = inv.exits.find((e) => e.name === r.choice);
    if (exit) {
      if (!exit.statuses.includes(r.status)) add("flow.choice-not-allowed", "choice", `exit ${r.choice} does not allow status ${r.status}`);
    } else if ((reserved as string[]).includes(r.choice)) {
      const rule = RESERVED[r.choice as Reserved];
      const driver = !candidate && inv.driverAuthored === true;
      if (rule.worker.includes(r.status) || (driver && rule.driver.includes(r.status))) {
        // allowed
      } else if (r.status === "fail" && rule.driver.includes("fail")) {
        add("flow.reserved-status", "choice", `a worker may not take ${r.choice} with fail`);
      } else add("flow.choice-not-allowed", "choice", `${r.choice} does not allow status ${r.status}`);
    } else add("flow.choice-not-allowed", "choice", `${r.choice} is not an exit of this stage`);
  }
  if (r.status !== "pass") return;
  const entries = (r.evidence.checks as string[] | undefined) ?? [];
  const finding = (name: string, allowNa: boolean) =>
    entries.some((e) => {
      if (!e.startsWith(`${name}: `)) return false;
      const rest = e.slice(name.length + 2).trim();
      if (rest === "") return false;
      return allowNa || !/^n\/a\b/.test(rest);
    });
  for (const name of inv.checks ?? []) {
    if (!finding(name, true)) add("flow.check-missing", "evidence.checks", `no finding for node check ${name}`);
  }
  const exit = inv.exits?.find((e) => e.name === r.choice);
  for (const name of exit?.checks ?? []) {
    if (!finding(name, false)) add("flow.check-missing", "evidence.checks", `no finding for exit check ${name}`);
  }
}

const CRIT = ["breaking", "critical", "major", "minor", "nit"];
const CMD_MAX = 1000;

function ledgerRules(dir: string, status: Status, add: Add): void {
  const path = join(dir, "ledger.json");
  const st = lstatSync(path, { throwIfNoEntry: false });
  if (!st?.isFile() || st.isSymbolicLink()) {
    add("flow.ledger", "ledger.json", "ledger.json is missing");
    return;
  }
  const parsed = readStrictJson(readFileSync(path));
  if (!parsed.ok || !Array.isArray(parsed.value)) {
    add("flow.ledger", "ledger.json", "ledger.json must be one JSON array");
    return;
  }
  const ids = new Set<string>();
  for (const [n, row] of parsed.value.entries()) {
    const bad = (m: string) => add("flow.ledger", `ledger.json[${n}]`, m);
    if (!isObject(row)) {
      bad("must be an object");
      continue;
    }
    const keys = ["id", "criticality", "status", "summary", "raised", "fixed"];
    for (const k of Object.keys(row)) if (!keys.includes(k)) bad(`unknown key ${k}`);
    for (const k of keys) if (row[k] === undefined) bad(`missing ${k}`);
    if (typeof row.id !== "string" || !/^V[1-9][0-9]*$/.test(row.id) || ids.has(row.id)) bad("id must be a unique V<n>");
    else ids.add(row.id);
    if (typeof row.criticality !== "string" || !CRIT.includes(row.criticality)) bad("criticality is not breaking, critical, major, minor, or nit");
    if (row.status !== "open" && row.status !== "fixed") bad("status must be open or fixed");
    if (typeof row.summary !== "string" || row.summary === "" || row.summary.length > 200 || row.summary.includes("\n")) bad("summary must be one line of at most 200 characters");
    if (typeof row.raised !== "string" || row.raised === "" || row.raised.includes("\n")) bad("raised must be one non-empty line");
    if (typeof row.fixed !== "string" || row.fixed.includes("\n") || (row.status === "fixed" && row.fixed === "")) bad("fixed must name a run when status is fixed");
    if (status === "pass" && row.status === "open" && row.criticality !== "nit") bad("a verifier pass has no open entry above nit");
  }
}

function envRules(dir: string, inv: CandidateInvocation, add: Add): void {
  const rel = (inv.outputs ?? [])
    .map((p) => p.replace(/^\{design\}(?=\/)/, inv.designDir ?? "{design}"))
    .find((p) => p.endsWith("/lld.md"));
  if (rel === undefined) {
    add("flow.env-block", "outputs", "envSpec needs an lld.md output");
    return;
  }
  const path = join(dir, "out", rel);
  const st = lstatSync(path, { throwIfNoEntry: false });
  if (!st?.isFile() || st.isSymbolicLink()) {
    add("flow.env-block", "outputs", `out/${rel} is not a regular file`);
    return;
  }
  const why = envSectionError(readFileSync(path, "utf8"));
  if (why) add("flow.env-block", "outputs", why);
}

/** Why `markdown` has no single valid env block, or undefined when it does. */
export function envSectionError(markdown: string): string | undefined {
  const sections: string[] = [];
  let cur: string[] | undefined;
  for (const line of markdown.split("\n")) {
    if (line.trim() === "## Build environment") {
      sections.push("");
      cur = [];
      continue;
    }
    if (cur !== undefined && /^#{1,2} /.test(line)) cur = undefined;
    if (cur !== undefined) {
      cur.push(line);
      sections[sections.length - 1] = cur.join("\n");
    }
  }
  if (sections.length !== 1) return "needs exactly one ## Build environment section";
  const blocks: string[] = [];
  const lines = (sections[0] ?? "").split("\n");
  for (let i = 0; i < lines.length; i++) {
    const open = /^```(.*)$/.exec(lines[i] ?? "");
    if (!open) continue;
    const info = open[1]!.trim();
    const buf: string[] = [];
    for (i++; i < lines.length && lines[i] !== "```"; i++) buf.push(lines[i] ?? "");
    if (i >= lines.length) return "an unclosed fence in ## Build environment";
    if (info !== "json sdlc-env") return "the section holds a fence that is not json sdlc-env";
    blocks.push(buf.join("\n"));
  }
  if (blocks.length !== 1) return "the section must hold exactly one json sdlc-env block";
  return envBlockError(blocks[0] ?? "");
}

/** Why `text` is not one valid `json sdlc-env` object, or undefined. */
export function envBlockError(text: string): string | undefined {
  const parsed = readStrictJson(text);
  if (!parsed.ok) return parsed.error.message;
  const o = parsed.value;
  if (!isObject(o)) return "the env block must be one JSON object";
  const keys = ["schemaVersion", "toolchain", "deps", "passEnv", "prove", "test"];
  for (const k of Object.keys(o)) if (!keys.includes(k)) return `unknown key ${k}`;
  if (o.schemaVersion !== 1) return "schemaVersion must be the integer 1";
  if (!commandList(o.toolchain, true)) return "toolchain must be an array of command lines";
  if (!Array.isArray(o.deps)) return "deps must be an array";
  const names = new Set<string>();
  for (const d of o.deps) {
    if (!isObject(d)) return "each dep must be an object";
    for (const k of Object.keys(d)) if (!["name", "setup", "start", "ready", "reset", "stop"].includes(k)) return `dep unknown key ${k}`;
    if (typeof d.name !== "string" || !NAME_RE.test(d.name) || names.has(d.name)) return "dep name must be a unique id";
    names.add(d.name);
    for (const k of ["setup", "start", "ready", "reset", "stop"]) {
      if (!commandList(d[k], true)) return `dep ${d.name} ${k} must be an array of command lines`;
    }
    if (Array.isArray(d.start) && d.start.length > 0 && Array.isArray(d.ready) && d.ready.length === 0) {
      return `dep ${d.name} ready is empty while start is not`;
    }
  }
  if (!Array.isArray(o.passEnv) || !o.passEnv.every((n) => typeof n === "string" && /^[A-Z][A-Z0-9_]{0,63}$/.test(n))) {
    return "passEnv must be an array of variable names";
  }
  if (!commandList(o.prove, false)) return "prove must be a non-empty array of command lines";
  if (typeof o.test !== "string" || !commandLine(o.test)) return "test must be one command line";
  return undefined;
}

function commandList(v: JsonValue | undefined, emptyOk: boolean): boolean {
  return Array.isArray(v) && (emptyOk || v.length > 0) && v.every((s) => typeof s === "string" && commandLine(s));
}

function commandLine(s: string): boolean {
  return s !== "" && s.length <= CMD_MAX && !s.includes("\n");
}
