# ALi Imagine 0.9.39 verification receipt

Source: `164e39b5499594ab07c4e7722370d7a555e5f5d4`, pushed to GitHub main.
Developer ID team: `P6GH8ZH6R2`.
Final Apple notarization accepted: `09fbb53f-6ec8-4a30-bf19-470bf079f31e`.
App and DMG are signed, notarized, stapled and Gatekeeper-accepted. The signed
updater passed public-key verification and actual Tauri extraction for 92 entries.

| Artifact | SHA-256 |
| --- | --- |
| ALi-Imagine_0.9.39_aarch64.dmg | 4b7aa3d392fa6006b68749023f00b197a133b0482a12625b04d1aeefa9ff974a |
| ALi-Imagine.app.tar.gz | c5ea1181426b333f59ecc40a401e42df7cdf0c92d07f17244ca3f84d42fcbf91 |

341 frontend tests, 628 Rust tests, production build, rustfmt, strict Clippy,
22 Qwen installer tests and 12 MCP tests passed. 98 optional tests were ignored
by the ordinary Rust suite; Turbo's native test was explicitly executed separately.
Browser IPC is mocked. Browser checks cover separate variant readiness, fixed
Turbo sampling, raw prompts, original-model 2x, omitted-step restoration,
certification refresh and the first-certified-Qwen case. Review findings were
fixed with regression tests; the final focused review found no important issues.

Turbo's independent native six-render Signal Test passed: generation, two-reference
editing, transparency generation/editing and byte-identical cache parity. It used
runtime SHA-256 `18fcf3510bff5141ec1004caa2595e7fb254466d9a221a2f5bf92f438809a1d8`.
Full/Unlocked runtime remains `31239e92f2179ccefdf9fa972f7808e8277b0921caf5d3f1ead76635b585d726`.
The first debug-harness file preflight was stopped before any native child started;
only the completed optimized probe counts as certification. Optional visual QA of
all signal-test images remains separate from technical readiness.

Installed-app MCP portrait jobs used the same refined prompt, 1024x1024, seed42050,
CFG1, opaque output and prefix cache on, without another Refine call:

- Turbo: `job_f897912addbc4a489711bfdf3e303438`, 8 steps, **79.360892s**.
  PNG SHA-256 `2db39e31af644cbca015d0fc5807667bc27f1426a1990e442e6ff3a80b6fa032`.
- Unlocked: `job_b1e8e38616f04a1f91588bfdd30e6981`, 40 steps, **262.888466s**.
  PNG SHA-256 `11c7ed458c21de28b378b704e83ec774295c58e0c56dffae0e6154c9306bd837`.

Actual PNG sizes, checksums, stored prompt/settings and model/runtime identities
were verified. Unlocked is byte-identical to its previous refined portrait.
Turbo retained natural skin detail, blue eyes, dark hair and soft window light,
with small face/framing differences. This single end-to-end comparison yielded
3.31x speedup including validation/loading. Server processes were cold; OS
filesystem caches were not controlled. It is not a universal speed/quality claim.
No new native Turbo2K upscale or Turbo angles acceptance is claimed; angles remain
Full-only. Existing models, originals, projects, queue and output lineage remain.

The final installed app includes readiness UI fixes added after the portrait runs;
its executable SHA-256 is `1c9199716df53f3fb28bd6ae23a2b663e786b5b1020f8f1cf49efd6d48407842`.
That executable matches the final signed bundle. Native image runtime and portrait
sampling code are unchanged by those UI fixes. Live MCP reports0.9.39 and Turbo
configured=true. Previous apps/database backup were retained, and no active render
was interrupted. ALi Resolve skill1.4.1 remains compatible; MCP descriptions now
include Turbo and model-specific Qwen status. Public H3 remains authorization-gated.
