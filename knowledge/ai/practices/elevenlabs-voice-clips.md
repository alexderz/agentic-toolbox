# ElevenLabs voice clips with Eleven v4

- Source: ElevenLabs documentation:
  [Models](https://elevenlabs.io/docs/overview/models),
  [Eleven v4](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4),
  [Best practices: Prompting Eleven v4](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices#prompting-eleven-v4),
  [Create speech](https://elevenlabs.io/docs/api-reference/text-to-speech/convert),
  [Create dialogue](https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert),
  [Changelog, September 28, 2026](https://elevenlabs.io/docs/changelog),
  [API pricing](https://elevenlabs.io/pricing/api).
- Distilled: `2026-10-17`
- Live docs win: append `.md` to any docs URL for clean Markdown, or start
  from [llms.txt](https://elevenlabs.io/docs/llms.txt). ElevenLabs says
  Eleven v4 is under continuous development and its behavior can shift.

## What it is

Eleven v4 (`eleven_v4`) is the ElevenLabs text-to-speech model released on
September 28, 2026. It follows bracketed audio tags such as `[excited]` or
`[whispers]` to direct delivery. This note covers how to produce short,
pre-rendered voice clips with it: for example, game prompts and feedback
lines. It covers model choice, tags, settings, API calls, audio formats,
cost, a batch recipe, and pitfalls.

## When to read

Read this before you render speech clips with ElevenLabs, before you move a
pipeline from `eleven_multilingual_v2` or `eleven_v3` to `eleven_v4`, or
before you budget characters for a batch.

## Choose the model

| Model ID | Use it for | Price per 1K characters | Characters per request | Audio tags | Voice settings |
| --- | --- | --- | --- | --- | --- |
| `eleven_v4` | Pre-rendered clips, narration, character lines | $0.08 | 10,000 | Yes | Stability, Similarity |
| `eleven_v4_turbo` | Real-time agents, about 100 ms median latency | $0.04 | Not published | Yes | Stability, Similarity |
| `eleven_v3` | Previous expressive model | $0.08 | 5,000 | Yes | Stability |
| `eleven_multilingual_v2` | Long-form stability; API default model | $0.08 | 10,000 | Not documented | Stability, Similarity, Style, Speed, Speaker boost |
| `eleven_flash_v2_5` | Lowest latency and cost | $0.04 | 40,000 | Not documented | As Multilingual v2 |

For offline clips where quality matters more than latency, use `eleven_v4`.
The v4 Turbo variant is documented mainly for the Text to Dialogue WebSocket.

The following differences from `eleven_multilingual_v2` break a straight swap:

- Eleven v4 has only **Stability** and **Similarity**. Style and Speed are not
  available, and SSML is not supported, including `<break time="1s" />`.
  Control pauses with ellipses, punctuation, and tags instead.
- Eleven v4 follows audio tags. The docs describe tags for Eleven v4 and
  Eleven v3, not for Multilingual v2, which takes emotion from the wording.
- Eleven v4 accepts `language_code`. Multilingual v2 does not.
- Eleven v4 reproduces the source voice more faithfully, including flaws in
  its training audio. The same voice ID can sound different from v2 or v3.
- When the output language differs from the voice's own language, Eleven v4
  speaks without the voice's original accent.

## Write audio tags

Audio tags are free-form, natural-language instructions in square brackets.
They are part of the `text` field, not a separate parameter. Put a tag
immediately before the words it affects, or immediately after them for a
reaction such as `[giggles]`.

```text
[excited] Yes! You did it!
[gently, kindly] Oops, not that one. Let's try again.
[curious] How many glowing pumpkins can you count? [giggles]
```

The documented tags fall into three groups. The lists aren't exhaustive.

| Group | Examples |
| --- | --- |
| Delivery and emotion | `[excited]`, `[curious]`, `[whispers]`, `[sighs]`, `[laughs]`, `[sarcastic]`, `[mischievously]`, `[warmly]`, `[cheerfully]`, `[crying]` |
| Sound events | `[applause]`, `[clapping]`, `[gulps]`, `[gentle footsteps]`, `[leaves rustling]` |
| Direction | `[Quiet, measured narration]`, `[Quick, light, playful pace]`, `[strong French accent]`, `[sings]` |

To get reliable results, follow these rules:

- Describe the voice, not a scene. Eleven v4 generates both vocal delivery and
  sound effects, so an ambiguous tag can come out as a sound effect. Prefer
  `[low, gravelly voice]` to a word that names a sound.
- Match tags to the voice. A delivery already in the voice's training audio
  lands more readily. A calm narrator voice doesn't shout well, and a
  professional voice may not giggle convincingly.
- Use punctuation as part of the direction. Ellipses add pauses and weight,
  capital letters add emphasis, and exclamation marks add energy.
- Expect variation. ElevenLabs describes tag following as not yet perfect.
  Render two or three takes of an important line and keep the best one.

ElevenLabs documents no limit on the number of tags per request. Their own
examples use one tag per sentence or short paragraph.

## Set voice settings

| Setting | Range | Default | Effect |
| --- | --- | --- | --- |
| Stability | 0.0–1.0 | 0.5 | Lower values give more expressive, varied takes; higher values hold a steady, flatter delivery. |
| Similarity | 0.0–1.0 | 0.75 | Higher values follow the reference voice more closely, at some cost to naturalness. |

The two endpoints name these fields differently:

- Create speech: `voice_settings.stability` and `voice_settings.similarity_boost`.
- Create dialogue: `settings.stability` and `settings.similarity`.

Start at the defaults. If tags sound too flat, try a lower Stability, such
as 0.4. If a set of clips varies too much, try a higher value, such as 0.6,
and pass a fixed `seed`. These values are starting points, not vendor
guidance. A seed is best effort; it doesn't guarantee identical audio.

The current docs don't describe the Creative, Natural, and Robust stability
presets that the web app offered for Eleven v3. Use the numeric value.

## Call the API

Both endpoints accept `eleven_v4`. Use Create speech for one voice per clip,
and Create dialogue for several speakers in one clip. Read the key from the
environment. Never write it into a file, and never pass it as a command-line
argument, where other users can read it in the process list. The curl
examples feed the header on standard input with `-H @-` for that reason.

To render one clip as raw 16-bit PCM:

```bash
printf 'xi-api-key: %s\n' "$ELEVENLABS_API_KEY" |
curl -sS --fail-with-body -H @- \
  "https://api.elevenlabs.io/v1/text-to-speech/VOICE_ID?output_format=pcm_24000" \
  -H "Content-Type: application/json" \
  -d '{
        "text": "[excited] Yes! You did it!",
        "model_id": "eleven_v4",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75},
        "seed": 7
      }' \
  -o clip.pcm
```

To render a two-speaker exchange:

```bash
printf 'xi-api-key: %s\n' "$ELEVENLABS_API_KEY" |
curl -sS --fail-with-body -H @- \
  "https://api.elevenlabs.io/v1/text-to-dialogue?output_format=pcm_24000" \
  -H "Content-Type: application/json" \
  -d '{
        "model_id": "eleven_v4",
        "inputs": [
          {"text": "[curious] What is three plus four?", "voice_id": "VOICE_ID_A"},
          {"text": "[excited] Seven!", "voice_id": "VOICE_ID_B"}
        ],
        "settings": {"stability": 0.5, "similarity": 0.75}
      }' \
  -o dialogue.pcm
```

Keep the total dialogue text at or below 2,000 characters per request. The
API reference allows at most 10 distinct voices per request. The Text to
Dialogue overview says there is no speaker limit; follow the API reference.

To find voice IDs, call `GET /v2/voices`, which is paginated. The older
`GET /v1/voices` still answers. Voices with `category` set to `premade` are
the ElevenLabs stock voices. Voice Library voices from other creators are a
separate set, and the voices overview restricts their API use on the Free
plan.

To check usage, call `GET /v1/user/subscription` and read
`character_count` and `character_limit`.

To render one clip in Python with only the standard library, and wrap it as
WAV:

```python
import json, os, urllib.request, wave

def speak(voice_id, text, path, rate=24000):
    req = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
        f"?output_format=pcm_{rate}",
        data=json.dumps({
            "text": text,
            "model_id": "eleven_v4",
            "voice_settings": {"stability": 0.5, "similarity_boost": 0.75},
        }).encode(),
        headers={"xi-api-key": os.environ["ELEVENLABS_API_KEY"],
                 "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        pcm = resp.read()
    with wave.open(path, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(rate)
        w.writeframes(pcm)

speak("VOICE_ID", "[gently, kindly] Oops, not that one. Let's try again.", "oops.wav")
```

## Request a format and convert to OGG

Request `pcm_24000` or `wav_24000`. PCM output is signed 16-bit
little-endian (S16LE) with no header. The docs don't state the channel
count; the examples here assume mono, so check the length of the first clip
you render. Wrap it with Python's `wave` module, as in the
previous example, or let `ffmpeg` read it raw. Formats at 44.1 kHz,
`pcm_44100` and `wav_44100`, require the Pro plan or higher; 24 kHz is
enough for speech. MP3 and Opus output are also available. Rendering from PCM
avoids encoding twice.

To convert to OGG Vorbis, for example for a game engine that loads `.ogg`
sounds:

```bash
# From raw PCM:
ffmpeg -f s16le -ar 24000 -ac 1 -i clip.pcm -c:a libvorbis -q:a 5 clip.ogg
# From WAV, with loudness evened out across a set of clips:
ffmpeg -i clip.wav -af loudnorm=I=-16:TP=-1.5:LRA=11 -ar 44100 -ac 1 \
  -c:a libvorbis -q:a 5 clip.ogg
```

Request audio without `audio_effects` when you need PCM. Reverb and panning
produce stereo audio, and the API rejects them for `pcm_*` formats.

## Control cost

- Billing counts the characters in `text`. Assume that audio tags count too,
  because they are part of the text.
- Each request costs its full text. A retake of a line costs the line again.
- Render each line once, cache the file under a stable name, and skip files
  that already exist.
- Audition several voices on one short line before you render a full set.
- Before a run, add up the characters and stop when the total is over a
  budget you chose.
- Read `character_count` before and after a batch, and record the difference.
- `eleven_v4_turbo` costs half as much, but the docs route it through the
  Text to Dialogue WebSocket. The REST recipe in this note isn't documented
  for it.

Concurrency, not requests per minute, limits HTTP use. Plans allow from 2
(Free) to 15 (Scale) concurrent Multilingual v2 requests. The docs don't
list a v4 column. The response headers `current-concurrent-requests` and
`maximum-concurrent-requests` report your current state. Requests over the
limit wait in a queue. Retry HTTP 429 and 5xx responses with backoff.

## Run a batch from a phrase list

1. Write `phrases.json`: settings, voices, lines, and the clip list.

   ```json
   {
     "model_id": "eleven_v4",
     "output_format": "pcm_24000",
     "sample_rate": 24000,
     "voice_settings": {"stability": 0.5, "similarity_boost": 0.75},
     "seed": 7,
     "max_chars": 2000,
     "voices": {"guide": "VOICE_ID_A", "helper": "VOICE_ID_B"},
     "lines": {
       "1": "[cheerful] Which tower is taller? Pull the lever to see the answers!",
       "2": "[excited] Yes! You did it!",
       "2-untagged": "Yes! You did it!"
     },
     "clips": [["guide", "1"], ["helper", "1"], ["guide", "2"], ["guide", "2-untagged"]]
   }
   ```

1. Save the following script as `render.py`. The script skips existing
   clips, refuses to start when the planned characters exceed `max_chars`,
   retries HTTP 429, 5xx, and network errors with backoff, and writes each
   WAV atomically. A retried request can be billed again, so `max_chars`
   caps the planned text, not the billed total. Run one copy at a time;
   two copies share the same temporary file names.

   ```python
   import json, os, sys, time, urllib.error, urllib.request, wave

   API = "https://api.elevenlabs.io"

   def call(method, path, body=None):
       headers = {"xi-api-key": os.environ["ELEVENLABS_API_KEY"]}
       data = None
       if body is not None:
           headers["Content-Type"] = "application/json"
           data = json.dumps(body).encode()
       req = urllib.request.Request(API + path, data=data, headers=headers, method=method)
       with urllib.request.urlopen(req, timeout=120) as resp:
           return resp.read()

   def used():
       return json.loads(call("GET", "/v1/user/subscription"))["character_count"]

   def wait_for(e, i):
       try:
           return float(e.headers.get("Retry-After"))
       except (TypeError, ValueError):
           return 2 ** i

   def render(cfg, voice_id, text, attempts=5):
       path = f"/v1/text-to-speech/{voice_id}?output_format={cfg['output_format']}"
       body = {"text": text, "model_id": cfg["model_id"],
               "voice_settings": cfg["voice_settings"], "seed": cfg["seed"]}
       for i in range(attempts):
           last = i == attempts - 1
           try:
               return call("POST", path, body)
           except urllib.error.HTTPError as e:
               if (e.code != 429 and e.code < 500) or last:
                   sys.exit(f"HTTP {e.code}: {e.read()[:300]!r}")
               time.sleep(wait_for(e, i))
           except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
               if last:
                   sys.exit(f"network error: {e}")
               time.sleep(2 ** i)

   cfg = json.load(open(sys.argv[1]))
   if cfg["output_format"] != f"pcm_{cfg['sample_rate']}":
       sys.exit("output_format must be pcm_<sample_rate>; this script writes raw PCM")
   out = sys.argv[2]
   os.makedirs(out, exist_ok=True)
   todo = [(v, l, os.path.join(out, f"{v}-{l}.wav")) for v, l in cfg["clips"]]
   todo = [t for t in todo if not os.path.exists(t[2])]
   chars = sum(len(cfg["lines"][l]) for _, l, _ in todo)
   if chars > cfg["max_chars"]:
       sys.exit(f"{chars} characters is over max_chars")
   before = used()
   for voice, line, dest in todo:
       pcm = render(cfg, cfg["voices"][voice], cfg["lines"][line])
       with wave.open(dest + ".part", "wb") as w:
           w.setnchannels(1); w.setsampwidth(2); w.setframerate(cfg["sample_rate"])
           w.writeframes(pcm)
       os.replace(dest + ".part", dest)
       print("wrote", dest)
   print("characters used by this run:", used() - before)
   ```

1. Run the script.

   ```bash
   python3 render.py phrases.json clips/
   ```

1. Convert the WAV files to OGG.

   ```bash
   for f in clips/*.wav; do
     ffmpeg -loglevel error -i "$f" -c:a libvorbis -q:a 5 "${f%.wav}.ogg"
   done
   ```

## Pitfalls

- Without `model_id`, Create speech uses `eleven_multilingual_v2` and Create
  dialogue uses `eleven_v3`. Always send `model_id`.
- `style`, `speed`, and SSML `<break>` don't apply to Eleven v4. Don't port
  them from a v2 pipeline and expect an effect.
- A tag that names a sound can render as a sound effect. A tag the voice
  can't perform can render flat. Listen to every clip before you ship it.
- With a non-English voice, English output loses the original accent by
  design. Pick a voice whose own language matches the output.
- The API returns HTTP 400 for `pcm_*` output with reverb or panning.
- A 44.1 kHz PCM or WAV request fails below the Pro plan. Use 24 kHz.
- Library voices can require a paid plan. A clip pipeline that must run on
  any plan uses stock voices.
- Behavior shifts as ElevenLabs updates Eleven v4. Pin the clips you ship as
  files, not as regenerate-on-build steps, and re-audition after updates.
- Numbers and symbols are normalized automatically (`apply_text_normalization`
  is `auto`). For predictable reading, write numbers as words: "three plus
  four", not "3 + 4".

## Unknown

- Whether every request example here works unchanged. They follow the API
  reference, but they were not run against the live API when this note was
  distilled. The docs disagree on one point: the Models page routes
  `eleven_v4` through Text to Dialogue, and the help pages also name Create
  speech.
- Whether audio-tag characters are billed. This note assumes they are.
- The per-request character limit and concurrency limit for
  `eleven_v4_turbo`, and v4 concurrency per plan.
- Whether the Opus formats return an Ogg container or raw Opus packets.
- The channel count of PCM output. The examples assume mono.
- How reliably each stock voice follows each tag. Test your voices.

## Do not

- Never put an API key in a file, a command-line argument, a log, or this
  repository. Read it from `ELEVENLABS_API_KEY` at run time.
- Never install ElevenLabs CLI skills or marketplace packs from this note.
  Call the HTTP API directly.
- Never remint this note as a skill. Link to it instead.
