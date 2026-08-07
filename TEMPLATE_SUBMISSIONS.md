# Lagoon Template Submission and Review

Lagoon's v2 community catalog is curated manually. There are no public upload
accounts or submission endpoints. A proposed template must be supplied as an
`.lmd` file and pass every check below before it is added to the Lagoon product
repository's template catalog.

## Submitter checklist

- Confirm that the Markdown, thumbnail, and every bundled image, poster, audio,
  video, and caption file are original, licensed for redistribution, or in the
  public domain. Confirm recorded people consented where applicable.
- Include a clear title, short description, creator attribution, and license in
  `lagoon.json`, with `formatVersion` set to `2`.
- Use a square 1:1 thumbnail and keep the file at or below 5 MiB. Finder and
  Quick Look expect square package artwork. Treat a wide lead image inside
  `document.md` as a separate composition.
- Remove private information, tracking links, credentials, and material that is
  unsafe or unlawful to distribute.
- Open the template in the current Lagoon release and verify its Markdown,
  Mermaid diagrams, images, audio, video, posters, and captions without access
  to the author's source folders or network.
- In Finder Quick Look, verify that the first referenced packaged audio track is
  playable but never autoplays, later tracks are summarized, every packaged
  video remains manual, and remote media is blocked.
- Use **Use Template…**, edit the resulting document, save it, close it, and
  reopen it to verify the complete round trip.

## Reviewer checklist

- Run the site catalog generator; it must accept the archive's schema, paths,
  image/media structure and type signatures, metadata, and size limits.
- Confirm the manifest thumbnail has equal pixel width and height and remains
  legible at small Finder sizes.
- Independently review ownership, license compatibility, image rights,
  attribution, content safety, and the accuracy of the description.
- Inspect the protected template preview and the generated catalog card at
  common window and screen sizes.
- Verify that unreferenced packaged files are invisible, the intended title
  track is first in rendered document order, captions match the spoken media,
  and the template contains no unexpected remote requests.
- Download the built site's `.lmd` response and confirm its MIME type, download
  filename, integrity, and successful opening on another Mac.
- Create a document copy and verify that the original template's bytes and
  modification date remain unchanged.

Rejected or superseded packages should be removed in a normal reviewed commit.
Do not replace an accepted package under the same filename unless the catalog
change is deliberate and its download has been retested.
