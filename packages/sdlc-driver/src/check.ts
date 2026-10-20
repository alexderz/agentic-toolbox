// Bundle check (docs/sdlc/flow-spec.md, rules B1–B14). checkBundle reads
// a bundle from the working tree, or with `at` from one commit, and
// returns every error; an empty list means clean.

import { basename, join, relative, resolve, sep } from "node:path";
import { fsTree, gitTree, loadBundle, type Bundle } from "./bundle.ts";
import { readFlow, type Flow, type FlowNode } from "./flow.ts";
import { git } from "./git.ts";
import type { Issue } from "./issue.ts";

export interface CheckOptions {
  /** Read the bundle at this commit instead of the working tree. */
  at?: string;
  /** `docs/INTAKE.md` at the reviewed ref, for a bundle commit outside reviewed history. */
  intake?: string;
}

export function checkBundle(bundleDir: string, opts: CheckOptions = {}): Issue[] {
  const abs = resolve(bundleDir);
  const top = git(abs, ["rev-parse", "--show-toplevel"]);
  // The toolbox root holds skills/ and SOURCES.md. Outside git, assume bundles/<id>/.
  const root = top.ok ? top.stdout.toString("utf8").trim() : resolve(abs, "../..");
  if (opts.at !== undefined && !top.ok) throw new Error(`${bundleDir} is not in a git repository; --at needs one`);
  const dir = relative(root, abs).split(sep).join("/");
  const tree = opts.at !== undefined ? gitTree(root, opts.at) : fsTree(root);
  const show = (rel: string) => (rel === "." ? bundleDir : join(bundleDir, rel));
  const { bundle, issues } = loadBundle(tree, dir, basename(abs), show, opts);
  if (!bundle.flowBytes) return issues;
  const file = show("flow.json");
  const read = readFlow(bundle.flowBytes, file);
  issues.push(...read.issues);
  if (read.flow) issues.push(...flowRules(read.flow, bundle, file, show("bundle.md")));
  return issues;
}

const REVIEW_CHECKS = ["intake", "sha-pins", "trust-boundary"];

function flowRules(flow: Flow, bundle: Bundle, file: string, bundleMd: string): Issue[] {
  const issues: Issue[] = [];
  const at = (node: string, exit: string | undefined, code: string, message: string) =>
    issues.push(exit === undefined ? { file, node, code, message } : { file, node, exit, code, message });
  const field = (f: string, code: string, message: string) => issues.push({ file, field: f, code, message });
  const nodes = flow.nodes;
  const byId = new Map<string, FlowNode>();
  for (const n of nodes) {
    if (byId.has(n.id)) at(n.id, undefined, "flow.target", "duplicate node id");
    else byId.set(n.id, n);
  }
  const job = (n: FlowNode | undefined) => (n?.persona ? bundle.personas.get(n.persona)?.job : undefined);
  const isModel = (n: FlowNode | undefined, j: string) => n?.kind === "model" && job(n) === j;

  if (flow.id !== bundle.id) field("id", "flow.field", `${flow.id} differs from the bundle id ${bundle.id}`);
  // A bad entry skips the rules that search from it.
  const entry = byId.get(flow.entry)?.scope === "chunk" ? byId.get(flow.entry) : undefined;
  if (!entry) field("entry", "flow.field", `${flow.entry} is not a chunk node`);
  const items = nodes.filter((n) => n.scope === "item");
  const itemEntry = flow.itemEntry === undefined ? undefined : byId.get(flow.itemEntry);
  if (items.length > 0 && flow.itemEntry === undefined) field("itemEntry", "flow.field", "required when a node has scope item");
  if (flow.itemEntry !== undefined) {
    if (itemEntry?.scope !== "item" || itemEntry.kind !== "model") field("itemEntry", "flow.field", `${flow.itemEntry} is not an item model node`);
    else if (bundle.personas.has(itemEntry.persona!) && job(itemEntry) !== "builder") at(itemEntry.id, undefined, "flow.persona", "the item entry's persona job must be builder");
  }
  const chunkLands = nodes.filter((n) => n.kind === "land" && n.scope === "chunk");
  for (const n of chunkLands.slice(1)) at(n.id, undefined, "flow.field", "at most one chunk land node");

  // B2, B3, B4: targets, reachability, exit shapes.
  const next = (to: string): FlowNode | undefined => (to === "@items" ? itemEntry : byId.get(to));
  for (const n of nodes) {
    for (const e of n.exits) {
      if (e.to === "@done") continue;
      if (e.to === "@items") {
        if (n.scope !== "chunk") at(n.id, e.name, "flow.target", "only chunk nodes may target @items");
        continue;
      }
      const t = byId.get(e.to);
      if (!t) at(n.id, e.name, "flow.target", `${e.to} is not a node id, @items, or @done`);
      else if (n.scope === "item" && t.scope === "chunk") at(n.id, e.name, "flow.target", `item node targets chunk node ${t.id}`);
    }
    if (n.exits.length === 0) at(n.id, undefined, "flow.dead-end", "the node has no exit");
    exitShape(n, byId, (exit, message) => at(n.id, exit, "flow.exit-shape", message));
  }
  const seen = new Set<string>();
  const queue = entry ? [entry] : [];
  for (const n of queue) {
    if (seen.has(n.id)) continue;
    seen.add(n.id);
    for (const e of n.exits) {
      const t = next(e.to);
      if (t && !seen.has(t.id)) queue.push(t);
    }
  }
  if (entry) for (const n of byId.values()) if (!seen.has(n.id)) at(n.id, undefined, "flow.unreachable", `not reachable from entry ${flow.entry}`);

  // B6: personas and prompt kinds.
  const landRole = new Map<string, Set<string>>();
  const need = (id: string | undefined, kinds: string[]) => {
    const p = id === undefined ? undefined : byId.get(id)?.persona;
    if (p) for (const k of kinds) (landRole.get(p) ?? landRole.set(p, new Set()).get(p)!).add(k);
  };
  for (const l of nodes.filter((n) => n.kind === "land")) {
    need(l.builder, ["test-failure", "fix", "merge-tip"]);
    need(l.verify, ["recheck", "land-recheck", ...(l.scope === "item" ? ["post-land"] : [])]);
    need(l.review, ["rereview"]);
  }
  for (const n of nodes.filter((n) => n.kind === "model")) {
    const p = bundle.personas.get(n.persona!);
    if (!p) {
      if (!bundle.personaFiles.has(n.persona!)) at(n.id, undefined, "flow.persona", `personas/${n.persona}.md does not exist`);
      continue;
    }
    if (p.scope !== n.scope) at(n.id, undefined, "flow.persona", `persona ${p.id} has scope ${p.scope}; the node has ${n.scope}`);
    if (!p.prompts.has("mint") && !p.prompts.has(`node-${n.id}`)) at(n.id, undefined, "persona.prompt-missing", `persona ${p.id} has neither ## Prompt: mint nor ## Prompt: node-${n.id}`);
  }
  for (const [pid, kinds] of landRole) {
    const p = bundle.personas.get(pid);
    for (const k of kinds) if (p && !p.prompts.has(k)) issues.push({ file: file.replace(/flow\.json$/, `personas/${pid}.md`), field: "-", code: "persona.prompt-missing", message: `the land sends ## Prompt: ${k}` });
  }

  // B8: skills.
  const union = new Set<string>();
  for (const p of bundle.personas.values()) for (const s of p.skills) union.add(s);
  for (const n of nodes) for (const s of n.skills ?? []) union.add(s);
  for (const s of union) if (!bundle.resolveSkill(s)) issues.push({ file: bundleMd, field: "-", code: "bundle.skill", message: `skill ${s} is neither the bundle's own nor in the skills home with a SOURCES.md row` });
  const listed = [...bundle.requiredSkills].sort().join(", ");
  if (listed !== [...union].sort().join(", ")) issues.push({ file: bundleMd, field: "-", code: "bundle.skill", message: `## Required skills lists ${listed || "none"}; personas and nodes use ${[...union].sort().join(", ") || "none"}` });

  // B10: land references.
  for (const l of nodes.filter((n) => n.kind === "land")) {
    const ref = (k: "builder" | "prove" | "verify" | "review", ok: (n: FlowNode) => boolean, what: string) => {
      const n = byId.get(l[k]!);
      if (!n || n.scope !== l.scope || !ok(n)) at(l.id, undefined, "flow.land-ref", `${k} ${l[k]} must be ${what} of scope ${l.scope}`);
      return n && n.scope === l.scope && ok(n);
    };
    ref("builder", (n) => isModel(n, "builder"), "a model node with job builder");
    ref("prove", (n) => n.kind === "command" && n.commands === (l.scope === "item" ? "groom" : "env"), `a command node with commands "${l.scope === "item" ? "groom" : "env"}"`);
    ref("verify", (n) => isModel(n, "verifier"), "a model node with job verifier");
    if (ref("review", (n) => isModel(n, "reviewer") && n.step === "Review", "a model node with step Review and job reviewer")) {
      const r = byId.get(l.review!)!;
      const missing = REVIEW_CHECKS.filter((c) => !(r.checks ?? []).includes(c));
      if (missing.length > 0) at(r.id, undefined, "flow.review-checks", `checks must hold ${missing.join(", ")}`);
    }
  }

  // B11: gate rows.
  const out = (n: FlowNode, suffix: string) => (n.outputs ?? []).some((p) => p.endsWith(suffix));
  const spec = (n: FlowNode) => n.kind === "model" && n.step === "Spec" && out(n, "/lld.md");
  const tagged = (t: string) => (n: FlowNode) => n.kind === "gate" && n.gate === t;
  const envCmd = (n: FlowNode) => n.kind === "command" && (n.commands === "env" || n.commands === "env-test");
  const chunkPlan = (suffix: string) => (n: FlowNode) => n.kind === "model" && n.scope === "chunk" && n.step === "Plan" && out(n, suffix);
  type Pred = (n: FlowNode) => boolean;
  const rows: [string, FlowNode[], Pred, [Pred, string][]][] = [
    ["gate.comparables", entry ? [entry] : [], chunkPlan("/hld.md"), [[chunkPlan("/comparables.md"), "the comparables node"]]],
    ["gate.plan", entry ? [entry] : [], spec, [[tagged("plan"), "the gate tagged plan"]]],
    ["gate.trial", entry ? [entry] : [], spec, [[tagged("trial"), "the gate tagged trial"]]],
    ["gate.spec", entry ? [entry] : [], (n) => n.step === "Groom" || n.scope === "item" || (n.scope === "chunk" && (isModel(n, "builder") || envCmd(n))),
      [[spec, "the Spec node"], [(n) => isModel(n, "security") && n.step === "Spec", "the security Spec node"], [tagged("spec"), "the gate tagged spec"]]],
    ["gate.env", entry ? [entry] : [], (n) => n.step === "Groom" || n.scope === "item",
      [[tagged("env"), "the gate tagged env"], [(n) => n.kind === "land" && n.scope === "chunk", "the chunk land node"]]],
  ];
  for (const b of nodes.filter((n) => isModel(n, "builder"))) {
    for (const l of nodes.filter((n) => n.kind === "land" && n.scope === b.scope)) {
      rows.push(["gate.land", [b], (n) => n === l, (["prove", "verify", "review"] as const).map((k) => [(n: FlowNode) => n.id === l[k], `its ${k} node ${l[k]}`])]);
    }
  }
  for (const [code, starts, target, required] of rows) {
    const targets = nodes.filter(target);
    if (targets.length === 0) continue;
    const absent = required.find(([p]) => !nodes.some(p));
    if (absent) {
      at(targets[0]!.id, undefined, code, `${absent[1]} does not exist`);
      continue;
    }
    const v = gateSearch(starts, target, required.map(([p]) => p), next);
    if (v) {
      const missing = required[v.k]![1];
      issues.push(v.exit === undefined
        ? { file, node: v.target.id, code, message: `reaches ${v.target.id} without passing ${missing}` }
        : { file, node: v.from!.id, exit: v.exit, code, message: `reaches ${v.target.id} without passing ${missing}` });
    }
  }

  // B14: env spec node and env-only nodes.
  const envSpecs = nodes.filter((n) => n.envSpec === true);
  for (const n of envSpecs.slice(1)) at(n.id, undefined, "flow.env", "envSpec on more than one node");
  for (const n of envSpecs) if (n.step !== "Spec" || !out(n, "/lld.md")) at(n.id, undefined, "flow.env", "envSpec needs step Spec and an outputs path ending /lld.md");
  if (envSpecs.length === 0) {
    for (const n of nodes) {
      if (envCmd(n)) at(n.id, undefined, "flow.env", `commands "${n.commands}" needs an envSpec node`);
      if (n.kind === "land" && n.scope === "chunk") at(n.id, undefined, "flow.env", "a chunk land node needs an envSpec node");
    }
  }
  return issues;
}

function exitShape(n: FlowNode, byId: Map<string, FlowNode>, bad: (exit: string | undefined, message: string) => void): void {
  const st = (e: { statuses: string[] }) => e.statuses.join(",");
  if (n.kind === "command") {
    const shapes = n.exits.map(st).sort().join(" ");
    if (shapes !== "fail pass") bad(undefined, "a command node has exactly two exits: one [pass], one [fail]");
  } else if (n.kind === "gate") {
    for (const e of n.exits) if (st(e) !== "pass" && st(e) !== "fail") bad(e.name, "each gate exit has exactly one status, pass or fail");
  } else if (n.kind === "land") {
    const e = n.exits[0];
    if (n.exits.length !== 1 || e?.name !== "done" || st(e) !== "pass") bad(e?.name, "a land node has exactly one exit, done, with [pass]");
    else if (n.scope === "item" ? e.to !== "@done" : byId.get(e.to)?.scope !== "chunk") bad(e.name, n.scope === "item" ? "an item land's done goes to @done" : "the chunk land's done goes to a chunk node");
  }
}

interface Violation {
  target: FlowNode;
  from?: FlowNode;
  exit?: string;
  k: number;
}

/**
 * Breadth-first search over (node, k), where k counts the required nodes
 * passed in order. Returns the shortest path's violation, if any.
 */
function gateSearch(starts: FlowNode[], target: (n: FlowNode) => boolean, required: ((n: FlowNode) => boolean)[], next: (to: string) => FlowNode | undefined): Violation | undefined {
  const step = (k: number, n: FlowNode) => (k < required.length && required[k]!(n) ? k + 1 : k);
  const seen = new Set<string>();
  const queue: [FlowNode, number][] = [];
  for (const s of starts) {
    const k = step(0, s);
    if (target(s) && k < required.length) return { target: s, k };
    queue.push([s, k]);
  }
  for (const [n, k] of queue) {
    const key = `${n.id}\0${k}`;
    if (seen.has(key)) continue;
    seen.add(key);
    for (const e of n.exits) {
      const t = next(e.to);
      if (!t) continue;
      const k2 = step(k, t);
      if (target(t) && k2 < required.length) return { target: t, from: n, exit: e.name, k: k2 };
      queue.push([t, k2]);
    }
  }
  return undefined;
}
