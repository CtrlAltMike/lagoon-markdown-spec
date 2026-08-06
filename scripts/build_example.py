#!/usr/bin/env python3
"""Build the minimal example package with deterministic ZIP metadata."""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "examples" / "basic"
DESTINATION = ROOT / "examples" / "basic.lmd"
FILES = ("lagoon.json", "document.md")
TIMESTAMP = (2026, 1, 1, 0, 0, 0)


with ZipFile(DESTINATION, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
    for name in FILES:
        info = ZipInfo(name, TIMESTAMP)
        info.compress_type = ZIP_DEFLATED
        info.create_system = 3
        info.external_attr = 0o100644 << 16
        info.flag_bits |= 0x800
        archive.writestr(info, (SOURCE / name).read_bytes())

print(f"Built {DESTINATION.relative_to(ROOT)}")
