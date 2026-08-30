# ALi Imagine 0.9.1

## Re-Frame 3D experimental preview

- Open 3D directly from a selected image; visiting FX first is no longer required.
- Pause a video and press 3D to use the exact paused frame, with nearby frames available for a smarter multiview scene.
- Build and inspect a real local Gaussian splat scene from the pinned DA3 Small model on Apple Silicon.
- Use Cinema 4D-style subject-pivot orbit, tilt, truck, pedestal, dolly, and focal controls inside a bounded reconstruction envelope.
- Let Qwen Vision analyze the untouched original before reconstruction.
- Reconstruct locally with FLUX.2 Klein Edit using the spatial camera plate and untouched original as two ordered references, or choose Krea 2 as an alternate path.
- Keep Gaussian scenes, plates, masks, and other Re-Frame working artifacts out of the normal Library.

## Reliability

- Embed the Re-Frame worker in the application binary so installed builds do not depend on a source checkout.
- Certify both ordinary FLUX.2 generation and a real two-reference Klein Edit before enabling reconstruction.
- Reduce peak LTX 2.5 VAE decode memory for long or high-resolution renders and return a more actionable decode-crash message.

## Preview boundary

Re-Frame 3D is experimental. A single photograph cannot reveal unseen ground truth; wider moves use generative reconstruction and can change occluded details. The coverage meter and bounded camera envelope communicate that uncertainty.

## Trust

This Apple-silicon build is Developer ID signed, Apple notarized, stapled, and Gatekeeper accepted. The in-app updater archive is signed with the existing ALi updater key.
