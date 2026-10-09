# ALi Imagine 0.9.20 release evidence

Source: https://github.com/tomislavrupic/ALi-Imagine/commit/01bbb158e839e655d3a67f154cd616afe9076dec
Review: https://github.com/tomislavrupic/ALi-Imagine/pull/11
Merged main: 3348557ea3f2ef2074badecc291560e04db629f0.
Apple notarization: f732df9c-5120-427e-8e97-3521d579db18 (Accepted).
Developer ID team: P6GH8ZH6R2. App and DMG stapled; Gatekeeper assessments accepted. Updater archive rebuilt from the stapled app and its signature verified against the existing bundled public key.

SHA-256:
- ALi-Imagine_0.9.20_aarch64.dmg: 617579b808191a4359dc33da29895727a8044ecacf4e0116c1aaa2edae4f52c2
- ALi-Imagine.app.tar.gz: 9c6d9fac1854be8140c085c2a1ec8dbb1e4797ae9b89b75c2be85aba9fc3b3b0

250 frontend tests and 514 Rust tests pass; 80 opt-in/model-dependent Rust tests ignored. Formatting, Clippy, production builds and 21 Python runtime mathematics tests pass. Regression coverage includes H3 cancellation, memory/recipe readiness, exact external dependency fingerprints and pending remote cancellation.

The final app was inspected: version 0.9.20, exact 24-file PDD runtime allowlist, all 22 manifest hashes matching, no trained curve/model bytes or generated Python caches, and the existing Qwen installer tree preserved. Model and adapter data remain in the local model library.

The native Metal WARP HTTP smoke test was explicitly run during 0.9.19 remote-render development and passed on the Studio; its implementation is unchanged in this update. Physical laptop installation, two-Mac rendering and every-model certification are not claimed.
