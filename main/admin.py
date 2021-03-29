from django.contrib import admin
from .models import TestApi


class TestApiAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'check')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'date', 'check')
    list_editable = ('check',)
    list_filter = ('check',)


admin.site.register(TestApi, TestApiAdmin)