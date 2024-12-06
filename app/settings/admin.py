from django.contrib import admin
from app.settings.models import SettingsBanner, Settings, GalleryMainPage, MainTours, VideoMainPage, Partners,\
ImageMainPage, DopInfo, AboutPage, AboutPercent, TeamAboutPage, ContactPage, Form
from django.utils.html import mark_safe
# Register your models here.

def image_preview(obj, field_name):
    if getattr(obj, field_name):
        return mark_safe(f'<img src="{getattr(obj, field_name).url}" width="100" />')
    return 'Нет изображения'

image_preview.short_description = 'Фото'

@admin.register(SettingsBanner)
class SettingsBannerAdmin(admin.ModelAdmin):
    list_display = ("id", 'title', 'image_preview')

    def image_preview(self, obj):
        return image_preview(obj, 'image')

@admin.register(Settings)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image_preview')

    def image_preview(self, obj):
        return image_preview(obj, 'image_plan')

@admin.register(GalleryMainPage)
class GalleryMainPageAdmin(admin.ModelAdmin):
    list_display = ("id", 'title', 'image_preview')

    def image_preview(self, obj):
        return image_preview(obj, 'image')

@admin.register(MainTours)
class MainToursAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image_preview')

    def image_preview(self, obj):
        return image_preview(obj, 'image')

@admin.register(VideoMainPage)
class VideoMainPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'icon')

@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ("image_preview",)

    def image_preview(self, obj):
        return image_preview(obj, 'image')

@admin.register(ImageMainPage)
class ImageMainPage(admin.ModelAdmin):
    list_display = ("image_preview",)

    def image_preview(self, obj):
        return image_preview(obj, 'image')

@admin.register(DopInfo)
class DopInfoAdmin(admin.ModelAdmin):
    list_display = ("id", 'title')

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ("id", 'title', 'image_preview')

    def image_preview(self, obj):
        return image_preview(obj, 'image')

@admin.register(AboutPercent)
class AboutPercentAdmin(admin.ModelAdmin):
    list_display = ("id", 'title', 'procent')

@admin.register(TeamAboutPage)
class TeamAboutPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'job_title', 'image_preview')

    def image_preview(self, obj):
        return image_preview(obj, 'image')

@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image_preview')

    def image_preview(self, obj):
        return image_preview(obj, 'image')

@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ("id", 'name', 'email')