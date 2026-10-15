# ALi Imagine 0.9.32 — FLUX 3, Qwen models and Explore

FLUX 3 Image Klein distilled replaces FLUX 2 in Create and Explore reconstruction.
The new engine runs locally through ALi's native MLX/Metal implementation using
BF16 weights, 16 steps and no classifier-free guidance.

- Generate images and edit a reference image in Create. Explore reconstruction can
  supply its ordered camera guide and original-image pair.
- The System setup card shows runtime, weights and real signal-test readiness.
- Model downloads use a pinned revision, file sizes and weight SHA-256s. Weights
  are separate from the app: approximately 20 GB, with 40 GiB free required.
- Accept access on https://huggingface.co/black-forest-labs/flux-3-image-klein and
  use your Hugging Face login during setup. The FLUX Kommunity License applies.
- Original images, historical FLUX 2 identities, queue records and provenance are
  preserved. Dream Score retains its separate FLUX 2 implementation.
- Includes **Qwen 2.1 Uncensored · Q8** as a separate model choice under the existing
  Qwen engine, with its own install, verification and real Signal Test. The
  standard model remains the default, and saved requests retain their model ID.
  The variant requires its 7.56 GB transformer plus the standard pack's companion
  components. Queue, transparency, caching and remote rendering use the selected
  model's identity and certification; the Angles adapter remains standard-only.
- Includes all current **Explore Local/Atlas** workspace updates: local scene
  recovery, calibrated camera controls, reconstruction prompts, source-aware
  review and the versioned camera-to-video handoff.
  Local scene coverage remains dependent on the supplied views; inspect each take.

Local smoke tests on an M3 Ultra with 96 GiB unified memory completed a 512×512
text render in 13.05 seconds and a two-reference edit in 31.95 seconds. These are
worker timings for one machine, not a speed guarantee or comparison against Base.
The actual queue-to-output path and ordered reference provenance were also tested.

Public H3 execution remains authorization-gated. The separate private H3 test app
is not included in this public download or updater. FLUX 3 Base training, LoRA
training, FP8/NVFP4 and ten-reference editing are not exposed by this integration.

This release snapshots the complete current ALi checkout, including the current
Qwen and Explore updates. Scene-builder replacement research is included as
source documentation; it is not advertised as a shipped reconstruction backend.
