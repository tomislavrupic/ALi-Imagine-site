# ALi Imagine 0.8.14

- Prevents long native LTX 2.5 upscales from silently completing with corrupted tail frames by using bounded overlapping chunks and post-render tail validation.
- Reduces peak memory pressure during 10- and 20-second LTX 2.5 upscales.
- Preserves source audio when present and permits silent source clips.
- Stops gallery and Stage videos from autoplaying when selected.
- Makes the CEL Character adapter download start directly after author-terms acceptance and shows progress on its card.
- Adds the hybrid Concepts + LoRA / Stage FX workflow foundation.
- Refines the footer update control position and typography.

Preview boundary: updater archives are signed with ALi's Tauri updater key. Public macOS distribution still requires Developer ID signing and Apple notarization.
