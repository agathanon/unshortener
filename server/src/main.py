"""Unshorten API"""
from typing import Optional
from urllib.parse import urlparse
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from unshorteners import unshorten_twitter, unshorten_tinyurl

UNSHORTEN = {
    't.co': unshorten_twitter,
    'tinyurl.com': unshorten_tinyurl
}

CACHE = {}

app = FastAPI(docs_url=None, redoc_url=None)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"]
)


@app.get('/')
async def receive_url(url: Optional[str] = None):
    """Receives a URL to unshorten"""
    if url is None:
        return {"error": "no url provided"}

    domain = urlparse(url).netloc
    if domain not in UNSHORTEN:
        return {"error": f"cannot unshorten {domain}"}

    if url in CACHE:
        return CACHE[url]

    result = UNSHORTEN[domain](url)
    if result:
        CACHE[url] = result
        return result

    return {"error": f"server error"}
