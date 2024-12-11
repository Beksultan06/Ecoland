from modeltranslation.translator import register, TranslationOptions
from app.news.models import NewsListDetails, NewsPage

@register(NewsListDetails)
class NewsListDetailstranslation(TranslationOptions):
    fields = ("title", 'month', 'descriptions')

@register(NewsPage)
class NewsPageTranslation(TranslationOptions):
    fields = ("title", )