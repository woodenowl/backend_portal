from rest_framework import routers
from .api import TestApiViewSet


routers = routers.DefaultRouter()
routers.register('api/test_api', TestApiViewSet, 'test')


urlpatterns = routers.urls
