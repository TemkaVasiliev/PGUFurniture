from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_at")  # Добавляем автора

admin.site.register(Article, ArticleAdmin)
