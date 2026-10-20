// Bundle loader. A Tree reads the toolbox either from a working tree or
// from one commit's objects (ls-tree, then cat-file --batch, with each
// blob's hash verified). loadBundle applies the layout, persona, and skill
// rules (B7, B8, B12) and returns what the flow rules need.

import { createHash } from "node:crypto";
import { lstatSync, readdirSync, readFileSync } from "node:fs";
import { join } from "node:path";
import { parseFrontmatter } from "./frontmatter.ts";
import { git } from "./git.ts";
import type { Issue } from "./issue.ts";
import type { Scope } from "./flow.ts";

export interface TreeEntry {
  path: string;
  type: "file" | "link" | "other";
  size: number;
}

export interface Tree {
  /** Every entry under `prefix` (a root-relative path), recursively. */
  list(prefix: string): TreeEntry[];
  /** A regular file's bytes, or undefined. */
  read(path: string): Buffer | undefined;
}

export function fsTree(root: string): Tree {
  return {
    list(prefix) {
      const out: TreeEntry[] = [];
      const walk = (rel: string) => {
        const st = lstatSync(join(root, rel), { throwIfNoEntry: false });
        if (!st) return;
        if (st.isDirectory()) for (const name of readdirSync(join(root, rel)).sort()) walk(rel === "" ? name : `${rel}/${name}`);
        else out.push({ path: rel, type: st.isSymbolicLink() ? "link" : st.isFile() ? "file" : "other", size: st.size });
      };
      walk(prefix);
      return out;
    },
    read(path) {
      return lstatSync(join(root, path), { throwIfNoEntry: false })?.isFile() ? readFileSync(join(root, path)) : undefined;
    },
  };
}

/** Reads `commit` from the repository at `root`. Throws when the commit does not resolve. */
export function gitTree(root: string, commit: string): Tree {
  const rev = git(root, ["rev-parse", "--verify", "--end-of-options", `${commit}^{commit}`]);
  if (!rev.ok) throw new Error(`${commit} is not a commit in ${root}`);
  const sha = rev.stdout.toString("utf8").trim();
  const algo = git(root, ["rev-parse", "--show-object-format"]).stdout.toString("utf8").trim() === "sha256" ? "sha256" : "sha1";
  const ids = new Map<string, string>();
  const cache = new Map<string, Buffer | undefined>();
  return {
    list(prefix) {
      const r = git(root, ["ls-tree", "-r", "-z", sha, "--", prefix]);
      if (!r.ok) throw new Error(`git ls-tree failed: ${r.stderr.trim()}`);
      const out: TreeEntry[] = [];
      for (const rec of r.stdout.toString("utf8").split("\0")) {
        const m = /^(\d{6}) (\w+) ([0-9a-f]+)\t(.*)$/s.exec(rec);
        if (!m) continue;
        const [, mode, type, id, path] = m as unknown as [string, string, string, string, string];
        if (prefix !== "" && path !== prefix && !path.startsWith(`${prefix}/`)) continue;
        const file = type === "blob" && (mode === "100644" || mode === "100755");
        if (file) ids.set(path, id);
        out.push({ path, type: mode === "120000" ? "link" : file ? "file" : "other", size: file ? blob(path)?.length ?? 0 : 0 });
      }
      return out;
    },
    read(path) {
      if (!ids.has(path)) this.list(path);
      return blob(path);
    },
  };
  function blob(path: string): Buffer | undefined {
    if (cache.has(path)) return cache.get(path);
    const id = ids.get(path);
    let bytes: Buffer | undefined;
    if (id !== undefined) {
      const r = git(root, ["cat-file", "--batch"], `${id}\n`);
      const out = r.stdout;
      const nl = out.indexOf(0x0a);
      const m = /^([0-9a-f]+) blob (\d+)$/.exec(out.subarray(0, nl).toString("utf8"));
      if (!r.ok || !m || m[1] !== id) throw new Error(`git cat-file did not print ${id} for ${path}`);
      bytes = out.subarray(nl + 1, nl + 1 + Number(m[2]));
      const h = createHash(algo).update(`blob ${bytes.length}\0`).update(bytes).digest("hex");
      if (h !== id) throw new Error(`${path}: object ${id} hashes to ${h}`);
    }
    cache.set(path, bytes);
    return bytes;
  }
}

export const JOBS = ["refiner", "architect", "designer", "ux-reviewer", "security", "groom-reviewer", "manager", "builder", "verifier", "reviewer"] as const;
const READ_ONLY_JOBS = ["refiner", "ux-reviewer", "security", "groom-reviewer", "verifier", "reviewer"];
/** Prompt kinds by job and scope. `repair`, `answer`, and `rehydrate` stay out of the file. */
const PROMPT_KINDS: Record<string, readonly string[]> = {
  "refiner:chunk": ["mint", "resume"],
  "architect:chunk": ["mint", "resume", "node-comparables", "node-hld", "node-spec", "node-groom", "paperwork"],
  "designer:chunk": ["mint", "resume", "node-mockups"],
  "ux-reviewer:chunk": ["mint", "resume"],
  "security:chunk": ["mint", "resume"],
  "groom-reviewer:chunk": ["mint", "resume"],
  "manager:chunk": ["mint", "stop", "gate", "apply-answer", "node-file-tickets"],
  "builder:chunk": ["node-env-prep", "resume", "test-failure", "fix", "merge-tip"],
  "builder:item": ["mint", "resume", "test-failure", "fix", "merge-tip"],
  "verifier:chunk": ["mint", "recheck", "land-recheck"],
  "verifier:item": ["mint", "recheck", "land-recheck", "post-land"],
  "reviewer:chunk": ["mint", "rereview"],
  "reviewer:item": ["mint", "rereview"],
};
const STATE_HEADINGS: Record<string, readonly string[]> = {
  builder: ["## Corrected errors", "## Open findings", "## Do not repeat", "## Next"],
  verifier: ["## Ledger", "## Nits", "## Last commands seen"],
  reviewer: ["## Verdicts", "## Open review comments", "## Security reads"],
  architect: ["## Node", "## Decisions", "## Open", "## Outputs written"],
  refiner: ["## Brief version", "## Cuts proposed", "## Open"],
  designer: ["## Work", "## Findings", "## Open"],
  "ux-reviewer": ["## Work", "## Findings", "## Open"],
  security: ["## Boundaries read", "## Findings", "## Open"],
  "groom-reviewer": ["## Reviewed commit", "## Findings", "## Open"],
  manager: ["## Stops handled", "## Pending asks", "## Parked"],
};
const TOOLS = ["read", "bash", "edit", "write", "grep", "find", "ls"];
const PERSONA_KEYS = ["schemaVersion", "id", "job", "scope", "readOnly", "model", "tools", "skills", "tracker"];
export const PLACEHOLDERS = [
  "ticket", "epic", "step", "node", "persona", "label", "run", "worktree", "branch", "projectMain", "range",
  "rangeMain", "log", "repair", "exits", "checks", "outputs", "tip", "landSha", "landResult", "verdict",
  "commentText", "stopKind", "stopRun", "question", "choices", "answer", "record", "ask", "extracted",
  "envSpec", "capability",
];
const MAX_FILE = 256 * 1024;
const TOP = ["bundle.md", "flow.json", "personas", "skills", "scripts"];
export const BUNDLE_ID = /^[a-z][a-z0-9-]{0,31}$/;

export interface Persona {
  id: string;
  job: string;
  scope: Scope;
  skills: string[];
  prompts: Set<string>;
}

export interface Bundle {
  id: string;
  flowBytes?: Buffer;
  /** Personas whose front matter parsed; a broken file is absent with an issue. */
  personas: Map<string, Persona>;
  personaFiles: Set<string>;
  requiredSkills: string[];
  scripts: Map<string, Buffer>;
  /** True when the skill is the bundle's own, or in the skills home with a SOURCES.md row. */
  resolveSkill(id: string): boolean;
}

export interface LoadOptions {
  /** `docs/INTAKE.md` at the reviewed ref, for a bundle commit outside reviewed history. */
  intake?: string;
}

/**
 * `dir` is the bundle's root-relative path; `show(rel)` names a bundle
 * file in issues.
 */
export function loadBundle(tree: Tree, dir: string, id: string, show: (rel: string) => string, opts: LoadOptions = {}): { bundle: Bundle; issues: Issue[] } {
  const issues: Issue[] = [];
  const layout = (rel: string, message: string, code = "bundle.layout") => issues.push({ file: show(rel), field: "-", code, message });
  const bundle: Bundle = { id, personas: new Map(), personaFiles: new Set(), requiredSkills: [], scripts: new Map(), resolveSkill: () => false };
  if (!BUNDLE_ID.test(id)) layout(".", `bundle id ${JSON.stringify(id)} does not match ^[a-z][a-z0-9-]{0,31}$`);
  const files = new Map<string, Buffer>();
  for (const e of tree.list(dir)) {
    const rel = e.path.slice(dir.length + 1);
    const top = rel.split("/")[0]!;
    if (e.type === "link") layout(rel, "symbolic link");
    else if (e.type === "other") layout(rel, "not a regular file");
    else if (e.size > MAX_FILE) layout(rel, `${e.size} bytes; the cap is 256 KiB`);
    else if (!TOP.includes(top) || (rel.includes("/") !== (top !== "bundle.md" && top !== "flow.json"))) layout(rel, "not an allowed top-level entry");
    else if (top === "personas" && !/^personas\/[^/]+\.md$/.test(rel)) layout(rel, "personas/ holds only <persona-id>.md files");
    else files.set(rel, tree.read(e.path)!);
  }
  bundle.flowBytes = files.get("flow.json");
  if (!bundle.flowBytes) layout("flow.json", "missing");
  for (const [rel, bytes] of files) {
    if (rel.startsWith("scripts/")) bundle.scripts.set(rel, bytes);
    const m = /^personas\/(.+)\.md$/.exec(rel);
    if (!m) continue;
    bundle.personaFiles.add(m[1]!);
    const p = readPersona(m[1]!, bytes.toString("utf8"), (code, message) => issues.push({ file: show(rel), field: "-", code, message }));
    if (p) bundle.personas.set(p.id, p);
  }
  const md = files.get("bundle.md");
  if (!md) layout("bundle.md", "missing");
  else bundleMd(md.toString("utf8"), bundle, (message, code) => layout("bundle.md", message, code), opts, dir);
  let sources: string[] | undefined;
  bundle.resolveSkill = (sid) => {
    if (files.has(`skills/${sid}/SKILL.md`)) return true;
    if (tree.read(`skills/${sid}/SKILL.md`) === undefined) return false;
    sources ??= (tree.read("SOURCES.md")?.toString("utf8") ?? "").split("\n");
    return sources.some((l) => l.split("|")[1]?.trim() === sid);
  };
  return { bundle, issues };
}

function readPersona(stem: string, text: string, add: (code: string, message: string) => void): Persona | undefined {
  const fm = parseFrontmatter(text);
  if (!fm.ok) return void add("persona.frontmatter", fm.message);
  const f = fm.fields;
  let ok = true;
  const bad = (message: string, code = "persona.frontmatter") => {
    add(code, message);
    if (code === "persona.frontmatter") ok = false;
  };
  for (const k of Object.keys(f)) if (!PERSONA_KEYS.includes(k)) bad(`unknown key ${k}`);
  for (const k of PERSONA_KEYS) if (f[k] === undefined) bad(`missing key ${k}`);
  if (f.schemaVersion !== undefined && f.schemaVersion !== 1) bad("schemaVersion must be 1");
  if (f.scope !== undefined && f.scope !== "chunk" && f.scope !== "item") bad("scope must be chunk or item");
  if (f.id !== undefined) {
    const re = f.scope === "item" ? /^[a-z][a-z0-9-]{0,7}$/ : /^[a-z][a-z0-9-]{0,31}$/;
    if (f.id !== stem) bad(`id ${String(f.id)} differs from the file stem ${stem}`);
    else if (!re.test(stem)) bad(`id does not match ${re.source} for scope ${String(f.scope)}`);
  }
  if (f.job !== undefined && !(JOBS as readonly unknown[]).includes(f.job)) bad(`job ${String(f.job)} is not a job`);
  for (const k of ["readOnly", "tracker"]) if (f[k] !== undefined && typeof f[k] !== "boolean") bad(`${k} must be true or false`);
  if (f.model !== undefined && typeof f.model !== "string") bad("model must be a model slot name");
  for (const k of ["tools", "skills"]) if (f[k] !== undefined && !Array.isArray(f[k])) bad(`${k} must be a list`);
  if (READ_ONLY_JOBS.includes(String(f.job)) && f.readOnly === false) bad(`job ${String(f.job)} must be readOnly: true`, "persona.readonly");
  if (Array.isArray(f.tools)) {
    for (const t of f.tools) if (!TOOLS.includes(t)) bad(`tool ${t} is not one of ${TOOLS.join(", ")}`, "persona.tools");
    if (f.readOnly === true && f.tools.some((t) => t === "edit" || t === "write")) bad("a read-only persona has no edit or write", "persona.tools");
  }
  const prompts = body(fm.body, add, typeof f.job === "string" ? f.job : "");
  const row = typeof f.job === "string" && (f.scope === "chunk" || f.scope === "item") ? PROMPT_KINDS[`${f.job}:${f.scope}`] : undefined;
  if (row === undefined && (JOBS as readonly string[]).includes(String(f.job)) && (f.scope === "chunk" || f.scope === "item")) {
    bad(`job ${String(f.job)} has no prompt-kind row for scope ${String(f.scope)}`);
  } else if (row !== undefined) {
    const missing = row.filter((k) => !prompts.has(k));
    if (missing.length > 0) bad(`missing ## Prompt: ${missing.join(", ")}`, "persona.prompt-missing");
  }
  if (!ok) return undefined;
  return { id: stem, job: f.job as string, scope: f.scope as Scope, skills: f.skills as string[], prompts };
}

// The state template holds `##` headings of its own, so the body splits
// only on `## Role`, `## State template`, and `## Prompt: <kind>`.
function body(text: string, add: (code: string, message: string) => void, job: string): Set<string> {
  const sections: { heading: string; lines: string[] }[] = [];
  const preamble: string[] = [];
  for (const line of text.split("\n")) {
    const h = line.startsWith("## ") ? line.slice(3).trim() : undefined;
    const split = h !== undefined && (h.startsWith("Prompt:") || (sections.length === 0 && h === "Role") || (sections.length === 1 && h === "State template"));
    if (split) sections.push({ heading: h!, lines: [] });
    else (sections.at(-1)?.lines ?? preamble).push(line);
  }
  if (preamble.some((l) => l.trim() !== "")) add("persona.section", "text before ## Role");
  if (sections[0]?.heading !== "Role") add("persona.section", "the first section must be ## Role");
  if (sections[1]?.heading !== "State template") add("persona.section", "the second section must be ## State template");
  const kinds = new Set<string>();
  const state = sections[1]?.heading === "State template" ? sections[1].lines : [];
  while (state.length > 0 && state.at(-1)!.trim() === "") state.pop();
  while (state.length > 0 && state[0]!.trim() === "") state.shift();
  if (state.length > 60) add("persona.section", `## State template has ${state.length} lines; the cap is 60`);
  const want = STATE_HEADINGS[job];
  if (want !== undefined) {
    const missing = want.filter((h) => !state.some((l) => l.trim() === h));
    if (missing.length > 0) add("persona.section", `missing ${missing.join(", ")}`);
  }
  for (const s of sections.slice(2)) {
    const m = /^Prompt: ([a-z][a-z0-9-]{0,31})$/.exec(s.heading);
    if (!m) {
      add("persona.section", `## ${s.heading} is not ## Prompt: <kind>`);
      continue;
    }
    if (kinds.has(m[1]!)) add("persona.section", `duplicate ## Prompt: ${m[1]}`);
    kinds.add(m[1]!);
    for (const p of s.lines.join("\n").matchAll(/\{\{([^{}]*)\}\}/g)) {
      if (!PLACEHOLDERS.includes(p[1]!)) add("persona.placeholder", `prompt ${m[1]}: {{${p[1]}}} is not a placeholder`);
    }
  }
  return kinds;
}

const HEADINGS = ["What it is", "Flow summary", "Required skills", "Personas", "Modes"];

function bundleMd(text: string, b: Bundle, bad: (message: string, code?: string) => void, opts: LoadOptions, dir: string): void {
  const sections = new Map<string, string[]>();
  const order: string[] = [];
  let title: string | undefined;
  let cur: string[] | undefined;
  let fence = false;
  for (const line of text.split("\n")) {
    if (line.startsWith("```")) fence = !fence;
    if (!fence && line.startsWith("# ")) {
      if (title !== undefined || order.length > 0) bad(`unexpected heading ${line}`);
      title = line.slice(2).trim();
      cur = undefined;
    } else if (!fence && line.startsWith("## ")) {
      const h = line.slice(3).trim();
      order.push(h);
      sections.set(h, (cur = []));
    } else cur?.push(line);
  }
  if (title !== `Bundle — ${b.id}`) bad(`the first heading must be # Bundle — ${b.id}`);
  const want = [...HEADINGS, ...(b.scripts.size > 0 || sections.has("Scripts") ? ["Scripts"] : [])];
  if (order.join("\n") !== want.join("\n")) bad(`headings must be ${want.map((h) => `## ${h}`).join(", ")}, in order`);
  const bullets = (h: string) =>
    (sections.get(h) ?? []).filter((l) => l.startsWith("- ")).map((l) => /^- `?([^`\s]+)`?/.exec(l)?.[1] ?? "");
  b.requiredSkills = bullets("Required skills");
  const personas = bullets("Personas").sort();
  if (personas.join() !== [...b.personaFiles].sort().join()) bad(`## Personas lists ${personas.join(", ") || "none"}; personas/ holds ${[...b.personaFiles].sort().join(", ") || "none"}`);
  const modes = bullets("Modes");
  if (modes.length === 0 || !modes.every((m) => m === "enforced" || m === "followed")) bad("## Modes lists enforced, followed, or both");
  const listed = new Map<string, { sha: string; record: string }>();
  for (const l of (sections.get("Scripts") ?? []).filter((l) => l.startsWith("- "))) {
    const m = /^- `(scripts\/[^`]+)` sha256 `([0-9a-f]{64})` intake `([a-z0-9][a-z0-9-]{0,39})`$/.exec(l);
    if (!m) bad(`## Scripts bullet is not \`scripts/<file>\` sha256 \`<hex>\` intake \`<record>\`: ${l}`, "bundle.script-intake");
    else listed.set(m[1]!, { sha: m[2]!, record: m[3]! });
  }
  for (const [rel, bytes] of b.scripts) {
    const sha = createHash("sha256").update(bytes).digest("hex");
    const entry = listed.get(rel);
    if (!entry) bad(`${rel} has no ## Scripts bullet`, "bundle.script-intake");
    else if (entry.sha !== sha) bad(`${rel} hashes to ${sha}, not the listed ${entry.sha}`, "bundle.script-intake");
    else if (opts.intake !== undefined && !intakeHas(opts.intake, entry.record, `${dir}/${rel}`, sha)) {
      bad(`${rel}: no line for record ${entry.record} with this path and hash under ## Script records in docs/INTAKE.md at the reviewed ref`, "bundle.script-intake");
    }
  }
  for (const rel of listed.keys()) if (!b.scripts.has(rel)) bad(`## Scripts lists ${rel}, which does not exist`, "bundle.script-intake");
}

function intakeHas(intake: string, record: string, path: string, sha: string): boolean {
  const start = intake.split("\n").findIndex((l) => l.trim() === "## Script records");
  if (start < 0) return false;
  const want = `\`${record}\` \`${path}\` sha256 \`${sha}\``;
  for (const l of intake.split("\n").slice(start + 1)) {
    if (l.startsWith("## ")) break;
    if (l.replace(/^- /, "").trim() === want) return true;
  }
  return false;
}
