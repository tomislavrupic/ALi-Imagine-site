# ALi Imagine 0.9.33 verification receipt

Source: `bf873bd2152a26d02663bac36cbc8f3a59e09404` on GitHub main.
Developer ID team: `P6GH8ZH6R2`.
Apple notarization accepted: `5e3fac9f-02f6-4b0b-8af7-137eea8f8a57`.

The app and DMG are signed, notarized, stapled and Gatekeeper-accepted.
The updater signature matches the bundled public key. Actual Tauri extraction
verified 82 entries, code signing, Gatekeeper and the stapled app ticket.

| Artifact | SHA-256 |
| --- | --- |
| ALi-Imagine_0.9.33_aarch64.dmg | 7118d3b1604c0c23c3b7a8da14363216ba0dc3c3254fc3f0433e70204926a00c |
| ALi-Imagine.app.tar.gz | 0dfb1bec0883a02544443004ec136caca6a12009ec973bb429bdc35c85ffc8d9 |

Fresh release checks: 325 frontend tests and 610 Rust tests passed (94 native
or model-dependent tests ignored); production build, fmt and strict Clippy passed.
MCP tests: 12 passed. Skill helper tests: 2 passed. Native Python parity and
contract tests: 14 passed. Browser submission verified ordered references,
layout, 4K dimensions and exact 1026x770 upscale delivery on a 1040x784 native
canvas. Malformed saved layout handling and timestamp timing fallback are tested.

Real inference with the final native worker passed text generation and ordered
two-reference editing. A 4096x2304 image completed in 1080.4807 seconds, reporting
36,552,153,312 bytes peak MLX memory; SHA-256:
`55b9bd2fba874cba8774602647e84f4475fb66b0a34cda8596a82ca06bd82497`.
The 4096x4096 check was decoder-only, not a full image generation test.

Public H3 remains authorization-gated. The private H3 test profile is excluded.
Model weights are separate from the installer. No fresh Qwen model inference
is claimed as part of this packaging pass.

Final real queue tests passed:

- queue-ten-refs-final: 2048x1152, 10 ordered references, 138.869 worker seconds; output SHA-256 `08d9fc3a6a6f959eb6f31d23cf9db1050c8fb133078b0b92bf6a2723a1a0f6a8`.
- queue-native-upscale-final: 1026x770, 1 ordered references, 44.899 worker seconds; output SHA-256 `62f4ed90457ec6c5043ab4239f134885dc2e7eb09868a316ca841572ae164f6e`.

The native upscale test used a JPEG with EXIF orientation 6 and uneven sides.
Normalization yielded 513x385; native generation used a 1040x784 canvas and
trimmed grid padding to deliver exactly 1026x770. PNG and OutputAsset dimensions,
source checksums, upscale method and existing queue lineage all matched.

The installed signed app reports version 0.9.33, generation_certified=true,
last_error=null, max_references=10 and max dimensions 4096x4096 through live MCP.
Its executable SHA-256 matches the released build:
`f44a0b29e6a20646050aa7d3b73b6a7fc422d8947289e573177f0bf1b39b66ec`.
