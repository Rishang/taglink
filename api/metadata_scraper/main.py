from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl, ValidationError
from fastapi.middleware.cors import CORSMiddleware
from metadataScraper import metadataparse
from typing import Optional

class url_link(BaseModel):
    url: HttpUrl

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/get_metadata/")
async def scraper(url_link: url_link):
    url_metadata = metadataparse(url_link.url)
    data = url_metadata.metadata
    return data
