#!/usr/bin/env python3
"""Generic URL -> file downloader.

Usage:
  python dl.py <URL>
  python dl.py <URL> -o output.pdf
  python dl.py <URL> -o output.pdf --ua "Mozilla/5.0 (Windows NT 10.0)"
  python dl.py -f urls.txt          # batch: one URL per line
  python dl.py -f urls.txt -d ./out # batch: write into ./out/
"""
import argparse
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


def derive_filename(url: str, response: requests.Response) -> str:
    cd = response.headers.get("content-disposition", "")
    if "filename=" in cd:
        name = cd.split("filename=", 1)[1].split(";")[0].strip().strip('"\'')
        if name:
            return unquote(name)
    name = os.path.basename(unquote(urlparse(url).path))
    if not name:
        name = "download.bin"
    if "." not in name:
        ctype = response.headers.get("content-type", "").split(";")[0].strip()
        ext = {
            "application/pdf": ".pdf",
            "application/zip": ".zip",
            "application/epub+zip": ".epub",
            "text/html": ".html",
        }.get(ctype, "")
        name += ext
    return name


def download(url: str, out: str | None, ua: str, timeout: int, chunk: int = 64 * 1024) -> str:
    sess = requests.Session()
    sess.headers.update({"User-Agent": ua, "Accept": "*/*"})

    with sess.get(url, stream=True, timeout=timeout, allow_redirects=True) as r:
        r.raise_for_status()
        out = out or derive_filename(url, r)
        Path(out).parent.mkdir(parents=True, exist_ok=True)
        size = int(r.headers.get("content-length") or 0)
        with open(out, "wb") as f, tqdm(
            desc=os.path.basename(out),
            total=size,
            unit="B",
            unit_scale=True,
            unit_divisor=1024,
            disable=size == 0,
        ) as bar:
            for piece in r.iter_content(chunk_size=chunk):
                if piece:
                    f.write(piece)
                    bar.update(len(piece))
    return out


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Download a file from a URL.")
    p.add_argument("url", nargs="?", help="URL to download (omit if using -f)")
    p.add_argument("-o", "--output", help="Output file path")
    p.add_argument("-f", "--from-file", help="File with one URL per line (batch mode)")
    p.add_argument("-d", "--out-dir", default=".", help="Output directory for batch mode")
    p.add_argument("--ua", default=DEFAULT_UA, help="User-Agent string")
    p.add_argument("--timeout", type=int, default=600, help="Request timeout (s)")
    args = p.parse_args()
    if not args.url and not args.from_file:
        p.error("provide a URL or -f <file>")
    return args


def main() -> int:
    args = parse_args()
    rc = 0

    urls: list[tuple[str, str | None]] = []  # (url, output)
    if args.url:
        urls.append((args.url, args.output))
    if args.from_file:
        with open(args.from_file, "r", encoding="utf-8") as f:
            for line in f:
                u = line.strip()
                if not u or u.startswith("#"):
                    continue
                urls.append((u, None))

    for url, out in urls:
        try:
            if out is None and args.from_file:
                # Batch mode: derive filename, write into out-dir
                target = None  # let download() derive, then move
            else:
                target = out
            saved = download(url, target, ua=args.ua, timeout=args.timeout)
            if args.from_file and args.out_dir != ".":
                dst = Path(args.out_dir) / Path(saved).name
                dst.parent.mkdir(parents=True, exist_ok=True)
                Path(saved).rename(dst)
                saved = str(dst)
            size_mb = os.path.getsize(saved) / (1024 * 1024)
            print(f"OK   {saved}  ({size_mb:.1f} MB)")
        except requests.HTTPError as e:
            print(f"FAIL {url}  HTTP {e.response.status_code}", file=sys.stderr)
            rc = 1
        except requests.RequestException as e:
            print(f"FAIL {url}  {type(e).__name__}: {e}", file=sys.stderr)
            rc = 1
        except KeyboardInterrupt:
            print("\nInterrupted", file=sys.stderr)
            return 130

    return rc


if __name__ == "__main__":
    sys.exit(main())
