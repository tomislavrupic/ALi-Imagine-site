# ALi Imagine v0.7.5 release artifacts

## macOS installer

```text
ALi-Imagine_0.7.5_aarch64.dmg
```

Public release:

```text
https://github.com/tomislavrupic/ALi-Imagine-site/releases/tag/v0.7.5
```

Size:

```text
11,016,796 bytes
```

SHA-256:

```text
a043f02175927fe79f0f5a866edaaec60849d4dd828c8ab4e96b8a757eacc1ae
```

Verification:

- DMG CRC validation passed with `hdiutil verify`.
- Installer contains ALi-Imagine 0.7.5 and an Applications shortcut.
- Embedded application and bundled WARP sidecar pass deep, strict code-sign verification.
- 52 frontend tests and 149 deterministic Rust tests passed; 34 explicitly gated model tests remained ignored.
- A real local Qwen vision smoke test rewrote rough Signal text while preserving its static-camera, no-cut, subject-motion, and audio constraints.
- Existing local projects, outputs, app-managed models, and Concept LoRAs are not bundled or modified.
- The application is ad-hoc signed and not Apple-notarized; first launch may require Control-click **Open** once.
