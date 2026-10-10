# ALi Imagine 0.9.23 release evidence

Source: https://github.com/tomislavrupic/ALi-Imagine/commit/378bbc2a8f0304dd5efd857113d141278f0819e6
Review: https://github.com/tomislavrupic/ALi-Imagine/pull/15
Merged main: 7a221bf6fcedc7a79da648b6cb5dabc46fce8462.
Apple public notarization: b9cc18e8-7dc7-4f3f-837b-2eecc8d77d65 (Accepted).
Developer ID team: P6GH8ZH6R2. App and DMG stapled; Gatekeeper accepted. The updater is rebuilt without macOS metadata from the stapled app, signed, and verified against the bundled public key. All 64 entries extract with the updater's path handling; the extracted app passes code signing, Gatekeeper and ticket validation.

SHA-256:
- ALi-Imagine_0.9.23_aarch64.dmg: 00c22cfc2f2dc7aeb047cc5f020c4ae0f00a8755a8942d2bd648d131ade7ba87
- ALi-Imagine.app.tar.gz: 9be1ce52adc27bb7ba9e05eae5f767d5a60e48dedac971b36ded6d23d0cb1eac

251 frontend tests and 517 Rust tests pass; 81 hardware/opt-in tests are ignored. Production build, formatting and Clippy pass. The actual App component was exercised through an isolated browser fixture with a generated solid-color clip. At 1440×960, 1120×720 and 900×680, System remains on-screen; active-card text stays above Stop; navigation and playback fit. Selecting the completed take exits Preview, immediately opens Result and retains percentage/steps. Screenshots are UI evidence, not model inference.

The Studio receives a separately signed/notarized private build using the existing h3-local-testing feature. It is not uploaded among public assets. The private build's public-updater guard remains, and model capability requirements are unchanged. No physical laptop render or new model certification is claimed.
