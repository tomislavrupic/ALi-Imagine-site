# ALi Imagine 0.9.36 verification receipt

Source build: `704cd3ea902c5a7ffb0d3a56c8bf1248724bb41d`, pushed to GitHub main.
Developer ID team: `P6GH8ZH6R2`.
Apple notarization accepted: `2a8fc914-e426-4eaf-a336-82708e7f0f86`.

The app and DMG are signed, notarized, stapled and Gatekeeper-accepted. Updater signature verification and actual Tauri extraction passed for 85 archive entries, including the BFL instruction attribution and license.

| Artifact | SHA-256 |
| --- | --- |
| ALi-Imagine_0.9.36_aarch64.dmg | 4a139a9b4c350e268080fa5484f420f0e614d70a9fdca1325ba34354f275bd80 |
| ALi-Imagine.app.tar.gz | 4d35667566c317438dbd41f8d5e100bf1c1fa574598c05d463a0ed84c3e9a23e |

336 frontend tests, 621 Rust tests, production build, rustfmt and strict Clippy passed. 96 optional native/model-dependent Rust tests were ignored in the ordinary suite. Twelve MCP tests and two guarded skill-helper tests passed. Production App browser checks covered automatic/caption submission, manual refinement, stale layout/canvas protection and caption metadata; UI IPC was mocked.

Signed native proof completed four sequential 512x512 Distilled renders: raw caption, automatic expansion, reference edit and locked layout. A real installed 0.9.36 MCP queue job then completed a 512x512 Base image at 25 steps / CFG 2.7 / seed 42037. Default-auto binding, the 1,456-character caption, original text, exact sampling, geometry and output checksum were verified. Expansion took 9.14s and native inference 48.70s in that individual run; these are not speed guarantees.

The selected assistant was ChatGPT gpt-6.1-sol. Official PUP weights were not installed. BFL instruction revision: `3f3edb52b2c55de0d49feab28598b68f7f8e4830`; instruction JSON SHA-256: `b5da3ed8bc04ab59dbdb747930f7dbff847e868903fed8028f85ee1a4ac82fb4`.

Image weights, pinned model revisions and native worker are unchanged. Existing generation certifications remain valid. Native worker SHA-256: `8a422da6a9bf5a6c2db18a078c9d3882fa23a5fc631f495c1ae11b3e8a5699d4`. Installed executable matches the signed bundle: `eba7b833032bcbc70cbbcd477c6089d59bfbe4dfe9ac75e4a7ec55e35f142214`. Live MCP reports 0.9.36. Previous app, coherent database backup and skill were retained before installation. Public H3 remains authorization-gated.

Skill 1.4.1 ZIP is reproducible, checksum-verified and matches all eight source files and the installed standalone skill.
