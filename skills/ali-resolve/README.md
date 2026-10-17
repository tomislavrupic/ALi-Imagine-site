# ALi Resolve skill 1.4.1

Requires macOS, ALi Imagine 0.9.35 or newer, Python 3, and DaVinci Resolve
with external scripting access. The app installs its Resolve panel and MCP
client when launched. Models are separate downloads.

Copy this entire ali-resolve folder to ~/.agents/skills/ali-resolve (or your
Codex skills directory), backing up any existing version. Keep scripts next
to SKILL.md. No credentials belong in this folder.

Launch ALi Imagine once, then register the stdio client:

```sh
codex mcp add ali-imagine -- python3 "$HOME/Library/Application Support/ALi-Imagine/mcp/server.py"
```

Reopen the Codex chat if needed. Run ali_status and ali_engine_status first.
The app uses authenticated loopback port 17843; the token stays in the
user-only app data directory and is read by the client. The Resolve bridge
uses port 17841. Do not expose either service publicly.

For a read-only connection check:

```sh
python3 scripts/mcp.py ali_status '{}'
python3 scripts/shot.py status
```

shot.py captures frames/audio and handles the legacy LTX bridge. mcp.py
provides direct MCP diagnostics. mcp_shot.py handles canonical request
receipts, polling and guarded video-only placement. Read SKILL.md before
submitting. Generation requires a ready supported runtime and explicit user
intent; H3 remains authorization-gated in public builds. Helpers support
whole-number timeline frame rates; unsupported fractional rates fail closed.

This package contains no app, models, credentials, receipts or media.
