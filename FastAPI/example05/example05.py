from fastapi import FastAPI

app = FastAPI()

@app.get("/cars/price")

async def cars_by_price(min_price: int = 0, max_price:int = 100000):

    if min_price < 0 | max_price > 100000: # max-min price validation
        return {"Message": "Error"}
    else:
        return {"Message": f"Listining cars with prices between {min_price} and {max_price}"}

