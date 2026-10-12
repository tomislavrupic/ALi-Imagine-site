# ALi Imagine 0.9.27 release evidence

Source build: https://github.com/tomislavrupic/ALi-Imagine/commit/6831c4ebf0630668bb46259c56fb68e13424bde1
Review: https://github.com/tomislavrupic/ALi-Imagine/pull/17
Merged main: 31061e48c0941ccfbd8d2e11779a568dcbc4bab2. Its source tree matches the built commit.
Apple notarization: d4afbb51-649e-47c0-adec-113a45cbfc77 (Accepted).
Developer ID team: P6GH8ZH6R2. App and DMG are stapled; Gatekeeper accepted both. The updater archive was rebuilt from the stapled app without macOS metadata and signed against the existing bundled updater key. All 64 entries passed Tauri-style extraction, code signing, Gatekeeper and ticket validation.

SHA-256:
- ALi-Imagine_0.9.27_aarch64.dmg: d24c6ac501a80b9f95cb821daabfc41e2e2ec54b4a9d2a17457e506b3f5440ad
- ALi-Imagine.app.tar.gz: bcdc31cc02bc53198b4b4fc0e535b274dbd9e9ed6a4d16f145281007e323411a

258 frontend tests, 538 Rust tests (82 hardware/opt-in tests ignored), 63 Python worker tests, formatting, Clippy and production build passed. The real native cancellation/recovery test was run separately and passed. Browser checks covered existing creation controls, inline Takes, gallery dragging, prompt-assist success/error/retry and inspector/footer polish; mocked IPC does not certify model inference.

Sequential same-input runs on the same 96 GiB Apple Silicon Mac measured a small warm LTX generation at 92.32s before and 21.33s after, and warm 2-step upscale at 12.03s before and 11.80s after. Cold generation was 92.04s before and 96.19s after; cold upscale was 87.79s before and 81.47s after. These are single samples with cold/warm prompt caches, not a guarantee for other inputs or flushed OS caches. Tested decoded video frames matched exactly. Generation audio also matched; imported source-audio delivery retained the existing AAC encoding path.

A signed native app imported an odd-sized audio clip and completed a default 2-step upscale: 270×258 to 540×516, 30 frames at 25 fps, 1.2 seconds, with source audio and lineage. Recorded render time was 84.57s. The final UI-only polish does not change rendering code. Broader visual quality remains separate from technical test success.

The public app is the ordinary default build with H3 execution fail-closed. The private H3 build installed on the development Mac is separate and never uploaded as a public release asset. Model weights, credentials, databases and user media are excluded.
