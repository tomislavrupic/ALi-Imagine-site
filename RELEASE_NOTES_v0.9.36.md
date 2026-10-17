ALi Imagine 0.9.36 adds automatic FLUX 3 caption expansion using BFL’s official instructions through your selected Prompt Assist connection. Your original Signal stays intact, and Output Info reveals the exact render caption and assistant model. No PUP model download is required. Turn off automatic expansion when supplying an already prepared caption.

Full captions are retained without the former 1,000-character truncation. Editing references keep their order; layout IDs and coordinates stay locked. Recorded captions are reused for replays. Cancellation prevents a late caption response from restarting a stopped job, and owned local Prompt Assist runtimes unload before FLUX rendering.

The recent Hugging Face changes updated caption guidance and configuration; the Base and Distilled weight files are unchanged. This update does not claim faster MLX rendering. Existing FLUX certification remains valid because the image worker is unchanged.

Includes all prior Base Steps/CFG controls, engine-specific LoRA browsing, native generative 2× upscaling, Draft/1K/2K/4K output, ten references, layout controls and Explore Prompt Assist. ALi Resolve skill 1.4.1 documents the new automatic/caption modes. Public H3 execution remains authorization-gated.

Real signed native tests passed raw-caption, automatic-caption, reference-edit and locked-layout rendering. The automatic caption test retained 1,327 characters. Tests used the existing selected ChatGPT gpt-6.1-sol connection; official PUP model weights were not installed. The macOS app and DMG are Developer ID signed and Apple notarized; the updater is signed and verified.

Validated with 336 frontend tests and 621 Rust tests, plus MCP, skill and browser checks. Installed 0.9.36 also completed an automatic-caption Base render at 512×512, 25 steps and CFG 2.7; the 1,456-character caption, original prompt, sampling and output checksum were verified. Caption expansion took 9.14 seconds and native rendering 48.70 seconds in that individual run.
