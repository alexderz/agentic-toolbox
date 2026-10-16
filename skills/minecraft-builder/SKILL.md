---
name: minecraft-builder
description: use this when a model builds, reviews, or plans a Minecraft Bedrock structure and needs block names or block states. It supplies the Bedrock block catalog so the model uses the tools it was given instead of remembered names or numeric ids.
---

# Minecraft builder

Load this before choosing a Bedrock block or a block state. The test is whether the model can build with the catalog, not whether it remembers names.

## Catalog

Read [references/blocks.json](references/blocks.json). That file is the block list.

- `format` is `minecraft-builder-blocks/1`.
- `edition` is `bedrock`.
- `catalogVersion` is `1.26.30`. A newer server may add blocks. A name that is not in this file is not available.
- Each `blocks[]` entry has `id` (`minecraft:<name>`), `states`, `transparent`, `light`, and `box`.
- `states` is `{}` when the block has no placement states. Otherwise each key maps to the values this catalog allows.
- `transparent` is true when the block does not hide what is behind it.
- `light` is the light level the block emits, from 0 through 15.
- `box` is `block` for a full cube, `empty` for no collision, or another shape name from the catalog.

Do not use protocol state ids, legacy data values, or a Java block name that this file does not list. Bedrock often uses a different name than Java. Oak signs in this catalog are `minecraft:standing_sign` and `minecraft:wall_sign`, not `oak_sign`.

## How to pick a block

1. Find the entry by `id`. If it is missing, pick another block from the file. Do not invent a name.
2. If `states` is `{}`, place the block with no states.
3. If `states` is not empty, set only keys listed for that block, and only to a listed value.
4. Leave a state unset only when the placement tool says the default is valid. Do not send a value that is not in the list.

## State meanings

Use these meanings only when that key is listed for the block.

| Key | Values | Meaning |
| --- | --- | --- |
| `facing_direction` | 0, 1, 2, 3, 4, 5 | 2 north, 3 south, 4 west, 5 east. 0 is down and 1 is up when the block lists them. A ladder or wall sign faces away from the block it is attached to. |
| `minecraft:cardinal_direction` | `north`, `south`, `west`, `east` | Named horizontal facing. |
| `pillar_axis` | `x`, `y`, `z` | Axis of a log, pillar, or similar block. |
| `minecraft:vertical_half` | `bottom`, `top` | Which half of the block space. |
| `upside_down_bit` | 0, 1 | 1 is the upside-down form, used by stairs. |
| `weirdo_direction` | 0, 1, 2, 3 | Rotation used by stairs and similar blocks. Do not treat these numbers as `facing_direction`. |
| `open_bit`, `lit`, `powered_bit`, `hanging` | 0 or 1, or `true` or `false` when listed | Off or on. |
| `ground_sign_direction` | 0 through 15 | Standing-sign rotation, 16 steps. |
| `direction` | 0 through 15 | Standing rotation for blocks that list it. |

## Operator blocks

`minecraft:command_block`, `minecraft:chain_command_block`, `minecraft:repeating_command_block`, `minecraft:structure_block`, `minecraft:jigsaw`, `minecraft:allow`, and `minecraft:deny` are in the catalog because they exist. Do not place them unless the task explicitly allows those operator blocks.

## Source

Derived from PrismarineJS `minecraft-data` Bedrock `1.26.30` `blocks.json` and `blockStates.json`. The raw protocol tables are not copied. Numeric state ids are omitted on purpose.

Done when every block id and every state value in the plan appears in `references/blocks.json` for that block.
