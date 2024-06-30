from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from .schemas import BookModel , ResponseModel
from .data import books
from helpers import custom_response


book_router = APIRouter()
@book_router.get("/books", response_model=ResponseModel)
async def get_all_books():
    return custom_response(success=True, data=books)


@book_router.get("/books/{book_id}")
async def get_book_by_id(book_id: str):
    for book in books:
        if book["id"] == book_id:
            return custom_response(success=True, data=book)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@book_router.post("/books")
async def create_a_book(book_data: BookModel):
    new_book = book_data.model_dump()
    try:
        books.append(new_book)
        return custom_response(success=True, data=new_book)
    except Exception as e:
        print(e)


@book_router.patch("/books/{book_id}")
async def update_a_book(book_id: str, book_data: BookModel):
    print(book_id)
    for book in books:
        if book["id"] == book_id:
            book.update(book_data.model_dump())
            return custom_response(success=True, data=book)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@book_router.delete("/books/{book_id}")
async def delete_a_book(book_id: str):
    for i, book in enumerate(books):
        if book["id"] == book_id:
            book_to_delete = books.pop(i)
            return custom_response(success=True, data=book_to_delete)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")