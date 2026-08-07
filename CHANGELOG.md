# Specification revision history

A specification revision identifies a publication of the written standard for
a format version. It does not itself change the `formatVersion` value stored in
`lagoon.json`. Revisions normally clarify an existing format; any exceptional
pre-adoption correction is recorded explicitly below.

## Revision 2.0 — 2026-08-07

- Publish Lagoon Markdown package format version 2.
- Reserve `media/` for packaged audio, video, and WebVTT captions while keeping
  `assets/` image-only.
- Define supported media families and deterministic signature validation.
- Define local video posters, the Quick Look title-track profile, and Lagoon's
  optional viewport-video playback profile.
- Retain the v1 archive limits and manifest identity.

## Revision 1.2 — 2026-08-07

- Require every declared v1 thumbnail to use a square 1:1 pixel canvas.
- Clarify that a manifest thumbnail and a lead image inside `document.md` are
  separate compositions.
- Record this as a pre-adoption correction rather than a general precedent for
  changing stable validation rules in place.

## Revision 1.1 — 2026-08-06

- Document that the JSON Schema intentionally leaves extended-grapheme-cluster
  length limits to implementations.
- Recommend the canonical JSON token `1` for `formatVersion` while recognizing
  JSON Schema's mathematical integer semantics.
- Accept uppercase and mixed-case thumbnail filename extensions.
- Define how readers handle individual non-NFC paths and normalized collisions.
- Reserve `assets/` for supported image files and require other extension data
  to use a different safe namespace.

## Revision 1.0 — 2026-08-06

- Initial publication of Lagoon Markdown package format version 1.
