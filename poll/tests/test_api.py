import pytest
from fastapi.testclient import TestClient

from mysite.asgi import fastapp
from poll.models import Book

client = TestClient(fastapp)


@pytest.fixture
def book():
    return Book.objects.create(title='asdf')


@pytest.mark.django_db
def test_api_book(book):
    response = client.get(f"/api/books/{book.id}")

    assert response.status_code == 200
    assert response.json() == {"title": book.title}


@pytest.mark.django_db
def test_api_books(book):
    assert Book.objects.count() == 1

    response = client.get("/api/books")

    assert response.status_code == 200
    assert response.json()['items'] == [book]
