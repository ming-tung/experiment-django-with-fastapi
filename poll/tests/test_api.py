import pytest
from fastapi.testclient import TestClient

from mysite.asgi import fastapp
from poll.models import Book

client = TestClient(fastapp)


@pytest.fixture
def book():
    return Book.objects.create(title='asdf')


@pytest.mark.django_db(transaction=True)
class TestBookAPI:
    def test_api_book(self, book):
        response = client.get(f"/api/books/{book.id}")

        assert response.status_code == 200
        assert response.json() == {
            'title': 'asdf',
            'uuid': str(book.uuid),
            'created_at': book.created_at.isoformat(),
            'updated_at': book.updated_at.isoformat(),
        }

    def test_api_books(self, book):
        assert Book.objects.count() == 1

        response = client.get("/api/books")

        assert response.status_code == 200
        assert response.json()['items'] == [
            {
                'title': 'asdf',
                'uuid': str(book.uuid),
                'created_at': book.created_at.isoformat(),
                'updated_at': book.updated_at.isoformat(),
            }
        ]
