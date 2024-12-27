from django.contrib import admin
from app.tour.models import Tour, Settings
from django.utils.html import mark_safe
from modeltranslation.admin import TranslationAdmin

# Register your models here.

def image_preview(obj, field_name='image'):
    """Generate an image preview for the admin."""
    if getattr(obj, field_name):
        return mark_safe(f'<img src="{getattr(obj, field_name).url}" width="100" />')
    return 'Нет изображения'

@admin.register(Tour)
class TourAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'image_preview']

    def image_preview(self, obj):
            return image_preview(obj, 'image')

@admin.register(Settings)
class SettingsAdmin(TranslationAdmin):
    list_display = ['id', "title", "image_preview"]
    search_fields = ['title']

    def image_preview(self, obj):
            return image_preview(obj, 'image')