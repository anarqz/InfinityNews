# Infinity News

News shown in the Infinity Horizon launcher (Play tab and News page) and on
https://infinity-horizon.com/news. The launcher reads this repository directly from
`raw.githubusercontent.com`; nothing here runs code.

## Every news item is a launcher release

`news.json` and `news/<tag>/{en,pt-BR}.md` are generated from the published `v*` releases of
[anarqz/InfinityHorizon](https://github.com/anarqz/InfinityHorizon/releases) by
`scripts/from_releases.py`: the release name is the title, the first point of the notes is the
summary, and the `## English` / `## Português` sections are the two languages. Drafts,
pre-releases and other tags are skipped. Do not edit the generated files by hand: write the
release notes instead.

The `sync-releases` workflow runs it every hour (and on demand), commits when something changed and
asks the site to rebuild. To run it locally:

```sh
python3 -I scripts/from_releases.py && python3 -I scripts/validate.py
```
