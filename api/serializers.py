from rest_framework import serializers
from books.models import Book, Todo
from post.models import Post
from happiness.models import HappyRecord
from django.contrib.auth import get_user_model


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("title", "subtitle", "author", "isbn")


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("title", "body", "id")


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("author", "title", "body", "created_at", "updated_at")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "username")


# class HappyRecordSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField(required=False, allow_blank=True, max_length=100)


class HappyRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HappyRecord
        fields = ("author", "happy_level", "id", "created_at", "updated_at")

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        happy_level = validated_data["happy_level"]

        return HappyRecord.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.happy_level = validated_data.get("happy_level", instance.happy_level)
        instance.save()
        return instance
