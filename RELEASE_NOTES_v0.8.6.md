# ALi Imagine v0.8.6

Version 0.8.6 keeps generated and derived media filenames compact and safely below macOS component limits.

- New generation filenames are capped at 120 ASCII characters.
- Chained outputs use a compact source identifier instead of recursively embedding the previous output filename.
- SeedVR2 video, LTX 2.5 spatial upscale, and Clean 2160p delivery share the same bounded allocator.
- Full source names, source IDs, checksums, prompts, models, seeds, and derivation history remain in metadata and the database.
- Existing media files are not renamed. Retrying a filename-length failure creates a new compact output name.
