# ALi Imagine 0.9.4

## Spatial Take quality

- Neutral Re-Frame camera commits now reproduce source pixels exactly and fail certification if dimensions or pixels change.
- Moved cameras keep a raw reprojection and create a confidence-aware Camera Guide that softens damaged or uncertain regions without blurring reliable evidence.
- The new Repair overlay shows which regions FLUX.2 is expected to reconstruct.

## Camera and identity together

- FLUX.2 Klein Edit now receives the cleaned Camera Guide and untouched original as ordered references.
- The guide controls camera, crop, scale, placement, and silhouette; the original protects identity, wardrobe, materials, color, lighting, typography, and style.
- The committed orbit is repeated in a concise camera contract so reconstruction does not fall back to the original viewpoint.
- Qwen Vision produces a compact identity-and-material card instead of competing with the spatial composition.

## Clean review workflow

- Reconstruction starts automatically after Qwen analysis.
- Original, Camera Guide, Repair mask, and reconstructed result remain directly reviewable in Spatial Take.
- Working plates and reconstruction previews stay outside the normal Library.
- **Keep Result in Library** explicitly promotes the chosen result without changing its file or provenance.

## Verified release gate

- Pixel-exact neutral and confidence-guide worker tests pass.
- Positive and negative three-quarter orbit sentinels both preserve one coherent subject, the chosen camera direction, materials, palette, crown, armor, and readable `FULLY IN` typography.
- Frontend, Rust, Python, production-build, formatting, Clippy, signing, notarization, updater, and public-download checks are required before publication.

Wide single-image moves remain generative reconstruction territory. Originals remain immutable, and local models remain separate explicit downloads.
