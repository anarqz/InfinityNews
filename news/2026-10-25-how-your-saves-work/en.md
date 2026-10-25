Your progress is the most important thing you bring to Infinity, so here's exactly how the launcher treats your saves.

## Your saves stay where the game puts them

Infinity keeps no copy of your saves anywhere else. They stay in Azimuth's own saves folder:

`<Azimuth>\data\titles\1A96545B\saves\player-1\`

## One set of profiles, offline and online

You have up to three profiles, signed in or not, and every one of them plays both offline and online. Each profile has its own identity, so its own save folder (`User_…`), side by side in `player-1`. Profiles never share a save.

- **A profile you create without signing in** (Noob only) registers its name the next time you sign in. If someone took that name in the meantime, the launcher asks you for a new one; the profile and its save stay exactly as they are.
- **Noob** profiles use one save folder offline and online: what you do offline continues online, and the other way round.
- **Hardcore** works differently: online always continues from your cloud career. Played offline, a Hardcore profile keeps that progress in a separate local folder that never uploads.

## Revisions: the game keeps the newest two

Each time the game saves, it writes a new *revision*. A revision only counts when it's complete: every file matches the list the game wrote with it. The game always loads the newest complete revision and keeps the two newest.

## Start from a save you already have

When you create a profile, you can start it from any existing save on your PC — they're listed most recently played first, with level and credits. Your original save is only read, never changed. The launcher copies it, checks every file, and only then makes it the new profile's newest revision. This only happens while the game is closed, and if anything goes wrong midway, the profile stays exactly as it was.

## Nothing is ever deleted

Whenever the launcher has to move something aside — an incomplete revision, an older save it replaces, a cloud version, a conflict — it first copies it to:

`saves\fi-launcher-archive\<User_…>\`

## Cloud saves

Only **Infinity Supporter** profiles in **Hardcore** mode keep a cloud save. Every other profile is local only.

For those profiles, around each play session:

- **Before the game starts,** the launcher resends anything that didn't upload last time, sets incomplete revisions aside and installs a newer cloud revision if there is one.
- **If something looks wrong,** like a conflict or a save still being written, the launch stops instead of guessing.
- **After you quit,** your newest complete revision is uploaded. If the upload fails, it stays pending and is retried at your next launch.

## Liveries are per PC

Your creations (liveries and their thumbnails) are shared by every profile on the same PC, and they aren't synced to the cloud.

## Good habits

- Close the game before touching the saves folder.
- Keep your own backup of `player-1` now and then — it never hurts.
