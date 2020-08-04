from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import viewsets


from books.models import Book, Todo
from post.models import Post
from happiness.models import HappyRecord
from .serializers import (
    BookSerializer,
    TodoSerializer,
    PostSerializer,
    UserSerializer,
    HappyRecordSerializer,
)
from .permission import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class HappyRecordViewSet(viewsets.ModelViewSet):
    queryset = HappyRecord.objects.all()
    serializer_class = HappyRecordSerializer


# class BookListAPIView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# class BookAPIView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# class TodoListAPIView(generics.ListAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer


# class TodoAPIView(generics.RetrieveAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer


# class PostListAPI(generics.ListCreateAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostAPI(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class UserList(generics.ListCreateAPIView):  # new
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):  # new
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
