# ALi Resolve skill for Codex — 1.0.0

This is the Codex skill used to operate ALi Imagine with DaVinci Resolve on a Mac. It is separate from the ALi Resolve plugin. No Sirius installation or ChatGPT manifest.json is required by this workflow.

## What you need

- Codex running locally on the same Mac as ALi Imagine and DaVinci Resolve.
- ALi Imagine with its Resolve bridge and ALi Resolve plugin installed. This ZIP does not include either app, the Resolve plugin, or models.
- Python 3 available as `python3`. Media review also uses `ffprobe` from FFmpeg.
- Resolve's Python scripting module and permission for external local scripting. If your Resolve edition does not expose external scripting, this helper cannot connect; check the scripting documentation shipped with your Resolve installation.
- A configured local LTX 2.5 runtime for generation. Connection checks do not download models or generate media.

This first export uses macOS paths. Windows and Linux are not supported by this package. It uses an existing installed bridge API; compatibility with every older ALi release has not been verified. Start with the connection check below.

## Easy installation

1. Unzip the download. You will get a folder named `ali-resolve`.
2. In Codex on that Mac, paste this request (adjust the Downloads path if necessary):

> Install the ALi Resolve skill from ~/Downloads/ali-resolve into ~/.agents/skills/ali-resolve. If a version already exists, compare it and preserve a backup before replacing it. Read its README.md and verify Python and the ALi Resolve plugin paths. Do not generate media or change my timeline.

Codex skills are folders; do not import this ZIP as a ChatGPT connector or search for a manifest.json. If the skill does not appear after installation, restart Codex.

## Check the connection first

Open ALi Imagine and Resolve, then open the intended Resolve project and timeline. In Codex:

> Use $ali-resolve to check my ALi and Resolve connections. Tell me the active project and timeline. Do not generate anything or change my timeline.

Or run in Terminal:

    python3 "$HOME/.agents/skills/ali-resolve/scripts/shot.py" status

The helper looks for the installed panel at:

    ~/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/ALi Resolve/ali_resolve.py

It loads Resolve scripting from:

    /Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules

ALi's local bridge is:

    http://127.0.0.1:17841/v1

Missing panel: finish installing the ALi Resolve plugin. Connection refused: open ALi Imagine and confirm its bridge is available. Resolve scripting unavailable: open a project/timeline and check Resolve's scripting permissions and edition support. A successful status check is not a generation test.

## First shot

Use a duplicate or dedicated takes timeline. Once the connection check succeeds:

> Use $ali-resolve to prepare a five-second preview shot from my current frame. Show me the captured anchor and prompt before submitting. Keep the original clips and audio intact.

After reviewing the preparation, authorize generation. Ask Codex to review the completed take before placing it back on the saved timeline position.

The current helper supports text-only, current-frame, first/last-frame and lip-sync preparation. It processes one job at a time and preserves shot receipts and source hashes. Fractional-frame-rate timelines are deliberately rejected pending verified timecode conversion. Lip-sync capture uses one enabled audio clip, not a full timeline mix.

## Package contents

- SKILL.md — workflow instructions
- scripts/shot.py — local bridge helper
- agents/openai.yaml — Codex display metadata
- README.md — this guide

The helper and skill are exported unchanged from the author's local skill. No credentials, media, project databases, model files, or Python caches are included. This export does not claim a fresh end-to-end generation test on another Mac.

Official Codex skill installation guidance: https://learn.chatgpt.com/docs/build-skills
