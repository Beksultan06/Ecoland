from django.contrib import admin
from app.destinations.models import DestinationsModels
from django.utils.html import mark_safe

# Register your models here.

def image_preview(obj, field_name):
    if getattr(obj, field_name):
        return mark_safe(f'<img src="{getattr(obj, field_name).url}" width="100" />')
    return 'Нет изображения'

image_preview.short_description = 'Фото'

@admin.register(DestinationsModels)
class DestinationsModelsAdmin(admin.ModelAdmin):
    list_display = ("title", 'image_preview')

    def image_preview(self, obj):
        return image_preview(obj, 'image')