# ALi Imagine 0.9.19 release evidence

Source: https://github.com/tomislavrupic/ALi-Imagine/commit/57ab668
Review: https://github.com/tomislavrupic/ALi-Imagine/pull/10
Apple notarization: c9851f43-9c68-4751-888a-21109b56047e (Accepted).
Developer ID team: P6GH8ZH6R2. App and DMG stapled; Gatekeeper assessments accepted. Updater signature verified using the existing bundled public key.

SHA-256:
- ALi-Imagine_0.9.19_aarch64.dmg: 550a85187dc4063ac41f62713d69c2161f72f6941fbc670bbea841222eb02c42
- ALi-Imagine.app.tar.gz: 2610b620420b2656b3820bc069717d045cfe8a88a05df72e81984848d19df197

237 frontend tests and 489 Rust tests pass; 79 opt-in/model-dependent tests ignored in the standard suite. The newly added native WARP HTTP smoke test was run explicitly and passed. Compilation, formatting, Clippy, signed release, notarization and updater signature checks pass. Physical laptop installation and two-Mac render validation are not claimed.
