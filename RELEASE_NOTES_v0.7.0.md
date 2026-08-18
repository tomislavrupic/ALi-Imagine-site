# ALi Imagine v0.7.0

## Guided first install and native LTX-2.5 upscale

Version 0.7.0 makes a clean ALi Imagine installation understandable before any large model download and adds an official model-backed LTX-2.5 2x derivative path.

### Highlights

- Rebuilt **Ready the Studio** around four explicit choices: enter immediately, connect xAI, set up local images, or set up local video.
- Detects preserved app-owned engines and certifications after an application update, so existing models are not presented as missing.
- Restores the complete fresh-install LTX-2.5 path inside System: pinned Native MLX runtime, Hugging Face token in macOS Keychain, explicit licence acceptance, model download, deep verification, and real signal test.
- Adds `LTX 2.5 2x` to eligible base LTX-2.5 results using the official BF16 latent spatial upscaler and three-forward fidelity refinement.
- Preserves the source 48 kHz audio, frame count, prompt, seed, hashes, project identity, and asset lineage in a new immutable output.
- Keeps SeedVR2 available as a separate restoration model and blocks recursive LTX 2x chains.

### Installation

1. Download the Apple Silicon DMG.
2. Drag **ALi-Imagine** to **Applications**.
3. Because this build is ad-hoc signed, Control-click the app and choose **Open**, then **Open**, if macOS shows an unidentified-developer warning.
4. Enter the full interface immediately or choose one guided setup path.

Large local models remain separate, explicit app-managed downloads. Existing projects, outputs, credentials, model installations, and certifications remain in place when the application is replaced.

### Verification boundary

The installer passed DMG CRC validation, deep code-signature integrity, bundle-version inspection, mounted-layout checks, and an isolated clean-start smoke test. The build is not Apple-notarized because no Developer ID Application identity or notarization credentials are installed on the build machine.
