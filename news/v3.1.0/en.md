- **ExtraOptions 0.6.0.** Infinity now ships ExtraOptions 0.6.0. Mods live in one folder per game: `mods\Forza Horizon 2\` and `mods\Forza Motorsport 5\`, each with its own load order. Before the first launch, the launcher moves your existing mods and their load order into the right game's folder. If a move cannot be done, it tells you why and keeps the game from starting until it can. Nothing is deleted, and ExtraOptions' own `mods\Cache` is never touched.
- **Settings.** New ExtraOptions options: Playground events on the map, and the mod database cache. Retired options are gone. Options that keep saves safe (missing save commits, offline VIP) stay locked off. The launcher checks every ExtraOptions settings file it writes, because an invalid one turns ExtraOptions off.
- **Mods by mode.** NOOB profiles can use any mod. HARDCORE profiles keep only cosmetic mods, in both games. Forza Motorsport 5's mods folder holds only mods installed by the launcher.
- **New mods.** Garage Revving (both modes) and Weather Control (NOOB only) are coming to the catalog.
- **Saves.** On the Resolve screen, **Keep this PC** now works. It no longer leaves the game showing "Resolve saves": the card shows "Uploads at the next Play", and this PC's save goes up when you press Play, without asking again.

The hook is updated (0.3.0+fh2online.125). Windows installations can use the launcher updater or extract the Windows x64 ZIP into a separate launcher folder. On Linux/Steam Deck, the launcher updater applies this release; if it cannot, rerun the [Linux/Steam Deck installer](https://github.com/anarqz/InfinityHorizon/tree/v2.0.4#install-on-linux-and-steam-deck).

[Download and full notes](https://github.com/anarqz/InfinityHorizon/releases/tag/v3.1.0)
