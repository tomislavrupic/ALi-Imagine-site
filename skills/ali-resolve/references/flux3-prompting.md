# FLUX 3 Prompt Assist

Use [BFL's current FLUX 3 Image guide](https://docs.bfl.ai/guides/prompting_summary),
[editing guide](https://docs.bfl.ai/guides/prompting_editing_multi_reference) and
[layout guide](https://docs.bfl.ai/guides/prompting_layout).

Write the finished frame: medium, subject and relationships, setting, lighting,
framing and concrete visible detail. Preserve the user's style and priorities.
Quote exact text. For edits, name the target, change and keep constraints.
Keep reference order and explicit roles; image 1 is ref_image_0. Preserve existing
layout IDs, coordinates and user-provided JSON. Never invent extra references,
identity details or box rows. Review results before applying or generating.

The hosted API has different fields from ALi's native Klein integration. Do not
remove local seeds or substitute hosted resolution/sampling settings. Distilled
uses 16 steps without CFG; Base defaults to 50 steps with CFG 3.5 and supports configurable native steps/CFG in ALi 0.9.35+. These settings belong
in the request, not the caption. Native edits/upscales do not guarantee exact
pixel restoration.

In ALi 0.9.36+, new UI/MCP FLUX requests automatically expand through the
selected local Qwen or ChatGPT Prompt Assist connection using BFL's pinned
`system_prompts.json` (revision `3f3edb52b2c55de0d49feab28598b68f7f8e4830`).
This uses the existing assistant, not BFL's 9B PUP weights. Keep the selected
connection; do not silently switch providers or download the PUP model.
`providerOptions.flux3_prompt_mode` is `auto` for a request needing expansion,
or `caption` for an already expanded caption or an exact prompt comparison.
An expansion error blocks generation; fix Prompt Assist or explicitly supply
a complete caption. Missing-mode historical jobs retain their original prompt.
Inspect `flux3_prompt_expansion` in the execution snapshot, output metadata,
or completed job result for the original text, caption, actual assistant model,
instruction revision/hash and elapsed time. Reruns reuse the recorded caption.
User boxes remain authoritative and are appended once by the image worker.
Manual Refine produces a full caption without the old 1000-character truncation;
layout drafts keep automatic layout-aware expansion enabled.

Explore 360 Scene supports source-aware Draft/Refine for its scene description,
with a review step and protection for text/source changes during refinement.
