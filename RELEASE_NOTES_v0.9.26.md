# ALi Imagine 0.9.26 — Faster upscale and cleaner creation controls

LTX Pixel Spatial 2× now accepts generated and imported videos, defaults to 2 steps, and offers a 2–8 step slider. Distilled generation also exposes 2–8 steps; DEV Quality exposes 2–40 steps with its existing certification boundary. Upscale preserves source aspect, frame count, frame rate, timing, audio and immutable lineage. Creative detail changes are expected.

VIDEO controls use aligned Aspect/Size fields, full-width Delivery and Framing, and three independent prompt checks: No text, No music and No voice. Supplied performance audio is preserved. Gallery media drags into source wells, Finder drops replace an occupied source, Takes open inline, and Outputs returns to grouped clips. Background activity and recent-media navigation are simpler; upscale render time appears in metadata.

Prompt Assist rejects empty output and uses H3-specific prompting guidance. Unchanged H3 installations reuse validated checksum receipts after restart. SeedVR2 has been retired across the app; existing outputs and provenance remain readable. Unneeded cloud/file-persistence controls and API status text have been removed from Create.

Validation: 258 frontend tests, 535 Rust tests (82 hardware/opt-in tests ignored), formatting, Clippy and production build. Browser checks cover pointer/Finder drops, image anchors, inline Takes, narrow layouts, checkboxes and keyboard operation. A real 2-step upscale delivered 2048×1152, 73 frames at 24 fps with source audio; its visual result was approved. Prompt exclusions guide generation, not post-production removal.

The public macOS app retains its existing H3 authorization guard. Private H3 Studio builds remain separate. No model weights are bundled, and existing model licences and installation requirements apply.
