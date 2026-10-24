# ALi Imagine 0.9.41 artifacts

Source commit: `bd7df95248e0da696012ff7d9d0bf55478791dec` (tag `v0.9.41`).

Developer ID Application signed with team `P6GH8ZH6R2`. Apple notarization submission `515dfa9f-f229-4edc-84e7-b337d8218085` accepted. App and DMG tickets stapled and validated; Gatekeeper accepted both.

The updater signature was verified against the bundled public key. Tauri extraction, the extracted app signature, Gatekeeper and stapled ticket checks passed (99 archive entries).

- DMG SHA-256: `be0ac48056bff7ba499aca07dd1cc454cf71955dd83952966f1c64107050a9f3`
- Updater SHA-256: `bb692bf251613d0be129f7927a2c0b9ab2a2c8e0d149b4eca9630b0b7985456c`
- Frontend: 384 tests passed.
- Rust: 662 passed, 100 ignored; formatting and Clippy passed.
- Python training worker: 14 tests passed.

[Download and release notes](https://github.com/tomislavrupic/ALi-Imagine-site/releases/tag/v0.9.41).

Model-dependent ignored tests are not inference certification. The existing Qwen 2× repair was also verified with a real 1344×768 to 2688×1536 render before release. Creative style fidelity remains subject to review.
