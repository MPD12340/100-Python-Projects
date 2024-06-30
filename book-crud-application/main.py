from fastapi import FastAPI
from .src.books.api import book_router



app = FastAPI()

app.include_router(book_router, prefix="/api/v1")
