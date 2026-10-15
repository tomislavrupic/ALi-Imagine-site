# ALi Imagine 0.9.33 — FLUX 3 resolution, layout and native upscale

- Keep Draft 512, use 1K by default, choose 2K Quality or native 4K Advanced.
  Aspect ratios and explicit sizes support native canvases up to 4096 pixels per
  side. Historical presets keep their original dimensions when reused.
- Native FLUX 3 generative 2× upscale is available in Image Edit's resolution
  control. It derives exact delivery size from the EXIF-oriented first source,
  uses a native aligned canvas, and trims only grid padding. Source sides must
  be 32–2048 pixels. Fine details, faces and lettering can be redrawn; inspect
  each result. This uses image editing, not a dedicated super-resolution model.
- Edit with up to ten ordered reference images. Layout boxes can place objects
  in the output or select and move a region from a named reference.
- Preserve reference order, original checksums, effective layout conditioning,
  delivered dimensions, native canvas, upscale factor and measured inference
  time in the existing job and output provenance.
- Fix the Render Time panel for FLUX images. New outputs expose their measured
  inference time; older completed jobs use saved render-start and completion
  timestamps, excluding queue waiting.
- Reduce high-resolution attention and decoder workspace using exact query
  batching and convolution strips. Attention retains all keys, convolution
  retains its halo, and normalization still sees the full image.
- Includes all prior Qwen 2.1 model choices and Explore Local/Atlas workflows,
  plus the ALi Resolve Codex skill 1.2.0 with FLUX 3 capability guidance.

A real 4096×2304 render on the M3 Ultra 96 GiB Mac completed in 1080.48 seconds
(18 minutes), reporting 36,552,153,312 bytes peak MLX memory (about 34 GiB).
This is one run on this machine, with other activity during sampling, not a
speed guarantee. A full 4096×4096 image was not rendered in this validation;
its decoder-only memory check passed. Keep 4K as an advanced, slower option.

FLUX 3 uses the distilled BF16 model at 16 steps without CFG. Model weights
remain a separate approximately 20 GB download requiring Hugging Face access.
The optional BFL 9B prompt upsampler, Base training and FP8/NVFP4 are separate
from this profile. Public H3 execution remains authorization-gated.
