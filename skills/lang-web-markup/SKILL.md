---
name: lang-web-markup
description: use this when writing or reviewing HTML or CSS — *.html, *.htm, *.css, *.scss, or a page's markup/a11y/style. do not use as the primary skill for *.tsx / *.jsx logic (load lang-js-ts first; this may be the second skill).
---

# HTML / CSS

One skill for markup and style. Compatible with `tdd`,
`verify-before-done`, `pr-review`, `security-hardening`. No
`scripts/`. May be the second skill next to `lang-js-ts`. Cap is still 2.

## Iron law

**Semantic HTML first. CSS you can delete. Keyboard and contrast are
not optional.**

## Tooling / verify

- Open the page if you can. Tab through the new control.
- Check heading order on the changed region.
- axe / Lighthouse only if the repo already runs them.

## Idioms a linter misses

- Real elements: `button`, `a`, `label for`, headings in order. No
  clickable `div`.
- Images have `alt` (empty only when decorative).
- Forms: label every control. Errors associated with fields.
- CSS: cascade + logical properties. No `!important` arms race.
- `:focus-visible`. Do not `outline: none` without a replacement.
- Color is not the only signal.
- `prefers-reduced-motion` when adding animation.

## Errors

- Broken heading levels and unlabeled inputs are bugs, not polish.

## Testing

- Keyboard path for every new control (Tab, Enter/Space, Esc).
- Responsive check at the project's existing breakpoints if you can
  render.

## PR review

- New clickable `div` / `span`: reject.
- `target=_blank` without `rel="noopener noreferrer"`: reject.
- New `!important`: reject unless it is undoing a third-party hole and
  you say so.
- Contrast of new text on its actual background.

## Security

- `innerHTML` of untrusted strings is a `lang-js-ts` Never. Markup
  templates do not concatenate user text.
- No unexpected third-party CSS/font network from a static page
  without asking.

## Always

- Semantic element. Labeled control. Visible focus.

## Ask first

- A new CSS framework.
- Disabling zoom / `user-scalable=no`.

## Never

- Clickable non-interactive elements as the primary control.
- Removing focus outlines with no replacement.
- Inline styles as the design system.

## Red flags

- "It's just a div with an onClick"
- "We'll fix a11y later"
- "outline: none looks cleaner"
