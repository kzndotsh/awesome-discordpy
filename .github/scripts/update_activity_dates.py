#!/usr/bin/env python3
"""Stamp last-activity dates onto GitHub, gist, and PyPI links in readme.md."""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

README_PATH = Path("readme.md")
CONTENT_START = "<!-- CONTENT -->"
CONTENT_END = "<!-- END CONTENT -->"
TIMEOUT_SECONDS = 20
MAX_WORKERS = 8
USER_AGENT = "awesome-discordpy-activity-bot"

ACTIVITY_SUFFIX = re.compile(r" \(last activity \d{4}-\d{2}\)\.?$")
LIST_ITEM = re.compile(
    r"^(?P<prefix>\s*-\s+\[[^\]]+\]\()(?P<url>https://[^)]+)(?P<mid>\)\s+-\s+)(?P<desc>.+)$"
)
GITHUB_REPO = re.compile(
    r"^https://github\.com/(?P<owner>[^/]+)/(?P<repo>[^/#?]+)(?:/.*)?$",
    re.IGNORECASE,
)
GIST = re.compile(
    r"^https://gist\.github\.com/(?:[^/]+/)?(?P<gist_id>[a-f0-9]+)(?:/.*)?$",
    re.IGNORECASE,
)
PYPI = re.compile(
    r"^https://pypi\.org/project/(?P<name>[^/#?]+)/?",
    re.IGNORECASE,
)

SKIP_REPOS = {"kzndotsh/awesome-discordpy"}


def github_headers() -> dict[str, str]:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": USER_AGENT,
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def http_json(url: str, headers: dict[str, str] | None = None) -> dict[str, object] | None:
    request = urllib.request.Request(
        url,
        headers=headers or {"User-Agent": USER_AGENT, "Accept": "application/json"},
        method="GET",
    )
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as exc:
        print(f"skip {url} ({exc.code})", file=sys.stderr)
        return None
    except urllib.error.URLError as exc:
        print(f"skip {url} ({exc.reason})", file=sys.stderr)
        return None


def month_from_iso(value: str) -> str:
    stamp = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if stamp.tzinfo is None:
        stamp = stamp.replace(tzinfo=timezone.utc)
    return stamp.strftime("%Y-%m")


def activity_for_url(url: str) -> str | None:
    gist = GIST.match(url)
    if gist:
        payload = http_json(
            f"https://api.github.com/gists/{gist.group('gist_id')}",
            github_headers(),
        )
        updated = payload.get("updated_at") if payload else None
        return month_from_iso(str(updated)) if isinstance(updated, str) else None

    pypi = PYPI.match(url)
    if pypi:
        payload = http_json(f"https://pypi.org/pypi/{pypi.group('name')}/json")
        if not payload:
            return None
        info = payload.get("info")
        urls = payload.get("urls")
        if isinstance(urls, list) and urls:
            upload_times = [
                item.get("upload_time_iso_8601")
                for item in urls
                if isinstance(item, dict)
            ]
            iso_times = [str(item) for item in upload_times if isinstance(item, str)]
            if iso_times:
                return month_from_iso(max(iso_times))
        if isinstance(info, dict):
            version = info.get("version")
            releases = payload.get("releases")
            if isinstance(version, str) and isinstance(releases, dict):
                files = releases.get(version)
                if isinstance(files, list) and files:
                    first = files[0]
                    if isinstance(first, dict) and isinstance(first.get("upload_time_iso_8601"), str):
                        return month_from_iso(str(first["upload_time_iso_8601"]))
        return None

    repo = GITHUB_REPO.match(url)
    if not repo:
        return None
    owner_repo = f"{repo.group('owner')}/{repo.group('repo')}"
    if owner_repo.lower() in SKIP_REPOS:
        return None
    payload = http_json(f"https://api.github.com/repos/{owner_repo}", github_headers())
    pushed = payload.get("pushed_at") if payload else None
    return month_from_iso(str(pushed)) if isinstance(pushed, str) else None


def apply_date(description: str, year_month: str) -> str:
    stripped = ACTIVITY_SUFFIX.sub("", description.rstrip())
    if stripped.endswith("."):
        stripped = stripped[:-1]
    return f"{stripped} (last activity {year_month})."


def unique_urls(block: str) -> list[str]:
    seen: set[str] = set()
    urls: list[str] = []
    for line in block.splitlines():
        match = LIST_ITEM.match(line)
        if not match:
            continue
        url = match.group("url")
        if url in seen:
            continue
        if GITHUB_REPO.match(url) or GIST.match(url) or PYPI.match(url):
            seen.add(url)
            urls.append(url)
    return urls


def rewrite_block(block: str, dates: dict[str, str]) -> str:
    lines: list[str] = []
    for line in block.splitlines():
        match = LIST_ITEM.match(line)
        if not match:
            lines.append(line)
            continue
        url = match.group("url")
        year_month = dates.get(url)
        if not year_month:
            lines.append(line)
            continue
        desc = apply_date(match.group("desc"), year_month)
        lines.append(f"{match.group('prefix')}{url}{match.group('mid')}{desc}")
    return "\n".join(lines)


def main() -> int:
    text = README_PATH.read_text(encoding="utf-8")
    start = text.find(CONTENT_START)
    end = text.find(CONTENT_END)
    if start == -1 or end == -1 or end < start:
        print("readme.md is missing CONTENT markers", file=sys.stderr)
        return 1

    start += len(CONTENT_START)
    block = text[start:end]
    urls = unique_urls(block)
    dates: dict[str, str] = {}
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {pool.submit(activity_for_url, url): url for url in urls}
        for future in as_completed(futures):
            url = futures[future]
            year_month = future.result()
            if year_month:
                dates[url] = year_month

    updated = rewrite_block(block, dates)
    README_PATH.write_text(
        f"{text[:start]}{updated}{text[end:]}",
        encoding="utf-8",
    )
    print(f"updated {len(dates)}/{len(urls)} links")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
