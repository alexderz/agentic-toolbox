// Persona front matter: a YAML subset parsed without a YAML library.
// Front matter is every leading line; the body starts at the first line
// that begins with `#`. One `key: value` per line; a value is true, false,
// a non-negative integer, a bare word, or a flow list of bare words.
// Blank lines are skipped.

export type FrontValue = boolean | number | string | string[];
export type Frontmatter =
  | { ok: true; fields: Record<string, FrontValue>; body: string }
  | { ok: false; message: string };

const WORD = /^[A-Za-z0-9._/-]+$/;

export function parseFrontmatter(text: string): Frontmatter {
  const lines = text.split("\n");
  let end = lines.findIndex((l) => l.startsWith("#"));
  if (end < 0) end = lines.length;
  const fields: Record<string, FrontValue> = {};
  for (const [n, line] of lines.slice(0, end).entries()) {
    if (line.trim() === "") continue;
    const m = /^([A-Za-z][A-Za-z0-9]*): (.+)$/.exec(line);
    const v = m ? value(m[2]!) : undefined;
    if (!m || v === undefined) return { ok: false, message: `line ${n + 1}: not key: value in the subset` };
    if (Object.hasOwn(fields, m[1]!)) return { ok: false, message: `line ${n + 1}: duplicate key ${m[1]}` };
    fields[m[1]!] = v;
  }
  return { ok: true, fields, body: lines.slice(end).join("\n") };
}

function value(s: string): FrontValue | undefined {
  if (s === "true") return true;
  if (s === "false") return false;
  if (/^(0|[1-9]\d*)$/.test(s)) return Number(s);
  if (WORD.test(s)) return s;
  const list = /^\[(.*)\]$/.exec(s);
  if (!list) return undefined;
  if (list[1] === "") return [];
  const items = list[1]!.split(", ");
  return items.every((w) => WORD.test(w)) ? items : undefined;
}
