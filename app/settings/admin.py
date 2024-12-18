from django.contrib import admin
from django.utils.html import mark_safe
from modeltranslation.admin import TranslationAdmin
from app.settings.models import *

# Generic method for displaying image preview
def image_preview(obj, field_name='image'):
    """Generate an image preview for the admin."""
    if getattr(obj, field_name):
        return mark_safe(f'<img src="{getattr(obj, field_name).url}" width="100" />')
    return 'Нет изображения'

image_preview.short_description = 'Фото'

@admin.register(Settings)
class SettingsAdmin(TranslationAdmin):
    list_display = ("id", 'title', "image_preview")

    def image_preview(self, obj):
            return image_preview(obj, 'image')

@admin.register(SettingsBanner)
class SettingsBannerAdmin(TranslationAdmin):
     list_display = ("id", 'title', 'image_preview')

     def image_preview(self, obj):
            return image_preview(obj, 'image')

@admin.register(GalleryMainPage)
class GalleryMainPageAdmin(TranslationAdmin):
    list_display = ("id", 'title', 'image_preview')

    def image_preview(self, obj):
            return image_preview(obj, 'image')

@admin.register(VideoMainPage)
class VideoMainPageAdmin(TranslationAdmin):
      list_display = ("id", 'title')

admin.site.register(Partners)
admin.site.register(ImageMainPage)


@admin.register(DopInfo)
class DopInfoAdmin(TranslationAdmin):
    list_display = ("id", 'title')

@admin.register(AboutPage)
class AboutPageAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'image_preview')

    def image_preview(self, obj):
            return image_preview(obj, 'image')

@admin.register(TeamAboutPage)
class TeamAboutPageAdmin(TranslationAdmin):
      list_display = ("id", 'title')

@admin.register(AboutPercent)
class AboutPercentAdmin(admin.ModelAdmin):
    list_display = ("id", "title")

@admin.register(ContactPage)
class ContactPageAdmin(TranslationAdmin):
    list_display = ("id", 'title', 'image_preview')

    def image_preview(self, obj):
            return image_preview(obj, 'image')

@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ("id", 'name')