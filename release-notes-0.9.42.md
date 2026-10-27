# ALi Imagine 0.9.42

LTX First + Last now reports frame-anchor preparation separately from Gemma prompt encoding, with accurate image-encoding timing. This corrects misleading progress reporting; the earlier long stall was not reproduced, so this release does not claim a proven performance or deadlock fix.

- Removes retired SeedVR2 commands and model-loading requirements from the Krea worker. Existing outputs and model files are preserved.
- Retains reference Looks, main-window reference selection, Qwen 2× and existing studio workflows.
- Adds isolated App Store development scaffolding. This is the direct-download release; the Store build remains gated pending compatibility and signing work.
- Retains tested ML dependency versions. No model weights are bundled.

Qwen models use the noncommercial Qwen Research License. Public H3 remains authorization-gated. Model access and licenses remain separate from the app.
