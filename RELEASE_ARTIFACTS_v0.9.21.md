# ALi Imagine 0.9.21 release evidence

Source: https://github.com/tomislavrupic/ALi-Imagine/commit/4b4c8bb379af86d6a6f7ecc000d9e310e02e94d1
Review: https://github.com/tomislavrupic/ALi-Imagine/pull/13
Merged main: 8337f5a42988d5f6e47cce219963569e9a06f42e.
Apple notarization: cc0e3af1-bac0-4755-8a19-104e4794ee49 (Accepted).
Developer ID team: P6GH8ZH6R2. App and DMG stapled; Gatekeeper assessments accepted. The updater was rebuilt from the stapled app without macOS metadata, then signed and verified against the existing bundled public key.

SHA-256:
- ALi-Imagine_0.9.21_aarch64.dmg: 42cf83e149b252b4942af6c9cf2d925652baabbcd6711046f3dab54efee29b39
- ALi-Imagine.app.tar.gz: 5c4ebe2d3e8536350f56336a42cb0325251c3cd5e9e43340de1e961585656f26

250 frontend tests and 515 Rust tests pass; 81 opt-in/model-dependent Rust tests ignored in the standard suite. Formatting, Clippy and production builds pass. The newly added native Tailscale read-only test was explicitly run and passed against the installed macOS Tailscale app without Terminal environment variables.

The original bug was reproduced: the unforced Tailscale executable returned a GUI startup message with exit code zero, causing JSON parsing to fail at line 1 column 1. With TAILSCALE_BE_CLI=1, it returned valid connected-device JSON. The new regression test verifies that CLI mode survives the Finder-style environment. No Tailscale configuration was changed during diagnostic tests.

The final app reports version 0.9.21. The release gate extracted all 64 archive entries using the same path layout as Tauri updater 2.10.1, then verified the extracted app with codesign, Gatekeeper and stapler. There are no AppleDouble metadata entries.

Physical installation, Accept render jobs setup and end-to-end rendering on the user's laptop are not claimed. Both Macs must use the same app version before pairing.
