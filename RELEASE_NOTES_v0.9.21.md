# ALi Imagine 0.9.21 — Fix laptop setup

Fixes **Accept render jobs on this Mac** failing with `expected value at line 1 column 1` when ALi is launched normally from Finder or Applications. Tailscale's macOS executable needs an explicit CLI mode in this environment; without it, it can start its GUI and return text instead of JSON. ALi now forces CLI mode for every Tailscale setup command and provides readable status errors.

Update **both Macs** to 0.9.21, then enable **System → Laptop rendering → Accept render jobs on this Mac** on the laptop. Copy its pairing link to the Studio, pair once, and use **Connect laptop / Disconnect laptop** beside the queue. Both Macs must run the same version. No Terminal commands are required for normal setup.

This release retains all 0.9.20 rendering, H3/PDD and preview changes, plus the corrected updater packaging and extraction gate. Compatible engines and exact model dependencies remain required; unsupported laptop jobs stay on the Studio. Existing H3 authorization and model certification requirements remain in force.

The original error was reproduced on a Mac without Terminal environment variables, then resolved by forcing CLI mode. A real connected Tailscale installation was tested in that environment using read-only status commands. Signed release, extraction and verification evidence is recorded separately. Physical installation and end-to-end rendering on the user's laptop still require that machine's run.

Tailscale documents this macOS behavior in its [CLI reference](https://tailscale.com/docs/reference/tailscale-cli?tab=macos).

## Verification

250 frontend tests and 515 Rust tests pass, along with formatting, Clippy and production builds. The real Tailscale CLI test passes without Terminal environment variables. The notarized updater passes signature verification, Tauri-compatible extraction, Gatekeeper and stapled-ticket validation.
