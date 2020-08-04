from django.contrib import admin

# Register your models here.
from .models import HappyType, HappyRecord

admin.site.register([HappyType, HappyRecord])
