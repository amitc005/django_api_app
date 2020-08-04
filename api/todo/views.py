from rest_framework import viewsets

from .models import Todo
from api.serializers import TodoSerializer
from api.permission import IsAuthorOrReadOnly


class TodoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
