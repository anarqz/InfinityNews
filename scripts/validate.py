#!/usr/bin/env python3
"""Quick typo check for the Infinity news feed before a commit.

Usage: python3 scripts/validate.py [repo root]. Exit 0 when fine, 1 with one line per problem.
Checks that news.json is valid JSON, every listed item has its folder and at least one Markdown
file, and images referenced by cover or Markdown exist. Standard library only.
"""

import json
import re
import sys
from pathlib import Path

MD_IMAGE = re.compile(r"!\[[^\]]*\]\(\s*<?([^)\s>]+)>?")

problems = []


def main(root):
    index = root / "news.json"
    try:
        doc = json.loads(index.read_text(encoding="utf-8-sig"))
    except FileNotFoundError:
        problems.append("news.json: missing")
        return
    except ValueError as error:
        problems.append(f"news.json: not valid JSON: {error}")
        return
    items = doc.get("items") if isinstance(doc, dict) else None
    if not isinstance(items, list):
        problems.append("news.json: needs an items list")
        return
    for n, item in enumerate(items):
        item_id = item.get("id") if isinstance(item, dict) else None
        if not isinstance(item_id, str) or not item_id:
            problems.append(f"items[{n}]: missing id")
            continue
        folder = root / "news" / item_id
        if not folder.is_dir():
            problems.append(f"{item_id}: folder news/{item_id}/ does not exist")
            continue
        markdown = [p for p in (folder / "en.md", folder / "pt-BR.md") if p.is_file()]
        if not markdown:
            problems.append(f"{item_id}: needs en.md and/or pt-BR.md")
        images = [item["cover"]] if isinstance(item.get("cover"), str) else []
        for md in markdown:
            images += [t for t in MD_IMAGE.findall(md.read_text(encoding="utf-8-sig")) if "://" not in t]
        for image in images:
            if not (folder / image).is_file():
                problems.append(f"{item_id}: image {image} does not exist")


if __name__ == "__main__":
    main(Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve())
    for line in problems:
        print(line)
    print("news feed OK" if not problems else f"{len(problems)} problem(s)")
    sys.exit(1 if problems else 0)
