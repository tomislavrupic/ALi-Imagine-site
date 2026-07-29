# ALi Imagine v0.4.9

## First-run compatibility

ALi Imagine now opens as a usable studio before any local engine, model, hardware
certification, API key, or existing project is present.

### Highlights

- Fixed a clean-install crash caused by a development-machine database path.
- Clean installs now store state in macOS Application Support.
- Added a zero-install **Explore Interface** path.
- Made xAI Grok the safe optional cloud path after adding an API key.
- Deferred LTX, Krea, FLUX, Hugging Face, and media discovery until needed.
- Prevented Library navigation from re-hashing multi-gigabyte model assets on
  the UI path.
- Moved local capability checks off the Tauri command thread so page changes
  remain responsive.
- Preserved existing projects and local-engine installations.

### Installation

1. Download the Apple Silicon DMG.
2. Drag **ALi-Imagine** to **Applications**.
3. On first launch, right-click the app and choose **Open** if macOS displays an
   unidentified-developer warning.
4. Explore the interface immediately, add an xAI key, or configure local engines
   later from **System**.

The application is ad-hoc signed and is not yet Apple-notarized.
