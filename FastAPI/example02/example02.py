from fastapi import FastAPI

app = FastAPI()
@app.get("/car/{id}")
async def root(id):
    return {"car_id":id}


@app.get("/books/{book_id}")
async def read_books(book_id:int):
    return {
        "book_id": book_id,
        "title": "Alice´s Adventures in Worderland",
        "author": "Lewis Carroll"
    }

@app.get("/authors/{author_id}")
async def read_author(author_id:int):
    return {
        "author_id": author_id,
        "author": "Lewis Carroll"
    }


@app.get("/books2")             #books2?genere=action&year=2025
async def read_books(year: int = None):
    if year:
        return {
            "year": year,
            "books": ["Book 1", "Book 2"]
        }
    return {"books":["All Books"]} #if there is no year in the link, it returns "All book"






    