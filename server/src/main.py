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
    allow_methods=["GET"]
)


@app.get('/')
async def unshorten_url(url: Optional[str] = None):
    if url is None:
        return {"error": "no url provided"}

    domain = urlparse(url).netloc

    if domain in SHORTEN_DOMAINS:
        return {"result": "shortened url"}
    else:
        return {"error": f"cannot shorten {url}"}
