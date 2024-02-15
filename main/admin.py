from django.contrib import admin

from .models import Article, ImageArticle


class ArticleAdmin(admin.ModelAdmin):
    list_editable = ['is_published']
    list_display = ['title', 'is_published']
    list_filter = ['is_published']

admin.site.register(Article, ArticleAdmin)
admin.site.register(ImageArticle)
