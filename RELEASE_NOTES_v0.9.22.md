# ALi Imagine 0.9.22 — Render progress and compact network control

Render phase, percentage and step count remain visible when switching from Preview to Source, Result, FX or 3D. Laptop jobs now send their engine phase and step/total count back to the Studio instead of only a percentage.

The large connection strip has been removed from Recent Outputs. Use the compact network planet icon beside System to connect or disconnect; green means connected. Pairing and detailed status remain in System.

Update both Macs to 0.9.22 before connecting. The previous H3/PDD controls, styles, previews, Tailscale setup and corrected updater packaging are retained. Standard releases preserve H3 execution and certification requirements. A private H3 test build now refuses a public-channel replacement that would disable private testing; it needs a matching private build instead.

Validation: 251 frontend tests; 517 Rust tests in both standard and private H3 configurations (81 hardware/opt-in tests ignored); formatting, Clippy and production builds. A real HTTP regression verifies laptop progress telemetry across isolated databases. Browser fixtures verify visible percentage/steps and the network control at 900/1600px. Public archives are Developer ID signed, Apple notarized, signature verified and extracted with Tauri-compatible path handling.

Physical cross-Mac rendering and inference quality are not claimed by these source and packaging checks.
