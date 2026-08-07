# Authoring `.lmd` Documents for Quick Look

Quick Look is often the first experience someone has with an `.lmd` document.
A strong preview should communicate the document's identity and purpose without
requiring the reader to open Lagoon.

This guide describes practical authoring techniques for composing that preview
effectively.

> This is non-normative authoring guidance. Quick Look dimensions and rendering
> can vary with macOS, window size, display scale, accessibility settings, and
> future system updates. The [LMD specification](SPEC-v2.md) remains
> authoritative for package structure and behavior.

## Thumbnail and lead image serve different purposes

The manifest `thumbnail` and the first image in `document.md` should not be
treated as the same artwork.

The manifest thumbnail must be **square (1:1)** in every LMD format version
because Finder and Quick Look use it as package artwork. The lead image is
rendered inside the document preview and generally works best as a **wide
banner, around 3:1 or wider**.

A package may therefore benefit from two related compositions:

- a square thumbnail designed for Finder; and
- a wide lead image designed for the first screen of the document preview.

Do not use a wide banner as the manifest thumbnail and assume Finder will
preserve its composition. Likewise, placing the square thumbnail at the top of
`document.md` may cause it to consume the entire first screen.

## Why lead-image proportions matter

Quick Look generally renders a document image at the full width of its content
column. Consequently, an image's aspect ratio—not merely its pixel dimensions—
determines how much vertical space it consumes.

The basic relationship is:

    rendered height = available content width ÷ image aspect ratio

where:

    image aspect ratio = image width ÷ image height

For illustration, at a content width of approximately 687 pixels:

| Image ratio | Approximate rendered height |
| ----------: | --------------------------: |
| 4:1 | 172px |
| 3:1 | 229px |
| 2:1 | 344px |
| 16:9 | 386px |
| 4:3 | 515px |
| 1:1 | 687px |

These figures are examples, not guaranteed Quick Look dimensions. The
relationship between width, ratio, and height remains useful at any window
size.

## Designing the first screen

### Prefer a wide lead image

A lead image around 3:1 or wider generally leaves room for the title, a short
introduction, and a visible indication of what follows.

Square or portrait artwork at the beginning of the Markdown document may
consume or exceed the entire first visible screen. Keep square package artwork
in the manifest thumbnail unless a full-screen document image is intentional.

### Budget the fold

Treat the first visible screen as a limited composition containing:

- the document title;
- an optional subtitle or short introduction;
- margins and spacing;
- the lead image; and
- a visible hint of the document's structure.

A useful approximation is:

    available image height =
      visible preview height
      − title block
      − introductory text
      − margins

The exact measurements vary, but the budgeting principle does not.

### Keep the introduction concise

Aim for no more than two short lines before the lead image. Move credits,
sourcing notes, provenance, and extended context below the image. This keeps
the opening clear without removing information from the document.

Line length varies with the Quick Look window and font settings, so a visual
line-count target is more reliable than a fixed character limit.

### Show what comes next

Place a structural element immediately after the lead image, such as:

- the first section heading;
- a table of contents;
- a summary table;
- a callout; or
- the beginning of the document's main argument.

Ideally, the bottom of the first screen reveals some of this structure. The
reader should see information scent rather than only the lower edge of an
image.

### Make imagery feel native to the document

Images that behave like artifacts—such as diagrams, maps, letters, newspaper
pages, forms, or mastheads—usually integrate naturally into a document preview.

Artwork presented on an arbitrary background may read as a pasted rectangle,
particularly against Quick Look's surrounding chrome. Where practical, let the
image's own material or subject define its background.

### Choose a document background intentionally

An LMD v2 manifest may declare an opaque sRGB `backgroundColor` such as
`#F7F1E3`. Lagoon uses this preference for the full on-screen document canvas
and chooses a light or dark content palette automatically. Other readers may
ignore the preference.

The document background is separate from the manifest thumbnail and does not
tint Finder's small package artwork. It also does not prescribe print, PDF, or
standalone HTML output. Authors should still verify that images, transparent
artwork, code samples, diagrams, and embedded media remain legible against the
chosen color in both Lagoon and Quick Look.

## Intentional full-screen imagery

Using the entire first screen for an image can be effective when the image
itself delivers the document's hook. Examples might include a newspaper front
page, a map, a framing diagram, or a deliberate title card.

The principle is not "never fill the first screen." It is "know when you are
spending the first screen, and make that choice intentionally."

## Audio and video in LMD v2

Quick Look never autoplays packaged audio or video.

### Choose the title track deliberately

The first referenced package-local `<audio>` element in rendered document order
is the title track. Quick Look exposes native controls for that track only.
Later packaged audio tracks are summarized and become available when the
document is opened in Lagoon.

Therefore:

- place the intended preview track first;
- give it a clear, accessible label;
- do not rely on a later track as a fallback; and
- verify that the title track uses a format supported by the target macOS
  versions.

If the title track is corrupt or unsupported, Quick Look displays its
unavailable state rather than substituting a later track.

### Give video a useful poster

Packaged videos remain manually playable in Quick Look. A descriptive poster
helps the reader understand the video before pressing Play and provides a
stable visual while the media is idle. Store local posters under `assets/` and
reference them from the video's `poster` attribute.

### Include captions

Use packaged WebVTT captions for spoken or meaning-bearing video. Captions
belong under `media/` and should be referenced with a `<track>` element. Do not
assume that audio alone communicates all necessary information.

### Do not depend on remote resources

Quick Look renders an LMD package without network access. Remote media, frames,
and connections are blocked. Everything required for the preview should be
packaged locally or represented by meaningful fallback text.

## Authoring checklist

Before publishing an `.lmd` document:

- Confirm the manifest thumbnail is square and remains recognizable at small
  Finder sizes.
- Treat the square thumbnail and wide lead image as separate compositions when
  necessary.
- Preview the document in Finder at compact and expanded Quick Look sizes.
- Confirm the title and introduction remain concise.
- Check whether the lead image leaves useful structure visible.
- Use a wide lead image unless a full-screen image is intentional.
- Confirm the intended title track is the first package-local audio element.
- Verify that audio and video never depend on autoplay.
- Add a useful poster and WebVTT captions to video.
- Confirm the preview works without network access.
- If `backgroundColor` is present, verify that the complete Quick Look canvas
  uses it and that text, diagrams, and transparent images remain readable.
- Open the same package in Lagoon and verify the complete document and all
  referenced media.

## Tooling opportunity

An authoring tool can estimate first-screen pressure from the opening image's
aspect ratio:

    estimated image height = preview content width ÷ image aspect ratio

The estimate can be combined with the title block and introductory text height.
If the total exceeds a representative Quick Look viewport, the tool can warn
that the opening composition may be clipped.

Such a warning should remain advisory because Quick Look dimensions are
controlled by macOS and can change.
