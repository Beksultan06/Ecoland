from modeltranslation.translator import register, TranslationOptions
from app.destinations.models import DestinationsDetailModels, DestinationsModels, DestinationsPynkt

@register(DestinationsModels)
class DestinationsModelsTranslation(TranslationOptions):
    fields = ('title', 'descriptions')

@register(DestinationsDetailModels)
class DestinationsDetailModelsTranslation(TranslationOptions):
    fields = ('title',)

@register(DestinationsPynkt)
class DestinationsPynktTranslation(TranslationOptions):
    fields = ("title", "descriptions")