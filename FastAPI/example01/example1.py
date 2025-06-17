from fastapi import FastAPI

app = FastAPI() #application instance

@app.get("/")  #defining route using a decorator, get reques at the path /
async def root():  #function designed to work asynchronously
    return{"message":"Hello FastAPI"} #returns dictionary, auto-conversion to JSON by FastAPI

@app.post("/")
async def post_root():
    return{"message":"Post request success!"}

