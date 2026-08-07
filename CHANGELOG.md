# Specification revision history

A specification revision identifies a publication of the written standard for
a format version. It does not itself change the `formatVersion` value stored in
`lagoon.json`. Revisions normally clarify an existing format; any exceptional
pre-adoption correction is recorded explicitly below.

## Revision 2.2 — 2026-08-07

- Add optional opaque sRGB `backgroundColor` manifest metadata for the
  preferred on-screen document canvas.
- Clarify that readers may ignore the preference, should select readable
  content colors when honoring it, and need not apply it to thumbnails,
  printing, PDF, standalone HTML, or application chrome.
- Add Quick Look authoring guidance and a v2 example background without
  changing package `formatVersion`.
- Define deterministic promotion of a same-named v1 extension during an
  upgrade, rejecting invalid values instead of discarding them.

## Revision 2.1 — 2026-08-07

- Restore the v1 rule that every regular file other than `document.md` has a
  25 MiB per-entry limit. Revision 2.0 accidentally narrowed this wording to
  image and media entries despite permitting safe extension files.
- State explicitly that both the 5 MiB thumbnail limit and the 8 MiB passive
  SVG limit take precedence over the general 25 MiB entry limit.
- Record the restored general entry limit as a pre-adoption correction; the
  package `formatVersion` remains `2`.

## Revision 1.3 — 2026-08-07

- State explicitly that both the 5 MiB thumbnail limit and the 8 MiB passive
  SVG limit take precedence over the general 25 MiB entry limit.
- Correct the thumbnail requirement list's conjunction punctuation without
  changing conformance.

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
