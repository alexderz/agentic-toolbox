// One check or validation error, and its console line:
// `<file>: node <id> exit <name>: <code>: <message>`, or
// `<file>: <field>: <code>: <message>` when no node applies.

export interface Issue {
  file: string;
  code: string;
  message: string;
  node?: string;
  exit?: string;
  field?: string;
}

export function formatIssue(i: Issue): string {
  let where: string;
  if (i.node !== undefined) where = i.exit !== undefined ? `node ${i.node} exit ${i.exit}` : `node ${i.node}`;
  else where = i.field ?? "-";
  return `${i.file}: ${where}: ${i.code}: ${i.message}`;
}
