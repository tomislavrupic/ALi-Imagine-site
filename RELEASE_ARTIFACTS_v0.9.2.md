# ALi Imagine v0.9.2 release artifacts

- Installer: `ALi-Imagine_0.9.2_aarch64.dmg`
- DMG SHA-256: `15e3d54d2d4f0cf66566c74a9065572dda648526527ac0bb531b22c7d4e9eb5d`
- Updater archive: `ALi-Imagine.app.tar.gz`
- Updater SHA-256: `2678b9ef6daf8c0d7ff0341d1a724f850b4ece60e1d150061be93d216ff5341b`
- Architecture: Apple Silicon (`arm64`)
- Bundle identifier: `com.haos.ali-imagine`
- Signing: Developer ID Application, team `P6GH8ZH6R2`
- Apple notarization submission: `f1fa631f-ce4f-48f7-93b5-24365f4fe3db` accepted

Verification: 82 frontend tests and 241 Rust tests passed; 60 hardware/model acceptance tests remained explicit opt-ins. Strict formatting and Clippy, production build, Developer ID signature verification, Apple notarization, ticket stapling, and Gatekeeper assessment passed. This refreshed 0.9.2 build adds native-resolution lossless paused-frame capture with fail-closed geometry verification.
