from fastapi import FastAPI, Body
from pydantic import BaseModel


class InsertCar(BaseModel):
    brand: str
    model: str
    year: int

app = FastAPI()


@app.post("/cars")
async def new_car(data: InsertCar):

    print(data)
    return {"message": data}


class UserModel(BaseModel):
    username: str
    name: str

@app.post("/car/user")
async def new_car_model(car: InsertCar, user: UserModel, code: int = Body(None)):
    return {"car": car, "user": user, "code": code}

#test: http POST http://localhost:8000/car/user \
#  car:='{"brand": "Honda", "model": "Civic", "year": 2022}' \
#  user:='{"username": "jdoe", "name": "John Doe"}' \
#  code:=1234


