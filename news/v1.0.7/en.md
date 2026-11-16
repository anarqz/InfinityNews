- Fix updater path validation under Wine/Proton when parent drive or mount paths are reported as links.
- Recognize the exact updater helper directory without confusing similarly named installation folders.
- Improve diagnostics when applying an update fails.

Signed-package verification and link checks inside the installation remain enabled.

Windows installations can use the launcher updater or extract the Windows x64 ZIP into a separate launcher folder. If an older Proton build cannot apply this update, rerun the [Linux/Steam Deck installer](https://github.com/anarqz/InfinityHorizon/tree/v1.0.7#install-on-linux-and-steam-deck).

[Download and full notes](https://github.com/anarqz/InfinityHorizon/releases/tag/v1.0.7)
