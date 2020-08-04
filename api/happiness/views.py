from rest_framework import viewsets

from .models import HappyRecord
from api.serializers import HappyRecordSerializer


class HappyRecordViewSet(viewsets.ModelViewSet):
    queryset = HappyRecord.objects.all()
    serializer_class = HappyRecordSerializer
