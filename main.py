from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}