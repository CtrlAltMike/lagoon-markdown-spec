# Lagoon Markdown package format

Lagoon Markdown (`.lmd`) is an open, ZIP-based container for a UTF-8 Markdown
document and its local images and media. It is a packaging format, not a new
Markdown dialect.

The current format version is **2**. The current specification revision is
**2.0**. Version 1 remains documented for compatibility at specification
revision **1.2**.

- [Read the current v2 specification](SPEC-v2.md)
- [Read the legacy v1 specification](SPEC.md)
- [Validate a v2 manifest with JSON Schema](schema/lmd-v2.schema.json)
- [Validate a v1 manifest with JSON Schema](schema/lmd-v1.schema.json)
- [Inspect the examples](examples/README.md)
- [Read the playback and Quick Look profile](PLAYBACK.md)
- [Read the Quick Look authoring guide](QUICK_LOOK_AUTHORING.md) — it is well
  worth reading before designing a package preview
- [Review template submission guidance](TEMPLATE_SUBMISSIONS.md)
- [Review the revision history](CHANGELOG.md)

## Canonical source

This repository is the sole canonical source for the Lagoon Markdown package
specification, its schemas, examples, and format-authoring guidance. Product
repositories and websites may link to or summarize the specification, but a
summary is non-normative. If another source conflicts with this repository,
this repository controls.

## Identification

| Property | Value |
| --- | --- |
| Filename extension | `.lmd` |
| Media type | `application/vnd.ebbline.lagoon-markdown` |
| Uniform Type Identifier | `com.ebbline.lagoon-markdown` |

## Minimal v2 package

```text
notes.lmd
├── lagoon.json
├── document.md
└── media/
    └── title.wav
```

An `.lmd` file can be inspected with any ZIP utility. Rename a copy to `.zip`
if your utility relies on filename extensions.

## Implementing the format

Third-party readers and writers may implement this specification without
permission. Readers should preserve unrecognized manifest properties and safe
archive entries when rewriting a package so future extensions survive a
round trip.

Agentic contributions are welcome. Work created or assisted by AI agents is
evaluated under the same technical standards as human-authored work. See
[Contributing](CONTRIBUTING.md#agentic-contributions) for the required
responsibility and disclosure policy.

## License

The specifications, schemas, examples, and guides are available under the
[MIT License](LICENSE).
