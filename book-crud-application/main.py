from fastapi import FastAPI, Request, status
from pydantic import BaseModel
from fastapi.exceptions import HTTPException
import logging
from typing import List, Union, Any, Dict


app = FastAPI()


class ResponseModel(BaseModel):
    success: bool
    data: Union[Dict[str, Any], List[Any], None] = None
    error: Union[str, None] = None


def custom_response(
    success: bool,
    data: Union[Dict[str, Any], List[Any], None] = None,
    error: Union[str, None] = None,
):
    return ResponseModel(success=success, data=data, error=error)


books = [
    {
        "id": "9781593275846",
        "title": "Eloquent JavaScript, 3rd Edition",
        "pageCount": 472,
        "price": "$39.95",
        "publication": "No Starch Press",
    },
    {
        "id": "9780132350884",
        "title": "Clean Code: A Handbook of Agile Software Craftsmanship",
        "pageCount": 464,
        "price": "$49.99",
        "publication": "Prentice Hall",
    },
    {
        "id": "9780596009205",
        "title": "Head First Design Patterns",
        "pageCount": 694,
        "price": "$59.99",
        "publication": "O'Reilly Media",
    },
    {
        "id": "9780132350884",
        "title": "Clean Code: A Handbook of Agile Software Craftsmanship",
        "pageCount": 464,
        "price": "$49.99",
        "publication": "Prentice Hall",
    },
    {
        "id": "9781492041259",
        "title": "Python Crash Course, 2nd Edition",
        "pageCount": 544,
        "price": "$39.99",
        "publication": "No Starch Press",
    },
]


class BookModel(BaseModel):
    id: str
    title: str
    pageCount: int | None = None
    price: str
    publication: str


@app.get("/books", response_model=ResponseModel)
async def get_all_books():
    return custom_response(success=True, data=books)


@app.get("/books/{book_id}")
async def get_book_by_id(book_id: str):
    for book in books:
        if book["id"] == book_id:
            return custom_response(success=True, data=book)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@app.post("/books")
async def create_a_book(book_data: BookModel):
    new_book = book_data.model_dump()
    try:
        books.append(new_book)
        return custom_response(success=True, data=new_book)
    except Exception as e:
        print(e)


@app.patch("/books/{book_id}")
async def update_a_book(book_id: str, book_data: BookModel):
    print(book_id)
    for book in books:
        if book["id"] == book_id:
            book.update(book_data.model_dump())
            return custom_response(success=True, data=book)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@app.delete("/books/{book_id}")
async def delete_a_book(book_id: str):
    for i, book in enumerate(books):
        if book["id"] == book_id:
            book_to_delete = books.pop(i)
            return custom_response(success=True, data=book_to_delete)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
