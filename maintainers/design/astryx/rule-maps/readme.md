# Change map (light pass) — `README.md`

Item: DER-775. People doc: light pass per `maintainers/writing-standard.md` Rule maps step 6.

Old: `README.md` at c82318b. New: [`README.md`](../../../../README.md).

| Old L | Change | Source |
| --- | --- | --- |
| 47 (`ui` bundle row) | Adds `astryx` to the `ui` bundle and one sentence on when it applies | manager ruling 8 |
| after 115 (`ui-craft` id row) | New `astryx` ownership row: first-party MIT body, upstream MIT facts, pin in SOURCES | manager ruling 8 |

No other line changed. The licence line (L12–14) is unchanged: the new body is MIT, the
repository default. `docs-google-style` was the style reference.

r1 review (DER-775 r1 finding 11): L116 (`astryx` ownership row) "No CLI, plugin, scripts, hooks or
network" became "No CLI, plugin, scripts or hooks. The skill itself makes no network call."
