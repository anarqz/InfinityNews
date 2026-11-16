- **Launcher updates no longer freeze.** The download's progress reached the window thousands of times per update and the window fell behind; it now refreshes a few times per second.
- **Slow or unstable connections finish the update.** The download no longer gives up after 5 minutes: it stops only when no data arrives for 30 seconds, and a stalled or broken download resumes where it stopped (up to 3 attempts). The launcher's log records the download's size, speed and any resume.

This release fixes the updater itself, so it helps from the next update on: this one is still downloaded by the updater you have now. The hook is unchanged (0.3.0+fh2online.98). Windows installations can use the launcher updater or extract the Windows x64 ZIP into a separate launcher folder. On Linux/Steam Deck, the launcher updater applies this release; if it cannot, rerun the [Linux/Steam Deck installer](https://github.com/anarqz/InfinityHorizon/tree/v1.2.2#install-on-linux-and-steam-deck).

[Download and full notes](https://github.com/anarqz/InfinityHorizon/releases/tag/v1.2.2)
