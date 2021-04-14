from rest_framework import serializers
from .models import TestApi, TestUserApi


class TestApiSerializers(serializers.ModelSerializer):
    class Meta:
        model = TestApi
        fields = '__all__'


class TestUserApiSerializers(serializers.ModelSerializer):
    class Meta:
        model = TestUserApi
        fields = '__all__'
