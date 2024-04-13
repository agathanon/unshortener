import re
import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from urllib.parse import urlparse

SHORTEN_DOMAINS = [
    't.co'
]

app = FastAPI(docs_url=None, redoc_url=None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"]
)


def unshorten_url(url: str):
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


@app.get('/')
async def receive_url(url: Optional[str] = None):
    if url is None:
        return {"error": "no url provided"}

    domain = urlparse(url).netloc

    if domain not in SHORTEN_DOMAINS:
        return {"error": f"cannot shorten {url}"}

    unshortened = unshorten_url(url)

    return {"result": unshortened}
