# ALi Imagine 0.9.27 — Faster repeated prompts and steadier rendering

- Reuse exact LTX prompt embeddings across generation and upscale. Model, tokenizer or encoder changes invalidate cached entries; an unavailable cache falls back to normal encoding.
- Reduce unnecessary work in LTX 2× upscale by skipping synthesized-audio decoding when the original source track is preserved. Keep adjustable steps and the 2-step default.
- Fix a reproduced database-lock failure when gallery/status refresh overlaps render progress writes.
- Use a compact Output Info chevron and evenly spaced, centered footer status dots.
- Check MP4 encoder completion and frame count, clean up failed exports, and record separate video-decode/export timings.

On one small repeated-prompt generation sample, elapsed time fell from 92.32 to 21.33 seconds; a small warm upscale changed from 12.03 to 11.80 seconds. These are single-run measurements on the same Apple Silicon Mac, not a general speed guarantee. Previously unseen prompts still require encoding. Decoded before/after video frames matched exactly in the tested clips; source dimensions, frame rate, duration and audio were checked separately.

Validation includes 258 frontend tests, 538 Rust tests, 63 Python worker tests, native cancellation/recovery, and an imported-video upscale through the signed app. Existing compact controls, inline Takes, gallery dragging and independent No text / No music / No voice checks are retained. SeedVR2 remains retired.

Developer ID signed and Apple notarized for Apple Silicon macOS. Existing projects and models are preserved. Public H3 authorization requirements are unchanged; private H3 builds remain separate. No model weights or user media are included.
