# ALi Imagine v0.8.1

Version 0.8.1 repairs clean-machine LTX 2.5 installation and makes native 2× jobs observable from click through completion.

- Fixes invalid parent-relative README declarations in all staged LTX MLX workspace packages.
- Installs the pinned LTX workspace packages into ALi's managed environment.
- Enforces and verifies `mlx-lm==0.31.2`.
- Automatically repairs older affected managed-source installations.
- Starts LTX 2.5 native 2× preflight immediately and keeps the job visible in Render Queue.
- Surfaces queue and terminal job failures instead of silently resetting the panel.

The clean runtime installer was verified from an empty isolated directory before release.

