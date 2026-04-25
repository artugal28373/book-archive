# Downloader

Generic URL → file downloader. Streams large files, shows progress, follows redirects, sets a real browser User-Agent.

## One-time setup

Open PowerShell or CMD in this folder, then:

```cmd
cd C:\Users\USER\Desktop\claude\downloader
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

After this, `(venv)` will appear in your prompt — that means the venv is active.

## Daily use

Activate the venv first (only needed once per terminal session):

```cmd
cd C:\Users\USER\Desktop\claude\downloader
venv\Scripts\activate
```

### Single download

```cmd
python dl.py "https://example.com/file.pdf"
```

Saves into the current directory, derived filename from URL or Content-Disposition.

### Custom output path

```cmd
python dl.py "https://example.com/file.pdf" -o "C:\Users\USER\Desktop\claude\01-math\linear-algebra\Strang-Calculus.pdf"
```

### Batch download

Make a text file with one URL per line (lines starting with `#` are ignored):

```
# urls.txt
https://example.com/book1.pdf
https://example.com/book2.pdf
```

Then:

```cmd
python dl.py -f urls.txt -d "C:\Users\USER\Desktop\claude\23-data-engineering"
```

All files land in the output directory you specify.

### Custom User-Agent

```cmd
python dl.py "URL" --ua "Mozilla/5.0 (something else)"
```

### Custom timeout

```cmd
python dl.py "URL" --timeout 1200
```

## Troubleshooting

**`pip` not recognized**: Python isn't installed or isn't on PATH. Reinstall Python and check "Add Python to PATH".

**SSL / certificate errors**: Some sites have broken cert chains. The script doesn't disable cert verification by default (safer). If you absolutely must, edit `dl.py` and add `verify=False` to the `sess.get(...)` call — but understand you're then trusting whatever certificate the server presents.

**HTTP 403 / 401**: The site is blocking automated downloads. Try a different User-Agent. Some sites require login cookies — those need a browser, not this tool.

**Slow downloads / timeouts**: Bump `--timeout 1200` (20 min) for large files.

**Wrong filename / no extension**: Pass `-o output.pdf` explicitly.

## What this tool does and doesn't do

It's a thin wrapper around the `requests` library. It will download whatever HTTP/HTTPS URL you point it at, exactly like `curl -L -o file URL`. It does **not**:

- Bypass paywalls or DRM
- Solve CAPTCHAs
- Handle JavaScript-rendered pages
- Authenticate to sites that need login
- Resume interrupted downloads (each run starts from byte 0)

You are responsible for ensuring you have the right to download whatever you point it at.
