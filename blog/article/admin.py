from django.contrib import admin
from . import models

@admin.register(models.Artile)
class ArticleAdmin (admin.ModelAdmin):
    list_display = ['title', 'text', 'date']


