# Lagoon Markdown package format, version 1

Status: stable

Format version: `1`

Specification revision: `1.1`

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHOULD**, **SHOULD NOT**,
and **MAY** in this document are to be interpreted as normative requirements.

## 1. Scope

A Lagoon Markdown package is a ZIP archive containing one UTF-8 Markdown
document, a JSON manifest, and optional local images or extension data. The
format does not define a Markdown dialect. A consumer decides which Markdown
features it renders.

Two workflows use the same container:

- A `document` is editable content.
- A `template` is a protected starter from which an application can create a
  separate `document` copy.

Protection is an application behavior, not encryption or access control.

## 2. Package layout

A typical package has this layout:

```text
example.lmd
├── lagoon.json
├── document.md
├── thumbnail.webp
└── assets
    ├── cover.png
    └── diagram.svg
```

`lagoon.json` and `document.md` are REQUIRED at the archive root. Asset files
SHOULD be stored below `assets/`. A thumbnail, when declared, MUST be a
root-level file.

Writers MUST store regular files only. They MUST NOT add explicit directory,
symbolic-link, hard-link, device, or other special entries. ZIP tools do not
need directory entries in order to store paths such as `assets/cover.png`.

Readers MUST ignore unrecognized safe files outside reserved paths and
namespaces such as `lagoon.json`, `document.md`, a declared thumbnail, and
`assets/`. A reader that rewrites a package SHOULD preserve those unrecognized
files byte-for-byte unless the user deliberately removes them. Section 7
defines the stricter rules for the reserved `assets/` namespace.

## 3. ZIP profile

A conforming v1 package MUST meet all of these requirements:

| Constraint | Requirement |
| --- | --- |
| Maximum archive size | 100 MiB (104,857,600 bytes) |
| Maximum entry count | 128, including required files |
| Maximum expanded size | 200 MiB (209,715,200 bytes) |
| Compression | STORE (method 0) or DEFLATE (method 8) only |
| Encryption | Prohibited |
| Multi-disk archives | Prohibited |
| ZIP64 | Prohibited |

`document.md` MUST NOT exceed 5 MiB (5,242,880 bytes). Each other regular file
MUST NOT exceed 25 MiB (26,214,400 bytes), with the smaller thumbnail limit in
section 6 taking precedence.

An implementation SHOULD store already-compressed raster images rather than
deflating them again.

## 4. Entry paths

Writers MUST encode every entry path in Unicode Normalization Form C (NFC).
Readers MUST normalize each path to NFC before applying the remaining path
requirements, detecting duplicates, or matching a manifest path to an archive
entry. A reader MAY warn about a non-NFC source path, but MUST NOT reject it
solely for its normalization form when the normalized path is otherwise safe
and unique.

Every normalized entry path MUST:

- be a non-empty relative path encoded as UTF-8;
- use `/` as its only separator;
- contain no empty, `.` (current-directory), or `..` (parent-directory)
  component;
- contain no control character;
- not begin with `/` or `\`; and
- not end with `/`.

Every normalized path MUST be unique. Readers MUST reject an archive containing
duplicate normalized paths. Matching of manifest paths to normalized archive
entries is case-sensitive.

## 5. Manifest

`lagoon.json` MUST contain a UTF-8 JSON object. This example shows every v1
field:

```json
{
  "format": "com.ebbline.lagoon-markdown",
  "formatVersion": 1,
  "role": "template",
  "entry": "document.md",
  "title": "Project Brief",
  "description": "A concise project brief.",
  "thumbnail": "thumbnail.webp",
  "creator": "Example Author",
  "license": "CC-BY-4.0"
}
```

### 5.1 Fields

| Field | Type | Requirement |
| --- | --- | --- |
| `format` | string | REQUIRED. MUST equal `com.ebbline.lagoon-markdown`. |
| `formatVersion` | integer | REQUIRED. MUST equal `1`. |
| `role` | string | REQUIRED. MUST be `document` or `template`. |
| `entry` | string | REQUIRED. MUST equal `document.md`. |
| `title` | string | REQUIRED. MUST contain 1–120 user-perceived characters after requiring at least one non-whitespace character. |
| `description` | string | Optional for documents; REQUIRED and non-blank for templates. MUST NOT exceed 500 user-perceived characters. |
| `thumbnail` | string | Optional for documents; REQUIRED for templates. See section 6. |
| `creator` | string | Optional creator or publisher attribution. |
| `license` | string | Optional license identifier or short license statement. |

The limits on `title` and `description` count Unicode extended grapheme
clusters. Leading and trailing whitespace count toward the maximum but do not
satisfy the non-blank requirement.

The JSON numeric values `1` and `1.0` are equal under JSON Schema's mathematical
integer semantics. Writers SHOULD serialize `formatVersion` in its canonical
form as the JSON token `1`.

### 5.2 Extensions

A manifest MAY contain additional properties with any JSON value. Writers
MUST NOT reuse a v1 field name with incompatible meaning. Readers MUST ignore
unrecognized properties. A reader that rewrites a supported package SHOULD
preserve them without changing their JSON value.

The accompanying [JSON Schema](schema/lmd-v1.schema.json) checks portable
structural requirements. It intentionally omits `maxLength` for `title` and
`description` because JSON Schema measures Unicode code points while this
specification measures extended grapheme clusters. Implementations MUST
perform an additional Unicode-aware check for the 120- and 500-character
limits. The schema documents this requirement with `$comment` annotations.

## 6. Thumbnails

When `thumbnail` is present:

- its value MUST be a valid path naming an existing root-level regular file;
- the value MUST NOT contain `/`;
- the file MUST be PNG (`.png`), JPEG (`.jpg` or `.jpeg`), or WebP (`.webp`);
- the extension and encoded image type MUST agree; and
- the file MUST NOT exceed 5 MiB (5,242,880 bytes).

Thumbnail-extension matching is ASCII case-insensitive; for example,
`thumbnail.png` and `COVER.PNG` are both valid names when their contents are
PNG images.

SVG and animated GIF thumbnails are not permitted. A 1200 × 630 pixel image
(about 1.91:1) is RECOMMENDED for catalog cards. Other dimensions are valid.
Authors SHOULD keep important content centered because consumers may apply a
cover crop. For faster downloads and decoding, authors SHOULD prefer WebP and
target a file size of 500 KiB (512,000 bytes) or less. This performance target
is a recommendation; the 5 MiB limit above remains the conformance ceiling.

## 7. Assets

The `assets/` namespace is reserved for images. Every regular file whose
normalized path begins with `assets/` MUST be a PNG, JPEG, GIF, WebP, or passive
SVG image. The filename extension and encoded type MUST agree. Readers MUST
reject a package containing an unsupported or invalid file below `assets/`;
for example, `assets/notes.txt` is invalid. Extension data that is not an image
MUST use a different safe namespace.

Asset paths may be referenced from `document.md` with ordinary relative
Markdown URLs, for example:

```markdown
![Diagram](assets/diagram.svg)
```

Remote URLs may remain in the Markdown, but network loading is a reader policy
and is not guaranteed by this format.

### 7.1 Raster-image safety profile

For compatibility with Lagoon's v1 reader, a raster image MUST decode to at
least one frame and MUST meet these limits:

- no more than 500 frames;
- no more than 64,000,000 pixels in any frame; and
- no more than 256,000,000 pixels across all frames.

Readers MAY enforce lower resource limits when necessary for their platform.

### 7.2 Passive SVG profile

An SVG asset MUST be valid UTF-8, contain an `svg` root element, and be no
larger than 8 MiB. It MUST NOT contain active or remotely loaded content,
including:

- `script`, `foreignObject`, `iframe`, `object`, or `embed` elements;
- event-handler attributes such as `onclick`;
- `javascript:` or `vbscript:` URLs;
- `data:text/html` URLs;
- CSS `@import`; or
- remote or scheme-relative URLs in CSS `url()`, `href`, or `xlink:href`.

Readers SHOULD parse and sanitize SVG defensively even after these checks.

## 8. Roles and copying

A reader SHOULD open a `document` for editing. It SHOULD treat a `template` as
read-only source material and offer an explicit copy operation. A copied
template MUST use role `document`; the original template MUST remain
unchanged.

`creator` and `license` are optional format fields. A distribution catalog MAY
require them as a separate publishing policy.

## 9. Versioning and forward compatibility

`formatVersion` identifies the package format, not the Markdown syntax. A v1
reader MUST NOT silently rewrite a package whose `formatVersion` it does not
support.

Future compatible metadata can use additional manifest properties and safe
archive entries. This is why round-trip preservation is strongly recommended.
A change that alters required paths, validation rules, or field meanings
requires a new integer format version.

## 10. Security considerations

Readers MUST validate the ZIP structure and every path before extracting any
entry. They MUST apply compressed, expanded, per-entry, and entry-count limits
while reading rather than only after extraction. They MUST NOT follow links or
write outside an isolated destination.

Markdown and SVG are untrusted input. Rendering applications SHOULD sanitize
raw HTML, restrict executable content, and make remote-resource loading an
explicit policy decision.

## 11. Recovery and interoperability

An `.lmd` file is an ordinary ZIP archive. Users can inspect a copy with any
ZIP utility and recover `document.md` and its images without Lagoon. The
`.lmd` extension is not a security boundary and does not imply encryption.
