from django.contrib import admin

# Register your models here.
from .models import Book, Todo

admin.site.register(Book)
admin.site.register(Todo)
