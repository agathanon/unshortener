"""Unshortening functions"""
import re
from typing import Optional
import requests


def unshorten_tinyurl(url: str) -> Optional[str]:
    """Retrieve the actual URL behind a TinyURL."""
    try:
        response = requests.get(url, timeout=4, allow_redirects=False)
    except requests.RequestException:
        return None

    if response.status_code == 301:
        return response.headers.get("location", None)

    return None


def unshorten_twitter(url: str) -> Optional[str]:
    """Retrieve the actual URL behind a Twitter URL."""
    pattern = re.compile(r"<title>(.*?)<\/title>")

    try:
        response = requests.get(
            url=url,
            headers={
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0"
            },
            timeout=4
        )
    except requests.RequestException:
        return None

    match = pattern.search(response.text)
    if match:
        return match.group(1)

    return None
