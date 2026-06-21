#!/usr/bin/env python3
"""
fetch.py — Fetch documentation from a source and save to human/ and versions/

Usage:
    python scripts/fetch.py sources/hermes.yaml
    python scripts/fetch.py --all

For each source config:
  - Loads the YAML to get page list
  - Fetches each page via curl
  - Extracts text content from HTML
  - Saves to human/<source>/<page>.md
  - Copies to versions/<source>/ with timestamp
"""

import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HUMAN_DIR = ROOT / "human"
VERSIONS_DIR = ROOT / "versions"
STATUS_DIR = ROOT / "status"
SOURCES_DIR = ROOT / "sources"


def load_config(source_name):
    """Load a source YAML config."""
    import yaml
    path = SOURCES_DIR / source_name
    if not path.exists():
        # Try with .yaml extension
        path = SOURCES_DIR / f"{source_name}.yaml"
    if not path.exists():
        print(f"ERROR: Config not found: {source_name}", file=sys.stderr)
        sys.exit(1)
    with open(path) as f:
        return yaml.safe_load(f)


def fetch_page(url):
    """Fetch a URL and convert HTML to readable markdown text."""
    try:
        result = subprocess.run(
            ["curl", "-sL", "-m", "30", url],
            capture_output=True, text=True, timeout=35
        )
        if result.returncode != 0:
            return None, f"curl failed with code {result.returncode}"

        html = result.stdout
        if not html or len(html) < 200:
            return None, "Response too short or empty"

        # Basic HTML-to-text extraction
        text = html_to_markdown(html)
        return text, None
    except subprocess.TimeoutExpired:
        return None, "Timeout"
    except Exception as e:
        return None, str(e)


def html_to_markdown(html):
    """Simple HTML to markdown conversion. Handles typical doc site structure."""
    import html as html_module

    # Remove script and style tags
    html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
    html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.DOTALL)
    html = re.sub(r'<noscript[^>]*>.*?</noscript>', '', html, flags=re.DOTALL)

    # Decode HTML entities
    html = html_module.unescape(html)

    # Try to find main content area (common doc site patterns)
    main_content = None
    for pattern in [
        r'<main[^>]*>(.*?)</main>',
        r'<article[^>]*>(.*?)</article>',
        r'class="[^"]*(?:content|markdown|documentation|doc-body)[^"]*"[^>]*>(.*?)(?=</(?:div|section|main))',
        r'<div[^>]*class="[^"]*(?:prose|md-content|entry-content)[^"]*"[^>]*>(.*?)</div>',
        r'<body[^>]*>(.*?)</body>',
    ]:
        m = re.search(pattern, html, re.DOTALL)
        if m:
            main_content = m.group(1)
            break

    if not main_content:
        main_content = html

    # Remove remaining HTML tags, preserve line structure
    text = main_content

    # Headers
    text = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1\n\n', text, flags=re.DOTALL)
    text = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1\n\n', text, flags=re.DOTALL)
    text = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1\n\n', text, flags=re.DOTALL)
    text = re.sub(r'<h4[^>]*>(.*?)</h4>', r'#### \1\n\n', text, flags=re.DOTALL)

    # Code blocks
    text = re.sub(r'<pre><code[^>]*>(.*?)</code></pre>', r'```\n\1\n```\n\n', text, flags=re.DOTALL)
    text = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', text, flags=re.DOTALL)
    text = re.sub(r'<pre[^>]*>(.*?)</pre>', r'```\n\1\n```\n\n', text, flags=re.DOTALL)

    # Links
    text = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', text, flags=re.DOTALL)

    # Images
    text = re.sub(r'<img[^>]*src="([^"]*)"[^>]*alt="([^"]*)"[^>]*>', r'![\2](\1)', text)
    text = re.sub(r'<img[^>]*src="([^"]*)"[^>]*>', r'![](\1)', text)

    # Lists
    text = re.sub(r'<li[^>]*>(.*?)</li>', r'* \1\n', text, flags=re.DOTALL)
    text = re.sub(r'</?ul[^>]*>', '\n', text)
    text = re.sub(r'</?ol[^>]*>', '\n', text)

    # Paragraphs and breaks
    text = re.sub(r'</p>', '\n\n', text)
    text = re.sub(r'<br\s*/?>', '\n', text)

    # Bold / italic
    text = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', text, flags=re.DOTALL)
    text = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', text, flags=re.DOTALL)
    text = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', text, flags=re.DOTALL)
    text = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', text, flags=re.DOTALL)

    # Tables
    text = re.sub(r'<table[^>]*>(.*?)</table>', r'\n[TABLE]\n\1\n[/TABLE]\n', text, flags=re.DOTALL)
    text = re.sub(r'<tr[^>]*>(.*?)</tr>', r'| \1 |\n', text, flags=re.DOTALL)
    text = re.sub(r'<t[hd][^>]*>(.*?)</t[hd]>', r' \1 ', text, flags=re.DOTALL)

    # Strip remaining HTML tags
    text = re.sub(r'<[^>]+>', '', text)

    # Clean up excessive whitespace
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    text = re.sub(r' +\n', '\n', text)

    # Remove nav/footer artifacts
    lines = text.split('\n')
    clean_lines = []
    skip_section = False
    for line in lines:
        stripped = line.strip()
        if re.search(r'(sidebar|footer|nav|menu|cookie|advertisement)', stripped, re.I):
            skip_section = True
            continue
        if stripped == '':
            skip_section = False
        if not skip_section:
            clean_lines.append(line)

    text = '\n'.join(clean_lines)
    text = re.sub(r'\n{4,}', '\n\n\n', text)

    return text.strip()


def get_page_key(path):
    """Convert a URL path to a safe filename key."""
    key = path.strip('/').replace('/', '-')
    if not key:
        key = 'index'
    return key


def fetch_source(cfg):
    """Fetch all pages for a source."""
    name = cfg['name']
    base_url = cfg['homepage'].rstrip('/')
    base_url = re.sub(r'/docs$', '', base_url)

    human_dir = HUMAN_DIR / name
    human_dir.mkdir(parents=True, exist_ok=True)

    status = {
        "name": name,
        "last_run": datetime.utcnow().isoformat(),
        "pages_total": len(cfg.get('pages', [])),
        "pages_success": 0,
        "pages_failed": 0,
        "errors": [],
        "success": True
    }

    for page_cfg in cfg.get('pages', []):
        path = page_cfg['path']
        title = page_cfg.get('title', '')

        # Build URL
        if path == '' or path == '/':
            url = f"{base_url}/"
        elif path.startswith('/'):
            url = f"{base_url}{path}"
        else:
            url = f"{base_url}/{path}"

        page_key = get_page_key(path)
        filepath = human_dir / f"{page_key}.md"

        print(f"  Fetching: {title or page_key}...", end=" ", flush=True)
        content, error = fetch_page(url)

        if content:
            # Add frontmatter
            md = f"---\ntitle: {title}\nsource: {name}\nurl: {url}\nfetched: {datetime.utcnow().isoformat()}\n---\n\n# {title}\n\n{content}"
            filepath.write_text(md, encoding='utf-8')
            print(f"OK ({len(content)} chars)")
            status['pages_success'] += 1
        else:
            print(f"FAIL: {error}")
            status['pages_failed'] += 1
            status['errors'].append(f"{page_key}: {error}")
            status['success'] = False

        # Small delay between requests
        time.sleep(0.5)

    # Save status
    (STATUS_DIR / name).mkdir(parents=True, exist_ok=True)
    with open(STATUS_DIR / f"{name}.json", 'w') as f:
        json.dump(status, f, indent=2)

    # Create version snapshot
    if status['pages_success'] > 0:
        timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
        version_dir = VERSIONS_DIR / name / timestamp
        version_dir.mkdir(parents=True, exist_ok=True)

        # Copy all fetched pages to version dir
        for page_cfg in cfg.get('pages', []):
            path = page_cfg['path']
            page_key = get_page_key(path)
            src = human_dir / f"{page_key}.md"
            if src.exists():
                import shutil
                shutil.copy2(src, version_dir / f"{page_key}.md")

        print(f"  Version snapshot: {name}/{timestamp}")

    return status


def main():
    import yaml

    if len(sys.argv) < 2:
        print("Usage: python scripts/fetch.py <source.yaml> [source2.yaml ...]")
        print("       python scripts/fetch.py --all")
        sys.exit(1)

    if sys.argv[1] == '--all':
        source_files = sorted(SOURCES_DIR.glob('*.yaml'))
    else:
        source_files = [Path(s) for s in sys.argv[1:]]

    all_ok = True
    for sf in source_files:
        if not sf.exists():
            print(f"SKIP (not found): {sf}")
            continue
        cfg = yaml.safe_load(sf.read_text())
        if not cfg.get('pages'):
            print(f"SKIP (no pages configured): {cfg.get('name', sf.name)}")
            continue
        print(f"\n=== Fetching: {cfg['display']} ({cfg['name']}) ===")
        status = fetch_source(cfg)
        if not status['success']:
            all_ok = False

    print(f"\n{'All sources OK' if all_ok else 'Some sources had errors'}")
    sys.exit(0 if all_ok else 1)


if __name__ == '__main__':
    main()
