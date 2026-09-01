# ALi Imagine 0.9.5

## Take Stacks

- Repeated generations from the same source and operation now appear as one Take Stack in Gallery and Recent Outputs.
- Open a stack to browse every take without losing the relationship to its source shot.
- Star one take as the best take. The choice is project-bounded, atomic, and persistent.
- Nothing is overwritten or deleted: every generated file and its lineage remain immutable.

## Spatial HQ hardening

- InfiniSplat keeps its own isolated runtime, exact model identity, explicit installation, and real-output certification boundary.
- Spatial HQ now checks complete model inventories and supports resumable managed downloads before certification.
- The released InfiniSplat checkpoint remains a single-image reconstruction path. ALi does not describe it as multi-view fusion.
- Quick and Detail remain available when Spatial HQ is missing, uncertified, or too slow for the current shot.

## Future H3 path, safely disabled

- The native Ref2VA, Turbo, chained-window, and preview request surfaces are prepared for a future licence review.
- Local MiniMax H3 execution remains fail-closed because the current community licence excludes the European Union. There is no environment-variable or UI bypass.

## Verified release gate

- 20 frontend files and 111 tests passed.
- 269 Rust tests passed; 66 hardware- or model-gated tests were ignored by design.
- TypeScript/Vite production build, Rust formatting, and Clippy warnings-as-errors passed.
- The Apple-silicon app and updater are signed with Developer ID, and the DMG is notarized and stapled by Apple.

Large models remain separate, explicit downloads. Projects, sources, generations, local models, and provenance survive application updates.
