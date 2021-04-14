from .models import TestApi, TestUserApi
from rest_framework import viewsets, permissions
from .serializers import TestApiSerializers, TestUserApiSerializers


class TestApiViewSet(viewsets.ModelViewSet):
    queryset = TestApi.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TestApiSerializers


class TestUserApiViewSet(viewsets.ModelViewSet):
    queryset = TestUserApi.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TestUserApiSerializers
