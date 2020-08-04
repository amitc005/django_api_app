from django.test import TestCase

# Create your tests here.
from .models import Book


class BookModalTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Book.objects.create(
            title="Harry Potter",
            subtitle="The Scocers stone",
            author="J.K Rollowing",
            isbn="TEST_ISBD",
        )

    def test_book_model(self):
        book = Book.objects.get(id=1)
        assert book.title == "Harry Potter"
        assert book.subtitle == "The Scocers stone"
        assert book.author == "J.K Rollowing"
        assert book.isbn == "TEST_ISBD"
