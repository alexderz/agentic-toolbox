#!/usr/bin/env bash
# Prove every matrix variant actually LOADS before the matrix commits hours to
# it. preflight.sh validated each model at its llama-swap default flags; the
# matrix overrides those flags, and coder30-max showed an override can OOM.
set -uo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$HERE"; # Provide set_variant/warm/vram for your runtime (see README).
source "${EVAL_LIB:-./lib.sh}"
OUT="$HERE/results/variant-probe.tsv"
mkdir -p "$HERE/results"
printf 'case\tmodel\tflags\tverdict\tload_s\tvram_mib\n' > "$OUT"
while IFS=$'\t' read -r case model flags note; do
  [ -z "${case:-}" ] && continue
  printf '%-18s ' "$case"
  if ! set_variant "$model" "$flags" >/dev/null 2>&1; then
    printf 'SET_FAILED\n'; printf '%s\t%s\t%s\tSET_FAILED\t\t\n' "$case" "$model" "$flags" >> "$OUT"; continue
  fi
  ls=$(warm "$model" 2>/dev/null || echo -1)
  if [ "$ls" = "-1" ]; then
    printf 'LOAD_FAILED\n'; printf '%s\t%s\t%s\tLOAD_FAILED\t\t\n' "$case" "$model" "$flags" >> "$OUT"
  else
    v=$(vram); printf 'OK  %ss  %s MiB\n' "$ls" "$v"
    printf '%s\t%s\t%s\tOK\t%s\t%s\n' "$case" "$model" "$flags" "$ls" "$v" >> "$OUT"
  fi
done < <(grep -v '^#' matrix.tsv)
echo; column -t -s$'\t' "$OUT"
