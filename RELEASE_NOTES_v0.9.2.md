# ALi Imagine 0.9.2

## Faster media review

- Clicking an image or video preview opens it directly in the main viewer.
- Newly selected videos open paused at the first frame instead of carrying playback state from the previous clip.
- Video posters remain visible while the first frame is loading, avoiding an empty stage.
- Stage zoom and pan reset when a new output is selected.

## Audio Video Prompt Assist

- `REFINE` is now available beside the Signal field in Audio Video mode.
- Qwen Vision grounds the refined performance direction in the untouched start frame.
- The performance-audio track remains authoritative for timing, vocals, and lip sync; Prompt Assist does not invent lyrics or dialogue.

## LTX 2.5 native 2x stability

- Lock every source token at 95% during three-forward refinement to reduce subject replacement.
- Process longer clips in bounded overlapping chunks instead of isolated hard cuts.
- Blend nine-frame overlaps and reject source-relative seam discontinuities before a derivative enters the Library.
- Preserve source audio, prompt, seed, checksums, and lineage in the immutable result.

## Road to 1.0

- Replace the old feature checklist with a production roadmap covering Fast Path, Spatial Take, Concepts continuity, sequences, finishing, delivery, and the 1.0 trust gate.
- Include master and social roadmap infographics in the source repository.

## Boundary

Re-Frame 3D and the native LTX 2x path remain experimental local workflows. The release adds stronger source preservation and fail-closed validation, but unseen spatial detail and generative video refinement can still change appearance. Originals remain immutable.

## Trust

This Apple-silicon build is Developer ID signed, Apple notarized, stapled, and Gatekeeper accepted. The in-app updater archive is signed with the existing ALi updater key.
