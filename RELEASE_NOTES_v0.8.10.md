# ALi Imagine v0.8.10

Version 0.8.10 brings the ALi Resolve panel into the native local-video workflow and makes current work easier to track.

- The Resolve panel can capture the current viewer frame plus enabled timeline audio under the playhead and enqueue an LTX 2.5 native lip-sync render.
- Timeline audio uses the exact source offset, a bounded duration, and a 48 kHz stereo handoff. Retimed clips are supported; complex Fairlight mixes should be bounced first.
- The Resolve panel now has a Qwen Prompt Assist Refine action with visible elapsed feedback and the same unified-memory render guard as the main app.
- Captured frames are registered once and reused between Refine and Generate.
- The current render appears in Recent Outputs and Library with green progress and its prompt; Output Info follows it until another output is selected.
- Completed assets have clearer coral status treatment and readable prompt previews.
- The 20-second duration option, Render Queue cancellation, Image Video end-frame slot, and recoverable Move to Trash behavior remain available.

This macOS Apple Silicon build is ad-hoc signed for direct testing and is not Apple-notarized. If macOS blocks the first launch, Control-click the app and choose Open.
