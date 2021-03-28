from rest_framework import serializers
from .models import TestApi


class TestApiSerializers(serializers.ModelSerializer):
    class Meta:
        model = TestApi
        fields = '__all__'
