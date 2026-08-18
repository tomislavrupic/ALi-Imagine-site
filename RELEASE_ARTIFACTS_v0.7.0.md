# ALi Imagine v0.7.0 release artifacts

## macOS installer

```text
ALi-Imagine_0.7.0_aarch64.dmg
```

Public release:

```text
https://github.com/tomislavrupic/ALi-Imagine-site/releases/tag/v0.7.0
```

Size:

```text
10,900,353 bytes
```

SHA-256:

```text
8152e4e5daec048cd03aa48ffbc97d74b486954a2d35c6e689cfa4440ad65cef
```

Verification:

- DMG CRC validation passed with `hdiutil verify`.
- Installer contains ALi-Imagine 0.7.0 and an Applications shortcut.
- Embedded application and bundled WARP sidecar pass deep, strict code-sign verification.
- An isolated clean-start smoke created a fresh database and reached frontend-ready state in 574 ms.
- Existing local projects and app-managed model storage are not bundled or modified.
- The application is ad-hoc signed and not Apple-notarized; first launch may require Control-click **Open** once.
