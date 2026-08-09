# ALi Imagine v0.6.4

## Project-aware local production

This release connects ALi Imagine to the Sirius execution layer and KITKAT memory handoffs while keeping every application independently usable and local-first.

### Highlights

- Added verified Sirius draft intake with immutable prompt provenance and optional shared Pixel project identity.
- Added native SeedVR2 3B temporal 2× video restoration for H3, LTX, cloud, and imported videos.
- Preserved source videos and original audio, with queue progress, cancellation, checksums, lineage, and recoverable failures.
- Kept LTX Pixel Spatial available as an optional LTX-specific upscale route.
- Separated video resolution and duration controls and removed legacy H3 runtime terminology.
- Improved H3 MLX progress, diagnostics, first/last-frame workflows, and send-to-ALi review behavior.

### Installation

1. Download the Apple Silicon DMG.
2. Drag **ALi-Imagine** to **Applications**.
3. On first launch, right-click the app and choose **Open** if macOS displays an unidentified-developer warning.
4. Open **System** to install or verify optional local engines.

Large local models remain separate app-managed downloads. Existing projects, outputs, credentials, model installations, and certifications remain in place. The application is ad-hoc signed and is not Apple-notarized.
