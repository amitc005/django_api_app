from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class HappyType(models.Model):
    happy_type = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description


class HappyRecord(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    happy_level = models.ForeignKey(HappyType, on_delete=models.DO_NOTHING, default="1")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author.__str__()} is {self.happy_level.description}"
