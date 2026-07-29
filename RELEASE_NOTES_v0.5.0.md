# ALi Imagine v0.5.0

## Locked production checkpoint

This release freezes the current ALi Imagine workflow after a stability and
media-viewing pass. Existing projects, immutable assets, xAI, Krea, LTX, and
local model installations remain compatible.

### Highlights

- Centered Stage media reliably and reset stale zoom or pan when the selected
  asset, source, mode, or comparison view changes.
- Kept Fit, zoom, and pan controls available without allowing previews to drift
  outside the Stage.
- Moved expensive local-engine filesystem and integrity checks off the UI
  thread, reducing stalls when opening System or switching workspaces.
- Added a native LTX Audio-to-Video path using one start frame, one audio file,
  and a performance signal.
- Preserved the legacy video-plus-audio LipDub path for existing recipes.
- Recorded resolved audio/video settings, timing, checksums, and model identity
  in immutable output provenance.
- Deferred deep model checksum validation until an operation runs while keeping
  lightweight readiness checks responsive.

### Installation

1. Download the Apple Silicon DMG.
2. Drag **ALi-Imagine** to **Applications**.
3. On first launch, right-click the app and choose **Open** if macOS displays an
   unidentified-developer warning.
4. Explore the interface immediately, add an xAI key, or configure local engines
   later from **System**.

Local engines and model weights are not bundled in the DMG. Existing
Application Support data is discovered in place.

The application is ad-hoc signed and is not yet Apple-notarized.
