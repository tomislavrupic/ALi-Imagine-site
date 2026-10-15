# ALi Imagine 0.9.34 — Base, native upscale and guided scene prompts

- Choose FLUX 3 Image Klein Distilled or Base in Create. Distilled remains the
  fast default at 16 steps without CFG. Base uses 50 steps with CFG 3.5 and has
  separate pinned BF16 weights, setup, readiness and real signal tests.
  Saved requests, output metadata and paired-Mac fingerprints keep the exact
  selected model. Base does not enable training or LoRA training in this release.
- The image-stage **FLUX 3 2×** button now queues native generative upscaling
  through FLUX, replacing that button's Real-ESRGAN route. It preserves the
  original output and Create draft, derives exact size from the EXIF-oriented
  source and records parent output lineage. Source sides must be 32–2048 pixels.
  Fine detail, faces and lettering can be redrawn. The chosen FLUX model is retained.
- Explore 360 Scene gains source-aware Prompt Assist: Draft an empty description
  or Refine existing text, review the proposal and apply it explicitly. Text or
  source changes invalidate an older proposal. It respects frozen scene time
  and the user's selected local Qwen or ChatGPT assistant connection.
- FLUX Prompt Assist now includes rules from BFL's current FLUX 3 Image,
  editing and layout guides: concrete scene descriptions, exact quoted text,
  ordered reference roles and preserved layout IDs. It can inspect all selected
  1–10 FLUX editing references in order. Hosted API settings are not substituted
  for native Klein settings, and the separate BFL prompt upsampler is not implied.
- Retains Draft 512, 1K default, 2K Quality, native 4K Advanced, custom sizes,
  ten-reference generation, layout controls and the fixed Render Time panel.
  Includes the prior Qwen and Explore updates. ALi Resolve skill 1.3.0 is a
  separate download with current model and prompting guidance.

Both models passed real native generation and two-reference editing tests on
the M3 Ultra 96 GiB Mac. Base 512×512 worker timings were 67.30 seconds for text
and 188.83 seconds for a two-reference edit; Distilled measured 24.86 and 33.14
seconds in this validation. These are individual local runs, not speed guarantees.
A further 576×1024 Base generation passed ALi's real queue, immutable output
and provenance checks in 142.18 seconds with 11.6 GiB reported peak MLX memory.

Each model's weights are a separate approximately 20 GB download requiring its
Hugging Face agreement. Base and high resolutions take longer; native 4K remains
advanced. Public H3 execution remains authorization-gated.
