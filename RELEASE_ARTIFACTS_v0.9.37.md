# ALi Imagine 0.9.37 verification receipt

Source build: `86dc092ffa76fac1c8bad812f36dafa5b2f1d246`, pushed to GitHub main.
Developer ID team: `P6GH8ZH6R2`.
Apple notarization accepted: `8c57d7e7-ccba-4e90-a70e-eb3351c0a06c`.

App and DMG are signed, notarized, stapled and Gatekeeper-accepted. Updater signature verification and actual Tauri extraction passed for 85 archive entries.

| Artifact | SHA-256 |
| --- | --- |
| ALi-Imagine_0.9.37_aarch64.dmg | bcfb1420ac5b4fe8fbaffd720382c39b30f9274f435d8d631e39f78f22e73197 |
| ALi-Imagine.app.tar.gz | 0b88ca0ddb86b938cce61cad643ada5b6138ac6746a74096a29ad76cf1533763 |

337 frontend tests, 623 Rust tests, production build, rustfmt and strict Clippy passed. The ordinary Rust suite ignored 97 optional tests. Extended browser checks covered long Qwen captions, exact trailing quoted text, all ordered references, raw Generate and preserved cache choices; browser IPC was mocked.

A separate signed native assistant test passed four cases using the existing selected ChatGPT gpt-6.1-sol connection. Portrait: 1,077 characters / 8.50s. Photon: 1,494 / 9.45s. Symbolic equations: 2,119 / 13.80s, interpreted as an abstract scene without lettering. Explicit inscription: 984 / 6.07s, retaining quoted “QuantumAddress”. The policy is an ALi-authored adaptation of official Qwen Image 2.1 generation/editing rewrite guidance at revision `ab96caa944157ca28a4f36b695c3047549f48f98`. Dedicated PE weights were not installed.

Installed 0.9.37 completed four sequential Unlocked Q8 jobs at 1024×1024, 40 steps and CFG 1. Portrait raw/refined used seed 42050; photon raw/refined used 42051. Model identity, exact prompts, sampling, native runtime hash, PNG geometry and output SHA-256 were verified. All four full-size PNGs were visually inspected.

| Comparison | Job | Queue to completion | PNG SHA-256 |
| --- | --- | --- | --- |
| Portrait raw | job_5ffddaf11d2442e4be0676a4d8540320 | 218.13s | 386c118f6a3753297d9acd7049a9d8f3ca68e2741a054260272b06b456c598c3 |
| Portrait refined | job_f5ba121dfc7c49cca28bc4a28c940930 | 211.22s | 11c7ed458c21de28b378b704e83ec774295c58e0c56dffae0e6154c9306bd837 |
| Photon raw | job_4af3233bf35d4397b6ff907f8005400d | 205.22s | b356336b89cc98e587ca0ca5423eb6ec633d5ae5bbbb8a5aee38218005e59b2a |
| Photon refined | job_9251d69064f64c1cb1e763ea473f5012 | 213.35s | 0511b522289c8629c0d083a7ef55b6eca1206fb274658f881436b0dcd9a3df6c |

Times include validation/loading, with optional assistant calls recorded separately. This is not a reference-edit cache benchmark or a universal quality claim. Refined portrait light/background are softer; raw has stronger texture and contrast. Refined photon helices/focal points are more distinct; raw is more organic. Raw prompting remains available.

Image weights, pinned revisions and native image workers are unchanged. Unlocked model: `qwen-image-2.1-uncensored-q8`; runtime: `26.10.1-ali-qwen21.1`, SHA-256 `31239e92f2179ccefdf9fa972f7808e8277b0921caf5d3f1ead76635b585d726`. Its separate existing certification remains valid.

Installed executable matches the signed bundle: `26001b47454624390a833bc1a9e1fbccba4db9b13b7973f0c449f3b7c364c063`. Live MCP reports 0.9.37. Previous app and coherent database backup were retained. The MCP schema is unchanged, and ALi Resolve skill 1.4.1 remains compatible. Public H3 remains authorization-gated.
