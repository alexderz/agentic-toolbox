#!/usr/bin/env bash
# Pre-flight: prove each model round-trips a structured tool call before the
# matrix spends hours on it. A model that cannot emit a parseable tool call
# scores zero for stack reasons, not capability -- catch that here.
set -uo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
API="${API:-http://127.0.0.1:8080/v1/chat/completions}"
OUT="$HERE/results/preflight.tsv"
RAW="$HERE/results/preflight-raw"
mkdir -p "$RAW" "$(dirname "$OUT")"

MODELS="${*:-$(awk -F'\t' 'NR>1&&$0!~/^#/{print $2}' "$HERE/matrix.tsv" | awk '!seen[$0]++')}"

printf 'model\tverdict\tfinish\ttool\tdetail\n' > "$OUT"

for m in $MODELS; do
  printf '=== %-24s ' "$m"
  body=$(cat <<JSON
{"model":"$m","max_tokens":512,
 "messages":[{"role":"user","content":"List the files in the current directory."}],
 "tools":[{"type":"function","function":{"name":"bash","description":"Run a shell command",
   "parameters":{"type":"object","properties":{"command":{"type":"string","description":"the command"}},"required":["command"]}}}]}
JSON
)
  t0=$(date +%s)
  resp=$(curl -s -m 1800 "$API" -H 'Content-Type: application/json' -d "$body" 2>&1)
  t1=$(date +%s)
  echo "$resp" > "$RAW/$m.json"

  finish=$(jq -r '.choices[0].finish_reason // "none"' <<<"$resp" 2>/dev/null)
  tool=$(jq -r '.choices[0].message.tool_calls[0].function.name // "none"' <<<"$resp" 2>/dev/null)
  args=$(jq -r '.choices[0].message.tool_calls[0].function.arguments // ""' <<<"$resp" 2>/dev/null)

  verdict=FAIL; detail=""
  if [[ -z "$resp" ]]; then
    detail="empty response"
  elif jq -e '.error' >/dev/null 2>&1 <<<"$resp"; then
    detail="api error: $(jq -rc '.error|tostring' <<<"$resp" | head -c 160)"
  elif [[ "$tool" == "none" ]]; then
    detail="no tool_call emitted (finish=$finish)"
  elif ! jq -e . >/dev/null 2>&1 <<<"$args"; then
    detail="arguments are not valid JSON"
  elif grep -qE '</parameter>|<tool_call>|</function>|<function=' <<<"$args"; then
    detail="XML leaked into arguments (parser mismatch)"
  elif [[ "$finish" != "tool_calls" ]]; then
    detail="parsed but finish=$finish (runaway generation)"
  else
    verdict=PASS; detail="$((t1-t0))s"
  fi

  printf '%s\t%s\t%s\t%s\t%s\n' "$m" "$verdict" "$finish" "$tool" "$detail" >> "$OUT"
  printf '%-4s %s\n' "$verdict" "$detail"
done

echo
echo "=== summary ==="
column -t -s$'\t' "$OUT"
