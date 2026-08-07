# Lagoon Markdown package format, version 2

Status: stable

Format version: `2`

Specification revision: `2.1`

> **Authoring companion:**
> [Authoring `.lmd` Documents for Quick Look](QUICK_LOOK_AUTHORING.md) is well
> worth reading before publishing a package. It covers square thumbnails,
> first-screen composition, and media ordering. The guide is non-normative;
> this specification remains the format contract.

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHOULD**, **SHOULD NOT**,
and **MAY** in this document are to be interpreted as normative requirements.

## 1. Scope

A Lagoon Markdown package is a ZIP archive containing one UTF-8 Markdown
document, a JSON manifest, and optional local images, audio, video, captions,
posters, or extension data. The format does not define a Markdown dialect. A
consumer decides which Markdown and media syntax it renders.

Two workflows use the same container:

- A `document` is editable content.
- A `template` is protected starter material from which an application can
  create a separate `document` copy.

Protection is an application behavior, not encryption or access control.

Version 2 extends version 1 by reserving `media/` and defining packaged audio,
video, and WebVTT captions. It retains the manifest identity and archive limits
from version 1.

## 2. Package layout

A typical v2 package has this layout:

```text
example.lmd
├── lagoon.json
├── document.md
├── thumbnail.webp
├── assets/
│   ├── cover.png
│   ├── diagram.svg
│   └── interview-poster.webp
└── media/
    ├── title-track.m4a
    ├── interview.mp4
    └── interview.vtt
```

`lagoon.json` and `document.md` are REQUIRED at the archive root. Image files
and video posters SHOULD be stored below `assets/`. Audio, video, and caption
files MUST be stored below `media/`. A thumbnail, when declared, MUST be a
root-level file.

Writers MUST store regular files only. They MUST NOT add explicit directory,
symbolic-link, hard-link, device, or other special entries. ZIP tools do not
need directory entries to store paths such as `media/title-track.m4a`.

Readers MUST ignore unrecognized safe files outside reserved paths and
namespaces such as `lagoon.json`, `document.md`, a declared thumbnail,
`assets/`, and `media/`. A reader that rewrites a package SHOULD preserve those
unrecognized files byte-for-byte unless the user deliberately removes them.
Sections 7 and 8 define stricter rules for the reserved namespaces.

## 3. ZIP profile

A conforming v2 package MUST meet all of these requirements:

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
MUST NOT exceed 25 MiB (26,214,400 bytes). The 5 MiB thumbnail limit in
section 6 and the 8 MiB SVG limit in section 7.2 take precedence.

Writers SHOULD use ZIP method STORE for raster-image and media formats whose
payloads are already compressed rather than deflating them again.

## 4. Entry paths

Writers MUST encode every entry path in Unicode Normalization Form C (NFC).
Readers MUST normalize each path to NFC before applying the remaining path
requirements, detecting duplicates, or matching a manifest or document path
to an archive entry. A reader MAY warn about a non-NFC source path, but MUST
NOT reject it solely for its normalization form when the normalized path is
otherwise safe and unique.

Every normalized entry path MUST:

- be a non-empty relative path encoded as UTF-8;
- use `/` as its only separator;
- contain no empty, `.` (current-directory), or `..` (parent-directory)
  component;
- contain no control character;
- not begin with `/` or `\`; and
- not end with `/`.

Every normalized path MUST be unique. Readers MUST reject an archive containing
duplicate normalized paths. Matching is case-sensitive.

## 5. Manifest

`lagoon.json` MUST contain a UTF-8 JSON object. This example shows every v2
field:

```json
{
  "format": "com.ebbline.lagoon-markdown",
  "formatVersion": 2,
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
| `formatVersion` | integer | REQUIRED. MUST equal `2`. |
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

The JSON numeric values `2` and `2.0` are equal under JSON Schema's mathematical
integer semantics. Writers SHOULD serialize `formatVersion` in its canonical
form as the JSON token `2`.

### 5.2 Extensions

A manifest MAY contain additional properties with any JSON value. Writers
MUST NOT reuse a v2 field name with incompatible meaning. Readers MUST ignore
unrecognized properties. A reader that rewrites a supported package SHOULD
preserve them without changing their JSON value.

The accompanying [JSON Schema](schema/lmd-v2.schema.json) checks portable
structural requirements. It intentionally omits `maxLength` for `title` and
`description` because JSON Schema measures Unicode code points while this
specification measures extended grapheme clusters. Implementations MUST
perform an additional Unicode-aware check for the 120- and 500-character
limits. Image dimensions and archive contents also require checks outside JSON
Schema.

## 6. Thumbnails

When `thumbnail` is present:

- its value MUST be a valid path naming an existing root-level regular file;
- the value MUST NOT contain `/`;
- the file MUST be PNG (`.png`), JPEG (`.jpg` or `.jpeg`), or WebP (`.webp`);
- the extension and encoded image type MUST agree;
- the decoded pixel width MUST equal the decoded pixel height; and
- the file MUST NOT exceed 5 MiB (5,242,880 bytes).

Thumbnail-extension matching is ASCII case-insensitive. SVG and animated GIF
thumbnails are not permitted. A thumbnail MUST use a square 1:1 canvas because
Finder and Quick Look expect square package artwork.

The manifest thumbnail is distinct from a lead image rendered inside
`document.md`. A lead image may use any dimensions allowed by section 7 and
often benefits from a wide composition. For faster downloads and decoding,
authors SHOULD prefer WebP and target a thumbnail file size of 500 KiB
(512,000 bytes) or less. This performance target is a recommendation; the
5 MiB limit remains the conformance ceiling.

## 7. Assets

The `assets/` namespace is reserved for images and video posters. Every regular
file whose normalized path begins with `assets/` MUST be a PNG, JPEG, GIF,
WebP, or passive SVG image. The filename extension and encoded type MUST agree.
Readers MUST reject a package containing an unsupported or invalid file below
`assets/`.

Asset paths may be referenced from `document.md` with ordinary relative URLs,
for example:

```markdown
![Diagram](assets/diagram.svg)
```

A local video poster SHOULD also resolve to an image below `assets/`.

### 7.1 Raster-image safety profile

A raster image MUST decode to at least one frame and MUST meet these limits:

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

## 8. Media

The `media/` namespace is reserved for audio, video, and WebVTT captions. Every
regular file whose normalized path begins with `media/` MUST use one of the
extensions in the following table and MUST satisfy the corresponding signature
profile. Extension matching is ASCII case-insensitive.

| Family | Extensions | Deterministic validation profile |
| --- | --- | --- |
| MPEG audio | `.mp3` | An MPEG audio frame header, optionally following a valid ID3v2 header |
| MPEG-4 audio | `.m4a` | ISO Base Media File Format header with a valid leading `ftyp` box |
| AAC | `.aac` | Valid ADTS header and frame length |
| Waveform audio | `.wav` | `RIFF` followed by `WAVE` at byte offset 8 |
| AIFF | `.aif`, `.aiff` | `FORM` followed by `AIFF` at byte offset 8 |
| AIFF-C | `.aifc` | `FORM` followed by `AIFC` at byte offset 8 |
| MPEG-4 video | `.mp4`, `.m4v` | ISO Base Media File Format header with a valid leading `ftyp` box |
| QuickTime video | `.mov` | ISO Base Media File Format `ftyp`, or a valid leading QuickTime `moov`, `mdat`, `wide`, `free`, `skip`, or `pnot` atom |
| WebM video | `.webm` | EBML header beginning `1A 45 DF A3` with a nonzero size descriptor |
| WebVTT captions | `.vtt` | UTF-8, with an optional UTF-8 BOM, beginning `WEBVTT` followed by whitespace or end of file |

Readers MUST reject unsupported, malformed, or extension-disguised entries
below `media/`. Passing the deterministic profile does not guarantee that a
platform can decode every codec carried by a permitted container. A consumer
MAY present an unavailable-media state when its media stack cannot play an
otherwise conforming file.

Inline `data:` audio and video are not part of version 2. Media must be a local
file or a remote URL interpreted by the consumer. Remote URLs are not package
entries, need not be downloaded by writers, and remain subject to each
consumer's network policy.

### 8.1 Document references

A file's presence below `media/` does not make it visible or playable by
itself. `document.md` determines presentation order and meaning. Consumers MAY
support relative media references in sanitized HTML `audio`, `video`, `source`,
and `track` elements or in a Markdown extension. A relative fragment or query
component is part of the document reference, not the archive entry name.

Writers that package local references SHOULD:

- ignore examples inside inline and fenced code;
- deduplicate references to the same source file;
- choose collision-safe archive paths without overwriting existing entries;
- preserve media fragments and queries when rewriting a reference;
- place audio, video, and captions below `media/`;
- place local video posters below `assets/`; and
- leave remote URLs unchanged.

Unreferenced packaged files remain ordinary archive entries and SHOULD remain
invisible to the document renderer. A reader that rewrites a package SHOULD
preserve safe unrecognized or unreferenced entries unless the user deliberately
removes them.

## 9. Roles and copying

A reader SHOULD open a `document` for editing. It SHOULD treat a `template` as
read-only source material and offer an explicit copy operation. A copied
template MUST use role `document`; the original template MUST remain unchanged.

`creator` and `license` are optional format fields. A distribution catalog MAY
require them as a separate publishing policy.

## 10. Versioning and compatibility

`formatVersion` identifies the package format, not the Markdown syntax. A v1
reader MUST reject a v2 manifest without rewriting the archive. A reader that
supports v1 and v2 MAY open a v1 package, but a writer that introduces packaged
media under the reserved `media/` namespace MUST set `formatVersion` to `2`.

Future compatible metadata can use additional manifest properties and safe
archive entries. A change that alters required paths, reserved namespaces,
validation rules, or field meanings requires a new integer format version.
Revision 2.1's restoration of v1's general per-entry limit is an explicit
pre-adoption correction to an internal v2.0 regression; it is not a general
precedent for changing a stable format in place.

## 11. Security and privacy considerations

Readers MUST validate the ZIP structure and every path before extracting any
entry. They MUST apply compressed, expanded, per-entry, and entry-count limits
while reading rather than only after extraction. They MUST NOT follow links or
write outside an isolated destination.

Markdown, SVG, captions, and media metadata are untrusted input. Rendering
applications SHOULD sanitize raw HTML, restrict executable content, and make
remote-resource loading an explicit policy decision. A local preview mode MAY
block all remote media, frames, and connections while retaining packaged-media
playback.

The reference Lagoon and Quick Look behavior is documented separately in
[PLAYBACK.md](PLAYBACK.md). Those application behaviors do not change package
conformance for third-party readers.

## 12. Recovery and interoperability

An `.lmd` file is an ordinary ZIP archive. Users can inspect a copy with any
ZIP utility and recover `document.md`, images, audio, video, and captions
without Lagoon. The `.lmd` extension is not a security boundary and does not
imply encryption.

Third-party readers and writers may implement this specification without
permission.
