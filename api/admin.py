from django.contrib import admin
from api.post.models import Post
from api.books.models import Book
from api.todo.models import Todo
from api.happiness.models import HappyRecord


# Register your models here.
admin.site.register([Post, Book, Todo, HappyRecord])
