from rest_framework import viewsets

from .models import Post
from api.serializers import PostSerializer
from api.permission import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
