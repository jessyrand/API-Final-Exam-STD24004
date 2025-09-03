from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse

app = FastAPI()


class Characteristic:
    max_speed: int
    max_fuel_capacity: int

class Cars(BaseModel):
    id: str
    brand: str
    model: str
    max_speed: int
    max_fuel_capacity: int

cars_stored : List[Cars] = []

@app.get("/ping")
def ping():
    return {"pong"}

@app.post("/cars")
def create_cars(cars_payload: List[Cars]):
    cars_stored.extend(cars_payload)
    return JSONResponse(content=serialize_cars(), status_code=201, media_type="application/json")

def serialize_cars():
    serialized_cars = []
    for car in cars_stored:
        serialized_cars.append(car.model_dump())
    return serialized_cars

@app.get("/cars")
def get_cars():
    return JSONResponse(content=serialize_cars(), status_code=200, media_type="application/json")

@app.get("/cars/{id}")
def get_car(id: str):
    for car in cars_stored:
        if car.id == id:
            return JSONResponse(content=car.model_dump(), status_code=200, media_type="application/json")
    return JSONResponse(content="Car not found", status_code=404, media_type="text/plain")