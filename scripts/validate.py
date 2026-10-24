#!/usr/bin/env python3
"""Validates the Infinity news feed against its contract (news.json + news/<id>/...).

Usage: python3 scripts/validate.py [repo root]. Exit 0 when valid, 1 with one line per problem.
Standard library only.
"""

import json
import re
import struct
import sys
from pathlib import Path

MAX_INDEX = 256 * 1024
MAX_MARKDOWN = 256 * 1024
MAX_IMAGE = 2 * 1024 * 1024
MAX_PIXELS = 4096
MAX_ITEMS = 50
LANGS = ("en", "pt-BR")
ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")
DATE_RE = re.compile(r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$")
SEMVER_RE = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(-[0-9A-Za-z-]+(\.[0-9A-Za-z-]+)*)?$"
)
ASSET_RE = re.compile(r"^assets/[A-Za-z0-9._-]+\.(png|jpg|jpeg)$")
ITEM_KEYS = {"id", "date", "title", "summary", "cover", "pinned", "minLauncher"}
MD_IMAGE = re.compile(r"!\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
MD_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
RAW_HTML = re.compile(r"<\s*/?\s*[A-Za-z][A-Za-z0-9-]*(\s[^>]*)?>")

problems = []


def fail(where, message):
    problems.append(f"{where}: {message}")


def image_size(data):
    if data[:8] == b"\x89PNG\r\n\x1a\n" and data[12:16] == b"IHDR":
        return "png", struct.unpack(">II", data[16:24])
    if data[:2] == b"\xff\xd8":
        i = 2
        while i + 9 < len(data):
            if data[i] != 0xFF:
                return "jpeg", None
            marker = data[i + 1]
            length = struct.unpack(">H", data[i + 2 : i + 4])[0]
            if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                h, w = struct.unpack(">HH", data[i + 5 : i + 9])
                return "jpeg", (w, h)
            i += 2 + length
        return "jpeg", None
    return None, None


def check_asset(item_dir, rel, where):
    if not ASSET_RE.match(rel):
        fail(where, f"image path {rel!r} must be assets/<name>.png|.jpg|.jpeg")
        return
    path = item_dir / rel
    if not path.is_file():
        fail(where, f"image {rel} does not exist")
        return
    data = path.read_bytes()
    if len(data) > MAX_IMAGE:
        fail(where, f"image {rel} is {len(data)} bytes (max {MAX_IMAGE})")
    kind, size = image_size(data)
    expected = "png" if rel.endswith(".png") else "jpeg"
    if kind != expected:
        fail(where, f"image {rel} is not a {expected.upper()} file")
    elif size is None:
        fail(where, f"image {rel}: could not read its dimensions")
    elif size[0] > MAX_PIXELS or size[1] > MAX_PIXELS:
        fail(where, f"image {rel} is {size[0]}x{size[1]} (max {MAX_PIXELS}x{MAX_PIXELS})")


def check_text(value, where, limit):
    if not isinstance(value, dict) or not value:
        fail(where, "must be an object with en and/or pt-BR")
        return
    for lang, text in value.items():
        if lang not in LANGS:
            fail(where, f"unknown language {lang!r}")
        elif not isinstance(text, str) or not text.strip():
            fail(f"{where}.{lang}", "must be a non-empty string")
        elif len(text) > limit:
            fail(f"{where}.{lang}", f"{len(text)} characters (max {limit})")


def check_markdown(item_dir, lang, where):
    path = item_dir / f"{lang}.md"
    if not path.is_file():
        return False
    raw = path.read_bytes()
    if len(raw) > MAX_MARKDOWN:
        fail(where, f"{lang}.md is {len(raw)} bytes (max {MAX_MARKDOWN})")
    if raw.startswith(b"\xef\xbb\xbf"):
        fail(where, f"{lang}.md starts with a BOM")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        fail(where, f"{lang}.md is not UTF-8")
        return True
    outside_code = re.sub(r"```.*?```|`[^`]*`", "", text, flags=re.S)
    if RAW_HTML.search(outside_code):
        fail(where, f"{lang}.md contains raw HTML, which the launcher does not render")
    for target in MD_IMAGE.findall(outside_code):
        check_asset(item_dir, target, f"{where} {lang}.md")
    for target in MD_LINK.findall(outside_code):
        if not target.startswith("https://"):
            fail(where, f"{lang}.md link {target!r} must be an https:// address")
    return True


def main(root):
    index = root / "news.json"
    if not index.is_file():
        fail("news.json", "missing")
        return
    raw = index.read_bytes()
    if len(raw) > MAX_INDEX:
        fail("news.json", f"{len(raw)} bytes (max {MAX_INDEX})")
    if raw.startswith(b"\xef\xbb\xbf"):
        fail("news.json", "starts with a BOM")
    try:
        doc = json.loads(raw.decode("utf-8"), object_pairs_hook=no_duplicates)
    except (UnicodeDecodeError, ValueError) as error:
        fail("news.json", f"not valid UTF-8 JSON: {error}")
        return
    if not isinstance(doc, dict) or set(doc) != {"schemaVersion", "items"}:
        fail("news.json", "must contain exactly schemaVersion and items")
        return
    if doc["schemaVersion"] != 1:
        fail("news.json", "schemaVersion must be 1")
    items = doc["items"]
    if not isinstance(items, list):
        fail("news.json", "items must be a list")
        return
    if len(items) > MAX_ITEMS:
        fail("news.json", f"{len(items)} items (max {MAX_ITEMS})")
    seen = set()
    for n, item in enumerate(items):
        where = f"items[{n}]"
        if not isinstance(item, dict):
            fail(where, "must be an object")
            continue
        extra = set(item) - ITEM_KEYS
        if extra:
            fail(where, f"unknown fields {sorted(extra)}")
        for key in ("id", "date", "title", "summary"):
            if key not in item:
                fail(where, f"missing {key}")
        item_id = item.get("id")
        if not isinstance(item_id, str) or not ID_RE.match(item_id):
            fail(where, "id must match ^[a-z0-9][a-z0-9-]{0,63}$")
            continue
        where = f"items[{n}] ({item_id})"
        if item_id in seen:
            fail(where, "duplicate id")
        seen.add(item_id)
        if not isinstance(item.get("date"), str) or not DATE_RE.match(item["date"]):
            fail(where, "date must be YYYY-MM-DD")
        check_text(item.get("title"), f"{where}.title", 120)
        check_text(item.get("summary"), f"{where}.summary", 280)
        if "pinned" in item and not isinstance(item["pinned"], bool):
            fail(where, "pinned must be true or false")
        if "minLauncher" in item and (
            not isinstance(item["minLauncher"], str) or not SEMVER_RE.match(item["minLauncher"])
        ):
            fail(where, "minLauncher must be a SemVer version such as 1.0.12")
        item_dir = root / "news" / item_id
        if not item_dir.is_dir():
            fail(where, f"folder news/{item_id}/ does not exist")
            continue
        if "cover" in item:
            if isinstance(item["cover"], str):
                check_asset(item_dir, item["cover"], f"{where}.cover")
            else:
                fail(where, "cover must be a string")
        found = [lang for lang in LANGS if check_markdown(item_dir, lang, where)]
        if not found:
            fail(where, "needs en.md and/or pt-BR.md")
    folders = {p.name for p in (root / "news").iterdir() if p.is_dir()} if (root / "news").is_dir() else set()
    for orphan in sorted(folders - seen):
        fail(f"news/{orphan}/", "folder is not listed in news.json")


def no_duplicates(pairs):
    keys = [k for k, _ in pairs]
    if len(keys) != len(set(keys)):
        raise ValueError(f"duplicate keys {sorted({k for k in keys if keys.count(k) > 1})}")
    return dict(pairs)


if __name__ == "__main__":
    main(Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve())
    for line in problems:
        print(line)
    print("news feed OK" if not problems else f"{len(problems)} problem(s)")
    sys.exit(1 if problems else 0)
