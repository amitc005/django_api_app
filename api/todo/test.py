from django.test import TestCase

# Create your tests here.
from .models import Todo


class TodoModalTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title="first todo", body="a body here")

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f"{todo.title}"
        assert expected_object_name == "first todo"

    def test_body_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f"{todo.body}"
        assert expected_object_name == "a body here"
