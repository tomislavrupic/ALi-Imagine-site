# ALi Imagine v0.7.8 release artifacts

## macOS installer

```text
ALi-Imagine_0.7.8_aarch64.dmg
```

Public release:

```text
https://github.com/tomislavrupic/ALi-Imagine-site/releases/tag/v0.7.8
```

Size:

```text
11,075,762 bytes
```

SHA-256:

```text
89f81410d46247af848417e9abf776508a13dfde4ac8ff4a8bc5340d5f480c7c
```

Verification:

- DMG CRC validation passed.
- Installer contains ALi-Imagine 0.7.8 and an Applications shortcut.
- Embedded application and bundled WARP sidecar pass deep, strict code-sign verification.
- 53 frontend tests and 161 deterministic Rust tests passed; 35 explicitly gated real-model tests remained ignored.
- A complete fresh Native MLX runtime install passed in isolated storage.
- Isolated first launch created a fresh database without touching the user's normal projects or models.
- Existing projects, outputs, app-managed models, external model libraries, and Concept LoRAs are not bundled or modified.
- The application is ad-hoc signed and not Apple-notarized; first launch may require Control-click **Open** once.
