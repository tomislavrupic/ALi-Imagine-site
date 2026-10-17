# FLUX 3 Image Klein distilled

ALi 0.9.35+ exposes two separate BF16 models through native MLX/Metal.
Provider: `flux3_mlx`.

- Distilled (default): `black-forest-labs/flux-3-image-klein`, 16 steps, no CFG.
- Base: `black-forest-labs/flux-3-image-klein-base`, defaults to 50 steps, CFG 3.5. Slower;
  separate weights and real generation/edit certification are required.

Keep the exact `modelId` in requests and saved recipes. Check readiness with
`ali_engine_status` and `model_id` set to that repository; an omitted model ID
checks Distilled. Certification for one model never enables the other.
Base sliders support 1-100 whole steps and CFG 1-10 (UI increments 0.1). Use
`providerOptions.steps` and `providerOptions.guidance`; omitted values keep 50/3.5.
Output metadata records the actual sampling recipe separately from the default
certification profile. Lower step counts trade refinement for speed; custom values
do not imply individual visual certification. Distilled stays fixed at 16/1 (no CFG).
Negative prompts and image-strength overrides are unsupported in both profiles.
Do not attach FLUX 2 LoRAs. Base inference does not expose training or LoRA training.

## Resolution

`resolution`: `flux3_512`, `flux3_1k`, `flux3_2k`, `flux3_4k` means a long edge of
512, 1024, 2048 or 4096 pixels. `aspectRatio`: `1:1`, `16:9`, `9:16`, `4:3`,
`3:4`, `3:2`, `2:3`, or `source` when an image is selected. Dimensions round to
the nearest 16 pixels. 4K square is 4096x4096; 4K 16:9 is 4096x2304.

For explicit dimensions use `resolution: "flux3_custom"` and
`providerOptions: {"width": 3840, "height": 2160}`. Both sides must be 64-4096,
multiples of 16. These are native generation sizes, not delivery upscales.
Large renders require more unified memory and time. An allocation failure is a
failed job: never silently reduce the dimensions or resubmit it at another size.
Historical `rapid`, `local_standard`, `landscape` and `portrait` presets retain
their old dimensions for reruns.

## Native generative 2x upscale

The output-stage **FLUX 3 2x** button queues this same native operation.
Use `operation: "image_edit"`, `resolution: "flux3_upscale_2x"`,
`aspectRatio: "source"` and `providerOptions.flux3_upscale_factor: 2`.
The first reference sets the size; its sides must be 32-2048 pixels. ALi derives
exact 2x delivery dimensions from the EXIF-oriented source, prepares a 16-pixel native canvas,
and trims only grid padding when needed. It never silently caps the scale.
Describe preservation of the original composition, identity, colors and text in
the prompt. This is FLUX 3 image-conditioned generation at the target size,
not a dedicated super-resolution checkpoint. Fine detail can be redrawn; inspect
faces and lettering. Original media, ordered references and the upscale factor
remain in the existing job/output provenance.

Draft remains 512, Default is 1K, Quality is 2K, and native 4K is Advanced.

## Editing and reference order

Use `operation: "image_edit"`, 1-10 distinct imported image `sourceAssetIds`,
and the first ID as `sourceAssetId`. The order defines `ref_image_0` through
`ref_image_9`. Inspect the images before submission and keep their checksums.
Text generation uses `operation: "image_generate"` with no reference IDs.
Each reference in a multi-reference edit is prepared under 1 MP on a 16-pixel
grid. A single reference is fitted/padded under 4 MP; original files stay intact.

## Layout boxes

Add `providerOptions.flux3_boxes`, an array of at most 64 rows. Coordinates are
`[y_min, x_min, y_max, x_max]`, normalized 0-1 from the top-left, with positive
area. IDs must be unique and begin with a letter; descriptions must be nonempty.

Place a new object:

```json
[{"id":"balloon","desc":"a red balloon","bbox":[0.08,0.10,0.45,0.42]}]
```

Select an object from the second reference and place it in the output:

```json
[{"id":"bird","desc":"the chrome bird","from":"ref_image_1",
  "src_bbox":[0.1,0.2,0.8,0.9],"tgt_bbox":[0.2,0.3,0.9,1.0]}]
```

`from: "target"` uses `tgt_bbox` only. A reference origin requires `src_bbox`;
its `tgt_bbox` is optional. Do not combine `bbox` with the edit rectangle fields.
ALi converts these boxes to BFL's 0-1000 canvas in the effective prompt and
records both the user's prompt and the exact layout conditioning in provenance.
Boxes guide the model; inspect the result rather than assuming exact placement.

BFL's optional 9B prompt upsampler is a separate model and is not installed or
silently substituted by this integration. ALi's existing prompt assistance
remains separate. Base training, FP8 and NVFP4 are not exposed by these native BF16 profiles.
Explore 360 Scene has source-aware Draft/Refine Prompt Assist. It follows the
user-selected local Qwen or ChatGPT connection and requires review before applying.
It is separate from BFL's prompt upsampler and does not generate an image by itself.

Prompt assistance: see [FLUX 3 prompting](flux3-prompting.md).

Reference: https://github.com/black-forest-labs/flux-3-image-klein
