# Examples

`basic.lmd` is a minimal v1 document package built from the files in `basic/`.
It intentionally contains no directory entries or assets.

`v2-media.lmd` is a v2 document package built from `v2-media/`. It contains a
small deterministic WAV title track under `media/` and declares an optional
warm on-screen document background.

Rebuild it from the repository root:

```sh
python3 scripts/build_example.py
python3 scripts/build_v2_example.py
```

Inspect it with any ZIP utility:

```sh
unzip -l examples/basic.lmd
unzip -l examples/v2-media.lmd
```
