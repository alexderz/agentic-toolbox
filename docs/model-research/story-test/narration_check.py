#!/usr/bin/env python3
"""Static checks for a story test round 3 script (a narration script tagged for ElevenLabs Eleven v4).

  python3 narration_check.py script.md [--json]

Reads the model's reply (NARRATION NOTES block, then === PART n === sections, the title as the first line of part 1)
and reports what can be counted before rendering:
- the story's word count without tags, the tag count, tags per 100 words, the distinct tags and the most used ones, and
  every part's full tag list (to spot tags that may play as sound effects);
- part sizes against the brief's 9,000 characters and the 10,000-character Eleven v4 request limit, and whether each
  part opens with a tag;
- the paragraph layout that ElevenLabs Studio needs: lines that hold only a tag, paragraphs that do not open with a
  tag, and paragraphs that end with a pause tag;
- text that would be read aloud wrongly or is out of format: digits, symbols, Markdown, SSML, empty, nested,
  unclosed or over-long brackets, text before the notes, CAPITALS emphasis count.
It does not grade the story.
"""
import collections, json, re, sys

TAG = re.compile(r"\[([^\[\]\n]{1,80})\]")
PART = re.compile(r"^=== PART (\d+) ===\s*$", re.M)
V4_LIMIT, BRIEF_LIMIT = 10000, 9000


def words(s):
    return len(TAG.sub(" ", s).replace("—", " ").split())


def check(text):
    text = text.replace("\r\n", "\n")
    r, problems = {}, []
    notes = re.search(r"^NARRATION NOTES:?\s*$(.*?)^END NOTES:?\s*$", text, re.M | re.S)
    r["notes_words"] = len(notes.group(1).split()) if notes else None
    if not notes:
        problems.append("no NARRATION NOTES ... END NOTES block")
    else:
        if r["notes_words"] > 150:
            problems.append(f"notes are {r['notes_words']} words (brief: at most 150)")
        if text[:notes.start()].strip():
            problems.append("text before the notes block")
    marks = list(PART.finditer(text))
    if not marks:
        problems.append("no === PART n === markers")
        parts = [text[notes.end():] if notes else text]
    else:
        parts = [text[m.end():(marks[i + 1].start() if i + 1 < len(marks) else len(text))] for i, m in enumerate(marks)]
        nums = [int(m.group(1)) for m in marks]
        if nums != list(range(1, len(nums) + 1)):
            problems.append(f"part numbers {nums}")
        if text[notes.end() if notes else 0:marks[0].start()].strip():
            problems.append("text between the notes and part 1 (not sent to the voice model)")
    first = [ln.strip() for ln in TAG.sub("", parts[0]).splitlines() if ln.strip()]
    r["title"] = first[0] if first else None
    body = "".join(parts)
    tags = [t.strip().lower() for t in TAG.findall(body)]
    r.update(words=words(body), tags=len(tags), distinct_tags=len(set(tags)),
             top_tags=collections.Counter(tags).most_common(8))
    r["tags_per_100_words"] = round(100 * len(tags) / max(r["words"], 1), 1)
    r["parts"] = []
    for i, p in enumerate(parts, 1):
        p = p.strip()
        r["parts"].append({"part": i, "chars": len(p), "words": words(p), "tags": TAG.findall(p),
                           "opens_with_tag": bool(TAG.match(p))})
        if len(p) > V4_LIMIT:
            problems.append(f"part {i} is {len(p)} characters, over the Eleven v4 request limit of {V4_LIMIT}")
        elif len(p) > BRIEF_LIMIT:
            problems.append(f"part {i} is {len(p)} characters (brief: at most {BRIEF_LIMIT})")
        if not TAG.match(p):
            problems.append(f"part {i} does not open with a tag")
    lines = [ln.strip() for ln in body.splitlines() if ln.strip()]
    alone = [ln for ln in lines if not TAG.sub("", ln).strip()]
    untagged = [ln for i, ln in enumerate(lines) if TAG.sub("", ln).strip() and not TAG.match(ln)
                and not (i and lines[i - 1] in alone)]
    trailing = [ln for ln in lines if TAG.sub("", ln).strip()
                and re.search(r"\[(short |long )?pauses?\]\s*$", ln, re.I)]
    r["layout"] = {"paragraphs": len(lines), "tag_only_lines": len(alone), "untagged_paragraphs": len(untagged),
                   "paragraphs_ending_in_a_pause": len(trailing)}
    if alone:
        problems.append(f"{len(alone)} lines hold only a tag (Studio voices each paragraph alone and may speak them)")
    if untagged:
        problems.append(f"{len(untagged)} paragraphs do not open with a tag (nor follow a tag-only line; in Studio they lose the direction)")
    if trailing:
        problems.append(f"{len(trailing)} paragraphs end with a pause tag (nothing follows it in Studio)")
    prose = TAG.sub(" ", body)
    caps = [c for c in re.findall(r"\b[A-Z]{2,}\b", prose) if c not in ("AI", "I")]
    r["caps_emphasis"] = len(caps)
    r["caps_words"] = collections.Counter(caps).most_common(8)
    digits = re.findall(r"\S*\d\S*", prose)
    r["digits"] = digits[:12]
    if digits:
        problems.append(f"{len(digits)} tokens with digits (should be words): {' '.join(digits[:6])}")
    symbols = re.findall(r"[%&$/@#<>=+*_|~^]", prose)
    if symbols:
        problems.append(f"{len(symbols)} symbols that a voice reads badly: {''.join(sorted(set(symbols)))}")
    if re.search(r"<break|<phoneme|</?speak", body):
        problems.append("SSML in the script (Eleven v4 ignores it)")
    if re.search(r"^\s*(#+ |[-*] |\d+\. |---+\s*$)", body, re.M):
        problems.append("Markdown headings, lists or rules")
    if re.search(r"\[\s*\]", body) or "[" in prose or "]" in prose:
        problems.append("empty, nested, unclosed, multi-line or over-long (over 80 characters) brackets")
    r["problems"] = problems
    return r


if __name__ == "__main__":
    res = check(open(sys.argv[1], encoding="utf-8").read())
    if "--json" in sys.argv:
        print(json.dumps(res, indent=1))
    else:
        print(f"title: {res['title']}\nwords {res['words']}, tags {res['tags']} ({res['tags_per_100_words']} per 100 words, "
              f"{res['distinct_tags']} distinct), CAPS emphasis {res['caps_emphasis']}, notes {res['notes_words']} words")
        print("top tags:", ", ".join(f"{t} x{n}" for t, n in res["top_tags"]))
        for p in res["parts"]:
            print(f"  part {p['part']}: {p['chars']} chars, {p['words']} words, {len(p['tags'])} tags")
        print("problems:", "; ".join(res["problems"]) or "none")
