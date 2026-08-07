# Lagoon playback and Quick Look profile

This document records the reference Lagoon and Quick Look behavior for media
inside Lagoon Markdown format v2 packages. It supports the package
specification but does not add conformance requirements for third-party
readers.

## Lagoon viewer playback

Lagoon provides a persisted **Autoplay visible videos** content setting. It is
On by default and applies to Markdown and Lagoon Markdown documents opened in
Lagoon.

Automatic playback follows these rules:

- Only package-local or document-local videos are eligible. Remote videos
  remain manual.
- A video is eligible only while its complete player is visible within the
  viewport.
- When multiple videos are eligible, only the topmost plays automatically.
- Automatic playback starts muted, resumes from the video's prior position,
  never enables looping, and pauses as soon as full visibility is lost.
- A manual pause suppresses automatic playback for that video until it leaves
  and re-enters the fully visible region.
- A manually started video may continue while partially visible, but pauses
  when it becomes fully offscreen.
- User-started audio or video takes priority and suppresses automatic video
  playback.
- Starting any media pauses every other playing audio or video element.
- User-started audio may continue offscreen until paused, replaced by another
  track, or the document closes.

Lagoon pauses media when the application resigns active status or the viewer is
dismantled. It reevaluates eligible video when the application becomes active.

Automatic playback is disabled in standalone HTML export, print/PDF rendering,
and Quick Look.

## Quick Look resource isolation

The Quick Look extension materializes validated renderer resources and the
package's `assets/` and `media/` entries into an extension-owned temporary
directory. It loads the rendered document with read-only file access so WebKit
can provide reliable local-media seeking without granting general filesystem
or network access.

The preview applies a restrictive content policy:

- remote media is blocked;
- remote frames are blocked;
- network connections are blocked;
- scripts supplied by the document are not executed; and
- the temporary directory is removed when the preview changes or closes.

## Quick Look title track

The title track is the first package-local `audio` element in rendered document
order.

Quick Look:

- exposes native play/pause, timeline, duration, seeking, and volume controls
  for the title track;
- never autoplays it;
- removes later package-local audio players from the preview; and
- inserts one accessible notice after the title track:

> N additional tracks — Open in Lagoon to listen.

`N` is the number of later package-local audio elements removed from the
preview. If the title track is corrupt or unsupported, Quick Look displays its
unavailable state and does not substitute another track.

Opening the package in Lagoon exposes every referenced audio track.
Unreferenced packaged files remain invisible.

## Quick Look video

Every referenced packaged video remains manually playable in Quick Look.
Quick Look removes autoplay behavior and provides native controls. Starting an
audio or video element pauses any other playing media element.

Authors should provide useful local posters below `assets/` and WebVTT captions
below `media/` for meaning-bearing video.
