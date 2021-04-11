from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, ValidationError
from typing import Optional
import feed

class input(BaseModel):
    url: str

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["POST"],
)

@app.post("/get_feed")
async def rss_data(input: input):
    f = feed.parse(input.url)
    return f
