# ALi Imagine 0.9.26 release evidence

Source build: https://github.com/tomislavrupic/ALi-Imagine/commit/a86decef874a497c74b4e8b00b1228b3513ebcb0
Review: https://github.com/tomislavrupic/ALi-Imagine/pull/16
Merged main: 830de4e24fdf20a9db15b079afeb4b3ab6a8d47c. Its source tree matches the built commit.
Apple notarization: 2f1b949c-884f-4fcc-bc54-e0d05aefd278 (Accepted).
Developer ID team: P6GH8ZH6R2. App and DMG are stapled; Gatekeeper accepted both. The updater archive is rebuilt from the stapled app without macOS metadata and signed against the existing bundled updater key. All 64 entries pass Tauri-style extraction, code signing, Gatekeeper and ticket validation.

SHA-256:
- ALi-Imagine_0.9.26_aarch64.dmg: 7a77954d7569d3558ac5a72bd0a93e098dcfa74e6fe43d28c1c6fa3e82fee8ef
- ALi-Imagine.app.tar.gz: 65d0e9b493eadeb337d187063455825e674e42da0792fce2ca24718abccc0330

258 frontend tests, 535 Rust tests (82 hardware/opt-in tests ignored), formatting, Clippy and production build pass. Ten Python pixel-upscale/sampling checks and twelve MCP tests pass. Production-App browser fixtures cover pointer/Finder drops, source replacement, image anchors, inline Takes, narrow controls, keyboard checkboxes, selected steps and command arguments. These fixtures do not certify model inference.

A real 2-step LTX upscale delivered 2048×1152, 73 frames at 24 fps in 281.197 seconds, preserving source audio, immutable source checksum and lineage. The user approved the visual result. The full-resolution source was 16:9; square speed-test crops are not format evidence. Adjustable-step distilled and DEV generation probes are documented in the private source repository.

The public app uses the ordinary default build with H3 execution fail-closed. The separately installed private H3 Studio app is not a public release asset. Model weights, generated film media, local credentials and databases are excluded.
