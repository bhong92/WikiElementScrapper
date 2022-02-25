from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from pydantic import BaseModel

from scrapper import findElement, getJSON

app = FastAPI()

class Data(BaseModel):
    name: str

@app.post("/api/chem-wiki", response_class=ORJSONResponse)
async def information(element: Data):
    return (getJSON(element.name))