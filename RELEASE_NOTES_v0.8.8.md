# ALi Imagine v0.8.8

Version 0.8.8 repairs the Qwen Prompt Assist Refine path and makes long-running background work unambiguous.

- Refine can now run while xAI cloud renders continue in the background.
- Local renders still pause Prompt Assist because both workloads share unified memory; the button explains why instead of appearing broken.
- The Refine button and Signal panel show a live Qwen elapsed timer while the local model loads, analyzes, and writes.
- Background work is explicitly labelled `RENDERING`, uses a green active state, and shows phase plus percentage.
- A completed queue flashes coral with `COMPLETE · 100%` for five seconds, so completion remains distinct from an error.
- Unknown render providers fail closed and continue to protect the local Prompt Assist runtime.
- Qwen 4B checksum repair, compact output filenames, the 20-second duration option, Render Queue cancellation, and the Image Video end-frame slot remain unchanged.
