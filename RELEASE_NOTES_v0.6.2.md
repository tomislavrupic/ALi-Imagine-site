# ALi Imagine v0.6.2

## Hailuo H3 references and diagnostics

This update expands the local Hailuo H3 workflow and makes long-running system
actions and renders easier to understand.

### Highlights

- Added certified H3 first-and-last-frame video generation.
- Added the separate H3 Ref2VA path for one ordered image and one audio
  reference, generating synchronized picture and sound locally.
- Added persistent progress feedback to System actions so verification and
  hardware tests visibly report that work has started.
- Added measured H3 render duration and phase timings to the selected asset's
  Inspector, including older renders whose metrics are stored in provenance.
- Preserved the original ALi Imagine application icon.

### Installation

1. Download the Apple Silicon DMG.
2. Drag **ALi-Imagine** to **Applications**.
3. On first launch, right-click the app and choose **Open** if macOS displays an
   unidentified-developer warning.
4. Open **System** to install or verify optional local engines.

Large local models are separate app-managed downloads and are not included in
the DMG. Existing projects, outputs, model installations, certifications, and
credentials remain in place when the application is updated.

The application is ad-hoc signed and is not Apple-notarized.
