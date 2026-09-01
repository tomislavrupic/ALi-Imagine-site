# ALi Imagine 0.9.5 release artifacts

- Source commit: `32b4c29a1a62c4e6179ca9526d95e6404c67092c`
- Apple notarization submission: `82697a51-90d0-4d0d-845d-1a8077da8d6b` (`Accepted`)
- Signing identity: `Developer ID Application: Tomislav Rupic (P6GH8ZH6R2)`
- Bundle identifier: `com.haos.ali-imagine`
- Architecture: Apple Silicon (`arm64`)
- DMG: `ALi-Imagine_0.9.5_aarch64.dmg` — 14,061,674 bytes
  - SHA-256: `4e754a530f54e9f678fd569d6ee8efd0e3fa79cfb6e354d685ca75a74b811ec4`
  - Disk-image checksum: valid
  - Stapler validation: passed
  - Gatekeeper: `accepted`, `source=Notarized Developer ID`
- Updater: `ALi-Imagine.app.tar.gz` — 12,455,211 bytes
  - SHA-256: `69fb0fb26c0956982d2f840a07faa324d2cba82f3368e01af708a7673e7137af`
  - Tauri updater signature: present and non-empty
- Frontend: 20 files / 111 tests passed; TypeScript/Vite production build passed.
- Rust: 269 passed / 66 ignored / 0 failed; formatting and Clippy warnings-as-errors passed.
- Release source: clean detached checkout of the verified application `main` commit above.
