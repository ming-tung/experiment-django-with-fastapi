from fastapi import HTTPException, Path

from poll.models import Book


def retrieve_object(model_class, id: int):
    instance = model_class.objects.filter(pk=id).first()
    if not instance:
        raise HTTPException(status_code=404, detail="Object not found.")
    return instance


def retrieve_book(
    q_id: int = Path(..., description="get book from db")
) -> Book:
    return retrieve_object(Book, q_id)


def retrieve_books():
    return Book.objects.all()
