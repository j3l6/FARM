import shutil
from fastapi import FastAPI, Form, File, UploadFile

app = FastAPI()

@app.post("/upload")
async def upload(
    picture: UploadFile = File(...),
    brand: str = Form(...),
    model: str = Form(...)):
    with open ("saved_file.png", "wb") as buffer: #file-like object is asiggned to the variable buffer
        shutil.copyfileobj(picture.file, buffer)  #copy the original file into the variable buffer
        return {"brand": brand, "model": model, "file_name": picture.filename}
