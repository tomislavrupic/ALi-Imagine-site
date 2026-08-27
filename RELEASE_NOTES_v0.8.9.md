# ALi Imagine v0.8.9

Version 0.8.9 removes phantom local renders after ALi restarts.

- A safely interrupted render no longer appears as an active Background task.
- Interrupted local work no longer blocks Qwen Prompt Assist or keeps queue polling alive.
- Interrupted jobs remain preserved under Attention and can be retried explicitly.
- Failed jobs remain selectable and removable without allowing interrupted history to be deleted accidentally.
- Real queued, validating, and processing renders still block Prompt Assist on unified-memory Macs.
- Cloud-render coexistence, live Qwen elapsed feedback, the 20-second duration option, Render Queue cancellation, and the Image Video end-frame slot remain unchanged.
