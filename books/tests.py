from django.test import TestCase

# Create your tests here.
from .models import Book, Todo


class TodoModalTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title="first todo", body="a body here")

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f"{todo.title}"
        self.assertEquals(expected_object_name, "first todo")

    def test_body_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f"{todo.body}"
        self.assertEquals(expected_object_name, "a body here")


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
        self.assertEquals(book.title, "Harry Potter")
        self.assertEquals(book.subtitle, "The Scocers stone")
        self.assertEquals(book.author, "J.K Rollowing")
        self.assertEquals(book.isbn, "TEST_ISBD")
