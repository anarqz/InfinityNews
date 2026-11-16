#!/usr/bin/env python3
"""Rebuild news.json and news/<tag>/ from the published launcher releases of anarqz/InfinityHorizon.

Every news item is a launcher release (owner, 2026-11-16). Drafts, pre-releases and tags that are
not `v<version>` (mod runtime, mod catalog) are skipped. Release notes with `## English` and
`## Português` sections give the two languages; a body without them is used for both.

    python3 scripts/from_releases.py            # reads the GitHub API (GH_TOKEN optional)
    python3 scripts/from_releases.py --check    # exit 1 when the files would change
"""
import json
import os
import re
import shutil
import sys
import urllib.request
from pathlib import Path

REPO = "anarqz/InfinityHorizon"
ROOT = Path(__file__).resolve().parents[1]
TAG = re.compile(r"^v\d+(\.\d+){1,3}$")
DATE = re.compile(r"^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2})")
HEADING = re.compile(r"^##[ \t]+(English|Portugu[eê]s\b[^\n]*)[ \t]*$", re.I | re.M)


def releases():
    out, page = [], 1
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "infinity-news-sync"}
    if os.environ.get("GH_TOKEN"):
        headers["Authorization"] = "Bearer " + os.environ["GH_TOKEN"]
    while True:
        req = urllib.request.Request(f"https://api.github.com/repos/{REPO}/releases?per_page=100&page={page}", headers=headers)
        with urllib.request.urlopen(req, timeout=30) as r:
            batch = json.load(r)
        out += batch
        if len(batch) < 100:
            return out
        page += 1


def split_languages(md):
    text = md.replace("\r\n", "\n")
    marks = [("en" if m.group(1).lower() == "english" else "pt-BR", m.start(), m.end()) for m in HEADING.finditer(text)]
    if not marks:
        return {"en": text.strip(), "pt-BR": text.strip()}
    parts = {}
    for i, (lang, _, end) in enumerate(marks):
        nxt = marks[i + 1][1] if i + 1 < len(marks) else len(text)
        part = text[end:nxt].strip()
        if part and lang not in parts:
            parts[lang] = part
    en = parts.get("en") or parts.get("pt-BR", "")
    return {"en": en, "pt-BR": parts.get("pt-BR") or en}


def first_point(md):
    line = next((l.strip() for l in md.split("\n") if l.strip() and not l.strip().startswith("#")), None)
    if not line:
        return None
    plain = re.sub(r"^[-*+]\s+|^\d+\.\s+", "", line)
    plain = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", plain)
    plain = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", plain)
    plain = re.sub(r"[*_`]", "", plain).strip()
    if not plain:
        return None
    return plain if len(plain) <= 200 else plain[:199].rstrip() + "…"


def build(raw):
    items, files = [], {}
    for r in raw:
        tag = r.get("tag_name")
        if r.get("draft") or r.get("prerelease") or not isinstance(tag, str) or not TAG.match(tag):
            continue
        m = DATE.match(r.get("published_at") or "")
        if not m:
            continue
        title = (r.get("name") or "").strip() or f"Infinity Horizon {tag[1:]}"
        notes = split_languages(r.get("body") or "")
        url = r.get("html_url") or ""
        item = {"id": tag, "date": m.group(1), "title": {"en": title, "pt-BR": title}}
        en, pt = first_point(notes["en"]), first_point(notes["pt-BR"])
        if en or pt:
            item["summary"] = {"en": en or pt, "pt-BR": pt or en}
        items.append(item)
        link = {"en": "Download and full notes", "pt-BR": "Download e notas completas"}
        for lang in ("en", "pt-BR"):
            body = notes[lang] or ""
            if url.startswith("https://github.com/"):
                body += f"\n\n[{link[lang]}]({url})"
            files[f"news/{tag}/{lang}.md"] = body.strip() + "\n"
    items.sort(key=lambda i: (i["date"], i["id"]), reverse=True)
    files["news.json"] = json.dumps({"schemaVersion": 1, "items": items}, ensure_ascii=False, indent=2) + "\n"
    return files


def current():
    out = {}
    for p in [ROOT / "news.json", *sorted((ROOT / "news").rglob("*"))]:
        if p.is_file():
            out[p.relative_to(ROOT).as_posix()] = p.read_text(encoding="utf-8", errors="replace")
    return out


def main():
    files = build(releases())
    if current() == files:
        print("news: up to date")
        return 0
    if "--check" in sys.argv:
        print("news: out of date")
        return 1
    shutil.rmtree(ROOT / "news", ignore_errors=True)
    for name, text in files.items():
        path = ROOT / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    print(f"news: wrote {len(files) - 1} files for {(len(files) - 1) // 2} releases")
    return 0


if __name__ == "__main__":
    sys.exit(main())
