from typing import List

from fastapi import APIRouter, Depends

from poll.adapters import retrieve_book, retrieve_books
from poll.models import Book
from poll.schemas import FastBook, FastBooks

books_router = APIRouter()


@books_router.get("/", response_model=FastBooks)
def get_books(
    books: List[Book] = Depends(retrieve_books),
) -> FastBooks:
    return FastBooks.from_queryset(books)


@books_router.get("/{q_id}", response_model=FastBook)
def get_book(
    book: Book = Depends(retrieve_book),
) -> FastBook:
    return FastBook.from_orm(book)
