# ALi Imagine v0.8.7

Version 0.8.7 repairs the Qwen Prompt Assist install verification failure on 16–32 GB Macs.

- The public `mlx-community/Qwen3.5-4B-MLX-4bit` model remains pinned to immutable revision `32f3e8ecf65426fc3306969496342d504bfa13f3`.
- Its verified `config.json` SHA-256 is corrected to `f3efc81b2ea8d96a45301037d3ccccbcccdef44a961845c87f286aaddbc6eaaa`.
- Checksum verification remains fail-closed; it is not disabled or relaxed.
- The failed partial download is preserved. After updating, Resume/Retry reuses it rather than downloading the 3.06 GB model again.
- Compact output filenames and all prior 0.8.6 behavior remain unchanged.
