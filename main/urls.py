from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
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
urlpatterns += [
    path('admin_local/', admin.site.urls),
    path('local', include('local.urls')),
]
