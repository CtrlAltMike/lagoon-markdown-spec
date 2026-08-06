# Specification revision history

Specification revisions clarify an existing format version. They do not
change the `formatVersion` value stored in `lagoon.json`.

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
