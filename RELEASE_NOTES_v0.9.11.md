# ALi Imagine v0.9.11

- Native Qwen Image 2.1 full Q8 engine with retained vision encoder, generation, ordered reference editing, transparent PNG output and reference caching.
- Existing queue and Library integration preserves raw/effective prompts, ordered references, output checksums and cancellation.
- Centered System installer animation with measured download percentages and transferred GB for supported installers, plus live activity for unmeasured build/verification stages.
- Clear failure states, fresh progress per action and reduced-motion support.

Verification: 349 Rust tests and 171 frontend tests pass. Browser checks cover actual System installation progress, repeated actions and failures. Qwen real-model acceptance includes 1024×1024 generation, one/two-reference editing, transparency, cache parity, Gallery ingestion and active-denoise cancellation.

Models are separate downloads. Qwen licensing follows the upstream research licence. Masks remain deferred; ten-reference and 2K performance have not been benchmarked.

## Install

Download the Apple-silicon DMG, open it, and drag ALi-Imagine into Applications. The app and DMG are Developer ID signed and Apple notarization was accepted. Existing projects and separately installed models remain in place.

This release is available by direct DMG download. The signed in-app update feed remains on its previous release until the separate updater-signing key is available.
