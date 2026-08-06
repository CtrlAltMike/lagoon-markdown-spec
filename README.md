# Lagoon Markdown package format

Lagoon Markdown (`.lmd`) is an open, ZIP-based container for a UTF-8
Markdown document and its local images. It is a packaging format, not a new
Markdown dialect.

The current format version is **1**. The current specification revision is
**1.1**; specification revisions clarify version 1 without changing the
on-disk `formatVersion` value.

- [Read the v1 specification](SPEC.md)
- [Validate a manifest with JSON Schema](schema/lmd-v1.schema.json)
- [Inspect the minimal example](examples/basic)
- [Review the revision history](CHANGELOG.md)

## Identification

| Property | Value |
| --- | --- |
| Filename extension | `.lmd` |
| Media type | `application/vnd.ebbline.lagoon-markdown` |
| Uniform Type Identifier | `com.ebbline.lagoon-markdown` |

## Minimal package

```text
notes.lmd
├── lagoon.json
└── document.md
```

An `.lmd` file can be inspected with any ZIP utility. Rename a copy to `.zip`
if your utility relies on filename extensions.

## Implementing the format

Third-party readers and writers may implement this specification without
permission. Readers should preserve unrecognized manifest properties and safe
archive entries when rewriting a package so future extensions survive a
round trip.

## License

This specification, schema, and examples are available under the
[MIT License](LICENSE).
