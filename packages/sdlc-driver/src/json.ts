// Strict JSON reader: one value, UTF-8, no duplicate keys, no nulls, no
// trailing text. A number written with a fraction or exponent is a
// JsonFloat, so `1.0` never passes as the integer `1`.

export class JsonFloat {
  readonly value: number;
  constructor(value: number) {
    this.value = value;
  }
}

export type JsonValue = string | number | boolean | JsonFloat | JsonValue[] | { [key: string]: JsonValue };
export type JsonObject = { [key: string]: JsonValue };

export type JsonErrorKind = "syntax" | "duplicate-key" | "null" | "trailing-text";
export type JsonRead =
  | { ok: true; value: JsonValue }
  | { ok: false; error: { kind: JsonErrorKind; message: string } };

class Stop extends Error {
  readonly kind: JsonErrorKind;
  constructor(kind: JsonErrorKind, message: string) {
    super(message);
    this.kind = kind;
  }
}

const decoder = new TextDecoder("utf-8", { fatal: true, ignoreBOM: true });

export function readStrictJson(input: string | Uint8Array): JsonRead {
  let text: string;
  if (typeof input === "string") text = input;
  else {
    try {
      text = decoder.decode(input);
    } catch {
      return { ok: false, error: { kind: "syntax", message: "not valid UTF-8" } };
    }
  }
  let i = 0;
  const fail = (kind: JsonErrorKind, message: string): never => {
    throw new Stop(kind, `${message} at offset ${i}`);
  };
  const ws = () => {
    while (i < text.length && " \t\n\r".includes(text[i]!)) i++;
  };
  const expect = (s: string) => {
    if (text.startsWith(s, i)) i += s.length;
    else fail("syntax", `expected ${JSON.stringify(s)}`);
  };
  const str = (): string => {
    expect('"');
    let out = "";
    for (;;) {
      if (i >= text.length) fail("syntax", "unterminated string");
      const c = text[i++]!;
      if (c === '"') return out;
      if (c < " ") fail("syntax", "control character in string");
      if (c !== "\\") {
        out += c;
        continue;
      }
      const e = text[i++];
      const simple: Record<string, string> = { '"': '"', "\\": "\\", "/": "/", b: "\b", f: "\f", n: "\n", r: "\r", t: "\t" };
      if (e !== undefined && e in simple) out += simple[e];
      else if (e === "u" && /^[0-9a-fA-F]{4}$/.test(text.slice(i, i + 4))) {
        out += String.fromCharCode(parseInt(text.slice(i, i + 4), 16));
        i += 4;
      } else fail("syntax", "bad escape");
    }
  };
  const value = (): JsonValue => {
    ws();
    const c = text[i];
    if (c === "{") {
      i++;
      const obj: JsonObject = {};
      ws();
      if (text[i] === "}") {
        i++;
        return obj;
      }
      for (;;) {
        ws();
        const k = str();
        if (Object.hasOwn(obj, k)) fail("duplicate-key", `duplicate key ${JSON.stringify(k)}`);
        ws();
        expect(":");
        obj[k] = value();
        ws();
        if (text[i] === ",") i++;
        else if (text[i] === "}") {
          i++;
          return obj;
        } else fail("syntax", "expected , or }");
      }
    }
    if (c === "[") {
      i++;
      const arr: JsonValue[] = [];
      ws();
      if (text[i] === "]") {
        i++;
        return arr;
      }
      for (;;) {
        arr.push(value());
        ws();
        if (text[i] === ",") i++;
        else if (text[i] === "]") {
          i++;
          return arr;
        } else fail("syntax", "expected , or ]");
      }
    }
    if (c === '"') return str();
    if (text.startsWith("true", i)) return (i += 4), true;
    if (text.startsWith("false", i)) return (i += 5), false;
    if (text.startsWith("null", i)) fail("null", "null value");
    const m = /^-?(?:0|[1-9]\d*)(\.\d+)?([eE][+-]?\d+)?/.exec(text.slice(i));
    if (!m) return fail("syntax", "unexpected character");
    i += m[0].length;
    const n = Number(m[0]);
    return m[1] || m[2] ? new JsonFloat(n) : n;
  };
  try {
    const v = value();
    ws();
    if (i < text.length) fail("trailing-text", "text after the JSON value");
    return { ok: true, value: v };
  } catch (e) {
    if (e instanceof Stop) return { ok: false, error: { kind: e.kind, message: e.message } };
    throw e;
  }
}

export function isObject(v: JsonValue | undefined): v is JsonObject {
  return typeof v === "object" && v !== null && !Array.isArray(v) && !(v instanceof JsonFloat);
}

export function isInteger(v: JsonValue | undefined): v is number {
  return typeof v === "number" && Number.isSafeInteger(v);
}
