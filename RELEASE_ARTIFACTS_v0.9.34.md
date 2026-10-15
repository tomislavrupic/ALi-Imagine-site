# ALi Imagine 0.9.34 verification receipt

Source build: `44f12807ac64ae7a468f88d1a28755458cf03baf`, pushed to GitHub main.
Developer ID team: `P6GH8ZH6R2`.
Apple notarization accepted: `208d7ac8-1c83-405c-8062-1d4d7380103b`.

The final app and DMG are signed, notarized, stapled and Gatekeeper-accepted.
The updater signature matches the bundled public key; actual Tauri extraction
verified 82 entries, signing, Gatekeeper and the stapled app ticket.

| Artifact | SHA-256 |
| --- | --- |
| ALi-Imagine_0.9.34_aarch64.dmg | e089552f10117ca21e3b73609269db8f691e3564623dea35c1de86a564830724 |
| ALi-Imagine.app.tar.gz | a060a32361b06de755d765cfc5637e3cac59ad7d0838761f0f037794f6a21056 |

Fresh final release checks: 328 frontend tests and 613 Rust tests passed (95
native/model-dependent tests ignored); production build, fmt and strict Clippy
passed. Native Python parity/contract tests: 16 passed, including serial Base
CFG against BFL's isolated two-sample pack. MCP: 12 tests. Skill helper: 2 tests.

Real independent native certifications passed for both models: text generation
and ordered two-reference editing. Both certifications use worker bundle
`72b2bf3560f4945136f14442800a734dfefcbee82cd23d36c4099d56608d2da0`.
Base revision: `1469d27cfb9bb1bd81d3a93f5a023b39dbf136e4`.
Distilled revision: `8454017f9ebaada30c998fccd9f67a80c7580f68`.
A real queued Base output additionally verified model/profile identity, CFG,
576x1024 PNG and OutputAsset geometry, SHA-256, timing and memory provenance.

Production-App browser fixture tests verified Base native-upscale submission,
1026x770 delivery on a 1040x784 native canvas, parent output ID and one immutable
reference. Explore Draft required review before application; edits made during
Refine were retained. Assistant responses in these UI tests were mocked. No fresh
ten-image assistant-model inference or Qwen image-model certification is claimed.
Guide contract and source-count tests verify the ordered 1–10 image request.

Installed app version: 0.9.34. Its executable matches the signed build:
`48647af59655c1be20d25c04b440384696e3d7fdfeb951f953d4bbf343e01136`.
Live MCP reports both models certified with no last_error; Base capabilities
show 50 steps, CFG=true and guidance=3.5. Public H3 execution remains disabled.
Skill 1.3.0 is available separately as an exact eight-file source ZIP.
