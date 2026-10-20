// Hand-written minimal types for the Node built-ins this package uses.
// Ruling S8 allows one dev dependency, `typescript`, so `@types/node` is
// not installed. Add a member here only when the code needs it.

interface Buffer extends Uint8Array {
  toString(encoding?: "utf8" | "hex"): string;
  subarray(start?: number, end?: number): Buffer;
}
declare var Buffer: {
  from(data: string | Uint8Array, encoding?: "utf8"): Buffer;
  concat(list: readonly Uint8Array[]): Buffer;
};

declare class TextDecoder {
  constructor(label: "utf-8", options?: { fatal?: boolean; ignoreBOM?: boolean });
  decode(input: Uint8Array): string;
}

declare var process: {
  argv: string[];
  execPath: string;
  env: Record<string, string | undefined>;
  exitCode: number | undefined;
  stdout: { write(s: string): boolean };
  stderr: { write(s: string): boolean };
};

interface ImportMeta {
  dirname: string;
  filename: string;
}

declare module "node:fs" {
  interface Stats {
    size: number;
    isFile(): boolean;
    isDirectory(): boolean;
    isSymbolicLink(): boolean;
  }
  interface Dirent {
    name: string;
  }
  export function readFileSync(path: string): Buffer;
  export function readFileSync(path: string, encoding: "utf8"): string;
  export function writeFileSync(path: string, data: string | Uint8Array): void;
  export function readdirSync(path: string): string[];
  export function lstatSync(path: string, options?: { throwIfNoEntry: boolean }): Stats | undefined;
  export function existsSync(path: string): boolean;
  export function mkdirSync(path: string, options?: { recursive: boolean }): void;
  export function mkdtempSync(prefix: string): string;
  export function rmSync(path: string, options?: { recursive: boolean; force: boolean }): void;
  export function symlinkSync(target: string, path: string): void;
  export function cpSync(src: string, dest: string, options?: { recursive: boolean }): void;
}

declare module "node:path" {
  export function join(...parts: string[]): string;
  export function resolve(...parts: string[]): string;
  export function dirname(p: string): string;
  export function basename(p: string, ext?: string): string;
  export function relative(from: string, to: string): string;
  export const sep: string;
}

declare module "node:os" {
  export function tmpdir(): string;
}

declare module "node:crypto" {
  interface Hash {
    update(data: string | Uint8Array): Hash;
    digest(encoding: "hex"): string;
  }
  export function createHash(algorithm: string): Hash;
}

declare module "node:child_process" {
  interface SpawnResult {
    status: number | null;
    stdout: Buffer;
    stderr: Buffer;
    error?: Error;
  }
  export function spawnSync(
    command: string,
    args: readonly string[],
    options?: {
      cwd?: string;
      env?: Record<string, string | undefined>;
      input?: string | Uint8Array;
      maxBuffer?: number;
    },
  ): SpawnResult;
}

declare module "node:test" {
  interface TestContext {
    skip(message?: string): void;
  }
  export function test(name: string, fn: (t: TestContext) => void | Promise<void>): void;
  export function describe(name: string, fn: () => void): void;
}

declare module "node:assert/strict" {
  const assert: {
    (value: unknown, message?: string): asserts value;
    equal(actual: unknown, expected: unknown, message?: string): void;
    deepEqual(actual: unknown, expected: unknown, message?: string): void;
    ok(value: unknown, message?: string): asserts value;
    match(value: string, re: RegExp, message?: string): void;
  };
  export default assert;
}
