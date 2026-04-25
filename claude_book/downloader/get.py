#!/usr/bin/env python3
"""Interactive downloader. Run, paste URL, get the file."""
import os
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

import requests
from tqdm import tqdm


DEFAULT_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)

HERE = Path(__file__).resolve().parent
CLAUDE_ROOT = HERE.parent
DOWNLOADS_DIR = HERE / "downloads"
DOWNLOADS_DIR.mkdir(exist_ok=True)


def list_categories():
    return sorted(
        d for d in CLAUDE_ROOT.iterdir()
        if d.is_dir() and len(d.name) >= 2 and d.name[:2].isdigit()
    )


def derive_filename(url: str, response: requests.Response) -> str:
    cd = response.headers.get("content-disposition", "")
    if "filename=" in cd:
        name = cd.split("filename=", 1)[1].split(";")[0].strip().strip('"\'')
        if name:
            return unquote(name)
    name = os.path.basename(unquote(urlparse(url).path)) or "download.bin"
    if "." not in name:
        ctype = response.headers.get("content-type", "").split(";")[0].strip()
        name += {
            "application/pdf": ".pdf",
            "application/zip": ".zip",
            "application/epub+zip": ".epub",
        }.get(ctype, "")
    return name


def download_one(url: str, out_dir: Path) -> Path:
    sess = requests.Session()
    sess.headers.update({"User-Agent": DEFAULT_UA, "Accept": "*/*"})
    with sess.get(url, stream=True, timeout=900, allow_redirects=True) as r:
        r.raise_for_status()
        name = derive_filename(url, r)
        out = out_dir / name
        # avoid overwrite
        if out.exists():
            stem, suffix = out.stem, out.suffix
            i = 2
            while (out_dir / f"{stem}-{i}{suffix}").exists():
                i += 1
            out = out_dir / f"{stem}-{i}{suffix}"
        size = int(r.headers.get("content-length") or 0)
        with open(out, "wb") as f, tqdm(
            desc=out.name, total=size, unit="B", unit_scale=True,
            unit_divisor=1024, disable=size == 0,
        ) as bar:
            for chunk in r.iter_content(chunk_size=64 * 1024):
                if chunk:
                    f.write(chunk)
                    bar.update(len(chunk))
    return out


def pick_destination() -> Path:
    """Ask user where to save. Empty/0 = default downloads/. Number = category folder."""
    cats = list_categories()
    print()
    print("Save where?")
    print(f"  [Enter]  default: downloads/  (you can move it later)")
    for i, c in enumerate(cats, 1):
        print(f"  {i:>2}.      {c.name}")
    print()
    choice = input("> ").strip()
    if not choice or choice == "0":
        return DOWNLOADS_DIR
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(cats):
            return cats[idx]
    except ValueError:
        pass
    print(f"  (didn't recognize '{choice}', using downloads/)")
    return DOWNLOADS_DIR


def main() -> int:
    print("=" * 60)
    print("  Interactive Downloader")
    print("  Paste a URL and press Enter. Empty URL or Ctrl+C to quit.")
    print("=" * 60)
    while True:
        print()
        try:
            url = input("URL > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye.")
            return 0
        if not url:
            print("Bye.")
            return 0
        if not url.startswith(("http://", "https://")):
            print("  Not an http(s) URL — try again.")
            continue
        out_dir = pick_destination()
        try:
            saved = download_one(url, out_dir)
            size_mb = os.path.getsize(saved) / (1024 * 1024)
            print(f"\n  OK   {saved.relative_to(CLAUDE_ROOT)}  ({size_mb:.1f} MB)")
        except requests.HTTPError as e:
            print(f"\n  FAIL  HTTP {e.response.status_code}")
        except requests.RequestException as e:
            print(f"\n  FAIL  {type(e).__name__}: {e}")
        except KeyboardInterrupt:
            print("\n  Cancelled.")
            return 130


if __name__ == "__main__":
    sys.exit(main())
