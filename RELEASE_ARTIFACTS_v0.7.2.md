# ALi Imagine v0.7.2 release artifacts

## macOS installer

```text
ALi-Imagine_0.7.2_aarch64.dmg
```

Public release:

```text
https://github.com/tomislavrupic/ALi-Imagine-site/releases/tag/v0.7.2
```

Size:

```text
10,927,044 bytes
```

SHA-256:

```text
3ee9492f2a78f95f3d534201aa60f71b9826cbfeacba71f63b7952a0eb0e3111
```

Verification:

- DMG CRC validation passed with `hdiutil verify`.
- Installer contains ALi-Imagine 0.7.2 and an Applications shortcut.
- Embedded application and bundled WARP sidecar pass deep, strict code-sign verification.
- An isolated clean-start smoke created a fresh database and reached frontend-ready state in 158 ms.
- 50 frontend tests, 14 MLX-worker tests, and 137 deterministic Rust tests passed.
- Existing local projects and app-managed model storage are not bundled or modified.
- The application is ad-hoc signed and not Apple-notarized; first launch may require Control-click **Open** once.
