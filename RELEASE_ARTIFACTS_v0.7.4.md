# ALi Imagine v0.7.4 release artifacts

## macOS installer

```text
ALi-Imagine_0.7.4_aarch64.dmg
```

Public release:

```text
https://github.com/tomislavrupic/ALi-Imagine-site/releases/tag/v0.7.4
```

Size:

```text
10,922,540 bytes
```

SHA-256:

```text
d5421c880a78400c8c356ef3e1767750ceb44963265495f3a605f4599502b9f5
```

Verification:

- DMG CRC validation passed with `hdiutil verify` locally and after a fresh GitHub release download.
- Installer contains ALi-Imagine 0.7.4 and an Applications shortcut.
- Embedded application and bundled WARP sidecar pass deep, strict code-sign verification.
- An isolated clean-start smoke created a fresh database and reached frontend-ready state in 147 ms.
- 52 frontend tests, 14 MLX-worker tests, and 137 deterministic Rust tests passed; strict Clippy and the production frontend build also passed.
- Existing local projects and app-managed model storage are not bundled or modified.
- The application is ad-hoc signed and not Apple-notarized; first launch may require Control-click **Open** once.
- LTX 2.5 native 2× routing was verified through tests and package inspection; a full GPU upscale render was not run for this release check.
