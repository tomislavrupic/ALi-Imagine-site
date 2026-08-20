# ALi Imagine v0.7.8

Version 0.7.8 repairs the LTX 2.5 first-install path and makes long local-model downloads visible.

## What is new

- The LTX installer now installs the Native MLX runtime that ALi Create actually uses.
- A pinned public runtime source and ALi's verified audio and end-frame additions are installed into app-owned storage.
- The model installer downloads only the five required LTX 2.5 BF16 files at the pinned revision.
- Interrupted model downloads are preserved and resume on retry.
- The installer shows phase, percentage, transferred GiB, and interrupted-download guidance.
- First-run buttons now clearly open an installer; downloads start only after explicit confirmation.
- Existing compatible LTX installations remain available after updating.

## Fast first install

1. Download the Apple Silicon DMG and drag ALi Imagine to Applications.
2. On first launch, Control-click ALi Imagine and choose **Open** if macOS asks.
3. Enter the studio immediately, or open **System → LTX 2.5** when you want local video.
4. Install the small Native MLX runtime, add your Hugging Face token, accept the LTX terms, then start the resumable model download.

The complete LTX 2.5 model pack is approximately 71 GB and requires about 85 GiB free during installation. Models, projects, outputs, credentials, LoRAs, and certifications remain outside the app bundle and survive updates.

## Verification

- 53 frontend tests and 161 deterministic Rust tests passed.
- A complete fresh Native MLX runtime install passed in isolated storage.
- The DMG CRC, mounted Applications shortcut, app version, deep strict code signature, and isolated clean startup were verified.

## macOS signing

This build is ad-hoc signed and not Apple-notarized because a Developer ID Application certificate is not available. First launch on another Mac may require the Control-click **Open** step above.
