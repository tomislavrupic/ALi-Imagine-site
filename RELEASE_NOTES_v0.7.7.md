# ALi Imagine v0.7.7

Version 0.7.7 makes LTX 2.5 Prompt Assist follow the official LTX 2.5 prompting structure while retaining ALi's fast, model-optional first launch.

## What is new

- Your Signal remains the authoritative creative direction; Prompt Assist fixes the English and adds compatible production detail without replacing the idea.
- Normal LTX suggestions follow shot, scene, action, character continuity, camera behavior, and audio in chronological present-tense prose.
- First-frame, last-frame, and first-plus-last workflows stay continuous unless you explicitly ask for an edit.
- Explicit multi-shot prompts use named transitions and preserve subject, framing, lighting, and audio continuity.
- Requested constraints such as a static camera, no cuts, subtle motion, language, accent, visible text, and exact frame endpoints are retained.

## Fast first install

1. Download the Apple Silicon DMG and drag ALi Imagine to Applications.
2. On first launch, Control-click ALi Imagine and choose **Open** if macOS asks.
3. Enter the studio immediately; no local model download is required.
4. Link an existing model folder or choose where future models are installed whenever you are ready.

Models, projects, outputs, credentials, LoRAs, and certifications remain outside the application bundle and survive app updates.

## Verification

- 53 frontend tests and 160 deterministic Rust tests passed.
- The DMG CRC, mounted Applications shortcut, app version, deep strict code signature, and isolated clean startup were verified.

## macOS signing

This build is ad-hoc signed and not Apple-notarized because a Developer ID Application certificate is not available. First launch on another Mac may require the Control-click **Open** step above.
