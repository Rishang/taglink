from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl, ValidationError
from metadataScraper import metadataparse
from typing import Optional

class url_link(BaseModel):
    url: HttpUrl

app = FastAPI()

@app.post("/")
async def scraper(url_link: url_link):
    url_metadata = metadataparse(url_link.url)
    data = url_metadata.metadata
    return data
