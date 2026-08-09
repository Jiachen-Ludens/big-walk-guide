#!/usr/bin/env python3
"""Deterministic audit for static game wiki sites.

Usage:
    cd <project-dir> && MIN=13 python3 <path>/audit_site.py

Checks:
- at least MIN .html files in the project root
- exactly one <h1> per page
- viewport meta present
- no TODO/lorem/待补充/placeholder markers
- every internal href target exists
"""

import os
import pathlib
import re
import sys


def main() -> int:
    minimum = int(os.environ.get("MIN", "13"))
    root = pathlib.Path(".")
    html_pages = sorted(root.glob("*.html"))

    if len(html_pages) < minimum:
        print(f"AUDIT_FAIL pages={len(html_pages)} min={minimum}")
        return 1

    for page in html_pages:
        text = page.read_text(encoding="utf-8", errors="replace")
        if text.count("<h1") != 1:
            print(f"AUDIT_FAIL {page}: expected exactly one <h1>")
            return 1
        if 'name="viewport"' not in text:
            print(f"AUDIT_FAIL {page}: missing viewport")
            return 1
        if re.search(r"TODO|lorem|待补充|placeholder", text, re.I):
            print(f"AUDIT_FAIL {page}: forbidden marker found")
            return 1
        for target in re.findall(r'href="([^"#][^"]*)"', text):
            if target.startswith("http"):
                continue
            if not (root / target).exists():
                print(f"AUDIT_FAIL {page}: broken internal link -> {target}")
                return 1

    print(f"AUDIT_OK {len(html_pages)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
