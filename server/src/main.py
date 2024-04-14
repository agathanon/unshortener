from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from urllib.parse import urlparse
from unshorten import unshorten_twitter

UNSHORTENERS = {
    't.co': unshorten_twitter
}

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
    if url is None:
        return {"error": "no url provided"}

    domain = urlparse(url).netloc

    if domain not in UNSHORTENERS:
        return {"error": f"cannot unshorten {domain}"}
    else:
        return UNSHORTENERS[domain](url)
