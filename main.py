from fastapi import FastAPI
from fastapi.responses import UJSONResponse

from scrapper import findElement, getJSON

app = FastAPI()

@app.post("/api/plot", response_class=UJSONResponse)
async def information(element: str):
    return (getJSON(element))