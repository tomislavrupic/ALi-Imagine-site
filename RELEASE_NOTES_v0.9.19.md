# ALi Imagine 0.9.19 — Laptop rendering

Pair a second Mac over Tailscale, then use **Connect laptop / Disconnect laptop** beside the queue. Connected jobs alternate between the Studio and laptop across ALi's engine families. Incompatible or unavailable laptop capabilities stay local with an explanation; models and settings are not silently substituted.

Completed laptop results return to the original project's Gallery with verified checksums and lineage. Accepted work can finish after Disconnect. Durable receipts prevent duplicate admission, and cancellation/restart recovery keeps uncertain work reserved until reconciled. Update installation is guarded during active rendering and transfers.

## Setup

1. Use the update icon on both Macs to install 0.9.19.
2. On the laptop, keep Tailscale connected and open **System → Laptop rendering → Accept render jobs on this Mac**.
3. Copy its pairing link; paste it into the Studio's Laptop rendering panel and select **Pair laptop**.
4. Use **Connect laptop** beside the queue. Keep ALi open on both Macs.

The laptop needs matching installed models and its own provider credentials. Existing licensing, model certification and H3 authorization restrictions remain in force. No model libraries or API keys are copied between Macs. Private Tailscale HTTPS Serve is required; ALi does not configure public Funnel.

## Verification

237 frontend tests and 489 Rust tests pass, with formatting, Clippy and production builds. HTTP tests cover two isolated databases, receipt idempotence, result integrity, cancellation, disconnect/restart behavior, pairing ownership and update coordination. An explicit native Metal WARP smoke test rendered a two-second MP4 through HTTP and imported it into the Studio Gallery. Independent review found no remaining release blockers after fixes.

Physical installation and mixed-engine rendering on a user's laptop still require that machine's own setup and verification. These tests do not certify every model on every Mac.
