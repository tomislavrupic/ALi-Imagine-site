# ALi Imagine 0.9.20 — Laptop rendering and latest creative tools

This update combines paired laptop rendering with the latest H3/PDD, custom step controls, live render previews, background activity, Horror 80s and Person Remover styles, keyframes and X2 preparation.

Pair once over your private Tailscale network, then use **Connect laptop / Disconnect laptop** beside the queue. New jobs alternate across Macs with compatible engines, exact models and required runtime readiness. Completed laptop results return to the original Gallery. Accepted work can finish after Disconnect; cancellation remains pending until the laptop confirms it.

## Updater repair

The updater package has been corrected after an archive-unpacking failure. If an earlier attempt failed, select **Check for updates** again and retry installation. The app version remains 0.9.20.

## Setup

1. Use the update icon on both Macs to install 0.9.20.
2. On the laptop, keep Tailscale connected and open **System → Laptop rendering → Accept render jobs on this Mac**.
3. Copy its pairing link; paste it into the Studio's Laptop rendering panel and select **Pair laptop**.
4. Use **Connect laptop** beside the queue. Keep ALi open on both Macs.

The laptop needs matching installed models and its own provider credentials. Requests that exceed its memory or lack required dependencies stay on the Studio without changing settings. The current PDD recipe requires 96 GB, so it stays on the Studio when paired with a 48 GB laptop. Trained model and adapter data remain in the local model library and are not bundled in the updater.

H3 execution remains authorization-gated in the public app. Existing licensing, model certification and engine readiness requirements remain in force.

## Verification boundaries

All 250 frontend tests and 514 Rust tests pass, with 80 opt-in/model-dependent Rust tests ignored. Formatting, Clippy, the production build and 21 Python runtime mathematics tests pass. Developer ID signing, Apple notarization, Gatekeeper and updater signature checks are recorded in the release evidence. HTTP integration tests verify receipt recovery, cancellation and checksummed Gallery import. A native Metal WARP HTTP smoke test rendered a two-second MP4 on the Studio during remote-render development.

Physical laptop installation and two-Mac rendering require that machine's setup and verification. These checks do not certify every model or establish laptop render speed.
