# ALi Imagine 0.9.38 verification receipt

Source: `3f4679b722579a2530e3d4ee22c0eccee22cb439`, pushed to GitHub main.
Developer ID team: `P6GH8ZH6R2`.
Apple notarization accepted: `5a28d87d-20cf-4532-9b03-404007549922`.

App and DMG are signed, notarized, stapled and Gatekeeper-accepted. The signed updater passed public-key verification and actual Tauri extraction for 85 entries.

| Artifact | SHA-256 |
| --- | --- |
| ALi-Imagine_0.9.38_aarch64.dmg | af16d1d89a2c9b214e77fb4ce0debe8b28a3fe5b55f81f438d37bc40ce6cc12a |
| ALi-Imagine.app.tar.gz | f4767ca17e661804b7d1d999195d5c7c7db3289706f0dbb8a39057cad6f33fb7 |

339 frontend tests, 625 Rust tests, TypeScript/Vite build, rustfmt, strict Clippy and 12 MCP tests passed. The ordinary Rust suite ignored 97 optional tests. Browser smoke covered Full/Unlocked output routing with a different selected engine, exact doubling, original source identity, Redo, small-image ordinary-preset transitions and rejecting unsupported 4K output; browser IPC was mocked. Backend regression verified that changing an original before first import cannot redefine its recorded render checksum. Focused review found no remaining important issues.

Installed 0.9.38 completed native MCP job `job_22d6167c470c40e688ff05e78af045e6` using the production request builder. Original output `output_3abf1bc157e34914810ba2312a39afc7` was a 1024×1024 Unlocked portrait. Native result `output_cbe4b391a36143d2a1eba4e90d1d2877` is 2048×2048, 40 steps, CFG 1, seed 42058, prefix cache on, transparency off. It uses `qwen-image-2.1-uncensored-q8`; no Refine or FLUX inference occurred. Exact prompt/settings, model/runtime identity, source-origin link, snapshot marker, derivation input and PNG dimensions/checksum were verified. The original file is unchanged.

Original SHA-256: `11c7ed458c21de28b378b704e83ec774295c58e0c56dffae0e6154c9306bd837`.
2× PNG SHA-256: `0254fe153e055f67fa44f5881b7ff79ec1a3b84702ab97232f374071ae5e9e15`.
Queue to completion: **1112.92s (18m 33s)** including validation/loading. This is a single observation, not a speed guarantee. Full-size visual inspection found the face, pose, composition and lighting remain close to the source, with reconstructed skin/hair detail. Pixel identity is not promised; Clean Upscale 2× remains the deterministic resize alternative.

The new native proof covers Unlocked at 2K. Full routing/provenance has regression and browser coverage plus its independent existing native certification; no new Full-at-2K or alpha render is claimed. Model weights and native image worker are unchanged. Runtime SHA-256 remains `31239e92f2179ccefdf9fa972f7808e8277b0921caf5d3f1ead76635b585d726`.

Installed executable SHA-256 matches the signed bundle: `2aae5b60f2969724a6986d6a29993aec45a260c247144cf92dd46ae9bca5acb4`. Live MCP reports 0.9.38 and installed MCP descriptions match source. Previous app and coherent database backup were retained; active LTX renders finished before installation. Existing queue, model library, projects and outputs were preserved. ALi Resolve skill 1.4.1 remains compatible. Public H3 remains authorization-gated.
