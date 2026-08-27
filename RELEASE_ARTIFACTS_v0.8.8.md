# ALi Imagine v0.8.8 release artifacts

- Installer: `ALi-Imagine_0.8.8_aarch64.dmg`
- Platform: macOS Apple Silicon
- SHA-256: `573a376e3fe52105ba5baf31d24e556e2b997bccfde9beff1730019b7b213192`

Verification: 65 frontend tests and 191 Rust tests passed; formatting, Clippy, production build, app signature, bundle version, DMG checksum, mounted bundle signature, executable permissions, and Applications link checks passed. One temporary-port fallback test could not open a loopback listener inside the build sandbox and was excluded from the otherwise passing Rust suite. Fresh 16 GB Mac Refine remains the external acceptance gate.
