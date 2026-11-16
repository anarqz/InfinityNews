- **A new official mod catalog.** It lists the Infinity mod runtime, Extra Options, Nitro System and the reviewed Remix Car Pack. Every download is checked against the size and hash the catalog lists.
- **No mod is mandatory.** Extra Options is no longer required to play, online or offline. A mod still brings what it depends on: Nitro System installs Extra Options.
- **The mod runtime installs itself.** It comes from the catalog when a mod that needs it is installed, and the launcher checks both of its signatures first. It no longer ships inside the launcher.
- **Mods made of your own files.** The Remix Car Pack uses the car pack you already have: choose its folder, a folder above it, or its ZIP. The launcher finds the files, checks every one and keeps its own verified copy, so the pack can move afterwards. On Steam Deck, a built-in file browser works with the controller and the Steam keyboard.
- **Every install shows a preview first.** You see where the mod goes and which existing files it replaces. Replaced files are backed up and restored when you disable or uninstall the mod. Updates show the same preview.
- **Other catalogs.** Configure → Mod catalog accepts another catalog address. An unofficial catalog is always marked as such, and never replaces the installed mod runtime.
- **GitHub limits.** When GitHub's API limit is reached, launcher updates are read from the release page instead. Updates are trusted exactly as before: the signed descriptor is verified, and the package must match its hash.
- **Offline screens.** No "Checking the latest official release…" banner appears before you sign in.
- **Fixes:**
  - the mod progress screen draws cleanly on Linux and Steam Deck;
  - singular texts ("1 file");
  - a clipped button in Portuguese;
  - error messages name the right address.
- The launcher log now records how the launcher closed.

Windows installations can use the launcher updater or extract the Windows x64 ZIP into a separate launcher folder. On Linux/Steam Deck, the launcher updater applies this release; if it cannot, rerun the [Linux/Steam Deck installer](https://github.com/anarqz/InfinityHorizon/tree/v1.0.11#install-on-linux-and-steam-deck).

[Download and full notes](https://github.com/anarqz/InfinityHorizon/releases/tag/v1.0.11)
