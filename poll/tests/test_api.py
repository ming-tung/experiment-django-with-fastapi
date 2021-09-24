import pytest

from fastapi.testclient import TestClient

from mysite.asgi import fastapp
from poll.models import Book

client = TestClient(fastapp)


@pytest.fixture
def book():
    return Book.objects.create(title='asdf')


@pytest.mark.django_db
def test_api_books_no_data():
    response = client.get("/api/books")
    assert response.status_code == 200
    assert response.json()['items'] == []


@pytest.mark.django_db
def test_api_books(book):
    response = client.get("/api/books")
    assert response.status_code == 200
    assert response.json()['items'] == [book]
