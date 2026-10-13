# ALi Imagine 0.9.29 verification receipt

Public source build: `49068a24b505f94dc754ab9eccb6fc0544d0cdf3`.
Developer ID team: `P6GH8ZH6R2`.
Apple notarization accepted: `dccb99de-23fb-4caf-8645-62aa7dc5250d`.
App and DMG signature, stapling and Gatekeeper checks passed. The updater
signature matches the bundled public key; actual Tauri extraction verified
71 entries, the signed executable and stapled ticket.

| Artifact | SHA-256 |
| --- | --- |
| ALi-Imagine_0.9.29_aarch64.dmg | aeebcadaeacaa381522ac609ce0e5324fe79d461d4d42b545ec23c3aac59ad64 |
| ALi-Imagine.app.tar.gz | 0b6afbe7bd708d78aee1b1e3dbb5329ec782cb7721dd9db79288d4088d23ec42 |

Fresh release checks: 280 frontend tests and 558 Rust tests passed (88
model-dependent tests ignored); production build, fmt and strict Clippy passed.
UI checks recorded on 12 October cover FX selection, independent Restore/upscale
step defaults, Gallery video pointer drops, LTX/H3/Qwen engine switching,
readiness refresh, processing request routing, LTX generation defaults, and
Duration placement with the selected duration reaching the generation request.
Native Finder drag still needs manual validation. No inference code changed in
this release; no new visual-quality or render-speed result is claimed.

Public H3 remains authorization-gated. The separate private local H3 build is
not uploaded as a public download or updater artifact.

The separate private 0.9.29 app was installed only after the queue was idle,
with a verified 0.9.28 rollback copy. The running app-control service reports
H3 `installed=true`, `local_execution_enabled=true`, `generation_certified=true`
and `availability_code=private_local_testing`. This verifies preserved native
readiness; no new H3 render was launched for this UI release.
