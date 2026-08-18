# ALi Imagine v0.7.4

## Native LTX 2.5 2× routing

Version 0.7.4 fixes the upscale action for current LTX 2.5 outputs and makes the intended pipeline explicit throughout the studio.

### Highlights

- Routes eligible LTX 2.5 outputs to the native latent 2× pipeline with three-forward refinement.
- Shows a single **LTX 2.5 2×** Stage action for LTX outputs.
- Renames the dedicated mode to **LTX 2.5 2×** and limits its picker to compatible outputs.
- Keeps **SeedVR2 2×** as a separate temporal-restoration path for non-LTX video.
- Preserves original audio, parent lineage, and immutable source media in the derived result.
- Includes the complete 0.7.3 Final 20, end-frame, direct-drop, and audio-fit improvements.

### Verification boundary

The routing regression is covered by frontend tests and was verified against a real completed LTX 2.5 database record. Packaging, installer, and clean-start checks passed. A full GPU LTX 2.5 2× render was not run during release verification.

### Installation

1. Download the Apple Silicon DMG.
2. Drag **ALi-Imagine** to **Applications**.
3. Because this build is ad-hoc signed, Control-click the app and choose **Open**, then **Open**, if macOS shows an unidentified-developer warning.
4. Existing projects, outputs, credentials, models, and certifications remain in place when the app is replaced.
