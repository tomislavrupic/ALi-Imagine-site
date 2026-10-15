# ALi Imagine 0.9.32 verification receipt

Public source build: `ec179c5621f289149557bc53326132ec19ba8b89`.
This snapshots all current ALi source updates: FLUX 3, Qwen model selection and
Explore Local/Atlas, including their source documentation.
Developer ID team: `P6GH8ZH6R2`.
Apple notarization accepted: `06476ce1-ead5-4eb7-9c29-32cbad64d0ff`.

The DMG's notarization ticket is stapled and validated, and Gatekeeper accepts
both the DMG and the signed 0.9.32 application inside it. The separately packaged
updater contains the stapled app. Its signature matches the bundled public key;
actual Tauri extraction verified 70 entries, code signing, Gatekeeper and the
app's stapled ticket.

| Artifact | SHA-256 |
| --- | --- |
| ALi-Imagine_0.9.32_aarch64.dmg | 72a82b9c198ac29dd19324f1e5946d077f90b0b79a1b42cb68ed1ab2eb2ce6f6 |
| ALi-Imagine.app.tar.gz | e0897da5e949b6930b031e0f0cf1f471fac1280bbede9a9b1e82b3c22e6c8c0e |

Fresh release checks: 319 frontend tests and 605 Rust tests passed (92
model-dependent tests ignored); production build, fmt and strict Clippy passed.
FLUX 3 was separately verified with the pinned official BF16 model: a real
512x512 text render, ordered two-reference edit and queue-to-output provenance.
Those tests used the installed native runtime; they are not mocked certification.
Qwen model updates are included, without claiming a fresh six-render Qwen run
as part of this packaging pass. Scene-builder replacement research remains
source documentation rather than a new advertised backend.

Public H3 remains authorization-gated. The separate private local H3 build is
not uploaded as a public download or updater artifact.
