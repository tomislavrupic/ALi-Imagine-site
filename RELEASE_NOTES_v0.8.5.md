# ALi Imagine v0.8.5

Version 0.8.5 repairs the two local-engine regressions reported after the Qwen Prompt Assist setup work.

- Prompt Assist now falls back to an available private loopback port when another local service already owns its preferred port. It never stops or replaces that service.
- Completing or repairing the LTX prerequisite now refreshes both System status and the Create engine list immediately, so LTX Local no longer stays disabled until restart.
- Install, cancel, model download, and verification paths use the same paired LTX refresh behavior.
- Qwen hardware matching, visible download progress, Cancel/Resume, the working 20-second duration, Render Queue cancellation, and the Image Video end-frame slot are unchanged.
- Existing projects, models, originals, settings, and certifications remain preserved.
