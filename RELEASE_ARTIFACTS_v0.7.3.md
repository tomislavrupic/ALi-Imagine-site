# ALi Imagine v0.7.3 release artifacts

## macOS installer

```text
ALi-Imagine_0.7.3_aarch64.dmg
```

Public release:

```text
https://github.com/tomislavrupic/ALi-Imagine-site/releases/tag/v0.7.3
```

Size:

```text
10,922,958 bytes
```

SHA-256:

```text
9f0cd40a950e8c4ea4cd0cdb6a3e3f16f64d9a0426b5bda1ab0bf4236c049151
```

Verification:

- DMG CRC validation passed with `hdiutil verify` locally and after a fresh GitHub release download.
- Installer contains ALi-Imagine 0.7.3 and an Applications shortcut.
- Embedded application and bundled WARP sidecar pass deep, strict code-sign verification.
- An isolated clean-start smoke created a fresh database and reached frontend-ready state in 130 ms.
- 50 frontend tests, 14 MLX-worker tests, and 137 deterministic Rust tests passed.
- Existing local projects and app-managed model storage are not bundled or modified.
- The application is ad-hoc signed and not Apple-notarized; first launch may require Control-click **Open** once.
