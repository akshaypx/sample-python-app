from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    repo: str
    # description: Optional[str] = None
    # price: float
    # tax: Optional[float] = None

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/repo/")
async def create_item(item: Item):
    return item