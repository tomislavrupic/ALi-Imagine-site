# ALi Imagine v0.7.5

## LTX 2.5 Prompt Guidance and Concept LoRAs

Version 0.7.5 turns the Signal field into a guided LTX 2.5 prompt editor and adds certified native-MLX loading for compatible LTX 2.5 Concept LoRAs.

### Highlights

- Rewrites rough user-written Signal text into fluent, production-ready LTX 2.5 direction.
- Treats the user's subject, action, camera, pacing, mood, audio, and constraints as authoritative instead of replacing them with a generic animation.
- Uses the supplied start frame, end frame, or first-and-last pair to add only compatible visual detail.
- Follows the official LTX 2.5 structure for shot framing, scene and light, chronological action, camera movement, and sound.
- Accepts the current Sirius runtime manifest and `vision` capability, with a smaller temporary analysis image for faster local Qwen processing.
- Preserves a completed prompt even if model cleanup returns a warning, while still releasing Qwen before LTX generation whenever possible.
- Adds verified Concept LoRA import, compatibility checks, adjustable strength, provenance, and native MLX generation routing.
- Keeps the existing LTX 2.5 2×, Final 20, end-frame, direct-drop, and audio-fit workflows.

### Local prompt model

Prompt Guidance uses `mlx-community/Qwen3.8-27B-4bit` from the Sirius model library. The model remains a separate local download and is not bundled in the installer.

### Installation

1. Download the Apple Silicon DMG.
2. Drag **ALi-Imagine** to **Applications**.
3. Because this build is ad-hoc signed, Control-click the app and choose **Open**, then **Open**, if macOS shows an unidentified-developer warning.
4. Existing projects, outputs, credentials, models, LoRAs, and certifications remain in place when the app is replaced.
