# ALi Imagine v0.6.0

## Hailuo H3 MLX

This release adds Hailuo H3 as an isolated local video engine for Apple Silicon.
Existing projects, immutable assets, xAI, Krea, FLUX.2, and LTX installations
remain compatible.

### Highlights

- Added local Hailuo H3 text-to-video and image-to-video generation with joint
  video and audio output.
- Added fixed Draft 3s, High Quality 3s, High Quality 5s, and Long 10s presets.
- Added an app-managed, isolated Python and MLX runtime so H3 does not alter the
  existing LTX environment.
- Added resumable model installation, pinned source identity, manifest
  verification, disk and memory preflight, and explicit model-license consent.
- Added a reduced real audiovisual signal test. H3 is offered as ready only
  after the exact installed model and runtime pass certification.
- Added queue cancellation, interrupted-job recovery, immutable output
  publishing, prompt caching, source checksums, and generation provenance.
- Fixed LTX text-embedding cache reuse across repeated generations.

### Installation

1. Download the Apple Silicon DMG.
2. Drag **ALi-Imagine** to **Applications**.
3. On first launch, right-click the app and choose **Open** if macOS displays an
   unidentified-developer warning.
4. Open **System** to install or verify optional local engines.

Local engines and model weights are not bundled in the DMG. Hailuo H3 is an
optional separate download of approximately 70 GB, and the installer performs
capacity checks before downloading it. Existing Application Support data is
discovered in place.

The application is ad-hoc signed and is not yet Apple-notarized.
