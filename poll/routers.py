from typing import List

from fastapi import APIRouter, Depends

from poll.adapters import retrieve_book, retrieve_books
from poll.models import Book as BookModel
from poll.schemas import BookSchema, BooksSchema, _BookSchema

books_router = APIRouter()


@books_router.get("/", response_model=BooksSchema)
def get_books(
    books: List[BookModel] = Depends(retrieve_books),
) -> BooksSchema:
    return BooksSchema.from_queryset(books)


@books_router.get("/{q_id}", response_model=BookSchema)
def get_book(
    book: BookModel = Depends(retrieve_book),
) -> BookSchema:
    return BookSchema.from_orm(book)


@books_router.post("/", status_code=201, response_model=BookSchema)
def post_book(
    book: _BookSchema,
) -> BookSchema:
    b = BookModel.from_api(book)
    b.save()
    return BookSchema.from_orm(b)
