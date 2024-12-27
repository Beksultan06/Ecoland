from modeltranslation.translator import register, TranslationOptions
from app.tour.models import Tour, Settings

@register(Tour)
class TourTranslations(TranslationOptions):
    fields = (
        "title", "person"
    )

@register(Settings)
class SettingsTranslations(TranslationOptions):
    fields = (
        "title", "main", "tour"
    )