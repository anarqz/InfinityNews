# Infinity News

News shown in the Infinity Horizon launcher (Play tab and News page). The launcher reads this
repository directly from `raw.githubusercontent.com`; nothing here runs code.

## Add a news item

1. Pick an id: lowercase letters, digits and dashes, for example `2026-11-02-new-cars`.
2. Create `news/<id>/en.md` and/or `news/<id>/pt-BR.md` (Markdown). Images go in
   `news/<id>/assets/` (PNG or JPEG, at most 2 MiB and 4096×4096) and are referenced as
   `![alt](assets/picture.png)`.
3. Add the item to `news.json`: `id`, `date` (`YYYY-MM-DD`), `title` and `summary` in `en` and/or
   `pt-BR`; optional `cover` (`assets/…`), `pinned` and `minLauncher`.
4. Run `python3 scripts/validate.py`, then commit to `main`. The launcher may take about five
   minutes to see a new commit.

Rules: no raw HTML; links must be `https://`; images only from the item's own `assets/` folder;
at most 50 items in `news.json`. Pinned items come first, then the newest.
