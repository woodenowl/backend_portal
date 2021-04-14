from rest_framework import routers
from .api import TestApiViewSet, TestUserApiViewSet


routers = routers.DefaultRouter()

routers.register(
    'api/test_api',
    TestApiViewSet,
    'test'
)

routers.register(
    'api/test_user_api',
    TestUserApiViewSet,
    'test_user'
)

urlpatterns = routers.urls
