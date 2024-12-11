from django.contrib import admin
from django.utils.html import mark_safe
from app.news.models import NewsPage, NewsListDetails, NewsComment
from modeltranslation.admin import TranslationAdmin

# Register your models here.
def image_preview(obj, field_name):
    if getattr(obj, field_name):
        return mark_safe(f'<img src="{getattr(obj, field_name).url}" width="100" />')
    return 'Нет изображения'

image_preview.short_description = 'Фото'

@admin.register(NewsPage)
class NewsPageAdmin(TranslationAdmin):
    list_display = ("id", 'title', 'image_preview')

    def image_preview(self, obj):
        return image_preview(obj, 'image')

@admin.register(NewsListDetails)
class NewsListDetailsAdmin(TranslationAdmin):
    list_display = ("id", "title", 'image_preview')

    def image_preview(self, obj):
        return image_preview(obj, 'image')

@admin.register(NewsComment)
class NewsCommentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email")