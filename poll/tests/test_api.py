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
    url = '/api/books/'

    def test_get_book(self, book):
        response = client.get(f"{self.url}{book.id}")

        assert response.status_code == 200
        assert response.json() == {
            'title': 'asdf',
            'uuid': str(book.uuid),
            'created_at': book.created_at.isoformat(),
            'updated_at': book.updated_at.isoformat(),
        }

    def test_get_books(self, book):
        assert Book.objects.count() == 1

        response = client.get(self.url)

        assert response.status_code == 200
        assert response.json()['items'] == [
            {
                'title': 'asdf',
                'uuid': str(book.uuid),
                'created_at': book.created_at.isoformat(),
                'updated_at': book.updated_at.isoformat(),
            }
        ]

    def test_post_book(self):
        response = client.post(
            self.url,
            json={'title': 'qwer'},
        )

        assert response.status_code == 201
        book = Book.objects.get(title='qwer')
        assert response.json() == {
            'title': 'qwer',
            'uuid': str(book.uuid),
            'created_at': book.created_at.isoformat(),
            'updated_at': book.updated_at.isoformat(),
        }
