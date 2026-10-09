# ALi Imagine 0.9.20 release evidence

Source: https://github.com/tomislavrupic/ALi-Imagine/commit/01bbb158e839e655d3a67f154cd616afe9076dec
Review: https://github.com/tomislavrupic/ALi-Imagine/pull/11
Merged main: 3348557ea3f2ef2074badecc291560e04db629f0.
Apple notarization: f732df9c-5120-427e-8e97-3521d579db18 (Accepted).
Developer ID team: P6GH8ZH6R2. App and DMG stapled; Gatekeeper assessments accepted. Updater archive rebuilt from the stapled app and its signature verified against the existing bundled public key.

SHA-256:
- ALi-Imagine_0.9.20_aarch64.dmg: 617579b808191a4359dc33da29895727a8044ecacf4e0116c1aaa2edae4f52c2
- ALi-Imagine_0.9.20_updater-r2.app.tar.gz: 29e7bbd8e7f5917ef8722b2b81400b0768400374e953f0da3c1f4242976825ad

250 frontend tests and 514 Rust tests pass; 80 opt-in/model-dependent Rust tests ignored. Formatting, Clippy, production builds and 21 Python runtime mathematics tests pass. Regression coverage includes H3 cancellation, memory/recipe readiness, exact external dependency fingerprints and pending remote cancellation.

The final app was inspected: version 0.9.20, exact 24-file PDD runtime allowlist, all 22 manifest hashes matching, no trained curve/model bytes or generated Python caches, and the existing Qwen installer tree preserved. Model and adapter data remain in the local model library.

The native Metal WARP HTTP smoke test was explicitly run during 0.9.19 remote-render development and passed on the Studio; its implementation is unchanged in this update. Physical laptop installation, two-Mac rendering and every-model certification are not claimed.

## Updater packaging repair (r2)

The original 0.9.20 archive contained macOS AppleDouble metadata. Tauri updater 2.10.1 strips the enclosing app path while extracting; the leading `._ALi-Imagine.app` regular file collided with its temporary directory, causing installation to fail before replacing the current app.

Source fix: https://github.com/tomislavrupic/ALi-Imagine/pull/12 (dd8c991ad624903e560e4f1f03fef90d56c42d57). The release script excludes macOS metadata/xattrs and now gates publication on Tauri-compatible extraction plus Apple trust checks. Two regression tests, formatting, Clippy and updater-signature verification pass.

The corrected 64-entry archive uses a fresh updater-r2 URL. It preserves the same signed, notarized app and passes the same extraction layout used by the installed 0.9.18 updater, followed by codesign, Gatekeeper and stapler validation. The DMG is unchanged. The initial archive is superseded; signature-only checks did not detect its extraction defect. Physical installation on the user's Mac is not claimed.
