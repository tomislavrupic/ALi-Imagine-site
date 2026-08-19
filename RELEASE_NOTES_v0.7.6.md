# ALi Imagine v0.7.6

## Independent Prompt Assist and external model libraries

Version 0.7.6 makes Prompt Assist an ALi-owned local capability and adds a safe, explicit destination for large model downloads.

### Highlights

- Installs a pinned `mlx-serve` 26.8.9 Prompt Assist runtime inside ALi's own Application Support directory.
- Reuses a verified local Qwen model without requiring Sirius to remain installed or open.
- Keeps Prompt Assist warm briefly for fast revisions, then releases unified memory before generation begins.
- Lets you link an existing model folder without moving, renaming, or deleting its contents.
- Lets you choose where future large model downloads live, including an external volume.
- Creates an isolated `ALi-Imagine Models` folder and activates completed downloads atomically.
- Preserves existing projects, outputs, credentials, models, LoRAs, and certifications during upgrade.

### Installation

1. Download the Apple Silicon DMG.
2. Drag **ALi-Imagine** to **Applications**.
3. Because this build is ad-hoc signed, Control-click the app and choose **Open**, then **Open**, if macOS shows an unidentified-developer warning.
4. Open **System** later if you want to change the destination for future model downloads.
