#!/usr/bin/env python3
"""Build a deterministic LMD v2 package containing a small WAV title track."""

from pathlib import Path
from wave import open as open_wave
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "examples" / "v2-media"
MEDIA = SOURCE / "media" / "title.wav"
DESTINATION = ROOT / "examples" / "v2-media.lmd"
FILES = ("lagoon.json", "document.md", "media/title.wav")
TIMESTAMP = (2026, 1, 1, 0, 0, 0)


MEDIA.parent.mkdir(parents=True, exist_ok=True)
with open_wave(str(MEDIA), "wb") as audio:
    audio.setnchannels(1)
    audio.setsampwidth(1)
    audio.setframerate(8_000)
    audio.writeframes(bytes([128]) * 800)

with ZipFile(DESTINATION, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
    for name in FILES:
        info = ZipInfo(name, TIMESTAMP)
        info.compress_type = ZIP_DEFLATED
        info.create_system = 3
        info.external_attr = 0o100644 << 16
        info.flag_bits |= 0x800
        archive.writestr(info, (SOURCE / name).read_bytes())

print(f"Built {DESTINATION.relative_to(ROOT)}")
