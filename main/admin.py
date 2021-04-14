from django.contrib import admin
from .models import TestApi, TestUserApi


class TestApiAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'check')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'date', 'check')
    list_editable = ('check',)
    list_filter = ('check',)


class TestUserApiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'password',)
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'password',)


admin.site.register(TestApi, TestApiAdmin)
admin.site.register(TestUserApi, TestUserApiAdmin)
