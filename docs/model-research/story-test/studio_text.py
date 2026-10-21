#!/usr/bin/env python3
"""Turn a story test round 3 script into text whose tags hold paragraph by paragraph.

  python3 studio_text.py script.md out.txt

ElevenLabs Studio voices each paragraph as its own request, so a tag can shape only the paragraph it is in, and a
paragraph that holds only a tag has no words for it to shape. A script written for whole-part API requests often
relies on a tag holding until the next one. This keeps every word and every tag the model chose, and changes only
where tags sit:
- drops the NARRATION NOTES block and the === PART n === markers;
- moves a tag that sits alone on a line onto the start of the next line of text;
- repeats the current narration tag (the first tag of the last tagged narration paragraph) on narration paragraphs
  that have none;
- splits a paragraph that opens with narration under a character's tag before that character's quoted line;
- adds "voice" to tags with "synthetic" but no "voice", which could otherwise play as a synth sound;
- removes [pause] and [long pause] tags that open a paragraph or end one, and reports where to put a silence instead;
- writes ICE in lower case, as the brief asks.

Dialogue is a paragraph that opens with a straight or curly double quote. The output separates paragraphs with blank
lines. It prints where to add silences and where the parts began. render_narration.py imports convert() to split the
same paragraphs into requests.
"""
import re
import sys

TAG = re.compile(r"\[[^\]\n]+\]")
TAG_LINE = re.compile(r"^\s*(\[[^\]\n]+\]\s*)+$")
LEAD = re.compile(r"^((?:\[[^\]\n]+\]\s*)*)(.*)$", re.S)
PART = re.compile(r"^=== PART \d+ ===$")
PAUSES = {"[pause]", "[pauses]", "[long pause]", "[short pause]"}
QUOTES = '"“'


def is_dialogue(body):
    return body[:1] in QUOTES


def fix_tag(t):
    if re.search(r"\bsynthetic\b", t) and "voice" not in t:
        t = re.sub(r"\bsynthetic\b", "synthetic voice", t)
    return t


def convert(script):
    """Return a list of paragraphs: dicts with text, part (a part starts here) and gap_before/gap_after tags."""
    paras, pending, in_notes, new_part = [], [], False, False
    for line in script.replace("\r\n", "\n").splitlines():
        s = line.strip()
        if re.fullmatch(r"NARRATION NOTES:?", s):
            in_notes = True
            continue
        if in_notes and not PART.fullmatch(s):
            in_notes = not re.fullmatch(r"END NOTES:?", s)
            continue
        in_notes = False
        if PART.fullmatch(s):
            new_part = bool(paras)
            continue
        if not s:
            continue
        if TAG_LINE.match(s):
            pending += TAG.findall(s)
            continue
        m = LEAD.match(s)
        paras.append({"tags": pending + TAG.findall(m.group(1)), "body": m.group(2).strip(), "part": new_part})
        pending, new_part = [], False
    if pending and paras:
        paras[-1]["trailing"] = pending

    dialogue_tags = {t for p in paras if is_dialogue(p["body"]) for t in p["tags"]}
    split = []
    for p in paras:
        q = min((i for i in (p["body"].find(c) for c in QUOTES) if i >= 0), default=-1)
        if p["tags"] and not is_dialogue(p["body"]) and q > 0 and p["tags"][-1] in dialogue_tags:
            split.append({"tags": [], "body": p["body"][:q].strip(), "part": p["part"]})
            split.append({"tags": p["tags"], "body": p["body"][q:].strip(), "part": False,
                          "trailing": p.get("trailing", [])})
        else:
            split.append(p)

    out, last_narration = [], None
    for p in split:
        tags, body = p["tags"], p["body"]
        gap_before = [t for t in tags if t in PAUSES]
        tags = [t for t in tags if t not in PAUSES]
        end = re.search(r"(\s*\[[^\]\n]+\])+\s*$", body)
        gap_after = list(p.get("trailing", []))
        if end and all(t in PAUSES for t in TAG.findall(end.group(0))):
            gap_after = TAG.findall(end.group(0)) + gap_after
            body = body[:end.start()].rstrip()
        if not is_dialogue(body):
            if tags:
                last_narration = tags[0]
            elif last_narration:
                tags = [last_narration]
        text = " ".join([fix_tag(t) for t in tags] + [TAG.sub(lambda m: fix_tag(m.group(0)), body)])
        text = re.sub(r"\bICE\b", "ice", text)
        out.append({"text": text, "part": p["part"], "gap_before": gap_before, "gap_after": gap_after})
    return out


if __name__ == "__main__":
    paras = convert(open(sys.argv[1], encoding="utf-8").read())
    open(sys.argv[2], "w", encoding="utf-8").write("\n\n".join(p["text"] for p in paras) + "\n")
    print(f"{len(paras)} paragraphs, {sum(len(p['text']) for p in paras)} characters")
    for i, p in enumerate(paras, 1):
        if p["gap_before"]:
            print(f"silence before paragraph {i}: {' '.join(p['gap_before'])}")
        if p["gap_after"]:
            print(f"silence after paragraph {i}: {' '.join(p['gap_after'])}")
    print("parts began at paragraphs:", [1] + [i for i, p in enumerate(paras, 1) if p["part"]])
