---
name: ali-resolve
description: Operate the installed ALi Imagine bridge for DaVinci Resolve to capture current or In/Out frames, generate LTX video one shot at a time, inspect results, and place takes back on the saved timeline position.
---

# ALi Imagine inside Resolve

Use the installed plugin's Python functions and local HTTP bridge, not simulated native clicks. This skill operates the user's existing ALi/Resolve installation; it does not change app source, install models, switch providers, or modify the plugin.

## Discover and freeze the target

Run `python3 scripts/shot.py status` (paths here are relative to this skill folder). It reads Resolve's current project/timeline and ALi's `/v1/status`.

Installed panel: `~/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/ALi Resolve/ali_resolve.py`.
Resolve module: `/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules`.
Bridge: `http://127.0.0.1:17841/v1`.

Both apps must be running. Confirm the reported project/timeline matches the user's task. The bridge targets local LTX 2.5 independently of ALi's visible cloud/image tab. `ready` is readiness, not evidence that a new generation works. Do not use gallery's latest unrelated output as the current job result.

## One-shot cycle

1. Choose a shot from the current edit/manifest. Use the existing duplicate animatic or a dedicated takes timeline. Position the playhead at the intended insertion frame. For In/Out, set actual Resolve marks and inspect both endpoint images; do not blindly accept an Out on the next cut.
2. Prepare a persistent shot directory under the video project:
   `python3 scripts/shot.py prepare /absolute/project/shots/shot-003-v01 --mode start_frame --prompt-file /absolute/prompt.txt --duration 5 --quality preview`
   Modes: `start_frame`, `first_last` (actual In/Out), `lip_sync` (current frame and timeline audio), `text_only`.
   The helper saves anchors, source hashes, prompt, ALi project ID, Resolve timeline UUID, and insertion frame. It restores the playhead after endpoint capture. It rejects fractional fps because the installed panel rounds timecode; implement verified rational/drop-frame conversion before using such timelines.
3. Inspect the saved anchors with `view_image`; read `shot.json`. Correct framing and endpoint continuity before generation. For lip sync, audition the specific audio source/offset; plugin captures one enabled audio clip, not a mixed timeline render.
4. `python3 scripts/shot.py submit /absolute/project/shots/shot-003-v01`
   Submit only one job at a time. Use authorization already given for generation; do not ask again per shot. Skill creation alone does not require starting a generation. Preview supports 5/10/20 seconds, working 5/10, final 5 in the inspected bridge. Do not change quality to bypass an engine error.
5. `python3 scripts/shot.py poll /absolute/project/shots/shot-003-v01`
   Poll with bounded waits and communicate meaningful progress. Do not resubmit on a timeout: submission is recorded as pending before POST and uncertain submissions require reconciliation against ALi jobs. On failed/cancelled job, retain evidence and diagnose; do not loop automatically.
6. Inspect the returned file with ffprobe and sampled frames, plus playback for motion/audio when available. Check anchor identity, temporal artifacts, duration, resolution, aspect ratio and intended motion. Separate technical validity from editorial acceptance. Record observations in the shot directory.
7. `python3 scripts/shot.py place /absolute/project/shots/shot-003-v01`
   Places only the matching completed job, video-only on a new upper track at the frozen frame. It refuses another active project/timeline and overlapping retry placement. Existing clips/audio remain intact. Verify start/end, source path, and project save. Do not stretch a 5-second render to fill a long storyboard placeholder; plan multiple shots or leave remaining placeholder visible.
8. Continue to the next shot only after this take is reviewed and the prior job is terminal. Failed visual takes remain alternatives, not approved replacements.

Use short motion-focused prompts grounded in each anchor: subject action, camera path, atmosphere and continuity. Keep film-specific rules in the project, not in this generic skill. Preserve model/job/source/output provenance per take. Never overwrite source anchors or publish/export the finished film implicitly.

## Verification boundaries

Report separately: skill installed, bridge connected, frames captured, generation completed, visual review, timeline placement, final render. The helper uses the installed module so future plugin changes may alter behavior: inspect that file when return shapes or errors change. Check every mutation's returned values.
