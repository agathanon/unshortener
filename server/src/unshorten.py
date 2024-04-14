import re
import requests


def unshorten_twitter(url):
    pattern = re.compile(r"<title>(.*?)<\/title>")

    response = requests.get(
        url=url,
        headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0"}
    )

    match = pattern.search(response.text)
    if match:
        return match.group(1)
    else:
        return None
