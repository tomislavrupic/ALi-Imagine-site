# ALi Imagine 0.9.22 release evidence

Source: https://github.com/tomislavrupic/ALi-Imagine/commit/3c556329da2d6ec580344bd9e7e738ca0d523661
Review: https://github.com/tomislavrupic/ALi-Imagine/pull/14
Merged main: 59698492b6ffd81f483462c9fd7ad7f39604e093.
Apple public notarization: e739174e-45ff-4165-a34f-6f6bb0291130 (Accepted).
Developer ID team: P6GH8ZH6R2. App and DMG stapled; Gatekeeper accepted. Updater rebuilt without macOS metadata from the stapled app, then signed and verified against the bundled public key. All 64 entries extracted with the Tauri updater's path layout; extracted app passed code signing, Gatekeeper and ticket validation.

SHA-256:
- ALi-Imagine_0.9.22_aarch64.dmg: 1c3677cd5d1c470b40000cefbc6608577f44e7e2f449774a8e9b9a0326b6d422
- ALi-Imagine.app.tar.gz: 06c646ef6e071a175387ff2b423f1cbbbc03db5196274efa7a69ebf1c602d229

251 frontend tests and 517 Rust tests pass; 81 hardware/opt-in Rust tests ignored. Standard and private H3 Clippy/test configurations pass. Browser fixtures cover the icon toggle and progress across Preview, Source, Result and FX at 900/1600px; these are not screenshots of model inference.

Compared with the original release-0918 working files, the H3 step slider, LoRA library/policy, timing feedback and model/style/DMAD implementations are retained. Earlier private H3 availability differed from the standard public build; a separate private Studio build was explicitly requested. That private build is not uploaded as a public release artifact. No model weights are added or changed here. No physical laptop render is claimed.
