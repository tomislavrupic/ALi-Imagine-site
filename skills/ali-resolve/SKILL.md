---
name: ali-resolve
description: Operate the installed ALi Imagine bridge for DaVinci Resolve to capture current or In/Out frames, generate H3/LTX and image-engine media through ALi MCP one shot at a time, inspect results, and place takes back on the saved timeline position.
---

# ALi Imagine inside Resolve

Use ALi Imagine MCP for engine/settings control and the installed Resolve plugin's Python functions for capture and timeline placement. Use existing installed services rather than simulated native clicks. Change providers/settings only within the user's requested work; model downloads require explicit authorization. This skill does not modify app source or plugin code.

## Discover and freeze the target

Run `python3 scripts/shot.py status` (paths here are relative to this skill folder). It reads Resolve's current project/timeline and ALi's `/v1/status`.

Installed panel: `~/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/ALi Resolve/ali_resolve.py`.
Resolve module: `/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules`.
Bridge: `http://127.0.0.1:17841/v1`.

Both apps must be running. Confirm the reported project/timeline matches the user's task. The bridge targets local LTX 2.5 independently of ALi's visible cloud/image tab. `ready` is readiness, not evidence that a new generation works. Do not use gallery's latest unrelated output as the current job result.

## ALi MCP routing

Preferred server: `ali-imagine` (registered in Codex). Start with `ali_status`, `ali_list_projects`, `ali_engine_status` and `ali_studio_snapshot`; inspect readiness and actual model/preset capabilities. MCP controls the app on authenticated loopback port 17843. Resolve capture/placement retains the existing 17841 bridge.

For H3, LoRAs, image engines, or explicit LTX quality settings, use `ali_generate` with the canonical request schema exposed by tools/list. Preserve project/source IDs and all requested providerOptions. Never assume arbitrary sampler steps or decode profiles are supported. H3 style certification and licensing gates still apply. `ali_training_workspace` lists project Concepts/adapters; `ali_install_h3_style` downloads only when explicitly requested.

Prepare and inspect anchors using the one-shot cycle below, retaining timeline UUID, record frame, source hashes and exact vocal offset. For MCP submissions, import anchors/audio with `ali_import_source`, then use returned source IDs in the generation request. Record the full request and returned job ID in shot.json before polling `ali_inspect_job`. Do not call the legacy submit command as well: that would create a second LTX job. After uncertain submission, reconcile `ali_list_jobs`; never blindly retry.

For saved shot receipts, use `python3 scripts/mcp_shot.py submit /absolute/shot-directory --request-file /absolute/request.json`, then `mcp_shot.py poll` and, after visual review, `mcp_shot.py place` with that directory. The request file must use ALi camelCase fields (`projectId`, `providerId`, `modelId`, `variationCount`, `providerOptions`). Source IDs must refer to imported, inspected anchors and the exact trimmed vocal audio. The helper records a pending submission before POST, refuses duplicates, and verifies matching output/provider/project before video-only placement.

MCP results are not automatically placed in Resolve. Validate the completed job's output, freeze project/timeline identity and insertion frame, then use `mcp_shot.py place`, the installed plugin's verified insertion function, or Resolve MCP for video-only placement. The existing `shot.py place` is for legacy bridge receipts; do not feed an MCP job response to it without adapting and verifying the receipt shape. Keep original audio and clips intact.

If MCP tools are not available in this chat, reopen the chat after registration. For local diagnostics use `python3 scripts/mcp.py ali_status '{}'`. The helper uses the same installed stdio adapter's authenticated HTTP client, returns JSON and never retries. If the app endpoint is unavailable, report it; do not silently fall back to LTX for a requested H3 job.

## Image and Explore capabilities (ALi 0.9.35+)

For FLUX 3 Distilled or Base, use `flux3_mlx` and the actual model ID returned by the app.
`ali_engine_status` with `engine: "flux"` or `"flux3"` discovers the current
profile and readiness; `flux2` names only the historical engine.
Read [FLUX 3 controls](references/flux3.md) before high-resolution, multi-reference
or bounding-box requests. Use [current prompting guidance](references/flux3-prompting.md)
when drafting or refining FLUX image prompts. Preserve the requested native size and ordered source
IDs. Distilled uses 16 steps without CFG; Base defaults to 50 steps with CFG 3.5. In ALi 0.9.35+, Base supports `providerOptions.steps` (whole numbers 1-100) and `providerOptions.guidance` (finite values 1-10). Distilled remains fixed at 16 steps without CFG.
In ALi 0.9.36+, new FLUX requests automatically expand through the selected Prompt Assist connection using official BFL caption instructions. Use `providerOptions.flux3_prompt_mode: "caption"` for an already expanded caption or an exact comparison; inspect the recorded expansion separately from the original request. Historical recipes retain their original prompt.
Do not substitute one model for the other or relabel an upscale as native generation.
Image outputs stay in ALi's Gallery; the video-only placement helper does not
insert still images into Resolve.

Qwen uses provider `qwen21_mlx` with distinct model IDs
`qwen-image-2.1-full-q8` and `qwen-image-2.1-uncensored-q8`. Inspect the selected
model's readiness; standard certification does not certify Uncensored. Angles
is standard-only. Never switch models to bypass setup or certification.

For Explore, inspect `ali_explore_scenes`; use the discovered schemas of
`ali_local_explore` and `ali_atlas_enqueue` for the requested local or cloud
workflow. Freeze scene version, camera and source identity before capturing a
view. A camera capture is a guide, not proof that unseen surfaces are recovered.
Apply an accepted image to Create through the existing camera-to-video handoff;
retain original source and camera provenance. Downloads and cloud actions still
require the user's scope and authorization.

## One-shot cycle

1. Choose a shot from the current edit/manifest. Use the existing duplicate animatic or a dedicated takes timeline. Position the playhead at the intended insertion frame. For In/Out, set actual Resolve marks and inspect both endpoint images; do not blindly accept an Out on the next cut.
2. Prepare a persistent shot directory under the video project:
   `python3 scripts/shot.py prepare /absolute/project/shots/shot-003-v01 --mode start_frame --prompt-file /absolute/prompt.txt --duration 5 --quality preview`
   Modes: `start_frame`, `first_last` (actual In/Out), `lip_sync` (current frame and timeline audio), `text_only`.
   The helper saves anchors, source hashes, prompt, ALi project ID, Resolve timeline UUID, and insertion frame. It restores the playhead after endpoint capture. It rejects fractional fps because the installed panel rounds timecode; implement verified rational/drop-frame conversion before using such timelines.
3. Inspect the saved anchors with `view_image`; read `shot.json`. Correct framing and endpoint continuity before generation. For lip sync, audition the specific audio source/offset; plugin captures one enabled audio clip, not a mixed timeline render.
4. **MCP route:** submit once with `ali_generate` and save its request/job ID. **Legacy LTX route only:** `python3 scripts/shot.py submit /absolute/project/shots/shot-003-v01`
   Submit only one job at a time. Use authorization already given for generation; do not ask again per shot. Skill creation alone does not require starting a generation. Preview supports 5/10/20 seconds, working 5/10, final 5 in the inspected bridge. Do not change quality to bypass an engine error.
5. **MCP route:** poll `ali_inspect_job` using the recorded ID. **Legacy LTX route only:** `python3 scripts/shot.py poll /absolute/project/shots/shot-003-v01`
   Poll with bounded waits and communicate meaningful progress. Do not resubmit on a timeout: submission is recorded as pending before POST and uncertain submissions require reconciliation against ALi jobs. On failed/cancelled job, retain evidence and diagnose; do not loop automatically.
6. Inspect the returned file with ffprobe and sampled frames, plus playback for motion/audio when available. Check anchor identity, temporal artifacts, duration, resolution, aspect ratio and intended motion. Separate technical validity from editorial acceptance. Record observations in the shot directory.
7. **MCP route:** use verified Resolve insertion at the frozen frame after checking the matching completed output. **Legacy LTX route only:** `python3 scripts/shot.py place /absolute/project/shots/shot-003-v01`
   Places only the matching completed job, video-only on a new upper track at the frozen frame. It refuses another active project/timeline and overlapping retry placement. Existing clips/audio remain intact. Verify start/end, source path, and project save. Do not stretch a 5-second render to fill a long storyboard placeholder; plan multiple shots or leave remaining placeholder visible.
8. Continue to the next shot only after this take is reviewed and the prior job is terminal. Failed visual takes remain alternatives, not approved replacements.

Use short motion-focused prompts grounded in each anchor: subject action, camera path, atmosphere and continuity. Keep film-specific rules in the project, not in this generic skill. Preserve model/job/source/output provenance per take. Never overwrite source anchors or publish/export the finished film implicitly.

## Verification boundaries

Report separately: skill installed, bridge connected, frames captured, generation completed, visual review, timeline placement, final render. The helper uses the installed module so future plugin changes may alter behavior: inspect that file when return shapes or errors change. Check every mutation's returned values.
