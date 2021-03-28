from .models import TestApi
from rest_framework import viewsets, permissions
from .serializers import TestApiSerializers


class TestApiViewSet(viewsets.ModelViewSet):
    queryset = TestApi.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TestApiSerializers
