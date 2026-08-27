# ALi Imagine v0.8.4

Version 0.8.4 repairs Prompt Assist startup on lower-memory Macs and cleans up the tester-reported Stage workflow issues.

- Prompt Assist automatically installs the public Qwen 3.5 4B 4-bit vision model on 16–32 GB Macs; 48 GB+ Macs retain Qwen 3.8 27B 4-bit.
- Setup shows the detected memory profile, exact download progress, Cancel/Resume, and requires a successful local startup before reporting Ready. No Hugging Face token is required.
- A paused Stage video can capture its current frame and load it as the Image Video start frame for continuation.
- Background status now visibly reaches green Complete, and the animated blue Stage perimeter sweep is removed.
- The working 20-second option, Render Queue cancellation, and Image Video end-frame slot are unchanged.
