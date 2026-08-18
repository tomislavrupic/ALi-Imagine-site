# ALi Imagine v0.7.2

## End frames, audio-fit duration, direct drops, and experimental Final 20

Version 0.7.2 makes LTX-2.5 video work more direct while preserving the certified defaults.

### Highlights

- Adds a clear **Start Frame / End Frame** selector. End-frame mode invents the chronological lead-in and lands on the supplied final image without reversing video or audio.
- Makes Start Frame, End Frame, and First + Last wells real mouse drop targets for Finder, the ALi Library, and HTTP(S) browser images.
- Fits performance audio to the nearest covering model-valid duration instead of falling from 20 seconds directly to 15 seconds.
- Adds an explicit opt-in **Experimental Direct Final 20** preset at 1280×704. Ordinary Final remains capped at its certified five-second budget.
- Keeps the packaged MLX worker self-contained in ALi-managed Application Support.
- Records endpoint choice, audio fit, source hashes, preset, experimental status, and complete render lineage in provenance.

### Installation

1. Download the Apple Silicon DMG.
2. Drag **ALi-Imagine** to **Applications**.
3. Because this build is ad-hoc signed, Control-click the app and choose **Open**, then **Open**, if macOS shows an unidentified-developer warning.
4. Existing projects, outputs, credentials, models, and certifications remain in place when the app is replaced.

### Verification boundary

The installer passed DMG CRC validation, deep code-signature integrity, bundle-version inspection, mounted-layout checks, and an isolated clean-start smoke test. The standard Preview, Working, and Final budgets retain their certified limits. Experimental Direct Final 20 is exposed as an opt-in test surface and is not claimed as a completed or certified 20-second Final render. The build is not Apple-notarized because no Developer ID Application identity or notarization credentials are installed on the build machine.
