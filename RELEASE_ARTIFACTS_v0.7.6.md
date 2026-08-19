# ALi Imagine v0.7.6 release artifacts

## macOS installer

```text
ALi-Imagine_0.7.6_aarch64.dmg
```

Public release:

```text
https://github.com/tomislavrupic/ALi-Imagine-site/releases/tag/v0.7.6
```

Size:

```text
11,043,848 bytes
```

SHA-256:

```text
bf23476bafbb3be5c06fdc230843e93e67d0a5d2f4f6a6688604ec2c705febd6
```

Verification:

- DMG CRC validation passed with `hdiutil verify`.
- Installer contains ALi-Imagine 0.7.6 and an Applications shortcut.
- Embedded application and bundled WARP sidecar pass deep, strict code-sign verification.
- 53 frontend tests and 158 deterministic Rust tests passed; 35 explicitly gated live tests remained ignored.
- Existing local projects, outputs, app-managed models, external model libraries, and Concept LoRAs are not bundled or modified.
- The application is ad-hoc signed and not Apple-notarized; first launch may require Control-click **Open** once.
