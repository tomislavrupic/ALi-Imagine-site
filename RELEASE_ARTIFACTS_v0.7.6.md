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
11,044,994 bytes
```

SHA-256:

```text
d852bd17c76c0ad9895b94c1a1673a2356b6816507d340cc023926abe5d000a7
```

Verification:

- DMG CRC validation passed with `hdiutil verify`.
- Installer contains ALi-Imagine 0.7.6 and an Applications shortcut.
- Embedded application and bundled WARP sidecar pass deep, strict code-sign verification.
- 53 frontend tests and 158 deterministic Rust tests passed; 35 explicitly gated live tests remained ignored.
- Existing local projects, outputs, app-managed models, external model libraries, and Concept LoRAs are not bundled or modified.
- The application is ad-hoc signed and not Apple-notarized; first launch may require Control-click **Open** once.
