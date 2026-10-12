#!/usr/bin/env python3
"""Check that every generated HTML page uses English, including navigation pages."""

from pathlib import Path
import re
import sys


def main() -> int:
    site = Path(sys.argv[1] if len(sys.argv) > 1 else "_site")
    pages = sorted(site.rglob("*.html"))
    required = (
        "index.html",
        "about/index.html",
        "projects/index.html",
        "categories/index.html",
        "tags/index.html",
        "archives/index.html",
    )

    errors = []
    for name in required:
        if not (site / name).is_file():
            errors.append(f"Missing navigation page: {name}")

    for page in pages:
        relative = page.relative_to(site)
        html = page.read_text(encoding="utf-8")
        if not re.search(r'<html\b[^>]*\blang\s*=\s*["\']en["\']', html, re.I | re.S):
            errors.append(f"{relative}: HTML language is not en")
        if re.search(r"[\uac00-\ud7a3]", html):
            errors.append(f"{relative}: Korean text found in rendered HTML")
        if "/app.min.js?baseurl=" in html:
            errors.append(f"{relative}: old PWA registration script still included")

    if not pages:
        errors.append("No generated HTML pages to check")

    if errors:
        print("\n".join(errors))
        return 1
    print(f"Checked {len(pages)} HTML pages: English locale and no stale PWA registration.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
