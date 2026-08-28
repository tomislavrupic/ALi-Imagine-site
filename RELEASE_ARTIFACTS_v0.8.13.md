# ALi Imagine v0.8.13 release artifacts

- Installer: `ALi-Imagine_0.8.13_aarch64.dmg`
- SHA-256: `b9f7684eba71e68ba175ee0c21e703428098b262cd9a80003449bb3c3ecb5854`
- Architecture: Apple Silicon (`arm64`)
- Bundle identifier: `com.haos.ali-imagine`
- Signing: ad-hoc hardened runtime; not notarized

Verification: 71 frontend tests and 223 Rust tests passed; 52 real-model tests remained explicit opt-ins. The IC-LoRA Union Canny and LipDub v0.9 real acceptance renders passed. Production build, DMG CRC, mounted bundle version, deep signature, Applications link, and installed-binary identity checks passed. Advanced Q8 Retake, Extend, and Warp acceptance remains a separate model-backed gate.
